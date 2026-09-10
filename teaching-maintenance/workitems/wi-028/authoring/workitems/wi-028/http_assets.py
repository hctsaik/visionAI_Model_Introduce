import json,hashlib,requests
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
W=Path(__file__).resolve().parent;C=W.parents[1]
paths=sorted(set(r['image'] for p in W.glob('*-active-assets.json') for r in json.loads(p.read_text(encoding='utf-8'))));assert len(paths)==36
def check(pair):
 prefix,path=pair;r=requests.get('http://127.0.0.1:8000/'+prefix+path,timeout=30);r.raise_for_status();h=hashlib.sha256(r.content).hexdigest();assert h==hashlib.sha256((C/path).read_bytes()).hexdigest();return {'route':prefix+path,'status':r.status_code,'sha256':h}
with ThreadPoolExecutor(max_workers=4) as pool:rows=list(pool.map(check,[(prefix,p) for prefix in ['', 'docs/'] for p in paths]))
(W/'http-assets.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8');print('PASS',len(rows),'HTTP/hash checks')

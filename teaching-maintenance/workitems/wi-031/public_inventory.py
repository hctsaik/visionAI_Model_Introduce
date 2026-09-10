import json,hashlib,threading
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests
W=Path(__file__).resolve().parent;C=W.parents[1];base='https://hctsaik.github.io/visionAI_Model_Introduce/'
norm=lambda b:b.replace(b'\r\n',b'\n')
r=requests.get(base,timeout=60);r.raise_for_status();same=norm(r.content)==norm((C/'docs/index.html').read_bytes())
assert same,'Published HTML differs from review baseline'
items=json.loads((W/'assets.json').read_text(encoding='utf-8'));local=threading.local()
def check(a):
 if not hasattr(local,'session'):local.session=requests.Session()
 try:
  r=local.session.head(base+a['path'],timeout=30,allow_redirects=True)
  return {'path':a['path'],'status':r.status_code,'method':'HEAD','content_type':r.headers.get('Content-Type')}
 except requests.RequestException as e:return {'path':a['path'],'error':str(e)}
with ThreadPoolExecutor(max_workers=12) as pool:rows=list(pool.map(check,items))
(W/'public-inventory.json').write_text(json.dumps({'html_matches':same,'normalized_html_sha256':hashlib.sha256(norm(r.content)).hexdigest(),'assets':rows,'scope':'HEAD verifies availability only, not image hash or visual correctness'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Public HTML identical;',len(rows),'active image paths;',sum(x.get('status')==200 for x in rows),'HTTP 200;',sum(x.get('status')!=200 for x in rows),'exceptions')

import hashlib,json,re
from pathlib import Path
import requests
W=Path(__file__).resolve().parent;C=W.parents[1]
d=json.loads(re.search(r'<script id="course-data" type="application/json">(.*?)</script>',(C/'docs/index.html').read_text(encoding='utf-8'),re.S)[1])
slugs=json.loads((W/'lesson-content.json').read_text(encoding='utf-8'))
rows=[]
for t in d['topics']:
 if t['id'] not in slugs:continue
 for k in ['modelPath','manifestPath']:
  p=t[k];r=requests.get('http://127.0.0.1:8000/docs/'+p,timeout=15);r.raise_for_status()
  assert r.content==(C/p).read_bytes(),p
  rows.append({'topic':t['id'],'path':p,'status':r.status_code,'sha256':hashlib.sha256(r.content).hexdigest()})
(W/'handoff-http.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('PASS',len(rows),'handoff document HTTP/hash checks')

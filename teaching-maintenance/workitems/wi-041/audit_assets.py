from pathlib import Path
import re,json,hashlib,urllib.request,urllib.error,importlib.util,concurrent.futures,time
W=Path(__file__).resolve().parent;C=W.parents[1];BASE='https://hctsaik.github.io/visionAI_Model_Introduce/'
html=(C/'docs/index.html').read_bytes();public=urllib.request.urlopen(BASE,timeout=30).read()
data=json.loads(re.search(rb'<script id="course-data" type="application/json">(.*?)</script>',html,re.S)[1])
spec=importlib.util.spec_from_file_location('bundle_audit',C/'tools/build_github_pages_site.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
assets=mod.referenced_assets(html.decode('utf8'));local=[]
for rel in assets:
 a=C/rel;b=C/'docs'/rel
 local.append({'path':rel.as_posix(),'source_exists':a.is_file(),'docs_exists':b.is_file(),'equal':a.is_file() and b.is_file() and hashlib.sha256(a.read_bytes()).digest()==hashlib.sha256(b.read_bytes()).digest()})
def check(url):
 try:
  req=urllib.request.Request(url,method='HEAD',headers={'User-Agent':'Mozilla/5.0'})
  with urllib.request.urlopen(req,timeout=15) as r:return {'url':url,'status':r.status,'final_url':r.url,'content_type':r.headers.get('Content-Type','')}
 except urllib.error.HTTPError as e:return {'url':url,'status':e.code,'error':str(e)}
 except Exception as e:return {'url':url,'status':None,'error':str(e)}
def walk(v):
 if isinstance(v,dict):
  for x in v.values():yield from walk(x)
 elif isinstance(v,list):
  for x in v:yield from walk(x)
 elif isinstance(v,str) and v.startswith(('https://','http://')):yield v
external=sorted(set(walk(data)));runs={}
for group,urls in [('public_assets',[BASE+urllib.parse.quote(r.as_posix(),safe='/') for r in assets]),('external_sources',external)]:
 rows=[]
 with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
  for f in concurrent.futures.as_completed([pool.submit(check,u) for u in urls]):
   rows.append(f.result())
   if len(rows)%100==0:print(group,len(rows),'/',len(urls),flush=True)
 rows.sort(key=lambda r:r['url']);runs[group]=rows
 (W/f'{group}.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
 print(group,'finished',len(rows),'non2xx',sum(not(r['status'] and 200<=r['status']<300) for r in rows),flush=True)
result={'public_html_sha256':hashlib.sha256(public).hexdigest(),'local_html_sha256':hashlib.sha256(html).hexdigest(),'public_equals_local':public==html,'source_docs_equal':html==(C/'interactive-learning.html').read_bytes(),'assets':local,'counts':{k:len(v) for k,v in runs.items()},'failures':{k:[r for r in v if not(r['status'] and 200<=r['status']<300)] for k,v in runs.items()}}
(W/'asset-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8');print('Complete',json.dumps({'equal':result['public_equals_local'],'local_asset_failures':sum(not r['equal'] for r in local),'counts':result['counts']},ensure_ascii=False),flush=True)

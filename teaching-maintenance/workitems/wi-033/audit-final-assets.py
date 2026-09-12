from pathlib import Path
import json,hashlib,sys
W=Path(__file__).resolve().parent;C=W.parents[1];sys.path.insert(0,str(C/'tools'))
from build_github_pages_site import referenced_assets
assets=referenced_assets((C/'interactive-learning.html').read_text(encoding='utf8'))
reviews={}
for p in W.glob('*assessment.json'):
 a=json.loads(p.read_text(encoding='utf8'))
 if isinstance(a,list):
  for r in a:
   if isinstance(r,dict) and 'image' in r and 'sha256' in r:reviews.setdefault(r['sha256'],[]).append((p.name,r))
selected=[]
for rel in assets:
 rel=Path(rel).as_posix()
 if Path(rel).suffix.lower()!='.png' or 'wi033-' not in Path(rel).name.lower():continue
 sha=hashlib.sha256((C/rel).read_bytes()).hexdigest();assert sha==hashlib.sha256((C/'docs'/rel).read_bytes()).hexdigest()
 assert sha in reviews,rel
 options=[(p,r) for p,r in reviews[sha] if r.get('native_review')=='passed' and r.get('total',0)>90 and not r.get('veto')]
 assert options,rel
 p,r=options[-1];assert sum(r['scores'])==r['total'];assert all(x[0]>=8 for x in r['completion'].values()),rel
 selected.append(dict(path=rel,sha256=sha,assessment=p,total=r['total'],native_source=r['image']))
assert sum('images/final/WI033-' in x['path'] for x in selected)==416
out=dict(status='passed',active_pngs=len(selected),engineering_pngs=416,other_pngs=len(selected)-416,min_score=min(r['total'] for r in selected),max_score=max(r['total'] for r in selected),assets=selected,user_approval='pending',model_inference=False)
(W/'final-selected-assets.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8')
print({k:v for k,v in out.items() if k!='assets'})

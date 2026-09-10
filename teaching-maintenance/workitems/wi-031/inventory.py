import hashlib,json,re,subprocess
from pathlib import Path
from collections import Counter
W=Path(__file__).resolve().parent; C=W.parents[1];R=C.parents[1]
html=(C/'docs/index.html').read_text(encoding='utf-8')
data=next(json.loads(x) for x in re.findall(r'<script[^>]*>(.*?)</script>',html,re.S) if x.lstrip().startswith('{') and 'topics' in x)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rows=[]; assets={}
def add(path,slug,layer):
 if not path:return
 p=C/path
 if not p.is_file():return
 a=assets.setdefault(path,{'path':path,'sha256':sha(p),'uses':[]})
 a['uses'].append({'topic':slug,'layer':layer})
for t in data['topics']:
 slug=t['id'];s=t['teachingStory'];v=s['beginner_path']['visuals'];first=[]
 for i,x in enumerate(v):
  views=x.get('reading_views') or [{'image':x.get('image')}]
  for j,view in enumerate(views):
   for k in ['image','mobile_image']:
    p=view.get(k)
    if p:add(p,slug,f'first-{i+1}-{j+1}-{k}');first.append(p)
 for x in t['slides']:add(x['image'],slug,'engineering-'+str(x['index']))
 def deepwalk(x):
  if isinstance(x,dict):
   for k,v in x.items():
    if k in ['image','mobile_image'] and isinstance(v,str):add(v,slug,'deep')
    else:deepwalk(v)
  elif isinstance(x,list):
   for v in x:deepwalk(v)
 deepwalk(s.get('deep_dive',{}))
 rows.append({'id':slug,'model':t['model'],'family':t['family'],'visuals':len(v),'first_paths':list(dict.fromkeys(first)),'engineering':[x['image'] for x in t['slides']],'deep_chapters':len(s.get('deep_dive',{}).get('chapters',[])),'status':'not_reviewed'})
for n,obj in [('inventory.json',rows),('assets.json',list(assets.values())),('course-data.json',data)]:
 (W/n).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
base={'commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=C,text=True).strip(),'git_status':subprocess.check_output(['git','status','--porcelain'],cwd=C,text=True),'html_sha256':sha(C/'docs/index.html'),'course_docs_equal':sha(C/'docs/index.html')==sha(C/'interactive-learning.html'),'topics':len(rows),'family_counts':dict(Counter(r['family'] for r in rows)),'unique_active_images':len(assets),'rules':{n:sha(R/n) for n in ['CLAUDE.md','IMAGE_STYLE_GUIDE.md','TEACHING_WEBPAGE_GUIDE.md','TEACHING_SCORING_RUBRIC.md','TEACHING_REVIEW_LOG.md']}}
(W/'baseline.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in base.items() if k!='rules'},indent=2));print('First-read unique images',len(set(p for r in rows for p in r['first_paths'])))

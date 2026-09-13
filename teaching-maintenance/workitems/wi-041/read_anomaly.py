from pathlib import Path
import re,json,sys
W=Path(__file__).resolve().parent;C=W.parents[1]
data=json.loads(re.search(r'<script id="course-data" type="application/json">(.*?)</script>',(C/'docs/index.html').read_text(encoding='utf8'),re.S)[1]);topics=[t for t in data['topics'] if t['family']=='anomaly'];seen=set();rows=[]
def read(v,path):
 if isinstance(v,dict):
  for k,x in v.items():yield from read(x,path+'.'+k)
 elif isinstance(v,list):
  for i,x in enumerate(v):yield from read(x,path+f'[{i}]')
 elif isinstance(v,str) and v not in seen:
  seen.add(v);yield [path,v]
for t in topics:
 items=[]
 for key in ['comparison','poc','boundary_cases','teach_back','transfer_check']:
  items+=list(read(t['teachingStory'].get(key,{}),key))
 for key in ['engineeringBrief','learnerBrief']:items+=list(read(t.get(key,{}),key))
 for i,s in enumerate(t['slides']):
  for k in ['guide','stages','misconception']:items+=list(read(s.get(k,{}),f'slides[{i}].{k}'))
 rows.append({'id':t['id'],'items':items})
(W/'anomaly-expanded.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
start=int(sys.argv[1]) if len(sys.argv)>1 else 0
for row in rows[start:start+4]:
 print('\nTOPIC',row['id'])
 for path,text in row['items']:print(path+': '+text)
print('TOTAL',len(rows),'uniquechars',sum(len(t) for r in rows for p,t in r['items']))

import json,hashlib,shutil
from pathlib import Path
W=Path(__file__).resolve().parent;C=W.parents[1];R=C.parents[1];S=C/'teaching-maintenance'
p=S/'manifest.json';m=json.loads(p.read_text(encoding='utf-8'));m['workitem']='WI-028'
new={}
for src in W.glob('qa-*/report.json'):
 new['workitems/wi-028/'+src.relative_to(W).as_posix()]=src
for src in list(W.glob('*.md'))+list(W.glob('*.json')):
 new['workitems/wi-028/'+src.name]=src
for name,src in [('WORKITEMS.md',R/'WORKITEMS.md'),('BEGINNER_VISUAL_TODO.md',C/'BEGINNER_VISUAL_TODO.md'),('BEGINNER_VISUAL_STATUS.md',C/'BEGINNER_VISUAL_STATUS.md')]:new['workitems/wi-028/'+name]=src
for slug in json.loads((W/'lesson-content.json').read_text(encoding='utf-8')):
 src=C/'_course_content/topics'/f'{slug}.json'
 new['workitems/wi-028/authoring/_course_content/topics/'+src.name]=src
 t=json.loads(src.read_text(encoding='utf-8'));rel=t['review_trace']['authority']
 new['workitems/wi-028/authoring/'+rel]=C/rel
for rel in ['_course_content/learner-briefs.json','tools/build_interactive_learning_html.py','tests/test_tall_mobile_artwork.py']:
 new['workitems/wi-028/authoring/'+rel]=C/rel
for src in W.glob('*.py'):new['workitems/wi-028/authoring/workitems/wi-028/'+src.name]=src
new['project/CLAUDE.md']=R/'CLAUDE.md'
known={r['snapshot']:r for r in m['files']}
for rel,src in new.items():
 if rel not in known:m['files'].append({'snapshot':rel,'source':str(src)})
for row in m['files']:
 dest=S/row['snapshot']
 if row['snapshot'] in new or row['snapshot'].startswith('project/'):
  src=Path(row['source']);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dest);row['sha256']=hashlib.sha256(src.read_bytes()).hexdigest()
 assert hashlib.sha256(dest.read_bytes()).hexdigest()==row['sha256']
p.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Verified',len(m['files']),'snapshots; historical checkpoints retained')

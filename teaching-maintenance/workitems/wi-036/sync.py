from pathlib import Path
import hashlib,json,shutil
W=Path(__file__).resolve().parent;C=W.parents[1];R=C.parents[1];S=C/'teaching-maintenance';mp=S/'manifest.json';m=json.loads(mp.read_text(encoding='utf8'));known={x['snapshot']:x for x in m['files']};files={}
for p in W.iterdir():
 if p.suffix in {'.md','.json','.py','.txt'}:files['workitems/wi-036/'+p.name]=p
for name in ['WORKITEMS.md','TEACHING_WEBPAGE_GUIDE.md','TEACHING_REVIEW_LOG.md']:files['project/'+name]=R/name
for name in ['BEGINNER_VISUAL_TODO.md','BEGINNER_VISUAL_STATUS.md']:files['course/'+name]=C/name
for rel in ['_course_content/poc-workbench.js','_course_content/poc-workbench.css','tools/build_interactive_learning_html.py','tests/test_poc_workbench.py']:files['workitems/wi-036/authoring/'+rel]=C/rel
for rel,src in files.items():
 dest=S/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dest)
 if rel not in known:known[rel]={'snapshot':rel};m['files'].append(known[rel])
 known[rel].update(source=str(src),sha256=hashlib.sha256(src.read_bytes()).hexdigest())
for row in m['files']:assert hashlib.sha256((S/row['snapshot']).read_bytes()).hexdigest()==row['sha256']
m['workitem']='WI-036';mp.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf8');print('Snapshots verified:',len(m['files']))

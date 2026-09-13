from pathlib import Path
import hashlib,json,shutil
W=Path(__file__).resolve().parent;C=W.parents[1];R=C.parents[1];S=C/'teaching-maintenance'
mp=S/'manifest.json';m=json.loads(mp.read_text(encoding='utf8'));known={x['snapshot']:x for x in m['files']};files={}
for p in W.rglob('*'):
 if p.is_file() and p.suffix in {'.md','.json','.py','.txt','.png','.html'}:
  files['workitems/wi-042/'+p.relative_to(W).as_posix()]=p
for p in (C/'workitems/wi-041').iterdir():
 if p.is_file() and (p.suffix in {'.md','.json','.py','.txt'} or p.name.startswith('recheck-finding-') and p.suffix=='.png'):
  files['workitems/wi-041/'+p.name]=p
for name in ['WORKITEMS.md','CLAUDE.md','IMAGE_STYLE_GUIDE.md','TEACHING_SCORING_RUBRIC.md','TEACHING_WEBPAGE_GUIDE.md','TEACHING_REVIEW_LOG.md']:
 files['project/'+name]=R/name
for name in ['BEGINNER_VISUAL_TODO.md','BEGINNER_VISUAL_STATUS.md']:files['course/'+name]=C/name
rels=['tools/verify_interactive_learning_html.py','tools/build_interactive_learning_html.py','tools/build_github_pages_site.py','tests/test_release_verifier.py','tests/test_detector_comparison_sharing.py']
rels += ['_course_content/topics/'+t+'.json' for t in json.loads((W/'changed-topics.json').read_text())]
for rel in rels:files['workitems/wi-042/authoring/'+rel]=C/rel
for rel,src in files.items():
 dest=S/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dest)
 if rel not in known:known[rel]={'snapshot':rel};m['files'].append(known[rel])
 known[rel].update(source=str(src),sha256=hashlib.sha256(src.read_bytes()).hexdigest())
for row in m['files']:assert hashlib.sha256((S/row['snapshot']).read_bytes()).hexdigest()==row['sha256'],row['snapshot']
m['workitem']='WI-042';mp.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Snapshots verified:',len(m['files']))

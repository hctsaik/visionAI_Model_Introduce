from pathlib import Path
import json,hashlib,shutil
W=Path(__file__).resolve().parent;C=W.parents[1];R=C.parents[1];S=C/'teaching-maintenance'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
mp=S/'manifest.json';m=json.loads(mp.read_text(encoding='utf8'));m['workitem']='WI-035';known={row['snapshot']:row for row in m['files']};new={}
for name in ['WORKITEMS.md','CLAUDE.md','IMAGE_STYLE_GUIDE.md','TEACHING_SCORING_RUBRIC.md','TEACHING_WEBPAGE_GUIDE.md','TEACHING_REVIEW_LOG.md']:new['project/'+name]=R/name
for name in ['BEGINNER_VISUAL_TODO.md','BEGINNER_VISUAL_STATUS.md']:new['course/'+name]=C/name
for src in W.iterdir():
 if src.suffix in {'.md','.json','.py','.txt'}:new['workitems/wi-035/'+src.name]=src
for name in ['REPORT.md','PLAN.md','scope.json','version-comparison.txt','wording-candidates.json']:new['workitems/wi-034/'+name]=C/'workitems/wi-034'/name
sources=[*sorted((C/'_course_content/topics').glob('*.json')),*sorted((C/'_batch_specs').glob('*.json')),C/'_course_content/learner-briefs.json',C/'_course_content/poc-workbench.js',C/'_course_content/poc-workbench.css']
sources += [C/p for p in ['tools/build_interactive_learning_html.py','tools/build_github_pages_site.py','tools/validate_teaching_preflight.py','tests/test_poc_workbench.py','tests/test_engineering_mobile_pages.py']]
for src in sources:new['workitems/wi-035/authoring/'+src.relative_to(C).as_posix()]=src
for rel,src in new.items():
 dest=S/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dest)
 if rel not in known:known[rel]={'snapshot':rel};m['files'].append(known[rel])
 known[rel].update(source=str(src),sha256=sha(src));assert sha(dest)==sha(src)
for row in m['files']:assert sha(S/row['snapshot'])==row['sha256'],row['snapshot']
mp.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Copied',len(new),'files; verified',len(m['files']),'snapshot hashes.')

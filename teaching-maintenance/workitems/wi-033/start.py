from pathlib import Path
import json,hashlib,shutil,subprocess,re
W=Path(__file__).resolve().parent;C=W.parents[1];R=C.parents[1]
rows=json.loads((W.parent/'wi-031/results.json').read_text(encoding='utf-8'))
first={'charuco','ecc','sift','lightglue','det-dino-detector','yolo-world'}
rows=[r for r in rows if r['id'] not in first];assert len(rows)==52
html=(C/'interactive-learning.html').read_text(encoding='utf-8')
data=json.loads(re.search(r'<script id="course-data" type="application/json">(.*?)</script>',html,re.S)[1])
catalog={t['id']:t for t in data['topics']}
sources=list((C/'_course_content/topics').glob('*.json'))+[C/'interactive-learning.html',C/'docs/index.html',C/'_course_content/learner-briefs.json']
for row in rows:
 row['status']='pending';row['user_approval']='pending';row['prior_audit']=row.pop('implementation_this_audit',None)
 pub=catalog[row['id']]
 for k in ['modelPath','manifestPath']:sources.append(C/pub[k])
 row['model_path']=pub['modelPath'];row['manifest_path']=pub['manifestPath']
 row['topic_source']=next(p.relative_to(C).as_posix() for p in (C/'_course_content/topics').glob('*.json') if json.loads(p.read_text(encoding='utf-8')).get('model')==row['model'])
 row['baseline_engineering']=[s['image'] for s in pub['slides']]
baseline=[]
for p in sources:
 dest=W/'baseline'/p.relative_to(C)
 if dest.exists():assert dest.read_bytes()==p.read_bytes(),p
 else:dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dest)
 baseline.append({'path':p.relative_to(C).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
for name in ['CLAUDE.md','IMAGE_STYLE_GUIDE.md','TEACHING_REVIEW_LOG.md','TEACHING_SCORING_RUBRIC.md','TEACHING_WEBPAGE_GUIDE.md']:
 p=R/name;dest=W/'baseline/authority'/name;dest.parent.mkdir(parents=True,exist_ok=True)
 if not dest.exists():shutil.copyfile(p,dest)
(W/'inventory.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
(W/'baseline.json').write_text(json.dumps({'head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=C,text=True).strip(),'files':baseline,'active_generation_processes':False},indent=2),encoding='utf-8')
print('Saved',len(baseline),'baseline files;',len(rows),'lessons')
for r in rows:print(r['id'],r['topic_source'])

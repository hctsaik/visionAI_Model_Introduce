from pathlib import Path
import json,shutil,hashlib,subprocess
W=Path(__file__).resolve().parent; C=W.parents[1]; R=C.parents[1]
slugs=['charuco','ecc','sift','lightglue','det-dino-detector','yolo-world']
files=[C/'_course_content/learner-briefs.json',C/'interactive-learning.html',C/'docs/index.html']
for slug in slugs:
 p=C/'_course_content/topics'/f'{slug}.json';t=json.loads(p.read_text(encoding='utf-8'));files.append(p)
 files.append(C/t['review_trace']['authority'])
records=[]
for p in files:
 d=W/'baseline'/p.relative_to(C); d.parent.mkdir(parents=True,exist_ok=True)
 if not d.exists():shutil.copyfile(p,d)
 records.append({'path':p.relative_to(C).as_posix(),'sha256':hashlib.sha256(d.read_bytes()).hexdigest()})
(W/'baseline.json').write_text(json.dumps({'files':records,'commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=C,text=True).strip(),'rules':{n:hashlib.sha256((R/n).read_bytes()).hexdigest() for n in ['CLAUDE.md','IMAGE_STYLE_GUIDE.md','TEACHING_WEBPAGE_GUIDE.md','TEACHING_SCORING_RUBRIC.md','TEACHING_REVIEW_LOG.md']}},ensure_ascii=False,indent=2),encoding='utf-8')
print('Saved baseline',len(files))

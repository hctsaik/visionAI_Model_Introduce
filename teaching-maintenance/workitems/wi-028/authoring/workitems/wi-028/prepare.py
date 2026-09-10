import json,shutil
from pathlib import Path
W=Path(__file__).resolve().parent; C=W.parents[1]
names=['frame-difference','background-subtraction','lucas-kanade','raft','bytetrack','convlstm','videomae','v-jepa']
B=W/'baseline';B.mkdir(exist_ok=True)
for slug in names:
 p=C/'_course_content/topics'/f'{slug}.json';t=json.loads(p.read_text(encoding='utf-8'))
 shutil.copy2(p,B/p.name)
 authority=C/t['review_trace']['authority'];shutil.copy2(authority,B/(slug+'-model.md'))
 print(slug,t['review_trace']['authority'],len(t['beginner_path']['visuals']))
shutil.copy2(C/'_course_content/learner-briefs.json',B/'learner-briefs.json')
s=(W.parent/'wi-027/baseline_views.py').read_text(encoding='utf-8')
s=s.replace("names=['dinov2','dinov3','clip','siglip','llava','qwen-vl','gemini-vision']",'names='+repr(names)).replace('14 baseline views and seven','16 baseline views and eight')
(W/'baseline_views.py').write_text(s,encoding='utf-8')

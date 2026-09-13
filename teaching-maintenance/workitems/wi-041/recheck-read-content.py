import json,re,sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf8');c=Path('teaching-images/vision-ai-model-selection');d=json.loads(re.search(r'<script id="course-data" type="application/json">(.*?)</script>',(c/'docs/index.html').read_text('utf8'),re.S)[1]);a=int(sys.argv[1]);b=int(sys.argv[2])
for t in d['topics'][a:b]:
 s=t['teachingStory']; print('\n###',t['id'],t['model']); print('HEAD',t['learnerBrief']['problem'],t['learnerBrief']['deliverable'],t['learnerBrief']['first']);
 for v in s['beginner_path']['visuals']: print('MAIN',v['title'],v['caption'],' | ',*[x['body'] for x in v['callouts']]);
 print('MECH',[(x['title'],x['body']) for x in s['mechanism_steps']]);print('COMPARE',s['comparison'],s['selection']);print('QUIZ',s['micro_example']);print('TRANSFER',s['transfer_check'])

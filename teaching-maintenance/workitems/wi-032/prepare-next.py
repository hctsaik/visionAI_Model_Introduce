from pathlib import Path
import json,subprocess,sys
W=Path(__file__).resolve().parent; C=W.parents[1]
jobs=json.loads((W/'label-correction-plan.json').read_text(encoding='utf-8-sig'))
for id,prompt in jobs:
 p=W/f'{id}-r02.md'
 p.write_text((W/f'{id}-r01.md').read_text(encoding='utf-8')+'\n## r02 label correction\n'+prompt+'\nActual PNG review pending; user approval pending.\n',encoding='utf-8')
 subprocess.run([sys.executable,str(C/'tools/validate_teaching_preflight.py'),str(p)],check=True)
for id in ['dino-core','world-core','detector-compare']:
 p=W/f'{id}-r01-mobile.md'
 p.write_text((W/f'{id}-r01.md').read_text(encoding='utf-8')+'\n## Mobile composition\nIndependently reflow three groups top to bottom, 768px wide, 32px minimum text, retain mechanism and single takeaway, not cropped desktop. Actual PNG review pending; user approval pending.\n',encoding='utf-8')
 subprocess.run([sys.executable,str(C/'tools/validate_teaching_preflight.py'),str(p)],check=True)

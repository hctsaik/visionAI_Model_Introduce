from pathlib import Path
import json,re
C=Path(__file__).resolve().parents[2]
data=json.loads(re.search(r'<script id="course-data" type="application/json">(.*?)</script>',(C/'docs/index.html').read_text(encoding='utf8'),re.S)[1])
for t in data['topics']:
 if t['id'] in ['convnext','vjepa','v-jepa','ad-anomalygpt']:
  print(t['id'],list(t))
  story=t.get('teachingStory',{})
  print(json.dumps({k:v for k,v in story.items() if k in ['mechanism_steps','mental_model','engineering_slides']},ensure_ascii=False,indent=2)[:9000])

from pathlib import Path
import json,sys
sys.stdout.reconfigure(encoding='utf8');p=Path('teaching-images/vision-ai-model-selection/workitems/wi-041/recheck-external-rendered-anchors.json');d=json.loads(p.read_text('utf8'));bad=[u for u in d['urls'] if ('%20%7C%20' in u or ' | ' in u or u.count('https://')>1 or u.count('http')>1)];print('rows',len(d['rows']),'unique',len(d['urls']),'suspect',bad);d['malformed_composite_candidates']=bad;d['validation']='58 actual rendered expanded lesson DOM hrefs; no network refetch';p.write_text(json.dumps(d,ensure_ascii=False,indent=2),'utf8')

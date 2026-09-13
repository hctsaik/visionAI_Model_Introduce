import json,re,sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf8');c=Path('teaching-images/vision-ai-model-selection');o=c/'workitems/wi-041';r=json.loads((o/'recheck-rendered-content.json').read_text('utf8'));print('Rows',len(r['rows']),'Unique',len({x['default'] for x in r['rows']}));
for x in r['rows']:
 if x['id'] in ['ad-diffad','u-net','yolo-seg','ad-efficientad','convlstm','videomae']:
  a=x['expanded'];n=a.find('實作時逐步核對');print(x['id'],a[n:n+1000])

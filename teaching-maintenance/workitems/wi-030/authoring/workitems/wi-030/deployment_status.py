import json,subprocess
from pathlib import Path
import requests
W=Path(__file__).resolve().parent;C=W.parents[1]
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=C,text=True).strip()
r=requests.get('https://api.github.com/repos/hctsaik/visionAI_Model_Introduce/actions/runs',params={'head_sha':head,'per_page':10},timeout=30);r.raise_for_status()
rows=[{k:x.get(k) for k in ['id','name','status','conclusion','head_sha','html_url','created_at']} for x in r.json()['workflow_runs']]
(W/'deployment-status.json').write_text(json.dumps({'commit':head,'runs':rows},indent=2)+'\n',encoding='utf-8')
print(json.dumps(rows,indent=2))

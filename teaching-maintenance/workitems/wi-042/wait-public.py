from pathlib import Path
import json,time,hashlib,urllib.request
W=Path(__file__).resolve().parent;C=W.parents[1];want=hashlib.sha256((C/'docs/index.html').read_bytes()).hexdigest();rows=[]
for i in range(24):
 try:
  with urllib.request.urlopen(urllib.request.Request('https://hctsaik.github.io/visionAI_Model_Introduce/',headers={'Cache-Control':'no-cache'}),timeout=20) as r:actual=hashlib.sha256(r.read()).hexdigest()
  row={'attempt':i+1,'sha256':actual,'matches':actual==want}
 except Exception as e:row={'attempt':i+1,'error':str(e),'matches':False}
 rows.append(row);(W/'deployment-wait.json').write_text(json.dumps(rows,indent=2),encoding='utf8');print(row,flush=True)
 if row['matches']:break
 time.sleep(10)
else:raise SystemExit('Deployment did not match within bounded wait')

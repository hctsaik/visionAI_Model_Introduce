from pathlib import Path
import json,subprocess,sys
W=Path(__file__).resolve().parent;C=W.parents[1]
selected=json.loads((W/'selected-assets.json').read_text(encoding='utf-8'))
briefs={r['brief'] for r in selected.values()}
for row in json.loads((W/'engineering-plan.json').read_text(encoding='utf-8')):
 version={'sift-engineering-1':'r06','yolo-world-engineering-2':'r05','yolo-world-engineering-3':'r07'}.get(row['id'],'r04')
 briefs.add(row['id']+'-'+version+'.md')
results=[]
for name in sorted(briefs):
 p=W/name;result=subprocess.run([sys.executable,'-X','utf8',str(C/'tools/validate_teaching_preflight.py'),str(p)],capture_output=True,text=True,encoding='utf-8')
 results.append({'brief':name,'returncode':result.returncode,'output':result.stdout.strip(),'error':result.stderr.strip()})
(W/'selected-preflight-validation.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
assert all(r['returncode']==0 for r in results)
print('PASS',len(results),'selected story briefs; image/user review are separate')

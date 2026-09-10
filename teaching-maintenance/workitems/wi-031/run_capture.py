import json,subprocess,sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
W=Path(__file__).resolve().parent
rows=json.loads((W/'inventory.json').read_text(encoding='utf-8'))
def run(r):
 p=W/'pages'/r['id']/'report.json'
 if p.exists() and all(x.get('complete') and x.get('capture_version')==2 for x in json.loads(p.read_text(encoding='utf-8'))):return
 result=subprocess.run([sys.executable,'-X','utf8',str(W/'capture.py'),r['id']],capture_output=True,text=True,encoding='utf-8')
 print(result.stdout or result.stderr,flush=True)
with ThreadPoolExecutor(max_workers=2) as pool:list(pool.map(run,rows))

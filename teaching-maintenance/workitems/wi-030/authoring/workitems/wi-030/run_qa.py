import subprocess,sys,json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
W=Path(__file__).resolve().parent
slugs=list(json.loads((W/'lesson-content.json').read_text(encoding='utf-8')))
def run(s):
 r=subprocess.run([sys.executable,'-X','utf8',str(W/'qa_lesson.py'),s,'3'],capture_output=True,text=True,encoding='utf-8')
 (W/(s+'-qa.log')).write_text(r.stdout+r.stderr,encoding='utf-8');print(s,r.returncode,flush=True);return r.returncode
with ThreadPoolExecutor(max_workers=2) as pool:results=list(pool.map(run,slugs))
sys.exit(any(results))

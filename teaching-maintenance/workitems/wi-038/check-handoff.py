from pathlib import Path
import subprocess,sys,os,json
W=Path(__file__).resolve().parent;C=W.parents[1];results=[]
for name,route in [('source','interactive-learning.html'),('docs','docs/index.html')]:
 r=subprocess.run([sys.executable,'-X','utf8','tests/test_poc_workbench.py','PocWorkbenchTests.test_lesson_handoff_keeps_candidate_as_context','-v'],cwd=C,env=dict(os.environ,VISIONAI_TEST_URL='http://127.0.0.1:8000/'+route),capture_output=True,text=True,encoding='utf8')
 (W/f'handoff-{name}.txt').write_text(r.stdout+r.stderr,encoding='utf8');assert r.returncode==0,r.stderr
 results.append(dict(route=route,passed=True));print(name,'handoff preserved after reload',flush=True)
(W/'handoff-verification.json').write_text(json.dumps(results,indent=2),encoding='utf8')

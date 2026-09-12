from pathlib import Path
import subprocess,sys,json,os
W=Path(__file__).resolve().parent;C=W.parents[1]
jobs={
'poc-docs':['tests/test_poc_workbench.py','-v'],
'poc-course':['tests/test_poc_workbench.py','-v'],
'regression':['-m','unittest','discover','-s','tests','-p','test_interactive_navigation.py','-v'],
'bundle':['-m','unittest','discover','-s','tests','-p','test_github_pages_bundle.py','-v'],
'engineering':['-m','unittest','discover','-s','tests','-p','test_engineering_mobile_pages.py','-v'],
'html':['tools/verify_interactive_learning_html.py'],
}
results=[]
for name,args in jobs.items():
 env=os.environ.copy()
 if name=='poc-course':env['VISIONAI_TEST_URL']='http://127.0.0.1:8000/interactive-learning.html'
 r=subprocess.run([sys.executable,'-X','utf8',*args],cwd=C,env=env,capture_output=True,text=True,encoding='utf8')
 (W/f'test-{name}.txt').write_text(r.stdout+r.stderr,encoding='utf8')
 results.append(dict(name=name,exit_code=r.returncode,log=f'test-{name}.txt'))
 print(name,r.returncode,flush=True)
 (W/'test-results.json').write_text(json.dumps(results,indent=2),encoding='utf8')
sys.exit(any(x['exit_code'] for x in results))

from pathlib import Path
import json,subprocess,sys,os,re,hashlib
from playwright.sync_api import sync_playwright
W=Path(__file__).resolve().parent;C=W.parents[1];results=[]
for route in ['docs/index.html','interactive-learning.html']:
 env=dict(os.environ,VISIONAI_TEST_URL='http://127.0.0.1:8000/'+route)
 r=subprocess.run([sys.executable,'-X','utf8','tests/test_poc_workbench.py','-v'],cwd=C,env=env,capture_output=True,text=True,encoding='utf8');name='docs' if route.startswith('docs') else 'course'
 (W/f'tests-{name}.txt').write_text(r.stdout+r.stderr,encoding='utf8');assert r.returncode==0,r.stderr
 results.append({'route':route,'behavior_tests':12,'passed':True});print(name,'12 passed',flush=True)
with sync_playwright() as p:
 b=p.chromium.launch(channel='msedge',headless=True)
 for route in ['docs/index.html','interactive-learning.html']:
  for width,height in [(1440,1000),(390,844)]:
   page=b.new_page(viewport={'width':width,'height':height});page.goto('http://127.0.0.1:8000/'+route+'#view=poc');name=('docs' if route.startswith('docs') else 'course')+f'-{width}'
   for i in range(3):
    page.locator('.poc-step-nav button').nth(i).click();assert page.locator('textarea:visible').count()==0
    assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
    page.evaluate('document.activeElement.blur();window.scrollTo({top:0,behavior:"instant"})');page.screenshot(path=str(W/f'{name}-step{i+1}.png'),full_page=True)
   page.locator('[data-action="fill-poc-example"]').click();page.locator('[data-action="poc-preview"]').filter(visible=True).first.click();page.wait_for_function("getComputedStyle(document.querySelector('.toast')).opacity==='0'");page.evaluate('document.activeElement.blur();window.scrollTo({top:0,behavior:"instant"})');page.screenshot(path=str(W/f'{name}-preview.png'),full_page=True);page.close()
 b.close()
current=(C/'docs/index.html').read_bytes();assert current==(C/'interactive-learning.html').read_bytes()
baseline=subprocess.check_output(['git','show','e9c732f:docs/index.html'],cwd=C)
pattern=rb'<script id="course-data" type="application/json">(.*?)</script>'
assert json.loads(re.search(pattern,current,re.S)[1])==json.loads(re.search(pattern,baseline,re.S)[1])
result={'routes':results,'total_behavior_tests':24,'screenshots':16,'empty_forms_visible_textareas':0,'horizontal_overflow':False,'course_data_unchanged':True,'course_docs_equal':True,'html_sha256':hashlib.sha256(current).hexdigest(),'user_approval':'pending'}
(W/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(result,ensure_ascii=False))

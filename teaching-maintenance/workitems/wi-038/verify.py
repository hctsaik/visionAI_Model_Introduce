from pathlib import Path
import json,subprocess,sys,os,re,hashlib
from playwright.sync_api import sync_playwright
W=Path(__file__).resolve().parent;C=W.parents[1];results=[]
def index_value(select):return select.locator('option').nth(1).get_attribute('value')
for route in ['docs/index.html','interactive-learning.html']:
 name='docs' if route.startswith('docs') else 'source'
 log=(W/f'tests-{name}.txt').read_text(encoding='utf8');assert '\nOK' in log,log
 count=int(re.search(r'Ran (\d+) tests',log)[1]);results.append({'route':route,'tests':count,'passed':True});print(name,count,'passed',flush=True)
with sync_playwright() as p:
 b=p.chromium.launch(channel='msedge',headless=True)
 for route in ['docs/index.html','interactive-learning.html']:
  for width,height in [(1440,1000),(390,844)]:
   page=b.new_page(viewport={'width':width,'height':height});page.goto('http://127.0.0.1:8000/'+route+'#view=poc');name=('docs' if route.startswith('docs') else 'course')+f'-{width}'
   for stage in ['question','result','preview']:
    if stage=='result':
     while page.locator('#poc-answer').count():
      select=page.locator('#poc-answer');qid=select.get_attribute('data-poc-answer');select.select_option('count' if qid=='task' else index_value(select));page.locator('[data-action="poc-next"]').click()
    if stage=='preview':page.locator('[data-action="poc-preview"]').click()
    assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
    page.evaluate('document.activeElement.blur();window.scrollTo({top:0,behavior:"instant"})');page.screenshot(path=str(W/f'{name}-{stage}.png'),full_page=True)
   page.close()
 b.close()
current=(C/'docs/index.html').read_bytes();assert current==(C/'interactive-learning.html').read_bytes()
baseline=subprocess.check_output(['git','show','193f70d:docs/index.html'],cwd=C)
pattern=rb'<script id="course-data" type="application/json">(.*?)</script>'
assert json.loads(re.search(pattern,current,re.S)[1])==json.loads(re.search(pattern,baseline,re.S)[1])
result={'routes':results,'screenshots':12,'course_data_unchanged':True,'course_docs_equal':True,'html_sha256':hashlib.sha256(current).hexdigest(),'user_approval':'pending'}
(W/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(result,ensure_ascii=False))

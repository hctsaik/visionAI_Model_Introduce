from pathlib import Path
import json,re,hashlib,subprocess
from playwright.sync_api import sync_playwright
W=Path(__file__).resolve().parent;C=W.parents[1]
raw=(C/'docs/index.html').read_bytes();assert raw==(C/'interactive-learning.html').read_bytes()
pattern=rb'<script id="course-data" type="application/json">(.*?)</script>'
current=json.loads(re.search(pattern,raw,re.S)[1]);old=json.loads(re.search(pattern,subprocess.check_output(['git','show','d16f6be:docs/index.html'],cwd=C),re.S)[1])
changed=[]
for t,b in zip(current['topics'],old['topics']):
 assert t['id']==b['id']
 if t!=b:
  changed.append(t['id']);assert t['id'] in ['convnext','v-jepa','ad-anomalygpt']
  before=b['teachingStory'].pop('mechanism_steps');after=t['teachingStory'].pop('mechanism_steps');assert before!=after;assert t==b
assert set(changed)=={'convnext','v-jepa','ad-anomalygpt'};assert current==old
with sync_playwright() as p:
 browser=p.chromium.launch(channel='msedge',headless=True)
 for width,height in [(1440,1000),(390,844)]:
  page=browser.new_page(viewport={'width':width,'height':height});errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
  page.goto('http://127.0.0.1:8000/docs/index.html#view=home');page.wait_for_timeout(300);page.screenshot(path=str(W/f'home-{width}.png'),full_page=True);page.screenshot(path=str(W/f'home-first-{width}.png'))
  assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
  page.locator('main .hero-actions [data-view="poc"]').click();page.locator('#poc-answer').wait_for();assert page.locator('#poc-answer').get_attribute('data-poc-answer')=='task'
  for topic in changed:
   page.goto('http://127.0.0.1:8000/docs/index.html#view=lesson&lesson='+topic+'&slide=4')
   chain=page.locator('.causal-chain');details=chain.locator('xpath=ancestor::details[1]');details.locator('summary').first.click();chain.wait_for(state='visible')
   text=chain.inner_text();assert 'WI030-' not in text and '由本課核心機制連接工作用途' not in text
   if topic=='ad-anomalygpt':assert '應用' in text and '選用' in text
   assert page.evaluate('document.documentElement.scrollWidth<=innerWidth');chain.screenshot(path=str(W/f'{topic}-{width}.png'),style='.topbar,.skip-link{visibility:hidden!important}');(W/f'{topic}-{width}.txt').write_text(text,encoding='utf8')
  assert not errors,errors;page.close()
 browser.close()
result={'changed_topics':changed,'only_mechanism_steps_changed':True,'source_docs_equal':True,'sha256':hashlib.sha256(raw).hexdigest(),'desktop_mobile_screenshots':10,'capture_note':'Fixed navigation hidden only in isolated causal-chain screenshots to avoid screenshot overlays. Home captures unchanged.','browser_errors':[],'user_review':'pending'}
(W/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(result,ensure_ascii=False))

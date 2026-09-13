from pathlib import Path
import urllib.request,hashlib,json,sys,subprocess
from playwright.sync_api import sync_playwright
W=Path(__file__).resolve().parent;C=W.parents[1];url='https://hctsaik.github.io/visionAI_Model_Introduce/'
expected=hashlib.sha256((C/'docs/index.html').read_bytes()).hexdigest()
with urllib.request.urlopen(urllib.request.Request(url,headers={'Cache-Control':'no-cache'}),timeout=30) as r:raw=r.read()
actual=hashlib.sha256(raw).hexdigest()
if actual!=expected:print('Deployment pending:',actual);sys.exit(3)
with sync_playwright() as p:
 b=p.chromium.launch(channel='msedge',headless=True)
 for width,height in [(1440,1000),(390,844)]:
  context=b.new_context(viewport={'width':width,'height':height});page=context.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
  page.goto(url+'#view=home');page.locator('main .hero-actions [data-view="poc"]').click();page.locator('#poc-answer').wait_for();assert page.locator('#poc-model').count()==0
  answers={'task':'count','placement':'fixed','visibility':'clear','data':'normal'}
  while page.locator('#poc-answer').count():
   select=page.locator('#poc-answer');qid=select.get_attribute('data-poc-answer');select.select_option(answers[qid]);page.locator('[data-action="poc-next"]').click()
  assert '逐格' in page.locator('#poc-result-title').inner_text()
  page.locator('[data-action="poc-preview"]').click();assert '固定' in page.locator('#poc-preview').inner_text()
  assert page.evaluate('document.documentElement.scrollWidth<=innerWidth');assert not errors
  before=page.evaluate('localStorage.getItem("vision-ai-model-selection-learning-v1")')
  page.locator('.poc-backup:not(#poc-legacy) summary').click()
  dialogs=[]
  page.on('dialog',lambda d:(dialogs.append(d.message),d.dismiss()))
  page.locator('#import-progress').set_input_files({'name':'unrelated.json','mimeType':'application/json','buffer':b'{"hello":"world"}'})
  page.wait_for_function('document.getElementById("toast").textContent.includes("無法")')
  assert not dialogs and page.evaluate('localStorage.getItem("vision-ai-model-selection-learning-v1")')==before
  page.evaluate('document.activeElement.blur();window.scrollTo({top:0,behavior:"instant"})');page.screenshot(path=str(W/f'recheck-public-{width}.png'),full_page=True);context.close()
 b.close()
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=C,text=True).strip();remote=subprocess.check_output(['git','ls-remote','origin','refs/heads/main'],cwd=C,text=True).split()[0];assert head==remote
result=dict(commit=head,remote_main=remote,public_url=url+'#view=home',public_html_sha256=actual,local_html_sha256=expected,public_desktop_mobile_smoke='passed',invalid_backup_preserved_original=True,user_approval='pending')
(W/'recheck-public-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(result,ensure_ascii=False))


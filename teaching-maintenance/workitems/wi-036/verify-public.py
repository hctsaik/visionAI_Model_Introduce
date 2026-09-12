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
  page.goto(url+'#view=poc');page.locator('#poc-task').select_option(index=1);assert page.locator('textarea:visible').count()==0;page.locator('#poc-output').select_option(index=1)
  page.locator('.poc-step-nav button').nth(1).click();page.locator('#poc-model').select_option('det-dino-detector');assert 'DINO' in page.locator('#poc-model-guide').inner_text()
  page.locator('.poc-step-nav button').nth(2).click();page.locator('#poc-owner').select_option(index=1);assert page.locator('textarea:visible').count()==0
  page.locator('[data-action="poc-preview"]').filter(visible=True).first.click();assert '漏裝' in page.locator('#poc-preview').inner_text()
  assert page.evaluate('document.documentElement.scrollWidth<=innerWidth');assert not errors
  page.evaluate('document.activeElement.blur();window.scrollTo({top:0,behavior:"instant"})');page.screenshot(path=str(W/f'public-final-{width}.png'),full_page=True);context.close()
 b.close()
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=C,text=True).strip();remote=subprocess.check_output(['git','ls-remote','origin','refs/heads/main'],cwd=C,text=True).split()[0];assert head==remote
result=dict(commit=head,remote_main=remote,public_url=url+'#view=poc',public_html_sha256=actual,local_html_sha256=expected,public_desktop_mobile_smoke='passed',user_approval='pending')
(W/'release-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(result,ensure_ascii=False))

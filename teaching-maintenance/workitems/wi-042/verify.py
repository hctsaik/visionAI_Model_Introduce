from pathlib import Path
import json,re,hashlib,subprocess,sys,http.server,threading,functools,os,urllib.request
from playwright.sync_api import sync_playwright
W=Path(__file__).resolve().parent;C=W.parents[1];public='--public' in sys.argv
raw=(C/'docs/index.html').read_bytes();assert raw==(C/'interactive-learning.html').read_bytes()
pattern=rb'<script id="course-data" type="application/json">(.*?)</script>'
data=json.loads(re.search(pattern,raw,re.S)[1]);oldraw=(W/'baseline/index.html').read_bytes();old=json.loads(re.search(pattern,oldraw,re.S)[1])
changed=[];expected=set(json.loads((W/'changed-topics.json').read_text()))
for a,b in zip(data['topics'],old['topics']):
 assert a['id']==b['id']
 if a!=b:
  changed.append(a['id']);assert a['id'] in expected
  a['teachingStory'].pop('mechanism_steps');b['teachingStory'].pop('mechanism_steps');assert a==b
assert set(changed)==expected and data==old
assert re.sub(pattern,b'COURSE',raw)==re.sub(pattern,b'COURSE',oldraw),'Shared renderer/JS unexpectedly changed'
class Quiet(http.server.SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
server=None
if public:
 url='https://hctsaik.github.io/visionAI_Model_Introduce/'
 with urllib.request.urlopen(urllib.request.Request(url,headers={'Cache-Control':'no-cache'}),timeout=30) as r:assert r.read()==raw,'Public deployment not current'
else:
 server=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Quiet,directory=str(C)))
 threading.Thread(target=server.serve_forever,daemon=True).start();url=f'http://127.0.0.1:{server.server_port}/docs/index.html'
result={'html_sha256':hashlib.sha256(raw).hexdigest(),'changed_topics':changed,'only_mechanism_steps_changed':True,'shared_template_unchanged':True,'mode':'public' if public else 'local','tests':{},'pages':[],'user_approval':'pending'}
def save(): (W/('release-verification.json' if public else 'verification.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
try:
 if not public:
  cmds=[('pytest',[sys.executable,'-X','utf8','-m','pytest','tests/test_release_verifier.py','tests/test_interactive_navigation.py','tests/test_github_pages_bundle.py','tests/test_release_hardening.py','tests/test_poc_workbench.py','-q']),('rules',['node','--test','tests/test_poc_decision.cjs']),('verifier-source',[sys.executable,'-X','utf8','tools/verify_interactive_learning_html.py']),('verifier-docs',[sys.executable,'-X','utf8','tools/verify_interactive_learning_html.py','docs/index.html'])]
  env={**os.environ,'VISIONAI_TEST_URL':url,'PYTHONUTF8':'1'}
  for name,cmd in cmds:
   print('Running',name,flush=True)
   with (W/(name+'.txt')).open('w',encoding='utf8') as f:r=subprocess.run(cmd,cwd=C,env=env,stdout=f,stderr=subprocess.STDOUT,timeout=240)
   result['tests'][name]=r.returncode;save();assert r.returncode==0,name
 with sync_playwright() as pw:
  browser=pw.chromium.launch(channel='msedge',headless=True)
  for width in [1440,390]:
   context=browser.new_context(viewport={'width':width,'height':1000 if width==1440 else 844},reduced_motion='reduce');p=context.new_page();p.set_default_timeout(15000);errors=[];p.on('pageerror',lambda e:errors.append(str(e)))
   for tid in changed:
    p.goto(url+'#view=lesson&lesson='+tid+'&slide=1',timeout=30000);p.locator('#lesson-title').wait_for()
    chain=p.locator('.causal-chain');chain.locator('xpath=ancestor::details[1]').locator('summary').first.click();chain.wait_for(state='visible')
    text=chain.inner_text();source=json.loads((C/'_course_content/topics'/f'{tid}.json').read_text(encoding='utf8'))
    for step in source['mechanism_steps']:
     assert step['title'] in text and step['body'] in text and step['why'] in text
    if tid=='ad-diffad':assert '一次 forward' not in text and '兩個噪聲尺度各做單步估計' in text
    assert p.evaluate('document.documentElement.scrollWidth<=innerWidth')
    image=f'{"public" if public else "local"}-{tid}-{width}.png';chain.screenshot(path=str(W/image),style='.topbar,.skip-link{visibility:hidden!important}')
    result['pages'].append({'topic':tid,'width':width,'text_matches_source':True,'screenshot':image});save()
   p.goto(url+'#view=home');p.locator('main .hero-actions [data-view="poc"]').click();p.locator('#poc-answer').wait_for()
   answers={'task':'count','placement':'fixed','visibility':'clear','data':'normal'}
   while p.locator('#poc-answer').count():
    select=p.locator('#poc-answer');select.select_option(answers[select.get_attribute('data-poc-answer')]);p.locator('[data-action="poc-next"]').click()
   assert '逐格' in p.locator('#poc-result-title').inner_text();p.locator('[data-action="poc-preview"]').click();assert '固定' in p.locator('#poc-preview').inner_text();assert not errors
   result[f'poc_{width}']='passed';save();context.close()
  browser.close()
 if public:
  result['commit']=subprocess.check_output(['git','rev-parse','HEAD'],cwd=C,text=True).strip()
  result['remote_main']=subprocess.check_output(['git','ls-remote','origin','refs/heads/main'],cwd=C,text=True).split()[0];assert result['commit']==result['remote_main']
 result['complete']=True;save();print(json.dumps(result,ensure_ascii=False),flush=True)
finally:
 if server:server.shutdown();server.server_close()

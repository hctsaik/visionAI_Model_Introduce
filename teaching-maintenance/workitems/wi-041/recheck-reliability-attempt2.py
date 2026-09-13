from pathlib import Path
import json, os, subprocess
from playwright.sync_api import sync_playwright

W=Path(__file__).resolve().parent
C=W.parents[1]
BASE='http://127.0.0.1:8014/docs/index.html'
KEY='vision-ai-model-selection-learning-v1'
results=[]
for name,cmd in [
    ('rules',['node',str(C/'tests/test_poc_decision.cjs')]),
    ('hardening',['python','-X','utf8',str(C/'tests/test_release_hardening.py'),'-v']),
    ('poc',['python','-X','utf8',str(C/'tests/test_poc_workbench.py'),'-v'])]:
    env=os.environ.copy();env['VISIONAI_TEST_URL']=BASE
    p=subprocess.run(cmd,capture_output=True,text=True,encoding='utf8',env=env)
    (W/f'recheck-reliability-attempt2-{name}.txt').write_text(p.stdout+p.stderr+f'\nEXIT: {p.returncode}\n',encoding='utf8')
    results.append({'suite':name,'exit':p.returncode})
    print(name,p.returncode,flush=True)

with sync_playwright() as pw:
    browser=pw.chromium.launch(channel='msedge',headless=True)
    context=browser.new_context(accept_downloads=True,viewport={'width':1440,'height':1000})
    page=context.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
    page.goto(BASE+'#view=poc');page.locator('#poc-answer').wait_for()
    def click(action):page.locator(f'[data-action="{action}"]:visible').first.click()
    def raw():return page.evaluate('(key)=>localStorage.getItem(key)',KEY)
    def backup():
        d=page.locator('.poc-backup').last
        if d.get_attribute('open') is None:d.locator('summary').click()
    # Chosen but not advanced answers must survive reload.
    page.locator('#poc-answer').select_option('measure');page.reload()
    assert page.locator('#poc-answer').get_attribute('data-poc-answer')=='task'
    assert page.locator('#poc-answer').input_value()=='measure'
    click('poc-next')
    for key,value in [('unit','mm'),('plane','planar'),('calibration','none'),('visibility','clear'),('data','few')]:
        assert page.locator('#poc-answer').get_attribute('data-poc-answer')==key
        page.locator('#poc-answer').select_option(value);click('poc-next')
    click('poc-preview')
    page.locator('.poc-optional').filter(has=page.locator('#poc-handoff')).locator('summary').click()
    note='夜班王工程師：先補校正；尺寸 < 5 mm & 原圖核對。'
    page.locator('#poc-handoff').fill(note)
    # Download immediately without forcing blur first.
    with page.expect_download() as info:click('export-poc-markdown')
    assert note in info.value.path().read_text(encoding='utf8')
    page.reload();click('poc-preview')
    assert note in page.locator('#poc-preview').inner_text()
    click('toggle-theme');assert page.locator('html').get_attribute('data-theme')=='dark'
    page.reload();assert page.locator('html').get_attribute('data-theme')=='dark'
    backup()
    with page.expect_download() as info:click('export-progress')
    exported=json.loads(info.value.path().read_text(encoding='utf8'))
    assert exported['poc']['_handoff']==note
    assert exported['theme']=='dark'
    page.once('dialog',lambda d:d.accept());page.locator('#import-progress').set_input_files(info.value.path())
    page.wait_for_function("document.getElementById('toast').textContent.includes('已匯入')")
    assert json.loads(raw())['poc']['_handoff']==note
    assert page.locator('html').get_attribute('data-theme')=='dark'
    # Structurally valid imported stale answers must not become current decisions.
    malicious={**exported,'poc':{'_flow':{'version':1,'answers':{'task':'text','textGoal':'transcribe','visibility':'clear','data':'few','unit':'mm','calibration':'none'},'confirmed':['task','unit','calibration','textGoal','visibility','data','bogus'],'current':''}}}
    backup();page.once('dialog',lambda d:d.accept())
    page.locator('#import-progress').set_input_files({'name':'stale.json','mimeType':'application/json','buffer':json.dumps(malicious).encode()})
    page.wait_for_function("document.querySelector('#poc-result-title')?.textContent.includes('文字')")
    assert '校正' not in page.locator('#poc-result').inner_text()
    assert page.locator('#poc-model').count()==0
    assert not errors,errors
    results.append({'audit':'dirty selection/reload, dirty note/immediate export/reload, dark theme/export/import, stale branch import','passed':True,'page_errors':errors})
    browser.close()
(W/'recheck-reliability-attempt2-evidence.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(results,ensure_ascii=False),flush=True)

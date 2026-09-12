from pathlib import Path
from playwright.sync_api import sync_playwright
import json,hashlib,re
W=Path(__file__).resolve().parent;C=W.parents[1];rows=[]
with sync_playwright() as p:
 b=p.chromium.launch(channel='msedge',headless=True)
 for route in ['interactive-learning.html','docs/index.html']:
  for width,height in [(1440,1000),(390,844)]:
   context=b.new_context(viewport={'width':width,'height':height});page=context.new_page()
   page.goto('http://127.0.0.1:8000/'+route+'#view=poc');page.locator('#poc-task').wait_for();tag=('docs' if route.startswith('docs') else 'course')+f'-{width}'
   page.screenshot(path=str(W/f'after-{tag}-empty.png'),full_page=True)
   page.locator('[data-action="fill-poc-example"]').click()
   page.wait_for_function("!document.querySelector('.toast').classList.contains('show')")
   for i in range(3):
    page.locator('.poc-step-nav button').nth(i).click();page.evaluate('document.activeElement.blur(); window.scrollTo(0,0)');page.screenshot(path=str(W/f'after-{tag}-step{i+1}.png'),full_page=True)
    rows.append(dict(route=route,width=width,step=i+1,overflow=page.evaluate('document.documentElement.scrollWidth>innerWidth'),visible_panels=page.locator('[data-poc-panel]:visible').count()))
   page.locator('[data-action="poc-preview"]').first.click();page.evaluate('document.activeElement.blur(); window.scrollTo(0,0)');page.screenshot(path=str(W/f'after-{tag}-preview.png'),full_page=True)
   if width==1440 and route.startswith('docs'):page.pdf(path=str(W/'poc-example.pdf'),format='A4')
   context.close()
 # Text corrections: all affected topics, both routes. No regenerated PNG claims.
 topics=json.loads((W/'content-changes.json').read_text(encoding='utf8'))['mechanism_topics']
 page=b.new_page(viewport={'width':1440,'height':1000})
 for route in ['interactive-learning.html','docs/index.html']:
  for id in topics:
   page.goto('http://127.0.0.1:8000/'+route+'#view=lesson&lesson='+id)
   page.locator('main details').evaluate_all('(xs)=>xs.forEach(x=>x.open=true)')
   chain=page.locator('.causal-chain').first
   rows.append(dict(route=route,topic=id,chain_visible=chain.is_visible(),text=chain.inner_text()))
   if route.startswith('docs') and id in ['det-dino-detector','resnet','yolo-world','dinov2','yoloe']:
    page.add_style_tag(content='.topbar,.skip-link{visibility:hidden!important}')
    chain.screenshot(path=str(W/f'after-{id}-causal.png'))
 b.close()
(W/'page-checks.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
data=json.loads(re.search(r'<script id="course-data" type="application/json">(.*?)</script>',(C/'docs/index.html').read_text(encoding='utf8'),re.S)[1]);ts={t['id']:t for t in data['topics']}
assert not [id for id,t in ts.items() if t['teachingStory']['mechanism_steps'][0]['body']==t['summary']]
assert ts['det-dino-detector']['slides'][2]['label']=='訓練時如何學會區分'
assert '每個候選物件的框' not in ts['det-dino-detector']['takeaway']
assert (C/'interactive-learning.html').read_bytes()==(C/'docs/index.html').read_bytes()
(W/'content-validation.json').write_text(json.dumps(dict(html_sha256=hashlib.sha256((C/'docs/index.html').read_bytes()).hexdigest(),summary_as_step0=0,dino_label=ts['det-dino-detector']['slides'][2]['label'],dino_takeaway=ts['det-dino-detector']['takeaway'],topics=len(ts),course_docs_equal=True),ensure_ascii=False,indent=2),encoding='utf8')
print('Saved 20 PoC screenshots; 38 lesson routes; content checks passed.')

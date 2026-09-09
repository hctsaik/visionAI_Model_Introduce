from pathlib import Path
import sys,json
from playwright.sync_api import sync_playwright
W=Path(__file__).resolve().parent;C=W.parents[1];sys.path.insert(0,str(C/'tools'))
from supporting_lessons import load_lessons
lessons=load_lessons(C);rows=[];O=W/'final-pages';O.mkdir(exist_ok=True)
with sync_playwright() as p:
 b=p.chromium.launch(channel='msedge',headless=True)
 for name,route in [('course','interactive-learning.html'),('docs','docs/index.html')]:
  for view in lessons:
   for width in [1440,360]:
    page=b.new_page(viewport={'width':width,'height':1000 if width==1440 else 800})
    page.goto('http://127.0.0.1:8000/'+route+'#view='+view,wait_until='networkidle')
    lesson=lessons[view];root=page.locator('.workplace-lesson');text=root.inner_text()
    assert lesson['title'] in text and lesson['intro'] in text
    for ch in lesson['chapters']:
     card=page.locator('#'+ch['id']);copy=card.inner_text()
     for field in ['case','principle','tradeoff','question']:assert ch[field] in copy
     for point in ch['points']:assert point in copy
     card.locator('details').evaluate('(e)=>e.open=true');assert ch['answer'] in card.inner_text();card.locator('details').evaluate('(e)=>e.open=false')
     fig=card.locator('figure');fig.locator('img').evaluate('(i)=>{i.loading="eager";return i.decode()}')
     fig.evaluate('(e)=>window.scrollTo({top:scrollY+e.getBoundingClientRect().top-92,behavior:"instant"})');page.wait_for_timeout(200)
     assert fig.bounding_box()['y']>=90
     page.screenshot(path=str(O/f'{name}-{view}-{width}-{ch["id"]}-top.png'))
     if width==360:
      fig.evaluate('(e)=>window.scrollTo({top:scrollY+e.getBoundingClientRect().bottom-innerHeight+20,behavior:"instant"})');page.wait_for_timeout(200)
      page.screenshot(path=str(O/f'{name}-{view}-{width}-{ch["id"]}-bottom.png'))
    rows.append({'route':route,'view':view,'width':width,'markdown_copy_matches':True,'stable_image_top_clear':3})
    page.close()
 b.close()
(W/'final-page-checks.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
print('8 final states: canonical Markdown rendered,24 stable image tops clear,12 mobile bottoms saved')

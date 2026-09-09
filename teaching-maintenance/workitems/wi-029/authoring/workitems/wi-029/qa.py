import json,hashlib,urllib.request,sys
from pathlib import Path
from playwright.sync_api import sync_playwright
W=Path(__file__).resolve().parent;C=W.parents[1];O=W/'qa';O.mkdir(exist_ok=True)
records=[]
with sync_playwright() as p:
 b=p.chromium.launch(channel='msedge',headless=True)
 for route,name in [('interactive-learning.html','course'),('docs/index.html','docs')]:
  for view in ['foundations','production']:
   for width,height in [(1440,1000),(390,844),(360,800)]:
    page=b.new_page(viewport={'width':width,'height':height});errors=[]
    page.on('pageerror',lambda e:errors.append(str(e)))
    page.goto(f'http://127.0.0.1:8000/{route}#view={view}',wait_until='networkidle')
    page.evaluate('document.fonts.ready')
    prefix=f'{name}-{view}-{width}'
    page.screenshot(path=str(O/(prefix+'-top.png')))
    cards=page.locator('.workplace-chapter');assert cards.count()==3
    imgs=[]
    for n in range(3):
     card=cards.nth(n);fig=card.locator('figure');im=fig.locator('img')
     fig.scroll_into_view_if_needed();im.evaluate('(i)=>i.decode()')
     state=im.evaluate('(i)=>({src:i.currentSrc,natural:[i.naturalWidth,i.naturalHeight],box:i.getBoundingClientRect().toJSON()})')
     assert 'wi029-' in state['src'] and ('mobile' if width<700 else 'desktop') in state['src']
     assert state['box']['width']<=width
     fig.screenshot(path=str(O/(prefix+f'-figure{n+1}.png')))
     card.locator('.workplace-explanation').screenshot(path=str(O/(prefix+f'-text{n+1}.png')))
     fig.get_by_role('button',name='放大完整圖',exact=True).click()
     page.locator('#lightbox[open]').wait_for();page.locator('#lightbox img').evaluate('(i)=>i.decode()')
     assert page.locator('#lightbox img').evaluate('(i)=>i.currentSrc')==state['src']
     page.keyboard.press('Escape');assert page.locator('#lightbox[open]').count()==0
     answer=card.locator('.workplace-exercise details');answer.locator('summary').click()
     assert answer.get_attribute('open') is not None and len(answer.locator('p').inner_text())>40
     answer.screenshot(path=str(O/(prefix+f'-answer{n+1}.png')))
     answer.locator('summary').click();imgs.append(state)
    if view=='production':
     result=page.locator('.production-example-result')
     assert '59 件' in result.inner_text() and '19.7 分鐘' in result.inner_text()
     page.locator('[data-action="production-candidate"][data-candidate="B"]').click()
     assert '140 件' in result.inner_text() and '46.7 分鐘' in result.inner_text() and '81 件' in result.inner_text()
     assert page.locator('[data-candidate="B"]').get_attribute('aria-pressed')=='true'
     page.locator('.workplace-example').screenshot(path=str(O/(prefix+'-comparison.png')))
     page.locator('[data-candidate="A"]').focus();page.keyboard.press('Enter')
     assert '59 件' in result.inner_text()
    else:
     page.locator('.workplace-comparison').screenshot(path=str(O/(prefix+'-comparison.png')))
    legacy=page.locator('.workplace-legacy');assert legacy.get_attribute('open') is None
    legacy.locator('summary').first.click();assert legacy.locator(':scope > details').count()==(18 if view=='foundations' else 24)
    item=legacy.locator(':scope > details').first;item.locator('summary').first.click()
    assert item.locator('img').count()>0
    legacy.locator('summary').first.click()
    page.locator('.workplace-toc a').nth(2).click();page.wait_for_timeout(150)
    assert page.url.endswith('#view='+view)
    assert not page.evaluate('document.documentElement.scrollWidth>innerWidth+1')
    text=page.locator('.workplace-lesson').inner_text();(O/(prefix+'.txt')).write_text(text,encoding='utf-8')
    page.locator('.workplace-handoff').screenshot(path=str(O/(prefix+'-handoff.png')))
    page.locator('.workplace-handoff [data-action="go"]').first.click()
    assert page.url.endswith('#view='+('production' if view=='foundations' else 'poc'))
    assert not errors,errors
    records.append({'route':route,'view':view,'viewport':[width,height],'images':imgs,'zoom':3,'selftests':3,'toc_route':True,'comparison':True,'archive':True,'navigation':True,'overflow':False,'page_errors':errors})
    page.close()
 # Explicit responsive zoom after viewport changes, without route rerender.
 page=b.new_page(viewport={'width':1440,'height':1000});page.goto('http://127.0.0.1:8000/docs/index.html#view=foundations')
 page.set_viewport_size({'width':360,'height':800})
 fig=page.locator('.workplace-figure').first;fig.scroll_into_view_if_needed();fig.locator('img').evaluate('(i)=>i.decode()')
 fig.get_by_role('button').click();page.locator('#lightbox img').evaluate('(i)=>i.decode()')
 assert 'mobile' in page.locator('#lightbox img').get_attribute('src');page.keyboard.press('Escape');b.close()
manifest=json.loads((C/'_course_content/supporting-lessons/assets.json').read_text(encoding='utf-8'));checks=[]
for prefix in ['', 'docs/']:
 for row in manifest.values():
  for mode in ['desktop','mobile']:
   a=row[mode];url='http://127.0.0.1:8000/'+prefix+a['path'];data=urllib.request.urlopen(url).read();assert hashlib.sha256(data).hexdigest()==a['sha256'];checks.append(url)
 for view in ['foundations','production']:
  rel=f'_course_content/supporting-lessons/{view}.md';assert urllib.request.urlopen('http://127.0.0.1:8000/'+prefix+rel).read()==(C/rel).read_bytes()
(W/'validation-summary.json').write_text(json.dumps({'states':records,'image_http_hashes':checks,'markdown_http':4,'responsive_zoom':True},ensure_ascii=False,indent=2),encoding='utf-8')
print('PASS:12 states,36 zoom/answers,24 PNG hashes,4 Markdown bodies,responsive zoom,comparisons/navigation/archive')

from pathlib import Path
import json
from playwright.sync_api import sync_playwright
W=Path(__file__).resolve().parent;U='https://hctsaik.github.io/visionAI_Model_Introduce/'
r={}
with sync_playwright() as pw:
 b=pw.chromium.launch(channel='msedge',headless=True)
 p=b.new_page(viewport={'width':390,'height':844},reduced_motion='reduce');p.set_default_timeout(10000)
 errors=[];p.on('pageerror',lambda e:errors.append(str(e)))
 p.goto(U,timeout=25000);p.locator('#global-search').fill('PatchCore')
 card=p.locator('main [data-action="lesson"][data-topic="ad-patchcore"]').first;card.wait_for();card.click();p.locator('#lesson-title').wait_for();r['search']=p.locator('#lesson-title').inner_text();assert r['search']=='PatchCore'
 nav=p.locator('[data-action="toggle-nav"]');nav.click();assert nav.get_attribute('aria-expanded')=='true'
 p.locator('#course-nav [data-action="go"]').first.click();r['drawer_closed']=nav.get_attribute('aria-expanded')=='false';assert r['drawer_closed']
 p.locator('[data-action="toggle-theme"]').click();theme=p.locator('html').get_attribute('data-theme');p.reload(timeout=25000);r['theme_persists']=p.locator('html').get_attribute('data-theme')==theme;assert r['theme_persists']
 p.goto(U+'#view=lesson&lesson=ad-patchcore&slide=1',timeout=25000);p.locator('#lesson-title').wait_for()
 fig=p.locator('main [data-action="open-concept"]').first.locator('xpath=ancestor::figure[1]');fig.evaluate('(e)=>scrollTo(0,e.getBoundingClientRect().top+scrollY-85)')
 fig.locator('img').evaluate_all('es=>es.forEach(e=>e.loading="eager")')
 p.wait_for_function('''fig=>{const a=[...fig.querySelectorAll('img')].filter(e=>e.getBoundingClientRect().width>0);return a.length>0&&a.every(e=>e.complete&&e.naturalWidth>0)}''',arg=fig.element_handle(),timeout=20000)
 p.screenshot(path=str(W/'recheck-public-mobile-title.png'));r['figure_top']=fig.bounding_box()['y']
 p.locator('main [data-action="open-concept"]').first.click();wrap=p.locator('.lightbox-image-wrap');wrap.wait_for()
 p.wait_for_function('''()=>{const e=document.querySelector('.lightbox-image-wrap img');return e&&e.complete&&e.naturalWidth>0}''',timeout=20000)
 r['zoom_start']=wrap.evaluate('(e)=>({left:e.firstElementChild.getBoundingClientRect().left,top:e.firstElementChild.getBoundingClientRect().top,boxLeft:e.getBoundingClientRect().left,boxTop:e.getBoundingClientRect().top})')
 wrap.evaluate('e=>{e.scrollLeft=e.scrollWidth;e.scrollTop=e.scrollHeight}')
 r['zoom_end']=wrap.evaluate('(e)=>({right:e.firstElementChild.getBoundingClientRect().right,bottom:e.firstElementChild.getBoundingClientRect().bottom,boxRight:e.getBoundingClientRect().right,boxBottom:e.getBoundingClientRect().bottom})')
 assert r['zoom_start']['left']>=r['zoom_start']['boxLeft']-1 and r['zoom_start']['top']>=r['zoom_start']['boxTop']-1
 assert r['zoom_end']['right']<=r['zoom_end']['boxRight']+1 and r['zoom_end']['bottom']<=r['zoom_end']['boxBottom']+1
 p.screenshot(path=str(W/'recheck-public-mobile-zoom-end.png'));p.keyboard.press('Escape');assert not wrap.is_visible();r['escape_closed']=True;r['page_errors']=errors;assert not errors;b.close()
(W/'recheck-public-mobile-ui.json').write_text(json.dumps(r,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(r,ensure_ascii=False))

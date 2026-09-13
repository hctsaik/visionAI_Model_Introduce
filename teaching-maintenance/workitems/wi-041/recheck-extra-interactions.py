from pathlib import Path
import json,time
from playwright.sync_api import sync_playwright
O=Path('teaching-images/vision-ai-model-selection/workitems/wi-041');U='http://127.0.0.1:8014/docs/index.html';out=[]
with sync_playwright() as pw:
 b=pw.chromium.launch(channel='msedge',headless=True)
 for w in [1440,390]:
  c=b.new_context(viewport={'width':w,'height':1000},reduced_motion='reduce');p=c.new_page();p.set_default_timeout(20000);p.goto(U);r={'width':w};p.locator('#global-search').fill('PatchCore');p.wait_for_timeout(800);r['search_url']=p.url;r['search_matches']=p.locator('main [data-action="lesson"][data-topic="ad-patchcore"]').count();assert r['search_matches']>0
  p.locator('main [data-action="lesson"][data-topic="ad-patchcore"]').first.click();p.locator('#lesson-title').wait_for();r['search_open']=p.locator('#lesson-title').inner_text()
  if w==390:
   n=p.locator('[data-action="toggle-nav"]');n.click();r['nav_open']=n.get_attribute('aria-expanded');assert r['nav_open']=='true';p.locator('#course-nav [data-action="go"]').first.click();r['nav_closed']=n.get_attribute('aria-expanded')
  p.locator('[data-action="toggle-theme"]').click();r['theme']=p.locator('html').get_attribute('data-theme');p.reload();r['theme_reload']=p.locator('html').get_attribute('data-theme');assert r['theme']==r['theme_reload'];p.locator('[data-action="toggle-theme"]').click()
  p.goto(U+'#view=lesson&lesson=ad-patchcore&slide=1');p.locator('#lesson-title').wait_for();fig=p.locator('main [data-action="open-concept"]').first.locator('xpath=ancestor::figure[1]');fig.evaluate('(e)=>scrollTo(0,e.getBoundingClientRect().top+scrollY-85)');p.wait_for_timeout(1500);r['figure_top']=fig.bounding_box()['y'];p.screenshot(path=str(O/f'recheck-title-reachable-{w}.png'));r['figure_images']=fig.locator('img').evaluate_all('async es=>{await Promise.all(es.map(e=>e.decode().catch(()=>{})));return es.map(e=>({src:e.currentSrc,width:e.naturalWidth,complete:e.complete}))}');fig.screenshot(path=str(O/f'recheck-stable-patchcore-{w}.png'))
  p.locator('main [data-action="open-concept"]').first.click();wrap=p.locator('.lightbox-image-wrap');r['zoom_start']=wrap.evaluate('(e)=>({left:e.firstElementChild.getBoundingClientRect().left,boxLeft:e.getBoundingClientRect().left})');wrap.evaluate('e=>{e.scrollLeft=e.scrollWidth;e.scrollTop=e.scrollHeight}');r['zoom_end']=wrap.evaluate('(e)=>({right:e.firstElementChild.getBoundingClientRect().right,boxRight:e.getBoundingClientRect().right,bottom:e.firstElementChild.getBoundingClientRect().bottom,boxBottom:e.getBoundingClientRect().bottom})');p.screenshot(path=str(O/f'recheck-zoom-end-{w}.png'));p.keyboard.press('Escape');out.append(r);(O/'recheck-extra-interactions.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8');print(w,'ok',flush=True);c.close()
 b.close()

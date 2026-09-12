from stable_image import READY
import json,sys,traceback
from pathlib import Path
from playwright.sync_api import sync_playwright
W=Path(__file__).resolve().parent; C=W.parents[1]
slugs=sys.argv[1:] or ['clip','siglip']
with sync_playwright() as pw:
 b=pw.chromium.launch(channel='msedge',headless=True)
 for slug in slugs:
  O=W/'pages'/slug; O.mkdir(parents=True,exist_ok=True); records=[]
  topic=json.loads((C/'_course_content/topics'/f'{slug}.json').read_text(encoding='utf-8'))
  for route in ['interactive-learning.html','docs/index.html']:
   name='course' if route.startswith('interactive') else 'docs'
   for width,height in [(1440,1000),(360,800)]:
    p=b.new_page(viewport={'width':width,'height':height});p.set_default_timeout(12000)
    errors=[];p.on('pageerror',lambda e:errors.append(str(e)))
    row=dict(topic=slug,route=route,width=width,errors=errors,images=[],zoom_checks=0)
    prefix=f'{name}-{width}'
    try:
     p.goto(f'http://127.0.0.1:8000/{route}#view=lesson&lesson={slug}&slide=1',wait_until='networkidle');p.evaluate('document.fonts.ready')
     assert p.locator('.beginner-visual').count()==len(topic['beginner_path']['visuals'])
     p.screenshot(path=str(O/f'{prefix}-top.png'))
     for i,card in enumerate(p.locator('.beginner-visual').all(),1):
      fig=card.locator('figure').first;fig.scroll_into_view_if_needed()
      im=fig.locator('img:visible');assert im.count()==1;im.evaluate(READY)
      state=im.evaluate('(i)=>({src:i.currentSrc,nw:i.naturalWidth,nh:i.naturalHeight,box:i.getBoundingClientRect().toJSON()})')
      assert state['box']['width']<=width
      if width==360:assert state['nh']>state['nw']
      state['kind']=f'main-{i}';row['images'].append(state)
      fig.screenshot(path=str(O/f'{prefix}-main-{i}.png'),style='.topbar,.skip-link{visibility:hidden!important}')
      card.locator('button[data-action="open-concept"]').first.click();p.locator('#lightbox[open]').wait_for()
      p.locator('#lightbox img').evaluate(READY);p.keyboard.press('Escape');assert not p.locator('#lightbox[open]').count();row['zoom_checks']+=1
     answer=p.get_by_text('看解釋與可接受的取捨',exact=True);answer.click()
     assert topic['micro_example']['reveal'] in answer.locator('..').inner_text();row['answer']=True
     answer.locator('..').screenshot(path=str(O/f'{prefix}-answer.png'))
     (O/f'{prefix}-reading.txt').write_text(p.locator('main').inner_text(),encoding='utf-8')
     for summary in p.locator('main details > summary').all():
      if summary.is_visible() and not summary.locator('..').evaluate('(e)=>e.open'):summary.click()
     (O/f'{prefix}-expanded.txt').write_text(p.locator('main').inner_text(),encoding='utf-8')
     figs=p.locator('.lesson-step figure');assert figs.count()==4
     for i,fig in enumerate(figs.all(),1):
      fig.scroll_into_view_if_needed();im=fig.locator('img');im.evaluate(READY)
      state=im.evaluate('(i)=>({src:i.currentSrc,nw:i.naturalWidth,nh:i.naturalHeight,box:i.getBoundingClientRect().toJSON()})')
      assert 'WI033-' in state['src'];assert ('mobile' if width==360 else 'desktop') in state['src']
      assert abs(state['box']['height']/state['box']['width']-state['nh']/state['nw'])<0.01
      state['kind']=f'engineering-{i}';row['images'].append(state);fig.screenshot(path=str(O/f'{prefix}-engineering-{i}.png'),style='.topbar,.skip-link{visibility:hidden!important}')
      fig.locator('button[data-action="open-lightbox"]').click()
      p.locator('#lightbox[open]').wait_for();p.locator('#lightbox img').evaluate(READY)
      zoom=p.locator('#lightbox img').evaluate('(i)=>({src:i.currentSrc,w:i.getBoundingClientRect().width,h:i.getBoundingClientRect().height})')
      assert zoom['w']>width if width==360 else zoom['w']==1672
      assert 'mobile' in zoom['src'] if width==360 else 'desktop' in zoom['src']
      p.locator('.lightbox-image-wrap').evaluate('(e)=>{e.scrollTop=e.scrollHeight;e.scrollLeft=e.scrollWidth}')
      if name=='docs':p.screenshot(path=str(O/f'{prefix}-zoom-{i}-end.png'))
      p.keyboard.press('Escape');assert not p.locator('#lightbox[open]').count();row['zoom_checks']+=1
     hand=p.locator('.engineer-handoff');hand.scroll_into_view_if_needed();p.screenshot(path=str(O/f'{prefix}-handoff.png'))
     row['overflow']=p.evaluate('document.documentElement.scrollWidth>innerWidth+1');assert not row['overflow']
     nxt=p.locator('.lesson-footer button').last;old=p.url;nxt.click();p.wait_for_timeout(200);assert p.url!=old;row['navigation']=True
     assert not errors;row['complete']=True
    except Exception as e:
     row.update(complete=False,failure=str(e),trace=traceback.format_exc());p.screenshot(path=str(O/f'{prefix}-failure.png'))
    records.append(row);p.close()
   (O/'report.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
  print(slug,[(r['route'],r['width'],r['complete'],r.get('failure','')[:150]) for r in records],flush=True)
 b.close()

from stable_image import READY
import json,hashlib,traceback
from pathlib import Path
from playwright.sync_api import sync_playwright
W=Path(__file__).resolve().parent;C=W.parents[1];records=[]
with sync_playwright() as pw:
 b=pw.chromium.launch(channel='msedge',headless=True)
 for slug in ['ad-anomalydino','ad-efficientad']:
  out=W/'deep'/slug;out.mkdir(parents=True,exist_ok=True)
  for route in ['interactive-learning.html','docs/index.html']:
   name='course' if route.startswith('interactive') else 'docs'
   for width in [1440,360]:
    p=b.new_page(viewport={'width':width,'height':1000 if width==1440 else 800});p.set_default_timeout(15000)
    errors=[];p.on('pageerror',lambda e:errors.append(str(e)))
    p.goto(f'http://127.0.0.1:8000/{route}#view=lesson&lesson={slug}&slide=1',wait_until='networkidle')
    p.evaluate("document.querySelector('.model-deep-dive').closest('details').open=true");p.evaluate('document.fonts.ready')
    assert p.locator('.deep-dive-chapter').count()==8
    for n,ch in enumerate(p.locator('.deep-dive-chapter').all(),1):
     row=dict(topic=slug,route=route,width=width,chapter=n,views=[],zooms=0)
     try:
      for q in ch.locator('details > summary').all():
       if q.is_visible() and not q.locator('..').evaluate('(e)=>e.open'):q.click()
      (out/f'{name}-{width}-chapter-{n}.txt').write_text(ch.inner_text(),encoding='utf-8')
      panels=ch.locator('.reading-view-panel');count=panels.count() or 1
      for v in range(count):
       if panels.count():
        buttons=ch.locator('[data-action="reading-view"]')
        if buttons.count():buttons.nth(v).click()
        fig=panels.nth(v).locator('figure')
       else:fig=ch.locator('figure').first
       fig.scroll_into_view_if_needed();p.wait_for_timeout(120)
       for im in fig.locator('img:visible,object:visible').all():im.evaluate(READY)
       for im in fig.locator('svg:visible image').all():im.evaluate('(i)=>new Promise((r,j)=>{const a=new Image();a.onload=r;a.onerror=j;a.src=i.href.baseVal})')
       key=f'{name}-{width}-c{n:02}-v{v+1:02}.png';fig.screenshot(path=str(out/key),style='.topbar,.skip-link{visibility:hidden!important}')
       state=fig.locator('img:visible').evaluate_all('(xs)=>xs.map(i=>({src:i.currentSrc,nw:i.naturalWidth,nh:i.naturalHeight,box:i.getBoundingClientRect().toJSON()}))')
       row['views'].append(dict(screenshot=key,images=state,box=fig.bounding_box()))
       for st in state:
        assert st['nw']>0
        if 'wi033-' in st['src'] and width==360:assert st['nh']>st['nw'] and 'mobile' in st['src']
       zoom=fig.locator('[data-action="open-concept"]:visible')
       if zoom.count():
        zoom.first.click();p.locator('#lightbox[open]').wait_for()
        try:
         media=p.locator('#lightbox img:visible,#lightbox object:visible')
         assert media.count()>0
         for im in media.all():im.evaluate(READY)
         row['zooms']+=1
        finally:p.keyboard.press('Escape')
      assert not p.evaluate('document.documentElement.scrollWidth>innerWidth+1');assert not errors
      row['complete']=True
     except Exception as e:
      row.update(complete=False,failure=str(e),trace=traceback.format_exc())
      if p.locator('#lightbox[open]').count():p.keyboard.press('Escape')
     records.append(row)
    p.close();(W/'batch2-deep-report.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
    print(slug,name,width,[(r['chapter'],r['complete']) for r in records[-8:]],flush=True)
 b.close()
assert all(r['complete'] for r in records)

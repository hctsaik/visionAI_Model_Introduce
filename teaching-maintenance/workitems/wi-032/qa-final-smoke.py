import json
from pathlib import Path
from playwright.sync_api import sync_playwright
W=Path(__file__).resolve().parent;C=W.parents[1];out=[]
new=list(json.loads((W/'lesson-content.json').read_text(encoding='utf-8')))
with sync_playwright() as pw:
 b=pw.chromium.launch(channel='msedge',headless=True)
 for slug in new+['resnet','raft','ad-patchcore']:
  for route in ['interactive-learning.html','docs/index.html']:
   p=b.new_page(viewport={'width':390,'height':844});p.set_default_timeout(15000);errors=[];p.on('pageerror',lambda e:errors.append(str(e)))
   p.goto(f'http://127.0.0.1:8000/{route}#view=lesson&lesson={slug}&slide=4',wait_until='networkidle')
   fig=p.locator('.lesson-step').nth(3).locator('figure');assert fig.is_visible();fig.scroll_into_view_if_needed();im=fig.locator('img');im.evaluate('(i)=>i.decode()')
   state=im.evaluate('(i)=>({src:i.currentSrc,w:i.naturalWidth,h:i.naturalHeight})')
   if slug in new:assert 'mobile.png' in state['src'] and 'WI032-' in state['src']
   else:assert 'WI032-' not in state['src']
   fig.locator('button').click();p.locator('#lightbox[open]').wait_for();p.locator('#lightbox img').evaluate('(i)=>i.decode()')
   assert p.locator('[data-action="lightbox-next"]').is_disabled()
   p.locator('[data-action="lightbox-prev"]').click();p.locator('#lightbox img').evaluate('(i)=>i.decode()')
   assert '3 / 4' in p.locator('.lightbox-footer').inner_text()
   p.locator('[data-action="lightbox-next"]').click();p.locator('#lightbox img').evaluate('(i)=>i.decode()')
   assert '4 / 4' in p.locator('.lightbox-footer').inner_text();p.keyboard.press('Escape');assert not p.locator('#lightbox[open]').count()
   links=[]
   for link in p.locator('.retained-evidence a').all():
    url=link.evaluate('(a)=>a.href');resp=p.request.get(url);assert resp.ok;links.append(url)
   assert not p.evaluate('document.documentElement.scrollWidth>innerWidth+1');assert not errors
   if slug in new:
    O=W/'pages'/slug;fig.screenshot(path=str(O/f"final-{'course' if route.startswith('interactive') else 'docs'}-390-engineering-4.png"),style='.topbar,.skip-link{visibility:hidden!important}')
    rowtext=p.locator('.engineer-handoff').inner_text()
    assert '把 SIFT warp' not in rowtext and '輸入與版本' not in rowtext # technical contracts remain collapsed
   out.append(dict(slug=slug,route=route,width=390,deep_link_visible=True,zoom_prev_next_escape=True,retained_links=links,legacy_fallback=slug not in new,errors=errors));p.close()
 b.close()
(W/'final-smoke.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print('PASS',len(out),'390px final/legacy/deep-link/lightbox navigation states')

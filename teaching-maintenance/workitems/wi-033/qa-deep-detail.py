from pathlib import Path
from playwright.sync_api import sync_playwright
import json
W=Path(__file__).resolve().parent;report=[]
with sync_playwright() as pw:
 b=pw.chromium.launch(channel='msedge',headless=True)
 for slug in ['ad-efficientad','ad-anomalydino']:
  p=b.new_page(viewport={'width':360,'height':900})
  p.goto(f'http://127.0.0.1:8000/docs/index.html#view=lesson&lesson={slug}&slide=1',wait_until='networkidle')
  p.evaluate("document.querySelector('.model-deep-dive').closest('details').open=true")
  p.evaluate("document.querySelectorAll('*').forEach(e=>{if(['fixed','sticky'].includes(getComputedStyle(e).position))e.style.visibility='hidden'})")
  for n in ([4,5,6,7,8] if slug=='ad-efficientad' else [6]):
   ch=p.locator('.deep-dive-chapter').nth(n-1)
   for sm in ch.locator('details>summary').all():
    if sm.is_visible() and not sm.locator('..').evaluate('(e)=>e.open'):sm.click()
   tabs=ch.locator('[data-action="reading-view"]');count=tabs.count() or 1
   for v in range(count):
    if tabs.count():tabs.nth(v).click()
    fig=(ch.locator('.reading-view-panel').nth(v).locator('figure') if tabs.count() else ch.locator('figure').first)
    steps=fig.locator('.deep-dive-mobile-steps li');els=steps.all() if steps.count() else [fig]
    for i,el in enumerate(els):
     el.scroll_into_view_if_needed();p.wait_for_timeout(500)
     name=f'detail-c{n:02}-v{v+1:02}-part{i+1}.png';el.screenshot(path=str(W/'deep'/slug/name))
     report.append(dict(topic=slug,chapter=n,view=v+1,part=i+1,path=f'deep/{slug}/{name}'))
  p.close()
 b.close()
(W/'deep-detail-report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print('Saved',len(report),'detail captures')

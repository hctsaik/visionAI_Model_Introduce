from pathlib import Path
from playwright.sync_api import sync_playwright
import json
W=Path(__file__).resolve().parent
with sync_playwright() as pw:
 b=pw.chromium.launch(channel='msedge',headless=True)
 p=b.new_page(viewport={'width':360,'height':800})
 p.goto('http://127.0.0.1:8000/docs/index.html#view=lesson&lesson=ad-efficientad&slide=1',wait_until='networkidle')
 p.evaluate("document.querySelector('.model-deep-dive').closest('details').open=true")
 e=p.locator('.deep-dive-mobile-steps li').first;e.scroll_into_view_if_needed()
 print(json.dumps(e.locator('svg,image').evaluate_all('xs=>xs.map(x=>({tag:x.tagName,html:x.outerHTML,box:x.getBoundingClientRect().toJSON(),width:getComputedStyle(x).width,height:getComputedStyle(x).height,viewBox:x.viewBox?.baseVal}))'),ensure_ascii=False,indent=2))
 p.wait_for_timeout(1500);e.screenshot(path=str(W/'crop-diagnostic.png'))
 b.close()

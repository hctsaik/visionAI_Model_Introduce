from playwright.sync_api import sync_playwright
from pathlib import Path
W=Path(__file__).resolve().parent
with sync_playwright() as p:
 b=p.chromium.launch(channel='msedge',headless=True);page=b.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto('http://127.0.0.1:8000/interactive-learning.html#view=lesson&lesson=ad-patchcore&slide=1',wait_until='networkidle')
 print(page.locator('body').inner_text()[:4500]);print(errors);page.screenshot(path=str(W/'baseline-debug.png'));b.close()

from pathlib import Path
from playwright.sync_api import sync_playwright
W=Path(__file__).resolve().parent
with sync_playwright() as p:
 b=p.chromium.launch(channel='msedge',headless=True,args=['--disable-gpu'])
 page=b.new_page(viewport={'width':1672,'height':941})
 f=W/'det-grounding-dino-interface-engineering-2-r02-desktop.svg'
 page.goto(f.as_uri());page.evaluate('document.fonts.ready');page.wait_for_timeout(2000)
 page.screenshot(path=str(W/'ground-render-diagnostic-fresh.png'))
 print(page.locator('svg > g').nth(2).locator('rect').count())
 b.close()

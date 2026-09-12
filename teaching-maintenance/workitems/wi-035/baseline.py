from pathlib import Path
from playwright.sync_api import sync_playwright
import json,hashlib
W=Path(__file__).resolve().parent; C=W.parents[1]
with sync_playwright() as p:
 b=p.chromium.launch(channel='msedge',headless=True)
 page=b.new_page(viewport={'width':1440,'height':1000})
 for name,url in [('public','https://hctsaik.github.io/visionAI_Model_Introduce/#view=poc'),('local','http://127.0.0.1:8000/docs/index.html#view=poc')]:
  page.goto(url,wait_until='networkidle');page.locator('#poc-task').wait_for()
  page.screenshot(path=str(W/f'before-{name}.png'),full_page=True)
  (W/f'before-{name}.txt').write_text(page.locator('main').inner_text(),encoding='utf8')
  if name=='public': (W/'public-baseline.html').write_text(page.content(),encoding='utf8')
 b.close()
print('Saved public/local baseline screenshots and text.')

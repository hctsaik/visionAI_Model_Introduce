from pathlib import Path
from playwright.sync_api import sync_playwright
W=Path(__file__).resolve().parent
with sync_playwright() as p:
 b=p.chromium.launch(channel='msedge',headless=True)
 for route,name in [('interactive-learning.html','course'),('docs/index.html','docs')]:
  for width,height in [(1440,1000),(390,844)]:
   page=b.new_page(viewport={'width':width,'height':height})
   page.goto('http://127.0.0.1:8000/'+route+'#view=poc');page.locator('[data-action="fill-poc-example"]').click()
   page.locator('[data-action="poc-preview"]').filter(visible=True).first.click()
   page.wait_for_function("!document.querySelector('.toast').classList.contains('show')")
   page.evaluate('document.activeElement.blur();window.scrollTo({top:0,behavior:"instant"})')
   page.wait_for_function('window.scrollY===0')
   page.screenshot(path=str(W/f'after-{name}-{width}-preview.png'),full_page=True)
   page.close()
 b.close()
print('Refreshed four stable preview screenshots.')

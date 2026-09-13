from pathlib import Path
import json
from playwright.sync_api import sync_playwright
OUT=Path(__file__).parent
URL='http://127.0.0.1:8000/docs/index.html'
with sync_playwright() as pw:
 b=pw.chromium.launch(channel='msedge',headless=True)
 for width in [1440,390]:
  context=b.new_context(viewport={'width':width,'height':900})
  p=context.new_page()
  for name,hash in [('home',''),('lesson','#view=lesson&lesson=det-dino-detector'),('poc','#view=poc')]:
   p.goto(URL+hash);p.locator('main').wait_for();p.wait_for_timeout(300)
   (OUT/f'ux-{width}-{name}.txt').write_text(p.locator('main').inner_text(),encoding='utf8')
   p.screenshot(path=str(OUT/f'ux-{width}-{name}.png'))
   buttons=p.locator('main button').evaluate_all('(els)=>els.map(e=>({text:e.innerText,action:e.dataset.action,topic:e.dataset.topic,y:Math.round(e.getBoundingClientRect().top+scrollY)}))')
   (OUT/f'ux-{width}-{name}-buttons.json').write_text(json.dumps(buttons,ensure_ascii=False,indent=2),encoding='utf8')
   print(width,name,flush=True)
  context.close()
 b.close()

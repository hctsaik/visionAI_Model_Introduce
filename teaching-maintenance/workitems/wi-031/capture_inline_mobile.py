import json
from pathlib import Path
from playwright.sync_api import sync_playwright
W=Path(__file__).resolve().parent
todo=[]
for f in (W/'pages').glob('*/report.json'):
 rows=json.loads(f.read_text(encoding='utf-8'))
 if any(r['width']==360 and len(r['visuals'])<r.get('cards',0) for r in rows):todo.append(f.parent.name)
out=[]
with sync_playwright() as pw:
 b=pw.chromium.launch(channel='msedge',headless=True)
 for slug in todo:
  p=b.new_page(viewport={'width':360,'height':800})
  p.goto(f'http://127.0.0.1:8000/docs/index.html#view=lesson&lesson={slug}&slide=1',wait_until='networkidle')
  for i,card in enumerate(p.locator('.beginner-visual').all()):
   for j,fig in enumerate(card.locator('figure').all()):
    if fig.is_visible():
     fig.scroll_into_view_if_needed();p.wait_for_timeout(100)
     fig.screenshot(path=str(W/'pages'/slug/f'360-v{i+1}-{j+1}.png'))
  out.append({'topic':slug,'figures':p.locator('.beginner-visual figure:visible').count(),'svg':p.locator('.reading-view-mobile:visible').count()})
  p.close()
 b.close()
(W/'inline-mobile-capture.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(out)

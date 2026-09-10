import json
from pathlib import Path
from playwright.sync_api import sync_playwright
W=Path(__file__).resolve().parent;C=W.parents[1];O=W/'baseline-views';O.mkdir(exist_ok=True)
names=['frame-difference', 'background-subtraction', 'lucas-kanade', 'raft', 'bytetrack', 'convlstm', 'videomae', 'v-jepa']
with sync_playwright() as p:
 b=p.chromium.launch(channel='msedge',headless=True)
 for slug in names:
  t=json.loads((W/'baseline'/f'{slug}.json').read_text(encoding='utf-8'))
  (O/f'{slug}-text.txt').write_text('\n\n'.join([t['scenario']['body'],t['mental_model']['body']]+[v['caption'] for v in t['beginner_path']['visuals']]),encoding='utf-8')
  for width in [1440,360]:
   page=b.new_page(viewport={'width':width,'height':1000})
   page.goto(f'http://127.0.0.1:8000/interactive-learning.html#view=lesson&lesson={slug}&slide=1',wait_until='networkidle')
   fig=page.locator('.beginner-visual figure').first;fig.scroll_into_view_if_needed();page.wait_for_timeout(350)
   if fig.locator('img:visible').count(): fig.locator('img:visible').first.evaluate('(i)=>i.decode()')
   page.screenshot(path=str(O/f'{slug}-{width}.png'));page.close()
 b.close()
print('16 baseline views and eight reading texts saved')

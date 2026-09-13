from pathlib import Path
import json
from playwright.sync_api import sync_playwright
out=Path(__file__).parent
with sync_playwright() as pw:
 b=pw.chromium.launch(channel='msedge',headless=True); evidence=[]
 for width in [1440,390]:
  c=b.new_context(viewport={'width':width,'height':900});p=c.new_page();p.goto('http://127.0.0.1:8000/docs/index.html#view=poc')
  for value in ['count','fixed','clear','normal']:
   p.locator('#poc-answer').select_option(value);p.locator('[data-action="poc-next"]').click()
   evidence.append({'width':width,'after':value,'boxes':p.locator('#poc-question-title, #poc-result-title, .topbar').evaluate_all('(els)=>els.map(e=>({id:e.id,cls:e.className,text:e.innerText,top:e.getBoundingClientRect().top,bottom:e.getBoundingClientRect().bottom}))')})
  p.screenshot(path=str(out/f'ux-{width}-poc-result-viewport.png'));c.close()
 (out/'ux-focus-evidence.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2),encoding='utf8');b.close()

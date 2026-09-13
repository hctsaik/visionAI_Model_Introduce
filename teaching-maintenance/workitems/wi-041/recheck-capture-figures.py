from pathlib import Path
import json
from playwright.sync_api import sync_playwright
O=Path('teaching-images/vision-ai-model-selection/workitems/wi-041');U='http://127.0.0.1:8000/docs/index.html'
with sync_playwright() as pw:
 b=pw.chromium.launch(channel='msedge',headless=True)
 for w in [1440,390]:
  c=b.new_context(viewport={'width':w,'height':1000},reduced_motion='reduce');p=c.new_page();p.goto(U);d=json.loads(p.locator('#course-data').text_content());seen=set()
  for t in d['topics']:
   if t['family'] in seen:continue
   seen.add(t['family']);p.goto(U+'#view=lesson&lesson='+t['id']+'&slide=1');p.locator('#lesson-title').wait_for()
   e=p.locator('main [data-action="open-concept"]').first;e.locator('xpath=ancestor::figure[1]').scroll_into_view_if_needed();p.locator('main img').evaluate_all('async es=>{es.forEach(e=>e.loading="eager");await Promise.all(es.map(e=>e.decode().catch(()=>{})))}');p.wait_for_timeout(1500);e.locator('xpath=ancestor::figure[1]').screenshot(path=str(O/f'recheck-figure-{w}-{t["id"]}.png'))
   e.click();p.locator('dialog[open] img').evaluate_all('async es=>await Promise.all(es.map(e=>e.decode().catch(()=>{})))');p.screenshot(path=str(O/f'recheck-zoom-{w}-{t["id"]}.png'));p.keyboard.press('Escape');print(w,t['id'],flush=True)
  c.close()
 b.close()

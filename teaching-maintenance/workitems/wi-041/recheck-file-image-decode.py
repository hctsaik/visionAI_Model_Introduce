from pathlib import Path
import json
from playwright.sync_api import sync_playwright
O=Path('teaching-images/vision-ai-model-selection/workitems/wi-041');U=Path('teaching-images/vision-ai-model-selection/docs/index.html').resolve().as_uri();out=[]
with sync_playwright() as pw:
 b=pw.chromium.launch(channel='msedge',headless=True,args=['--allow-file-access-from-files'])
 for w in [1440,390]:
  c=b.new_context(viewport={'width':w,'height':1000},reduced_motion='reduce');p=c.new_page();p.goto(U);d=json.loads(p.locator('#course-data').text_content());seen=set()
  for t in d['topics']:
   p.goto(U+'#view=lesson&lesson='+t['id']+'&slide=1');p.locator('#lesson-title').wait_for();p.locator('main details').evaluate_all('es=>es.forEach(e=>e.open=true)');imgs=p.locator('main img').evaluate_all('async es=>{es.forEach(e=>e.loading="eager");await Promise.all(es.map(e=>e.decode().catch(()=>{})));return es.map(e=>({src:e.getAttribute("src"),ok:e.complete&&e.naturalWidth>0}))}');out.append({'width':w,'topic':t['id'],'images':imgs,'overflow':p.evaluate('document.documentElement.scrollWidth>innerWidth')})
   if t['family'] not in seen:
    seen.add(t['family']);fig=p.locator('main [data-action="open-concept"]').first.locator('xpath=ancestor::figure[1]');fig.screenshot(path=str(O/f'recheck-finalfigure-{w}-{t["id"]}.png'))
   (O/'recheck-file-image-decode.json').write_text(json.dumps(out,indent=2),encoding='utf8');print(w,t['id'],len(imgs),sum(not x['ok'] for x in imgs),flush=True)
  c.close()
 b.close()

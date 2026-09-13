from pathlib import Path
import json,re
from playwright.sync_api import sync_playwright
c=Path(__file__).parents[2];out=Path(__file__).parent
d=json.loads(re.search(r'<script id="course-data" type="application/json">(.*?)</script>',(c/'docs/index.html').read_text('utf8'),re.S)[1]);rows=[]
with sync_playwright() as pw:
 b=pw.chromium.launch(channel='msedge',headless=True);p=b.new_page()
 p.goto('http://127.0.0.1:8000/docs/index.html')
 for t in d['topics']:
  p.goto('http://127.0.0.1:8000/docs/index.html#view=lesson&lesson='+t['id']+'&slide=1',wait_until='domcontentloaded')
  p.wait_for_function('(id)=>!!document.querySelector("#primer-title-"+id)',arg=t['id'])
  p.locator('main details').evaluate_all('(els)=>els.forEach(e=>e.open=true)')
  links=p.locator('main a[href]').evaluate_all('els=>els.map(e=>({href:e.href,text:e.textContent})).filter(e=>/^https?:/.test(e.href)&&!e.href.startsWith(location.origin))')
  rows.append({'id':t['id'],'links':links})
 b.close()
(out/'recheck-external-rendered-anchors.json').write_text(json.dumps({'rows':rows,'urls':sorted({l['href'] for r in rows for l in r['links']})},ensure_ascii=False,indent=2),'utf8')
print('anchors complete',len(rows))

from pathlib import Path
import json,re,hashlib,time
from playwright.sync_api import sync_playwright
c=Path('teaching-images/vision-ai-model-selection');out=c/'workitems/wi-041';h=(c/'docs/index.html').read_text('utf8');d=json.loads(re.search(r'<script id="course-data" type="application/json">(.*?)</script>',h,re.S)[1]);result={'timestamp':time.strftime('%Y-%m-%d %H:%M:%S'),'html_sha256':hashlib.sha256(h.encode()).hexdigest(),'scope':'rendered DOM text, not visual review','rows':[]}
with sync_playwright() as pw:
 b=pw.chromium.launch(channel='msedge',headless=True);p=b.new_page(viewport={'width':1440,'height':900});p.goto('http://127.0.0.1:8000/docs/index.html')
 for t in d['topics']:
  p.goto('http://127.0.0.1:8000/docs/index.html#view=lesson&lesson='+t['id']+'&slide=1',wait_until='domcontentloaded');p.locator('#lesson-title').wait_for();default=p.locator('main').inner_text();p.locator('main details').evaluate_all('(els)=>els.forEach(e=>e.open=true)');expanded=p.locator('main').inner_text();result['rows'].append({'id':t['id'],'url':p.url,'default':default,'expanded':expanded});(out/'recheck-rendered-content.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),'utf8')
 b.close()
print('rendered',len(result['rows']))

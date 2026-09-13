from pathlib import Path
import re,json,hashlib,urllib.request
from playwright.sync_api import sync_playwright
W=Path(__file__).resolve().parent;C=W.parents[1]
url='https://hctsaik.github.io/visionAI_Model_Introduce/'
raw=urllib.request.urlopen(url,timeout=30).read();local=(C/'docs/index.html').read_bytes()
data=json.loads(re.search(rb'<script id="course-data" type="application/json">(.*?)</script>',local,re.S)[1])
print('DATA',type(data).__name__,list(data)[:12],flush=True)
result={'public_sha256':hashlib.sha256(raw).hexdigest(),'local_sha256':hashlib.sha256(local).hexdigest(),'public_equals_local':raw==local,'pages':[]}
with sync_playwright() as p:
 b=p.chromium.launch(channel='msedge',headless=True)
 for width,height in [(1440,1000),(390,844)]:
  context=b.new_context(viewport={'width':width,'height':height});page=context.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
  for route in ['home','library','poc']:
   page.goto(url+'#view='+route);page.locator('main h1').wait_for();page.wait_for_timeout(350)
   text=page.locator('main').inner_text();(W/f'public-{route}-{width}.txt').write_text(text,encoding='utf8')
   page.screenshot(path=str(W/f'public-{route}-{width}.png'),full_page=True)
   result['pages'].append({'route':route,'width':width,'height':page.locator('main').bounding_box()['height'],'overflow':page.evaluate('document.documentElement.scrollWidth>innerWidth'),'heading':page.locator('main h1').inner_text(),'visible_buttons':page.locator('main button:visible').count(),'broken_images':page.locator('main img').evaluate_all('(imgs)=>imgs.filter(i=>!i.complete||!i.naturalWidth).map(i=>i.src)')})
  result.setdefault('errors',[]).extend(errors);context.close()
 b.close()
(W/'public-inspection.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(result,ensure_ascii=False),flush=True)

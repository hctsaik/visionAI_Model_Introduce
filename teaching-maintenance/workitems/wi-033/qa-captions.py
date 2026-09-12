import json,hashlib
from pathlib import Path
from playwright.sync_api import sync_playwright
W=Path(__file__).resolve().parent;C=W.parents[1];report=[]
with sync_playwright() as pw:
 b=pw.chromium.launch(channel='msedge',headless=True)
 p=b.new_page(viewport={'width':360,'height':800});p.set_default_timeout(15000)
 for tp in sorted((C/'_course_content/topics').glob('*.json')):
  t=json.loads(tp.read_text(encoding='utf-8'))
  assert isinstance(t,dict)
  slug=tp.stem
  p.goto(f'http://127.0.0.1:8000/docs/index.html#view=lesson&lesson={slug}&slide=1',wait_until='domcontentloaded');p.evaluate('document.fonts.ready')
  caps=p.locator('.beginner-visual figcaption');assert caps.count()>=3
  checks=caps.evaluate_all('xs=>xs.map(c=>{let t=c.querySelector("strong"),b=c.querySelector("button");let a=t.getBoundingClientRect(),z=b.getBoundingClientRect();return {bottom:a.bottom,buttonTop:z.top,display:getComputedStyle(t).display,clear:a.bottom<=z.top,inside:z.right<=innerWidth}})')
  assert all(x['clear'] and x['inside'] for x in checks),(slug,checks)
  report.append(dict(topic=slug,captions=checks))
 b.close()
(W/'caption-verification.json').write_text(json.dumps(dict(html_sha256=hashlib.sha256((C/'docs/index.html').read_bytes()).hexdigest(),topics=report),ensure_ascii=False,indent=2),encoding='utf-8')
assert len(report)==58,len(report)
print('Mobile caption checks passed:',len(report),'topics,',sum(len(r['captions']) for r in report),'captions')

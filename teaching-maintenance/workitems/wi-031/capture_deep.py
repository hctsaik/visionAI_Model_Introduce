import json
from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image
W=Path(__file__).resolve().parent
data=json.loads((W/'course-data.json').read_text(encoding='utf-8'))
records=[]
with sync_playwright() as pw:
 b=pw.chromium.launch(channel='msedge',headless=True)
 for t in data['topics']:
  if not t.get('teachingStory',{}).get('deep_dive'):continue
  out=W/'deep'/t['id'];out.mkdir(parents=True,exist_ok=True)
  for width in [1440,360]:
   p=b.new_page(viewport={'width':width,'height':1000 if width==1440 else 800})
   p.set_default_timeout(15000)
   p.goto('http://127.0.0.1:8000/docs/index.html#view=lesson&lesson='+t['id']+'&slide=1',wait_until='networkidle')
   p.evaluate("document.querySelector('.model-deep-dive').closest('details').open=true")
   p.evaluate('document.fonts.ready')
   for n,ch in enumerate(p.locator('.deep-dive-chapter').all(),1):
    row={'topic':t['id'],'width':width,'chapter':n,'views':[]}
    for q in ch.locator('details > summary').all():q.click()
    (out/f'{width}-chapter-{n}.txt').write_text(ch.inner_text(),encoding='utf-8')
    panels=ch.locator('.reading-view-panel')
    count=panels.count() or 1
    for v in range(count):
     if panels.count():
      buttons=ch.locator('[data-action="reading-view"]')
      if buttons.count():buttons.nth(v).click()
      fig=panels.nth(v).locator('figure')
     else:fig=ch.locator('figure').first
     fig.scroll_into_view_if_needed()
     p.wait_for_timeout(120)
     for im in fig.locator('img:visible,object:visible').all():
      im.evaluate('(i)=>i.tagName==="IMG" ? i.decode() : new Promise(r=>i.contentDocument?.documentElement?r():i.addEventListener("load",r,{once:true}))')
     for im in fig.locator('svg:visible image').all():
      im.evaluate('(i)=>new Promise((r,j)=>{const a=new Image();a.onload=r;a.onerror=j;a.src=i.href.baseVal})')
     key=f'{width}-c{n:02}-v{v+1:02}.png';fig.screenshot(path=str(out/key))
     row['views'].append({'screenshot':key,'title':fig.inner_text(),'box':fig.bounding_box()})
    records.append(row)
   p.close()
  for width in [1440,360]:
   paths=sorted(out.glob(f'{width}-c*.png'))
   for n in range(0,len(paths),2):
    ims=[Image.open(x).convert('RGB') for x in paths[n:n+2]]
    canvas=Image.new('RGB',(sum(x.width for x in ims),max(x.height for x in ims)),'white');left=0
    for im in ims:canvas.paste(im,(left,0));left+=im.width
    canvas.save(out/f'panel-{width}-{n//2+1:02}.png')
  (W/'deep-capture.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
  print(t['id'],'deep complete',flush=True)
 b.close()

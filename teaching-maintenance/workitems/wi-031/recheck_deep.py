from pathlib import Path
from PIL import Image,ImageStat
from playwright.sync_api import sync_playwright
import json,re
W=Path(__file__).resolve().parent
bad=[p for p in (W/'deep').glob('*/1440-c??-v??.png') if max(ImageStat.Stat(Image.open(p).convert('RGB').crop((15,110,990,490))).stddev)<3]
rs=[]
with sync_playwright() as pw:
 b=pw.chromium.launch(channel='msedge',headless=True)
 p=b.new_page(viewport={'width':1440,'height':1000})
 for path in bad:
  slug=path.parent.name;c,v=map(int,re.findall(r'\d+',path.stem)[1:])
  dest=path.with_stem(path.stem+'-recheck')
  if dest.exists() and max(ImageStat.Stat(Image.open(dest).convert('RGB').crop((15,110,990,490))).stddev)>3:
   rs.append({'original':str(path.relative_to(W)),'recheck':str(dest.relative_to(W)),'stddev':ImageStat.Stat(Image.open(dest).convert('RGB').crop((15,110,990,490))).stddev});continue
  p.close();p=b.new_page(viewport={'width':1440,'height':1000})
  p.goto('http://127.0.0.1:8000/docs/index.html#view=lesson&lesson='+slug+'&slide=1',wait_until='domcontentloaded')
  p.evaluate("document.querySelector('.model-deep-dive').closest('details').open=true")
  ch=p.locator('.deep-dive-chapter').nth(c-1);ch.locator('[data-action="reading-view"]').nth(v-1).click()
  fig=ch.locator('.reading-view-panel').nth(v-1).locator('figure');fig.scroll_into_view_if_needed();p.wait_for_timeout(1800)
  dest=path.with_stem(path.stem+'-recheck');fig.screenshot(path=str(dest))
  rs.append({'original':str(path.relative_to(W)),'recheck':str(dest.relative_to(W)),'stddev':ImageStat.Stat(Image.open(dest).convert('RGB').crop((15,110,990,490))).stddev})
 b.close()
(W/'deep-recheck.json').write_text(json.dumps(rs,ensure_ascii=False,indent=2),encoding='utf-8')
for slug in {p.parent.name for p in bad}:
 paths=sorted((W/'deep'/slug).glob('1440-c*-recheck.png'))
 for n in range(0,len(paths),2):
  ims=[Image.open(x).convert('RGB') for x in paths[n:n+2]];o=Image.new('RGB',(sum(x.width for x in ims),max(x.height for x in ims)),'white');left=0
  for im in ims:o.paste(im,(left,0));left+=im.width
  o.save(W/'deep'/slug/f'recheck-panel-{n//2+1:02}.png')
print('rechecks',len(rs),'still blank',sum(max(r['stddev'])<3 for r in rs),flush=True)

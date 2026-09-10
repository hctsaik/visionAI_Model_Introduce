import json,sys,traceback
from pathlib import Path
from playwright.sync_api import sync_playwright
W=Path(__file__).resolve().parent;C=W.parents[1]
slug=sys.argv[1];O=W/'pages'/slug;O.mkdir(parents=True,exist_ok=True)
records=[]
with sync_playwright() as pw:
 b=pw.chromium.launch(channel='msedge',headless=True)
 for width,height in [(1440,1000),(360,800)]:
  p=b.new_page(viewport={'width':width,'height':height});p.set_default_timeout(15000)
  errors=[];p.on('pageerror',lambda e:errors.append(str(e)))
  row={'topic':slug,'width':width,'errors':errors,'visuals':[],'zoom_checks':0,'capture_version':2}
  try:
   p.goto(f'http://127.0.0.1:8000/docs/index.html#view=lesson&lesson={slug}&slide=1',wait_until='networkidle')
   p.evaluate('document.fonts.ready')
   (O/f'{width}-default.txt').write_text(p.locator('main').inner_text(),encoding='utf-8')
   p.screenshot(path=str(O/f'{width}-top.png'))
   cards=p.locator('.beginner-visual');row['cards']=cards.count()
   for i,card in enumerate(cards.all()):
    for j,fig in enumerate(card.locator('figure').all()):
     if not fig.is_visible():continue
     imgs=fig.locator('img:visible,object:visible')
     if not imgs.count():continue
     fig.scroll_into_view_if_needed()
     for im in imgs.all():
      if im.evaluate('(i)=>i.tagName')=='IMG':im.evaluate('(i)=>i.decode()')
      else:im.evaluate('(i)=>new Promise((resolve,reject)=>{if(i.contentDocument?.documentElement)resolve();else {i.addEventListener("load",resolve,{once:true});setTimeout(()=>reject(new Error("SVG object load timeout")),10000)}})')
     key=f'{width}-v{i+1}-{j+1}';fig.screenshot(path=str(O/(key+'.png')))
     if width==360 and fig.locator('.concept-image-link').count():
      anchor=fig.locator('.concept-image-link').first
      if anchor.evaluate('(e)=>e.scrollWidth>e.clientWidth+5'):
       anchor.evaluate('(e)=>e.scrollLeft=e.scrollWidth');fig.screenshot(path=str(O/(key+'-right.png')));anchor.evaluate('(e)=>e.scrollLeft=0')
     row['visuals'].append({'key':key,'title':card.locator('h3').all_text_contents(),'images':imgs.evaluate_all('(xs)=>xs.map(i=>({src:i.currentSrc||i.data,nw:i.naturalWidth||0,nh:i.naturalHeight||0,box:i.getBoundingClientRect().toJSON()}))')})
    zoom=card.locator('button[data-action="open-concept"]')
    if zoom.count():
     zoom.first.click();p.locator('#lightbox[open]').wait_for()
     p.wait_for_function("()=>{let i=document.querySelector('#lightbox img'),o=document.querySelector('#lightbox object');return (i&&i.complete&&i.naturalWidth>0)||(o&&o.contentDocument?.documentElement)}")
     p.keyboard.press('Escape');assert not p.locator('#lightbox[open]').count();row['zoom_checks']+=1
   answer=p.get_by_text('看解釋與可接受的取捨',exact=True)
   if answer.count():
    answer.click();answer.locator('..').screenshot(path=str(O/f'{width}-answer.png'));row['answer_opened']=True
   (O/f'{width}-reading.txt').write_text(p.locator('main').inner_text(),encoding='utf-8')
   hand=p.locator('.engineer-handoff')
   if hand.count():hand.scroll_into_view_if_needed();p.screenshot(path=str(O/f'{width}-operations.png'))
   row['default_overflow']=p.evaluate('document.documentElement.scrollWidth>innerWidth+1')
   # Open actual details controls, preserving the underlying teaching source.
   opened=[]
   for summary in p.locator('main details > summary').all():
    if summary.is_visible() and not summary.locator('..').evaluate('(e)=>e.open'):
     summary.click();opened.append(summary.inner_text())
   (O/f'{width}-expanded.txt').write_text(p.locator('main').inner_text(),encoding='utf-8')
   row['opened_details']=opened;row['expanded_overflow']=p.evaluate('document.documentElement.scrollWidth>innerWidth+1')
   row['expanded_images']=p.locator('main img:visible,main object:visible').evaluate_all('(xs)=>xs.map(i=>({src:i.currentSrc||i.data,nw:i.naturalWidth||0,nh:i.naturalHeight||0,box:i.getBoundingClientRect().toJSON()}))')
   # Four original engineering figures are reviewed separately from the new main path.
   for i,fig in enumerate(p.locator('.lesson-step figure').all()):
    if not fig.is_visible():continue
    fig.scroll_into_view_if_needed()
    for im in fig.locator('img:visible').all():im.evaluate('(i)=>i.decode()')
    fig.screenshot(path=str(O/f'{width}-engineering-{i+1}.png'))
   nxt=p.locator('.lesson-footer button').last
   if nxt.count():
    old=p.url;nxt.click();p.wait_for_timeout(150);row['navigation_changed']=p.url!=old
   row['complete']=True
  except Exception as e:
   row['failure']=str(e);row['trace']=traceback.format_exc();row['complete']=False
   p.screenshot(path=str(O/f'{width}-failure.png'))
  records.append(row);p.close()
 b.close()
(O/'report.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(slug,[(r['width'],r['complete'],r.get('cards'),r.get('failure','')[:100]) for r in records],flush=True)

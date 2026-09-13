from pathlib import Path
import json,time,traceback
from playwright.sync_api import sync_playwright
OUT=Path(__file__).parent; OUT.mkdir(exist_ok=True)
URL='http://127.0.0.1:8000/docs/index.html'
ledger={'started':time.strftime('%Y-%m-%d %H:%M:%S'),'lessons':[],'routes':[],'screenshots':[],'fatal':None}
def save(): (OUT/'browser-coverage.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2),encoding='utf8')
def images(p):
 return p.evaluate('''async()=>{const a=[...document.querySelectorAll('main img')];a.forEach(e=>e.loading='eager');await Promise.all(a.map(e=>e.decode().catch(()=>{})));return {total:a.length,broken:a.filter(e=>!e.complete||!e.naturalWidth).map(e=>e.getAttribute('src'))};}''')
def screenshot(p,name):
 p.screenshot(path=str(OUT/(name+'.png')));ledger['screenshots'].append(name+'.png')
def inspect(p):
 return {'overflow':p.evaluate('document.documentElement.scrollWidth>innerWidth'), 'images':images(p),'h1':p.locator('main h1').all_text_contents()}
try:
 with sync_playwright() as pw:
  b=pw.chromium.launch(channel='msedge',headless=True)
  for width in [1440,390]:
   ctx=b.new_context(viewport={'width':width,'height':900});p=ctx.new_page();p.set_default_timeout(10000);errors=[];p.on('pageerror',lambda e:errors.append(str(e)))
   p.goto(URL);data=json.loads(p.locator('#course-data').text_content());topics=data['topics'];families=data['families'];seen=set()
   for topic in topics:
    tid=topic['id'];row={'topic':tid,'width':width,'slides':[],'concepts':[],'chapters':[],'errors':[]};start=len(errors)
    try:
     p.goto(URL+'#view=lesson&lesson='+tid+'&slide=1');p.locator('#lesson-title').wait_for()
     row['default']=inspect(p)
     if topic['family'] not in seen:
      seen.add(topic['family']);p.evaluate('scrollTo(0,0)');screenshot(p,f'lesson-{width}-{tid}')
     # Real click exercise reveal and completion/bookmark toggles for every lesson.
     reveal=p.locator('summary').filter(has_text='看解釋與可接受的取捨')
     row['learning_checks']=reveal.count()
     for item in reveal.all(): item.click();assert item.locator('..').get_attribute('open') is not None
     for action in ['toggle-complete','bookmark']:
      button=p.locator(f'main [data-action="{action}"]').first
      before=button.inner_text();button.click();assert button.inner_text()!=before;button.click()
     # Open references to inventory every actual chapter and four-slide section.
     p.locator('main details').evaluate_all('(els)=>els.forEach(e=>e.open=true)')
     row['expanded']=inspect(p)
     for chapter in p.locator('main .model-chapter').all():
      chapter.scroll_into_view_if_needed();row['chapters'].append({'id':chapter.get_attribute('id'),'visible':chapter.is_visible()})
     # Every rendered main teaching visual must open and close its real zoom dialog.
     concept_count=p.locator('main [data-action="open-concept"]').count()
     for i in range(concept_count):
      trigger=p.locator('main [data-action="open-concept"]').nth(i);trigger.click()
      modal=p.locator('dialog[open]');assert modal.is_visible()
      row['concepts'].append({'index':i,'title':modal.locator('#lightbox-title').inner_text(),'broken':modal.locator('img').evaluate_all('(els)=>els.filter(e=>e.complete&&!e.naturalWidth).length')})
      p.locator('[data-action="close-lightbox"]').click();assert not p.locator('dialog[open]').count()
     slide_buttons=p.locator('main [data-action="open-lightbox"]')
     for i in range(slide_buttons.count()):
      trigger=slide_buttons.nth(i);index=trigger.get_attribute('data-slide');trigger.click();modal=p.locator('dialog[open]');assert modal.is_visible()
      row['slides'].append({'slide':index,'title':modal.locator('#lightbox-title').inner_text(),'images':modal.locator('img').evaluate_all('async els=>{await Promise.all(els.map(e=>e.decode().catch(()=>{})));return els.map(e=>({src:e.currentSrc,ok:!!e.naturalWidth}))}'),'prev_disabled':modal.locator('[data-action="lightbox-prev"]').is_disabled(),'next_disabled':modal.locator('[data-action="lightbox-next"]').is_disabled()})
      if index=='1':
       modal.locator('[data-action="lightbox-next"]').click();assert '02' in modal.locator('#lightbox-title').inner_text();modal.locator('[data-action="lightbox-prev"]').click();assert '01' in modal.locator('#lightbox-title').inner_text()
      p.keyboard.press('Escape');assert not p.locator('dialog[open]').count()
     # In-page chapter/step links, then route next/back while retaining lesson identity.
     jumps=p.locator('main [data-action="jump-step"]')
     row['step_links']=jumps.count()
     if jumps.count():jumps.last.click()
     footer=p.locator('.lesson-footer [data-action="lesson"]')
     if footer.count():
      nextid=footer.last.get_attribute('data-topic');footer.last.click();assert nextid in p.url;p.go_back();assert tid in p.url
     row['errors']=errors[start:]
    except Exception as e:row['failure']=str(e);row['errors']=errors[start:];screenshot(p,f'flag-{width}-{tid}')
    ledger['lessons'].append(row);save();print(width,tid,'FAIL' if row.get('failure') else 'ok',flush=True)
   routes=[('home','home'),('library','library'),('foundations','foundations'),('production','production'),('glossary','glossary')]+[('family-'+f['id'],'library&family='+f['id']) for f in families]
   for name,route in routes:
    row={'name':name,'width':width};start=len(errors)
    try:
     p.goto(URL+'#view='+route);row.update(inspect(p));p.locator('main details').evaluate_all('(els)=>els.forEach(e=>e.open=true)');row['expanded']=inspect(p)
     for button in p.locator('main [data-action="reading-view"]').all():button.click()
     for button in p.locator('main [data-action="jump-chapter"]').all():button.click()
     p.evaluate('scrollTo(0,0)');screenshot(p,f'route-{width}-{name}');row['errors']=errors[start:]
    except Exception as e:row['failure']=str(e)
    ledger['routes'].append(row);save()
   ctx.close()
  b.close()
except Exception:ledger['fatal']=traceback.format_exc()
ledger['finished']=time.strftime('%Y-%m-%d %H:%M:%S');save()

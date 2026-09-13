from pathlib import Path
import json,time,traceback,sys
from playwright.sync_api import sync_playwright
OUT=Path(__file__).parent;URL='http://127.0.0.1:8000/docs/index.html';WIDTH=int(sys.argv[1]);FILE=OUT/f'coverage-{WIDTH}.json'
ledger={'started':time.strftime('%Y-%m-%d %H:%M:%S'),'width':WIDTH,'lessons':[],'routes':[],'screenshots':[],'prior_attempts':[],'fatal':None}
for oldfile in [OUT/'browser-coverage.json',OUT/'browser-mobile-coverage.json',FILE]:
 if oldfile.exists():
  old=json.loads(oldfile.read_text(encoding='utf8'))
  for row in old.get('lessons',[]):
   if row['width']==WIDTH:
    if row.get('failure'):ledger['prior_attempts'].append(row)
    elif not any(x['topic']==row['topic'] for x in ledger['lessons']):ledger['lessons'].append(row)
  ledger['screenshots']+=old.get('screenshots',[])
def save():FILE.write_text(json.dumps(ledger,ensure_ascii=False,indent=2),encoding='utf8')
def imagecheck(p):
 return p.evaluate('''async()=>{const a=[...document.querySelectorAll('main img')];a.forEach(e=>e.loading='eager');await Promise.all(a.map(e=>e.decode().catch(()=>{})));return {total:a.length,broken:a.filter(e=>!e.complete||!e.naturalWidth).map(e=>e.getAttribute('src'))};}''')
def snap(p,name):p.screenshot(path=str(OUT/(name+'.png')));ledger['screenshots'].append(name+'.png')
def inspect(p):return {'overflow':p.evaluate('document.documentElement.scrollWidth>innerWidth'),'images':imagecheck(p),'h1':p.locator('main h1').all_text_contents()}
try:
 with sync_playwright() as pw:
  b=pw.chromium.launch(channel='msedge',headless=True);ctx=b.new_context(viewport={'width':WIDTH,'height':900},reduced_motion='reduce');p=ctx.new_page();p.set_default_timeout(7000);errors=[];p.on('pageerror',lambda e:errors.append(str(e)))
  p.goto(URL);data=json.loads(p.locator('#course-data').text_content());seen=set();done={r['topic'] for r in ledger['lessons']}
  for topic in data['topics']:
   tid=topic['id'];special=topic['family'] not in seen;seen.add(topic['family'])
   if tid in done:continue
   row={'topic':tid,'width':WIDTH,'slides':[],'chapters':[],'concepts':[],'errors':[],'interaction_scope':'family first' if special else 'rendered breadth'};start=len(errors)
   try:
    p.goto(URL+'#view=lesson&lesson='+tid+'&slide=1');p.locator('#lesson-title').wait_for();row['default']=inspect(p)
    if special:p.evaluate('scrollTo(0,0)');snap(p,f'lesson-{WIDTH}-{tid}')
    # All lesson check disclosures are exercised once; self-marking is sampled per layout.
    reveal=p.locator('summary').filter(has_text='看解釋與可接受的取捨');row['learning_checks']=reveal.count()
    for item in reveal.all():item.click();assert item.locator('..').get_attribute('open') is not None
    if special:
     for action in ['toggle-complete','bookmark']:
      button=p.locator(f'main [data-action="{action}"]').first;before=button.inner_text();button.click();assert button.inner_text()!=before;button.click()
    p.locator('main details').evaluate_all('(els)=>els.forEach(e=>e.open=true)');row['expanded']=inspect(p)
    for chapter in p.locator('main .deep-dive-chapter').all():
     chapter.scroll_into_view_if_needed();row['chapters'].append({'id':chapter.get_attribute('id'),'visible':chapter.is_visible(),'images':chapter.locator('img').evaluate_all('els=>els.map(e=>({src:e.currentSrc,ok:!!e.naturalWidth,width:e.getBoundingClientRect().width}))')})
    for step in p.locator('main .lesson-step').all():
     step.scroll_into_view_if_needed();row['slides'].append({'id':step.get_attribute('id'),'visible':step.is_visible(),'images':step.locator('img').evaluate_all('els=>els.map(e=>({src:e.currentSrc,ok:!!e.naturalWidth,width:e.getBoundingClientRect().width}))')})
    row['main_visuals']=p.locator('main .beginner-visual,main .workplace-visual').evaluate_all('els=>els.map(e=>({id:e.id,visible:!!e.getClientRects().length,images:e.querySelectorAll("img").length}))')
    if special:
     concepts=p.locator('main [data-action="open-concept"]');row['concept_count']=concepts.count()
     if concepts.count():
      concepts.first.click();assert p.locator('dialog[open]').is_visible();row['concepts'].append(p.locator('#lightbox-title').inner_text());p.locator('[data-action="close-lightbox"]').click()
     slides=p.locator('main [data-action="open-lightbox"]')
     if slides.count():
      slides.first.click();modal=p.locator('dialog[open]');row['zoom_titles']=[modal.locator('#lightbox-title').inner_text()]
      for _ in range(3):modal.locator('[data-action="lightbox-next"]').click();row['zoom_titles'].append(modal.locator('#lightbox-title').inner_text())
      assert modal.locator('[data-action="lightbox-next"]').is_disabled();modal.locator('[data-action="lightbox-prev"]').click();p.keyboard.press('Escape');assert not p.locator('dialog[open]').count()
     jumps=p.locator('main [data-action="jump-step"]');row['step_links']=jumps.count()
     if jumps.count():jumps.last.click()
     footer=p.locator('.lesson-footer [data-action="lesson"]')
     if footer.count():n=footer.last.get_attribute('data-topic');footer.last.click();assert n in p.url;p.go_back();assert tid in p.url
    row['errors']=errors[start:]
   except Exception as e:row['failure']=str(e);row['errors']=errors[start:];snap(p,f'flag-{WIDTH}-{tid}')
   ledger['lessons'].append(row);save();print(WIDTH,tid,'FAIL' if row.get('failure') else 'ok',flush=True)
  for name,route in [('home','home'),('library','library'),('foundations','foundations'),('production','production'),('glossary','glossary')]+[('family-'+f['id'],'library&family='+f['id']) for f in data['families']]:
   row={'name':name,'width':WIDTH};start=len(errors)
   try:
    p.goto(URL+'#view='+route);row.update(inspect(p));p.locator('main details').evaluate_all('(els)=>els.forEach(e=>e.open=true)');row['expanded']=inspect(p)
    buttons=p.locator('main [data-action="reading-view"]');row['reading_views']=buttons.count()
    for button in buttons.all():button.click()
    p.evaluate('scrollTo(0,0)');snap(p,f'route-{WIDTH}-{name}');row['errors']=errors[start:]
   except Exception as e:row['failure']=str(e)
   ledger['routes'].append(row);save()
  ctx.close();b.close()
except Exception:ledger['fatal']=traceback.format_exc()
ledger['finished']=time.strftime('%Y-%m-%d %H:%M:%S');save()

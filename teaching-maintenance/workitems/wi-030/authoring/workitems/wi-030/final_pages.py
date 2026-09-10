import json
from pathlib import Path
from playwright.sync_api import sync_playwright
P=Path(__file__).resolve().parent;C=P.parents[1]
content=json.loads((P/'lesson-content.json').read_text(encoding='utf-8'))
copy={k:{slug:a[k] for slug,a in content.items()} for k in ['first','evidence']}
records=[]
with sync_playwright() as pw:
 b=pw.chromium.launch(channel='msedge',headless=True)
 for slug,a in content.items():
  for width in [1440,360]:
   page=b.new_page(viewport={'width':width,'height':1000 if width==1440 else 800})
   errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
   page.goto('http://127.0.0.1:8000/docs/index.html#view=lesson&lesson='+slug+'&slide=1',wait_until='networkidle')
   text=page.locator('main').inner_text()
   assert a['core'] in text and a['compare'] in text and a['change'] in text
   assert copy['first'][slug] in text and copy['evidence'][slug] in text
   assert page.locator('.core-ideas .guide-list > li').count()==3
   images=page.locator('.beginner-visual figure img:visible');assert images.count()==3
   for img in images.all():
    img.scroll_into_view_if_needed()
    img.evaluate('(i)=>i.decode()')
   page.evaluate('window.scrollTo(0,0)')
   page.screenshot(path=str(P/f'final-{slug}-{width}-top.png'))
   images.first.evaluate('(e)=>window.scrollTo(0,scrollY+e.getBoundingClientRect().top-85)')
   page.screenshot(path=str(P/f'final-{slug}-{width}-core.png'))
   page.locator('.engineer-handoff').scroll_into_view_if_needed()
   page.screenshot(path=str(P/f'final-{slug}-{width}-operations.png'))
   answer=page.get_by_text('看解釋與可接受的取捨',exact=True)
   answer.click()
   assert a['quiz'][3] in answer.locator('..').inner_text()
   answer.locator('..').screenshot(path=str(P/f'final-{slug}-{width}-quiz.png'))
   text=page.locator('main').inner_text()
   if width==1440:
    (P/f'final-page-reading-{slug}.txt').write_text(text,encoding='utf-8')
   assert page.evaluate('document.documentElement.scrollWidth<=innerWidth+1')
   assert not errors
   records.append({'slug':slug,'width':width,'conditional_quiz_answer_checked':True,'core_comparison_and_cost_visible':True,'first_and_evidence_visible':True,'three_core_callouts':True,'images':images.evaluate_all('(xs)=>xs.map(i=>({src:i.currentSrc,width:i.getBoundingClientRect().width,height:i.getBoundingClientRect().height}))'),'overflow':False,'errors':errors})
   page.close()
 b.close()
(P/'final-page-checks.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
print('PASS',len(records),'final states; core/comparison/cost/operating-copy visible')

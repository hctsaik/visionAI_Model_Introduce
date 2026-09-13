from pathlib import Path
import json
from playwright.sync_api import sync_playwright
OUT=Path(__file__).parent
URL='http://127.0.0.1:8000/docs/index.html'
with sync_playwright() as pw:
 b=pw.chromium.launch(channel='msedge',headless=True)
 results=[]
 for width in [1440,390]:
  ctx=b.new_context(viewport={'width':width,'height':900});p=ctx.new_page();p.goto(URL)
  p.get_by_role('button',name='從第一張教學圖開始：ChArUco',exact=True).click()
  lesson=p.url
  p.get_by_role('button',name='完成本主題',exact=True).click()
  completed=p.get_by_role('button',name='✓ 已完成',exact=True).is_visible()
  summary=p.locator('summary').filter(has_text='看解釋與可接受的取捨')
  if summary.count():
   check_y=summary.evaluate('(e)=>Math.round(e.getBoundingClientRect().top+scrollY)');summary.click();parent=summary.locator('..')
   (OUT/f'ux-{width}-learning-check.txt').write_text(parent.inner_text(),encoding='utf8');parent.screenshot(path=str(OUT/f'ux-{width}-learning-check.png'))
  else: check_y=None
  p.locator('[data-action="send-to-poc"]').click();p.locator('#poc-answer').wait_for()
  for key,value in [('task','count'),('placement','fixed'),('visibility','clear'),('data','normal')]:
   assert p.locator('#poc-answer').get_attribute('data-poc-answer')==key
   p.locator('#poc-answer').select_option(value);p.locator('[data-action="poc-next"]').click()
  p.locator('#poc-result').screenshot(path=str(OUT/f'ux-{width}-poc-result.png'))
  (OUT/f'ux-{width}-poc-result.txt').write_text(p.locator('#poc-result').inner_text(),encoding='utf8')
  results.append({'width':width,'home_cta_lesson':lesson,'complete_without_check':completed,'learning_check_y':check_y,'result_title':p.locator('#poc-result-title').inner_text(),'overflow':p.evaluate('document.documentElement.scrollWidth>innerWidth')})
  ctx.close()
 (OUT/'ux-walk-evidence.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf8')
 b.close()

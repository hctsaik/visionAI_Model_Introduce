import json,hashlib
from pathlib import Path
from playwright.sync_api import sync_playwright
W=Path(__file__).resolve().parent;C=W.parents[1]
data=json.loads((W/'course-data.json').read_text(encoding='utf-8'))
records=[]
with sync_playwright() as pw:
 b=pw.chromium.launch(channel='msedge',headless=True)
 p=b.new_page(viewport={'width':360,'height':800})
 for t in data['topics']:
  p.goto('http://127.0.0.1:8000/docs/index.html#view=lesson&lesson='+t['id']+'&slide=1',wait_until='domcontentloaded')
  p.evaluate('document.fonts.ready')
  figs=p.locator('.beginner-visual figcaption')
  for n,cap in enumerate(figs.all(),1):
   if not cap.is_visible():continue
   hit=cap.evaluate('''c=>{const s=c.querySelector('strong'),b=c.querySelector('button');if(!s||!b)return null;let br=b.getBoundingClientRect(),sr=s.getBoundingClientRect(),bad=[];const walk=document.createTreeWalker(s,NodeFilter.SHOW_TEXT);while(walk.nextNode()){let n=walk.currentNode;for(let i=0;i<n.length;i++){let r=document.createRange();r.setStart(n,i);r.setEnd(n,i+1);for(let q of r.getClientRects())if(q.right>br.left+.5&&q.left<br.right-.5&&q.bottom>br.top+.5&&q.top<br.bottom-.5)bad.push(n.textContent[i])}}return {text:s.innerText,overlap_chars:bad.join(''),strong:sr.toJSON(),button:br.toJSON(),caption:c.getBoundingClientRect().toJSON()}}''')
   if hit:records.append({'topic':t['id'],'figure':n,**hit})
 # Recheck a blank captured SVG view after settling and save evidence without modifying site styles.
 p.set_viewport_size({'width':1440,'height':1000})
 p.goto('http://127.0.0.1:8000/docs/index.html#view=lesson&lesson=resnet&slide=1',wait_until='networkidle')
 p.evaluate("document.querySelector('.model-deep-dive').closest('details').open=true")
 ch=p.locator('.deep-dive-chapter').nth(7)
 ch.locator('[data-action="reading-view"]').nth(2).click()
 fig=ch.locator('.reading-view-panel').nth(2).locator('figure');fig.scroll_into_view_if_needed()
 p.wait_for_timeout(1500)
 fig.screenshot(path=str(W/'deep/resnet/1440-c08-v03-recheck.png'))
 b.close()
(W/'caption-layout.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
hits=[r for r in records if r['overlap_chars']]
print('caption checks',len(records),'overlap',len(hits),'topics',len({r['topic'] for r in hits}),flush=True)
print([(r['topic'],r['figure'],r['overlap_chars']) for r in hits],flush=True)

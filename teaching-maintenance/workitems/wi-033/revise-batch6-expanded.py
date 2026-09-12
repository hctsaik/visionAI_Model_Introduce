from pathlib import Path
import json,runpy,subprocess,sys,asyncio
from playwright.async_api import async_playwright
W=Path(__file__).resolve().parent;m=runpy.run_path(str(W/'plan-batch6-prototypes.py'))
ids=['ad-winclip-engineering-1','ad-winclip-engineering-3','ad-winclip-engineering-4','ad-anomalyclip-engineering-3','ad-anomalyclip-engineering-4','ad-ddad-engineering-4','frame-difference-engineering-3','frame-difference-engineering-4','background-subtraction-engineering-3','background-subtraction-engineering-4']
p=W/'engineering-plan.json';rows=json.loads(p.read_text(encoding='utf-8'));checks=[]
for r in rows:
 if r['id'] not in ids:continue
 r['version']='r02'
 if r['id']=='ad-winclip-engineering-1':r['panels'][0]['graphic']='b6-win-holdout'
 if r['id']=='ad-winclip-engineering-4':r['title']='WinCLIP：與學習提示比較'
 if r['id']=='ad-ddad-engineering-4':r['panels'][2]=dict(title='兩路評分仍用真缺陷獨立驗',graphic='b6-ad-validate')
 if r['id']=='frame-difference-engineering-4':r['panels'][2]['graphic']='b6-fd-bg-compare'
 f=W/(r['id']+'-r02.md');f.write_text(m['brief'](r)+'\n實看r01手機後修正：零樣本不標正常訓練、孔口圈不填孔、影片保留未印字方件與位置、標題不斷英文、DDAD反例結尾改獨立驗證。\n',encoding='utf-8');checks.append(m['v'].validate(f))
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8');(W/'batch6-expanded-r02-preflight-validation.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2),encoding='utf-8')
p=W/'batch6-main-mobile-plan.json';mainrows=json.loads(p.read_text(encoding='utf-8'));r=mainrows[0];r['version']='r02';f=W/(r['id']+'-r02.md');f.write_text(m['brief'](r)+'\n圈標不填孔，保留正常工件同一孔口。\n',encoding='utf-8');m['v'].validate(f);p.write_text(json.dumps(mainrows,ensure_ascii=False,indent=2),encoding='utf-8')
(W/'checkpoint-note.md').write_text('### WI-033 第六批擴展手機初審修正\n\n24擴展手機及2共用首讀均已實看。發現WinCLIP零樣本誤標訓練、孔口圈填色掩孔、影片方件多L標記/位置、英文標題斷字，已修10故事與1共用手機r02 preflight。即將渲染20工程PNG和1主圖；其他桌機尚未審，整合與驗頁未做。完成33/52，使用者核准pending，全部52課繼續。\n',encoding='utf-8');runpy.run_path(str(W/'append-checkpoint.py'))
subprocess.run([sys.executable,'-X','utf8',str(W/'render.py'),*ids],check=True)
mobile=runpy.run_path(str(W/'make-batch6-main-mobile.py'))
async def render_one():
 svg,w,h=mobile['make'](r,True);svg=svg.replace('工程圖解｜教學示意，非模型實測','首讀圖解｜作者示意，非模型實測');f=W/(r['id']+'-r02-mobile.svg');assert not f.exists();f.write_text(svg,encoding='utf-8')
 async with async_playwright() as p:
  b=await p.chromium.launch(channel='msedge',headless=True,args=['--disable-gpu']);page=await b.new_page(viewport=dict(width=w,height=h));await page.goto(f.as_uri());await page.evaluate('document.fonts.ready');await page.wait_for_timeout(500);await page.screenshot(path=str(f.with_suffix('.png')));await b.close()
asyncio.run(render_one());print('21 revised PNGs rendered; review pending')

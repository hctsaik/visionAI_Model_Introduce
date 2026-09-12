from pathlib import Path
import runpy,json,importlib.util,asyncio
from playwright.async_api import async_playwright
import render
W=Path(__file__).resolve().parent;C=W.parents[1]
m=runpy.run_path(str(W/'make-batch7-sr-main.py'));row=m['row'];row['version']='r02';row['detail']+=' r01兩設備實看：局部圓孔跨出裁切框，r02以SVG viewport截取真正局部；去除學生無需知道的換圖歷史。'
brief=runpy.run_path(str(W/'plan-batch7-prototypes.py'))['brief'];p=W/(row['id']+'-r02.md');p.write_text(brief(row),encoding='utf-8')
sp=importlib.util.spec_from_file_location('v',C/'tools/validate_teaching_preflight.py');v=importlib.util.module_from_spec(sp);sp.loader.exec_module(v)
(W/'batch7-main-r02-preflight-validation.json').write_text(json.dumps(v.validate(p),ensure_ascii=False,indent=2),encoding='utf-8');(W/'batch7-main-plan.json').write_text(json.dumps([row],ensure_ascii=False,indent=2),encoding='utf-8')
(W/'checkpoint-note.md').write_text('### WI-033 第七批擴展初審與SR修正\n\n33擴展66PNG已生成；前5課的15故事30PNG原生實看，時間軸標籤需分別定位，VideoMAE平均例將明寫平方差。其餘18故事36PNG未看。SR主反例2PNG實看見局部孔超裁切框，r02 preflight通過，即將渲染2PNG。正式引用未改；完成41/52。使用者核准pending，全部52課持續。\n',encoding='utf-8');runpy.run_path(str(W/'append-checkpoint.py'))
async def main():
 render.graphic=m['graphic']
 async with async_playwright() as p:
  b=await p.chromium.launch(channel='msedge',headless=True,args=['--disable-gpu'])
  for mode in ['desktop','mobile']:
   svg,w,h=render.make(row,mode=='mobile');svg=svg.replace('工程圖解｜教學示意，非模型實測','首讀反例｜作者示意，非模型實測');f=W/(row['id']+'-r02-'+mode+'.svg');assert not f.exists();f.write_text(svg,encoding='utf-8');page=await b.new_page(viewport=dict(width=w,height=h));await page.goto(f.as_uri());await page.evaluate('document.fonts.ready');await page.wait_for_timeout(500);await page.screenshot(path=str(f.with_suffix('.png')));await page.close()
  await b.close()
asyncio.run(main())

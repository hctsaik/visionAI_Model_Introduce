from pathlib import Path
import json,runpy,importlib.util,asyncio,subprocess,sys
from playwright.async_api import async_playwright
W=Path(__file__).resolve().parent;C=W.parents[1]
sp=importlib.util.spec_from_file_location('d',W/'deep-batch5.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
rows=json.loads((W/'engineering-plan.json').read_text(encoding='utf-8'))
r=next(r for r in rows if r['id']=='ad-rd4ad-engineering-1');r['version']='r02';r['panels'][1]['graphic']='b5-rd-train-bottleneck'
brief=W/(r['id']+'-r02.md');brief.write_text((W/(r['id']+'-r01.md')).read_text(encoding='utf-8')+'\n修訂：訓練步驟改為正常無刮傷工件，避免把待測傷件誤作訓練輸入。r01桌機實看發現；r02 PNG待審。\n',encoding='utf-8');m.v.validate(brief)
p=next(r for r in rows if r['id']=='ad-padim-engineering-4');p['detail']=p['detail'].replace('圖內PatchCore無孔板僅原型符號不適合跨件比較，工程比較圖須以同單孔板替換來源示意；','比較圖保持同一單孔板；')
(W/'engineering-plan.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
deep=json.loads((W/'batch5-deep-plan.json').read_text(encoding='utf-8'));f=deep[0];f['version']='r02';f['panels'][1]['tiles'][0]=[[600,250,370,348],[100,115,470,442]]
brief=W/'patchcore-deep-features-r02.md';brief.write_text((W/'patchcore-deep-features-r01.md').read_text(encoding='utf-8')+'\n修訂：縮短第二格向量來源裁切，排除底端半行舊標籤。保留完整28×28格圖。r02 PNG待審。\n',encoding='utf-8');m.v.validate(brief)
(W/'batch5-deep-plan.json').write_text(json.dumps(deep,ensure_ascii=False,indent=2),encoding='utf-8')
(W/'checkpoint-note.md').write_text('### WI-033 第五批桌機審查補修\n\n24擴展桌機及兩深讀手機已實看。RD4AD工程1訓練圖需無刮傷正常輸入；PatchCore features手機排除裁切半行標籤。兩份r02 preflight通過，即將渲染3PNG，未整合；擴展手機待看。完成25/52，全部52課持續，使用者核准pending。產物workitems/wi-033。\n',encoding='utf-8');runpy.run_path(str(W/'append-checkpoint.py'))
subprocess.run([sys.executable,str(W/'render.py'),'ad-rd4ad-engineering-1'],check=True)
async def main():
 async with async_playwright() as pw:
  b=await pw.chromium.launch(channel='msedge',headless=True);p=await b.new_page(viewport={'width':768,'height':2800});svg=W/'patchcore-deep-features-r02-mobile.svg';assert not svg.exists();svg.write_text(m.m.make(f),encoding='utf-8');await p.goto(svg.as_uri());await p.evaluate('document.fonts.ready');await p.wait_for_timeout(300);await p.screenshot(path=str(svg.with_suffix('.png')));await b.close()
asyncio.run(main())

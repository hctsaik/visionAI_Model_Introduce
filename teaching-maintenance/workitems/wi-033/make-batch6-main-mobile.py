from pathlib import Path
import json,runpy,asyncio
from playwright.async_api import async_playwright
from render import make,rect,text,arrow,pill,B,G,O,N
from batch5_graphics import board
from batch3_graphics import caption
import render
W=Path(__file__).resolve().parent;C=W.parents[1];m=runpy.run_path(str(W/'plan-batch6-prototypes.py'))
rows=[dict(id='clip-shared-errors',title='文字懂異常，仍可能看錯細節',takeaway='語意相似需回原圖，分開驗誤報與漏檢。',kind='D',mobile_height=2400,panels=[dict(title='同一金屬板：正常q與刮傷p',graphic='b6-clip-pair'),dict(title='作者反例：正常誤報、刮傷漏檢',graphic='b6-clip-errors'),dict(title='固定取像與真值，再比較設定',graphic='main-verify')],detail='以同一雙孔板正常N的允收孔口q與異常A刮傷p，維持原身份；正常反光誤報與細傷漏檢為作者假設。第三節點要求固定可見度/取像、正常與真缺陷獨立留出、比較提示設定；不捏造分數。'),dict(id='clip-shared-methods',title='三種圖文方法，先選工作結果',takeaway='同件、同漏檢要求，再比資料與覆核成本。',kind='D',mobile_height=2400,panels=[dict(title='WinCLIP：人工文字＋局部視窗',graphic='main-win'),dict(title='AnomalyCLIP：輔助資料學提示',graphic='main-ac'),dict(title='AnomalyGPT：位置線索＋對話',graphic='main-gpt')],detail='三節點各展示同金屬板p和一種方法：WinCLIP人工提示/可加正常參考的+模式；AnomalyCLIP預訓練提示和辅助標註；AnomalyGPT已訓練內建定位與對話。位置圖只示輸出形式，不表示相同成效或精密輪廓。保留原桌機和頁面補充解釋。')]
for r in rows:r.update(version='r01',source='https://arxiv.org/html/2303.14814v1 ; https://arxiv.org/html/2310.18961v3 ; https://github.com/CASIA-IVA-Lab/AnomalyGPT')
def main_graphic(k):
 if k=='main-verify':
  a=board(155,5,.5,2,True,True)
  for i,t in enumerate(['固定解析度、光線與拍攝位置','留出正常與真缺陷，逐件對真值','同漏檢要求比較誤報與覆核量']):a+=text(15,172+i*63,t,27,B if i!=1 else O,700)
  return a+caption('細節不可見時，先改善取像','提示變更也要重新驗證')
 if k in ['main-win','main-ac','main-gpt']:
  a=board(15,10,.55,2,True,True)+arrow(220,74,258,74)+rect(285,30,125,90,'#E2EDF9',B,3)+rect(364,81,25,25,O,'none',0)+text(290,155,'位置線索p?',27,B,700)
  ls={'main-win':['人工正常／異常描述','WinCLIP+：可加正常視覺參考'],'main-ac':['已學提示：來自輔助標註','目標零樣本，仍需獨立驗證'],'main-gpt':['已訓練定位與對話模組','問題：哪裡可疑？→ 對照原图']}[k]
  a+=text(15,224,ls[0],28,B,700)+text(15,285,ls[1],25,N)
  return a+caption('同板輸出形式示意，非實測','位置不等於輪廓、尺寸或根因')
 return original(k)
original=render.graphic;render.graphic=main_graphic
async def main():
 checks=[]
 for r in rows:
  p=W/(r['id']+'-r01.md');p.write_text(m['brief'](r)+'\n只改兩課共用手機首讀，SVG程式原生新圖；桌機與補充文字保留。\n',encoding='utf-8');checks.append(m['v'].validate(p))
 (W/'batch6-main-mobile-plan.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8');(W/'batch6-main-preflight-validation.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2),encoding='utf-8')
 (W/'checkpoint-note.md').write_text('### WI-033 第六批共用手機首讀preflight\n\n兩共用手機原圖此前已實看，現以3節點重排正常q/刮傷p反例與三方法比較。兩preflight通過，即將渲染2PNG；24擴展48PNG另在生成，尚未審或整合。完成33/52，使用者核准pending；全部52課持續。\n',encoding='utf-8');runpy.run_path(str(W/'append-checkpoint.py'))
 async with async_playwright() as p:
  b=await p.chromium.launch(channel='msedge',headless=True,args=['--disable-gpu'])
  for r in rows:
   svg,w,h=make(r,True);svg=svg.replace('工程圖解｜教學示意，非模型實測','首讀圖解｜作者示意，非模型實測');f=W/(r['id']+'-r01-mobile.svg');assert not f.exists();f.write_text(svg,encoding='utf-8');page=await b.new_page(viewport=dict(width=w,height=h));await page.goto(f.as_uri());await page.evaluate('document.fonts.ready');await page.wait_for_timeout(500);await page.screenshot(path=str(f.with_suffix('.png')));await page.close()
  await b.close()
 print('2 shared main mobile PNGs rendered; review pending')
if __name__=='__main__':asyncio.run(main())

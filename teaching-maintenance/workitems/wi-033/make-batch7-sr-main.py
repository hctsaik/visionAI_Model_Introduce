from pathlib import Path
import json,runpy,asyncio,importlib.util
from playwright.async_api import async_playwright
import render
from render import rect,text,arrow,circle,group,B,G,O,N
from batch7_graphics import panel
from batch3_graphics import grid,caption
W=Path(__file__).resolve().parent;C=W.parents[1];m=runpy.run_path(str(W/'plan-batch7-prototypes.py'))
row=dict(id='sr-same-board-counterexample',version='r01',title='超解析反例：同一孔邊，細節仍不確定',takeaway='缺口是否存在，要靠真正有解析力的取像。',kind='D',mobile_height=2304,panels=[dict(title='矩形雙孔板，固定左孔邊q',graphic='sr-main-source'),dict(title='同一q可有不同高解析候選',graphic='sr-main-alternatives'),dict(title='重新取像確認q的真實邊界',graphic='sr-main-evidence')],detail='恢復首讀同一矩形板大左孔小右孔與四角固定點。固定左大孔左邊q；粗格只示意資訊不足，不聲稱兩幾何候選精確降採樣相等。候選A平滑、B有小缺口（白色孔向左延伸）；兩者是作者可能性示意，均非實測。第三節點區分模型放大估計與實際更高解析取像，需校正/位置對準後判斷。替換原圓板右下邊主反例桌機及手機，連動圖說/mental_model限制。',source='https://arxiv.org/abs/2104.07636')

def local(x,y,dent=False,col=B):
 a=rect(0,0,195,170,'url(#steel)','#73899E',4)+circle(164,85,61,'#73899E','white')
 if dent:a+='<path d="M 107,67 L 83,76 L 99,95 L 107,100 Z" fill="white" stroke="white" stroke-width="2"/>'
 a+=rect(76,52,50,66,'none',col,2)
 return group(x,y,1,'<svg width="195" height="170" viewBox="0 0 195 170" overflow="hidden">'+a+'</svg>')

original=render.graphic
def graphic(k):
 if k=='sr-main-source':return panel(20,20,.75,style='sr')+rect(72,78,32,32,'none',O,0)+text(58,135,'q',28,O,700)+arrow(117,95,331,93,O)+grid(4,345,37,115)+text(20,276,'粗採樣：孔邊細節還看不清',29,B,700)+caption('從同一孔邊q放大，保持位置對應','粗格示意資訊不足，非實際像素值')
 if k=='sr-main-alternatives':return local(20,20)+local(275,20,True,O)+text(20,240,'候選A：平滑',27,B)+text(275,240,'候選B：小缺口',26,O)+caption('同一q的可能細節，尚未確認','不聲稱兩示意圖精確降採樣相同')
 if k=='sr-main-evidence':return panel(20,20,.6,style='sr')+rect(61,66,27,27,'none',O,0)+arrow(120,86,278,86,G)+local(285,20,True,G)+text(20,234,'重新取像＋對準同一q',29,G,700)+caption('這一步需要真實更高解析觀測','生成結果不是用來驗自己的真值')
 return original(k)

async def main():
 sp=importlib.util.spec_from_file_location('v',C/'tools/validate_teaching_preflight.py');v=importlib.util.module_from_spec(sp);sp.loader.exec_module(v)
 p=W/(row['id']+'-r01.md');p.write_text(m['brief'](row),encoding='utf-8');check=v.validate(p)
 (W/'batch7-main-plan.json').write_text(json.dumps([row],ensure_ascii=False,indent=2),encoding='utf-8');(W/'batch7-main-preflight-validation.json').write_text(json.dumps([check],ensure_ascii=False,indent=2),encoding='utf-8')
 (W/'checkpoint-note.md').write_text('### WI-033 SR同件主反例preflight\n\n原主反例圓板右下邊與核心矩形板不一致，現固定矩形大左小右孔與左孔q；兩可能邊界不假稱精確同降採樣。preflight通過，即將生成2PNG，尚未審/整合。33擴展66PNG生成中。完成41/52，使用者核准pending，全部52課持續。\n',encoding='utf-8');runpy.run_path(str(W/'append-checkpoint.py'))
 render.graphic=graphic
 async with async_playwright() as p:
  b=await p.chromium.launch(channel='msedge',headless=True,args=['--disable-gpu'])
  for mode in ['desktop','mobile']:
   svg,w,h=render.make(row,mode=='mobile');svg=svg.replace('工程圖解｜教學示意，非模型實測','首讀反例｜作者示意，非模型實測');f=W/(row['id']+'-r01-'+mode+'.svg');assert not f.exists();f.write_text(svg,encoding='utf-8');page=await b.new_page(viewport=dict(width=w,height=h));await page.goto(f.as_uri());await page.evaluate('document.fonts.ready');await page.wait_for_timeout(500);await page.screenshot(path=str(f.with_suffix('.png')));await page.close()
  await b.close()
 print('2 SR main PNG rendered; actual review pending')
if __name__=='__main__':asyncio.run(main())

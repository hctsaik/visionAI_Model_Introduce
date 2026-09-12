from pathlib import Path
import importlib.util,json,asyncio
from playwright.async_api import async_playwright
W=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('reflow',W/'deep-batch3-reflow.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
def panel(title,tiles,notes):return dict(title=title,tiles=tiles,notes=notes)
def row(id,source,title,provenance,takeaway,panels):return dict(id=id,source='_course_content/generated-concepts/'+source,title=title,provenance=provenance,takeaway=takeaway,panels=panels)
ROWS=[
row('resnet-deep-skip','resnet/resnet-e02-skip.svg','跳接保留同一輸入特徵','原算例重排；非模型實際推論','主路學修正，直通輸入在相加點會合。',[
 panel('普通塊：輸入經過全部層',[([35,150,250,600],[185,95,305,560])],['普通路徑直接學整個輸出H(x)']),
 panel('殘差塊：保留 x，再加 F(x)',[([350,150,385,600],[150,95,390,560])],['x=[2,1,3]；F(x)=[0,2,−1]','相加得到[2,3,2]，再經ReLU']),
 panel('修正為零，直通仍保留輸入',[([805,170,830,570],[15,100,665,500])],['形狀不同時需投影或對齊','直通的是特徵，不是修補後照片'])]),
row('resnet-deep-bn','resnet/resnet-e01-04-bn.svg','同件回應，訓練批次會影響中心化','沿用BatchNorm簡化算例；非新推論','部署使用保存統計，並重新驗證域內表現。',[
 panel('固定同件與回應 x=5',[([40,160,400,425],[135,90,440,485])],['此處只說中心化，省略縮放與偏移']),
 panel('訓練：兩批使用不同平均值',[([450,200,1150,95],[15,130,660,100]),([450,325,1150,95],[15,330,660,100])],['批A：[3,5,7]，5−5=0','批B：[5,8,11]，5−8=−3']),
 panel('eval：兩批都使用保存 μ=4',[([450,455,1150,95],[15,130,660,100]),([450,585,1150,95],[15,330,660,100])],['同件 x=5，兩次都是5−4=1','完整BN還包含方差、縮放與偏移'])]),
row('resnet-deep-cnx-spatial','convnext/convnext-e01-03-spatial.svg','ConvNeXt：先在同通道看附近','沿用ConvNeXt Tiny本機值；非缺陷分類','49個位置乘各自權重後相加，再加偏置。',[
 panel('同一R-01，同通道的鄰域',[([35,170,390,525],[20,100,285,450]),([430,200,390,455],[330,100,335,450])],['stem通道69/96，位置(39,15)','橘框選取同通道7×7鄰域']),
 panel('放大該位置附近的49個回應',[([845,265,345,370],[120,120,445,490])],['每個格位的回應有自己的權重','這一步沒有混合不同通道']),
 panel('乘權重、相加、再加偏置',[([1255,210,390,460],[130,110,450,520])],['沿用原記錄：相加+b → 0.23','框選、權重與核算仍保留在來源'])]),
row('resnet-deep-cnx-channel','convnext/convnext-e01-03-channels.svg','ConvNeXt：同位置再混通道','沿用本機值；展示前三大貢獻','合併所有通道後，仍有GELU、投影與殘差。',[
 panel('固定位置，先看通道69的貢獻',[([425,225,365,490],[170,100,380,525])],['同位置(39,15)，先經LayerNorm','通道69：14.55 × 0.132 ≈ 1.92']),
 panel('同位置的通道9與通道4',[([835,225,355,490],[20,100,305,430]),([1240,225,355,490],[350,100,305,430])],['通道9：7.76 × 0.103 ≈ 0.80','通道4：5.16 × 0.142 ≈ 0.73']),
 panel('三項加其餘通道與偏置',[([35,155,370,445],[160,100,380,430]),([460,755,1160,55],[15,550,660,55])],['1.92 + 0.80 + 0.73 + 2.10 = 5.55','96通道組成384回應；非分類輸出'])]),
row('resnet-deep-vit-attention','vit-classifier/vit-classifier-e01-06-r01-attention.svg','ViT：同一位置取用其他位置訊息','沿用ViT-B/16本機權重；末層第1頭','按權重混合value；原圖裁片不是全部貢獻。',[
 panel('原R-01中的查詢與四個參考位置',[([40,170,730,570],[10,95,665,535])],['橘框是查詢(5,7)，藍框是參考','沿用原模型記錄，沒有重新推論']),
 panel('前兩個參考位置的加權貢獻',[([785,205,185,330],[25,125,285,495]),([985,205,185,330],[355,125,285,495])],['權重乘value的一個分量','不是把百分比叫做缺陷機率']),
 panel('再合併其餘參考位置',[([1185,205,185,330],[25,125,285,495]),([1385,205,185,330],[355,125,285,495])],['此圖只展四個權重最大的patch','最後一層的value已含其他位置脈絡'])]),
row('segformer-deep-task','segformer/segformer-e01-01-task.svg','先標亮線位置，再交付候選','W-01原像素與概念標註；非模型推論','亮線是外觀位置，物理原因仍需製程證據。',[
 panel('固定來源W-01晶圓',[([40,205,530,530],[40,90,600,550])],['原場景作為位置追蹤的共同來源']),
 panel('放大同一處細亮線',[([600,205,530,530],[40,90,600,550])],['保持同一工件、同一外觀位置']),
 panel('依定義標註像素類別',[([1160,205,500,530],[55,90,560,550])],['圖中為概念標註，不是模型推論','每顆die的ID與尺寸須另接流程'])]),
row('segformer-deep-scales','segformer/segformer-e01-03-scales.svg','同一細線，用四個尺度觀察','沿用平均縮小概念場；非MiT特徵','細圖留窄線，粗圖看範圍；四尺度皆需保留。',[
 panel('同一局部的細線與範圍訊號',[([30,185,325,470],[150,90,395,550])],['這裡用平均縮小解釋尺度代價']),
 panel('較細的第1與第2尺度',[([365,290,300,380],[15,135,315,405]),([685,290,300,380],[345,135,315,405])],['第1尺度1/4；第2尺度1/8','細線的局部位置仍較清楚']),
 panel('較粗的第3與第4尺度',[([1000,290,300,380],[15,135,315,405]),([1320,290,330,380],[345,135,315,405])],['第3尺度1/16；第4尺度1/32','實際特徵還取決於學習與取像'])]),
row('segformer-deep-sr','segformer/segformer-e01-04-sr.svg','保留查詢，縮減K/V位置','沿用8×8簡化位置示例；非模型回應','關係數減少16倍，不代表實際速度快16倍。',[
 panel('原有64個查詢位置',[([35,230,615,440],[25,115,635,475])],['8×8=64，每個Q仍保留','橘框只標其中一個查詢位置']),
 panel('K/V縮到2×2，共4個位置',[([705,240,545,440],[40,115,590,475])],['每個Q與4個K算權重，再混合V','每邊縮4倍，位置數縮16倍']),
 panel('比較关系數，再驗證細節與時間',[([1275,345,365,165],[60,150,550,255])],['原本64×64=4096組','縮減後64×4=256組','其他運算與硬體仍影響耗時'])]),
row('segformer-deep-decoder','segformer/segformer-e01-05-decoder.svg','四尺度對齊，保留後一起判像素','沿用W-01亮線融合概念；非模型推論','投影、resize、沿通道拼接，再學習分類。',[
 panel('四組尺度保留自己的內容',[([45,175,1100,265],[15,160,660,200])],['各尺度投影到相容的通道數','不是四張遮罩直接平均']),
 panel('調整成相同網格後沿通道拼接',[([45,450,1110,145],[15,150,660,115]),([45,600,810,180],[15,350,660,150])],['同位置組合四組不同內容','對齊到第一尺度，再融合分類']),
 panel('像素候選回到原圖核對',[([900,540,740,280],[15,160,660,280])],['此處是概念候選，不是實測結果','回到輸入大小後仍需邊界驗證'])])
]
async def main():
 revised={'resnet-deep-bn','resnet-deep-cnx-spatial','resnet-deep-cnx-channel','segformer-deep-sr','segformer-deep-decoder'}
 for r in ROWS:
  if r['id']=='resnet-deep-bn':
   r['panels'][1]['tiles']=[([695,210,585,75],[15,130,640,120]),([695,339,585,75],[15,340,640,120])]
   r['panels'][2]['tiles']=[([695,468,585,75],[15,130,640,120]),([695,597,585,75],[15,340,640,120])]
  if r['id']=='resnet-deep-cnx-spatial':r['omit_arrows']=['M757,434.0 L845,431.12']
  if r['id'] in ['resnet-deep-cnx-channel','segformer-deep-sr','segformer-deep-decoder']:r['omit_arrows']=True
  if r['id']=='resnet-deep-cnx-channel':r['panels'][2]['tiles']=r['panels'][2]['tiles'][:1]
  if r['id']=='segformer-deep-decoder':
   r['panels'][0]['tiles']=[([45+j*280,175,250,282],[20+(j%2)*335,95+(j//2)*275,300,260]) for j in range(4)]
   r['panels'][1]['tiles']=[([525,500,315,315],[130,125,440,440])]
   r['panels'][2]['tiles']=[([1205,465,330,365],[130,110,440,485])]
 for r in ROWS:m.preflight(r)
 (W/'batch3-deep-expanded-plan.json').write_text(json.dumps(ROWS,ensure_ascii=False,indent=2),encoding='utf-8')
 import sys
 if '--plan' in sys.argv:return
 async with async_playwright() as p:
  b=await p.chromium.launch(channel='msedge',headless=True)
  for r in ROWS:
   if r['id']!='segformer-deep-decoder':continue
   f=W/(r['id']+'-r03-mobile.svg');assert not f.exists();(W/(r['id']+'-r03.md')).write_text((W/(r['id']+'-r01.md')).read_text(encoding='utf-8')+'\n修訂：完整四尺度採2×2排列，裁切終點止於圖格後，排除下一行字頂端碎點；拼接與結果獨立放大。待實看。\n',encoding='utf-8');f.write_text(m.make(r),encoding='utf-8')
   page=await b.new_page(viewport={'width':768,'height':2800},device_scale_factor=1);await page.goto(f.as_uri());await page.wait_for_timeout(300);await page.screenshot(path=str(f.with_suffix('.png')));await page.close()
  await b.close()
if __name__=='__main__':asyncio.run(main())

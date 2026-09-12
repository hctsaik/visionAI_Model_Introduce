"""Concrete deployment and comparison scenes using the reviewed family objects."""
from render import rect,text,line,arrow,circle,group,pill,B,N,G,O,L,PALE
from batch3_graphics import grid,caption,matrix
from batch4_graphics import pcb,bracket,sockets,label
R='#C6473D'

def card(x,y,w,lines,col=B):
 a=rect(x,y,w,55+42*(len(lines)-1),'white',col,6)
 for i,s in enumerate(lines):a+=text(x+12,y+37+i*42,s,27,col,650)
 return a

def graphic(k):
 if k=='ground-task':
  a=pcb(20,12,.76)+text(20,238,'想找的類別：resistor',30,G,700)+text(20,298,'不必先給每件的座標',29)
  return a+caption('文字描述目標，影像提供位置','工業料號能否辨識仍須另驗')
 if k=='ground-link':
  a=pcb(25,5,.75,True)+pill(55,247,320,'resistor',G)+arrow(155,242,104,174,G)+arrow(273,242,245,174,G)
  return a+caption('同一詞語可以對應兩個物件','框是相關位置，不是精確輪廓')
 if k=='vlm-task':
  a=sockets(20,8,.87)+card(20,225,437,['問題：哪一側未見螺絲？'])
  return a+caption('影像與檢查問題一起定義任務','問題需能由可見部位支持')
 if k=='vlm-observation':
  a=sockets(15,5,.72)+arrow(94,160,94,201,B)+arrow(231,160,326,201,O)
  a+=card(15,215,208,['左：有螺絲'],B)+card(248,215,221,['右：未見'],O)
  return a+caption('先逐側對照影像可見內容','此圖是證據關係，不是模型熱點')
 if k=='vlm-result':
  a=card(20,15,437,['描述：右側未見螺絲'],B)+card(20,123,437,['原因：未知'],O)+card(20,231,437,['接手：原圖＋回答＋覆核'])
  return a+caption('交出可查證的描述與未知項','不從空座推定漏裝或振動鬆脫')
 if k=='gemini-fields':
  a=card(20,15,437,['left：可見狀態','right：可見狀態','cause：已知原因或unknown'])
  a+=text(25,226,'逐欄定義要交付的內容',31,B,700)+text(25,289,'先定欄位，再對照原圖',29)
  return a+caption('這是欄位設計，不是API回覆','格式有規格，內容仍須另外核對')
 if k=='dino-failure-pair':
  a=bracket(15,20,.7)+bracket(264,20,.7,True)+rect(432,124,23,28,'none',O,0)
  a+=text(20,250,'完整支架',29,G,700)+text(265,250,'同件小缺口',29,O,700)
  return a+caption('同L支架、同孔位，只改右緣','細小變化可能在整圖表示中變弱')
 if k=='dino-failure-vectors':
  a=card(15,20,447,['完整：[.20, .80]','缺口：[.21, .79]'],B)+text(20,194,'歐氏距離 ≈ .014',35,B,700)+text(20,258,'相近 ≠ 沒有缺口',35,O,800)+text(20,307,'作者給定反例，不是模型特徵',26)
  return a+caption('特徵相似度不是允收規格','僅调門檻不能補回丟失的線索')
 if k=='dino-failure-detail':
  a=bracket(20,5,1.08,True)+rect(280,169,30,36,'none',O,0)+arrow(422,122,310,181,O)+text(324,94,'同一缺口',28,O,700)
  a+=text(20,291,'先核對原圖，再評局部方法',29,B,700)
  return a+caption('局部取樣／下游頭需另驗證','DINOv2不自動交出缺陷輪廓')
 if k=='gemini-failure-input':
  a=sockets(20,15,.9)+rect(220,36,139,150,'none',O,0)+text(20,273,'左有螺絲；右是空座',32,B,700)
  return a+caption('固定主線的同一圓接頭','只核對可見狀態，不從照片猜原因')
 if k=='gemini-failure-gates':
  a=card(20,20,440,['格式檢查：可解析 ✓'],G)+card(20,129,440,['內容檢查：右側填錯 ×'],R)
  a+=text(25,269,'右欄應記：not_visible',31,B,700)
  return a+caption('格式通過，內容仍然不通過','先回原圖查欄位，再交付工作結論')
 if k=='det-labels':
  a=pcb(30,12,.9,True)+text(22,286,'A：resistor　B：resistor',29,B,700)
  return a+caption('同一影像，兩件逐一標註','103／272是印字，類別都是電阻')
 if k=='yolo-dense':
  a=pcb(5,10,.46)+arrow(192,65,228,65)+grid(5,246,13,107)+grid(3,374,13,90)
  a+=text(237,154,'融合多尺度特徵',28,B,700)+arrow(352,172,352,205)
  a+=card(10,230,450,['各格位 → 框＋類別候選'])
  return a+caption('候選多，允許同件有重複框','格位是機制示意，不是偵測結果')
 if k=='det-map':
  a=rect(15,5,260,240,'#DCE7F1',L,6)+pcb(25,45,.6,True)+text(294,70,'縮放',28,B)+text(294,123,'補邊',28,O)
  a+=text(20,293,'原圖x = (模型x − 左補邊) / 比例',25,B,700)
  return a+caption('框先還原補邊，再除縮放比','原圖座標仍不是毫米尺寸')
 if k=='det-audit':
  a=pcb(25,12,.9)+rect(110,48,76,162,'none',O,0)
  a+=text(20,278,'A：定位偏移　B：漏框',29,R,700)
  return a+caption('示意錯誤：逐件回原圖核對','同時記錄定位與前後處理耗時')
 if k=='rt-encode':
  a=pcb(10,12,.46)+grid(4,245,12,96)+grid(2,366,12,82)+arrow(194,75,232,75)
  a+=arrow(336,127,336,160)+pill(18,177,447,'混合編碼：尺度內＋尺度間')+arrow(230,231,230,258)+text(39,305,'選query起點 → decoder',30,B,700)
  return a+caption('同一影像的多尺度表示','query由表示選出，不從真值抄框')
 if k=='rt-depth':
  a=text(20,34,'同一query起點',29,B,700)
  for y,stops,col in [(102,2,O),(225,4,B)]:
   for i in range(stops):
    x=25+i*114;a+=rect(x,y,67,53,'white',col,3)+text(x+33,y+35,str(i+1),28,col,700,'middle')
    if i<stops-1:a+=arrow(x+74,y+27,x+105,y+27,col)
  a+=text(273,137,'較少更新',28,O)+text(22,314,'較多更新：品質與耗時另測',27,B)
  return a+caption('可調輸出層依實作能力而定','圖中2／4次僅為示意，不是設定值')
 if k=='ground-prompt':
  a=pcb(15,10,.58)+card(275,16,205,['查詢：','resistor'],G)
  a+=card(20,200,438,['保存模型＋完整提示詞','換詞語就是換一項條件'])
  return a+caption('同圖改詞，候選可能改變','領域詞與料號需獨立驗證')
 if k=='ground-threshold':
  a=text(20,36,'固定同一詞：resistor',29,G,700)+text(20,102,'A：.90　B：.80　板面：.10',27,B)
  a+=card(20,147,438,['門檻.50 → 留A、B','門檻.85 → 只留A'],O)
  a+=text(20,300,'單一分数簡化例；非實測',27)
  return a+caption('詞／框門檻分別依實作保存','分數門檻不等於幾何誤差允收')
 if k=='ye-modes':
  a=card(15,12,214,['文字：','resistor'],G)+pcb(256,10,.53)+rect(291,30,47,94,'none',O,0)
  a+=text(253,183,'視覺：圈ROI',27,O,700)+text(20,231,'可選不同提示入口',32,B,700)+text(20,287,'後兩步只示範視覺SAVPE',27)
  return a+caption('文字、視覺、免提示是不同模式','不是三個模組必須依序執行')
 if k=='ye-audit':
  a=pcb(20,10,.72,True)+text(328,61,'A ↔ 框A',25,B)+text(328,112,'B ↔ 框B',25,G)
  a+=card(20,220,443,['原圖＋提示ROI＋逐件遮罩'])
  return a+caption('漏件、相似件誤報與邊界各驗','提示來源不保存，結果就難重現')
 if k=='det-partnumber':
  a=pcb(25,10,.9)+text(20,274,'103 ≠ 272',38,O,800)+text(244,276,'不能直接互換',28)
  return a+caption('同屬電阻，不代表同一規格','OCR／標籤與物料規格另核對')
 if k=='dino-input':
  a=bracket(65,12,1.0)+text(25,292,'同一L支架：兩孔位置固定',30,B,700)
  return a+caption('輸入影像，尚無良／不良判定','工件類別和缺陷規格由下游定義')
 if k=='dino-downstream':
  a=card(20,15,440,['表示向量 / patch表示'])+arrow(240,87,130,139)+arrow(240,87,362,139,G)
  a+=card(15,153,210,['標註任務頭','類別分數'])+card(255,153,210,['正常參考庫','最近距離'],G)
  a+=text(20,305,'兩個可選下游，不是固定串接',27,O)
  return a+caption('任務輸出要有資料和判定規格','骨幹特徵本身不是缺陷機率')
 if k=='dino-bank':
  a=bracket(10,12,.57)+bracket(213,12,.57)+arrow(211,167,211,214)
  a+=card(20,232,433,['參考庫：[.2,.8]、[.3,.7]'])
  return a+caption('正常參考用同一骨幹抽特徵','兩維向量僅為距離教學例')
 if k=='dino-distance':
  a=text(20,43,'待測 q = [.4, .6]',32,B,700)+text(20,111,'r1 = [.2, .8]　距離≈.283',28)+text(20,175,'r2 = [.3, .7]　距離≈.141',28,G,700)+arrow(237,206,237,239)+text(30,294,'最近：r2；距離不是缺陷率',29,G,700)
  return a+caption('同一特徵空間的歐氏距離例','換骨幹或前處理，庫也須重驗')
 if k=='dino-review':
  a=bracket(10,15,.7)+bracket(278,15,.7)+text(20,227,'待測支架',29,B)+text(274,227,'最近參考',29,G)+text(20,302,'先核對孔位、表面與條件',30)
  return a+caption('保留原圖和參考來源便於覆核','沒有像素標註就不能宣稱輪廓精度')
 if k=='dino-background':
  a=rect(10,18,218,222,'#DFE6ED','none',6)+rect(251,18,218,222,'#D9ECD8','none',6)+bracket(30,35,.67)+bracket(271,35,.67)
  a+=text(20,300,'同件、同孔位；只改背景',31,B,700)
  return a+caption('條件變化不等於工件缺陷','示意控制變因，不是新模型測試')
 if k=='dino-shift':
  a=card(20,18,436,['原背景：距離 .14','新背景：距離 .29'],B)+text(20,186,'給定反例：距離可能變',30,O,700)+text(20,247,'兩張圖的工件都未改變',30)+text(20,302,'先查正常變化是否有覆蓋',28)
  return a+caption('分數改變，不能直接判不良','距離與門檻都要用域內資料驗證')
 if k in ['vlm-contract','gemini-contract']:
  a=sockets(15,12,.63)+card(20,188,448,['固定原圖＋完整問題','模型識別／schema／生成設定' if k=='gemini-contract' else '模型／processor／生成設定'])
  return a+caption('請求與回覆都要可追溯','服務版本變動另做回歸' if k=='gemini-contract' else '不同LLaVA版本需核對處理方式')
 if k=='vlm-audit':
  a=sockets(15,10,.68)+text(22,210,'右側未見螺絲：圖中可核對',27,B,700)+text(22,262,'原因／遮擋：保持未知',29,O,700)+text(22,312,'低可信 → 原圖與回答交覆核',27)
  return a+caption('回答、位置證據與決策分開','流暢文字不能作自動放行依據')
 if k=='vlm-scene':
  a=sockets(15,15,1)+text(25,279,'左：可見螺絲　右：空座',30,B,700)
  return a+caption('兩候選共用同一接頭影像','先固定需要交付的欄位與允收')
 if k=='vlm-roi':
  a=sockets(10,10,.72)+rect(42,35,99,101,'none',B,0)+rect(177,35,99,101,'none',O,0)
  a+=text(340,69,'左ROI',26,B)+text(340,130,'右ROI',26,O)+arrow(172,171,172,220)+card(20,234,437,['固定座位：有／未見／待覆核'])
  return a+caption('固定問題可另評專用分類器','仍需遮擋資料、門檻與誤判驗證')
 if k=='qwen-input':
  a=label(30,10,1.13)+text(24,278,'局部工作欄位：批號B08',31,B,700)
  return a+caption('原銘牌批號欄位的簡化示意','保留可讀字符，再問模型讀取')
 if k=='qwen-budget':
  a=label(20,10,.75)+card(20,191,436,['像素預算＋長寬比','processor＋模型版本'])
  return a+caption('設定變更會影響視覺token','應用硬體實測記憶體與完整耗時')
 if k=='qwen-uncertain':
  a=card(20,20,433,['清楚：B08 → 核對後保存'],G)+card(20,128,433,['不清：B0? → 重拍／未知'],O)
  a+=text(25,281,'文字是情境示意，非降採樣結果',25)
  return a+caption('別用常見批號補造看不清的字','原像素不足時，更多token也有限')
 if k=='qwen-check':
  a=label(15,10,.72)+text(305,85,'真值B08',27,G,700)+card(20,202,437,['逐字錯誤／未知率／覆核量','加入前後處理與網路耗時'])
  return a+caption('格式與可讀內容分別核對','題目、欄位與測試集都需固定')
 if k=='qwen-ocr':
  a=label(20,10,.8)+arrow(174,176,174,219)+card(20,229,434,['固定ROI → OCR → B08'])
  return a+caption('同欄位比較字串，不假造勝負','版面變動、不清字符和時延各驗')
 raise ValueError(k)

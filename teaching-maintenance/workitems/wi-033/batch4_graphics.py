"""Original vector scenes; every numeric example is illustrative."""
from render import rect,text,line,arrow,circle,group,pill,B,N,G,O,L,PALE
from batch3_graphics import grid,matrix,caption
R='#C6473D'

def pcb(x=30,y=25,s=1,boxes=False):
 a=rect(0,0,390,240,'#D9ECE6','#77A796',12)
 for xx,num,name in [(105,'103','A'),(270,'272','B')]:
  a+=line(xx,0,xx,240,'#92B6A2',12)+rect(xx-30,40,60,155,'#9AA6AC','#6F7F88',5)+rect(xx-30,65,60,105,'#243B40','#243B40',2)
  a+=text(xx,123,num,25,'white',700,'middle')+text(xx,223,name,25,N,700,'middle')
  if boxes:a+=rect(xx-42,28,84,180,'none',B,0)
 return group(x,y,s,a)

def bracket(x=25,y=25,s=1,defect=False):
 path='M0 0 H110 V140 H260 V160 H250 V177 H260 V220 H0 Z' if defect else 'M0 0 H110 V140 H260 V220 H0 Z'
 a='<path d="'+path+'" fill="url(#steel)" stroke="#748A9C" stroke-width="4"/>'
 a+=circle(55,62,23,'#748A9C','white')+circle(209,180,23,'#748A9C','white')
 return group(x,y,s,a)

def sockets(x=25,y=25,s=1):
 a=rect(0,0,410,205,'#34424B','#23333D',15)
 for xx in [112,300]:
  a+=circle(xx,103,67,'#82939F','#1F2B33')+circle(xx,103,43,'#566671','#101B22')
 a+=circle(112,103,32,'#AAB6BD','#CAD3D8')+line(89,103,135,103,'#596D79',6)+line(112,80,112,126,'#596D79',6)
 return group(x,y,s,a)

def label(x=30,y=25,s=1):
 return group(x,y,s,rect(0,0,360,175,'#DDE4E8','#8799A6',8)+rect(25,25,310,124,'white',L,3)+text(45,65,'批號 / LOT',25)+text(45,124,'B08',48,N,800))

def graphic(k):
 k=k.removeprefix('b4-')
 if k=='yolo-candidates':
  a=pcb(10,5,.83)
  for dx,dy,c in [(0,0,B),(8,7,O),(-8,-6,R)]:a+=rect(58+dx,26+dy,70,149,'none',c,0)
  a+=rect(199,26,70,149,'none',G,0)+text(351,44,'A .93',25,B)+text(351,88,'A .87',25,O)+text(351,132,'A .76',25,R)+text(351,176,'B .91',25,G)
  return a+caption('A重複三框；B另有一框','框與分數是作者給定算例')
 if k=='yolo-nms':
  a=text(20,42,'排序：.93 > .91 > .87 > .76',27,B,700)
  for i,(s,v,c) in enumerate([('A .93','保留',B),('B .91','保留',G),('A .87','與A重疊 → 刪',O),('A .76','與A重疊 → 刪',R)]):a+=text(25,101+i*57,s,29,c,700)+text(190,101+i*57,v,28,c)
  return a+caption('同類別框：IoU > 0.5才抑制','B與A不重疊，不會被A刪除')
 if k in ['yolo-output','rt-output','ground-output','ye-output']:
  scale=.83 if k=='yolo-output' else .9
  a=pcb(10 if k=='yolo-output' else 25,15,scale,True)
  if k=='ye-output':
   for x in [92.5,241]:a+='<g opacity=".5">'+rect(x,51,54,139.5,'#72C4BD',G,5)+'</g>'
  a+=text(30,300,{'yolo-output':'A .93　B .91','rt-output':'q1：A　q2：B　q3：淘汰','ground-output':'resistor → A、B框','ye-output':'A、B：相似類別的框與遮罩'}[k],28,B,700)
  return a+caption('回原圖查漏件與框的位置',{'yolo-output':'去重不能補回未產生的候選','rt-output':'示意分數篩選；不用NMS','ground-output':'詞語與框，不是像素遮罩','ye-output':'相似外觀不保證料號相同'}[k])
 if k=='rt-match':
  for i,lab in enumerate(['q1','q2','q3']):
   a='' if i==0 else a
   a+=pill(20,30+i*90,90,lab)+arrow(125,53+i*90,262,53+i*90)+pill(280,30+i*90,180,['真值A','真值B','背景'][i],G if i<2 else O)
  return a+caption('一個真值只分配一個query','訓練用匹配；推論不讀真值')
 if k=='rt-refine':
  a=pcb(25,15,.9)+rect(64,23,126,194,'none',O,0)+rect(78,37,91,166,'none',B,0)+text(20,282,'起點框',28,O)+arrow(150,270,245,270)+text(267,282,'修正框',28,B)
  return a+caption('decoder取影像線索更新框','圖示q1；其他query也各自更新')
 if k=='ground-input':
  a=pcb(10,8,.55)+arrow(240,65,288,65)+pill(304,43,170,'影像特徵')
  a+=rect(15,201,205,55,'white',L,6)+text(28,237,'resistor',30,G)+arrow(237,228,288,228,G)+pill(304,206,170,'文字token',G)
  return a+caption('同一PCB，查詢「電阻」','兩路編碼後進入特徵互動')
 if k=='ground-align':
  a=text(150,34,'區域A　區域B　板面',25,B)+text(10,91,'詞',26,G)
  a+=matrix([[.9,.8,.1]],92,53,116)+text(20,226,'resistor ↔ 區域表示',32,B,700)+arrow(55,264,431,264)+arrow(431,292,55,292,G)
  return a+caption('詞與影像特徵交換訊息','數值是相容性示意，不是實測')
 if k=='ye-roi':
  a=pcb(20,15,.9)+rect(76,35,92,168,'none',O,0)+text(20,290,'圈選A作為視覺提示',31,O,700)
  return a+caption('參考ROI指定想找的外觀','本圖只走SAVPE視覺提示模式')
 if k=='ye-pool':
  a=text(20,42,'語意特徵　　啟動權重',28,B,700)+text(25,100,'[2, 0]　 ×　0.75',32)+text(25,162,'[0, 2]　 ×　0.25',32)+line(25,187,437,187,L,2)+arrow(237,202,237,235)+text(80,286,'提示表示 [1.5, 0.5]',32,G,700)
  return a+caption('ROI啟動權重做加權聚合','兩維算例；不是模型真實維度')
 if k=='dino-views':
  a=bracket(22,22,.76)+bracket(286,67,.48)+rect(292,104,52,53,'#879CB1',B,1)+text(20,266,'全圖視圖',29,B)+text(265,266,'遮蔽視圖',29,O)
  return a+caption('同一支架，產生不同視圖','不是把兩個工件當同一目標')
 if k=='dino-learn':
  a=pill(15,28,210,'Teacher',G)+pill(260,28,210,'Student')+text(23,115,'目標停止梯度',27,G)+text(270,115,'預測表示',28,B)+text(24,175,'[.2, .8]',30,G,700)+text(280,175,'[.6, .4]',30,B,700)+arrow(180,162,265,162,G)+text(60,217,'Student學習對齊目標',30,B,700)+arrow(363,262,121,262,O)+text(105,304,'EMA更新Teacher',27,O)
  return a+caption('整圖自蒸餾＋局部遮蔽目標','學表示，不是重建原始像素')
 if k=='dino-deploy':
  a=bracket(12,15,.46)+arrow(140,73,185,73)+pill(200,49,257,'預訓練骨幹')+arrow(321,112,321,149)+text(35,211,'整圖：[.2, .8, …]',31,B,700)+grid(3,300,165,128)+text(23,286,'查庫／分類',28)+text(290,323,'局部patch',25)
  return a+caption('部署抽特徵，再接下游任務','此處不需要Teacher與訓練配對')
 if k=='llava-encode':
  a=sockets(15,15,.85)+arrow(192,204,192,242)+pill(24,259,400,'視覺編碼器 → 影像表示')
  return a+caption('左座有螺絲，右座未見螺絲','固定同一照片，保留可見證據')
 if k=='llava-project':
  a=text(20,45,'影像表示 [a, b, …]',31,B,700)+arrow(218,65,218,104)+pill(25,117,400,'原版：學習線性投影')+arrow(218,170,218,203)+text(20,244,'視覺token＋「哪邊有螺絲？」',27)+text(20,300,'→ 語言模型輸入空間',31,G,700)
  return a+caption('投影橋接不同表示空間','示意向量長度不是實際維度')
 if k=='llava-answer':
  a=sockets(25,12,.66)+text(22,204,'左側 → 可見 → 螺絲',31,B,700)+text(22,254,'右側 → 未見 → 螺絲',31,B,700)+text(22,301,'原因：未知',29,O,700)
  return a+caption('逐token回答仍可能犯錯','空座不能證明漏裝或鬆脫原因')
 if k=='qwen-dynamic':
  a=label(10,15,.56)+grid(2,300,15,100)+label(10,160,.76)+grid(3,320,170,130)
  return a+caption('長寬比／解析度影響token數','格數是示意；仍有像素預算')
 if k=='qwen-position':
  a=grid(3,34,40,225,mark=(1,2))+text(300,78,'t：時間',28,B,700)+text(300,142,'h：高度',28,G,700)+text(300,206,'w：寬度',28,O,700)+text(32,307,'M-RoPE → 帶位置的表示',30,B,700)
  return a+caption('圖像／影片保留空間與時間','單張影像仍有高度與寬度')
 if k=='qwen-answer':
  a=label(35,10,.92)+text(25,221,'問題：批號是什麼？',30)+text(25,275,'可見答案：B08',34,B,700)
  return a+caption('以原圖可讀文字核對回答','若像素只剩B0?，保留不確定')
 if k=='gemini-request':
  a=sockets(15,8,.69)+text(20,196,'問題：逐側核對螺絲',30,B,700)+text(20,253,'欄位：left / right / cause',28)+text(20,305,'固定影像與欄位要求',29)
  return a+caption('公開API的輸入／輸出介面','不臆測服務內部視覺架構')
 if k=='gemini-json':
  a=rect(10,15,467,285,'white',L,8)
  for i,t in enumerate(['{','  "left": "present",','  "right": "present",','  "cause": "unknown"','}']):a+=text(25,58+i*49,t,28,R if i==2 else N,600)
  return a+caption('反例：JSON格式能解析','右側內容仍錯；作者設計回覆')
 if k=='gemini-check':
  a=sockets(25,8,.65)+text(20,203,'left：present　✓',29,G,700)+text(20,254,'right：not_visible',29,B,700)+text(20,305,'cause：unknown',29,O,700)
  return a+caption('逐欄對照影像證據才驗內容','本圖沒有呼叫API或重跑模型')
 from batch4_expanded_graphics import graphic as expanded
 return expanded(k)

"""New vector evidence scenes for classification, segmentation and keypoints."""
from render import rect,text,line,arrow,circle,group,plate,pill,bars,B,N,G,O,L,PALE
R='#C6473D';P='#8060A4'
def matrix(vals,x=25,y=60,cell=76,col=B,labels=True):
 a=''
 for i,row in enumerate(vals):
  for j,v in enumerate(row):
   a+=rect(x+j*cell,y+i*cell,cell-5,cell-5,('#DBEAFE' if v>=0 else '#FCE5DD'),col,5)
   if labels:a+=text(x+j*cell+(cell-5)/2,y+i*cell+cell*.64,str(v),31,col,700,'middle')
 return a
def grid(n,x,y,size=155,mark=None,col=B):
 a='';d=size/n
 for i in range(n):
  for j in range(n):a+=rect(x+j*d,y+i*d,d-2,d-2,O if (i,j)==mark else '#E3EEF9',col,1)
 return a
def caption(a,b):return text(15,350,a,29,N,700)+text(15,397,b,27)
def wire(x=40,y=50,s=1,gap=False,mask=False):
 a=rect(0,0,385,210,'#EAF0F5','#73899E',12)
 a+=rect(20,28,72,144,'#ADBCC7','#73899E',6)+rect(295,28,72,144,'#ADBCC7','#73899E',6)
 a+=f'<path d="M65 103 H155 L182 71 H236 L263 103 H325" fill="none" stroke="{B if mask else "#B88842"}" stroke-width="{13 if mask else 10}" stroke-linejoin="round"/>'
 if gap:a+=rect(184,60,16,24,'#EAF0F5','none',0)
 return group(x,y,s,a)
def scaffold():
 return grid(4,20,20,112)+arrow(145,77,194,157)+grid(2,200,134,90)+arrow(296,175,339,79)+grid(4,351,20,112)
def masks(x,y,s=1,mode='both'):
 a=rect(0,0,210,140,'white',L,4)
 for xx,yy,which in [(8,8,'top'),(110,75,'bottom')]:
  if mode in ['both','signed',which]:
   col=P if mode=='signed' and which=='bottom' else B
   body='<path d="M0,0 H95 L120,35 H250 V160 H0 Z" fill="'+col+'"/>'
   for cx in [60,190]:body+=circle(cx,102,24,'white','white')
   a+=group(xx,yy,.35,body)
 return group(x,y,s,a)
def scores(name):
 a=plate(12,12,.61,True)+text(230,60,name,31,B,700)
 a+=group(0,126,.93,bars(['完整','刮傷'],[.18,.82]))
 return a+caption('分數對應事先定義的類別','教學给定分數；不是位置圖')
def audit_pair(kind='class'):
 a=plate(15,35,.67,True)+plate(276,35,.67,False)
 a+=text(20,198,'真刮傷',30,O,700)+text(278,198,'允收正常',30,G,700)
 if kind=='class':a+=text(15,265,'查漏判',32,O,700)+text(277,265,'查錯拒',32,O,700)
 else:a+=text(15,265,'邊界／位置',30,B,700)+text(277,265,'誤報',30,O,700)
 return a
def kpt_plate(occluded=False):
 a=plate(40,50,1.1,False,True)
 if occluded:a+=rect(221,120,100,111,'#D8E0E8','#A7B4C2',5)+text(222,255,'C被遮住',29,O,700)
 return a
def scene(k):
 if k=='res-data':
  a=plate(15,35,.72,False)+plate(266,35,.72,True)+pill(15,198,198,'完整',G)+pill(266,198,198,'刮傷',O)
  return a+caption('影像與類別標註一一配對','按工件／批次分訓練與測試')
 if k=='class-common':return scene('res-data').replace('影像與類別標註一一配對','共同照片、標籤與留出批次').replace('按工件／批次分訓練與測試','候選模型各用相容前處理')
 if k=='res-residual':
  a=plate(10,10,.46,True)+arrow(141,55,195,55)+matrix([[2,1],[0,3]],222,15,48)
  a+=arrow(271,121,271,163)+text(16,208,'x + F(x)',34,B,700)+matrix([[3,1],[2,2]],254,183,48)
  return a+caption('主路學修正，直通保留輸入','更新的是表示，不是修補工件')
 if k in ['res-score','cnx-score']:return scores('ResNet' if k=='res-score' else 'ConvNeXt')
 if k in ['res-contract','cnx-contract']:
  a=plate(25,35,.9,True)+rect(31,38,223,148,'none',O,0)+text(286,83,'裁切固定',29,O,700)+text(286,146,'縮放固定',29,B,700)
  a+=rect(20,228,439,70,'white',L,6)+text(34,273,'類別0：完整　類別1：刮傷',28,B,700)
  return a+caption('權重與類別順序一起保存','不能交換分數欄位再交付')
 if k in ['res-pool','cnx-pool']:
  a=matrix([[2,0],[0,2]],15,25,66)+arrow(169,88,237,88)+text(269,77,'平均 = 1',33,B,700)
  a+=matrix([[1,1],[1,1]],15,180,66)+arrow(169,243,237,243)+text(269,232,'平均 = 1',33,B,700)
  return a+caption('彙整後可交分類頭','不同空間圖可能有相同平均')
 if k in ['res-review','cnx-review','vit-review']:return audit_pair()+caption('同一留出集，逐類核對錯誤','時間包括取像、前處理與交付')
 if k=='common-background':
  a=rect(12,22,220,186,'#E5E7EB','none',6)+rect(261,22,220,186,'#DDEAD7','none',6)+plate(29,46,.7,True)+plate(278,46,.7,True)
  return a+text(15,271,'工件不變，只改背景',32,B,700)+caption('缺陷仍是同一條刮傷','比較兩張是否被分到同一類')
 if k=='res-scope':return scores('整圖分類').replace('分數對應事先定義的類別','整件類別，沒有刮傷座標')
 if k=='res-alternative':
  a=plate(40,30,1,True)+rect(156,77,31,57,'none',O,0)+text(15,257,'像素標註 → 分割訓練',31,B,700)
  return a+caption('需要位置，另評像素輸出','多付標註成本；仍需誤差驗證')
 if k=='cnx-block':
  a=plate(10,20,.52,True)+arrow(158,66,221,66)+grid(4,245,12,115,mark=(1,1))
  a+=pill(15,191,188,'空間鄰域')+arrow(217,215,260,215)+pill(274,191,188,'通道組合',G)
  return a+caption('局部線索逐層彙整成表示','純卷積區塊；另有殘差路徑')
 if k=='vit-patches':
  a=plate(15,32,1.2,True)
  for x in range(15,316,60):a+=line(x,32,x,224,B,2)
  for y in range(32,225,48):a+=line(15,y,315,y,B,2)
  a+=text(20,288,'同一影像切片，內容未換件',29,B,700)
  return a+caption('每一片投影成一個token','格線是分片，不是缺陷分割')
 if k=='vit-tokens':
  a=''
  for i,col in enumerate([B,G,O]):
   x=15+i*160;a+=rect(x,33,123,107,'#E3EEF9',col,7)+text(x+23,96,f'片{i+1}',31,col,700)+text(x+35,179,'+',33,col,700)+rect(x,210,123,51,'white',col,7)+text(x+8,246,f'位置{i+1}',27,col,700)
  return a+caption('內容表示與位置表示相加','位置不是替換掉原始內容')
 if k=='vit-cls':
  a=''
  for i in range(3):a+=pill(12+i*162,28,136,f'片{i+1}')+arrow(78+i*162,79,238,144)
  a+=pill(142,163,210,'分類token')+arrow(247,215,247,254)+text(58,297,'完整0.18／刮傷0.82',32,B,700)
  return a+caption('交換資訊後，分類頭讀出CLS','給定分類例；不是位置熱圖')
 if k in ['vit-resolution','seg-resolution']:
  a=wire(9,5,.54)+text(15,150,'細線輸入',29,B,700)+wire(245,5,.54)+text(245,150,'粗格取樣位置',28,O,700)
  for xx in range(250,449,25):a+=line(xx,5,xx,119,O,1)
  for yy in range(5,120,25):a+=line(245,yy,453,yy,O,1)
  a+=line(15,216,445,216,L,2)+text(15,272,'先確認需要的線索仍在',31,B,700)
  return a+caption('更多輸出格不等於更多觀測','同件、同缺陷，改輸入解析度')
 if k=='vit-cost':
  a=grid(2,17,35,144)+grid(4,278,35,144)+text(22,228,'4 tokens',32,B,700)+text(272,228,'16 tokens',32,B,700)
  a+=text(15,293,'配對數：16 → 256',32,O,700)
  return a+caption('標準注意力配對隨N²增長','簡化算例；其他運算另計')
 if k=='unet-data':
  a=wire(12,12,.53)+wire(247,12,.53,mask=True)+text(18,178,'原圖',31,B,700)+text(249,178,'像素真值',31,G,700)
  a+=text(15,270,'焊線／背景，格位需對齊',30,B,700)
  return a+caption('像素標註定義要學的區域','按批次留出，避免同件洩漏')
 if k=='unet-bridge':
  a=scaffold()+line(135,21,340,21,G,5)+arrow(340,21,340,83,G,5)+text(181,60,'跳接',31,G,700)
  a+=wire(145,224,.4,mask=True)
  return a+caption('粗尺度上下文接回細位置','同尺度串接，再學融合')
 if k in ['unet-output','seg-output']:
  a=wire(10,25,.57)+arrow(242,89,281,89)+wire(290,45,.46,mask=True)
  a+=text(12,257,'藍色＝焊線類；其餘＝背景',28,B,700)
  return a+caption('輸出每個像素的語意類別','相同類別，不代表不同實例ID')
 if k=='unet-contract':
  a=wire(25,20,.85)+rect(54,51,260,106,'none',O,0)+arrow(192,197,192,236)+rect(55,247,330,51,'white',B,0)+text(66,283,'ROI → resize → padding',26,B,700)
  return a+caption('裁切起點、比例與補邊要留存','後續用同一映射還原像素')
 if k=='unet-map':
  a=wire(15,20,.53,mask=True)+arrow(240,91,274,91)+wire(277,34,.5,mask=True)
  a+=text(15,245,'模型格位 → 還原ROI',31,B,700)+text(15,291,'同一條線，回到原圖位置',30,B,700)
  return a+caption('還原resize与padding後疊回','不能把模型座標直接當原圖')
 if k in ['unet-review','seg-review']:
  a=wire(10,14,.53)+wire(247,14,.53,gap=True,mask=True)+text(17,180,'原圖連續',30,B,700)+text(248,180,'候選斷裂',30,O,700)
  a+=text(15,270,'連通／邊界／錯分／延遲',29,B,700)
  return a+caption('檢查最窄位置，不只看IoU','物理尺寸另需校正與誤差驗證')
 if k in ['unet-line','unet-gap']:
  gap=k=='unet-gap';a=wire(30,20,1,gap=gap,mask=gap)+rect(204,71,68,44,'none',O,0)
  a+=text(30,290,'同位置：'+('中間缺一段' if gap else '完整跨過細縫'),31,O,700)
  return a+caption('放大中央窄線核對連通','真值與候選只改同一小段')
 if k=='unet-boundary':
  a=wire(15,12,.55)+wire(245,12,.55,gap=True,mask=True)+text(18,200,'真值：連續',30,G,700)+text(247,200,'候選：斷裂',30,O,700)
  return a+text(15,270,'大區域相近，不代表連通',31,B,700)+caption('單独記細線斷裂與邊界誤差','相同標註規則下比較候選')
 if k in ['yseg-scene','yseg-data']:
  a=plate(15,20,.65)+plate(264,168,.65)+text(22,165,'甲',30,B,700)+text(421,218,'乙',30,G,700)
  if k=='yseg-data':a+=rect(12,15,172,115,'none',B,0)+rect(261,163,172,115,'none',G,0)
  return a+caption('兩件同類支架，在同一影像','逐件標註輪廓與類別')
 if k=='yseg-branches':
  a=grid(4,15,76,118)+arrow(148,132,240,60)+arrow(148,139,240,239)
  a+=pill(252,28,215,'共享原型P')+pill(252,210,215,'每框係數c',G)
  return a+caption('同一特徵，分出兩種產物','P与c再組合；兩者不是串接')
 if k in ['yseg-output','yseg-semantic']:
  a=masks(30,15,1.8,'both')
  if k=='yseg-output':a+=text(211,76,'甲',31,B,700)+text(185,220,'乙',31,G,700)
  else:a+=text(20,312,'兩塊都屬「支架」類',31,B,700)
  return a+caption('孔洞仍是背景，不填滿',('甲／乙為本影像實例' if k=='yseg-output' else '語意類別不等於逐件身份'))
 if k=='yseg-pair':
  a=scene('yseg-coef').split(text(15,350,'每個框保留自己的係數',29,N,700))[0]
  return a+caption('框索引與係數索引一一對應','過濾候選時一併保留或移除')
 if k=='yseg-filter':
  a=plate(20,50,.55)+rect(15,45,148,99,'none',B,0)+rect(23,52,148,99,'none',O,0)+arrow(192,96,277,96)+plate(308,50,.55)+rect(303,45,148,99,'none',B,0)
  a+=text(15,256,'去重保留甲 → 同索引係數',30,B,700)
  return a+caption('保留候選的幾何不因去重改變','相同框与係數用來產生遮罩')
 if k=='yseg-review':return masks(20,15,1.8,'both')+text(15,310,'核對空孔與相鄰件分離',30,B,700)+caption('遮罩、框、分數和原圖一起存','精密輪廓與尺寸另做誤差驗證')
 if k=='kpt-data':return kpt_plate()+caption('A是缺口角，B/C是具名孔心','自訂工件需定義並標註點名')
 if k=='kpt-heatmaps':return scene('kpt-decode')
 if k=='kpt-occluded':return kpt_plate(True)+caption('同件C孔被遮住，A/B仍可見','標註可見性與點身份要分開')
 if k=='kpt-estimate':
  a=kpt_plate(True)+circle(249,164,8,O)+line(236,149,262,178,O,3,True)+text(17,301,'C是估計，不代表已看見',30,O,700)
  return a+caption('保留每點分數與原圖','遮擋點另評，不以有座標放行')
 if k=='kpt-review':
  a=kpt_plate()+text(25,291,'具名2D點 + K + 已知3D',29,B,700)
  return a+caption('另接PnP，再核對重投影','點數、退化與校正都需檢查')
 if k=='kpt-scope':return kpt_plate()+text(20,298,'A ↔ A，B ↔ B，C ↔ C',30,B,700)+caption('具名2D座標供幾何對應','點的可信度與可見性另查')
 if k=='kpt-mask':return masks(30,25,1.7,'top')+caption('分割交物件區域，並非點名','要孔心仍需定義提取與驗證')
 if k=='res-split':
  a=matrix([[2,1],[0,3]],25,40,68)+text(25,25,'輸入特徵 x',30,B,700)
  a+=arrow(170,106,250,106)+pill(260,75,210,'學習修正 F')
  a+=line(190,106,190,248)+arrow(190,248,440,248,G)+text(202,288,'直通仍是同一x',28,G,700)
  return a+caption('一份輸入，兩條路徑','藍路學修正；綠路保留輸入')
 if k=='res-delta':
  a=matrix([[2,1],[0,3]],20,65,64)+arrow(161,125,213,125)+matrix([[1,0],[2,-1]],249,65,64,O)
  a+=text(30,38,'x',30,B,700)+text(251,38,'F(x)',30,O,700)
  return a+text(20,260,'卷積層學的是修正量',31,B,700)+caption('修正可以增加，也可以減少','F(x)是特徵，不是修復照片')
 if k=='res-sum':
  a=matrix([[2,1],[0,3]],15,35,61,G)+text(150,113,'+',40,B,800)+matrix([[1,0],[2,-1]],208,35,61,O)
  a+=line(380,100,432,100)+line(432,100,432,266)+arrow(432,266,397,266)+matrix([[3,1],[2,2]],265,205,61,B)+text(15,245,'對應格相加',30,B,700)
  return a+caption('x + F(x) → 更新後的表示','形狀不同，先投影或對齊')
 if k=='cnx-spatial':
  a=grid(4,20,50,164,mark=(1,1))+grid(4,294,50,164,mark=(1,1),col=G)
  for x in [20,294]:a+=rect(x+1,y:=51,121,121,'none',O,0)
  a+=text(20,25,'通道A',29,B,700)+text(294,25,'通道B',29,G,700)
  a+=text(10,274,'鄰域例：1 + 2 + 0 = 3',31,B,700)
  return a+caption('空間卷積：通道彼此不混合','小格僅示意；原始核為7×7')
 if k=='cnx-channel':
  a=grid(3,20,32,116,mark=(1,1))+grid(3,20,183,116,mark=(1,1),col=G)
  a+=text(63,107,'2',30,N,800)+text(63,258,'5',30,N,800)
  a+=arrow(151,90,242,171)+arrow(151,240,242,190,G)+rect(257,130,206,114,'#EDE6F5',P,12)+text(268,169,'½×2+½×5',28,P,700)+text(283,218,'= 3.5',32,P,700)
  return a+caption('看的是同位置的不同線索','擴張通道、非線性，再縮回')
 if k=='cnx-residual':
  a=grid(3,10,95,97)+arrow(119,145,159,145)+pill(168,105,199,'空間→通道')+arrow(375,145,431,145)+circle(449,145,21,B,'white')+text(449,155,'+',32,B,700,'middle')
  a+=line(124,146,124,41,G)+line(124,41,449,41,G)+arrow(449,41,449,113,G)
  return a+text(20,249,'同形狀輸入沿上方保留',31,G,700)+caption('主路結果再加直通輸入','兩路相加，不是相互替代')
 if k=='vit-query':
  a=plate(20,20,.88,True)+rect(123,60,47,54,'none',O,0)+rect(166,87,45,49,'none',G,0)
  a+=line(146,116,88,224,O,3,True)+line(191,139,302,224,G,3,True)
  a+=pill(20,237,190,'刮傷片',O)+pill(257,237,190,'孔邊片',G)
  return a+caption('同一圖，不同位置各有表示','框是分片示意，不是偵測框')
 if k=='vit-attention':
  a=pill(15,126,119,'查詢Q')+arrow(143,143,226,69,O,7)+arrow(143,160,226,245,G,4)
  a+=pill(247,34,217,'值A：[2,0]',O)+pill(247,213,217,'值B：[0,4]',G)
  a+=text(157,89,'0.75',28,O,700)+text(156,247,'0.25',28,G,700)
  return a+caption('依相關程度，取不同份量','權重是教學給定，非缺陷率')
 if k=='vit-update':
  a=text(15,50,'0.75 × [2,0]',34,O,700)+text(15,102,'+ 0.25 × [0,4]',34,G,700)+line(15,132,433,132,L,3)+text(15,185,'= [1.5,1]',39,B,800)
  a+=arrow(228,209,228,247)+pill(90,263,283,'分類token再讀出')
  return a+caption('本例展示加權，不是平均貼圖','實際還有多頭、殘差與MLP')
 if k=='unet-encode':
  a=wire(5,10,.52)+line(68,151,419,151,L,2)+grid(6,18,184,118,mark=(2,3))+arrow(156,242,211,242)+grid(3,237,196,104,mark=(1,1))
  return a+caption('小格變少，上下文範圍變大','細線位置在粗尺度更難分開')
 if k=='unet-skip':
  a=scaffold()+line(136,21,340,21,G,5)+arrow(340,21,340,83,G,5)+text(193,65,'跳接',30,G,700)
  a+=grid(4,10,226,93)+text(126,284,'串接',32,G,700)+grid(4,253,226,93,col=G)+text(355,284,'融合',28,B,700)
  return a+caption('編碼細節送到對應解碼尺度','拼接特徵，不是直接相加')
 if k=='unet-decode':
  a=grid(3,18,48,110,mark=(1,1))+arrow(147,111,209,111)+grid(6,241,32,168,mark=(2,3))
  a+=arrow(327,211,327,232)+wire(181,241,.38,mask=True)
  return a+caption('上採樣後融合，再逐像素判類','藍色線是語意遮罩示意')
 if k=='seg-scales':
  a=''
  for i,(n,size) in enumerate([(8,130),(4,105),(2,78),(1,54)]):
   x=12+i*120;y=40+i*43;a+=grid(n,x,y,size,mark=(0,0))+text(x,y+size+37,f'尺度{i+1}',26,B,700)
  return a+caption('同件表示，四種空間粒度','較粗格也對應原圖區域')
 if k=='seg-align':
  a=''
  for i,n in enumerate([8,4,2,1]):
   yy=20+i*73;a+=grid(n,15,yy,55,mark=(0,0))+arrow(84,yy+26,215,yy+26)+grid(8,233,yy,55,mark=(0,0))
  a+=text(304,94,'投影',32,B,700)+text(304,166,'上採樣',32,B,700)+text(304,238,'同格位',32,B,700)
  return a+caption('四路先對齊空間與通道','不是拿不同格位直接相加')
 if k=='seg-fuse':
  a=''
  for i in range(4):a+=grid(4,20+i*16,20+i*16,110,col=[B,G,O,P][i])
  a+=arrow(197,109,257,109)+pill(271,78,188,'串接＋融合')+arrow(363,138,363,197)+wire(200,215,.43,mask=True)
  return a+caption('學習各尺度如何共同判斷','融合後才輸出每像素類別')
 if k=='yseg-proto':
  a=grid(4,15,47,112)+arrow(140,105,214,60)+arrow(140,105,214,213)
  a+=masks(245,4,.8,'both')+text(250,140,'P1：甲+乙',28,B,700)
  a+=masks(245,171,.8,'signed')+text(250,310,'P2：甲−乙',28,P,700)
  return a+caption('原型是可組合的空間基底','原型本身不等於某一件物體')
 if k=='yseg-coef':
  a=plate(15,20,.55)+plate(268,145,.55)
  a+=rect(9,14,154,106,'none',B,0)+rect(260,135,160,118,'none',G,0)
  a+=text(186,65,'甲：[½,½]',32,B,700)+text(8,216,'乙：[½,−½]',30,G,700)
  return a+caption('每個框保留自己的係數','兩係數為簡化例，非實測')
 if k=='yseg-combine':
  a=text(15,40,'甲：½P1 + ½P2',33,B,700)+text(15,92,'乙：½P1 − ½P2',33,G,700)
  a+=arrow(240,115,240,148)+masks(15,171,1,'top')+masks(248,171,1,'bottom')
  return a+caption('組合後再依自己的框取遮罩','實際原型、係數由訓練學得')
 if k=='kpt-roi':
  a=rect(10,10,466,261,'white',L,10)+plate(107.5,100,.5,False,True)+rect(100,50,200,160,'none',B,0)
  a+=text(17,301,'框：(100,50)，200×160',28,B,700)
  return a+caption('ROI從原圖取得同件特徵','孔心B/C與缺口A始終對應')
 if k=='kpt-decode':
  a=''
  for i,(label,pos,col) in enumerate([('A',(1,1),O),('B',(2,0),B),('C',(2,2),G)]):
   x=15+i*158;a+=grid(4,x,72,138,mark=pos,col=col)+text(x+60,42,label,36,col,800,'middle')
  a+=text(15,265,'每個點各有一張位置分布',30,B,700)
  return a+caption('分開解碼，才不會弄丟點名','色塊為示意，不是實測熱圖')
 if k=='kpt-map':
  a=rect(12,20,186,149,'white',B,0)+circle(63,67,8,O)+text(215,62,'u=0.275',30,O,700)+text(215,107,'v=0.3125',30,O,700)
  a+=text(15,216,'x = 100 + 0.275×200',30,B,700)+text(15,262,'y = 50 + 0.3125×160',30,B,700)+text(15,311,'A → (155,100)',36,O,800)
  return a+caption('原點與尺度一起還原','連續座標算例，格心依實作')
 raise ValueError(k)
def graphic(k):
 if not k.startswith('b3-'):raise ValueError(k)
 return scene(k[3:])

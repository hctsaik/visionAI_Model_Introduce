"""Fresh analytic SVG illustrations, never pixel edits of existing assets."""
from render import rect,text,line,arrow,circle,group,feature,pill,B,N,G,O,L,PALE

def lines(*ss,y=315):return ''.join(text(15,y+48*i,s,27) for i,s in enumerate(ss))
def marker(x,y,s=1,dx=0,glare=False):
 a=rect(0,0,190,175,'#D6E0E9','#8399AD',10)
 for xx,yy in [(13,13),(177,13),(13,162),(177,162)]:a+=circle(xx,yy,4,'#8295A6',PALE)
 a+='<path d="M55,35 v75 h75" fill="none" stroke="#243548" stroke-width="20"/>'
 if glare:a+=rect(45,75,100,70,'white','none',16)
 return group(x+dx*s,y+dx*.5*s,s,a)
def pair(glare=False):return marker(8,55,1)+marker(285,55,1,dx=20,glare=glare)+text(15,30,'前影格',29)+text(292,30,'後影格',29)+arrow(210,138,265,138)
def board(x,y,s=1,rot=False,scratch=False):
 a=rect(0,0,210,230,'#CAD8E4','#71899F',13)+text(38,37,'A-01',28,N,700)+line(22,24,22,52,N,4)+line(13,33,31,33,N,4)
 for xx,yy in [(63,85),(149,85),(63,172),(149,172)]:a+=circle(xx,yy,23,'#7F98AC',PALE)
 if scratch:a+=line(107,187,125,211,'#B54F46',7)
 if rot:a=f'<g transform="rotate(180 105 115)">{a}</g>'
 return group(x,y,s,a)
def tray(x,y,s=1,missing=False,spot=False,glare=False):
 a=rect(0,30,350,150,'#A3B7C7','#71869A',12)
 for i in range(3):
  xx=12+i*114;a+=rect(xx,50,98,110,'#607A90','#71869A',5)
  if not(missing and i==1):
   a+=rect(xx+10,30,78,110,'#D2DFE8','#6F8598',7)+f'<ellipse cx="{xx+49}" cy="30" rx="39" ry="16" fill="#E5EDF4" stroke="#6F8598" stroke-width="3"/>'
   if i==2 and spot:a+='<path d="M282,78 l15,-7 9,13 -6,20 -22,5 -4,-13 Z" fill="#6A514D"/>'
   if i==2 and glare:a+=rect(270,63,45,61,'white','none',11)
 return group(x,y,s,a)
def grid(x,y,values,size=35):
 return ''.join(rect(x+(i%3)*size,y+(i//3)*size,size-2,size-2,'#F7DFC0' if v>.3 else '#D5E6F6',L,0)+text(x+(i%3)*size+size/2,y+(i//3)*size+size*.67,str(v),size*.42,N,500,'middle') for i,v in enumerate(values))
def flowfield(x,y,dense=False):
 a=marker(0,0,1.5)
 for xx,yy in ([(90,53),(90,168),(200,168)] if not dense else [(x,y) for x in range(35,265,42) for y in range(32,255,43)]):a+=arrow(xx,yy,xx+21,yy+9,B,3)
 return group(x,y,1,a)
def graphic(k):
 if k=='flow-pair':return pair()+lines('同一 L 形刻痕，工件平移','固定時間差、裁切與取像')
 if k=='lk-texture':
  a=marker(145,0,1.1)+rect(196,105,70,65,'none',B,0)+arrow(218,148,278,148,O)+arrow(218,148,218,81,G)
  return a+lines('角點：兩方向都有亮度變化','單一平邊只能限制一方向','平坦區幾乎沒有位移線索',y=264)
 if k=='lk-pyramid':
  a=marker(22,10,.42)+arrow(115,49,155,49)+marker(172,10,.68)+arrow(306,85,337,85)+marker(350,10,.72)
  return a+text(25,198,'粗尺度',29)+text(187,198,'傳遞估計',29)+text(353,198,'細修',29)+lines('先縮小影像，抓粗位移','逐層放大估計，再局部修正','反光蓋住的內容不會回來',y=263)
 if k=='lk-gradients':
  a=marker(8,18,.72)+rect(153,22,334,212,'white',L,9)
  for j,st in enumerate(['Ix','Iy','It']):a+=text(213+95*j,62,st,31,B,700,'middle')
  for i,values in enumerate([[1,0,'−2'],[0,1,'−1'],[1,1,'−3']]):
   for j,value in enumerate(values):a+=text(213+95*j,111+50*i,value,31,N,500,'middle')
  return a+lines('小窗內三個像素的給定梯度','Ix / Iy：空間亮度變化','It：跨影格亮度變化',y=285)
 if k=='lk-equations':return pill(20,15,460,'同一小窗，共同未知 u / v')+text(35,120,'Ix · u + Iy · v + It ≈ 0',32,B,700)+text(45,199,'u = 2',38)+text(45,256,'v = 1',38)+text(45,313,'u + v = 3',38)+text(20,398,'多條限制一起解；真實資料有誤差',27)
 if k=='lk-solution':
  a=line(65,80,65,245,L,2)+line(65,245,415,245,L,2)+arrow(90,90,330,210,B,7)+line(90,90,330,90,G,3)+line(330,90,330,210,O,3)+text(165,75,'u = 2',31,G)+text(344,150,'v = 1',31,O)
  return a+lines('影像座標：右為正，下為正','像素／影格間隔；非毫米速度','另查可解性、殘差與往返',y=290)
 if k=='flow-points':return pair()+circle(63,165,7,O)+text(73,163,'p',30,O)+circle(360,175,7,O)+text(370,173,'p′',30,O)+text(15,282,'p → p′',38,B)+lines('前後座標與時間一併保存','每個點有自己的有效性',y=345)
 if k=='lk-reject':return marker(10,15,1)+marker(286,15,1,20,True)+text(23,257,'清楚點對',30,G)+text(285,257,'對應不可見',30,O)+lines('殘差／往返不符：退出追蹤','重新找點，不延續錯誤箭頭',y=328)
 if k=='flow-measure':return arrow(35,60,180,115)+text(221,95,'像素位移',33,B)+arrow(240,140,240,196)+pill(45,215,405,'相機／尺度／平面條件')+arrow(240,263,240,305)+text(45,356,'物理位移 ÷ 真實時間差',33)+text(45,407,'移動相機、深度變化另處理',26,O)
 if k=='flow-work':return pair()+lines('同影格對、同時間與解析度','先定需要哪些位置的位移')
 if k=='flow-sparse':return flowfield(93,5)+lines('被選中的角點，逐點核對','輸出少，不等於錯誤必定少')
 if k=='flow-dense':return flowfield(93,5,True)+lines('每個位置給向量，不是追蹤ID','箭頭示意，不代表模型實測')
 if k=='raft-correlation':
  a=feature(15,30,[1,.5,.8])
  for i,vals in enumerate([[.9,.5,.9],[.2,.7,.5],[.8,.1,.4]]):a+=feature(360,i*65,vals,G)+line(100,55,346,22+i*65,G,2)
  a+=grid(175,196,[.2,.8,.3,.4,.1,.7,.3,.5,.1],37)
  return a+text(10,143,'圖1局部',27)+text(355,214,'圖2各處',27)+lines('全位置配對 → 相關性體','多尺度池化；不等於光流',y=358)
 if k=='raft-context':return marker(10,10,.65)+arrow(152,72,215,72)+pill(225,45,240,'Context encoder')+arrow(345,100,345,167)+pill(225,184,235,'情境 / 隱狀態',G)+lines('由第一張影格提供','與相關性一起進更新單元','不是第二張圖的缺陷標籤',y=282)
 if k=='raft-lookup':
  a=grid(55,10,[.1,.2,.1,.2,.8,.5,.1,.3,.2],80)+rect(129,82,95,95,'none',O,0)+text(326,142,'查詢區',29,O)
  return a+lines('位置 = 原座標 + 目前光流','在各尺度查周圍相關線索','每次更新後，查詢位置會變',y=287)
 if k=='raft-update':
  a=''
  for i,name in enumerate(['相關線索','目前光流','影像情境','隱狀態']):
   yy=10+i*80;col=B if i<2 else G;a+=pill(10,yy,190,name,col)+arrow(207,yy+21,304,157,col,3)
  return a+pill(310,135,175,'更新單元')+arrow(398,184,398,291)+text(22,372,'位移增量 + 新隱狀態',32,B)+text(22,414,'只用模型已有的輸入資訊',26)
 if k=='raft-refine':return text(25,48,'舊光流 + 增量 = 新光流',33,B,700)+text(35,108,'(1, 0) + (1, 1) = (2, 1)',33)+arrow(65,171,165,171)+arrow(165,171,265,271,G)+arrow(65,171,265,271,O)+text(300,245,'新向量',28,O)+lines('新座標再查詢，最後上採樣','算術示意；非實測收斂曲線',y=350)
 if k=='raft-reject':return marker(145,8,1.2,20,True)+text(205,155,'?',60,O,700)+lines('看不見對應，仍可能有數值','往返檢查是應用驗證工具','原始RAFT不原生保證置信度',y=285)
 if k=='raft-cost':return ''.join(text(18,45+82*i,s,29)+rect(185,20+82*i,w,32,B if i%2==0 else G,'none',2) for i,(s,w) in enumerate([('特徵',160),('相關性',265),('更新×次數',210),('上採樣',110)]))+text(18,407,'示意成本項：另量時間與記憶體',26)
 if k in ['raft-fewer','raft-more']:
  n=3 if k.endswith('fewer') else 6;a=''
  for i in range(n):a+=rect(20+i*77,40,65,80,'#C4DCF4',B,5)+text(52+i*77,91,i+1,28,B,700,'middle')
  return a+text(20,183,'更新次數：示意較少' if n==3 else '更新次數：示意較多',32)+lines('同資料量位移錯誤與覆蓋','量完整時間與記憶體','更多更新不保證一定改善',y=265)
 if k=='flow-common-cases':
  a=text(15,25,'清楚組',28,G)+group(25,35,.7,pair())+text(15,235,'反光組：只遮住後影格',28,O)+group(25,244,.7,pair(True))
  return a
 if k in ['flow-common-lk','flow-common-raft']:
  name='點對' if k.endswith('lk') else '位移場'
  a=pill(15,20,200,'清楚組',G)+arrow(225,43,285,43)+text(305,55,name,33)+pill(15,152,200,'反光組',O)+arrow(225,175,285,175)+text(305,187,name,33)
  return a+lines('兩組都跑，不只挑有利條件','核對原圖、錯誤與可用覆蓋','未實測；不替任一方法判勝',y=284)
 if k=='adino-support':return board(20,12,.8)+board(276,12,.8)+lines('允收正常外觀先確認','參考與獨立測試分開')
 if k=='adino-encode':return board(5,10,.55)+arrow(133,90,192,90)+pill(201,65,274,'固定 DINOv2')+arrow(337,116,337,177)+feature(307,195,[.6,1,.3])+lines('整张圖送入，局部token交出','放大框不是逐塊重新編碼','本產品不需再微調骨幹',y=290)
 if k=='adino-memory':
  a=rect(25,15,445,228,'white',L,12)
  for i in range(3):a+=feature(50,45+62*i,[.3+.2*i,.8,.4])+text(175,72+62*i,f'N-{i+1} / 位置 {i+1}',30)
  return a+lines('特徵與來源影像ID一起存','模型、前處理、參考版本相容','不是一套新缺陷類別權重',y=294)
 if k=='adino-query':return board(18,8,.85,False,True)+rect(99,159,34,41,'none',O,0)+arrow(220,123,282,123)+feature(305,100,[1,0])+lines('待測整圖 → 固定DINOv2','追同一右下刮痕位置','特徵比較，非照片直接相減',y=284)
 if k=='adino-distance':
  a=feature(16,40,[1,0])+text(10,135,'待測',30)
  for i,(v,c) in enumerate([('0.40',G),('0.62',B),('0.55',B)]):
   cosine=1-float(v);a+=arrow(110,80,232,53+95*i,c,3)+feature(242,25+95*i,[cosine,(1-cosine*cosine)**.5],c)+text(363,60+95*i,v,36,c,700)
  return a+lines('最小：0.40，不等於正常','給定特徵距離；非插圖實測',y=347)
 if k=='adino-location':return board(145,5,1.0,False,True)+rect(241,184,37,40,'#F6C787',O,0)+lines('每個patch距離回到其位置','上採樣／平滑後仍非精密邊界','整件：最高1%距離另聚合',y=289)
 if k in ['adino-clean','adino-contamination']:
  vals=['0.40','0.55']+(['0.03'] if k.endswith('contamination') else []);a=board(10,10,.7,False,True)
  for i,v in enumerate(vals):a+=text(220,62+73*i,'候選 '+v,33,O if v=='0.03' else B)
  return a+lines('同一待測刮痕、同模型','最近 '+min(vals)+'；圖中距離為給定','原候選不變，只增加參考',y=281)
 if k=='adino-revalidate':return board(30,10,.75)+board(290,10,.75,False,True)+lines('同正常 + 真缺陷留出集','核對誤報、漏檢及覆核量','另量建庫、查詢與記憶體',y=281)
 if k=='adino-upright':return board(143,2,1.1)+lines('同一A-01，刻字與孔位固定','此例正常規格需另行指定')
 if k in ['adino-rotated','adino-rotate-free','adino-rotate-required']:
  a=board(143,2,1.1,True)
  return a+lines(*({'adino-rotated':['同一群組整體旋轉180度','刻字與所有孔洞一起旋轉'],'adino-rotate-free':['規格允許自由方向','可測旋轉參考，另驗誤報'],'adino-rotate-required':['規格要求標誌朝上','不可因建庫就把倒置當正常']}[k]))
 if k=='adino-rotation-rule':return pill(22,25,440,'規格允許自由擺放',G)+text(33,120,'驗旋轉參考是否有幫助',31)+pill(22,207,440,'規格要求標誌朝上',O)+text(33,300,'方向另驗，倒置不能放寬',31)+text(33,399,'兩種規格不能共用同一接受條件',25)
 if k=='eff-teacher':return tray(55,10,1.1)+arrow(230,210,230,252)+pill(40,276,420,'預訓練教師 T：固定')+text(28,390,'正常托盤先確認，異常另留驗證',28)
 if k=='eff-student1':return pill(10,22,200,'固定 T')+pill(281,22,200,'學生 S1',G)+feature(45,113,[.5,1,.7])+feature(315,113,[.3,.8,.5],G)+arrow(251,141,160,141,G)+lines('正常影像讓表示接近','學生兩組輸出共享前層','訓練有難例損失與外域抑制',y=276)
 if k=='eff-train-global':return pill(130,10,235,'教師 T 固定')+arrow(241,58,241,117)+text(260,96,'目標',25)+pill(130,133,235,'AE 學重建',G)+arrow(241,181,241,237)+text(260,219,'目標',25)+pill(130,252,235,'S2 學 AE',G)+text(20,346,'同一影像分別送T、AE與學生',27)+text(20,394,'箭頭提供學習目標，非串接輸入',26)
 if k=='eff-test':return tray(55,5,1.1,True,True)+lines('中間缺件、右側污點','同一影像送T、學生與AE','位置與表示皆為教學示意',y=280)
 if k=='eff-two-diffs':
  a=pill(8,10,165,'T')+pill(317,10,165,'S1',G)+text(220,44,'−',37)+arrow(242,60,242,101)+pill(116,114,255,'local：均方差')
  a+=pill(8,223,165,'AE')+pill(317,223,165,'S2',G)+text(220,257,'−',37)+arrow(242,270,242,311)+pill(116,324,255,'global：均方差',G)
  return a+text(22,405,'每個位置：通道平方差再平均',27)
 if k=='eff-calibrate':
  a=pill(10,10,200,'local')+pill(280,10,200,'global',G)+arrow(110,64,110,108)+arrow(380,64,380,108,G)+pill(10,125,200,'線性校正')+pill(280,125,200,'線性校正',G)+arrow(110,177,243,227)+arrow(380,177,243,227,G)+pill(110,247,265,'兩圖平均')
  return a+text(20,361,'正常驗證分位數 → 各自校正',29)+text(20,410,'融合圖最大值：整件分數',28)
 if k=='eff-ablation':
  a=''
  local=[.6 if i==5 else .1 for i in range(9)];glob=[.6 if i==4 else .1 for i in range(9)];fused=[round((x+y)/2,2) for x,y in zip(local,glob)]
  for x,name,vals in [(5,'local',local),(172,'global',glob),(339,'平均',fused)]:a+=text(x+5,38,name,30)+grid(x+3,65,vals,45)
  return a+lines('已對齊尺度的給定算例','分支分開保存，定位同原圖','融合是否改善，另驗真缺陷',y=283)
 if k=='eff-review':return tray(55,5,1.1,True,True)+rect(189,65,96,140,'none',O,4)+rect(352,86,50,70,'none',O,4)+lines('缺件、污點分開記錄漏檢','允收正常变化另記誤報','回原圖，不把亮區當尺寸',y=279)
 if k=='eff-cost':return ''.join(text(18,46+87*i,s,29)+rect(180,20+87*i,w,35,B if i%2==0 else G,'none',3) for i,(s,w) in enumerate([('取像/傳輸',120),('前處理',100),('T/S/AE',260),('映回/交付',150)]))+text(18,413,'僅列成本構成；不是實測時間比例',25)
 if k=='eff-new-product':return tray(55,4,1.1)+lines('同為正常，也有新的材質與外觀','先確認代表性正常訓練資料','模型名稱不會替你適配產品',y=280)
 if k=='eff-maintenance':return pill(15,15,455,'新正常訓練資料')+arrow(243,67,243,106)+pill(15,123,455,'學生 / AE 按需要重訓',G)+arrow(243,174,243,217)+pill(15,234,455,'新正常驗證分布校正',O)+lines('權重、分位數與資料一起保存','保留舊版供回放比較',y=351)
 if k=='eff-update-check':return tray(25,10,.6)+tray(257,10,.6,True,True)+lines('新舊版本跑相同留出集','量誤報、漏檢、訓練與校正成本','每件耗時與更新工時分開',y=246)
 if k=='eff-glare':return tray(55,5,1.1,True,True,True)+lines('仍是同件、同位置的污點','反光遮住線索；缺件仍可見','兩路都不能保證補回資訊',y=280)
 from batch2_deep_graphics import graphic as deep
 return deep(k)

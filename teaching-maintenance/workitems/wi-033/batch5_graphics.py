"""Concrete, original SVG anomaly-detection teaching scenes; no model inference."""
from render import rect,text,line,arrow,circle,group,pill,B,N,G,O,L,PALE
from batch3_graphics import grid,matrix,caption
R='#C6473D'
def board(x=25,y=25,s=1,holes=2,defect=False,mark=False):
 a=rect(0,0,350,225,'url(#steel)','#748A9C',8)
 if holes:
  a+=circle(68,65,35,'#748A9C','white')
  if holes==2:a+=circle(282,181,22,'#748A9C','white')
 for xx,yy in [(13,13),(337,13),(13,212),(337,212)]:a+=circle(xx,yy,3,'#748A9C')
 if defect:a+=line(266,133,300,103,'#34424B',6)+line(260,142,286,122,'#EDF2F6',3)
 if mark:a+=rect(247,94,65,58,'none',O,0)+text(318,124,'p',31,O,700)
 return group(x,y,s,a)
def mapboard(value='2.24',holes=2):
 a=board(35,15,1.1,holes,True)
 a+=rect(35+247*1.1,15+94*1.1,65*1.1,58*1.1,'#FFB366',O,0)
 a+=text(25,310,'p：'+value+' → 回原圖查證',29,O,700)
 return a
def vecbox(x,y,label,value,col=B):return rect(x,y,220,72,'white',col,6)+text(x+12,y+30,label,25,col,700)+text(x+12,y+60,value,27,col)
def graphic(k):
 k=k.removeprefix('b5-')
 if k=='pc-coreset':
  a=board(10,12,.44,0)+board(195,12,.44,0)+arrow(180,116,180,155)+pill(45,162,350,'固定CNN抽局部特徵')
  for i,(xx,yy) in enumerate([(70,239),(100,248),(83,270),(270,247),(290,270),(311,253)]):a+=circle(xx,yy,7,B)
  a+=circle(83,270,17,O,'none')+circle(290,270,17,O,'none')+text(345,257,'挑代表',25,O)
  return a+caption('正常庫存局部特徵代表','coreset不是每張影像取一張')
 if k=='pc-distance':
  a=text(20,45,'待測p = [3, 2]',34,O,700)
  a+=vecbox(20,80,'r1 = [0, 0]','√13 ≈ 3.61')+vecbox(260,80,'r2 = [2, 0]','√5 ≈ 2.24',G)
  a+=arrow(244,185,244,222)+rect(40,233,410,65,'#EDF8F0',G,8)+text(58,276,'最近是r2：局部距離2.24',29,G,700)
  return a+caption('在同一特徵空間找最近鄰','二維算例，非像素相減')
 if k=='pc-map':
  a=matrix([[.1,.2,.1],[.1,.2,2.24]],15,25,75)+arrow(246,100,275,100)+board(282,30,.55,0,True,True)
  a+=text(15,232,'保留局部p的網格位置',30,B,700)+text(15,284,'上採樣回原圖：僅定位線索',27)
  return a+caption('逐局部距離形成可疑圖','整圖分數另有重加權')
 if k=='padim-fit':
  a=board(15,15,.57,1,False,True)+board(270,15,.57,1,False,False)
  a+=circle(270+68*.57,15+65*.57,26,G,'none')+text(350,59,'q',28,G,700)
  a+=arrow(125,155,125,193)+arrow(378,155,378,193,G)
  a+=vecbox(10,208,'平面p分布','μp / Σp')+vecbox(265,208,'孔口q分布','μq / Σq',G)
  return a+caption('跨正常影像收集同位置特徵','p和q不可共用一個位置分布')
 if k=='padim-direction':
  a='<ellipse cx="230" cy="135" rx="140" ry="35" transform="rotate(-30 230 135)" fill="#E5EFFB" stroke="'+B+'" stroke-width="3"/>'
  a+=arrow(230,135,351,65,B)+arrow(230,135,172,35,O)+circle(230,135,5,N)+text(367,64,'u',28,B)+text(139,32,'v',28,O)
  a+=text(20,245,'u變異4：偏移2 → 距離1',28,B,700)+text(20,296,'v變異.25：偏移2 → 距離4',28,O,700)
  return a+caption('主軸方向不同，距離不同','特徵空間示意，非影像座標')
 if k=='padim-map':return mapboard('馬氏距離',1)+caption('每個位置查自己的正常範圍','工件偏移也可能改變距離')
 if k=='sub-fit':
  a=board(15,15,.48,2)+arrow(196,68,240,68)+pill(250,45,225,'固定DINOv2')
  a+=arrow(350,96,350,143)+text(20,185,'正常特徵中心化：μ = 0',29,B)
  a+=line(35,267,460,267,B,5)
  for xx,yy in [(85,257),(145,271),(225,260),(288,274),(345,260),(400,271)]:a+=circle(xx,yy,6,B)
  a+=text(40,319,'本例PCA保留U = [1, 0]',29,G,700)
  return a+caption('保留正常變動的主要方向','均值為0是本算例的設定')
 if k=='sub-project':
  a=line(45,280,450,280,B,4)+line(45,280,45,30,L,2)+arrow(45,280,300,100,O)+line(300,100,300,280,R,5,True)
  a+=circle(300,100,7,O)+circle(300,280,7,G)+text(280,65,'x = [3, 2]',29,O,700)+text(210,322,'投影 [3, 0]',29,G,700)
  a+=line(282,280,282,262,G,2)+line(282,262,300,262,G,2)+text(326,194,'殘差2',28,R)
  return a+caption('垂直落回保留的正常方向','特徵投影，不是工件幾何投影')
 if k=='sub-residual':
  a=text(20,42,'[3, 2] − [3, 0] = [0, 2]',31,B,700)+text(20,100,'殘差長度 = 2',32,O,700)
  a+=arrow(240,122,240,153)+board(110,165,.68,2,True,True)
  return a+caption('局部p的殘差排回p的位置','保留全維時可能連異常也解釋')
 if k=='stf-branches':
  a=board(10,95,.43,2,True,True)+arrow(170,144,230,60)+arrow(170,144,230,225,G)
  a+=pill(240,35,235,'教師：固定')+pill(240,206,235,'學生：正常訓練',G)
  a+=grid(4,245,94,80,col=B)+grid(2,352,104,65,col=B)+grid(4,245,263,55,col=G)+grid(2,340,263,55,col=G)
  return a+caption('同一影像、相同架構分兩路','訓練只更新學生；推論都固定')
 if k=='stf-distance':
  a=vecbox(10,25,'教師單位向量','T = [1, 0]')+vecbox(263,25,'學生單位向量','S = [.8, .6]',G)
  a+=text(20,155,'同層、同位置p',31,N,700)+text(20,215,'差 = [.2, −.6]',31,O)
  a+=text(20,282,'½ × (.2² + .6²) = .2',34,B,700)
  return a+caption('先正規化，再算半平方距離','二維數值只是機制算例')
 if k=='stf-merge':
  a=''
  for i,(n,v) in enumerate([(4,'.2'),(4,'.4'),(4,'.5')]):a+=grid(n,15+i*160,15,112,mark=(2,3))+text(28+i*160,166,'p：'+v,28,O)
  a+=text(20,225,'已上採樣到相同位置網格',29,B,700)+arrow(240,242,240,268)+text(40,313,'.2 × .4 × .5 = .04',32,G,700)
  return a+caption('各層差圖對齊後逐點相乘','本例不是缺陷機率')
 if k in ['rd-bottleneck','rd-train-bottleneck']:
  a=board(15,10,.42,2,k=='rd-bottleneck',k=='rd-bottleneck')+arrow(173,55,215,55)+pill(227,32,245,'固定教師')
  a+=grid(4,15,130,100)+grid(3,165,140,82)+grid(2,295,149,67)+arrow(210,238,210,264)+pill(70,275,360,'可訓練單類瓶頸',G)
  return a+caption('多尺度教師表示壓成嵌入','正常資料訓練瓶頸及學生')
 if k=='rd-decode':
  a=pill(25,22,430,'輸入：教師的瓶頸嵌入',G)+arrow(239,80,239,122)
  a+=grid(2,15,201,62,col=G)+arrow(87,232,132,232,G)+grid(3,143,176,102,col=G)+arrow(258,232,304,232,G)+grid(4,316,146,151,col=G)
  a+=text(15,320,'粗 → 中 → 細：重建特徵',30,G,700)
  return a+caption('反向解碼，不直接讀原圖','輸出是表示，不是修復照片')
 if k=='rd-compare':
  a=text(45,30,'教師',28,B,700)+text(289,30,'重建',28,G,700)
  for i,n in enumerate([4,3,2]):a+=grid(n,45,55+i*88,70,mark=(1,1),col=B)+arrow(134,90+i*88,267,90+i*88)+grid(n,288,55+i*88,70,col=G)+text(386,100+i*88,'差異',25,O)
  return a+caption('同尺度、同位置的餘弦差','各層對齐整合後回原圖')
 if k=='ae-input':
  a=board(12,15,.66,2,True,True)+text(222,167,'q',27,G,700)+arrow(250,96,283,96)+rect(302,51,135,135,'#282828',O,2)+text(368,140,'40',42,'white',700,'middle')
  a+=text(20,277,'原圖p：灰階40',32,O,700)
  return a+caption('先固定同一張待測板A','p是刮傷處，q是正常小孔')
 if k=='ae-reconstruct':
  a=pill(15,15,160,'編碼')+arrow(186,36,216,36)+rect(230,19,44,36,G,G,3)+arrow(287,36,318,36)+pill(330,15,160,'解碼')
  a+=board(15,90,.65,2,False,True)+rect(305,105,135,135,'#969696',G,2)+text(372,189,'150',40,'white',700,'middle')
  a+=text(20,308,'重建p：灰階150',32,G,700)
  return a+caption('正常資料學壓縮與還原','重建估計並非正常真值')
 if k=='ae-difference':
  a=rect(25,25,130,100,'#282828',O,2)+text(90,91,'40',40,'white',700,'middle')+text(190,89,'−',38)+rect(250,25,130,100,'#969696',G,2)+text(315,91,'150',40,'white',700,'middle')
  a+=text(25,185,'|40 − 150| = 110',39,O,700)+arrow(240,205,240,240)+text(25,290,'同位置p → 差異圖',32,B,700)
  return a+caption('同座標相減，才能追差值','差異小仍可能是缺陷被複製')
 if k=='draem-train':
  a=board(12,15,.48,2)+board(268,15,.48,2,True,True)+text(12,159,'正常目標',27,B)+text(268,159,'合成異常',27,O)
  a+=arrow(98,175,98,210)+arrow(350,175,350,210,O)+vecbox(10,223,'重建監督','正常原圖')+vecbox(264,223,'定位監督','合成mask',O)
  a+=rect(408,228,66,57,'#26394A','none',1)+rect(454,252,12,12,'white','none',0)
  return a+caption('原圖教重建，mask教定位','兩種監督來源要分清楚')
 if k=='draem-pair':
  a=board(10,15,.52,2,True,True)+board(280,15,.52,2,False,True)+text(10,170,'待測原圖',28,O)+text(280,170,'重建估計',28,G)
  a+=arrow(100,190,200,247,O)+arrow(368,190,288,247,G)+pill(82,262,355,'兩張共同送入判別器')
  return a+caption('原圖與重建一起作證據','推論不提供缺陷真值mask')
 if k=='draem-seg':
  a=pill(35,20,420,'學習式判別分割網路')+arrow(240,79,240,120)+grid(4,20,150,153,mark=(2,3))+arrow(187,223,239,223)+board(250,142,.64,2,True,True)
  return a+caption('學出位置圖，再對照原圖p','不是把兩張影像直接相減')
 if k=='uni-input':
  a=board(10,15,.6,2,True,True)+arrow(241,92,286,92)+grid(5,307,24,155,mark=(2,3))
  a+=text(15,255,'整張原圖 → 固定骨幹',31,B,700)+text(15,304,'原始特徵保留作比較目標',27)
  return a+caption('輸入影像沒有被塗掉','多類正常共訓重建部分')
 if k=='uni-mask':
  a='';size=43
  for i in range(5):
   for j in range(5):
    blocked=1<=i<=3 and 1<=j<=3
    a+=rect(20+j*size,15+i*size,size-2,size-2,'#C5CCD3' if blocked else '#DCEAFF',N if (i,j)==(2,2) else L,1)
  a+=text(20+2*size+12,15+2*size+30,'p',29,O,700)+text(260,65,'灰：不取用',28,N)+text(260,123,'藍：可讀取',28,B)
  a+=text(20,284,'p遮自己 + 近鄰的連線',29,O,700)
  return a+caption('以p為中心的局部取用示意','5×5格不是固定輸入尺寸')
 if k=='uni-rebuild':
  a=pill(20,15,440,'逐層query引導重建')+arrow(240,78,240,112)
  a+=grid(4,20,138,135,mark=(2,3))+text(26,313,'原特徵',27,B)+arrow(171,205,287,205)+grid(4,310,138,135)+text(318,313,'重建特徵',27,G)
  return a+caption('同位置比較，再排回可疑圖','特徵擾動只用在訓練')
 from batch5_expanded_graphics import graphic as expanded
 return expanded(k)

"""Same-piece SVG mechanism scenes for batch 6; all numeric examples authored."""
from render import rect,text,line,arrow,circle,group,pill,B,N,G,O,L,PALE
from batch3_graphics import grid,matrix,caption
from batch5_graphics import board,vecbox
R='#C6473D'
def belt(x=10,y=30,s=1,pos=130,label='',flash=False,mask=False):
 a=rect(0,0,440,165,'#606972' if not mask else '#15222F','#73899E',4)+line(0,8,440,8,'#ACB6BF',8)+line(0,157,440,157,'#ACB6BF',8)
 if pos is not None:
  a+=rect(pos,40,85,85,'white' if mask else 'url(#steel)','#DAE1E7',1)
  if label:a+=text(pos+20,104,label,47,N,700)
 if flash:a+=rect(0,0,440,165,'#FFFFFF77','none',0)
 return group(x,y,s,a)
def cells(vals,y,col=B):
 return ''.join(rect(25+i*85,y,80,54,'#E3EEF9',col,1)+text(65+i*85,y+36,v,27,col,700,'middle') for i,v in enumerate(vals))
def graphic(k):
 k=k.removeprefix('b6-')
 if k=='dino-drop':
  a=board(15,15,.4)+arrow(166,62,210,62)+pill(225,40,245,'固定DINOv2')+text(20,153,'訓練：隨機丟棄部分表示',29,B,700)
  for i in range(6):a+=rect(25+65*i,179,55,53,L if i in [1,4] else B,'white',1)
  a+=text(20,287,'eval：關閉Dropout',31,G,700)
  return a+caption('正常資料只教重建路徑','灰格只示意丟棄，不是影像擦除')
 if k=='dino-linear':
  a=grid(4,30,30,220)
  for xx,yy in [(43,43),(231,43),(43,230),(231,230)]:a+=arrow(xx,yy,140,140,B,3)
  a+=circle(140,140,19,O)+text(278,98,'分散聚合',29,B,700)+text(277,153,'多個位置',27)+pill(65,275,360,'線性注意力解碼')
  return a+caption('降低專注同位置照抄的捷徑','不是固定平均，也不保证檢出')
 if k=='dino-groups':
  a=text(15,28,'原始層',28,B,700)+text(280,28,'重建層',28,G,700)
  for y in [55,190]:
   a+=grid(2,20,y,55)+grid(2,90,y,55)+text(78,y+35,'+',20)+arrow(155,y+27,210,y+27)+grid(2,280,y,55,col=G)+grid(2,350,y,55,col=G)
   a+=text(338,y+35,'+',20)+text(20,y+90,'兩側各相加 → 比對同組',26)
  return a+caption('淺／深可分組，各組內相加','放寬逐層對應；非逐層硬配對')
 if k=='inv-condition':
  a=board(15,15,.45,2,True,True)+arrow(182,65,228,65)+grid(4,245,20,115,mark=(2,3))+arrow(300,144,300,171)+pill(20,180,440,'融合 → 重縮放 → 風格轉換')
  a+=grid(2,65,247,65)+arrow(143,277,225,277)+grid(4,245,240,85)
  return a+caption('同輸入產生各尺度空間條件','條件保留位置，不是全圖一數')
 if k=='inv-modulate':
  a=text(20,38,'給定標準化後 z = 3',31,B,700)+vecbox(15,73,'p：縮放2／偏移1','2 × 3 + 1 = 7',O)+vecbox(250,73,'q：縮放.5／偏移0','.5 × 3 + 0 = 1.5',G)
  a+=grid(3,35,180,100,mark=(1,2))+arrow(155,227,265,227)+grid(3,285,180,100,col=G)+text(37,316,'常數起步 → 逐階調制',28,B,700)
  return a+caption('SSM：空間風格調制','此例只追一個已標準化分量')
 if k=='inv-compare':
  a=text(25,35,'原特徵',29,B,700)+text(285,35,'重建特徵',29,G,700)+grid(4,25,65,150,mark=(2,3))+grid(4,285,65,150,col=G)+arrow(188,145,265,145)
  a+=text(45,269,'同位置餘弦差 → 回原圖p',29,O,700)
  return a+caption('正常訓練MSE；推論比餘弦差','重建的是特徵，不是修復照片')
 if k=='dd-guide':
  a=board(145,15,.55,2,True,True)+text(20,163,'原圖A保持不變，每步給條件',28,B,700)
  a+=line(239,176,239,201)+line(65,201,410,201)
  for x in [65,239,410]:a+=arrow(x,201,x,234)+rect(x-48,245,96,64,L,B,5)+text(x,285,'去噪',24,B,700,'middle')
  return a+caption('條件始終來自同一張A','不是每步拿上一張當新的真值')
 if k=='dd-steps':
  a=''
  for i,n in enumerate([25,10,0]):
   x=5+i*163;a+=board(x,50,.4,2,i==0)
   for j in range(n):a+=circle(x+8+(j*23)%128,55+(j*19)%79,2,'#34424B')
   a+=text(x+65,170,['加噪','中間','恢復R'][i],27,B,700,'middle')
   if i<2:a+=arrow(x+144,100,x+160,100)
  a+=text(25,252,'步數／引導強度影響R',30,O,700)
  return a+caption('示意三個狀態，非固定三步','R是恢復估計，不是正常真值')
 if k=='dd-compare':
  a=board(5,5,.45,2,True,True)+board(280,5,.45)+text(50,140,'原A',27,O,700)+text(326,140,'恢復R',27,G,700)
  a+=vecbox(15,175,'像素：同座標比','| A(p) − R(p) |',O)+vecbox(250,175,'適配後特徵比','共用提取器',G)+arrow(130,257,220,287)+arrow(370,257,260,287)+text(147,316,'加權整合',29,B,700)
  return a+caption('兩路差異都来自同一對A／R','各路尺度與權重需固定驗證')
 if k=='win-prompts':
  a=vecbox(15,20,'正常狀態詞','完整／無損',G)+vecbox(250,20,'異常狀態詞','受損／刮傷',O)+text(25,146,'搭配多個描述句型',30,B,700)+arrow(126,165,126,200)+arrow(360,165,360,200)+pill(35,210,400,'固定CLIP文字編碼')
  a+=text(30,303,'正常向量N       異常向量A',29)
  return a+caption('人工組合提示，再整合文字表示','非用目標資料更新骨幹')
 if k=='win-windows':
  a=board(25,15,1.1,2,True,True)+rect(260,93,115,115,'none',B,0)+rect(230,63,115,115,'none',G,0)+text(380,213,'W1',26,B,700)+text(250,53,'W2',26,G,700)
  a+=text(25,309,'每窗整體表示 → 比N／A',30,B,700)
  return a+caption('示意兩個同尺度重疊窗覆蓋p','窗內保留局部，非普通切圖resize')
 if k=='win-harmonic':
  a=vecbox(15,20,'覆盖p的窗W1','給定分數 0.2',B)+vecbox(250,20,'覆盖p的窗W2','給定分數 0.8',G)+arrow(120,107,205,151)+arrow(360,107,280,151)+text(30,198,'2 / (1/.2 + 1/.8) = .32',30,O,700)+grid(4,185,235,84,mark=(2,3))
  return a+caption('共同位置取調和平均0.32','多尺度再融合；分數非缺陷機率')
 if k=='ac-train':
  a=rect(25,25,140,85,'#4385B8',B,5)+text(28,143,'輔助連接器',26,B,700)+rect(285,25,145,85,'#ECF0EB','#AFBABB',3)+line(315,40,356,62,R,4)+line(356,62,345,95,R,4)+text(290,143,'輔助陶瓷板',26,B,700)
  a+=text(45,200,'正常／異常＋位置標註',30)+arrow(235,220,235,250)+pill(20,265,440,'學物件無關的兩組提示')
  return a+caption('整圖與局部監督共同教提示','目標金屬板不參與這次訓練')
 if k=='ac-match':
  a=board(15,15,.43,2,True,True)+arrow(174,65,220,65)+grid(4,240,15,115,mark=(2,3))+text(20,167,'CLIP固定權重＋DPAM',28,B,700)
  a+=vecbox(15,210,'局部p影像表示','比兩狀態相似',B)+vecbox(250,210,'學到的提示','正常N／異常A',G)
  return a+caption('DPAM調注意力，保留局部語意','不是把目標缺陷文字拿來訓練')
 if k=='ac-local':
  a=text(20,40,'局部定位',30,B,700)+grid(4,30,65,150,mark=(2,3))+text(260,40,'整圖分數',30,G,700)+rect(260,87,175,38,L,'none',3)+rect(260,87,110,38,G,'none',3)
  a+=arrow(110,234,110,266)+arrow(340,234,340,266)+text(35,300,'回原圖p',29,B,700)+text(250,300,'判整體可疑',29,G,700)
  return a+caption('局部位置與整圖各有教學責任','示意條長不代表實測或效能')
 if k=='fd-frames':
  a=belt(20,15,.85,85)+belt(20,175,.85,85+85/3)+text(325,55,'前幀',27,'white',700)+text(325,215,'後幀',27,'white',700)
  return a+caption('同方件向右移動，相機固定','只改時間，不偷換工件')
 if k=='fd-values':
  a=text(25,30,'前幀',27,B,700)+cells([20,100,100,100,20],45)+text(25,139,'後幀',27,G,700)+cells([20,20,100,100,100],154)+text(25,247,'絕對差',27,O,700)+cells([0,80,0,0,80],262,O)
  return a+caption('同一橫切列，逐座標相減','灰階給定算例；中間重疊不變')
 if k=='fd-bands':
  a=rect(25,35,425,205,'#142332','#142332',4)+rect(110,80,37,110,'white','none',0)+rect(220,80,37,110,'white','none',0)+text(70,281,'離開帶',29,B,700)+text(260,281,'進入帶',29,O,700)
  return a+caption('兩亮帶源自同一方件移動','不能從兩帶直接數出兩個物件')
 if k=='bg-history':
  a=''
  for i,pos in enumerate([50,165,290]):a+=belt(15+i*145,30,.3,pos)
  a+=text(30,135,'多時間影格 → 同位置統計',29,B,700)+arrow(230,152,230,175)+belt(55,182,.8,None)
  return a+caption('常見外觀累積成背景模型','MOG2可保留多個常見分布')
 if k=='bg-compare':
  a=belt(15,15,.49,None)+belt(255,15,.49,160)+text(50,125,'累積背景',26,B,700)+text(282,125,'目前有方件',26,O,700)+arrow(105,140,170,172)+arrow(370,140,290,172)+belt(55,182,.8,160,mask=True)
  return a+caption('同位置比較，方件形成前景','不是只和上一張影格相減')
 if k=='bg-update':
  a=belt(20,10,.95,160)+text(25,203,'停留很久＋背景持續更新',29,O,700)+arrow(237,219,237,244)+rect(25,257,425,62,'#142332','#142332',3)+text(238,298,'前景可能消失',29,'white',700,'middle')
  return a+caption('物件仍在場景，模型已學作背景','示意不指定幾秒必然吸收')
 if k=='byte-detections':
  a=belt(15,45,1,65,'L')+rect(284,85,85,85,'url(#steel)','#DAE1E7',1)+rect(76,80,92,95,'none',O,0)+rect(280,80,92,95,'none',B,0)+text(72,28,'低分 .3',28,O,700)+text(278,28,'高分 .9',28,B,700)
  a+=rect(110,45,33,76,'#A2ACB3','#748A9C',0)+text(25,263,'ID7處短暫遮擋 → 低分框',29,O,700)
  return a+caption('偵測器先出框與分數','分數為給定例，不是門檻建議')
 if k=='byte-match':
  a=text(20,30,'第一輪：高分框配現有軌跡',28,B,700)+rect(25,52,72,67,'none',G,0)+rect(32,58,72,67,'none',B,0)+arrow(125,83,220,83)+text(240,91,'已配對',29,G,700)
  a+=text(20,168,'第二輪：剩餘軌跡配低分框',28,O,700)+rect(25,190,72,67,'none',G,0)+rect(32,196,72,67,'none',O,0)+text(47,240,'L',35,N,700)+arrow(125,223,220,223)+text(240,234,'續接ID7',29,G,700)
  return a+caption('先高再低，低分仍需位置依據','孤立低分框不直接產生新ID')
 if k=='byte-life':
  a=''
  for i,(lab,col) in enumerate([('ID7',G),('lost',O),('移除',R)]):a+=rect(20+i*160,45,130,90,'white',col,4)+text(85+i*160,103,lab,29,col,700,'middle')
  a+=arrow(155,90,175,90)+arrow(315,90,335,90)+text(20,188,'未匹配 → 暫留 → 超期移除',28)+text(20,251,'保留期內匹配可重新啟用ID7',27,G,700)
  return a+caption('續接需證據；長遮擋仍會丟失','計數線與事件由下游另訂')
 from batch6_expanded_graphics import graphic as expanded
 return expanded(k)

from render import rect,text,line,arrow,circle,plate,group,feature,pill,B,N,G,O,L,PALE
import math

def washer(x,y,s=1,defect=False,patches=False):
 a=circle(100,100,85,'#748A9E','#C8D6E3')+circle(100,100,37,'#748A9E',PALE)
 if defect:a+='<path d="M175,85 H192 V115 H175 Z" fill="'+PALE+'" stroke="'+PALE+'"/>'
 if patches:
  for xx,yy,lab in [(100,25,'A'),(174,100,'B'),(25,100,'C')]:a+=rect(xx-16,yy-16,32,32,'none',B,1)+text(xx-9,yy-24,lab,25,B,700)
 return group(x,y,s,a)

def gram(x,y,angles):
 a=''
 for i,u in enumerate(angles):
  for j,v in enumerate(angles):
   val=math.cos(math.radians(u-v));a+=rect(x+58*j,y+58*i,55,55,'#BBD5EF' if val>.7 else '#ECF2F8',L,2)+text(x+58*j+27,y+58*i+36,f'{val:.1f}',23,N,500,'middle')
 return a

def pixelwasher(x,y,s=1):
 # Analytic coarse sampling of the same washer, not an edit of any bitmap.
 a=''
 for i in range(8):
  for j in range(8):
   covered=0
   for sy in range(10):
    for sx in range(10):
     xx=(j+(sx+.5)/10)*25-100;yy=(i+(sy+.5)/10)*25-100;rr=math.hypot(xx,yy)
     covered+=37<rr<85 and not (75<xx<92 and -15<yy<15)
   fraction=covered/100
   col='#'+''.join(f'{round(bg+(fg-bg)*fraction):02X}' for bg,fg in zip((245,249,255),(196,210,224)))
   a+=rect(j*25,i*25,24,24,col,L,0)
 return group(x,y,s,a)

def defectmap(x,y,s=1):
 a=plate(0,0,1)+rect(115,44,38,62,'#FFE1B5',O,4)
 return group(x,y,s,a)

def noisyplate(x,y,s,amount,defect=True):
 a=plate(0,0,1,defect=defect)
 for i in range(8):
  for j in range(12):
   if ((i*7+j*11)%9)<amount:a+=rect(j*21,i*20,19,18,'#879DB5' if (i+j)%2 else '#EEF4F9','none',0)
 return group(x,y,s,a)

def scene(boxes=False,points=False,links=False,neutral=False):
 a=''
 for j,(x,y,col) in enumerate([(25,35,B),(255,115,G)]):
  if neutral:col='#647A91'
  a+=plate(x,y,.75)
  if boxes:a+=rect(x-9,y-16,206,154,'none',col,6)+text(x,y-23,'物件 '+str(j+1),24,col)
  if points:
   pts=[(x+71.25,y),(x+45,y+76.5),(x+142.5,y+76.5)]
   if links:
    for u,v in [(0,1),(1,2),(2,0)]:a+=line(*pts[u],*pts[v],col,3)
   for (xx,yy),lab in zip(pts,'ABC'):a+=circle(xx,yy,6,col)+text(xx+9,yy-7,lab,23,col,700)
 return a

def pointgroups():
 a=''
 for x,col,name in [(65,B,'物件 1'),(315,G,'物件 2')]:
  pts=[(x+45,290),(x,355),(x+95,355)]
  for u,v in [(0,1),(1,2),(2,0)]:a+=line(*pts[u],*pts[v],col,3)
  for (xx,yy),lab in zip(pts,'ABC'):a+=circle(xx,yy,6,col)+text(xx+9,yy-8,lab,24,col,700)
  a+=text(x,405,name,27,col)
 return a

def graphic(k):
 if k=='pose-two':return scene()+text(15,305,'同一張原始影像',31,B,700)+text(15,355,'要保留各物件 A／B／C 身份',26)+text(15,404,'點名對應同一部位',28)
 if k=='pose-topdown':
  a=group(0,20,.86,scene(boxes=True))+arrow(245,250,245,282)
  return a+pointgroups()
 if k=='pose-bottomup':
  a=group(0,20,.86,scene(points=True,neutral=True))+arrow(245,250,245,282)
  return a+pointgroups()
 if k=='pose-correspondence':
  return plate(100,80,1.1,points=True)+text(15,315,'A：缺口轉角　B／C：孔心',26)+text(15,365,'影像點名 ↔ CAD 同名位置',27)+text(15,415,'示意三點，不保證唯一解',26,O)
 if k=='pose-calibration':
  a=plate(40,50,.8,points=True)+arrow(280,100,450,100)+text(350,80,'X',27,B)+arrow(280,100,280,210,G)+text(294,208,'Y',27,G)
  return a+text(280,245,'Z = 0 平面例',23)+pill(20,265,220,'相機 K／畸變')+pill(255,265,215,'3D 點／單位',G)+text(15,365,'CAD 座標與影像身份對齊',27)+text(15,414,'鎖定校正、解法與點數',27)
 if k=='pose-transform':
  a=plate(30,45,.6,points=True)+arrow(210,100,330,100)+rect(350,55,105,90,'#DCE8F5',B,8)+circle(402,100,26,B,PALE)+text(20,200,'物體座標',28)+text(340,200,'相機座標',28)
  a+=pill(105,255,285,'R：旋轉　t：平移')
  return a+text(15,360,'相機點 = R × 物體點 + t',28)+text(15,410,'t 的單位跟 CAD 一致',28)
 if k=='pose-reproject':
  a=plate(105,65,1.1,points=True)
  for x,y in [(214,72),(173,174),(317,183)]:a+=circle(x,y,9,G,'none')
  return a+text(15,319,'橘實心：觀測點',28,O)+text(15,365,'綠空心：姿態重投影',28,G)+text(15,415,'逐點比較，不能只看平均',27)
 if k=='pose-delivery':
  a=''
  for i,(lab,v) in enumerate([('A',.8),('B',.3),('C',.6)]):a+=text(20,65+80*i,lab,32)+rect(90,39+80*i,v*300,30,B,'none',3)
  return a+text(15,298,'示意殘差；單位為 pixel',27)+text(15,350,'保存點ID、可見性與校正版本',25)+text(15,405,'R／t → 工作站；外參另行核對',25)
 if k=='pose-ambiguous':
  a=plate(100,70,1.1,points=True)+rect(177,40,100,80,'#647A91','#647A91',5)
  return a+text(15,305,'辨識方向的缺口被遮住',29,O)+text(15,360,'孔洞外觀相似，點名可能互換',25)+text(15,412,'這是身份問題，不只是點偏移',25)
 if k=='pose-ambiguity-error':
  a=''
  for j,(col,name) in enumerate([(B,'候選 1'),(G,'候選 2')]):
   y=55+160*j;a+=text(15,y,name,28,col)
   for i in range(3):a+=circle(205+i*90,y-10,10,col,'none')+circle(208+i*90,y-7,5,O)
  return a+text(15,337,'两套身份都可能有小殘差',27)+text(15,397,'低重投影誤差 ≠ 物理姿態正確',24,O)
 if k=='pose-disambiguate':
  a=plate(30,50,.7)+rect(63,70,25,25,B,B,1)+text(245,105,'可移除標記',29,B)+plate(30,235,.7)+arrow(270,285,410,205,G)+text(260,345,'額外視角',29,G)
  return a+text(15,415,'先驗表面限制、校正與節拍',26)
 if k=='dino-gram-input':
  a=washer(135,10,.8,patches=True)+arrow(185,210,120,255)+arrow(290,210,360,255)+pill(15,276,220,'較早教師',G)+pill(263,276,220,'目前學生')
  return a+text(15,378,'同一圖、同一組 patch 位置',26)+text(15,424,'教師關係作目標，學生可更新',25)
 if k=='dino-gram-matrix':
  a=text(25,40,'教師目標',29,G)+text(275,40,'目前學生',29,B)+gram(20,85,[0,30,90])+gram(275,85,[0,60,80])
  a+=arrow(267,175,215,175,O)+text(15,310,'每格：兩個 patch 的相似度',26)+text(15,360,'行列皆依 A／B／C 排列',27)+text(15,410,'對稱矩陣；二維向量算例',26)
  return a
 if k=='dino-gram-update':
  a=pill(20,35,220,'關係差異',G)+pill(267,35,220,'其他自監督損失')
  a+=arrow(120,90,205,180,G)+arrow(370,90,285,180)+pill(100,205,310,'共同更新學生參數')
  return a+text(15,320,'保留局部關係，特徵仍能改變',25)+text(15,369,'只在訓練中施加此約束',28,B)+text(15,419,'部署由骨幹交出特徵',28)
 if k=='dino-washer':return washer(110,30,1.3,patches=True)+text(15,345,'同一墊圈，多個局部位置',29)+text(15,402,'先鎖定解析度與前處理',28)
 if k=='dino-patchfeatures':
  a=washer(15,25,.85,patches=True)+arrow(220,120,253,120)
  for i,(lab,vals) in enumerate([('A',[1,.4,.7]),('B',[.3,1,.6]),('C',[.8,.5,.2])]):a+=text(275,55+i*85,lab,28)+feature(325,30+i*85,vals)
  return a+text(15,345,'每個位置一個上下文表示',27)+text(15,398,'彩色／條塊不是缺陷分數',27,O)
 if k=='dino-nearest':
  a=text(15,40,'查詢位置 B',29,B)+feature(60,65,[.3,1,.6])+arrow(200,90,260,90)+feature(300,65,[.35,.9,.6],G)+text(290,40,'參考位置',29,G)
  a+=washer(40,180,.95,patches=True)+washer(260,180,.95,patches=True)
  return a+text(15,418,'下游比較表示，再回到原圖核對',25)
 if k=='dino-version':return washer(135,15,1.05)+pill(70,275,370,'固定骨幹／解析度')+text(15,374,'部署不使用 Gram 教師',28)+text(15,418,'來源影像與前處理一併保存',25)
 if k=='dino-library':
  a=washer(10,20,.65)+arrow(180,85,245,85)+rect(270,20,210,180,'white',L,8)
  for i,vals in enumerate([[1,.4,.7],[.3,1,.6],[.8,.5,.2]]):a+=group(295,45+50*i,.8,feature(0,0,vals))
  return a+text(15,280,'新骨幹 → 重抽參考特徵',29,B)+text(15,340,'不同骨幹的庫不能直接混用',26)+text(15,405,'保存影像ID、位置與版本',27)
 if k=='dino-evaluate':
  a=washer(5,10,.6)+washer(190,10,.6,defect=True)+text(335,80,'同留出集',27)
  for i,(title,label,col) in enumerate([('工作結果','命中／漏檢',B),('運算成本','抽特徵＋查庫',G),('維護成本','記憶體／重建',O)]):a+=pill(10,170+i*84,205,title,col)+text(240,201+i*84,label,27,col)
  return a
 if k=='dino-notch':return washer(110,20,1.3,defect=True)+arrow(450,115,372,140,O)+text(310,65,'右側缺口',27,O)+text(15,350,'同件、同方向、同一缺口',28)+text(15,412,'先確認輸入有沒有工作細節',25)
 if k=='dino-resolution':
  return pixelwasher(120,25,1.1)+text(15,317,'粗取樣把小缺口平均變弱',27)+text(15,368,'這是輸入取樣示意',28)+text(15,418,'不是模型推論熱圖',28,O)
 if k=='dino-retake':
  return washer(15,40,.55,defect=True)+arrow(170,100,235,100)+washer(280,20,.95,defect=True)+text(15,275,'調整工作距離／ROI／解析度',26)+text(15,338,'重抽特徵 → 重測漏檢與誤報',25)+text(15,405,'看得清楚仍不保證判得正確',25,O)
 if k=='diff-noise-branches':
  a=plate(15,100,.6,defect=True)+text(15,245,'原圖 A',29)+arrow(182,154,255,90)+arrow(182,154,255,245)
  a+=noisyplate(290,35,.65,7)+text(280,175,'高噪聲',27)+noisyplate(290,218,.65,2)+text(280,355,'低噪聲',27)
  return a+text(15,416,'同一原圖，兩個噪聲尺度',27)
 if k=='diff-guidance':
  a=plate(10,25,.65)+text(220,80,'正常估計 N',29,G)+arrow(235,120,235,278,G)+text(250,175,'引導',27,G)
  a+=noisyplate(10,235,.58,2)+arrow(175,280,265,280)+plate(298,235,.67)+text(290,388,'恢復 R',29,B)
  return a+text(15,430,'每尺度單步，不是整套只跑一次',24)
 if k=='diff-segment':
  a=plate(10,15,.55,defect=True)+text(15,145,'原圖 A',26)+plate(280,15,.55)+text(280,145,'恢復 R',26)
  a+=arrow(110,160,195,205)+arrow(365,160,280,205)+pill(120,220,280,'學習的分割網路')+arrow(260,270,260,297)+defectmap(190,300,.55)
  return a+text(15,355,'位置圖',27,O)+text(15,422,'比較線索由分割學習利用',26)
 if k=='gpt-features':
  a=plate(130,0,.85,defect=True)+arrow(235,145,235,180)+pill(85,193,310,'固定影像編碼器')
  a+=arrow(185,245,100,290)+arrow(315,245,395,290)+feature(55,315,[1,.3,.6])+feature(325,315,[.2,.9,.6])+text(15,410,'全局表示',27)+text(300,410,'局部表示',27)
  return a
 if k=='gpt-localize':
  a=pill(20,10,450,'局部表示 → 影像解碼器')+arrow(125,65,125,98)+feature(70,120,[.2,.9,.6])+arrow(175,145,250,145)
  a+=text(260,107,'與文字表示比相似',24)+text(260,155,'正常',25,G)+rect(345,134,30,23,G,'none',2)+text(260,212,'異常',25,O)+rect(345,191,115,23,O,'none',2)
  a+=arrow(365,230,280,268)+defectmap(135,280,.7)
  return a+text(15,421,'內建位置圖；順位為示意',25,O)
 if k=='gpt-prompt':
  a=defectmap(10,12,.52)+arrow(155,62,225,62)+pill(235,40,250,'提示學習器')+arrow(355,98,355,170)
  a+=pill(20,185,180,'影像表示')+arrow(205,208,265,208)+pill(285,185,200,'LLM')
  a+=text(15,287,'問題：哪裡異常？',27)+arrow(240,275,355,236)+arrow(355,243,355,325)
  return a+rect(35,345,440,74,'white',L,8)+text(48,392,'示意回答：支架中部有刮痕',25)
 if k=='dino-comparison-data':return washer(15,35,.95)+washer(270,35,.95,defect=True)+text(15,298,'同一正常／缺口留出集',28)+text(15,354,'固定取像、工作指標與硬體',26)+text(15,411,'兩個方案各自建相容的庫',27)
 if k in ['dino-compare-v2','dino-compare-v3']:
  newer=k.endswith('v3');col=G if newer else B
  a=washer(15,20,.65)+arrow(180,80,250,80,col)+group(290,50,1,feature(0,0,[.3,1,.6] if newer else [1,.4,.7],col))
  a+=arrow(345,120,345,175,col)+rect(245,190,210,96,'white',col,6)+text(270,245,'相容特徵庫',28,col)
  return a+text(15,335,'重抽特徵、重建下游' if newer else '保留原有版本與基準',28,col)+text(15,394,'比較錯誤與完整成本',28)
 if k=='diff-normal-training':
  a=plate(15,30,.6)+text(15,166,'正常圖',27)+arrow(195,85,265,85)+noisyplate(290,30,.6,5,False)+text(285,166,'加噪示意',27)
  a+=arrow(360,190,360,235)+pill(105,250,350,'學習噪聲估計與恢復')
  return a+text(15,365,'正常外觀提供恢復目標',28)+text(15,419,'真缺陷留給獨立驗證',27)
 if k=='diff-synthetic':
  a=plate(15,35,.85,defect=True)+text(20,223,'合成刮痕',28)+rect(280,35,200,136,'#E2EAF2',L,6)+rect(375,72,24,45,O,O,2)+text(288,223,'位置遮罩',28,O)
  return a+text(15,333,'影像與遮罩指同一部位',29)+text(15,391,'合成樣本不是實際缺陷驗證',25)
 if k=='diff-training-targets':
  a=pill(25,25,210,'正常恢復目標',G)+pill(265,25,215,'合成位置監督',O)
  a+=arrow(125,90,125,170,G)+arrow(370,90,370,170,O)+pill(25,193,210,'恢復網路',G)+pill(265,193,215,'分割網路',O)
  return a+text(15,334,'學去噪／恢復',28,G)+text(265,334,'學異常位置',28,O)+text(15,413,'兩個責任，最後一起驗整套',26)
 if k=='diff-save-pair':return plate(15,40,.75,defect=True)+plate(285,40,.75)+text(15,235,'原圖 A',30)+text(285,235,'恢復 R',30)+text(15,340,'同張來源、相同尺寸／座標',27)+text(15,406,'保留中間圖才知道錯在哪裡',25)
 if k=='diff-output':return defectmap(100,60,1.1)+text(15,330,'位置圖映回原圖尺寸',29)+text(15,384,'連同原圖給人工覆核',28)+text(15,431,'域內門檻与允收條件另驗',25)
 if k=='diff-time':
  a=''
  for i,(lab,w,col) in enumerate([('两尺度估計',310,B),('分割',190,G),('前後處理',100,O)]):a+=text(15,45+i*100,lab,29,col)+rect(15,63+i*100,w,32,col,'none',4)
  return a+text(15,402,'相對條長僅示意：全程都要量',25)
 if k=='diff-defect-input':return plate(105,65,1.1,defect=True)+text(15,325,'同一支架、中部刮痕',29)+text(15,385,'固定原圖，不更換異常位置',26)
 if k in ['diff-clean-detected','diff-retained-missed']:
  retained=k.endswith('missed');a=plate(15,30,.65,defect=retained)+text(245,90,'恢復 R 保留痕跡' if retained else '恢復 R 變乾淨',26)
  a+=text(15,192,'A + R → 分割',28,B)+arrow(220,204,220,226)
  a+=(plate(15,235,.65) if retained else defectmap(15,235,.65))+text(245,288,'位置圖漏掉' if retained else '位置圖找到',27,O)
  return a+text(15,410,'假設結果，需真實資料驗證',26)
 if k=='gpt-training-text':return plate(120,10,.95,defect=True)+rect(20,240,460,90,'white',L,8)+text(40,292,'支架中部有線狀痕跡',29)+text(15,411,'位置、影像与文字配對',28)
 if k=='gpt-training-targets':
  a=pill(20,35,215,'影像編碼器')+pill(270,35,210,'LLM')+text(155,138,'保持固定',30,N,700)
  a+=pill(20,218,215,'影像解碼器',G)+pill(265,218,220,'提示學習器',G)+text(160,327,'更新參數',30,G,700)
  return a+text(15,416,'位置与文字訓練訊號提供監督',25)
 if k=='gpt-review':
  a=defectmap(15,20,.75)+rect(245,40,235,120,'white',L,8)+text(261,88,'中部有痕跡',28)+text(261,134,'回原圖核對',27,B)
  return a+plate(135,220,.85,defect=True)+text(15,411,'文字、位置与原圖要對得上',26)
 if k=='gpt-mismatch':
  a=defectmap(125,20,.95)+rect(20,250,455,91,'white',O,8)+text(38,304,'假設錯答：左孔邊有裂縫',27,O)
  return a+text(15,412,'定位在中部，文字沒有相同證據',24)
 if k=='gpt-work-comparison':
  a=defectmap(15,20,.62)+text(210,80,'只看位置',29,B)+defectmap(15,190,.62)+text(210,245,'位置＋對話',29,G)
  return a+text(15,362,'同資料比較錯誤、延遲、工時',25)+text(15,416,'流暢不等於少誤判或省時間',25)
 raise ValueError(k)

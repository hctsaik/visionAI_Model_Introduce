from render import rect,text,line,arrow,circle,plate,group,feature,pill,bars,B,N,G,O,L,PALE
import math
def gear(x,y,s=1):
 pts=[]
 for i in range(48):
  r=90 if i%4 in [0,1] else 73;a=2*math.pi*i/48;pts.append((100+r*math.cos(a),100+r*math.sin(a)))
 return group(x,y,s,'<polygon points="'+' '.join(f'{a:.1f},{b:.1f}' for a,b in pts)+'" fill="url(#steel)" stroke="#73899E" stroke-width="3"/>'+circle(100,100,30,'#73899E',PALE))
def bearing(x,y,s=1):
 a=circle(100,100,86,'#73899E','#CED9E4')+circle(100,100,58,'#73899E',PALE)
 for j in range(8):
  a+=circle(100+70*math.cos(j*math.pi/4),100+70*math.sin(j*math.pi/4),8,'#647A91','#E9EFF5')
 return group(x,y,s,a)
def vectorrow(y,label,values,col=B):return text(15,y+27,label,28,col)+feature(235,y,values,col)
def sheet(x,y,label,w=170):return rect(x,y,w,60,'white',L,6)+text(x+12,y+40,label,28)
def matrix(labels=True,train=False):
 a=text(160,30,'支架詞',25,B)+text(305,30,'齒輪詞',25,O)+plate(0,65,.37)+gear(0,220,.47)
 for i in range(2):
  for j in range(2):
   x,y=160+145*j,55+145*i;col=G if i==j else O
   a+=rect(x,y,125,115,'#E6F2EB' if i==j else '#FFF0DA',col,8)
   a+=text(x+62,y+53,'配對' if i==j else '不配對',25,col,700,'middle')
   a+=text(x+62,y+90,'拉近' if i==j else '分開',26,col,600,'middle')
 return a
def graphic(k):
 if k=='clip-softmax':
  a=text(158,29,'支架詞',25)+text(325,29,'齒輪詞',25)+plate(8,78,.38)+gear(8,226,.48)
  for i in range(2):
   for j in range(2):
    a+=rect(155+165*j,65+145*i,125,100,'#A6C9EE' if i==j else '#E8EFF8',B if i==j else L,4)+text(217+165*j,125+145*i,'正配對' if i==j else '其他',24,B,600,'middle')
  a+=arrow(160,181,438,181,B,3)+arrow(299,69,299,302,B,3)
  return a+text(15,362,'每行與每列各做 softmax',26)+text(15,412,'正配對與同批其他項比較',26)
 if k=='siglip-local':
  a=matrix()
  return a+text(15,367,'每對各算 sigmoid 損失',26)+text(15,416,'再合併更新同一組參數',26)
 if k=='catalog':
  return plate(20,65,.8)+gear(275,55,.8)+bearing(160,230,.72)+text(15,32,'同一資料庫，不同外觀',27)+text(15,420,'先界定要找的零件',28)
 if k=='descriptions':
  a=sheet(25,20,'金屬支架',275)+sheet(25,110,'有齒的齒輪',275)+sheet(25,200,'滾珠軸承',275)
  for j,values in enumerate([[.7,1,.3],[.3,.6,1],[1,.3,.7]]):a+=arrow(315,50+j*90,365,50+j*90)+group(380,35+j*90,.8,feature(0,0,values))
  return a+text(20,335,'每句各有一個表示',29)+text(20,390,'描述改了，比較也會改',28)
 if k=='retrieval':
  return sheet(15,15,'查詢：金屬支架',445)+plate(20,125,.68)+rect(8,105,195,155,'none',B,8)+gear(275,122,.64)+text(35,305,'候選前列',28,B)+text(282,305,'較後列',28)+text(15,365,'先看找回的原始照片',29)+text(15,410,'再核對工件身份',28)
 if k=='text-cache':
  a=vectorrow(35,'金屬支架',[1,.7,.3],B)+vectorrow(125,'齒輪',[.3,1,.6],O)+vectorrow(215,'軸承',[.8,.5,1],G)
  return a+rect(220,15,240,275,'none',L,10)+text(15,343,'候選文字 ↔ 快取表示',29)+text(15,396,'一併保存模型與文字版本',26)
 if k in ['cache-match','siglip-match']:
  a=plate(10,20,.62)+arrow(180,70,235,70)+feature(255,47,[1,.6,.3],B)+text(205,27,'影像編碼',24,B)
  a+=arrow(310,110,310,165)+rect(180,185,270,100,'#E9F1FC',B,8)+text(200,246,'表示比較',32,B,700)
  a+=sheet(10,180,'快取',130)+arrow(145,230,173,230,G)+arrow(310,290,310,325)
  a+=rect(195,345,215,23,B,'none',3)+rect(195,385,85,23,'#9CBDDF','none',3)+text(15,364,'支架',26)+text(15,405,'齒輪',26)
  return a
 if k=='cache-refresh':
  a=sheet(15,20,'舊：零件',185)+line(22,45,190,65,O,4)+sheet(240,20,'新：聯軸器',245)+arrow(360,100,360,152)
  a+=feature(257,174,[1,.3,.8,.6,.2],B)+arrow(330,235,330,267)+plate(25,280,.50)+gear(220,280,.45)+text(15,417,'重測已知與未知件',29)
  return a+text(15,140,'重新編碼',28,B)+text(15,211,'更新快取',28,B)
 if k=='gear-input':
  return gear(112,28,1.3)+text(15,345,'同一齒輪影像',31,B,700)+text(15,398,'輸入不因候選錯誤而改變',26)
 if k=='missing-candidate':
  return plate(20,20,.64)+bearing(280,12,.65)+text(35,176,'支架',30)+text(320,176,'軸承',30)+rect(20,214,205,36,O,'none',4)+rect(20,274,125,36,'#C6D5E6','none',4)+text(250,243,'仍有第一名',28,O)+text(15,365,'齒輪不在候選裡',30,O,700)+text(15,413,'順位示意，非模型實測',25)
 if k=='candidate-review':
  return gear(20,30,.75)+sheet(225,44,'新增齒輪',240)+arrow(155,111,210,86)+text(15,240,'補候選後重新測試',31,B,700)+plate(25,282,.55)+bearing(215,268,.55)+text(15,410,'細微差異也可測專用分類器',25)
 if k=='paired-training':
  return plate(15,30,.56)+line(180,90,245,90,G,5)+sheet(265,55,'金屬支架',205)+gear(15,215,.65)+line(180,280,245,280,G,5)+sheet(265,245,'齒輪',205)+text(15,405,'圖文身份提供正負標籤',28)
 if k=='pair-matrix':return matrix()+text(15,393,'每一格都是一個學習例',27)
 if k=='pair-update':
  a=rect(20,35,200,100,'#E6F2EB',G,8)+text(38,93,'正配對損失',29,G)+rect(265,35,210,100,'#FFF0DA',O,8)+text(280,93,'負配對損失',29,O)
  a+=arrow(120,140,180,202)+arrow(370,140,300,202)+pill(128,218,260,'合併梯度更新')
  a+=arrow(182,270,120,325)+arrow(325,270,390,325)+pill(15,346,217,'影像編碼器')+pill(268,346,217,'文字編碼器',G)
  return a
 if k=='sigmoid-pairs':
  a=text(15,38,'正配對：支架圖＋支架詞',28)+line(30,110,450,110,L,4)+circle(135,110,9,O)+arrow(160,110,365,110,G)+text(15,167,'目標：提高配對分數',28,G)
  a+=text(15,230,'負配對：支架圖＋齒輪詞',28)+line(30,305,450,305,L,4)+circle(345,305,9,O)+arrow(320,305,105,305,O)+text(15,360,'目標：降低配對分數',28,O)
  return a+text(15,417,'學習方向示意，非實測數字',25)
 if k=='loss-aggregate':
  a=''
  for i,(x,y,col) in enumerate([(35,30,G),(295,30,O),(35,180,O),(295,180,G)]):
   a+=rect(x,y,165,80,'#EEF4FC',col,8)+text(x+82,y+50,'配對 '+str(i+1),27,col,700,'middle')
   if i<2:a+=line(x+82,y+85,245,150,col,4)+arrow(245,150,245,325,col,4)
   else:a+=arrow(x+82,y+88,245,325,col,4)
  return a+pill(110,345,280,'同一組模型參數')
 if k=='score-review':
  a=bars(['支架','齒輪','軸承'],[.8,.35,.2])
  return a+text(15,351,'示意分數 ≠ 正確率',29,O)+text(15,397,'未知件與低分件另做覆核',26)
 if k=='both-missing':
  a=text(15,40,'共同候選：支架／軸承',29)
  for j,lab in enumerate(['CLIP','SigLIP']):a+=pill(15,100+j*133,140,lab)+rect(190,108+j*133,210,27,'#B9CFE5','none',3)+rect(190,148+j*133,125,27,'#DFE8F2','none',3)
  return a+text(15,385,'兩者皆無「齒輪」可選',29,O)+text(15,425,'不假設兩個模型的實際順位',24)
 if k=='comparison-work':
  a=plate(20,35,.48)+gear(195,18,.48)+bearing(343,18,.48)+text(15,171,'同資料、候選與取像',29,B)
  for j,(label,col) in enumerate([('誤配／漏掉未知件',O),('模型與前處理成本',B),('人工覆核需求',G)]):a+=circle(30,230+j*70,8,col)+text(55,240+j*70,label,28)
  return a
 raise ValueError(k)

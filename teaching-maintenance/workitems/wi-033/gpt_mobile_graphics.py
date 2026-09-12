from render import rect,text,line,arrow,circle,group,feature,pill,B,N,G,O,L,PALE

def sample(x,y,s=1,mark=None,labels=False):
 a=rect(0,0,180,220,'#C9D5E1','#73899E',8)+circle(53,58,30,'#73899E',PALE)+circle(137,169,22,'#73899E',PALE)
 a+='<path d="M103,127 l35,-31" stroke="#8B655D" stroke-width="4"/>'
 if mark=='p':a+=rect(94,91,52,47,'#FFE0AE',O,4)
 if mark=='q':a+=circle(137,169,31,O,'#FFE0AE')
 if labels:a+=text(140,95,'p',28,B,700)+text(158,201,'q',28,G,700)
 return group(x,y,s,a)

def graphic(k):
 if k=='gpt-mobile-training':
  a=sample(20,15,.75,'p')+rect(280,15,135,165,'#E5EEF7',L,6)+rect(350,84,40,36,O,O,3)
  return a+text(15,237,'合成影像',29)+text(265,237,'同位置遮罩',29)+pill(25,287,450,'文字：右側有異常區')+text(15,404,'學解碼器／提示器；骨幹固定',25)
 if k=='gpt-mobile-location':
  a=sample(15,30,.8)+arrow(195,115,270,115)+sample(300,30,.8,'p')
  return a+text(15,266,'同張測試圖',28)+text(290,266,'內建位置圖',28,O)+text(15,338,'局部特徵經解碼、比狀態文字',25)+text(15,405,'位置線索來自模型內建支路',26)
 if k=='gpt-mobile-answer':
  a=sample(15,5,.45,'p')+arrow(118,55,175,55)+pill(190,30,295,'提示學習器')+arrow(350,90,350,170)
  a+=text(15,176,'影像表示',26)+text(15,222,'使用者問題',26)+arrow(170,192,260,192)+pill(278,171,205,'固定 LLM')+arrow(365,228,365,275)
  return a+rect(20,292,465,104,'white',L,8)+text(40,333,'示意：右側有可疑痕跡',27)+text(40,376,'回原圖核對位置與說法',27,B)
 if k=='gpt-mobile-evidence':return sample(135,10,1.15,labels=True)+text(15,328,'p：看得見的線狀痕跡',28,B)+text(15,377,'q：正常孔邊',28,G)+text(15,424,'兩處分開核對',27)
 if k=='gpt-mobile-wrong':
  return sample(15,20,.85,'q',True)+rect(215,50,270,172,'white',O,8)+text(231,94,'假設錯答',29,O,700)+text(230,145,'右下裂縫是',27)+text(230,191,'夾具壓壞。',27)+text(15,330,'位置誤指 q；根因沒有證據',26)+text(15,400,'流暢肯定仍要退回覆核',27)
 if k=='gpt-mobile-review':
  a=sample(335,5,.6,labels=True)
  for i,(lab,s,col) in enumerate([('觀察','p 有線痕',B),('推測','可能刮傷',O),('未知','深度／根因',G)]):a+=pill(15,35+110*i,120,lab,col)+text(155,67+110*i,s,28,col)
  return a+text(15,418,'保存原圖，補拍後依規範處置',25)
 if k in ['gpt-mobile-winclip','gpt-mobile-anomalyclip','gpt-mobile-gpt']:
  a=sample(20,20,.7)+arrow(175,100,260,100)+sample(310,20,.7,'p')
  if k.endswith('winclip'):
   a+=rect(45,60,65,65,'none',B,2)+rect(70,90,65,65,'none',B,2)
   captions=['人工狀態文字＋視窗聚合','WinCLIP+ 可加正常參考','交出分數與位置線索']
  elif k.endswith('anomalyclip'):captions=['輔助資料先學狀態提示','用已學模型驗證新工件','交出分數與位置線索']
  else:captions=['合成圖／遮罩／文字先對齊','內建定位再轉提示接 LLM','交出位置與對話回答']
  for i,cap in enumerate(captions):a+=text(15,272+i*68,cap,27,B if i==0 else N)
  return a
 raise ValueError(k)

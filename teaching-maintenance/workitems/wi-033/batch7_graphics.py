"""Authored, code-native mechanism illustrations; no inference outputs."""
from render import rect,text,line,arrow,circle,group,pill,B,N,G,O,L,PALE
from batch3_graphics import grid,caption,matrix
R='#C6473D'
def panel(x=20,y=20,s=1,style='top',defect=0,mask=False,noise=False,outline=False,faint=False):
 a=rect(0,0,360,240,'#13222F' if outline else 'url(#steel)','white' if outline else '#73899E',9)
 holes=[(65,47,24),(295,47,24)] if style in ('top','ano','paint') else [(115,122,26),(275,122,22)]
 if style=='sr':holes=[(125,105,46),(285,105,29)]
 for xx,yy,rr in holes:a+=circle(xx,yy,rr,'white' if outline else '#73899E','#13222F' if outline else 'white')
 if style=='sr':
  for xx,yy in [(18,18),(342,18),(18,222),(342,222)]:a+=circle(xx,yy,6,'#73899E')
 locs=[(175,184,80,40)] if style in ('top','paint') else [(108,196,100,34),(282,195,58,27)]
 if style=='ano':locs=[(100,159,92,65),(280,186,54,34)]
 for j,(xx,yy,ww,hh) in enumerate(locs):
  if mask:a+=rect(xx-ww/2,yy-hh/2,ww,hh,'#CE791744',O,4)
  if defect>j:
   if style=='paint':a+=f'<path d="M {xx-25},{yy-10} q 17,-15 33,0 q 20,6 10,20 q -18,8 -43,-2 Z" fill="#25313A"/>'
   else:a+=line(xx-ww/2+8,yy+hh/2-7,xx+ww/2-8,yy-hh/2+7,'#9CAAB5' if faint else '#253846',2 if faint else 5)+line(xx-ww/2+13,yy+hh/2-3,xx+ww/2-3,yy-hh/2+9,'white',1 if faint else 2)
 if noise:
  for i in range(95):a+=circle(8+(i*67)%342,7+(i*43)%227,2,'#6A7886')
 return group(x,y,s,a)
def gripper(x=10,y=10,s=1,stage=0):
 a=rect(0,0,220,175,'#E4EBF1','#73899E',5)+rect(72,117,76,44,'url(#steel)','#73899E',2)+rect(72,10,76,35,N,N,2)
 gap=[54,39,37][stage];drop=[32,63,92][stage]
 a+=line(110-gap,34,110-gap,drop+35,N,13)+line(110+gap,34,110+gap,drop+35,N,13)
 a+=line(110-gap,drop+35,110-gap+11,drop+35,N,9)+line(110+gap,drop+35,110+gap-11,drop+35,N,9)
 return group(x,y,s,a)
def strip(y=20):
 return ''.join(gripper(10+i*160,y,.64,i)+text(20+i*160,y+133,['張開 t−1','接近 t','夾住 t+1'][i],24) for i in range(3))
def vals(v,x=20,y=30,sz=70,col=B):
 return ''.join(rect(x+i*sz,y,sz-4,55,'white',col,2)+text(x+i*sz+(sz-4)/2,y+37,str(n),26,col,700,'middle') for i,n in enumerate(v))
def edge(x=25,y=20,s=1,blur=False,ring=False):
 a=rect(0,0,190,140,'#23313E','#73899E',3)+rect(0,0,95,140,'url(#steel)','none',0)
 if blur:
  for i,c in enumerate(['#B4C1CD','#9DAEBC','#7F929F','#657A88','#435966']):a+=rect(66+i*12,0,13,140,c,'none',0)
 if ring:a+=rect(88,0,8,140,'white','none',0)+rect(108,0,7,140,'#06121A','none',0)+rect(123,0,5,140,'#657A88','none',0)
 return group(x,y,s,a)
def graph_profile(values,x=25,y=180,w=415,h=100,col=B):
 a=line(x,y+h,x+w,y+h,L,2)+line(x,y,x,y+h,L,2)
 pts=' '.join(f'{x+i*w/(len(values)-1)},{y+h-v*h}' for i,v in enumerate(values))
 return a+f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="4"/>'
def graphic(k):
 k=k.removeprefix('b7-')
 if k=='conv-input':return strip()+grid(3,25,197,90)+text(135,237,'H(t−1)',29,B)+grid(3,285,197,90,col=G)+text(385,237,'C(t−1)',26,G)+caption('空間格保留夾爪與方塊位置','X(t)與上一時間的兩種狀態')
 if k=='conv-gate':return text(20,37,'X(t)、H(t−1) → 卷積門控',29,B,700)+grid(3,30,65,115,mark=(1,1))+text(180,100,'同位置：保留＋加入',27)+text(180,151,'f × 舊C + i × 候選',25)+text(20,234,'0.5 × 0.4 + 0.8 × 0.5',31)+text(20,291,'新C = 0.6',36,G,700)+caption('單一格的作者算例','f與i由網路學到，非手設常數')
 if k=='conv-next':return grid(3,20,25,90,col=G)+text(132,59,'C(t)',28,G,700)+text(132,111,'H(t)=o×tanh(C(t))',24)+arrow(65,132,65,212,G)+arrow(248,132,248,212)+pill(20,225,290,'下一步卷積門控')+text(328,168,'X(t+1)',26,B,700)+arrow(380,179,380,245)+arrow(375,245,319,245)+caption('C與H傳到下一個時間點','用H接任務頭，輸出另訓練')
 if k=='mae-tube':
  a=strip()
  for i in range(3):
   a+=grid(3,20+i*160,180,110)
   for rr,cc in [(0,1),(1,1),(2,1)]:a+=rect(20+i*160+cc*110/3,180+rr*110/3,34,34,'#9BABB9','white',0)
  return a+caption('同空間位置，跨時間一致遮蔽','小格示意；實際常用90–95%')
 if k=='mae-decode':return vals(['V','V','V'],20,20,65)+arrow(225,47,270,47)+pill(285,25,185,'編碼器')+arrow(375,83,375,130)+pill(250,148,220,'輕量解碼器')+vals(['M','M'],20,148,65,col=G)+arrow(158,175,237,175,G)+arrow(350,207,350,232)+grid(3,317,238,66)+caption('可見token＋遮蔽token解碼','V為可見，M為可學習遮蔽符號')
 if k=='mae-loss':return gripper(20,20,.82,1)+rect(77,92,60,45,'none',O,1)+gripper(270,20,.82,1)+rect(327,92,60,45,'none',G,1)+text(20,202,'原像素（訓練目標）',25,O)+text(270,202,'重建像素',25,G)+text(20,269,'同一遮蔽格：平方差',30,B,700)+caption('原像素只當重建監督','部署分類不使用這個解碼器')
 if k=='jepa-context':return gripper(20,20,.85,1)+rect(57,82,60,60,'#9BABB9','white',1)+arrow(216,92,260,92)+pill(275,70,200,'上下文編碼')+arrow(375,125,375,173)+pill(245,192,230,'預測器')+text(20,217,'遮蔽位置',29,O)+arrow(158,207,233,207,O)+caption('預測器知道要預測哪一格','完整遮蔽內容不送入上下文')
 if k=='jepa-target':return gripper(20,20,.8,1)+arrow(205,89,255,89,G)+pill(270,68,200,'目標編碼器',G)+arrow(370,124,370,155,G)+grid(3,332,170,75,col=G)+text(20,217,'完整影片',29)+text(20,287,'停止梯度；EMA更新權重',29,G,700)+caption('目標來自完整影片同位置','不是和上下文一起反傳梯度')
 if k=='jepa-loss':return text(20,35,'預測特徵',28,B,700)+vals([.2,.8],20,60,100)+text(270,35,'目標特徵',28,G,700)+vals([.4,.7],270,60,100,col=G)+text(20,185,'(|0.2−0.4| + |0.8−0.7|) / 2',26)+text(20,260,'平均L1差 = 0.15',34,O,700)+caption('兩維同位置作者算例','是訓練差異，不是異常分數')
 if k=='fill-learn':return panel(20,15,.48,defect=1,mask=True)+arrow(210,85,255,85)+pill(267,62,205,'LoRA適配')+text(20,192,'缺陷外觀／物件關係',29,B,700)+text(20,248,'注意位置：三種損失',29,G,700)+caption('少量缺陷與人工遮罩配對','微調文字與注意力的低秩參數')
 if k=='fill-generate':return panel(20,25,.55,mask=True)+arrow(229,90,273,90)+panel(280,25,.55,defect=1,mask=True)+text(20,200,'正常圖＋下方遮罩',27)+text(280,200,'合成刮傷',27,O)+text(20,278,'已學缺陷條件 → 多步去噪',29,B,700)+caption('同一雙孔板，下方區域填傷','mask指定位置，仍需核對結果')
 if k=='fill-select':return panel(20,20,.55,defect=1,mask=True,faint=True)+panel(280,20,.55,defect=1,mask=True)+text(20,204,'候選A：給定0.1',26)+text(280,204,'候選B：給定0.3',26,G)+text(20,271,'LFS選較大遮罩內LPIPS',29,B,700)+caption('相對正常圖，局部感知差異','較大不等於物理真實或正確')
 if k=='ano-condition':return panel(20,20,.5,style='ano',defect=2)+panel(285,20,.5,style='ano',mask=True)+text(20,182,'學外觀嵌入',27,B)+text(285,182,'編碼遮罩位置',27,G)+arrow(110,202,225,240)+arrow(375,202,275,240,G)+pill(55,250,385,'兩種條件共同引導')+caption('同板兩區：大左下、小右下','外觀學長相，遮罩描述位置')
 if k=='ano-feedback':return panel(20,20,.55,style='ano',defect=1,mask=True)+text(250,74,'右小區仍弱',29,O,700)+arrow(370,95,370,154,O)+text(250,192,'更多注意',29,B,700)+text(20,279,'比較暫時估計與正常圖',29)+caption('遮罩內變化弱處得到補強','生成時自適應，不保證必成功')
 if k=='ano-result':return panel(20,20,.72,style='ano',defect=2,mask=True)+text(310,86,'兩區均核對',26,G,700)+text(310,145,'孔位仍保留',26)+text(20,255,'背景與原正常圖融合',30,B,700)+caption('檢查圖像与mask逐區對應','兩個mask不能直接當兩個真傷')
 if k=='tf-input':return panel(20,10,.65,style='mid',mask=True)+panel(290,10,.45,style='mid',defect=2)+text(20,208,'正常板＋局部遮罩',27,B)+text(290,164,'參考刮傷',26,G)+text(20,281,'已訓練模型權重固定',31,G,700)+caption('中部兩孔、下方兩刮傷區','參考影像提供局部外觀線索')
 if k=='tf-gradient':return grid(3,25,20,110,mark=(2,1))+grid(3,345,20,110,mark=(2,1),col=G)+text(20,170,'生成局部特徵',25,B)+text(320,170,'參考特徵',25,G)+arrow(145,75,235,75)+arrow(335,75,255,75,G)+text(210,116,'對齊差',26,O)+arrow(245,139,245,206,O)+pill(30,227,425,'對latent求梯度 → 引導採樣')+caption('z(t)更新為下一步生成狀態','有反向求導，不代表訓練權重')
 if k=='tf-result':return panel(20,20,.72,style='mid',defect=2,mask=True)+text(310,80,'補弱區',28,O)+text(310,139,'保留紋理',28,G)+text(20,264,'核對孔位、材質與兩個遮罩',28,B,700)+caption('自適應遮罩＋背景紋理保持','跨材質參考仍可能帶錯外觀')
 if k=='control-input':return panel(20,20,.9,outline=True)+text(20,286,'文字：銀色雙孔金屬板',30,B,700)+caption('輪廓含外框與兩個孔位','輪廓條件不是缺陷分數')
 if k=='control-inject':return pill(20,25,440,'固定預訓練主幹')+pill(20,160,220,'可訓練分支',G)+arrow(255,180,310,180,G)+rect(327,142,139,73,'white',G,6)+text(397,188,'零卷積',27,G,700,'middle')+arrow(397,135,397,85,G)+text(20,263,'初始輸出0；訓練後可非0',29)+caption('條件殘差加入對應主幹層','零初始化不是永久不傳訊號')
 if k=='control-result':return panel(20,20,.5,noise=True)+arrow(212,78,270,78)+panel(280,20,.5)+text(20,195,'多步去噪，每步有條件',29,B,700)+text(20,265,'輸出孔位／外框回比原輪廓',28)+caption('布局受控，表面細節仍是生成','輪廓沒描述的裂紋仍不確定')
 if k=='paint-input':return panel(20,20,.58,style='paint',defect=1)+panel(270,20,.58,style='paint',defect=1,mask=True)+text(20,217,'原圖另存',29,B)+text(270,217,'1 = 可編修區',27,O)+caption('同板下方待編修污點','本圖遮罩約定，API需核對')
 if k=='paint-process':return panel(20,20,.9,style='paint',mask=True,noise=False)+arrow(67,170,147,170,B,4)+arrow(343,170,263,170,B,4)+text(20,282,'外部上下文 → 內部去噪',29,B,700)+caption('指定區域內生成連續外觀','各實作保留外區的方式不同')
 if k=='paint-check':return panel(20,20,.55,style='paint',defect=1,mask=True)+panel(280,20,.55,style='paint',mask=True)+text(20,207,'原影像',29,B)+text(280,207,'編修候選',29,G)+text(20,276,'接縫、孔位、遮罩外逐一比',28)+caption('編修結果另存，不覆蓋原始圖','影像補平不等於實體修復')
 if k=='restore-observe':return panel(20,20,.8,style='mid',noise=True)+text(325,89,'觀測 y',29,B,700)+text(20,272,'y = A x + n',36)+caption('A為退化，n為觀測雜訊','原x未知；以線性退化為例')
 if k=='restore-candidate':return panel(20,20,.5,style='mid',noise=True)+arrow(215,83,271,83)+panel(280,20,.5,style='mid')+text(20,207,'觀測＋退化條件',29,B)+text(20,278,'已學先驗 → 多步候選',29,G)+caption('先驗補足可能的影像細節','不同復原方法接入條件不同')
 if k=='restore-check':return vals([0,100],20,25,100)+vals([40,60],270,25,100,col=G)+text(20,132,'兩候選，各取平均',30)+arrow(120,153,195,222)+arrow(370,153,285,222,G)+pill(160,230,160,'觀測50')+caption('兩組不同細節，都對得回50','作者算例：相符不代表唯一')
 if k=='blur-forward':return edge(20,20)+arrow(220,89,265,89)+edge(280,20,blur=True)+graph_profile([1,1,.95,.7,.3,.05,0,0])+caption('清晰階躍經曝光平均展寬','示意單一直邊，不涵蓋所有模糊')
 if k=='blur-inverse':return edge(20,20,blur=True)+arrow(220,89,265,89)+edge(280,20)+text(20,225,'觀測模糊 → 估計清晰',30,B,700)+text(20,290,'反卷積或已學復原模型',29)+caption('輸出清晰只是候選','運動/失焦等退化要先分辨')
 if k=='blur-check':return edge(20,20,ring=True)+edge(280,20)+text(20,204,'候選有多重邊',28,O)+text(280,204,'独立清晰取像',26,G)+text(20,276,'同位置比邊緣，不只看銳利',28)+caption('振鈴可能造出不存在的輪廓','較短曝光、對焦與重新取像驗證')
 if k=='sr-low':return panel(20,20,.75,style='sr')+rect(72,78,32,32,'none',O,0)+arrow(125,105,340,115,O)+grid(4,350,75,110)+text(20,279,'固定左孔邊q的粗像素',30,B,700)+caption('矩形雙孔板，局部身份固定','不是把另一工件當同一觀測')
 if k=='sr-estimate':return grid(3,20,90,110)+arrow(145,140,218,64)+arrow(145,151,218,235,G)+grid(5,235,10,130)+grid(5,235,177,130,mark=(2,2),col=G)+text(380,73,'插值',28,B)+text(380,244,'學習',28,G)+caption('同一低解析，兩種估計路徑','高解析新增細節仍需證據')
 if k=='sr-check':return vals([20,80],20,20,100)+vals([40,60],270,20,100,col=G)+text(20,141,'子像素不同，平均都為50',29)+arrow(120,170,195,230)+arrow(370,170,285,230,G)+pill(170,245,140,'低解析50')+caption('降採樣一致，仍可能不唯一','這是數值算例，不是實測孔形')
 from batch7_expanded_graphics import graphic as expanded
 return expanded(k)

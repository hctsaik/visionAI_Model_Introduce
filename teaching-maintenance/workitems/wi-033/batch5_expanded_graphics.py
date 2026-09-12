from render import rect,text,line,arrow,circle,group,pill,B,N,G,O,L,PALE
from batch3_graphics import grid,matrix,caption
from batch5_graphics import board,vecbox,mapboard
R='#C6473D'
def contract(lines,holes=2):
 a=board(12,15,.43,holes,True,True)+text(193,58,'同一處理版本',29,B,700)
 for i,s in enumerate(lines):a+=rect(15,130+i*60,464,50,'white',B,5)+text(28,164+i*60,s,27,B)
 return a
def validation(holes=2):
 a=board(10,20,.6,holes,True,True)+board(265,20,.6,holes,False)
 a+=text(20,213,'真缺陷：查漏檢',28,R,700)+text(270,213,'正常：查誤報',28,G,700)
 a+=text(20,288,'固定留出資料 + 門檻 + 覆核量',26,B)
 return a
def graphic(k):
 if k.startswith('split-'):
  h=int(k[-1]);a=board(10,20,.45,h)+board(280,20,.45,h,True,True)
  a+=text(20,170,'訓練：確認正常',29,G,700)+text(272,170,'留出：獨立驗證',27,O,700)
  a+=line(246,20,246,305,L,3,True)+text(20,235,'正常變化須涵蓋',26)+text(272,235,'正常 + 真缺陷',26)+text(272,288,'不回灌訓練',26,O)
  return a+caption('同工件，訓練與驗證分開','不把待測影像自動當正常')
 if k.startswith('scratch-'):
  h=int(k[-1]);return board(40,20,1.1,h,True,True)+text(30,308,'同一工件A，追刮傷位置p',30,B,700)+caption('保持孔位、位置與允收定義','候選方案共用同一工作題目')
 if k.startswith('validation-'):return validation(int(k[-1]))+caption('位置結果回到原圖逐件核對','獨立驗證誤報、漏檢及耗時')
 if k=='pc-coreset-onehole':
  a=board(10,12,.44,1)+board(195,12,.44,1)+arrow(180,116,180,155)+pill(45,162,350,'固定CNN抽局部特徵')
  for xx,yy in [(70,239),(100,248),(83,270),(270,247),(290,270),(311,253)]:a+=circle(xx,yy,7,B)
  a+=circle(83,270,17,O,'none')+circle(290,270,17,O,'none')+text(345,257,'挑代表',25,O)
  return a+caption('同單孔板建立正常代表庫','查局部代表，非各位置高斯')
 if k in ['pc-delivery','rd-delivery']:
  a=mapboard('局部距離' if k=='pc-delivery' else '特徵差異',0 if k=='pc-delivery' else 2)
  return a+caption('交原圖、位置圖與影像分數','異常分數不直接給尺寸或類別')
 if k=='pc-contract':return contract(['固定骨幹 / 層 / 前處理','聚合 + coreset + 庫版本','新query與舊庫：特徵需相容'],0)+caption('庫存的是同規則的局部表示','換設定後需重建或重驗相容性')
 if k=='pc-cost':
  a=text(15,40,'給定512維 float32 特徵',30,B,700)+rect(15,80,440,44,B,'none',3)+text(15,159,'10000筆：20.48 MB',32,B,700)
  a+=rect(15,203,44,44,G,'none',3)+text(15,288,'1000筆：2.048 MB',32,G,700)
  return a+caption('僅特徵容量；不含索引/模型','筆數減十倍，不保證快十倍')
 if k=='pc-coverage':
  a=text(15,44,'正常局部 q = [2, 0]',32,G,700)+vecbox(15,88,'原库有[2, 0]','最近距離 = 0',G)+vecbox(265,88,'若只留[0, 0]','最近距離 = 2',O)
  a+=board(145,190,.55,0)+text(15,321,'同正常工件，距離卻升高',28,O,700)
  return a+caption('代表子集仍要涵蓋正常變化','給定反例，非coreset實際結果')
 if k=='pc-contamination':
  a=text(15,40,'誤存刮傷 [3, 2] 為正常',31,R,700)+board(15,78,.5,0,True,True)+arrow(210,126,256,126,R)+vecbox(266,88,'污染庫新增','r3 = [3, 2]',R)
  a+=text(15,251,'p查到r3：距離 = 0',33,O,700)+text(15,302,'刮傷仍在原圖，沒有消失',28)
  return a+caption('低距離也可能來自錯誤資料','正常庫來源需可追溯與審核')
 if k=='padim-contract':return contract(['固定取像 / 對齊 / 空間網格','特徵維度 + 各位置μ / Σ','正則化與評分設定一起保存'],1)+caption('每個位置有自己的正常統計','工件換位，不能直接套舊分布')
 if k=='padim-regularize':
  a=text(15,40,'高度相關的兩個特徵分量',29,B,700)+matrix([[1,1],[1,1]],15,75,70)+arrow(172,145,239,145)+matrix([[1.1,1],[1,1.1]],260,75,80)
  a+=text(15,250,'左：不可逆；右：加0.1 I',28,O,700)+text(15,301,'正則化只改善數值，不能補資料',26)
  return a+caption('協方差估計與求解要穩定','給定矩陣例；0.1不是建議值')
 if k=='padim-shift':
  a=rect(10,15,222,185,'white',L,2)+rect(260,15,222,185,'white',L,2)+board(20,35,.5,1)+board(294,55,.5,1)
  a+=rect(45,48,23,35,'none',O,0)+rect(295,48,23,35,'none',O,0)+text(20,240,'原定位',29,B)+text(272,240,'同好件位移',29,O)
  a+=text(20,299,'固定影像位置可能讀到不同部位',27)
  return a+caption('位移與工件缺陷是不同原因','先看對齊，再解讀位置距離')
 if k=='sub-contract':return contract(['骨幹 / 前處理 / 正常資料','均值 μ + 正交方向 U + 維度k','先減μ → 投影 → 再加μ'])+caption('本例μ=0，不是所有資料都為0','保存設定，才能重現局部殘差')
 if k=='sub-validation':return validation()+caption('k變大需重驗正常與真缺陷','不只挑最低的正常擬合誤差')
 if k=='sub-one':
  a=line(30,255,470,255,B,4)+line(310,80,310,255,R,5,True)+circle(310,80,8,O)+circle(310,255,8,G)+text(225,50,'x=[3,2]',30,O)
  a+=text(20,306,'一維：投影[3,0]，殘差2',31,B,700)
  return a+caption('保留水平正常方向','同一向量仍有垂直未解釋量')
 if k=='sub-full':
  a=rect(25,30,440,236,'#DFEDFA',B,0)+line(45,245,445,245,B,2)+line(45,245,45,47,B,2)+circle(310,80,9,G)+text(95,160,'x = 投影 = [3, 2]',32,G,700)
  a+=text(20,309,'全兩維保留：殘差 = 0',33,O,700)
  return a+caption('所有向量都能被完整投回','差異消失不代表工件沒缺陷')
 if k=='stf-train':
  a=board(10,20,.43,2)+arrow(170,65,233,65)+pill(244,40,240,'教師：固定')+arrow(355,101,355,150)+text(248,190,'正常特徵目標',27,B)
  a+=pill(245,232,240,'學生：更新',G)+arrow(356,212,356,232,G)+text(15,283,'只用正常圖',28,G,700)
  return a+caption('學生匹配教師的多尺度表示','不需要每種缺陷都作訓練類別')
 if k=='stf-contract':return contract(['教師checkpoint + 學生checkpoint','同層 / 同位置 / 向量正規化','插值 + 逐層相乘 + 門檻'])+caption('兩路權重配對保存','推論不再更新學生')
 if k=='rd-contract':return contract(['固定教師 + 可訓練瓶頸權重','反向學生 + 同尺度配對','餘弦差 / 插值 / 彙整設定'])+caption('教師、瓶頸、學生是一組','只交學生，嵌入來源仍不完整')
 if k=='ae-train':
  a=board(10,15,.44,2)+arrow(180,64,220,64)+pill(235,40,250,'AE編碼 / 解碼')
  a+=arrow(355,100,355,152)+board(278,165,.48,2)+text(20,206,'正常輸入',29,G)+text(20,256,'同圖作目標',29,B)
  return a+caption('正常影像教壓縮與還原','重建估計需和輸入同座標')
 if k=='ae-contract':return contract(['相同裁切 / resize / 座標','相同灰階或RGB數值範圍','差異定義 + 門檻 + 版本'])+caption('不要把0–1與0–255直接相減','同一套前處理與重建輸出約定')
 if k=='ae-errors':return validation()+caption('刮傷若被複製：可能漏檢','正常孔若被模糊：可能誤報')
 if k=='ae-copy':
  a=board(15,20,.55,2,True,True)+board(275,20,.55,2,True,True)+text(20,200,'原p：40',31,O,700)+text(280,200,'重建p：40',31,G,700)
  a+=text(70,294,'|40 − 40| = 0',39,R,700)
  return a+caption('重建跟著複製同一刮傷','小差異也可能是漏檢')
 if k=='ae-hole':
  a=board(15,20,.55,2)+board(275,20,.55,2)
  a+=circle(275+282*.55,20+181*.55,12,'#ABB8C4','#ABB8C4')+text(20,205,'原q：30',31,B,700)+text(270,205,'模糊q：100',30,O,700)
  a+=text(65,291,'|30 − 100| = 70',36,O,700)
  return a+caption('給定反例：正常小孔被模糊','較大差異也可能是誤報')
 if k=='draem-contract':return contract(['重建網路 + 判別網路權重','合成來源 / 區域策略 / 訓練版本','前處理 + 位置分數 / 門檻'])+caption('保存訓練來源以利重現','部署不輸入缺陷真值mask')
 if k=='draem-transfer':
  a=board(10,20,.6,2)+rect(163,79,31,33,'#E99536',O,2)+board(260,20,.6,2,True,True)
  a+=text(15,217,'合成紋理塊',29,O,700)+text(265,217,'真刮傷例',29,B,700)+text(20,290,'位置相近，外觀與形成原因不同',27)
  return a+caption('合成異常不是所有真缺陷','仍須獨立真例驗轉移效果')
 if k=='uni-multiclass':
  a=board(10,20,.39,2)+rect(194,40,100,70,'#4180BD',B,8)+rect(200,130,90,35,'white',L,2)+rect(344,40,122,90,'#EDF0EC','#BCC6C3',5)
  a+=text(15,204,'金屬板',26,B)+text(182,204,'連接器',26,B)+text(352,204,'陶瓷板',26,B)
  a+=arrow(239,230,239,265)+pill(45,277,400,'各類正常 → 共用重建模型')
  return a+caption('原主線三種產品的簡化示意','正常共同訓練，驗收仍按產品')
 if k=='uni-training':
  a=pill(15,18,470,'正常影像 → 固定骨幹特徵')+arrow(250,82,250,112)+vecbox(10,138,'訓練输入','受擾動特徵',O)+vecbox(264,138,'重建目標','原正常特徵',G)
  a+=arrow(239,229,239,262)+pill(65,277,380,'更新重建部分與query',G)
  return a+caption('擾動特徵練習還原正常表示','骨幹固定；不是重畫原圖')
 if k=='uni-eval':
  a=board(10,15,.49,2,True,True)+arrow(192,72,238,72)+grid(4,269,15,133,mark=(2,3))
  a+=text(15,215,'eval：使用原特徵',33,B,700)+text(15,273,'不加訓練用的特徵擾動',29,O)
  return a+caption('同位置原表示與重建表示比較','保存鄰域、query與模型版本')
 if k=='uni-validation':
  a=text(15,42,'按產品逐列保留驗證',31,B,700)
  for i,name in enumerate(['金屬板','連接器','陶瓷板']):
   y=82+74*i;a+=rect(15,y,465,57,'white',L,5)+text(27,y+37,name,29,B,700)+text(175,y+37,'誤報 / 漏檢 / 覆核',27)
  return a+caption('單一平均值可能掩蓋弱類別','每種正常變化與真缺陷都要驗')
 if k=='uni-shortcut':
  a=vecbox(10,28,'原特徵','[.6, .8]',O)+vecbox(264,28,'若重建相同','[.6, .8]',G)
  a+=text(45,173,'相同捷徑 → 距離0',34,R,700)+board(142,205,.5,2,True,True)
  return a+caption('重建相同，刮傷仍可在原圖','作者給定反例，不是模型結果')
 raise ValueError(k)

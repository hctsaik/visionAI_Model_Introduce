"""Concrete authored engineering scenes; source-derived concepts, no model runs."""
from render import rect,text,line,arrow,circle,group,pill,B,N,G,O,L,PALE
from batch3_graphics import grid,caption
from batch7_graphics import panel,gripper,strip,vals,edge,graph_profile
R='#C6473D'

def contract(lines,cap,sub):
 a=rect(30,10,430,282,'white',L,9)
 for i,(label,value) in enumerate(lines):
  yy=48+i*78;a+=text(48,yy,label,24,B,700)+text(48,yy+34,value,27,N)
 return a+caption(cap,sub)

def failed_grip(x=20,y=20,s=1):
 # The same gripper closes above the block: contact never occurs.
 a=gripper(0,0,1,2)+rect(0,40,220,135,'#E4EBF1','none',0)+rect(72,117,76,44,'url(#steel)','#73899E',2)
 a+=line(84,34,84,93,N,13)+line(136,34,136,93,N,13)+line(84,93,96,93,N,9)+line(136,93,124,93,N,9)
 return group(x,y,s,a)

def data_pair(style='top',defect=1):
 return panel(20,20,.55,style=style,defect=defect,mask=True)+panel(280,20,.55,style=style)+text(20,204,'訓練／參考來源',26,B)+text(280,204,'真實留出另存',26,G)

def pass_fail(style='top',defect=1):
 return panel(20,20,.55,style=style)+panel(280,20,.55,style=style,defect=defect)+text(20,205,'正常：驗誤報',27,B)+text(280,205,'缺陷：驗漏檢',27,O)+text(20,280,'真實留出，按件與批次分開',28,G,700)

def shifted_panel(x=20,y=20,s=.9,filled=False):
 a=panel(0,0,1)
 if filled:a+=circle(65,47,27,'#BDCBD6','#BDCBD6')
 else:a+=circle(65,47,35,O,'none')
 return group(x,y,s,a)

def graphic(k):
 if k=='video-labels':return gripper(20,20,.82,2)+failed_grip(270,20,.82)+text(20,204,'接觸並夾住',27,G)+text(270,204,'閉合但未碰到',27,O)+text(20,276,'標註整段：成功／失敗',29,B,700)+caption('兩種結果都要有標註影片','相鄰影格不能跨訓練與驗證')
 if k=='conv-head':return strip()+pill(20,198,170,'ConvLSTM')+arrow(205,221,248,221)+grid(3,265,184,70)+arrow(345,221,385,221)+text(394,212,'任務',25,G,700)+text(394,247,'頭',25,G,700)+caption('H為時序表示，頭給任務輸出','表示本身不是成功／失敗標籤')
 if k=='video-validation':return gripper(20,20,.75,2)+failed_grip(295,20,.75)+text(20,201,'成功誤判？',28,B)+text(285,201,'失敗漏判？',28,O)+text(20,271,'以完整片段統計＋端到端時間',27,G,700)+caption('按片段、工件或批次留出','不要把連續相似幀當獨立測試')
 if k=='video-timing':return strip()+line(50,198,440,198,B,3)+''.join(line(50+i*130,185,50+i*130,212,B,3)+text(50+i*130,251,['0','Δt','2Δt','3Δt'][i],29,N,400,'middle') for i in range(4))+caption('保存片長、幀距、裁切與縮放','同樣幀數，不代表同樣時間長度')
 if k=='conv-reset':return pill(20,20,190,'影片A：H/C')+arrow(220,42,271,42)+pill(280,20,190,'A下一段')+line(30,110,460,110,L,2)+pill(20,146,190,'切換影片B',G)+arrow(220,168,269,168,G)+pill(280,146,190,'初始狀態',G)+text(20,279,'重設規則要與訓練方式一致',28)+caption('同片續接，換片明確重設','不把A的狀態當B的歷史')
 if k=='conv-contract':return contract([('時間與空間','幀距／解析度／裁切'),('配套權重','ConvLSTM＋任務頭'),('執行狀態','初始化／續接／重設')],'模型與狀態策略一起交付','總延遲含取像、前處理及讀出')
 if k=='video-missed':return gripper(20,20,.64,0)+failed_grip(180,20,.64)+gripper(340,20,.64,2)+rect(170,9,152,137,'none',O,4)+text(20,207,'抽樣A',28,B)+text(183,207,'未取到',28,O)+text(348,207,'抽樣B',28,B)+arrow(55,254,432,254)+caption('短事件發生在兩次取樣之間','模型未看到的事件不能靠記憶補證')
 if k=='conv-decay':return vals([1,.5,.25,.125],20,35,115)+''.join(arrow(90+i*115,127,147+i*115,127) for i in range(3))+text(20,213,'每步乘0.5；不加入新值',29)+text(20,278,'三步後：1 × 0.5³ = 0.125',30,G,700)+caption('作者單格例：舊訊號可衰減','真實忘記門是學到的變動值')
 if k=='mae-pretrain':return gripper(20,20,.8,1)+rect(50,68,60,60,'#9BABB9','white',1)+arrow(215,89,271,89)+pill(285,67,180,'重建預訓練')+text(20,226,'目標：被遮住的原像素',30,B,700)+caption('原影片提供自監督訊號','此時沒有教夾取成功的標籤')
 if k=='video-head':return gripper(20,20,.8,2)+text(20,201,'影片標籤：成功',28,G)+arrow(215,82,268,82)+pill(285,60,180,'表示＋任務頭')+text(20,275,'固定骨幹／微調：模式需寫明',27)+caption('標註任務教最後判斷','目標與輸出定義必須一致')
 if k=='video-delivery':return failed_grip(20,20,.85)+arrow(224,90,272,90)+pill(290,69,180,'任務輸出')+text(270,186,'示意：失敗',29,O,700)+text(20,276,'保留片段與時間 → 人員覆核',27)+caption('類別是下游頭的輸出','非本輪真實影片推論結果')
 if k=='video-token-cost':return rect(20,30,200,65,PALE,B,6)+text(120,73,'100 tokens',29,B,700,'middle')+rect(20,140,400,65,PALE,G,6)+text(220,183,'200 tokens',29,G,700,'middle')+text(20,277,'全注意力配對數隨N平方成長',28)+caption('N平方：1萬對4萬配對項','是計算量尺度，不是實測毫秒')
 if k=='video-failure':return gripper(20,20,.82,2)+failed_grip(270,20,.82)+text(20,211,'夾住',29,G)+text(270,211,'未接觸',29,O)+text(20,278,'背景相同，關鍵只在夾爪間隙',27)+caption('局部動作小，但任務結果不同','不能只看全畫面重建相似度')
 if k=='mae-error-average':return grid(10,20,20,190,mark=(5,5))+text(235,62,'99格：平方差0',25,B)+text(235,124,'1格：平方差100',25,O)+text(20,262,'總平方差100 ÷ 100格 = 1',29,G,700)+caption('作者例：平均可掩關鍵局部','重建差不等於事件分類正確率')
 if k=='jepa-pretrain':return gripper(20,20,.8,1)+rect(50,68,60,60,'#9BABB9','white',1)+arrow(215,88,267,88)+grid(3,292,40,100,col=G)+text(270,188,'目標特徵',29,G)+text(20,278,'同遮蔽位置，預測表示',29,B,700)+caption('不是重建可見像素的預訓練','完整影片只為目標支路提供內容')
 if k=='jepa-contract':return contract([('原版骨幹','2024 V-JEPA checkpoint'),('下游模式','固定骨幹＋讀出，或另微調'),('部署輸出','影片表示 → 已訓練任務頭')],'EMA屬預訓練目標更新','不是每段現場影片自動再訓練')
 if k=='compare-pixel':return gripper(20,20,.72,1)+rect(57,85,51,36,'none',O,1)+vals([20,22],270,40,95)+text(250,171,'原值／重建值',27)+text(20,268,'像素平方差：(20−22)² = 4',28,B,700)+caption('VideoMAE：重建像素作監督','作者单像素例，非模型實測')
 if k=='compare-feature':return vals([.2,.8],20,30,95)+vals([.4,.7],270,30,95,col=G)+text(20,175,'特徵L1平均差 = 0.15',32,G,700)+text(20,273,'與像素平方差的單位不同',29)+caption('V-JEPA：同位置目標表示','不能用0.15與4排名模型好壞')
 if k=='fill-dataset':return data_pair()+caption('真刮傷與mask配對，底圖另存','參考用過的工件不再算獨立測試')
 if k=='fill-handoff':return panel(20,20,.7,defect=1,mask=True)+text(310,73,'位置',29,G)+text(310,127,'材質',29,G)+text(310,181,'孔位',29,G)+arrow(170,209,170,245)+pill(25,260,430,'合成圖＋核對後標註 → 訓練')+caption('來源、遮罩與版本一起保存','效益交真實留出集檢驗')
 if k=='fill-contract':return contract([('生成來源','底圖／缺陷例／mask'),('適配模型','基模＋LoRA／文字'),('候選挑選','種子／步數／LFS設定')],'每張合成圖可追溯到條件','不能只保存挑選後的漂亮圖')
 if k=='generation-cost':return ''.join(rect(30+i*110,30,85,100,PALE,B,6)+text(72+i*110,91,str(i+1),32,B,700,'middle') for i in range(4))+text(20,199,'4候選 × 每張20步',33)+text(20,273,'= 80次去噪呼叫',35,G,700)+caption('作者算例，未含挑選與前處理','總時間還要實測，非80毫秒')
 if k=='fill-validation':return pass_fail()+caption('比較加合成前後的真實錯誤','不能用合成圖本身證明資料效益')
 if k=='fill-artifact':return panel(20,20,.9,mask=True)+rect(145,167,62,37,'#19252F',O,4)+text(20,283,'不合理黑塊也會增加局部差異',27,O,700)+caption('同位置，但外觀不是可信刮傷','距離較大不自動代表更好候選')
 if k=='ano-dataset':return data_pair('ano',2)+caption('外觀與兩區遮罩一一核對','原板上方兩孔，缺陷在下方')
 if k=='ano-pair-check':return panel(20,20,.85,style='ano',defect=2,mask=True)+text(355,97,'大區',27,G)+text(355,168,'小區',27,G)+text(20,283,'兩區各驗：位置、範圍、孔位',27)+caption('逐區對應後才可用標註','整圖平均不能掩蓋小區漏生成')
 if k=='ano-contract':return contract([('外觀','異常embedding＋基模'),('位置','mask編碼器＋原遮罩'),('採樣','AAR／背景融合／種子步數')],'條件與生成模型一起版本化','大小區域分別保存覆蓋證據')
 if k=='ano-two-masks':return panel(20,20,.9,style='ano',mask=True)+text(20,285,'指定兩區 ≠ 已觀測到兩傷',30,B,700)+caption('大左下、小右下是生成条件','必須回頭看實際產出的影像')
 if k=='ano-one-defect':return panel(20,20,.9,style='ano',defect=1,mask=True)+circle(272,187,32,O,'none')+text(20,285,'右側只有mask，沒有刮傷',29,O,700)+caption('若保留雙傷標註，就會錯標','本圖為作者失敗示意')
 if k=='ano-reject':return panel(20,20,.58,style='ano',defect=1,mask=True)+line(256,38,449,162,R,6)+line(449,38,256,162,R,6)+text(20,229,'剔除，或按可見傷修正標註',29,R,700)+caption('修正後仍要驗證真實資料效益','自適應引導不是免審保證')
 if k=='tf-delivery':return panel(20,20,.86,style='mid',defect=2,mask=True)+text(350,91,'孔位',28,G)+text(350,159,'紋理',28,G)+text(20,282,'圖／mask／參考／設定一起留存',26)+caption('兩處刮傷與目標材質逐一比','合成結果不能直接當物理真值')
 if k=='tf-fixed':return rect(30,25,410,114,'white',G,7)+text(235,89,'預訓練權重 W 固定',33,G,700,'middle')+vals(['z(t)','z(next)'],40,210,190)+arrow(192,175,311,175)+caption('改變的是生成中的latent','有梯度不代表有權重optimizer')
 if k=='tf-autograd-cost':return pill(20,20,440,'latent → 特徵 → 差異')+arrow(390,86,390,139,O)+pill(20,160,440,'差異梯度 → latent引導',O)+text(20,281,'保存中間激活，增加計算與記憶體',26)+caption('採樣成本含前向與求導','不能以免訓練推論為必定更快')
 if k=='tf-contract':return contract([('每次來源','正常圖／參考傷／mask'),('引導','特徵對齊與梯度設定'),('保持與採樣','AdaIN／融合／步數種子')],'每個生成條件都可影響结果','端到端時間包含求導與融合')
 if k=='tf-material':
  a=panel(20,20,.55,style='mid')+rect(280,20,195,132,'#BD956A','#795836',4)
  for i in range(6):a+=f'<path d="M 285,{35+i*18} q 70,25 185,-4" fill="none" stroke="#805731" stroke-width="3"/>'
  return a+line(335,122,425,57,'#30281F',5)+text(20,209,'目標：金屬板',27,B)+text(280,209,'參考：木紋傷',27,O)+caption('材質不同，參考可能帶偏','位置相合不代表局部紋理合理')
 if k=='tf-contamination':
  a=panel(20,20,.9,style='mid',mask=True)+rect(74,181,90,28,'#BD956A','#795836',1)
  for i in range(4):a+=line(77,186+i*5,161,183+i*5,'#805731',2)
  return a+text(20,286,'金屬板局部出現木紋',31,O,700)+caption('作者反例：局部對齊不等於物理真實','背景保持仍需驗mask內材質')
 if k=='control-contract':return contract([('基模與分支','匹配的ControlNet版本'),('控制圖','輪廓前處理／解析度'),('採樣','文字／強度／起止步／種子')],'輪廓和控制模型需匹配','只換文字不代表條件仍相容')
 if k=='control-overlay':return panel(20,20,.9)+rect(20,20,324,216,'none',G,8)+circle(78.5,62.3,21.6,G,'none')+circle(285.5,62.3,21.6,G,'none')+text(20,288,'綠線：原條件；底圖：生成候選',26,G,700)+caption('外框與兩孔逐一疊合核對','輪廓相符仍不是實際尺寸證據')
 if k=='control-strength':return pill(20,20,440,'分支殘差 r')+arrow(100,81,100,143)+arrow(370,81,370,143,G)+pill(20,161,190,'0.5 × r')+pill(280,161,190,'1.0 × r',G)+text(20,285,'給定權重示例，不是建議參數',28)+caption('注入量不同，輸出需同條件驗','強度大不保證細節更真實')
 if k=='control-two-surfaces':return panel(20,20,.55)+panel(280,20,.55,defect=1)+text(20,209,'無傷候選',28,B)+text(280,209,'有傷候選',28,O)+text(20,279,'兩者外框與孔位完全一樣',29)+caption('表面刮傷不在這張輪廓條件內','輪廓符合不能證明傷是真實的')
 if k=='control-real-check':return panel(20,20,.55,defect=1)+panel(280,20,.55)+text(20,205,'生成刮傷',28,O)+text(280,205,'原始觀測',28,G)+text(20,278,'同位置回比，缺乏觀測就待確認',26)+caption('生成可用於創作或資料候選','現場缺陷判定須原始觀測證據')
 if k=='paint-contract':return contract([('原始來源','原圖另存＋尺寸座標'),('遮罩約定','本圖1=修改；API另核對'),('生成設定','縮放／羽化／模型／種子')],'原圖、mask與候選一起保存','不要讓編修版覆蓋原始觀測')
 if k=='paint-tight':return panel(20,20,.9,style='paint',defect=1)+rect(170,182,21,17,'#CE791744',O,0)+text(20,288,'遮罩太小，污點邊緣在範圍外',27,O,700)+caption('若只改小內區，外圈可能殘留','依原始污點邊界檢查修改範圍')
 if k=='paint-wide':return panel(20,20,.9,style='paint',defect=1)+rect(45,45,265,175,'#CE791733',O,5)+text(20,288,'過大遮罩包含了部分孔位',29,O,700)+caption('修改範圍擴大，也會暴露鄰近結構','邊界、孔位及遮罩外都要比')
 if k=='paint-real-hole':return shifted_panel()+text(20,287,'左上真孔被指定為可編修區',28,O,700)+caption('橘圈是要改的影像區域','原板同時仍有右上孔')
 if k=='paint-filled-hole':return shifted_panel(filled=True)+text(20,287,'候選照片：左孔像素被填平',28,G,700)+caption('只改影像，右孔保持原位置','照片中不見孔，不代表補了材料')
 if k=='paint-recapture':return shifted_panel()+text(20,287,'重新取像：同一真孔仍存在',29,B,700)+caption('沒有物理修補，孔仍在實物上','編修照片不可作修復驗收證據')
 if k=='restore-delivery':return panel(20,20,.5,style='mid')+arrow(212,83,270,83)+panel(280,20,.5,style='mid',noise=True)+text(20,205,'候選套回A',28,B)+text(280,205,'回比原觀測',27,G)+text(20,280,'依噪聲模型檢查殘差是否合理',28)+caption('資料一致性之外，再驗獨立成像','不假設已知這張原圖的真實噪聲')
 if k=='restore-contract':return contract([('觀測','原圖 y／取像條件'),('退化假設','算子 A／雜訊 n'),('候選生成','模型／步數／種子／融合')],'退化假設需要有取像依據','示意公式不代替實際退化辨識')
 if k=='restore-multiple':return panel(20,20,.55,style='mid')+panel(280,20,.55,style='mid',defect=1,faint=True)+text(20,208,'候選A',29,B)+text(280,208,'候選B',29,G)+text(20,280,'低解析觀測可能無法辨別細節',28)+caption('候選不同，不能自行指定一個為真值','需額外觀測或任務驗證')
 if k=='restore-wrong-a':return panel(20,20,.52,style='mid',noise=True)+arrow(218,85,273,85,O)+panel(280,20,.52,style='mid')+line(451,22,451,143,'white',4)+line(458,22,458,143,N,4)+line(464,22,464,143,'white',2)+text(20,207,'實際：加性雜訊',26,B)+text(270,207,'誤用去模糊',27,O)+caption('同板右外框出現多重邊的反例','漂亮或銳利並不證明模型合適')
 if k=='blur-source':return edge(20,20,1.55,blur=True)+text(340,71,'曝光',28,B)+text(340,127,'運動',28,B)+text(340,183,'對焦',28,B)+text(20,288,'原始模糊邊另存，取像設定同留',26)+caption('先辨識模糊來源與空間變化','單一直邊只是局部教學示意')
 if k=='blur-contract':return contract([('原觀測','解析度／曝光／運動／對焦'),('復原模型','訓練退化與checkpoint'),('比較方式','同位置清晰參考＋邊緣誤差')],'模型與實際退化條件需對應','不只比重建圖的視覺銳利度')
 if k=='blur-position':return edge(20,20,1.55)+line(167,10,167,253,G,4)+line(188,10,188,253,O,4)+text(330,80,'真邊100',26,G)+text(330,143,'估計102',26,O)+text(330,206,'差2像素',26,O)+text(20,294,'給定：102 − 100 = 2像素',28)+caption('同座標比位置，不能只比斜率','示意像素未校正，不是毫米')
 if k=='blur-validation':return edge(20,20,ring=True)+edge(280,20)+text(20,201,'假邊／偏移',28,O)+text(280,201,'獨立清晰圖',27,G)+text(20,278,'同硬體：總延遲＋邊緣誤差',28)+caption('取像、傳輸與前後處理一起計時','快或清晰都不能單獨代表可量測')
 if k=='blur-ringing':return edge(20,20,1.55,ring=True)+text(340,67,'多峰',29,O)+arrow(353,83,210,83,O)+text(20,282,'選中假峰，邊緣座標就會偏',29,O,700)+caption('增添高頻不等於恢复真實輪廓','振鈴可能使量測選錯邊')
 if k=='sr-contract':return contract([('原觀測','低解析影像＋取像條件'),('放大設定','輸入尺寸／倍率／退化假設'),('輸出候選','模型版本／另存生成影像')],'保留同板同q的來源關係','輸出像素不可冒充新增觀測')
 if k=='sr-pixel-cost':return grid(4,20,30,100)+arrow(142,80,217,80)+grid(8,250,30,200,col=G)+text(20,259,'100×100',28,B)+text(270,259,'200×200',28,G)+caption('寬高各兩倍：1萬變4萬像素','是輸出量，不保證延遲正好四倍')
 if k=='sr-real-check':return panel(20,20,.75,style='sr')+rect(72,78,32,32,'none',O,0)+arrow(115,94,337,102,O)+grid(6,350,45,115,col=G)+text(20,275,'右側需要真實高解析重新取像',27,G,700)+caption('同q比較細節與下游錯誤','插值與生成都不能自證真實細節')
 raise ValueError('Unimplemented scene: '+k)

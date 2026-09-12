"""Task, deployment and counterexample scenes; all numbers are authored examples."""
from render import rect,text,line,arrow,circle,group,pill,B,N,G,O,L
from batch3_graphics import grid,caption
from batch5_graphics import board,vecbox
from batch6_graphics import belt,cells
R='#C6473D'
def contract(lines,video=False):
 a=belt(15,5,.42,130,'L' if video=='byte' else '') if video else board(15,5,.43,2,True,True)
 a+=text(215,68,'固定同一版本',28,B,700)
 for i,t in enumerate(lines):a+=rect(20,128+i*65,440,54,'white',L,3)+text(30,163+i*65,t,26,B)
 return a
def validate():
 return board(10,15,.54,2,True,True)+board(265,15,.54)+text(15,185,'刮傷：驗漏檢',28,O,700)+text(270,185,'正常：驗誤報',28,G,700)+text(30,274,'獨立留出集＋原圖覆核',29,B,700)
def graphic(k):
 if k=='win-holdout':
  return board(15,15,.52)+board(270,15,.52,2,True,True)+text(15,177,'正常：獨立驗證',27,G,700)+text(267,177,'缺陷：獨立驗證',27,O,700)+text(30,266,'零樣本：目標不參與訓練',28,B,700)+caption('先用人工文字與固定CLIP','留出資料用來查誤報與漏檢')
 if k=='fd-bg-compare':
  return belt(15,15,.49,None)+belt(255,15,.49,130)+text(50,125,'累積背景',26,B,700)+text(282,125,'目前有方件',26,O,700)+arrow(105,140,170,172)+arrow(370,140,290,172)+belt(55,182,.8,130,mask=True)+caption('同停留位置，相對舊背景比較','背景尚未吸收此物件的示意')
 if k=='ad-scratch':return board(30,15,1.1,2,True,True)+caption('同一金屬板，大小孔與刮傷p','同件任務；位置不偷換')
 if k=='ad-split':
  return board(15,15,.52)+board(270,15,.52,2,True,True)+text(15,177,'確認正常：訓練',27,G,700)+text(267,177,'獨立留出：驗證',27,O,700)+text(30,266,'正常與真缺陷分開保存',29,B,700)+caption('待測影像不回灌作正常','驗證保留正常變化與真缺陷')
 if k=='ad-delivery':
  return grid(4,20,50,150,mark=(2,3))+arrow(188,128,235,128)+board(260,45,.57,2,True,True)+text(20,274,'位置圖＋原圖＋影像分數',29,B,700)+caption('分數供回查原位置p','允收規則與尺寸判定另外定義')
 if k=='ad-validate':return validate()+caption('位置分數回原圖逐件檢查','獨立正常與真缺陷不可省略')
 if k=='dino-data':
  a=board(10,15,.4)+rect(190,25,105,75,'#4385B8',B,5)+rect(345,25,110,75,'#ECF0EB','#AEBBBB',3)
  a+=text(10,147,'金屬板',25,B,700)+text(187,147,'連接器',25,B,700)+text(340,147,'陶瓷板',25,B,700)+arrow(235,180,235,220)+pill(30,250,420,'多類正常 → 共用模型')
  return a+caption('三種產品只收確認正常','產品切分保留獨立驗證')
 if k=='dino-train':
  return board(15,15,.43)+arrow(180,66,220,66)+pill(230,42,230,'固定DINOv2')+arrow(330,98,330,136)+pill(20,160,440,'可訓練MLP＋線性注意力解碼')+text(35,274,'原正常特徵 → 重建目標',29,G,700)+caption('更新重建部分，不更新骨幹','分組比較与難位置訓練配套')
 if k=='dino-contract':return contract(['骨幹＋MLP＋解碼器','取用層／分組／前處理','eval／評分／門檻'])+caption('分組和權重共同版本化','改分組也須重驗留出資料')
 if k=='class-validation':
  a=text(25,43,'每個產品獨立留出',30,B,700)
  for i,t in enumerate(['金屬板','連接器','陶瓷板']):a+=rect(20,80+i*75,440,58,'white',L,3)+text(30,118+i*75,t,26,B,700)+text(170,118+i*75,'誤報／漏檢／覆核',25)
  return a+caption('單一平均值可能掩蓋弱類','正常變化與真缺陷都要驗')
 if k=='dino-copy':
  return vecbox(15,30,'原特徵','[.6, .8]',B)+vecbox(250,30,'若重建相同','[.6, .8]',G)+text(50,182,'餘弦差 = 0',35,O,700)+board(145,220,.42,2,True,True)+caption('表示相同，原圖仍有刮傷','给定反例；非模型推論結果')
 if k=='inv-train':
  return board(15,15,.42)+arrow(180,65,215,65)+grid(4,235,15,110)+text(20,177,'正常特徵 → 空間條件',29,B,700)+arrow(235,195,235,230)+pill(20,255,440,'常數特徵 → SSM重建')+caption('固定編碼器，學條件和重建','正常特徵作MSE重建目標')
 if k=='inv-contract':return contract(['編碼器／尺度融合','SSM／解碼器／標準化','前處理／餘弦差／門檻'])+caption('空間條件保留每位置','SSM指空間風格調制')
 if k=='inv-average':
  return text(20,43,'若把p、q條件平均',30,B,700)+vecbox(15,85,'縮放平均','(2 + .5)/2 = 1.25',O)+vecbox(250,85,'偏移平均','(1 + 0)/2 = .5',G)+text(25,229,'1.25 × 3 + .5 = 4.25',31,O,700)+text(25,296,'p、q得到同一個值',30,B,700)+caption('原本7／1.5的區別消失','给定局部算例，不預測性能')
 if k=='dd-train':
  return board(145,5,.5)+arrow(220,133,130,172)+arrow(265,133,365,172)+vecbox(15,190,'正常影像','教去噪模型',B)+vecbox(250,190,'正常特徵','教適配比較',G)+caption('兩部分依正常資料準備','測試原圖持續引導恢復')
 if k=='dd-contract':return contract(['採樣步數／引導／隨機種子','去噪模型／適配特徵','兩路權重／前處理／門檻'])+caption('恢復估計和評分一併保存','同張圖可受採樣設定影響')
 if k=='dd-cost':
  return text(25,40,'給定：每步去噪4ms',31,B,700)+vecbox(15,87,'20步','20 × 4 = 80ms',B)+vecbox(250,87,'50步','50 × 4 = 200ms',O)+rect(25,205,160,34,B,'none',0)+rect(25,255,400,34,O,'none',0)+caption('只是去噪呼叫的時間算例','另計前後處理與特徵比較')
 if k=='dd-copy':
  return board(10,10,.55,2,True,True)+board(267,10,.55,2,True,True)+text(30,184,'原p = 40',30,O,700)+text(280,184,'R的p = 40',30,G,700)+text(55,281,'|40 − 40| = 0',37,R,700)+caption('若刮傷被保留，像素差可為0','特徵路徑能否補足須驗證')
 if k=='win-task':
  return board(20,10,.6,2,True,True)+rect(160,55,72,72,'none',B,0)+vecbox(255,40,'人工文字','正常／異常',G)+arrow(160,181,230,227)+arrow(355,151,280,227)+pill(20,260,440,'局部視窗表示比兩種狀態')+caption('固定CLIP，文字與影像配對','目標零樣本仍須目標驗證')
 if k=='win-contract':return contract(['CLIP／人工提示句型','視窗尺度／調和聚合','前處理／參考模式／門檻'])+caption('先明列是否使用正常參考','分數尺度不當作缺陷機率')
 if k=='win-reference':
  return board(15,20,.45)+board(255,20,.45)+text(35,167,'正常參考1',26,G,700)+text(276,167,'正常參考2',26,G,700)+arrow(125,187,205,225)+arrow(345,187,275,225)+pill(30,250,420,'WinCLIP+：另加視覺比對')+caption('参考只收確認正常的影像','與原文字線索互補整合')
 if k=='clip-pair':
  return board(15,25,.54)+board(265,25,.54,2,True,True)+circle(52,60,23,'#E8C56B','none')+text(84,71,'q',26,O,700)+text(20,195,'正常N：孔口反光q',25,G,700)+text(270,195,'異常A：細刮傷p',25,O,700)+caption('同板身份與允收定義固定','只比較正常變化與真缺陷')
 if k=='clip-errors':
  return board(15,15,.54)+board(265,15,.54,2,True,True)+circle(52,50,23,O,'none')+text(84,58,'q',25,O,700)+text(15,183,'若q判異常：誤報',25,R,700)+text(268,183,'若p判正常：漏檢',25,R,700)+text(30,280,'固定取像＋獨立真值查核',29,B,700)+caption('位置回到可見影像查原因','作者反例，不是模型分數')
 if k=='clip-compare':
  return validate()+caption('相同留出集，比兩種提示來源','同時記錄覆核量與漏檢代價')
 if k=='ac-provenance':
  return rect(15,30,150,88,'#4385B8',B,4)+text(17,163,'輔助資料',28,B,700)+arrow(182,74,222,74)+pill(230,48,230,'已學提示')+board(155,216,.43,2,True,True)+text(15,202,'目標板未參與學習',28,O,700)+caption('學習來源與目標資料分開','零樣本是對目標類別而言')
 if k=='ac-contract':return contract(['輔助資料／切分／提示權重','固定CLIP／DPAM','影像解析度／評分／門檻'])+caption('提示來源可追溯，權重要匹配','改提示或解析度後重新驗證')
 if k=='fd-threshold':
  return text(25,38,'給定絕對差',29,B,700)+cells([0,80,0,0,80],65,O)+text(25,171,'給定門檻30：差 > 30',29,B,700)+cells([0,1,0,0,1],204,G)+caption('80超過30，0不超過30','教學門檻，並非部署建議值')
 if k=='fd-contract':return contract(['前後幀時間／固定相機','曝光／ROI／灰階處理','差分門檻／後處理'],True)+caption('幀距影響移動距離與雙帶','保存時間順序以便追查')
 if k=='fd-flash':
  return belt(20,15,.85,130)+belt(20,175,.85,130,flash=True)+text(330,55,'前',28,'white',700)+text(330,215,'後',28,N,700)+caption('方件不動，曝光升高也有差','全畫面亮起可能只是光照變化')
 if k=='fd-still':
  return belt(20,15,.85,130)+belt(20,175,.85,130)+text(330,55,'前',28,'white',700)+text(330,215,'後',28,'white',700)+caption('同方件停住，兩幀位置相同','相鄰差分會失去靜止物件')
 if k=='fd-zero':
  return text(25,42,'同位置前後值相同',30,B,700)+cells([20,100,100,100,20],65)+cells([20,100,100,100,20],145,G)+text(25,261,'差 = [0, 0, 0, 0, 0]',30,O,700)+caption('全零差分不代表現場空無一物','靜止物件仍在原影格')
 if k=='bg-delivery':
  return belt(20,15,.95,160,mask=True)+arrow(235,190,235,230)+pill(20,255,440,'後段：區域處理／偵測／追蹤')+caption('前景mask沒有類別或永久ID','陰影與雜訊要按任務處理')
 if k=='bg-warmup':
  return belt(20,15,.95,130)+text(25,212,'相機啟動／移位／切換場景',28,O,700)+text(25,282,'重建背景，驗穩定後再用',28,B,700)+caption('背景未穩定時前景可能亂跳','啟動策略不能只看單張圖')
 if k=='bg-rate':
  return vecbox(15,30,'較快更新','適應變化較快',B)+vecbox(250,30,'較慢更新','保留歷史較久',G)+belt(110,148,.55,130)+text(15,282,'停留吸收 ↔ 光照殘留',30,O,700)+caption('快慢都有代價，要用同段影片驗','不指定通用最佳learningRate')
 if k=='bg-contract':return contract(['history／learningRate','陰影標籤／ROI／前處理','場景切換／背景重置'],True)+caption('背景狀態依賴前段影格','同參數但不同歷史，結果可不同')
 if k=='bg-track':
  return belt(20,15,.95,160)+rect(169,50,87,89,'none',G,0)+text(285,97,'ID7',30,G,700)+text(25,234,'物件身份另存於追蹤狀態',29,B,700)+text(25,295,'長遮擋仍需處理丟失',28,O,700)+caption('前景變空不等於可刪除實物記錄','偵測與追蹤也需要驗證')
 if k=='byte-count':
  return belt(20,20,.95,250,'L')+line(240,20,240,177,O,4)+arrow(167,115,287,115,G)+text(250,220,'ID7已跨線',29,G,700)+text(25,290,'下游記錄：ID7／方向／時間',26,B,700)+caption('跨線事件需另定重複政策','框或ID數量不直接等於通過件數')
 if k=='byte-contract':return contract(['偵測器／分數與匹配門檻','有效幀率／丟失緩衝','計數線／方向／重複規則'],'byte')+caption('場景切換時重置不相關軌跡','按完整影片驗證斷軌與誤計數')
 if k=='byte-buffer':
  return text(25,42,'給定有效緩衝：30幀',30,B,700)+vecbox(15,90,'30fps','30 / 30 = 1秒',B)+vecbox(250,90,'10fps','30 / 10 = 3秒',O)+text(25,256,'核對實作是否按fps縮放',29,B,700)+caption('相同幀數不等於相同秒數','示意有效幀數，不套用預設參數')
 if k=='byte-switch':
  return belt(20,20,.9,130,'L')+text(25,215,'ID7 → 遮擋超期 → 新ID12',27,O,700)+text(25,284,'同物件可能被誤當第二件',29,R,700)+caption('同L標記物件仍可能換ID','需用完整影片查重複计數')
 if k=='byte-isolated':
  return belt(20,20,.9,None)+rect(260,64,85,85,'none',O,0)+text(275,110,'.3',28,O,700)+text(25,225,'附近沒有可接的活動軌跡',28,B,700)+text(25,285,'孤立低分 → 不直接建ID',28,O,700)+caption('此框是偵測器誤框的給定例','低分再匹配不是全收低分框')
 if k=='byte-new':
  return belt(20,20,.9,250)+rect(240,50,85,85,'none',B,0)+text(25,225,'未配對高分框 → 新候選',28,B,700)+text(25,285,'依實作確認與後續續接',28,G,700)+caption('高分也不等於一定是真物件','繼續核對偵測與身份穩定性')
 raise ValueError(k)

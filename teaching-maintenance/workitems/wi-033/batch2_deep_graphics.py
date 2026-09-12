from batch2_graphics import board,lines
from render import rect,text,line,arrow,circle,group,feature,pill,B,N,G,O,L,PALE

def graphic(k):
 if k=='deep-eff-learn':return board(10,8,.52)+arrow(135,70,187,70)+pill(200,47,270,'T 固定')+arrow(338,99,338,149)+text(358,132,'目標',25)+pill(200,166,270,'學生 / AE 學習',G)+lines('同影像分別送三者，T提供目標','學生兩組輸出共享前層','不同目標，下一段分開比較',y=287)
 if k=='deep-board-input':return board(142,4,1.05,False,True)+lines('A-01：四孔與下中線痕','同一工件贯穿本章，非模型實測')
 if k=='deep-eff-candidate':return board(10,10,.55)+arrow(145,73,191,73)+pill(210,48,264,'正常訓練')+arrow(340,102,340,158)+pill(210,174,264,'候選模型',G)+lines('另送待測影像，才產生位置圖','不需預先列完所有缺陷類別','可見線痕不保證一定檢出',y=287)
 if k=='deep-board-review':return board(145,4,1.05,False,True)+rect(247,191,43,43,'none',O,2)+lines('位置回原圖，依允收規格覆核','記誤報、漏檢與人工工時','完整時間含取像與前後處理',y=285)
 if k in ['deep-data-train','deep-data-calibrate','deep-data-test']:
  names={'deep-data-train':['確認正常樣本，涵蓋允收變化','用於學生與AE訓練','不是全部未知樣本都已涵蓋'],'deep-data-calibrate':['未參與訓練的正常品','估計local/global分位數尺度','最終測試不可拿來挑校正值'],'deep-data-test':['独立正常與真缺陷一起保留','量誤報、漏檢與覆核負擔','同件近似照片不可跨拆']}
  a=board(20,10,.72)+board(292,10,.72,False,k=='deep-data-test')
  return a+lines(*names[k],y=279)
 if k=='deep-train-local':return board(10,10,.5)+arrow(119,73,167,73)+pill(187,45,280,'教師 T 固定')+arrow(330,98,330,161)+pill(187,180,280,'S1 學 T',G)+lines('同影像進教師與學生','正常特徵回應朝目標接近','學習目標箭頭，非推論串接',y=287)
 if k=='deep-output-location':return board(140,5,1.05,False,True)+rect(241,190,45,43,'#F7C886',O,0)+lines('正常訓練 → 可疑位置線索','幫人找到該看的區域','不直接交付缺陷類別或輪廓',y=290)
 if k=='deep-output-contour':
  a=board(140,5,1.05,False,True)+group(140,5,1.05,'<path d="M103,187 l7,-5 20,28 -7,6 Z" fill="none" stroke="#CE7917" stroke-width="3"/>')
  return a+lines('已定義目標 → 輪廓標註訓練','像素輪廓／面積另做驗證','實體面積還需校正與誤差',y=290)
 if k=='deep-board-glare':return board(142,4,1.05,False,True)+rect(242,193,50,48,'white','none',12)+lines('同一細痕被反光遮住','高門檻可能同时壓掉真缺陷','沒有捏造模型失敗結果',y=287)
 if k=='deep-board-reacquire':return board(15,10,.6,False,True)+arrow(163,103,217,103)+board(255,10,.95,False,True)+lines('調光源、倍率、曝光与檢查範圍','來源與新輸入一併保存','重新驗正常與真缺陷',y=287)
 if k in ['deep-compare-efficient','deep-compare-patchcore','deep-compare-seg']:
  a=board(5,8,.5)+arrow(120,80,176,80)
  options={'deep-compare-efficient':['學生 / AE 適配','正常分位數重校正','位置篩查；更新後重驗','訓練、校正、推論与記憶體'],'deep-compare-patchcore':['特徵 → 正常庫','重抽特徵 / 取代表子集','位置篩查；新庫重驗門檻','建庫、記憶體与每件查詢'],'deep-compare-seg':['輪廓標註 → 適配','已定義目標与獨立測試','工作輸出：像素輪廓','標註、訓練与推論成本']};v=options[k]
  a+=pill(190,55,285,v[0],G)+arrow(331,108,331,164)+rect(180,182,302,91,'white',L,8)+text(190,238,v[1],25,B)
  return a+lines(v[2],v[3],y=335)
 if k=='deep-transfer-area':return board(15,12,.65,False,True)+arrow(165,95,220,95)+pill(231,65,240,'輪廓標註')+arrow(347,120,347,166)+pill(231,181,240,'分割驗證',G)+lines('像素面積不直接等於平方毫米','實體尺度需校正与誤差驗證','資料與驗收隨需求更新',y=287)
 raise ValueError(k)

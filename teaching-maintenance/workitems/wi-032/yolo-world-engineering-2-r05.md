# WI-032 yolo-world-engineering-2 r01
- lesson objective: 保留影像與文字两條來源，才看得懂比對。
- page type: C
- primary reading path: 視覺多尺度特徵 → 視覺語言路徑 → 區域與詞彙打分 → 工作核對與接手
- major visual nodes:
  1. 視覺多尺度特徵
  2. 視覺語言路徑
  3. 區域與詞彙打分
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-21-alignment-to-measurement_v01.png`
- pale-yellow takeaway: #FFF4CC：保留影像與文字两條來源，才看得懂比對。
- generation: 新建精確SVG→PNG，桌機1672×941、手機直向；actual PNG review pending，user approval pending。與首讀PNG分開。
- source: https://arxiv.org/abs/2401.17270
- evidence: RepVL-PAN相关实现涉及图像与文字交互及多尺度特征融合；此图只表达职责，不伪称完整张量架构。region-text相似关系用于类别评分，边框回归另承担位置。

## r02 prototype correction
保持ChArUco同標靶到重投影，不混入金屬工件；相機軸標示與取樣方向分開。原生與頁內pending。
## r03 審查後修正
棋盤交點修正為兩黑兩白；ECC影像座標僅2D，插值用四像素數值示例；SIFT幾何圖避免重複，新增候選外點與8方向；LightGlue修剪移除後續邊，注意力點不共線；DINO位置初始化與decoder更新分開，正負訓練目標不串成時序；YOLO-World矩陣列／欄與文字引導權重有可核對意義。原生與頁內pending，user approval pending。
## r04 最終候選
已依實圖修正對應、2D座標、八方向、正負分支及有標籤矩陣。桌機與手機原生／實頁核對仍需完成。來源：https://arxiv.org/html/2401.17270v3
以論文v3的RepVL-PAN為例，Text-guided CSPLayer把影像／詞彙相似經max與sigmoid形成權重，乘回影像特徵；Image-Pooling Attention另用池化的影像資訊更新文字表示。區域與詞彙相似度用於類別評分，框回歸另負責位置。圖只展開文字引導權重與區域比對，矩陣深淺為示意，不是實際權重輸出。部署版本可能省略或改寫模組，需按官方設定核對。

## r05
文字引導綠箭頭繞右邊，避免穿過max/sigmoid標註。原生／頁內待核對。

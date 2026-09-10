# WI-032 det-dino-detector-engineering-3 r01
- lesson objective: 帶噪查詢是訓練輔助，正式推論不用真值。
- page type: C
- primary reading path: 從真值產生帶噪查詢 → 近正樣本還原目標 → 負樣本學無物件 → 工作核對與接手
- major visual nodes:
  1. 從真值產生帶噪查詢
  2. 近正樣本還原目標
  3. 負樣本學無物件
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-21-alignment-to-measurement_v01.png`
- pale-yellow takeaway: #FFF4CC：帶噪查詢是訓練輔助，正式推論不用真值。
- generation: 新建精確SVG→PNG，桌機1672×941、手機直向；actual PNG review pending，user approval pending。與首讀PNG分開。
- source: https://arxiv.org/abs/2203.03605
- evidence: 正负带噪查询以不同噪声范围构建，正样本学习还原对应GT框/类，负样本学习无物件。噪声示意不是实际采样统计；不能将no-object目标解释为原图里真的没有物件。

## r02 prototype correction
保持ChArUco同標靶到重投影，不混入金屬工件；相機軸標示與取樣方向分開。原生與頁內pending。
## r03 審查後修正
棋盤交點修正為兩黑兩白；ECC影像座標僅2D，插值用四像素數值示例；SIFT幾何圖避免重複，新增候選外點與8方向；LightGlue修剪移除後續邊，注意力點不共線；DINO位置初始化與decoder更新分開，正負訓練目標不串成時序；YOLO-World矩陣列／欄與文字引導權重有可核對意義。原生與頁內pending，user approval pending。
## r04 最終候選
已依實圖修正對應、2D座標、八方向、正負分支及有標籤矩陣。桌機與手機原生／實頁核對仍需完成。來源：https://arxiv.org/abs/2203.03605
正負帶噪查詢以不同噪聲范圍構建，正樣本學習還原對應GT框/類，負樣本學習無物件。噪聲示意不是實際采樣統計；不能將no-object目標解釋為原圖里真的沒有物件。

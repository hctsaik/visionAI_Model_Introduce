# WI-032 sift-engineering-2 r01
- lesson objective: ratio test篩含糊候選，不是幾何真值證明。
- page type: C
- primary reading path: 把梯度放進局部格 → 組成描述向量 → 比較第一與第二候選 → 工作核對與接手
- major visual nodes:
  1. 把梯度放進局部格
  2. 組成描述向量
  3. 比較第一與第二候選
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-21-alignment-to-measurement_v01.png`
- pale-yellow takeaway: #FFF4CC：ratio test篩含糊候選，不是幾何真值證明。
- generation: 新建精確SVG→PNG，桌機1672×941、手機直向；actual PNG review pending，user approval pending。與首讀PNG分開。
- source: https://docs.opencv.org/4.13.0/da/df5/tutorial_py_sift_intro.html
- evidence: 標準SIFT描述子為4×4空間格、每格8方向，共128維；實作含加權、正規化及截斷等步驟。最近與次近描述子距離比可用來篩掉含糊候選，但閾值須用目標資料验证。

## r02 prototype correction
保持ChArUco同標靶到重投影，不混入金屬工件；相機軸標示與取樣方向分開。原生與頁內pending。
## r03 審查後修正
棋盤交點修正為兩黑兩白；ECC影像座標僅2D，插值用四像素數值示例；SIFT幾何圖避免重複，新增候選外點與8方向；LightGlue修剪移除後續邊，注意力點不共線；DINO位置初始化與decoder更新分開，正負訓練目標不串成時序；YOLO-World矩陣列／欄與文字引導權重有可核對意義。原生與頁內pending，user approval pending。
# WI-032 lightglue-engineering-1 r01
- lesson objective: LightGlue不取代找點，也不直接給工站姿態。
- page type: C
- primary reading path: 相容extractor → LightGlue更新配對 → 點對交幾何估計 → 工作核對與接手
- major visual nodes:
  1. 相容extractor
  2. LightGlue更新配對
  3. 點對交幾何估計
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-21-alignment-to-measurement_v01.png`
- pale-yellow takeaway: #FFF4CC：LightGlue不取代找點，也不直接給工站姿態。
- generation: 新建精確SVG→PNG，桌機1672×941、手機直向；actual PNG review pending，user approval pending。與首讀PNG分開。
- source: https://github.com/cvg/LightGlue
- evidence: 官方提供多種extractor相容設定，部署應記錄權重、前處理與影像尺寸。點對與匹配信心不等於幾何準確率，後端求解與工作驗證仍需另行負責。

## r02 prototype correction
保持ChArUco同標靶到重投影，不混入金屬工件；相機軸標示與取樣方向分開。原生與頁內pending。
## r03 審查後修正
棋盤交點修正為兩黑兩白；ECC影像座標僅2D，插值用四像素數值示例；SIFT幾何圖避免重複，新增候選外點與8方向；LightGlue修剪移除後續邊，注意力點不共線；DINO位置初始化與decoder更新分開，正負訓練目標不串成時序；YOLO-World矩陣列／欄與文字引導權重有可核對意義。原生與頁內pending，user approval pending。
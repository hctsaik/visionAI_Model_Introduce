# WI-032 ecc-engineering-1 r01
- lesson objective: 相關值不是缺陷標記，也不是獨立定位誤差。
- page type: C
- primary reading path: 模板與待對圖 → 依外觀做局部更新 → 輸出與核對分開 → 工作核對與接手
- major visual nodes:
  1. 模板與待對圖
  2. 依外觀做局部更新
  3. 輸出與核對分開
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-21-alignment-to-measurement_v01.png`
- pale-yellow takeaway: #FFF4CC：相關值不是缺陷標記，也不是獨立定位誤差。
- generation: 新建精確SVG→PNG，桌機1672×941、手機直向；actual PNG review pending，user approval pending。與首讀PNG分開。
- source: https://docs.opencv.org/4.13.0/dc/d6b/group__video__track.html
- evidence: OpenCV findTransformECC回傳相關值並更新warpMatrix。對齊影像需另行warp，獨立地標殘差與下游檢查也需另外計算；不把概念曲線當真實迭代紀錄。

## r02 prototype correction
保持ChArUco同標靶到重投影，不混入金屬工件；相機軸標示與取樣方向分開。原生與頁內pending。
## r03 審查後修正
棋盤交點修正為兩黑兩白；ECC影像座標僅2D，插值用四像素數值示例；SIFT幾何圖避免重複，新增候選外點與8方向；LightGlue修剪移除後續邊，注意力點不共線；DINO位置初始化與decoder更新分開，正負訓練目標不串成時序；YOLO-World矩陣列／欄與文字引導權重有可核對意義。原生與頁內pending，user approval pending。
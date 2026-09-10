# WI-032 ecc-engineering-2 r01
- lesson objective: 靠密集外觀更新幾何，不靠逐點描述子。
- page type: C
- primary reading path: 目前warp重採樣 → 對比模板強度 → 更新後重新取樣 → 工作核對與接手
- major visual nodes:
  1. 目前warp重採樣
  2. 對比模板強度
  3. 更新後重新取樣
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-21-alignment-to-measurement_v01.png`
- pale-yellow takeaway: #FFF4CC：靠密集外觀更新幾何，不靠逐點描述子。
- generation: 新建精確SVG→PNG，桌機1672×941、手機直向；actual PNG review pending，user approval pending。與首讀PNG分開。
- source: https://docs.opencv.org/4.13.0/dc/d6b/group__video__track.html
- evidence: 同一物件的強度曲線僅用來顯示错位如何影响比较。ECC局部最优化依照当前几何和强度计算参数更新；过远初始位置、遮挡或模型不适用仍可能失败。

## r02 prototype correction
保持ChArUco同標靶到重投影，不混入金屬工件；相機軸標示與取樣方向分開。原生與頁內pending。
## r03 審查後修正
棋盤交點修正為兩黑兩白；ECC影像座標僅2D，插值用四像素數值示例；SIFT幾何圖避免重複，新增候選外點與8方向；LightGlue修剪移除後續邊，注意力點不共線；DINO位置初始化與decoder更新分開，正負訓練目標不串成時序；YOLO-World矩陣列／欄與文字引導權重有可核對意義。原生與頁內pending，user approval pending。
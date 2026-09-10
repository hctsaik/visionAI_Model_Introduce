# WI-032 charuco-engineering-2 r01
- lesson objective: ID解決身份，棋盤角點提供精細影像位置。
- page type: C
- primary reading path: 標記辨認位置 → 棋盤交點供定位 → 同ID連回板座標 → 工作核對與接手
- major visual nodes:
  1. 標記辨認位置
  2. 棋盤交點供定位
  3. 同ID連回板座標
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-21-alignment-to-measurement_v01.png`
- pale-yellow takeaway: #FFF4CC：ID解決身份，棋盤角點提供精細影像位置。
- generation: 新建精確SVG→PNG，桌機1672×941、手機直向；actual PNG review pending，user approval pending。與首讀PNG分開。
- source: https://docs.opencv.org/4.13.0/da/d13/tutorial_aruco_calibration.html
- evidence: 偵測到ArUco標記之後，ChArUco流程估計及細化棋盤交點位置；實際可用角點取決於清晰度、視角、遮擋與設定。不能把marker中心替換成棋盤角點。

## r02 prototype correction
保持ChArUco同標靶到重投影，不混入金屬工件；相機軸標示與取樣方向分開。原生與頁內pending。
## r03 審查後修正
棋盤交點修正為兩黑兩白；ECC影像座標僅2D，插值用四像素數值示例；SIFT幾何圖避免重複，新增候選外點與8方向；LightGlue修剪移除後續邊，注意力點不共線；DINO位置初始化與decoder更新分開，正負訓練目標不串成時序；YOLO-World矩陣列／欄與文字引導權重有可核對意義。原生與頁內pending，user approval pending。
## r04 最終候選
已依實圖修正對應、2D座標、八方向、正負分支及有標籤矩陣。桌機與手機原生／實頁核對仍需完成。來源：https://docs.opencv.org/4.13.0/da/d13/tutorial_aruco_calibration.html
偵測到ArUco標記之後，ChArUco流程估計及細化棋盤交點位置；實際可用角點取決於清晰度、視角、遮擋與設定。不能把marker中心替換成棋盤角點。

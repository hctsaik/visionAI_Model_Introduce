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
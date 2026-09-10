# WI-032 charuco-engineering-4 r01
- lesson objective: 把參數與取像條件綁定，改條件就重新核對。
- page type: D
- primary reading path: 光學與影像條件 → 改條件後重查投影 → 量測另有尺寸基準 → 工作核對與接手
- major visual nodes:
  1. 光學與影像條件
  2. 改條件後重查投影
  3. 量測另有尺寸基準
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-21-alignment-to-measurement_v01.png`
- pale-yellow takeaway: #FFF4CC：把參數與取像條件綁定，改條件就重新核對。
- generation: 新建精確SVG→PNG，桌機1672×941、手機直向；actual PNG review pending，user approval pending。與首讀PNG分開。
- source: https://docs.opencv.org/4.13.0/da/d13/tutorial_aruco_calibration.html
- evidence: 更換鏡頭、對焦或解析度後應重新確認參數適用性；已知縮放／裁切可換算像素內參但仍需驗證。毫米準確還涉及外參、工作平面、標靶真實尺寸和誤差預算。

## r02 prototype correction
保持ChArUco同標靶到重投影，不混入金屬工件；相機軸標示與取樣方向分開。原生與頁內pending。
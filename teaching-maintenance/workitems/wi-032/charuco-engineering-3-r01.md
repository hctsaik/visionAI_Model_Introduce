# WI-032 charuco-engineering-3 r01
- lesson objective: 姿態、相機校正與工站轉換，是不同的交付。
- page type: C
- primary reading path: 板上3D與影像2D點 → 求板到相機的R/t → 重投影與多解核對 → 工作核對與接手
- major visual nodes:
  1. 板上3D與影像2D點
  2. 求板到相機的R/t
  3. 重投影與多解核對
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-21-alignment-to-measurement_v01.png`
- pale-yellow takeaway: #FFF4CC：姿態、相機校正與工站轉換，是不同的交付。
- generation: 新建精確SVG→PNG，桌機1672×941、手機直向；actual PNG review pending，user approval pending。與首讀PNG分開。
- source: https://docs.opencv.org/4.13.0/da/d13/tutorial_aruco_calibration.html
- evidence: solvePnP把板上物體座標轉到相機座標。平面與特定求解器可能涉及多解；需結合可見性、重投影和工作約束核對，單一低誤差不自動保證工站量測。

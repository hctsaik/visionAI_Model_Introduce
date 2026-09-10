# WI-032 charuco-engineering-1 r01
- lesson objective: 建立的是相機幾何，不是每天工件的定位結果。
- page type: C
- primary reading path: 已知板上座標 → 多視角觀測 → 估相機模型 → 工作核對與接手
- major visual nodes:
  1. 已知板上座標
  2. 多視角觀測
  3. 估相機模型
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-21-alignment-to-measurement_v01.png`
- pale-yellow takeaway: #FFF4CC：建立的是相機幾何，不是每天工件的定位結果。
- generation: 新建精確SVG→PNG，桌機1672×941、手機直向；actual PNG review pending，user approval pending。與首讀PNG分開。
- source: https://docs.opencv.org/4.13.0/da/d13/tutorial_aruco_calibration.html
- evidence: 以標靶已知3D平面座標與各視角2D點估計相機模型；板上Z=0不等於影像是正視投影。校正需要合適視角、模型及品質核對，不能把固定工件對位當成校正。

## r02 prototype correction
保持ChArUco同標靶到重投影，不混入金屬工件；相機軸標示與取樣方向分開。原生與頁內pending。
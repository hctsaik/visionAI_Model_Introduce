# WI-032 sift-engineering-1 r01
- lesson objective: SIFT特徵、matcher點對與幾何變換分開。
- page type: C
- primary reading path: 跨尺度找局部 → 尺度與主方向 → 關鍵點與描述子 → 工作核對與接手
- major visual nodes:
  1. 跨尺度找局部
  2. 尺度與主方向
  3. 關鍵點與描述子
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-21-alignment-to-measurement_v01.png`
- pale-yellow takeaway: #FFF4CC：SIFT特徵、matcher點對與幾何變換分開。
- generation: 新建精確SVG→PNG，桌機1672×941、手機直向；actual PNG review pending，user approval pending。與首讀PNG分開。
- source: https://docs.opencv.org/4.13.0/da/df5/tutorial_py_sift_intro.html
- evidence: SIFT透過尺度空間極值與局部定位找點，分配主方向後計算局部梯度描述子。匹配器以描述子尋找點對；單應、姿態或對齊並不是SIFT本身的輸出。

## r02 prototype correction
保持ChArUco同標靶到重投影，不混入金屬工件；相機軸標示與取樣方向分開。原生與頁內pending。
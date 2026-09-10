# WI-032 ecc-engineering-3 r01
- lesson objective: 先寫清楚映射方向，再決定反矩陣與取樣設定。
- page type: C
- primary reading path: 定義座標與方向 → 明確定義W → 取樣旗標須相符 → 工作核對與接手
- major visual nodes:
  1. 定義座標與方向
  2. 明確定義W
  3. 取樣旗標須相符
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-21-alignment-to-measurement_v01.png`
- pale-yellow takeaway: #FFF4CC：先寫清楚映射方向，再決定反矩陣與取樣設定。
- generation: 新建精確SVG→PNG，桌機1672×941、手機直向；actual PNG review pending，user approval pending。與首讀PNG分開。
- source: https://docs.opencv.org/4.13.0/dc/d6b/group__video__track.html
- evidence: OpenCV findTransformECC的warp常配warpAffine/warpPerspective及WARP_INVERSE_MAP，把input重採樣至template座標。若交換角色或自行取逆矩陣，旗標也必須一致；用已知平移點做驗證，不憑圖看起來像就認為方向正確。

## r02 prototype correction
保持ChArUco同標靶到重投影，不混入金屬工件；相機軸標示與取樣方向分開。原生與頁內pending。
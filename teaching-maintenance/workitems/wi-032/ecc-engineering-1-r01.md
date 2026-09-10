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

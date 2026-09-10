# WI-032 lightglue-engineering-1 r01
- lesson objective: LightGlue不取代找點，也不直接給工站姿態。
- page type: C
- primary reading path: 相容extractor → LightGlue更新配對 → 點對交幾何估計 → 工作核對與接手
- major visual nodes:
  1. 相容extractor
  2. LightGlue更新配對
  3. 點對交幾何估計
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-21-alignment-to-measurement_v01.png`
- pale-yellow takeaway: #FFF4CC：LightGlue不取代找點，也不直接給工站姿態。
- generation: 新建精確SVG→PNG，桌機1672×941、手機直向；actual PNG review pending，user approval pending。與首讀PNG分開。
- source: https://github.com/cvg/LightGlue
- evidence: 官方提供多種extractor相容設定，部署應記錄權重、前處理與影像尺寸。點對與匹配信心不等於幾何準確率，後端求解與工作驗證仍需另行負責。

## r02 prototype correction
保持ChArUco同標靶到重投影，不混入金屬工件；相機軸標示與取樣方向分開。原生與頁內pending。
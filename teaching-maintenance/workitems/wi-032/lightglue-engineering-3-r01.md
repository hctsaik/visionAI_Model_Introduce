# WI-032 lightglue-engineering-3 r01
- lesson objective: 自適應不是每張圖都更快的保證。
- page type: C
- primary reading path: 深度：可能提早停止 → 寬度：修剪部分點 → 量完整處理鏈 → 工作核對與接手
- major visual nodes:
  1. 深度：可能提早停止
  2. 寬度：修剪部分點
  3. 量完整處理鏈
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-21-alignment-to-measurement_v01.png`
- pale-yellow takeaway: #FFF4CC：自適應不是每張圖都更快的保證。
- generation: 新建精確SVG→PNG，桌機1672×941、手機直向；actual PNG review pending，user approval pending。與首讀PNG分開。
- source: https://github.com/cvg/LightGlue
- evidence: 自適應深度依信心提前停止，寬度修剪部分低可匹配點以減少後續計算；實際門檻與后端实现有关。完整时间包含extractor、資料搬移、matcher及几何估计，不能只用名称宣称更快。

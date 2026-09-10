# WI-032 yolo-world-engineering-3 r01
- lesson objective: 快取向量不等於已完成模型重參數化。
- page type: C
- primary reading path: 固定詞彙先編碼 → 實作可做重參數化 → 換詞彙就更新產物 → 工作核對與接手
- major visual nodes:
  1. 固定詞彙先編碼
  2. 實作可做重參數化
  3. 換詞彙就更新產物
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-21-alignment-to-measurement_v01.png`
- pale-yellow takeaway: #FFF4CC：快取向量不等於已完成模型重參數化。
- generation: 新建精確SVG→PNG，桌機1672×941、手機直向；actual PNG review pending，user approval pending。與首讀PNG分開。
- source: https://arxiv.org/abs/2401.17270
- evidence: 官方reparameterize文档区分快取文本特征和进一步转换部署结构。采用时应记录版本、词汇、编码器及部署产物；换词汇需要对应更新，不只改前端显示文字。

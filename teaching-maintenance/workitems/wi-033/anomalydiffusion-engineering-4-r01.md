# AnomalyDiffusion：兩個遮罩只長一傷
- lesson objective: 未生成的區域，不能沿用缺陷標籤。
- page type: D
- primary reading path: 條件指定左大右小兩區 → 反例只生成左側刮傷 → 剔除或修標，再驗訓練效益 → 未生成的區域，不能沿用缺陷標籤。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 未生成的區域，不能沿用缺陷標籤。 #FFF4CC
- major visual nodes:
  1. 條件指定左大右小兩區
  2. 反例只生成左側刮傷
  3. 剔除或修標，再驗訓練效益
同板同mask，一傷對兩標籤是錯標反例；AAR可能改善但不保證避免。不得用合成量取代真實留出集。
來源：https://arxiv.org/html/2312.05767v1
模式：新SVG→PNG作者機制示意，非本輪模型推論。11課原首讀桌機與V-JEPA/SR手機已實看；夾爪方塊、各課矩形板孔位/缺陷位置保持原身份。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

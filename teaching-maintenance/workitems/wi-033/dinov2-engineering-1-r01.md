# DINOv2：先抽表示，再定義下游任務
- lesson objective: 骨幹交特徵，分類與異常判定還要另接。
- page type: C
- primary reading path: 同一L支架作輸入 → 骨幹抽整圖與局部表示 → 下游可分類或查庫 → 骨幹交特徵，分類與異常判定還要另接。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 骨幹交特徵，分類與異常判定還要另接。 #FFF4CC
- major visual nodes:
  1. 同一L支架作輸入；b4-dino-input
  2. 骨幹抽整圖與局部表示；b4-dino-deploy
  3. 下游可分類或查庫；b4-dino-downstream

DINOv2預訓練表示可支援整圖與密集下游；本身不是工廠缺陷分類規格。部署選定骨幹和前處理，抽特徵後才用標註頭或參考庫決定任務；圖中向量為示意。
來源：https://arxiv.org/abs/2304.07193
模式：新精確SVG→1672×941及768×2304PNG；八家族原型已實看通過。三節點、單讀序，保留原有效主線與具體工件身份。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

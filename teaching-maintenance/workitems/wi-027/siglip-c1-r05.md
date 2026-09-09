# WI027 SigLIP手機r05
- lesson objective: 正負配對身分正確，完整保留訓練到部署及結論。
- page type: C — 配對學習。
- primary reading path: 圖文樣本 → 同圖正負配對 → 更新兩編碼器 → 部署比較。
- major visual nodes:
  1. 工件與文字。
  2. 同支架圖配支架文字為正、配齒輪文字為負。
  3. 合計損失分別更新兩編碼器。
  4. 部署圖文各自編碼比相似度。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已看。
- pale-yellow takeaway: #FFF4CC 逐對學配合程度，分數仍要用自己的資料驗證。
- correction: r04補回結論，但生成器擅把負配對影像改成齒輪；僅將第二列影像改回同支架。r04原生861×1827，布局不再1:3；先以326px實看是否滿足閱讀再决定採用，不以要求尺寸冒充輸出尺寸。
- generation: siglip-mobile-r05-prompt.json；原生及326px審查pending；user approval pending。

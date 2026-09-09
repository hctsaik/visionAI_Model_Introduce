# WI027 Qwen反例r03
- lesson objective: 低像素與原圖文字區裁切的細節及成本取捨。
- page type: D — 輸入細節對比。
- primary reading path: 原始銘牌 → 低像素模糊 → 原圖文字區 → 回答及成本比較。
- major visual nodes:
  1. 長銘牌A17與B08。
  2. 低解析度與不確定回答。
  3. 原圖只裁批次文字、核對B08及成本。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已看。
- pale-yellow takeaway: #FFF4CC 比較答案時，同時比較細節覆蓋、token 與完整耗時。
- correction: r02手機放大裁切仍帶錯位置螺絲；桌面框選文字卻裁入兩顆螺絲。改緊框僅文字，放大僅文字與金屬，不帶螺絲或邊緣；移除無關自造廠名。generation-batch13.json，原生／頁內審查pending，user approval pending。

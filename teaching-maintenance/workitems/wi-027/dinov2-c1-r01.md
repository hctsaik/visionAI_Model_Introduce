# WI-027 DINOv2 核心原型 r01
- lesson objective: 看懂無人工類別標籤的自監督學習，如何產生可用於找相似工件的影像特徵。
- page type: C — 解釋訓練來源到部署用途。
- primary reading path: 無標籤工件影像 → 不同視圖學一致特徵 → 部署抽取特徵 → 下游查相似工件。
- major visual nodes:
  1. 未標類別的影像；同一雙孔金屬支架的全景及局部視圖。
  2. 訓練：Teacher 提供特徵目標，Student 從不同視圖學匹配；局部遮蔽與對應特徵。
  3. 部署：新支架只經已學會的 DINOv2 encoder，輸出整圖特徵條與保留位置的局部特徵圖。
  4. 下游查庫：新支架整圖特徵與參考工件特徵比相似度，找出相似支架而非齒輪；不是缺陷判定。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，沿用金屬物件質感、就近圖像證據、淡細框和清楚主路徑。
- pale-yellow takeaway: #FFF4CC：先把影像學成特徵，再由下游決定怎麼用。
- input identity: 銀色雙孔 L 形支架；全景、局部來源與輸出格位可追蹤。參考庫另有同類支架與明顯不同的齒輪，不畫缺陷分數。
- evidence: AI生成教學示意，無模型實測；特徵色塊為質性表示，不是分割標籤。
- source: https://arxiv.org/abs/2304.07193 ; https://github.com/facebookresearch/dinov2
- learning applied: WI-026 訓練與推論分開；不把 feature 畫成像素真值或檢測框。遮住正文仍需看得出 Teacher→Student 的學習方向與查庫兩方。
- generation: built-in imagegen; desktop 16:9 PNG，mobile 1:3 獨立重排；原型先桌面再擴展。
- actual review: pending；user approval: pending。
- verification: 原生PNG、936px桌面及326px手機實看，物件一致、箭頭不串错、單一黃結論；先原型再批次。

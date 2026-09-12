# ViT：把影像區塊變成可交流的表示
- lesson objective: 切片保留位置，分類仍需資料與任務頭。
- page type: C — 真實資料變換用C，同條件比較用D。
- primary reading path: 同件影像切成區塊 → 各片加入位置表示 → 分類token讀出整件分數 → 切片保留位置，分類仍需資料與任務頭。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看具體工件與映射、短句、單黃结論；不沿用多欄小字。
- pale-yellow takeaway: 切片保留位置，分類仍需資料與任務頭。 #FFF4CC
- major visual nodes:
  1. 同件影像切成區塊；證據場景 b3-vit-patches
  2. 各片加入位置表示；證據場景 b3-vit-tokens
  3. 分類token讀出整件分數；證據場景 b3-vit-cls

## 輸入、方法、輸出與證據
原始ViT把不重疊patch線性投影成token，加入位置嵌入及分類token；Transformer交換資訊，最後CLS表示經分類頭讀出類別。本課是分類器，不把patch熱圖當分割。
來源：https://arxiv.org/abs/2010.11929。保留WI-031已成立首讀，新工程圖各自有責任。共用圖元只保存相同工件，不用改名熱圖代替各方法。三段箭頭僅表示本頁實際資料或推論關係，D頁無跨方法因果箭頭。
生成模式：新建精確SVG再渲染PNG，桌機1672×941，手機768×2304。分類支架或分割細焊線按本圖身份固定，不冒充本輪模型實測。每模型先工程2原型，實看前不擴展；逐張原生與頁內尺寸另評。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

# ConvNeXt：卷積也能逐步整理分類線索
- lesson objective: 先定義類別，再用分層卷積彙整影像。
- page type: C — 真實資料變換用C，同條件比較用D。
- primary reading path: 有標籤的支架照片 → 空間與通道各做一次混合 → 彙整後交出類別分數 → 先定義類別，再用分層卷積彙整影像。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看具體工件與映射、短句、單黃结論；不沿用多欄小字。
- pale-yellow takeaway: 先定義類別，再用分層卷積彙整影像。 #FFF4CC
- major visual nodes:
  1. 有標籤的支架照片；證據場景 b3-res-data
  2. 空間與通道各做一次混合；證據場景 b3-cnx-block
  3. 彙整後交出類別分數；證據場景 b3-cnx-score

## 輸入、方法、輸出與證據
原始ConvNeXt是純卷積骨幹，借鑑現代設計但不是自注意力Transformer。分層下採樣整理影像，區塊含depthwise空間卷積、通道混合與殘差；下游分類頭和標註定義類別。
來源：https://arxiv.org/abs/2201.03545。保留WI-031已成立首讀，新工程圖各自有責任。共用圖元只保存相同工件，不用改名熱圖代替各方法。三段箭頭僅表示本頁實際資料或推論關係，D頁無跨方法因果箭頭。
生成模式：新建精確SVG再渲染PNG，桌機1672×941，手機768×2304。分類支架或分割細焊線按本圖身份固定，不冒充本輪模型實測。每模型先工程2原型，實看前不擴展；逐張原生與頁內尺寸另評。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

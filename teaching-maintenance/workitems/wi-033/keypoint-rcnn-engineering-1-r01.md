# Keypoint R-CNN：先找物件，再找具名點
- lesson objective: 點的身份要先定義，座標不能混成無名熱區。
- page type: C — 真實資料變換用C，同條件比較用D。
- primary reading path: 支架A缺口、B/C孔心 → 每件ROI保留相對位置 → A/B/C各有自己的位置分布 → 點的身份要先定義，座標不能混成無名熱區。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看具體工件與映射、短句、單黃结論；不沿用多欄小字。
- pale-yellow takeaway: 點的身份要先定義，座標不能混成無名熱區。 #FFF4CC
- major visual nodes:
  1. 支架A缺口、B/C孔心；證據場景 b3-kpt-data
  2. 每件ROI保留相對位置；證據場景 b3-kpt-roi
  3. A/B/C各有自己的位置分布；證據場景 b3-kpt-heatmaps

## 輸入、方法、輸出與證據
把Mask R-CNN的關鍵點支路用於自訂工件，需重新定義並標註關鍵點身份；人體預訓練權重不直接懂支架孔心。每個ROI的每個關鍵點有位置分布，經解碼映回原圖，不是任意紅色熱區。
來源：https://arxiv.org/abs/1703.06870。保留WI-031已成立首讀，新工程圖各自有責任。共用圖元只保存相同工件，不用改名熱圖代替各方法。三段箭頭僅表示本頁實際資料或推論關係，D頁無跨方法因果箭頭。
生成模式：新建精確SVG再渲染PNG，桌機1672×941，手機768×2304。分類支架或分割細焊線按本圖身份固定，不冒充本輪模型實測。每模型先工程2原型，實看前不擴展；逐張原生與頁內尺寸另評。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

# ResNet：背景變了，分類依據仍要成立
- lesson objective: 同件換背景測捷徑，定位需求另選位置輸出。
- page type: D — 真實資料變換用C，同條件比較用D。
- primary reading path: 同件放在兩種背景 → 分類器只給整件類別 → 需要位置時比較分割 → 同件換背景測捷徑，定位需求另選位置輸出。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看具體工件與映射、短句、單黃结論；不沿用多欄小字。
- pale-yellow takeaway: 同件換背景測捷徑，定位需求另選位置輸出。 #FFF4CC
- major visual nodes:
  1. 同件放在兩種背景；證據場景 b3-common-background
  2. 分類器只給整件類別；證據場景 b3-res-scope
  3. 需要位置時比較分割；證據場景 b3-res-alternative

## 輸入、方法、輸出與證據
相同支架與缺口只改背景，檢查模型是否依背景而非工件分類。若要缺陷位置，另評分割及其像素標註成本；ResNet可當骨幹，但本分類頭不因有熱圖可視化就變成分割器。
來源：https://arxiv.org/abs/1512.03385。保留WI-031已成立首讀，新工程圖各自有責任。共用圖元只保存相同工件，不用改名熱圖代替各方法。三段箭頭僅表示本頁實際資料或推論關係，D頁無跨方法因果箭頭。
生成模式：新建精確SVG再渲染PNG，桌機1672×941，手機768×2304。分類支架或分割細焊線按本圖身份固定，不冒充本輪模型實測。每模型先工程2原型，實看前不擴展；逐張原生與頁內尺寸另評。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

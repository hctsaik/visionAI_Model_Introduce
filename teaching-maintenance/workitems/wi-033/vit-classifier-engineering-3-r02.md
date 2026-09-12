# ViT：改切片設定，細節與成本都會變
- lesson objective: 先確認細傷還可見，再測分類與記憶體。
- page type: C — 真實資料變換用C，同條件比較用D。
- primary reading path: 同一細痕與輸入取樣 → 切片尺度改變token數 → 保留同件測試與錯分類型 → 先確認細傷還可見，再測分類與記憶體。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看具體工件與映射、短句、單黃结論；不沿用多欄小字。
- pale-yellow takeaway: 先確認細傷還可見，再測分類與記憶體。 #FFF4CC
- major visual nodes:
  1. 同一細痕與輸入取樣；證據場景 b3-vit-resolution
  2. 切片尺度改變token數；證據場景 b3-vit-cost
  3. 保留同件測試與錯分類型；證據場景 b3-vit-review

## 輸入、方法、輸出與證據
改解析度會改token數及注意力成本；改patch尺寸涉及模型配置與權重相容性，不能隨意把現有權重改為另一尺寸。先查實際輸入可見線索，再比較分類、記憶體及延遲；圖中的格子是分片概念而非真實注意力圖。
來源：https://arxiv.org/abs/2010.11929。保留WI-031已成立首讀，新工程圖各自有責任。共用圖元只保存相同工件，不用改名熱圖代替各方法。三段箭頭僅表示本頁實際資料或推論關係，D頁無跨方法因果箭頭。
生成模式：新建精確SVG再渲染PNG，桌機1672×941，手機768×2304。分類支架或分割細焊線按本圖身份固定，不冒充本輪模型實測。每模型先工程2原型，實看前不擴展；逐張原生與頁內尺寸另評。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

修訂r02：原生實看後縮小U-Net輸出避免壓字；粗取樣改同件格線位置，不能人工挖斷當取樣實測；YOLO去重前後同顯示尺度；移除無目標箭頭；ViT刮傷名稱與圖一致。新候選待實看，未整合。

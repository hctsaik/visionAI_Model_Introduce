# SegFormer：解析度與細邊界一起驗
- lesson objective: 多尺度不能補回取像已消失的細線。
- page type: C — 真實資料變換用C，同條件比較用D。
- primary reading path: 原圖細線與較粗取樣 → 融合輸出映回原圖 → 核對細線、邊界與時間 → 多尺度不能補回取像已消失的細線。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看具體工件與映射、短句、單黃结論；不沿用多欄小字。
- pale-yellow takeaway: 多尺度不能補回取像已消失的細線。 #FFF4CC
- major visual nodes:
  1. 原圖細線與較粗取樣；證據場景 b3-seg-resolution
  2. 融合輸出映回原圖；證據場景 b3-unet-map
  3. 核對細線、邊界與時間；證據場景 b3-seg-review

## 輸入、方法、輸出與證據
雖不依赖固定位置編碼，仍需依模型和實作處理輸入尺寸與padding，不能說任意尺寸均等好。測同一細線在不同解析度的可見性、邊界誤差與整條流程成本；不把插值出更多像素當新增觀測。
來源：https://arxiv.org/abs/2105.15203。保留WI-031已成立首讀，新工程圖各自有責任。共用圖元只保存相同工件，不用改名熱圖代替各方法。三段箭頭僅表示本頁實際資料或推論關係，D頁無跨方法因果箭頭。
生成模式：新建精確SVG再渲染PNG，桌機1672×941，手機768×2304。分類支架或分割細焊線按本圖身份固定，不冒充本輪模型實測。每模型先工程2原型，實看前不擴展；逐張原生與頁內尺寸另評。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

修訂r02：原生實看後縮小U-Net輸出避免壓字；粗取樣改同件格線位置，不能人工挖斷當取樣實測；YOLO去重前後同顯示尺度；移除無目標箭頭；ViT刮傷名稱與圖一致。新候選待實看，未整合。

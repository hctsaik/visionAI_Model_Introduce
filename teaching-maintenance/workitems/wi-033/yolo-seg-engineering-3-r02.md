# YOLO-Seg：遮罩要和同一個框一起交付
- lesson objective: 把框、類別與遮罩綁定，映回原圖再核對。
- page type: C — 真實資料變換用C，同條件比較用D。
- primary reading path: 候選框與係數保持配對 → 去重保留後產生對應遮罩 → 原圖檢查孔洞與相鄰件 → 把框、類別與遮罩綁定，映回原圖再核對。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看具體工件與映射、短句、單黃结論；不沿用多欄小字。
- pale-yellow takeaway: 把框、類別與遮罩綁定，映回原圖再核對。 #FFF4CC
- major visual nodes:
  1. 候選框與係數保持配對；證據場景 b3-yseg-pair
  2. 去重保留後產生對應遮罩；證據場景 b3-yseg-filter
  3. 原圖檢查孔洞與相鄰件；證據場景 b3-yseg-review

## 輸入、方法、輸出與證據
遵循實作的候選過濾與去重，索引必須同步框、類別、係數，不能將甲框配乙mask。映回需還原letterbox，輪廓不能填掉空孔；定位與量測仍須另外驗證，遮罩不是亞像素尺寸真值。
來源：https://docs.ultralytics.com/reference/nn/modules/head/#ultralytics.nn.modules.head.Segment。保留WI-031已成立首讀，新工程圖各自有責任。共用圖元只保存相同工件，不用改名熱圖代替各方法。三段箭頭僅表示本頁實際資料或推論關係，D頁無跨方法因果箭頭。
生成模式：新建精確SVG再渲染PNG，桌機1672×941，手機768×2304。分類支架或分割細焊線按本圖身份固定，不冒充本輪模型實測。每模型先工程2原型，實看前不擴展；逐張原生與頁內尺寸另評。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

修訂r02：原生實看後縮小U-Net輸出避免壓字；粗取樣改同件格線位置，不能人工挖斷當取樣實測；YOLO去重前後同顯示尺度；移除無目標箭頭；ViT刮傷名稱與圖一致。新候選待實看，未整合。

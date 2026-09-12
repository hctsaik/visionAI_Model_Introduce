# YOLO-Seg：同類零件也要各有一張遮罩
- lesson objective: 每件有框、類別與遮罩，身份只屬當前影像。
- page type: C — 真實資料變換用C，同條件比較用D。
- primary reading path: 两件同類支架各自標註 → 共享影像特徵產生兩路 → 每件係數組合出自己的遮罩 → 每件有框、類別與遮罩，身份只屬當前影像。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看具體工件與映射、短句、單黃结論；不沿用多欄小字。
- pale-yellow takeaway: 每件有框、類別與遮罩，身份只屬當前影像。 #FFF4CC
- major visual nodes:
  1. 两件同類支架各自標註；證據場景 b3-yseg-data
  2. 共享影像特徵產生兩路；證據場景 b3-yseg-branches
  3. 每件係數組合出自己的遮罩；證據場景 b3-yseg-output

## 輸入、方法、輸出與證據
以YOLOv8式prototype和mask coefficients路徑說明。訓練需各實例的類別與輪廓，推論保留各物件框、分數和實例遮罩；圖中甲乙只是這張影像的實例，不是跨影格追蹤ID。
來源：https://docs.ultralytics.com/reference/nn/modules/head/#ultralytics.nn.modules.head.Segment。保留WI-031已成立首讀，新工程圖各自有責任。共用圖元只保存相同工件，不用改名熱圖代替各方法。三段箭頭僅表示本頁實際資料或推論關係，D頁無跨方法因果箭頭。
生成模式：新建精確SVG再渲染PNG，桌機1672×941，手機768×2304。分類支架或分割細焊線按本圖身份固定，不冒充本輪模型實測。每模型先工程2原型，實看前不擴展；逐張原生與頁內尺寸另評。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

手機實看修訂：標題刮傷名稱同步；比較具體指ConvNeXt逐通道卷積，不泛稱所有卷積；ROI標籤框加寬，乙標籤與邊框分離。待重新實看。

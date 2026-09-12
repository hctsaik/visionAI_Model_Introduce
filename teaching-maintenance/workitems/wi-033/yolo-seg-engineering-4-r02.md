# 語意與實例分割：同類是否需要分成兩件
- lesson objective: 需要逐件交付時，比較實例標註與分離品質。
- page type: D — 真實資料變換用C，同條件比較用D。
- primary reading path: 同一影像有兩件支架 → 語意：兩件都屬支架類 → 實例：甲乙各有遮罩 → 需要逐件交付時，比較實例標註與分離品質。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看具體工件與映射、短句、單黃结論；不沿用多欄小字。
- pale-yellow takeaway: 需要逐件交付時，比較實例標註與分離品質。 #FFF4CC
- major visual nodes:
  1. 同一影像有兩件支架；證據場景 b3-yseg-scene
  2. 語意：兩件都屬支架類；證據場景 b3-yseg-semantic
  3. 實例：甲乙各有遮罩；證據場景 b3-yseg-output

## 輸入、方法、輸出與證據
共同输入与物件外观不变。语意遮罩同色表示同類，不一定提供逐件身份；實例分割分出甲乙，可支援後續逐件統計。重疊與遮擋仍可能分錯，需要標註與域內驗證；不聲稱必然比語意分割更適合所有工作。
來源：https://docs.ultralytics.com/reference/nn/modules/head/#ultralytics.nn.modules.head.Segment。保留WI-031已成立首讀，新工程圖各自有責任。共用圖元只保存相同工件，不用改名熱圖代替各方法。三段箭頭僅表示本頁實際資料或推論關係，D頁無跨方法因果箭頭。
生成模式：新建精確SVG再渲染PNG，桌機1672×941，手機768×2304。分類支架或分割細焊線按本圖身份固定，不冒充本輪模型實測。每模型先工程2原型，實看前不擴展；逐張原生與頁內尺寸另評。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

手機實看修訂：標題刮傷名稱同步；比較具體指ConvNeXt逐通道卷積，不泛稱所有卷積；ROI標籤框加寬，乙標籤與邊框分離。待重新實看。

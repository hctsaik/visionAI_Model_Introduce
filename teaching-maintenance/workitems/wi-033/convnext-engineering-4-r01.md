# ConvNeXt與ResNet：先固定同一分類任務
- lesson objective: 兩者都需域內驗證，架構新舊不能替代結果。
- page type: D — 真實資料變換用C，同條件比較用D。
- primary reading path: 共同照片與類別定義 → ResNet殘差卷積路徑 → ConvNeXt空間通道路徑 → 兩者都需域內驗證，架構新舊不能替代結果。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看具體工件與映射、短句、單黃结論；不沿用多欄小字。
- pale-yellow takeaway: 兩者都需域內驗證，架構新舊不能替代結果。 #FFF4CC
- major visual nodes:
  1. 共同照片與類別定義；證據場景 b3-class-common
  2. ResNet殘差卷積路徑；證據場景 b3-res-residual
  3. ConvNeXt空間通道路徑；證據場景 b3-cnx-block

## 輸入、方法、輸出與證據
兩個候選各用相容前處理，固定產品、類別、訓練資料及留出樣本。比較錯分類型、訓練資源、完整延遲；保留ResNet作合理起點，不能把ConvNeXt現代化設計當所有資料上都較準的保證。
來源：https://arxiv.org/abs/2201.03545。保留WI-031已成立首讀，新工程圖各自有責任。共用圖元只保存相同工件，不用改名熱圖代替各方法。三段箭頭僅表示本頁實際資料或推論關係，D頁無跨方法因果箭頭。
生成模式：新建精確SVG再渲染PNG，桌機1672×941，手機768×2304。分類支架或分割細焊線按本圖身份固定，不冒充本輪模型實測。每模型先工程2原型，實看前不擴展；逐張原生與頁內尺寸另評。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

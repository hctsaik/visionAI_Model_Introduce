# ConvNeXt：效率要連同解析度一起驗
- lesson objective: 保存模型配置，測完整分類流程與錯分代價。
- page type: C — 真實資料變換用C，同條件比較用D。
- primary reading path: 固定影像裁切與解析度 → 由多尺度特徵彙整分類 → 比較時間與細傷錯分 → 保存模型配置，測完整分類流程與錯分代價。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看具體工件與映射、短句、單黃结論；不沿用多欄小字。
- pale-yellow takeaway: 保存模型配置，測完整分類流程與錯分代價。 #FFF4CC
- major visual nodes:
  1. 固定影像裁切與解析度；證據場景 b3-cnx-contract
  2. 由多尺度特徵彙整分類；證據場景 b3-cnx-pool
  3. 比較時間與細傷錯分；證據場景 b3-cnx-review

## 輸入、方法、輸出與證據
相同產品固定測試集與裁切，記錄ConvNeXt尺寸、精度格式、硬體與整條流程延遲。較小模型或輸入不保證可保留細傷線索；比較整件錯分及人工覆核，不用論文單一指標代替本地選型。
來源：https://arxiv.org/abs/2201.03545。保留WI-031已成立首讀，新工程圖各自有責任。共用圖元只保存相同工件，不用改名熱圖代替各方法。三段箭頭僅表示本頁實際資料或推論關係，D頁無跨方法因果箭頭。
生成模式：新建精確SVG再渲染PNG，桌機1672×941，手機768×2304。分類支架或分割細焊線按本圖身份固定，不冒充本輪模型實測。每模型先工程2原型，實看前不擴展；逐張原生與頁內尺寸另評。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

# ViT與卷積：同題比較資料與計算代價
- lesson objective: 全局交流是能力來源，不保證小資料就更準。
- page type: D — 真實資料變換用C，同條件比較用D。
- primary reading path: 相同分類照片與標籤 → 卷積先聚合局部鄰域 → 注意力跨片交換資訊 → 全局交流是能力來源，不保證小資料就更準。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看具體工件與映射、短句、單黃结論；不沿用多欄小字。
- pale-yellow takeaway: 全局交流是能力來源，不保證小資料就更準。 #FFF4CC
- major visual nodes:
  1. 相同分類照片與標籤；證據場景 b3-class-common
  2. 卷積先聚合局部鄰域；證據場景 b3-cnx-spatial
  3. 注意力跨片交換資訊；證據場景 b3-vit-attention

## 輸入、方法、輸出與證據
在相同產品和標籤下比較預訓練、可調整資料量、輸入解析度及硬體成本；卷積局部先驗可能適合部分小資料任務，ViT利用大規模預訓練仍需域內驗證。候選可並行，不畫成必須串接。
來源：https://arxiv.org/abs/2010.11929。保留WI-031已成立首讀，新工程圖各自有責任。共用圖元只保存相同工件，不用改名熱圖代替各方法。三段箭頭僅表示本頁實際資料或推論關係，D頁無跨方法因果箭頭。
生成模式：新建精確SVG再渲染PNG，桌機1672×941，手機768×2304。分類支架或分割細焊線按本圖身份固定，不冒充本輪模型實測。每模型先工程2原型，實看前不擴展；逐張原生與頁內尺寸另評。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

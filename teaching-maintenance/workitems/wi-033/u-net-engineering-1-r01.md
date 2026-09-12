# U-Net：標出每個像素屬於哪一類
- lesson objective: 像素標註教會區域，輸出仍需回原圖核對。
- page type: C — 真實資料變換用C，同條件比較用D。
- primary reading path: 原圖與細焊線標註 → 編碼與解碼接回細節 → 逐像素分類得到語意遮罩 → 像素標註教會區域，輸出仍需回原圖核對。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看具體工件與映射、短句、單黃结論；不沿用多欄小字。
- pale-yellow takeaway: 像素標註教會區域，輸出仍需回原圖核對。 #FFF4CC
- major visual nodes:
  1. 原圖與細焊線標註；證據場景 b3-unet-data
  2. 編碼與解碼接回細節；證據場景 b3-unet-bridge
  3. 逐像素分類得到語意遮罩；證據場景 b3-unet-output

## 輸入、方法、輸出與證據
沿用板上細焊線工作例，以對齊的影像和像素類別標註訓練。收縮路徑取得上下文，擴張路徑結合對應高解析度特徵恢復定位；輸出是語意區域，不自帶校正後尺寸。
來源：https://arxiv.org/abs/1505.04597。保留WI-031已成立首讀，新工程圖各自有責任。共用圖元只保存相同工件，不用改名熱圖代替各方法。三段箭頭僅表示本頁實際資料或推論關係，D頁無跨方法因果箭頭。
生成模式：新建精確SVG再渲染PNG，桌機1672×941，手機768×2304。分類支架或分割細焊線按本圖身份固定，不冒充本輪模型實測。每模型先工程2原型，實看前不擴展；逐張原生與頁內尺寸另評。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

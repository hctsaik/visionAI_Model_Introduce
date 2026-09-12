# U-Net：粗尺度找上下文，細尺度補位置
- lesson objective: 跳接提供對應特徵，解碼器仍要學會融合。
- page type: C — 真實資料變換用C，同條件比較用D。
- primary reading path: 下採樣：位置變粗 → 同尺度特徵沿跳接送達 → 上採樣融合後逐像素分類 → 跳接提供對應特徵，解碼器仍要學會融合。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看具體工件與映射、短句、單黃结論；不沿用多欄小字。
- pale-yellow takeaway: 跳接提供對應特徵，解碼器仍要學會融合。 #FFF4CC
- major visual nodes:
  1. 下採樣：位置變粗；證據場景 b3-unet-encode
  2. 同尺度特徵沿跳接送達；證據場景 b3-unet-skip
  3. 上採樣融合後逐像素分類；證據場景 b3-unet-decode

## 輸入、方法、輸出與證據
原始U-Net以crop and concatenate把編碼特徵送到匹配尺度的解碼器，並非每條skip都逐元素相加。示意省略卷積邊界尺寸，但保留同尺度配對與融合；遮罩由學習分類得到，不直接複製原圖邊緣。
來源：https://arxiv.org/abs/1505.04597。保留WI-031已成立首讀，新工程圖各自有責任。共用圖元只保存相同工件，不用改名熱圖代替各方法。三段箭頭僅表示本頁實際資料或推論關係，D頁無跨方法因果箭頭。
生成模式：新建精確SVG再渲染PNG，桌機1672×941，手機768×2304。分類支架或分割細焊線按本圖身份固定，不冒充本輪模型實測。每模型先工程2原型，實看前不擴展；逐張原生與頁內尺寸另評。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

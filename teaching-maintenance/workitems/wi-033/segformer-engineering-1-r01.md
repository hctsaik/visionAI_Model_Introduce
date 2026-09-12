# SegFormer：四個尺度一起判讀每個位置
- lesson objective: 多尺度補上下文，輸出仍是語意類別圖。
- page type: C — 真實資料變換用C，同條件比較用D。
- primary reading path: 板面影像與像素標註 → 分層編碼產生四尺度 → 對齊融合成語意遮罩 → 多尺度補上下文，輸出仍是語意類別圖。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看具體工件與映射、短句、單黃结論；不沿用多欄小字。
- pale-yellow takeaway: 多尺度補上下文，輸出仍是語意類別圖。 #FFF4CC
- major visual nodes:
  1. 板面影像與像素標註；證據場景 b3-unet-data
  2. 分層編碼產生四尺度；證據場景 b3-seg-scales
  3. 對齊融合成語意遮罩；證據場景 b3-seg-output

## 輸入、方法、輸出與證據
MiT分層Transformer產生四種尺度特徵；輕量MLP解碼器投影、對齊、串接和融合後輸出語意類別。它不自動給每個相同類別物件獨立身份，與實例分割區分。
來源：https://arxiv.org/abs/2105.15203。保留WI-031已成立首讀，新工程圖各自有責任。共用圖元只保存相同工件，不用改名熱圖代替各方法。三段箭頭僅表示本頁實際資料或推論關係，D頁無跨方法因果箭頭。
生成模式：新建精確SVG再渲染PNG，桌機1672×941，手機768×2304。分類支架或分割細焊線按本圖身份固定，不冒充本輪模型實測。每模型先工程2原型，實看前不擴展；逐張原生與頁內尺寸另評。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

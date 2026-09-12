# AnomalyGPT：先定位，再接看圖對話

- lesson objective: 內建位置提供線索，回答仍回原圖核對。
- page type: C — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 訓練：合成影像與位置對齊 → 測試：同圖內建定位 → 位置轉提示，連同圖文回答
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 內建位置提供線索，回答仍回原圖核對。 #FFF4CC
- major visual nodes:
  1. 訓練：合成影像與位置對齊；具體視覺 gpt-mobile-training
  2. 測試：同圖內建定位；具體視覺 gpt-mobile-location
  3. 位置轉提示，連同圖文回答；具體視覺 gpt-mobile-answer

## 機制、證據與修正

手機核心原四段密圖減為三段。保留原金屬板兩孔對角佈局、右側細痕，改以新SVG重建同一類幾何示意；訓練、內建定位與提示/影像/問題接LLM分清。原桌機主線保留，沒有修改既有bitmap。

來源：https://github.com/CASIA-LMC-Lab/AnomalyGPT 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG 對角兩孔金屬板、同位置細痕；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2304。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

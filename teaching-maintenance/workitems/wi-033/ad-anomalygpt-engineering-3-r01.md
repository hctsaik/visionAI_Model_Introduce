# AnomalyGPT：文字與位置一起交付

- lesson objective: 回答、位置和原圖一起覆核，對不上就保留疑問。
- page type: C — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 保留同一影像的定位 → 問題與位置提示參與回答 → 核對文字是否有原圖證據
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 回答、位置和原圖一起覆核，對不上就保留疑問。 #FFF4CC
- major visual nodes:
  1. 保留同一影像的定位；具體視覺 gpt-localize
  2. 問題與位置提示參與回答；具體視覺 gpt-prompt
  3. 核對文字是否有原圖證據；具體視覺 gpt-review

## 機制、證據與修正

交付原圖、內建定位與對話記錄，逐項核對文字描述的部位和異常類型。對話可協助判讀但不能替代定位驗證；若回答與圖不一致，保留失敗狀態並回原圖。額外外部檢測器是應用整合選擇，不是原模型必需支路。

來源：https://github.com/CASIA-LMC-Lab/AnomalyGPT 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG 金屬支架／齒輪／軸承；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

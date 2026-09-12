# AnomalyGPT：定位由內建支路產生

- lesson objective: 內建位置圖先轉提示，再連同影像與問題產生回答。
- page type: C — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 同一影像產生全局與局部表示 → 內建解碼與圖文匹配定位 → 位置轉提示後接入 LLM
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 內建位置圖先轉提示，再連同影像與問題產生回答。 #FFF4CC
- major visual nodes:
  1. 同一影像產生全局與局部表示；具體視覺 gpt-features
  2. 內建解碼與圖文匹配定位；具體視覺 gpt-localize
  3. 位置轉提示後接入 LLM；具體視覺 gpt-prompt

## 機制、證據與修正

影像編碼器提供全局與局部表示。局部表示經影像解碼器，與正常／異常文字特徵匹配得位置圖，再由prompt learner轉為提示；LLM另接全局影像表示與使用者問題。此圖是原模型內建支路，不把任意外部檢測器當必要輸入。

來源：https://github.com/CASIA-LMC-Lab/AnomalyGPT 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG 金屬支架／齒輪／軸承；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

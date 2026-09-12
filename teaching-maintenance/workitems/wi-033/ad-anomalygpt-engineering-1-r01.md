# AnomalyGPT：用成對資料學定位與回答

- lesson objective: 合成影像、遮罩與文字要描述同一處异常。
- page type: C — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 影像異常與遮罩對齊 → 文字描述同一位置與外觀 → 更新解碼器與提示學習器
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 合成影像、遮罩與文字要描述同一處异常。 #FFF4CC
- major visual nodes:
  1. 影像異常與遮罩對齊；具體視覺 diff-synthetic
  2. 文字描述同一位置與外觀；具體視覺 gpt-training-text
  3. 更新解碼器與提示學習器；具體視覺 gpt-training-targets

## 機制、證據與修正

用合成異常影像、位置遮罩及文字配對訓練；預訓練影像編碼器和LLM保持固定，更新影像解碼器及提示學習器。遮罩和描述須對上同一異常，否則不同監督互相矛盾；真實未見缺陷仍需獨立驗證。

來源：https://github.com/CASIA-LMC-Lab/AnomalyGPT 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG 金屬支架／齒輪／軸承；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

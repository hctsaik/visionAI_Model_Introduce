# Pose：對稱件的小誤差也可能騙人

- lesson objective: 遇到身份歧義，補可見證據並攔下不確定姿態。
- page type: C — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 遮擋讓點身份變模糊 → 候選都能貼近觀測點 → 增加可辨認的觀測
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 遇到身份歧義，補可見證據並攔下不確定姿態。 #FFF4CC
- major visual nodes:
  1. 遮擋讓點身份變模糊；具體視覺 pose-ambiguous
  2. 候選都能貼近觀測點；具體視覺 pose-ambiguity-error
  3. 增加可辨認的觀測；具體視覺 pose-disambiguate

## 機制、證據與修正

近對稱工件上缺口被擋，錯誤ID也可能有低重投影誤差。比較有標記與第二視角的選擇時，需核對表面限制、可見性、校正與節拍，不只挑分數略低的姿態。不能確認就輸出失敗狀態並覆核。

來源：https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG 金屬支架／齒輪／軸承；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

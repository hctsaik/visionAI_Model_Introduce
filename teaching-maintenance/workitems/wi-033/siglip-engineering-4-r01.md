# SigLIP：逐對學習不會補出缺少的類別

- lesson objective: 選型要看本地錯誤與成本，不能只看損失名稱。
- page type: D — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 兩種模型看同一齒輪 → 兩者候選都缺齒輪 → 固定條件後比較取捨
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 選型要看本地錯誤與成本，不能只看損失名稱。 #FFF4CC
- major visual nodes:
  1. 兩種模型看同一齒輪；具體視覺 gear-input
  2. 兩者候選都缺齒輪；具體視覺 both-missing
  3. 固定條件後比較取捨；具體視覺 comparison-work

## 機制、證據與修正

CLIP 與 SigLIP 使用相同工件照片、相同缺少正確答案的候選時，都不能因有最高分就判定正確。比較需固定資料及候選，測誤配、拒答和完整成本；原論文的訓練優點不保證每個域內任務較好。

來源：https://arxiv.org/abs/2303.15343 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG 金屬支架／齒輪／軸承；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

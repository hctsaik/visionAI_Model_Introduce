# SigLIP：部署交出分數，不是回答

- lesson objective: 以固定模型比較候選，再用域內資料設定覆核。
- page type: C — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 保存候選文字表示 → 新影像與候選逐一比 → 依工作風險核對結果
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 以固定模型比較候選，再用域內資料設定覆核。 #FFF4CC
- major visual nodes:
  1. 保存候選文字表示；具體視覺 text-cache
  2. 新影像與候選逐一比；具體視覺 siglip-match
  3. 依工作風險核對結果；具體視覺 score-review

## 機制、證據與修正

部署用預訓練好的圖文表示比較相似性；可依实现轉換配對分數，但不把 sigmoid 值直接當作域內正確率。結果是候選分數或排名，不是逐字生成回答，也不自帶可靠未知類別拒答。

來源：https://arxiv.org/abs/2303.15343 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG 金屬支架／齒輪／軸承；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

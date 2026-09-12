# CLIP：文字可快取，改字就要更新

- lesson objective: 換文字或權重後，更新表示並重測候選排名。
- page type: C — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 先保存文字及其表示 → 新影像與快取表示比較 → 更換候選後重新核對
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 換文字或權重後，更新表示並重測候選排名。 #FFF4CC
- major visual nodes:
  1. 先保存文字及其表示；具體視覺 text-cache
  2. 新影像與快取表示比較；具體視覺 cache-match
  3. 更換候選後重新核對；具體視覺 cache-refresh

## 機制、證據與修正

同一模型／前處理下可預先計算候選文字表示。新影像只需走影像編碼器，再與相容文字表示比較。改文字、權重或設定時更新相關快取，使用已知和未知零件重新驗證；文字快取並不是把影像直接送進文字編碼器。

來源：https://arxiv.org/abs/2103.00020 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG 金屬支架／齒輪／軸承；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

Revision r02: see prototype-review.md; candidate identity, arrow routing, label spacing and mobile wrapping rechecked.

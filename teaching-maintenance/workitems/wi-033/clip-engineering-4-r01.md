# CLIP：第一名也可能沒有正確答案

- lesson objective: 先確認候選涵蓋需求，再決定排序能否交付。
- page type: C — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 待測照片確實是齒輪 → 候選只有支架與軸承 → 加入候選仍要驗證
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 先確認候選涵蓋需求，再決定排序能否交付。 #FFF4CC
- major visual nodes:
  1. 待測照片確實是齒輪；具體視覺 gear-input
  2. 候選只有支架與軸承；具體視覺 missing-candidate
  3. 加入候選仍要驗證；具體視覺 candidate-review

## 機制、證據與修正

同一齒輪影像遇到缺少齒輪的候選集合，仍會有第一名。補齊描述後先檢查易混淆與未知資料；若工作要求細微尺寸或缺陷差別，可準備標註資料測專用分類器。以下排名為反例示意，不代表模型實測。

來源：https://arxiv.org/abs/2103.00020 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG 金屬支架／齒輪／軸承；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

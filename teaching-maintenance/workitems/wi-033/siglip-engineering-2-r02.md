# SigLIP：雙路編碼，逐對計算損失

- lesson objective: 改變的是配對訓練目標，兩個編碼器仍並行。
- page type: C — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 影像與文字分別進模型 → 每一對依正負標籤學習 → 全部配對訊號一起更新
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 改變的是配對訓練目標，兩個編碼器仍並行。 #FFF4CC
- major visual nodes:
  1. 影像與文字分別進模型；具體視覺 clip-dual
  2. 每一對依正負標籤學習；具體視覺 sigmoid-pairs
  3. 全部配對訊號一起更新；具體視覺 loss-aggregate

## 機制、證據與修正

圖文表示的內積經可學習尺度與偏移後，以正／負標籤計算 sigmoid 損失。圖中高低分僅解釋學習方向，不是模型機率校正結果；部署時不需提供正負訓練標籤。

來源：https://arxiv.org/abs/2303.15343 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG 金屬支架／齒輪／軸承；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

Revision r02: see prototype-review.md; candidate identity, arrow routing, label spacing and mobile wrapping rechecked.

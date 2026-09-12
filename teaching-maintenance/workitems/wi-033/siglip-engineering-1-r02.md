# SigLIP：每個圖文配對都給學習訊號

- lesson objective: 正配對拉近、負配對分開，共同更新編碼器。
- page type: C — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 先知道哪個描述配哪張圖 → 逐對比較配對與不配對 → 損失共同更新兩編碼器
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 正配對拉近、負配對分開，共同更新編碼器。 #FFF4CC
- major visual nodes:
  1. 先知道哪個描述配哪張圖；具體視覺 paired-training
  2. 逐對比較配對與不配對；具體視覺 pair-matrix
  3. 損失共同更新兩編碼器；具體視覺 pair-update

## 機制、證據與修正

原始 SigLIP 的圖文編碼器分別產生表示，對正負圖文對計算 sigmoid 損失，梯度共同更新參數。每對有自己的二元目標，不需要 CLIP 式的整批 softmax 正規化；逐對計算不代表每對訓練一個獨立模型。

來源：https://arxiv.org/abs/2303.15343 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG 金屬支架／齒輪／軸承；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

Revision r02: see prototype-review.md; candidate identity, arrow routing, label spacing and mobile wrapping rechecked.

# DINOv3：縮圖後的缺口可能變弱

- lesson objective: 先讓工作細節可見，再驗證特徵與下游判斷。
- page type: C — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 同一墊圈，缺口在右側 → 縮小取樣讓缺口變弱 → 補取像，重新驗下游
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 先讓工作細節可見，再驗證特徵與下游判斷。 #FFF4CC
- major visual nodes:
  1. 同一墊圈，缺口在右側；具體視覺 dino-notch
  2. 縮小取樣讓缺口變弱；具體視覺 dino-resolution
  3. 補取像，重新驗下游；具體視覺 dino-retake

## 機制、證據與修正

同一墊圈的右側缺口在粗取樣中可能被平均而減弱；本圖固定件形與方向，不把後段換成別種工件。提高輸入可見性只改善證據條件，不保證DINOv3或下游一定找出異常；仍要測漏檢及正常品誤報。

來源：https://arxiv.org/html/2508.10104v1 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG 金屬支架／齒輪／軸承；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

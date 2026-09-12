# DINOv3：換骨幹也要重建相容參考

- lesson objective: 保存權重與前處理，同條件重建庫並量完整成本。
- page type: C — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 固定取像與骨幹版本 → 建立相容的參考表示 → 核對下游結果與成本
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 保存權重與前處理，同條件重建庫並量完整成本。 #FFF4CC
- major visual nodes:
  1. 固定取像與骨幹版本；具體視覺 dino-version
  2. 建立相容的參考表示；具體視覺 dino-library
  3. 核對下游結果與成本；具體視覺 dino-evaluate

## 機制、證據與修正

部署不跑Gram教師；用固定權重與前處理抽取表示，再建相容特徵庫或訓練下游頭。不能把DINOv2庫直接當DINOv3庫查詢。以同一留出集核對命中／漏檢、抽特徵和查庫時間、記憶體與重建成本，不能只比較色圖漂亮程度。

來源：https://arxiv.org/html/2508.10104v1 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG 金屬支架／齒輪／軸承；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

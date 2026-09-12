# EfficientAD：換產品要更新哪些部分

- lesson objective: 模型與正常校正一起重驗，不能只換產品名稱。
- page type: C — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 新產品有不同正常外觀 → 適配學生／AE與分數尺度 → 同留出集比較更新前後
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 模型與正常校正一起重驗，不能只換產品名稱。 #FFF4CC
- major visual nodes:
  1. 新產品有不同正常外觀；具體視覺 eff-new-product
  2. 適配學生／AE與分數尺度；具體視覺 eff-maintenance
  3. 同留出集比較更新前後；具體視覺 eff-update-check

## 機制、證據與修正

換產品先確認正常訓練涵蓋；按需要重新訓練學生與AE，重新建立正常驗證分位數，保留舊版作對照。固定教師版本不代表下游分數可直接沿用；比較正常誤報、真缺陷漏檢、訓練/校正成本與每件耗時，不能只記模型檔大小。

來源：https://arxiv.org/html/2303.14535v3 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG L形刻痕板、A-01刻字板或三格圓柱托盤，依各圖聲明；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

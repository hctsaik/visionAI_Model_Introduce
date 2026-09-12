# DINOv3：以工作結果決定是否換骨幹

- lesson objective: 同題比較效果與重建代價，保留基準也合理。
- page type: D — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 同一批正常與缺口件 → 既有骨幹：保留相容基準 → 新骨幹：重建後再比較
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 同題比較效果與重建代價，保留基準也合理。 #FFF4CC
- major visual nodes:
  1. 同一批正常與缺口件；具體視覺 dino-comparison-data
  2. 既有骨幹：保留相容基準；具體視覺 dino-compare-v2
  3. 新骨幹：重建後再比較；具體視覺 dino-compare-v3

## 機制、證據與修正

工程4不重複主反例。固定同一批正常與缺口墊圈及取像，各自使用相容骨幹與參考表示；記錄下游漏檢/誤報、抽特徵/查庫時間與重建負擔。新骨幹訓練機制不同，不代表每項域內指標一定進步。

來源：https://arxiv.org/html/2508.10104v1 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG 金屬支架／齒輪／軸承；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

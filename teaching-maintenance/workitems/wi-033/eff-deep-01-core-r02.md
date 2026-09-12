# EfficientAD：局部特徵與整體重建合作

- lesson objective: 兩路分工不同，正常尺度對齊後一起驗。
- page type: C — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 正常影像讓三個角色學習 → 局部T/S1，全局AE/S2 → 正常驗證尺度對齊再融合
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 兩路分工不同，正常尺度對齊後一起驗。 #FFF4CC
- major visual nodes:
  1. 正常影像讓三個角色學習；具體視覺 deep-eff-learn
  2. 局部T/S1，全局AE/S2；具體視覺 eff-two-diffs
  3. 正常驗證尺度對齊再融合；具體視覺 eff-calibrate

## 機制、證據與修正

保留深讀核心的T/S/AE分工；手機改直向三段，用同章四孔板。學生第一組學T、AE學T、第二組學AE；T固定。local/global各自正常分位數校正後平均，最大值作整件分數；實測節拍另量。

來源：https://arxiv.org/html/2303.14535v3 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG L形刻痕板、A-01刻字板或三格圓柱托盤，依各圖聲明；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2304。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

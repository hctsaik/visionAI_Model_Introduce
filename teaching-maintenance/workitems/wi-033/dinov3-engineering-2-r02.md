# DINOv3：訓練時守住局部關係

- lesson objective: Gram 只約束訓練，部署仍輸出特徵。
- page type: C — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 同一影像，對照兩個模型 → 比較 patch 之間的關係 → 用關係差異更新學生
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: Gram 只約束訓練，部署仍輸出特徵。 #FFF4CC
- major visual nodes:
  1. 同一影像，對照兩個模型；具體視覺 dino-gram-input
  2. 比較 patch 之間的關係；具體視覺 dino-gram-matrix
  3. 用關係差異更新學生；具體視覺 dino-gram-update

## 機制、證據與修正

Gram矩陣記錄同圖patch特徵的兩兩內積；以較早教師的關係當目標，約束目前學生，並保留原有自監督訓練目標。這不是把特徵逐點鎖成相同數值，也不是推論時要額外跑的模組。本圖數字為二維單位向量算例。

來源：https://arxiv.org/html/2508.10104v1 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG 金屬支架／齒輪／軸承；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

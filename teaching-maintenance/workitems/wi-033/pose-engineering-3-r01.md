# Pose：姿態還要投回原图檢查

- lesson objective: 交付 R／t、座標單位與逐點誤差，再核對實體。
- page type: C — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 保存姿態與座標契約 → 把 3D 點投回相機影像 → 逐點誤差與站點交付
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 交付 R／t、座標單位與逐點誤差，再核對實體。 #FFF4CC
- major visual nodes:
  1. 保存姿態與座標契約；具體視覺 pose-transform
  2. 把 3D 點投回相機影像；具體視覺 pose-reproject
  3. 逐點誤差與站點交付；具體視覺 pose-delivery

## 機制、證據與修正

R/t表示物體到相機的變換，t單位跟3D工件座標一致。重投影把已知3D點經R/t與相機模型映回原圖，逐點比較觀測與投影；若用去畸變影像須搭配相應相機設定。交付點ID、可見性、誤差、版本與失敗狀態，外部機器人座標另需外參。

來源：https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG 金屬支架／齒輪／軸承；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

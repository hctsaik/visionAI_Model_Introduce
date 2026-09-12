# Pose：影像點必須對上實體點

- lesson objective: 先鎖定點名與相機設定，才能解讀姿態。
- page type: C — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 影像中找得到同名點 → 已知 3D 點與相機設定 → PnP 求物體到相機的姿態
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 先鎖定點名與相機設定，才能解讀姿態。 #FFF4CC
- major visual nodes:
  1. 影像中找得到同名點；具體視覺 pose-correspondence
  2. 已知 3D 點與相機設定；具體視覺 pose-calibration
  3. PnP 求物體到相機的姿態；具體視覺 pose-transform

## 機制、證據與修正

同一支架的點名應跨影像與CAD一致。三點圖解只教對應；實際點數、幾何形狀與PnP方法影響可解性。需固定K、畸變、座標系及CAD單位，輸出的R/t才有意義；不以關鍵點熱區直接當姿態。

來源：https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG 金屬支架／齒輪／軸承；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

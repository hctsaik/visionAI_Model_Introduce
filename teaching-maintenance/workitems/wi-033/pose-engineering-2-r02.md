# Pose：先框再找點，或先找點再分組

- lesson objective: 兩條替代路徑都交出有身份的 2D 點。
- page type: D — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 共同輸入：兩個支架 → Top-down：先框後找點 → Bottom-up：先點後分組
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 兩條替代路徑都交出有身份的 2D 點。 #FFF4CC
- major visual nodes:
  1. 共同輸入：兩個支架；具體視覺 pose-two
  2. Top-down：先框後找點；具體視覺 pose-topdown
  3. Bottom-up：先點後分組；具體視覺 pose-bottomup

## 機制、證據與修正

兩種2D關鍵點方法是替代方案。Top-down先偵測每個物件，再於各ROI估點並映回原圖；Bottom-up先估全圖點，再歸到不同實例。兩者都須保留物件ID、點名與原圖座標。求3D姿態仍需已知3D對應、K與畸變，這裡的三點僅解釋分組，不聲稱足以唯一求PnP。

來源：https://mmpose.readthedocs.io/en/latest/guide_to_framework.html ; https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG 金屬支架／齒輪／軸承；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

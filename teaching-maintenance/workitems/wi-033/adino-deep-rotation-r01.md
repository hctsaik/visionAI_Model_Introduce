# 旋轉前，先問方向是否屬於規格

- lesson objective: 整件與刻字一起旋轉；正常參考不能改寫允收規格。
- page type: D — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 原件：A-01刻字朝上 → 同件剛性旋轉180度 → 自由擺放與朝上規格分開
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 整件與刻字一起旋轉；正常參考不能改寫允收規格。 #FFF4CC
- major visual nodes:
  1. 原件：A-01刻字朝上；具體視覺 adino-upright
  2. 同件剛性旋轉180度；具體視覺 adino-rotated
  3. 自由擺放與朝上規格分開；具體視覺 adino-rotation-rule

## 機制、證據與修正

修正原深讀6章旋轉圖：以同一個SVG工件群組做180度旋轉，孔、缺口與刻字全部一起變換，沒有重畫另一件或保留正向刻字。若允收自由方向，可驗旋轉參考；朝向本身是缺陷則另立規則。此圖不替換遮罩/接線視圖。

來源：https://arxiv.org/html/2405.14529v2 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG L形刻痕板、A-01刻字板或三格圓柱托盤，依各圖聲明；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2304。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

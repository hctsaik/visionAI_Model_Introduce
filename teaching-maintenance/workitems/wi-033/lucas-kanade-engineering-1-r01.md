# Lucas–Kanade：先讓角點有可追的鄰域

- lesson objective: 清楚角點、穩定影格與小位移，是局部解的起點。
- page type: C — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 同相機相鄰影格 → 角點提供兩方向線索 → 金字塔先粗後細
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 清楚角點、穩定影格與小位移，是局部解的起點。 #FFF4CC
- major visual nodes:
  1. 同相機相鄰影格；具體視覺 flow-pair
  2. 角點提供兩方向線索；具體視覺 lk-texture
  3. 金字塔先粗後細；具體視覺 lk-pyramid

## 機制、證據與修正

同一L形標记随工件平移；先固定相機、時間間隔及取像，選有雙方向梯度的角點。金字塔由粗到細估計位移，傳遞估計再修細；它擴大可處理位移，但不能補回被反光遮住的內容。

來源：https://docs.opencv.org/4.13.0/d4/dee/tutorial_optical_flow.html 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG L形刻痕板、A-01刻字板或三格圓柱托盤，依各圖聲明；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

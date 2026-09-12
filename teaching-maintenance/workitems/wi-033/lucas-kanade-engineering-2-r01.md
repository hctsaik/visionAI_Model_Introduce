# Lucas–Kanade：多個像素一起限制位移

- lesson objective: 局部梯度支持共同位移，解出數字後仍要檢查。
- page type: C — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 局部像素提供亮度變化 → 共同的小位移符合多條式子 → 把解變成可核對的向量
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 局部梯度支持共同位移，解出數字後仍要檢查。 #FFF4CC
- major visual nodes:
  1. 局部像素提供亮度變化；具體視覺 lk-gradients
  2. 共同的小位移符合多條式子；具體視覺 lk-equations
  3. 把解變成可核對的向量；具體視覺 lk-solution

## 機制、證據與修正

在小位移、局部共同運動與亮度一致假設下，每個像素給Ix·u+Iy·v+It≈0。教學給定三組梯度(1,0,-2)、(0,1,-1)、(1,1,-3)，共同解u=2、v=1，單位是影格間像素位移。真實資料以最小平方近似求解，再查矩陣條件、殘差及往返一致性；示意數值不是對插圖執行光流的結果。

來源：https://docs.opencv.org/4.13.0/d4/dee/tutorial_optical_flow.html 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG L形刻痕板、A-01刻字板或三格圓柱托盤，依各圖聲明；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

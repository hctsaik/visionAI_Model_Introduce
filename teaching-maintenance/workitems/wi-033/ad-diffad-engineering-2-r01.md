# DiffusionAD：恢復與定位分兩個工作

- lesson objective: 原圖與恢復圖一起進分割，最後才交出異常位置。
- page type: C — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 同一原圖走兩個噪聲尺度 → 高噪聲估計引導低噪聲恢復 → 原圖＋恢復圖 → 分割位置
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 原圖與恢復圖一起進分割，最後才交出異常位置。 #FFF4CC
- major visual nodes:
  1. 同一原圖走兩個噪聲尺度；具體視覺 diff-noise-branches
  2. 高噪聲估計引導低噪聲恢復；具體視覺 diff-guidance
  3. 原圖＋恢復圖 → 分割位置；具體視覺 diff-segment

## 機制、證據與修正

同一原圖A加入高低噪聲；高噪聲正常估計N引導低噪聲恢復R。各尺度用單步估計，不是整套只呼叫一次網路；A和R一起進學習的分割網路，不是直接拿R當最終檢測答案。

來源：https://github.com/HuiZhang0812/DiffusionAD 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG 金屬支架／齒輪／軸承；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

# AnomalyGPT：會回答不代表會判對

- lesson objective: 同圖比較定位與文字證據，再量覆核成本。
- page type: D — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 共同原圖：刮痕在中部 → 位置在中部，文字卻說孔邊 → 帶對話是否真能減少工時
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 同圖比較定位與文字證據，再量覆核成本。 #FFF4CC
- major visual nodes:
  1. 共同原圖：刮痕在中部；具體視覺 diff-defect-input
  2. 位置在中部，文字卻說孔邊；具體視覺 gpt-mismatch
  3. 帶對話是否真能減少工時；具體視覺 gpt-work-comparison

## 機制、證據與修正

同一支架若位置圖指中部，回答卻描述孔邊，不能因語句流暢就放行。以同一批真缺陷與正常圖比較只看位置或加問答的錯誤、延遲和人工覆核时间；沒有收益時保留簡單流程也合理。

來源：https://github.com/CASIA-LMC-Lab/AnomalyGPT 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG 金屬支架／齒輪／軸承；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

# EfficientAD：保留兩路，才知道融合改了什麼

- lesson objective: 兩路與融合圖一起驗，完整流程一起計時。
- page type: C — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 保存局部、全局與融合 → 回同托盤核對兩種錯誤 → 相機到覆核的完整時間
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 兩路與融合圖一起驗，完整流程一起計時。 #FFF4CC
- major visual nodes:
  1. 保存局部、全局與融合；具體視覺 eff-ablation
  2. 回同托盤核對兩種錯誤；具體視覺 eff-review
  3. 相機到覆核的完整時間；具體視覺 eff-cost

## 機制、證據與修正

保存原圖、原始local/global圖、正常分位數校正及融合結果。用獨立正常與真缺陷對照各分支及融合錯誤；同時量取像、前處理、教師/學生/AE、映回與交付的完整耗時，不能從論文毫秒數推定產線節拍。

來源：https://arxiv.org/html/2303.14535v3 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG L形刻痕板、A-01刻字板或三格圓柱托盤，依各圖聲明；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

# DiffusionAD：去噪與定位要分別學

- lesson objective: 正常資料教恢復，合成異常和遮罩教定位。
- page type: C — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 正常影像加噪聲練恢復 → 合成異常有已知位置 → 兩個網路各有訓練責任
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 正常資料教恢復，合成異常和遮罩教定位。 #FFF4CC
- major visual nodes:
  1. 正常影像加噪聲練恢復；具體視覺 diff-normal-training
  2. 合成異常有已知位置；具體視覺 diff-synthetic
  3. 兩個網路各有訓練責任；具體視覺 diff-training-targets

## 機制、證據與修正

正常圖用於學習噪聲估計及恢復；合成異常與已知遮罩提供分割監督。兩個網路不能只用一張異常熱圖概括。合成資料仍需覆盖任務變化，最後以未見正常與真缺陷驗證。

來源：https://github.com/HuiZhang0812/DiffusionAD 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG 金屬支架／齒輪／軸承；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

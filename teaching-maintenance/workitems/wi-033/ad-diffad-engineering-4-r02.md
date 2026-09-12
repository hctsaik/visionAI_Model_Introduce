# DiffusionAD：恢復變乾淨不等於漏檢

- lesson objective: 檢查最後位置圖，分清恢復成功與定位失敗。
- page type: D — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 共同原圖：支架有刮痕 → 恢復乾淨，分割仍可定位 → 恢復保留刮痕，另查漏檢
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 檢查最後位置圖，分清恢復成功與定位失敗。 #FFF4CC
- major visual nodes:
  1. 共同原圖：支架有刮痕；具體視覺 diff-defect-input
  2. 恢復乾淨，分割仍可定位；具體視覺 diff-clean-detected
  3. 恢復保留刮痕，另查漏檢；具體視覺 diff-retained-missed

## 機制、證據與修正

固定同一刮痕影像，比較恢復是否去除異常及最後分割是否找到位置。去掉異常本來就是恢復子任務的方向，不直接等於漏檢；缺陷留在R也不必然漏，但會改變可用線索。兩條示意結果需以真實留出集驗證。

來源：https://github.com/HuiZhang0812/DiffusionAD 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG 金屬支架／齒輪／軸承；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

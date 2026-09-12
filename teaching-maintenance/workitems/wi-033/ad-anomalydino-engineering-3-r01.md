# AnomalyDINO：換參考就要重驗正常定義

- lesson objective: 保存參考版本，誤報與漏檢要一起比較。
- page type: C — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 固定待測件與原參考庫 → 只增加一個刮傷參考 → 重跑相同留出案例
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 保存參考版本，誤報與漏檢要一起比較。 #FFF4CC
- major visual nodes:
  1. 固定待測件與原參考庫；具體視覺 adino-clean
  2. 只增加一個刮傷參考；具體視覺 adino-contamination
  3. 重跑相同留出案例；具體視覺 adino-revalidate

## 機制、證據與修正

固定模型與前處理只增加候選時，最近距離不會增加；若新增參考含缺陷，原本异常可能變得相近。用同一刮痕、原候選距離0.40/0.55、新污染候選0.03說明算術，不宣稱真實模型結果。更新後同时測正常與真缺陷，保存庫來源並量建庫、查詢及記憶體。

來源：https://arxiv.org/html/2405.14529v2 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG L形刻痕板、A-01刻字板或三格圓柱托盤，依各圖聲明；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

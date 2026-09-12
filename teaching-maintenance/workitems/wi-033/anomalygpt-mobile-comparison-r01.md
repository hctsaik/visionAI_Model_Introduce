# 三種圖文方法：先選工作結果

- lesson objective: 先驗定位，再驗對話能否減少覆核成本。
- page type: D — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → WinCLIP：人工狀態與視窗 → AnomalyCLIP：學到的提示 → AnomalyGPT：定位加對話
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 先驗定位，再驗對話能否減少覆核成本。 #FFF4CC
- major visual nodes:
  1. WinCLIP：人工狀態與視窗；具體視覺 gpt-mobile-winclip
  2. AnomalyCLIP：學到的提示；具體視覺 gpt-mobile-anomalyclip
  3. AnomalyGPT：定位加對話；具體視覺 gpt-mobile-gpt

## 機制、證據與修正

同一工件与取像比較三種工作輸出：WinCLIP人工狀態提示/視窗与可選正常參考；AnomalyCLIP輔助資料學提示；AnomalyGPT合成資料對齊後內建定位/對話。圖中位置皆為機制示意，不宣稱同精度。成本與驗收在正文固定正常/真缺陷、硬體、解析度与漏檢要求。

來源：https://github.com/CASIA-LMC-Lab/AnomalyGPT ; https://arxiv.org/abs/2303.14814 ; https://arxiv.org/abs/2310.18961 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG 對角兩孔金屬板、同位置細痕；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2304。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

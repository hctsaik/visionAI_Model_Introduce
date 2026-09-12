# 正常資料要乾淨，也要涵蓋合理變化

- lesson objective: 訓練、校正與最終測試分開，先查資料來源。
- page type: C — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 已確認正常：用來訓練 → 獨立正常：用來校正 → 正常與真缺陷：留作測試
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 訓練、校正與最終測試分開，先查資料來源。 #FFF4CC
- major visual nodes:
  1. 已確認正常：用來訓練；具體視覺 deep-data-train
  2. 獨立正常：用來校正；具體視覺 deep-data-calibrate
  3. 正常與真缺陷：留作測試；具體視覺 deep-data-test

## 機制、證據與修正

重排手機2章資料分工。已確認正常影像訓練學生/AE；未參與訓練的正常驗證影像建立分位數尺度；另留正常/真缺陷作最終測試。同一工件近似照片不可跨拆，單批資料不能代表全部產品變化。

來源：https://arxiv.org/html/2303.14535v3 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG L形刻痕板、A-01刻字板或三格圓柱托盤，依各圖聲明；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2304。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

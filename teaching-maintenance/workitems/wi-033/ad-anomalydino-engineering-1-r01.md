# AnomalyDINO：固定模型，正常局部存庫

- lesson objective: 免額外訓練，仍要選乾淨正常參考並建立相容庫。
- page type: C — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 少量乾淨正常影像 → 整圖進固定DINOv2 → 局部表示連同來源存庫
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 免額外訓練，仍要選乾淨正常參考並建立相容庫。 #FFF4CC
- major visual nodes:
  1. 少量乾淨正常影像；具體視覺 adino-support
  2. 整圖進固定DINOv2；具體視覺 adino-encode
  3. 局部表示連同來源存庫；具體視覺 adino-memory

## 機制、證據與修正

本課少樣本路徑用固定預訓練DINOv2抽整張影像的局部tokens，保留選定正常樣本的特徵與來源。不是逐張裁片重新訓練，也不是零設定；取像、resize及選用mask/rotation需寫清，未見正常與真缺陷另外留出。

來源：https://arxiv.org/html/2405.14529v2 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG L形刻痕板、A-01刻字板或三格圓柱托盤，依各圖聲明；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

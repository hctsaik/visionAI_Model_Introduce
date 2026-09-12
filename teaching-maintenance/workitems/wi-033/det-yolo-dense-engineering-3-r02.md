# YOLO：去重設定也屬於交付條件
- lesson objective: 模型、前處理與門檻一起固定，再驗漏件。
- page type: C
- primary reading path: 縮放補邊後仍須映回 → 同類候選按門檻去重 → 逐件核對漏框與重複框 → 模型、前處理與門檻一起固定，再驗漏件。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 模型、前處理與門檻一起固定，再驗漏件。 #FFF4CC
- major visual nodes:
  1. 縮放補邊後仍須映回；b4-det-map
  2. 同類候選按門檻去重；b4-yolo-nms
  3. 逐件核對漏框與重複框；b4-det-audit

保留resize/letterbox映射、類別順序、權重、分數與IoU門檻。還原原圖座標後逐件驗漏框、重複與定位誤差，時間包括前後處理。圖中框分數為教學例，不是當前推論。
來源：https://docs.ultralytics.com/models/yolov8/
模式：新精確SVG→1672×941及768×2304PNG；八家族原型已實看通過。三節點、單讀序，保留原有效主線與具體工件身份。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

修訂：末格改為另驗定位偏移與漏框。避免把高重疊同類重複框放在明確NMS去重後，造成同一算例前後矛盾。此處是另一測試例，不是假稱中格輸出失效。原生審查pending。

# AE：用正常影像學壓縮與還原
- lesson objective: 重建提供對照，差異大小還須驗證。
- page type: C
- primary reading path: 同板正常資料與測試分開 → 正常影像教編碼與解碼 → 待測同位置相減形成線索 → 重建提供對照，差異大小還須驗證。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 重建提供對照，差異大小還須驗證。 #FFF4CC
- major visual nodes:
  1. 同板正常資料與測試分開；b5-split-2
  2. 正常影像教編碼與解碼；b5-ae-train
  3. 待測同位置相減形成線索；b5-ae-difference
正常訓練影像作為AE重建目標；測試原圖與重建估計同位置比較。保留40/150/110原算例，位置差異供原圖覆核；原圖不能在推論時被重建結果取代作真值。
來源：https://arxiv.org/html/2103.04257v3
模式：新精確SVG→1672×941/768×2304PNG，原生八家族原型已審；三節點單讀序，保留同件身份與首讀。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

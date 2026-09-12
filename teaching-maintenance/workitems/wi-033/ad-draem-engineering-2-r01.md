# DRAEM：兩種監督，兩張圖判別
- lesson objective: 重建提供對照，判別器學習位置輸出。
- page type: C
- primary reading path: 正常圖與合成mask各教一事 → 待測原圖與重建共同輸入 → 判別網路學可疑位置 → 重建提供對照，判別器學習位置輸出。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 重建提供對照，判別器學習位置輸出。 #FFF4CC
- major visual nodes:
  1. 正常圖與合成mask各教一事；draem-train
  2. 待測原圖與重建共同輸入；draem-pair
  3. 判別網路學可疑位置；draem-seg

訓練以正常圖作重建目標、合成異常mask作判別定位目標；推論待測影像經重建，原影像與重建一起送判別網路。位置圖不是單純像素相減，推論不提供真值mask。保留同板A刮傷p；合成外觀只是訓練工具，仍需真缺陷驗證。
來源：https://arxiv.org/abs/2108.07610
模式：新精確SVG→1672×941/768×2304PNG，非既有點陣編修。八課原首讀桌機已實看：PatchCore無孔板、PaDiM單孔板，其餘左上大孔/右下小孔板及右側刮傷p，保持身份；先機制原型再擴展。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

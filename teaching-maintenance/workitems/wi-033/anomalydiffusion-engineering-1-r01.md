# AnomalyDiffusion：兩區各有資料責任
- lesson objective: 圖與遮罩要逐區一致，才可當訓練樣本。
- page type: C
- primary reading path: 真缺陷教外觀與位置 → 同板雙區條件生成 → 逐區驗證圖與標註 → 圖與遮罩要逐區一致，才可當訓練樣本。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 圖與遮罩要逐區一致，才可當訓練樣本。 #FFF4CC
- major visual nodes:
  1. 真缺陷教外觀與位置
  2. 同板雙區條件生成
  3. 逐區驗證圖與標註
保持原上方雙孔板及大左下小右下兩傷。合成mask是生成條件，不自動成為真值；空mask區或越界都要剔除或修標。
來源：https://arxiv.org/html/2312.05767v1
模式：新SVG→PNG作者機制示意，非本輪模型推論。11課原首讀桌機與V-JEPA/SR手機已實看；夾爪方塊、各課矩形板孔位/缺陷位置保持原身份。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

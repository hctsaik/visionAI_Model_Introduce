# Inpainting：指定內區，保留外部上下文
- lesson objective: 編修影像可以補平，實物狀態並未改變。
- page type: C
- primary reading path: 原圖與可編修遮罩分開保存 → 遮罩內去噪、外部提供上下文 → 檢查接縫與遮罩外變動 → 編修影像可以補平，實物狀態並未改變。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 編修影像可以補平，實物狀態並未改變。 #FFF4CC
- major visual nodes:
  1. 原圖與可編修遮罩分開保存
  2. 遮罩內去噪、外部提供上下文
  3. 檢查接縫與遮罩外變動
同上方雙孔板，下方污點為可編修區。以擴散修補為例，原圖與二值mask定義位置；mask 1為修改的本圖約定，API可能相反。生成內區與外部上下文融合，不保證所有pipeline遮罩外逐像素不變；比較原圖與編修版並另存。真孔被影像填平不代表實體補材。
來源：https://arxiv.org/abs/2201.09865
模式：新SVG→PNG作者機制示意，非本輪模型推論。11課原首讀桌機與V-JEPA/SR手機已實看；夾爪方塊、各課矩形板孔位/缺陷位置保持原身份。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

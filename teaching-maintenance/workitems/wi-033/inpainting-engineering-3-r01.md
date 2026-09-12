# Inpainting：遮罩太緊或太大各有代價
- lesson objective: 按原位置驗接縫、孔位與遮罩外變化。
- page type: C
- primary reading path: 緊遮罩保留邊缘污點 → 大遮罩可能波及鄰近結構 → 保留原圖與mask縮放記錄 → 按原位置驗接縫、孔位與遮罩外變化。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 按原位置驗接縫、孔位與遮罩外變化。 #FFF4CC
- major visual nodes:
  1. 緊遮罩保留邊缘污點
  2. 大遮罩可能波及鄰近結構
  3. 保留原圖與mask縮放記錄
遮罩需包含預期修改區；羽化/膨脹可能改善接縫也擴大修改範圍，實作各異。不能推薦固定像素寬度。
來源：https://arxiv.org/abs/2201.09865
模式：新SVG→PNG作者機制示意，非本輪模型推論。11課原首讀桌機與V-JEPA/SR手機已實看；夾爪方塊、各課矩形板孔位/缺陷位置保持原身份。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

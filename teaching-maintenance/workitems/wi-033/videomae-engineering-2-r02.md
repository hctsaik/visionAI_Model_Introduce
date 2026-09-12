# VideoMAE：遮時空塊，訓練補像素
- lesson objective: 補像素訓練表示，部署另接任務頭。
- page type: C
- primary reading path: 同一格位置跨時間遮蔽 → 可見token編碼再解碼 → 只比被遮位置的像素 → 補像素訓練表示，部署另接任務頭。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 補像素訓練表示，部署另接任務頭。 #FFF4CC
- major visual nodes:
  1. 同一格位置跨時間遮蔽
  2. 可見token編碼再解碼
  3. 只比被遮位置的像素
原版VideoMAE預訓練使用跨時間一致tube mask，通常90–95%高比例；圖中小格只示意對位，不代表實際比例。編碼器處理可見tokens，輕量解碼器加入mask tokens重建像素，以原遮蔽位置像素監督；下游動作分類使用編碼器及另外訓練任務頭，不使用預訓練解碼器。 r01實看修正：解碼重建格上移，與caption保留間距。
來源：https://arxiv.org/abs/2203.12602
模式：新SVG→PNG作者機制示意，非本輪模型推論。11課原首讀桌機與V-JEPA/SR手機已實看；夾爪方塊、各課矩形板孔位/缺陷位置保持原身份。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

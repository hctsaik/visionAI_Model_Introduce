# ConvLSTM：狀態生命週期要明定
- lesson objective: 換影片或相機時，依任務重設記憶。
- page type: C
- primary reading path: 順序、幀距與縮放固定 → 同片續接，換片重設 → 保存狀態與任務頭版本 → 換影片或相機時，依任務重設記憶。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 換影片或相機時，依任務重設記憶。 #FFF4CC
- major visual nodes:
  1. 順序、幀距與縮放固定
  2. 同片續接，換片重設
  3. 保存狀態與任務頭版本
推論狀態初始化/持續/重設需符合訓練方式；不能讓相機A記憶污染B。保存幀距、解析度、網路及任務頭版本，量完整預處理/狀態更新/任務輸出延遲。
來源：https://arxiv.org/abs/1506.04214
模式：新SVG→PNG作者機制示意，非本輪模型推論。11課原首讀桌機與V-JEPA/SR手機已實看；夾爪方塊、各課矩形板孔位/缺陷位置保持原身份。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

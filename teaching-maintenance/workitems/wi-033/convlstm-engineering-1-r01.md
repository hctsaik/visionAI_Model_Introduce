# ConvLSTM：影片狀態接上明確任務
- lesson objective: 時序表示要接任務頭，才有可驗的輸出。
- page type: C
- primary reading path: 連續夾取影片與任務標註 → 卷積記憶接任務頭 → 完整影片驗失敗與延遲 → 時序表示要接任務頭，才有可驗的輸出。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 時序表示要接任務頭，才有可驗的輸出。 #FFF4CC
- major visual nodes:
  1. 連續夾取影片與任務標註
  2. 卷積記憶接任務頭
  3. 完整影片驗失敗與延遲
同夾爪方塊，夾取成功/失敗是另定義標籤；ConvLSTM產生H/C，分類頭需有監督。以整段影片或實體工件切分，不讓相鄰幀跨訓練驗證。
來源：https://arxiv.org/abs/1506.04214
模式：新SVG→PNG作者機制示意，非本輪模型推論。11課原首讀桌機與V-JEPA/SR手機已實看；夾爪方塊、各課矩形板孔位/缺陷位置保持原身份。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

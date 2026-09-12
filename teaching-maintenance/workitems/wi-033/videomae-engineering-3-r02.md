# VideoMAE：token與取樣決定成本
- lesson objective: 減少取樣可省成本，也可能漏掉短事件。
- page type: C
- primary reading path: 固定片長、幀距與裁切 → 時空token數影響注意力 → 同硬體驗事件召回與延遲 → 減少取樣可省成本，也可能漏掉短事件。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 減少取樣可省成本，也可能漏掉短事件。 #FFF4CC
- major visual nodes:
  1. 固定片長、幀距與裁切
  2. 時空token數影響注意力
  3. 同硬體驗事件召回與延遲
全注意力成對數約隨N平方；給定100與200 tokens，其N平方1萬/4萬只是計算量尺度示例，不是實測毫秒。取樣跨距大可能漏短失敗。 r01實看修正：时间刻度及標籤各自定位。
來源：https://arxiv.org/abs/2203.12602
模式：新SVG→PNG作者機制示意，非本輪模型推論。11課原首讀桌機與V-JEPA/SR手機已實看；夾爪方塊、各課矩形板孔位/缺陷位置保持原身份。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

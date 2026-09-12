# DefectFill：適配與挑選成本分開算
- lesson objective: 候選越多，生成與挑選的成本都會累積。
- page type: C
- primary reading path: 保存LoRA與遮罩版本 → 多候選乘上多步採樣 → 挑選仍需真缺陷驗證 → 候選越多，生成與挑選的成本都會累積。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 候選越多，生成與挑選的成本都會累積。 #FFF4CC
- major visual nodes:
  1. 保存LoRA與遮罩版本
  2. 多候選乘上多步採樣
  3. 挑選仍需真缺陷驗證
保存基模/LoRA、文字、mask、種子、採樣與LFS設定。作者例4候選×20步=80去噪呼叫，未含LPIPS與預處理；增加候選不保證增加資料效益。
來源：https://arxiv.org/html/2503.13985v1
模式：新SVG→PNG作者機制示意，非本輪模型推論。11課原首讀桌機與V-JEPA/SR手機已實看；夾爪方塊、各課矩形板孔位/缺陷位置保持原身份。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

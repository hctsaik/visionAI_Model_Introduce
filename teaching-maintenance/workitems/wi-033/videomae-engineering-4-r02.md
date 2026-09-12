# VideoMAE：補得像，不保證分類對
- lesson objective: 像素重建與任務判斷必須分開驗。
- page type: D
- primary reading path: 背景很像，夾取卻失敗 → 平均像素差可能掩小事件 → 依事件留出驗任務頭 → 像素重建與任務判斷必須分開驗。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 像素重建與任務判斷必須分開驗。 #FFF4CC
- major visual nodes:
  1. 背景很像，夾取卻失敗
  2. 平均像素差可能掩小事件
  3. 依事件留出驗任務頭
作者例：100格中99格平方差0、關鍵格100，平均1；平均重建差不能直接當事件成功率。少數關鍵動作需標註與下游驗證。 r01實看修正：99格/1格都明寫平方差，避免把差100誤讀成平方後1萬。
來源：https://arxiv.org/abs/2203.12602
模式：新SVG→PNG作者機制示意，非本輪模型推論。11課原首讀桌機與V-JEPA/SR手機已實看；夾爪方塊、各課矩形板孔位/缺陷位置保持原身份。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

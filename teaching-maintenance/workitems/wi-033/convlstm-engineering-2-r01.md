# ConvLSTM：卷積門控更新空間記憶
- lesson objective: 新影格和舊狀態，逐位置決定記住什麼。
- page type: C
- primary reading path: 新影格與前一步空間狀態 → 門控保留舊值、加入新值 → 新狀態傳到下一時間點 → 新影格和舊狀態，逐位置決定記住什麼。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 新影格和舊狀態，逐位置決定記住什麼。 #FFF4CC
- major visual nodes:
  1. 新影格與前一步空間狀態
  2. 門控保留舊值、加入新值
  3. 新狀態傳到下一時間點
同一夾爪與方塊依序張開、接近、夾住。X_t及H_(t-1)以卷積產生門控，C_t=f_t⊙C_(t-1)+i_t⊙候選；H_t=o_t⊙tanh(C_t)。原論文可有peephole。給定單位置Cprev=.4,f=.5,i=.8,candidate=.5得C=.6；其餘位置另有值。不是每張影格都重新歸零；任务頭另訓練。
來源：https://arxiv.org/abs/1506.04214
模式：新SVG→PNG作者機制示意，非本輪模型推論。11課原首讀桌機與V-JEPA/SR手機已實看；夾爪方塊、各課矩形板孔位/缺陷位置保持原身份。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

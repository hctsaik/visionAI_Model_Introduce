# RT-DETR：query逐步定位各個物件
- lesson objective: 輸出是物件框；一對一匹配只在訓練使用。
- page type: C
- primary reading path: 同PCB有兩個標註框 → 混合編碼後選query起點 → decoder更新後輸出框 → 輸出是物件框；一對一匹配只在訓練使用。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 輸出是物件框；一對一匹配只在訓練使用。 #FFF4CC
- major visual nodes:
  1. 同PCB有兩個標註框；b4-det-labels
  2. 混合編碼後選query起點；b4-rt-encode
  3. decoder更新後輸出框；b4-rt-output

多尺度骨幹特徵經高效混合編碼器，query選擇提供decoder的初始查詢；decoder利用影像特徵更新框與分數。一對一匹配用來訓練責任，不在推論讀標註真值。
來源：https://arxiv.org/abs/2304.08069
模式：新精確SVG→1672×941及768×2304PNG；八家族原型已實看通過。三節點、單讀序，保留原有效主線與具體工件身份。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

# RT-DETR：訓練分工，推論逐步修框
- lesson objective: 一對一匹配是訓練責任，推論仍需篩選與核對。
- page type: C
- primary reading path: 訓練：query對應真值 → 推論：從起點框逐步調整 → 輸出框與分數，沒有NMS → 一對一匹配是訓練責任，推論仍需篩選與核對。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 一對一匹配是訓練責任，推論仍需篩選與核對。 #FFF4CC
- major visual nodes:
  1. 訓練：query對應真值；b4-rt-match
  2. 推論：從起點框逐步調整；b4-rt-refine
  3. 輸出框與分數，沒有NMS；b4-rt-output

训练时一對一匹配讓不同query學不同物件，沒有匹配的query學背景。推論不讀真值：混合編碼與query選擇提供起點，decoder反覆取影像線索更新框。示意q1對A、q2對B、q3未過分數篩選。省去NMS不代表無門檻、零重複或固定更快。
來源：https://arxiv.org/abs/2304.08069
生成模式：新建精確SVG→桌機1672×941、手機768×2304 PNG；不編修既有點陣素材。已實看本批原主線的具體工件，保留PCB雙電阻、L支架與雙圓接頭的身份。各家族先原型實看再擴展其他工程；DINOv2/Gemini主反例另統一同件。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

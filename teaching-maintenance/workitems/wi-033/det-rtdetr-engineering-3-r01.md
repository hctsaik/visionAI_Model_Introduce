# RT-DETR：修框次數也要連品質驗
- lesson objective: 減少decoder層可改成本，不能預設品質不變。
- page type: C
- primary reading path: 固定影像與起點query → 較少或較多次更新 → 交付原圖框並驗錯誤 → 減少decoder層可改成本，不能預設品質不變。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 減少decoder層可改成本，不能預設品質不變。 #FFF4CC
- major visual nodes:
  1. 固定影像與起點query；b4-rt-encode
  2. 較少或較多次更新；b4-rt-depth
  3. 交付原圖框並驗錯誤；b4-det-audit

若使用的實作支援選擇decoder輸出層，可評較少更新的速度/精度取捨；需固定checkpoint、輸入與門檻，並在部署硬體實測。模型輸出映回原圖，不拿query分數當物理定位誤差。
來源：https://arxiv.org/abs/2304.08069
模式：新精確SVG→1672×941及768×2304PNG；八家族原型已實看通過。三節點、單讀序，保留原有效主線與具體工件身份。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

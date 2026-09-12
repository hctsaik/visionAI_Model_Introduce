# PatchCore：縮庫，要連正常覆蓋一起驗
- lesson objective: 庫小可以省資源，漏掉正常變化會有代價。
- page type: C
- primary reading path: 特徵版本必須與庫一致 → 代表數量影響儲存成本 → 漏掉正常代表可能升高距離 → 庫小可以省資源，漏掉正常變化會有代價。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 庫小可以省資源，漏掉正常變化會有代價。 #FFF4CC
- major visual nodes:
  1. 特徵版本必須與庫一致；b5-pc-contract
  2. 代表數量影響儲存成本；b5-pc-cost
  3. 漏掉正常代表可能升高距離；b5-pc-coverage
保存骨幹、層、前處理、聚合、coreset及索引。給定10000×512 float32特徵約20.48MB，留1000代表約2.048MB，未含索引/其他模型成本；只是容量算例，不能宣稱查找快十倍。縮库後用獨立正常與真缺陷驗證。
來源：https://arxiv.org/abs/2106.08265
模式：新精確SVG→1672×941/768×2304PNG，原生八家族原型已審；三節點單讀序，保留同件身份與首讀。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

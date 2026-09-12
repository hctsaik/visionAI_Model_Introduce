# RT-DETR與YOLO：比較工作代價
- lesson objective: 去掉NMS是一項設計，域內結果才決定取捨。
- page type: D
- primary reading path: 共同PCB與逐件驗收 → RT-DETR以query修框 → YOLO以分數整理候選 → 去掉NMS是一項設計，域內結果才決定取捨。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 去掉NMS是一項設計，域內結果才決定取捨。 #FFF4CC
- major visual nodes:
  1. 共同PCB與逐件驗收；b4-det-labels
  2. RT-DETR以query修框；b4-rt-refine
  3. YOLO以分數整理候選；b4-yolo-nms

固定影像、類別、硬體與成本範圍，分別調整候選門檻並比較逐件錯誤。不能把training matching放進推論，也不能以NMS是否存在代替完整延遲測試。
來源：https://arxiv.org/abs/2304.08069
模式：新精確SVG→1672×941及768×2304PNG；八家族原型已實看通過。三節點、單讀序，保留原有效主線與具體工件身份。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

# YOLO與RT-DETR：同一PCB比較交付
- lesson objective: 比較逐件錯誤與完整延遲，不只看有無NMS。
- page type: D
- primary reading path: 同影像、類別與留出件 → YOLO：密集候選與NMS → RT-DETR：query直接交框 → 比較逐件錯誤與完整延遲，不只看有無NMS。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 比較逐件錯誤與完整延遲，不只看有無NMS。 #FFF4CC
- major visual nodes:
  1. 同影像、類別與留出件；b4-det-labels
  2. YOLO：密集候選與NMS；b4-yolo-candidates
  3. RT-DETR：query直接交框；b4-rt-output

共同任務與硬體下，各用相容前處理與已驗證門檻，比較漏框、重複框、定位、記憶體及端到端時間。RT-DETR省NMS不保證本機更快；YOLOv8式作合理可部署基準。
來源：https://docs.ultralytics.com/models/yolov8/
模式：新精確SVG→1672×941及768×2304PNG；八家族原型已實看通過。三節點、單讀序，保留原有效主線與具體工件身份。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

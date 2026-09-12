# YOLOv8式：從有標註的物件學出框
- lesson objective: 框與類別來自訓練，不能用熱點代替框。
- page type: C
- primary reading path: 同PCB逐件標類別與框 → 多尺度特徵產生密集候選 → 去重後交出兩件的位置 → 框與類別來自訓練，不能用熱點代替框。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 框與類別來自訓練，不能用熱點代替框。 #FFF4CC
- major visual nodes:
  1. 同PCB逐件標類別與框；b4-det-labels
  2. 多尺度特徵產生密集候選；b4-yolo-dense
  3. 去重後交出兩件的位置；b4-yolo-output

同PCB電阻A103/B272皆標resistor框；YOLOv8式骨幹與neck融合多尺度特徵，head預測類別與框，候選經門檻及NMS整理。輸出是影像框與類別，不是輪廓或物理尺寸；格位只示意候選位置。
來源：https://docs.ultralytics.com/models/yolov8/
模式：新精確SVG→1672×941及768×2304PNG；八家族原型已實看通過。三節點、單讀序，保留原有效主線與具體工件身份。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

# YOLOv8式：候選重複，按分數去重
- lesson objective: NMS整理重複框，最後仍要回原圖查漏件。
- page type: C
- primary reading path: 同一影像產生四個候選 → 分數排序，再比重疊 → 保留A與B的兩個框 → NMS整理重複框，最後仍要回原圖查漏件。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: NMS整理重複框，最後仍要回原圖查漏件。 #FFF4CC
- major visual nodes:
  1. 同一影像產生四個候選；b4-yolo-candidates
  2. 分數排序，再比重疊；b4-yolo-nms
  3. 保留A與B的兩個框；b4-yolo-output

同一PCB有103與272兩顆電阻；A有三個重複候選，分數0.93/0.87/0.76，B為0.91。教學例採同類別NMS，A的候選IoU超過0.5，因此依分數保留A0.93與B0.91。門檻和分數為給定算例，不是模型推論。這裡限定YOLOv8式密集偵測，不推廣到所有YOLO版本。
來源：https://docs.ultralytics.com/models/yolov8/
生成模式：新建精確SVG→桌機1672×941、手機768×2304 PNG；不編修既有點陣素材。已實看本批原主線的具體工件，保留PCB雙電阻、L支架與雙圓接頭的身份。各家族先原型實看再擴展其他工程；DINOv2/Gemini主反例另統一同件。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

修訂：r01 PNG部分圖形／文字缺畫，SVG節點完整；改用disable-gpu並等字型/500ms繪製。NMS前後尺度一致，YOLOE遮罩覆蓋完整電阻並透明保留料號；DINO遮蔽視圖名稱精確。所有候選仍需逐張原生審查。

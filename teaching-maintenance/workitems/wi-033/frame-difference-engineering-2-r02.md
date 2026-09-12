# Frame Difference：同座標相減，留下雙帶
- lesson objective: 雙帶來自同物件前後位置，不能當兩個物件。
- page type: C
- primary reading path: 同一方件，前後移動一格 → 固定座標，逐格取絕對差 → 只有離開與進入兩帶亮 → 雙帶來自同物件前後位置，不能當兩個物件。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 雙帶來自同物件前後位置，不能當兩個物件。 #FFF4CC
- major visual nodes:
  1. 同一方件，前後移動一格
  2. 固定座標，逐格取絕對差
  3. 只有離開與進入兩帶亮
給定一維橫切灰階：前幀[20,100,100,100,20]，後幀[20,20,100,100,100]，差[0,80,0,0,80]。方件向右移一格，中間重疊不變；兩條亮帶是同一物件的離開與進入，不是兩物件或完整輪廓。教學算例未跑影像演算法。
來源：https://docs.opencv.org/4.x/d2/de8/group__core__array.html
模式：新SVG→PNG；八課原首讀桌機已逐張實看，異常金屬板維持大小孔及右側刮傷，影片維持方件/ID7的L標記。先機制原型再擴展。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

修正r01實際審查：分組相加雙側符號、特徵格與字距、DDAD加噪原件含刮傷、Win同尺寸重疊窗、Byte第二工件、影片背景與文字分離。

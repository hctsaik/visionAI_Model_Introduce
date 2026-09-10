# WI-032 det-dino-detector-engineering-2 r01
- lesson objective: 推論起點來自影像，不是人工真值框。
- page type: C
- primary reading path: 影像提供候選位置 → 內容查詢可學習 → decoder逐層更新 → 工作核對與接手
- major visual nodes:
  1. 影像提供候選位置
  2. 內容查詢可學習
  3. decoder逐層更新
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-21-alignment-to-measurement_v01.png`
- pale-yellow takeaway: #FFF4CC：推論起點來自影像，不是人工真值框。
- generation: 新建精確SVG→PNG，桌機1672×941、手機直向；actual PNG review pending，user approval pending。與首讀PNG分開。
- source: https://arxiv.org/abs/2203.03605
- evidence: DINO mixed query selection以encoder候选提供位置初始化，同时使用可学习内容queries。decoder进一步精修框与类别；与训练专用的GT noisy queries区分，不能把二者画在同一推论路径。

## r02 prototype correction
保持ChArUco同標靶到重投影，不混入金屬工件；相機軸標示與取樣方向分開。原生與頁內pending。
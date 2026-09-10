# WI-032 yolo-world-engineering-2 r01
- lesson objective: 保留影像與文字两條來源，才看得懂比對。
- page type: C
- primary reading path: 視覺多尺度特徵 → 視覺語言路徑 → 區域與詞彙打分 → 工作核對與接手
- major visual nodes:
  1. 視覺多尺度特徵
  2. 視覺語言路徑
  3. 區域與詞彙打分
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-21-alignment-to-measurement_v01.png`
- pale-yellow takeaway: #FFF4CC：保留影像與文字两條來源，才看得懂比對。
- generation: 新建精確SVG→PNG，桌機1672×941、手機直向；actual PNG review pending，user approval pending。與首讀PNG分開。
- source: https://arxiv.org/abs/2401.17270
- evidence: RepVL-PAN相关实现涉及图像与文字交互及多尺度特征融合；此图只表达职责，不伪称完整张量架构。region-text相似关系用于类别评分，边框回归另承担位置。

## r02 prototype correction
保持ChArUco同標靶到重投影，不混入金屬工件；相機軸標示與取樣方向分開。原生與頁內pending。
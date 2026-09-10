# WI-032 det-dino-detector-engineering-3 r01
- lesson objective: 帶噪查詢是訓練輔助，正式推論不用真值。
- page type: C
- primary reading path: 從真值產生帶噪查詢 → 近正樣本還原目標 → 負樣本學無物件 → 工作核對與接手
- major visual nodes:
  1. 從真值產生帶噪查詢
  2. 近正樣本還原目標
  3. 負樣本學無物件
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-21-alignment-to-measurement_v01.png`
- pale-yellow takeaway: #FFF4CC：帶噪查詢是訓練輔助，正式推論不用真值。
- generation: 新建精確SVG→PNG，桌機1672×941、手機直向；actual PNG review pending，user approval pending。與首讀PNG分開。
- source: https://arxiv.org/abs/2203.03605
- evidence: 正负带噪查询以不同噪声范围构建，正样本学习还原对应GT框/类，负样本学习无物件。噪声示意不是实际采样统计；不能将no-object目标解释为原图里真的没有物件。

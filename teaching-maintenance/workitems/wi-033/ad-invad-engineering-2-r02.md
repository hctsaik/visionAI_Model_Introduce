# InvAD：空間條件，逐位置調制
- lesson objective: 同一輸入形成空間條件，控制特徵重建。
- page type: C
- primary reading path: 輸入特徵轉成空間條件 → 同一標準化值，不同調制 → 重建特徵回比原表示 → 同一輸入形成空間條件，控制特徵重建。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 同一輸入形成空間條件，控制特徵重建。 #FFF4CC
- major visual nodes:
  1. 輸入特徵轉成空間條件
  2. 同一標準化值，不同調制
  3. 重建特徵回比原表示
本課為2024 Feature Inversion的InvAD。固定影像編碼器抽特徵，融合/重縮放/風格轉換產生空間條件；由常數特徵起步，SSM以每位置縮放和偏移調制標準化特徵。给定z=3，p縮放2偏移1得7，q縮放0.5偏移0得1.5；這只是SSM局部算例。正常訓練MSE重建，推論餘弦差。SSM是Spatial Style Modulation，不是狀態空間模型。
來源：https://arxiv.org/html/2404.10760v1
模式：新SVG→PNG；八課原首讀桌機已逐張實看，異常金屬板維持大小孔及右側刮傷，影片維持方件/ID7的L標記。先機制原型再擴展。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

修正r01實際審查：分組相加雙側符號、特徵格與字距、DDAD加噪原件含刮傷、Win同尺寸重疊窗、Byte第二工件、影片背景與文字分離。

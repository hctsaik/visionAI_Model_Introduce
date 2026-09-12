# Dinomaly：限制照抄，再分組比較
- lesson objective: 訓練擾動與分組對照，要和推論設定分開。
- page type: C
- primary reading path: 正常特徵，訓練才Dropout → 線性注意力分散聚合 → 多層分組後比較差異 → 訓練擾動與分組對照，要和推論設定分開。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 訓練擾動與分組對照，要和推論設定分開。 #FFF4CC
- major visual nodes:
  1. 正常特徵，訓練才Dropout
  2. 線性注意力分散聚合
  3. 多層分組後比較差異
固定DINOv2，用正常特徵訓練瓶頸及解碼器；訓練MLP Dropout阻止直接照抄，eval關閉。線性注意力降低聚焦相同位置的捷徑；多層按組相加後比較，放寬逐層對應。訓練另降低已重建良好位置的梯度影響。圖中兩組/小格為機制示意，不是固定層號或維度。
來源：https://arxiv.org/html/2405.14325v5
模式：新SVG→PNG；八課原首讀桌機已逐張實看，異常金屬板維持大小孔及右側刮傷，影片維持方件/ID7的L標記。先機制原型再擴展。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

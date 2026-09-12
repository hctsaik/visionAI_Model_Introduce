# Dinomaly：訓練擾動，部署要關閉
- lesson objective: 保存層分組與eval設定，才可重現差異。
- page type: C
- primary reading path: 訓練Dropout，推論關閉 → 保存重建與分組版本 → 按產品驗誤報和漏檢 → 保存層分組與eval設定，才可重現差異。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 保存層分組與eval設定，才可重現差異。 #FFF4CC
- major visual nodes:
  1. 訓練Dropout，推論關閉
  2. 保存重建與分組版本
  3. 按產品驗誤報和漏檢
保存骨幹、MLP、解碼器、使用層和分組、前處理及評分。Dropout只於訓練；放鬆逐層配對與難位置訓練策略不等於省略驗證。部署需eval，變更分組後重新驗。
來源：https://arxiv.org/html/2405.14325v5
模式：新SVG→PNG；八課原首讀桌機已逐張實看，異常金屬板維持大小孔及右側刮傷，影片維持方件/ID7的L標記。先機制原型再擴展。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

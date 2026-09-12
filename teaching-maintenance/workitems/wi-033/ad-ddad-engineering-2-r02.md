# DDAD：原圖引導，每步逐漸去噪
- lesson objective: 恢復估計與原圖的兩種差異，共同提供線索。
- page type: C
- primary reading path: 待測原圖持續提供條件 → 多步去噪形成恢復估計 → 像素與適配特徵各自比較 → 恢復估計與原圖的兩種差異，共同提供線索。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 恢復估計與原圖的兩種差異，共同提供線索。 #FFF4CC
- major visual nodes:
  1. 待測原圖持續提供條件
  2. 多步去噪形成恢復估計
  3. 像素與適配特徵各自比較
正常影像訓練去噪及適配特徵比較；測試以待測原圖引導每步去噪，得到恢復估計R。原A與R同位置的像素差和適配特徵差加權形成位置線索；恢復不是正常真值，圖中三狀態不是固定採樣步數，也不是本輪模型結果。
來源：https://arxiv.org/abs/2305.15956
模式：新SVG→PNG；八課原首讀桌機已逐張實看，異常金屬板維持大小孔及右側刮傷，影片維持方件/ID7的L標記。先機制原型再擴展。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

修正r01實際審查：分組相加雙側符號、特徵格與字距、DDAD加噪原件含刮傷、Win同尺寸重疊窗、Byte第二工件、影片背景與文字分離。

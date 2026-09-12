# RD4AD：从瓶頸反向重建教師特徵
- lesson objective: 學生從教師嵌入重建，逐尺度對照教師。
- page type: C
- primary reading path: 教師多尺度特徵進瓶頸 → 學生由粗到細還原特徵 → 同尺度兩份表示逐一比 → 學生從教師嵌入重建，逐尺度對照教師。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 學生從教師嵌入重建，逐尺度對照教師。 #FFF4CC
- major visual nodes:
  1. 教師多尺度特徵進瓶頸；rd-bottleneck
  2. 學生由粗到細還原特徵；rd-decode
  3. 同尺度兩份表示逐一比；rd-compare

固定教師編碼器抽多尺度特徵，可訓練one-class瓶頸和反向學生解碼器以正常資料學重建。學生輸入是教師嵌入，不是原圖；對應尺度的教師與重建特徵以餘弦差異比較並映回位置。教師高低尺度與學生逆向重建對應清楚，不把輸出說成修復照片。
來源：https://openaccess.thecvf.com/content/CVPR2022/html/Deng_Anomaly_Detection_via_Reverse_Distillation_From_One-Class_Embedding_CVPR_2022_paper.html
模式：新精確SVG→1672×941/768×2304PNG，非既有點陣編修。八課原首讀桌機已實看：PatchCore無孔板、PaDiM單孔板，其餘左上大孔/右下小孔板及右側刮傷p，保持身份；先機制原型再擴展。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

# ResNet：先把整張照片分到已知類別
- lesson objective: 整圖分類要類別標註，細傷位置不會自動交付。
- page type: C — 真實資料變換用C，同條件比較用D。
- primary reading path: 同件照片與類別標註 → 殘差逐步更新影像表示 → 分類頭交出整件分數 → 整圖分類要類別標註，細傷位置不會自動交付。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看具體工件與映射、短句、單黃结論；不沿用多欄小字。
- pale-yellow takeaway: 整圖分類要類別標註，細傷位置不會自動交付。 #FFF4CC
- major visual nodes:
  1. 同件照片與類別標註；證據場景 b3-res-data
  2. 殘差逐步更新影像表示；證據場景 b3-res-residual
  3. 分類頭交出整件分數；證據場景 b3-res-score

## 輸入、方法、輸出與證據
沿用支架完整／缺口兩類工作例。用有標註的整圖訓練分類器，殘差分支學相對輸入的修正；分類頭彙整特徵後交付類別分數，無法直接交付缺口座標。圖中分數是給定示意。
來源：https://arxiv.org/abs/1512.03385。保留WI-031已成立首讀，新工程圖各自有責任。共用圖元只保存相同工件，不用改名熱圖代替各方法。三段箭頭僅表示本頁實際資料或推論關係，D頁無跨方法因果箭頭。
生成模式：新建精確SVG再渲染PNG，桌機1672×941，手機768×2304。分類支架或分割細焊線按本圖身份固定，不冒充本輪模型實測。每模型先工程2原型，實看前不擴展；逐張原生與頁內尺寸另評。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

# SegFormer：先對齊尺度，再融合線索
- lesson objective: 四路特徵共同進解碼器，不是四張遮罩投票。
- page type: C — 真實資料變換用C，同條件比較用D。
- primary reading path: 四尺度的格位各不相同 → 各自投影並上採樣對齊 → 串接融合後逐像素分類 → 四路特徵共同進解碼器，不是四張遮罩投票。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看具體工件與映射、短句、單黃结論；不沿用多欄小字。
- pale-yellow takeaway: 四路特徵共同進解碼器，不是四張遮罩投票。 #FFF4CC
- major visual nodes:
  1. 四尺度的格位各不相同；證據場景 b3-seg-scales
  2. 各自投影並上採樣對齊；證據場景 b3-seg-align
  3. 串接融合後逐像素分類；證據場景 b3-seg-fuse

## 輸入、方法、輸出與證據
四尺度表示先用MLP統一通道維度，再對齊到同一空間尺度，串接後用MLP融合及分類。顯示同一焊線位置在各尺度的對應，不能把四幅彩格當四次獨立模型分割，也不以框取代輸出遮罩。
來源：https://arxiv.org/abs/2105.15203。保留WI-031已成立首讀，新工程圖各自有責任。共用圖元只保存相同工件，不用改名熱圖代替各方法。三段箭頭僅表示本頁實際資料或推論關係，D頁無跨方法因果箭頭。
生成模式：新建精確SVG再渲染PNG，桌機1672×941，手機768×2304。分類支架或分割細焊線按本圖身份固定，不冒充本輪模型實測。每模型先工程2原型，實看前不擴展；逐張原生與頁內尺寸另評。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

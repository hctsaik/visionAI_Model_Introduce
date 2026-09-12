# ResNet：保留輸入，再加上學到的修正
- lesson objective: 同形狀才能逐位置相加；換形狀需先對齊。
- page type: C — 真實資料變換用C，同條件比較用D。
- primary reading path: 輸入x分成兩條路 → 主路學修正F(x) → 對齊後逐項相加 → 同形狀才能逐位置相加；換形狀需先對齊。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看具體工件與映射、短句、單黃结論；不沿用多欄小字。
- pale-yellow takeaway: 同形狀才能逐位置相加；換形狀需先對齊。 #FFF4CC
- major visual nodes:
  1. 輸入x分成兩條路；證據場景 b3-res-split
  2. 主路學修正F(x)；證據場景 b3-res-delta
  3. 對齊後逐項相加；證據場景 b3-res-sum

## 輸入、方法、輸出與證據
用同位置2×2特徵教學例：x=[2,1;0,3]，F(x)=[1,0;2,-1]，相加得到[3,1;2,2]。直通路是輸入特徵而非原圖；形狀不同時需投影或其他對齊。展示殘差核心，啟用函數與其他層於正文說明，不把加法當缺陷消除。
來源：https://arxiv.org/abs/1512.03385。保留WI-031已成立首讀，新工程圖各自有責任。共用圖元只保存相同工件，不用改名熱圖代替各方法。三段箭頭僅表示本頁實際資料或推論關係，D頁無跨方法因果箭頭。
生成模式：新建精確SVG再渲染PNG，桌機1672×941，手機768×2304。分類支架或分割細焊線按本圖身份固定，不冒充本輪模型實測。每模型先工程2原型，實看前不擴展；逐張原生與頁內尺寸另評。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

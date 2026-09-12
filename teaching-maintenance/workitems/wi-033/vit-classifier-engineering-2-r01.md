# ViT：一個位置也會參考其他區塊
- lesson objective: 注意力加權其他表示，位置身份仍要保留。
- page type: C — 真實資料變換用C，同條件比較用D。
- primary reading path: 缺口片與孔邊片各有表示 → 依內容形成參考權重 → 加權更新，再由CLS分類 → 注意力加權其他表示，位置身份仍要保留。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看具體工件與映射、短句、單黃结論；不沿用多欄小字。
- pale-yellow takeaway: 注意力加權其他表示，位置身份仍要保留。 #FFF4CC
- major visual nodes:
  1. 缺口片與孔邊片各有表示；證據場景 b3-vit-query
  2. 依內容形成參考權重；證據場景 b3-vit-attention
  3. 加權更新，再由CLS分類；證據場景 b3-vit-update

## 輸入、方法、輸出與證據
示意某query对兩個value加權0.75和0.25；value [2,0]與[0,4]加權成[1.5,1]。這是單頭簡化算例，實際還含多頭投影、殘差、正規化和MLP。注意力不是物理缺陷機率，也不能用線寬宣稱模型實测解釋。
來源：https://arxiv.org/abs/2010.11929。保留WI-031已成立首讀，新工程圖各自有責任。共用圖元只保存相同工件，不用改名熱圖代替各方法。三段箭頭僅表示本頁實際資料或推論關係，D頁無跨方法因果箭頭。
生成模式：新建精確SVG再渲染PNG，桌機1672×941，手機768×2304。分類支架或分割細焊線按本圖身份固定，不冒充本輪模型實測。每模型先工程2原型，實看前不擴展；逐張原生與頁內尺寸另評。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

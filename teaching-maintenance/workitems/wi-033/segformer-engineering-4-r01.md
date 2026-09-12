# SegFormer與U-Net：共同標註才可比較
- lesson objective: 語意相同、標註一致，再比細節與運算代價。
- page type: D — 真實資料變換用C，同條件比較用D。
- primary reading path: 共同細線影像與真值 → U-Net用對應跳接融合 → SegFormer用四尺度融合 → 語意相同、標註一致，再比細節與運算代價。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看具體工件與映射、短句、單黃结論；不沿用多欄小字。
- pale-yellow takeaway: 語意相同、標註一致，再比細節與運算代價。 #FFF4CC
- major visual nodes:
  1. 共同細線影像與真值；證據場景 b3-unet-line
  2. U-Net用對應跳接融合；證據場景 b3-unet-bridge
  3. SegFormer用四尺度融合；證據場景 b3-seg-align

## 輸入、方法、輸出與證據
同一產品、同一像素標註規則及留出影像，兩候選各用相容前處理。比較細線連通、邊界、換產品適配及完整延遲；圖只展示機制差異，不編造候選熱圖勝負。
來源：https://arxiv.org/abs/2105.15203。保留WI-031已成立首讀，新工程圖各自有責任。共用圖元只保存相同工件，不用改名熱圖代替各方法。三段箭頭僅表示本頁實際資料或推論關係，D頁無跨方法因果箭頭。
生成模式：新建精確SVG再渲染PNG，桌機1672×941，手機768×2304。分類支架或分割細焊線按本圖身份固定，不冒充本輪模型實測。每模型先工程2原型，實看前不擴展；逐張原生與頁內尺寸另評。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

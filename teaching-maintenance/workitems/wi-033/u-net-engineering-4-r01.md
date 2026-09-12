# U-Net：看起來像一條線，仍可能斷一格
- lesson objective: 同件檢查細線連通，不能只看大區域重疊。
- page type: D — 真實資料變換用C，同條件比較用D。
- primary reading path: 同一焊線跨過細縫 → 候選遮罩在細處斷裂 → 核對連通與邊界，再選型 → 同件檢查細線連通，不能只看大區域重疊。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看具體工件與映射、短句、單黃结論；不沿用多欄小字。
- pale-yellow takeaway: 同件檢查細線連通，不能只看大區域重疊。 #FFF4CC
- major visual nodes:
  1. 同一焊線跨過細縫；證據場景 b3-unet-line
  2. 候選遮罩在細處斷裂；證據場景 b3-unet-gap
  3. 核對連通與邊界，再選型；證據場景 b3-unet-boundary

## 輸入、方法、輸出與證據
同一細線的真值和示意候選只在中央窄處不同；大區域重疊可能掩蓋斷線。固定標註規則與解析度，比較U-Net和多尺度Transformer候選的邊界、连通、錯分及延遲，不把單一IoU排名當唯一決策。
來源：https://arxiv.org/abs/1505.04597。保留WI-031已成立首讀，新工程圖各自有責任。共用圖元只保存相同工件，不用改名熱圖代替各方法。三段箭頭僅表示本頁實際資料或推論關係，D頁無跨方法因果箭頭。
生成模式：新建精確SVG再渲染PNG，桌機1672×941，手機768×2304。分類支架或分割細焊線按本圖身份固定，不冒充本輪模型實測。每模型先工程2原型，實看前不擴展；逐張原生與頁內尺寸另評。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

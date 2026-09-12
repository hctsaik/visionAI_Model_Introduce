# 關鍵點與分割：要具名位置還是整片區域
- lesson objective: 按交付選標註：具名點、輪廓與姿態各有責任。
- page type: D — 真實資料變換用C，同條件比較用D。
- primary reading path: 同一支架工作需求 → 關鍵點：A/B/C具名座標 → 分割：逐像素物件區域 → 按交付選標註：具名點、輪廓與姿態各有責任。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看具體工件與映射、短句、單黃结論；不沿用多欄小字。
- pale-yellow takeaway: 按交付選標註：具名點、輪廓與姿態各有責任。 #FFF4CC
- major visual nodes:
  1. 同一支架工作需求；證據場景 b3-kpt-data
  2. 關鍵點：A/B/C具名座標；證據場景 b3-kpt-scope
  3. 分割：逐像素物件區域；證據場景 b3-kpt-mask

## 輸入、方法、輸出與證據
固定同一支架影像，若要孔中心身份對應可評關鍵點；若要整片邊界可評分割。兩者都不單獨保證物理姿態或毫米尺寸；按可見性、標註成本、幾何誤差與後續用途比較。
來源：https://arxiv.org/abs/1703.06870。保留WI-031已成立首讀，新工程圖各自有責任。共用圖元只保存相同工件，不用改名熱圖代替各方法。三段箭頭僅表示本頁實際資料或推論關係，D頁無跨方法因果箭頭。
生成模式：新建精確SVG再渲染PNG，桌機1672×941，手機768×2304。分類支架或分割細焊線按本圖身份固定，不冒充本輪模型實測。每模型先工程2原型，實看前不擴展；逐張原生與頁內尺寸另評。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

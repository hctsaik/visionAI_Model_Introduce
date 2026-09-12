# ResNet：分類結果要連回原圖與標籤
- lesson objective: 保存類別映射與前處理，換批次後重驗誤判。
- page type: C — 真實資料變換用C，同條件比較用D。
- primary reading path: 鎖定裁切與類別映射 → 彙整表示再讀出分數 → 回原圖核对錯分樣本 → 保存類別映射與前處理，換批次後重驗誤判。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看具體工件與映射、短句、單黃结論；不沿用多欄小字。
- pale-yellow takeaway: 保存類別映射與前處理，換批次後重驗誤判。 #FFF4CC
- major visual nodes:
  1. 鎖定裁切與類別映射；證據場景 b3-res-contract
  2. 彙整表示再讀出分數；證據場景 b3-res-pool
  3. 回原圖核对錯分樣本；證據場景 b3-res-review

## 輸入、方法、輸出與證據
推論固定裁切、resize、標準化、權重與類別順序。分類頭使用彙整特徵，不把可視化特徵圖當缺陷位置。保存分數與原圖，分批次驗漏判與誤判；全域平均會弱化某些細小線索，是否漏判仍需資料驗證。
來源：https://arxiv.org/abs/1512.03385。保留WI-031已成立首讀，新工程圖各自有責任。共用圖元只保存相同工件，不用改名熱圖代替各方法。三段箭頭僅表示本頁實際資料或推論關係，D頁無跨方法因果箭頭。
生成模式：新建精確SVG再渲染PNG，桌機1672×941，手機768×2304。分類支架或分割細焊線按本圖身份固定，不冒充本輪模型實測。每模型先工程2原型，實看前不擴展；逐張原生與頁內尺寸另評。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

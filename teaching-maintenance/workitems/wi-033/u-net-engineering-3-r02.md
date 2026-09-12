# U-Net：像素位置先映回，再談尺寸
- lesson objective: 記錄resize與裁切，像素遮罩不能直接當毫米。
- page type: C — 真實資料變換用C，同條件比較用D。
- primary reading path: 裁切與縮放都留下映射 → 遮罩回到原圖同一位置 → 輪廓核對後才另接量測 → 記錄resize與裁切，像素遮罩不能直接當毫米。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看具體工件與映射、短句、單黃结論；不沿用多欄小字。
- pale-yellow takeaway: 記錄resize與裁切，像素遮罩不能直接當毫米。 #FFF4CC
- major visual nodes:
  1. 裁切與縮放都留下映射；證據場景 b3-unet-contract
  2. 遮罩回到原圖同一位置；證據場景 b3-unet-map
  3. 輪廓核對後才另接量測；證據場景 b3-unet-review

## 輸入、方法、輸出與證據
保存ROI、resize比例、padding及類別映射，將預測映回原图再核對細線斷裂、孔洞與邊界誤差。量測另需相機校正及誤差驗證；IoU高不保證細線連通或毫米誤差達標。
來源：https://arxiv.org/abs/1505.04597。保留WI-031已成立首讀，新工程圖各自有責任。共用圖元只保存相同工件，不用改名熱圖代替各方法。三段箭頭僅表示本頁實際資料或推論關係，D頁無跨方法因果箭頭。
生成模式：新建精確SVG再渲染PNG，桌機1672×941，手機768×2304。分類支架或分割細焊線按本圖身份固定，不冒充本輪模型實測。每模型先工程2原型，實看前不擴展；逐張原生與頁內尺寸另評。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

手機實看修訂：標題刮傷名稱同步；比較具體指ConvNeXt逐通道卷積，不泛稱所有卷積；ROI標籤框加寬，乙標籤與邊框分離。待重新實看。

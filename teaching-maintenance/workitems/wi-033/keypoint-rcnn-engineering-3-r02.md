# Keypoint R-CNN：遮住的點也可能被猜出
- lesson objective: 估計位置與可見證據分開，可信度不足要覆核。
- page type: C — 真實資料變換用C，同條件比較用D。
- primary reading path: 遮擋覆住同件的C孔 → 模型仍可能給C的估計 → 原圖核對後才接幾何求解 → 估計位置與可見證據分開，可信度不足要覆核。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看具體工件與映射、短句、單黃结論；不沿用多欄小字。
- pale-yellow takeaway: 估計位置與可見證據分開，可信度不足要覆核。 #FFF4CC
- major visual nodes:
  1. 遮擋覆住同件的C孔；證據場景 b3-kpt-occluded
  2. 模型仍可能給C的估計；證據場景 b3-kpt-estimate
  3. 原圖核對後才接幾何求解；證據場景 b3-kpt-review

## 輸入、方法、輸出與證據
不可把每個輸出座標當已見到真實點。可見性標註與模型回傳的score/visibility欄位需按實作解讀；保留原圖、具名座標與分數，遮擋點單獨評估。接PnP另需K、畸變、3D對應與足够非退化點。
來源：https://arxiv.org/abs/1703.06870。保留WI-031已成立首讀，新工程圖各自有責任。共用圖元只保存相同工件，不用改名熱圖代替各方法。三段箭頭僅表示本頁實際資料或推論關係，D頁無跨方法因果箭頭。
生成模式：新建精確SVG再渲染PNG，桌機1672×941，手機768×2304。分類支架或分割細焊線按本圖身份固定，不冒充本輪模型實測。每模型先工程2原型，實看前不擴展；逐張原生與頁內尺寸另評。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

修訂r02：原生實看後縮小U-Net輸出避免壓字；粗取樣改同件格線位置，不能人工挖斷當取樣實測；YOLO去重前後同顯示尺度；移除無目標箭頭；ViT刮傷名稱與圖一致。新候選待實看，未整合。

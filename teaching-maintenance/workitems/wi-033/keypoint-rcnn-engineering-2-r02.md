# Keypoint R-CNN：ROI座標要映回原圖
- lesson objective: 同一個點沿ROI與原圖映射，A/B/C不能互換。
- page type: C — 真實資料變換用C，同條件比較用D。
- primary reading path: 原圖框出同一件支架 → ROI內各點分開解碼 → 依框位與尺度映回原圖 → 同一個點沿ROI與原圖映射，A/B/C不能互換。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看具體工件與映射、短句、單黃结論；不沿用多欄小字。
- pale-yellow takeaway: 同一個點沿ROI與原圖映射，A/B/C不能互換。 #FFF4CC
- major visual nodes:
  1. 原圖框出同一件支架；證據場景 b3-kpt-roi
  2. ROI內各點分開解碼；證據場景 b3-kpt-decode
  3. 依框位與尺度映回原圖；證據場景 b3-kpt-map

## 輸入、方法、輸出與證據
ROIAlign取得對齊特徵，關鍵點頭分別產生K個位置heatmaps。圖用連續ROI座標示意x=x0+u*w、y=y0+v*h；實作還要遵循格心、resize與padding約定。A點[0.275,0.3125]在框原點[100,50]、寬高[200,160]時映到[155,100]。
來源：https://arxiv.org/abs/1703.06870。保留WI-031已成立首讀，新工程圖各自有責任。共用圖元只保存相同工件，不用改名熱圖代替各方法。三段箭頭僅表示本頁實際資料或推論關係，D頁無跨方法因果箭頭。
生成模式：新建精確SVG再渲染PNG，桌機1672×941，手機768×2304。分類支架或分割細焊線按本圖身份固定，不冒充本輪模型實測。每模型先工程2原型，實看前不擴展；逐張原生與頁內尺寸另評。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

修訂r02：修正圖文相碰及結果箭頭；YOLO兩原型改同件代數例P1=甲+乙、P2=甲−乙，係數各為[½,½]與[½,−½]。關鍵點框與A位置使用同座標算例。ConvNeXt增加鄰域與通道可追算變化；以上均需重新實看。

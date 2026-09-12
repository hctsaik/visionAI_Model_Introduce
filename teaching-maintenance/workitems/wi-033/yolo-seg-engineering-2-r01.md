# YOLO-Seg：共用原型，每件用不同係數
- lesson objective: 原型乘各件係數，再依物件框取回遮罩。
- page type: C — 真實資料變換用C，同條件比較用D。
- primary reading path: 共享特徵產生原型圖 → 每個候選各有係數 → 組合、裁框、映回影像 → 原型乘各件係數，再依物件框取回遮罩。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看具體工件與映射、短句、單黃结論；不沿用多欄小字。
- pale-yellow takeaway: 原型乘各件係數，再依物件框取回遮罩。 #FFF4CC
- major visual nodes:
  1. 共享特徵產生原型圖；證據場景 b3-yseg-proto
  2. 每個候選各有係數；證據場景 b3-yseg-coef
  3. 組合、裁框、映回影像；證據場景 b3-yseg-combine

## 輸入、方法、輸出與證據
檢測頭預測框/類別和每個候選的mask coefficients；Proto支路產生共享basis maps。保留候選的係數線性組合原型，经相應後處理與裁框映回。兩原型是簡化代數例，實際通道數與後處理依所用版本；不能把每張原型直接叫某件物體。
來源：https://docs.ultralytics.com/reference/nn/modules/head/#ultralytics.nn.modules.head.Segment。保留WI-031已成立首讀，新工程圖各自有責任。共用圖元只保存相同工件，不用改名熱圖代替各方法。三段箭頭僅表示本頁實際資料或推論關係，D頁無跨方法因果箭頭。
生成模式：新建精確SVG再渲染PNG，桌機1672×941，手機768×2304。分類支架或分割細焊線按本圖身份固定，不冒充本輪模型實測。每模型先工程2原型，實看前不擴展；逐張原生與頁內尺寸另評。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

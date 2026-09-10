# WI-032 yolo-world-engineering-3 r01
- lesson objective: 快取向量不等於已完成模型重參數化。
- page type: C
- primary reading path: 固定詞彙先編碼 → 實作可做重參數化 → 換詞彙就更新產物 → 工作核對與接手
- major visual nodes:
  1. 固定詞彙先編碼
  2. 實作可做重參數化
  3. 換詞彙就更新產物
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-21-alignment-to-measurement_v01.png`
- pale-yellow takeaway: #FFF4CC：快取向量不等於已完成模型重參數化。
- generation: 新建精確SVG→PNG，桌機1672×941、手機直向；actual PNG review pending，user approval pending。與首讀PNG分開。
- source: https://arxiv.org/abs/2401.17270
- evidence: 官方reparameterize文档区分快取文本特征和进一步转换部署结构。采用时应记录版本、词汇、编码器及部署产物；换词汇需要对应更新，不只改前端显示文字。

## r02 prototype correction
保持ChArUco同標靶到重投影，不混入金屬工件；相機軸標示與取樣方向分開。原生與頁內pending。
## r03 審查後修正
棋盤交點修正為兩黑兩白；ECC影像座標僅2D，插值用四像素數值示例；SIFT幾何圖避免重複，新增候選外點與8方向；LightGlue修剪移除後續邊，注意力點不共線；DINO位置初始化與decoder更新分開，正負訓練目標不串成時序；YOLO-World矩陣列／欄與文字引導權重有可核對意義。原生與頁內pending，user approval pending。
# WI-032 lightglue-engineering-4 r01
- lesson objective: 看不見或分不出的部分，不能要求模型猜對。
- page type: D
- primary reading path: 少重疊 → 對稱與重複 → 補資料再比較 → 工作核對與接手
- major visual nodes:
  1. 少重疊
  2. 對稱與重複
  3. 補資料再比較
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-21-alignment-to-measurement_v01.png`
- pale-yellow takeaway: #FFF4CC：看不見或分不出的部分，不能要求模型猜對。
- generation: 新建精確SVG→PNG，桌機1672×941、手機直向；actual PNG review pending，user approval pending。與首讀PNG分開。
- source: https://github.com/cvg/LightGlue
- evidence: 用相同影像與独立几何证据比较传统matcher及LightGlue；无法观测的独特细节不是换配对器一定能补回。优先核对重叠、纹理与遮挡，再决定是否换算法。

## r02 prototype correction
保持ChArUco同標靶到重投影，不混入金屬工件；相機軸標示與取樣方向分開。原生與頁內pending。
## r03 審查後修正
棋盤交點修正為兩黑兩白；ECC影像座標僅2D，插值用四像素數值示例；SIFT幾何圖避免重複，新增候選外點與8方向；LightGlue修剪移除後續邊，注意力點不共線；DINO位置初始化與decoder更新分開，正負訓練目標不串成時序；YOLO-World矩陣列／欄與文字引導權重有可核對意義。原生與頁內pending，user approval pending。
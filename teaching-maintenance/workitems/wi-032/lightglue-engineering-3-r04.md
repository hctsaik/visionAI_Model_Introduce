# WI-032 lightglue-engineering-3 r01
- lesson objective: 自適應不是每張圖都更快的保證。
- page type: C
- primary reading path: 深度：可能提早停止 → 寬度：修剪部分點 → 量完整處理鏈 → 工作核對與接手
- major visual nodes:
  1. 深度：可能提早停止
  2. 寬度：修剪部分點
  3. 量完整處理鏈
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-21-alignment-to-measurement_v01.png`
- pale-yellow takeaway: #FFF4CC：自適應不是每張圖都更快的保證。
- generation: 新建精確SVG→PNG，桌機1672×941、手機直向；actual PNG review pending，user approval pending。與首讀PNG分開。
- source: https://github.com/cvg/LightGlue
- evidence: 自適應深度依信心提前停止，寬度修剪部分低可匹配點以減少後續計算；實際門檻與后端实现有关。完整时间包含extractor、資料搬移、matcher及几何估计，不能只用名称宣称更快。

## r02 prototype correction
保持ChArUco同標靶到重投影，不混入金屬工件；相機軸標示與取樣方向分開。原生與頁內pending。
## r03 審查後修正
棋盤交點修正為兩黑兩白；ECC影像座標僅2D，插值用四像素數值示例；SIFT幾何圖避免重複，新增候選外點與8方向；LightGlue修剪移除後續邊，注意力點不共線；DINO位置初始化與decoder更新分開，正負訓練目標不串成時序；YOLO-World矩陣列／欄與文字引導權重有可核對意義。原生與頁內pending，user approval pending。
## r04 最終候選
已依實圖修正對應、2D座標、八方向、正負分支及有標籤矩陣。桌機與手機原生／實頁核對仍需完成。來源：https://github.com/cvg/LightGlue
自適應深度依信心提前停止，寬度修剪部分低可匹配點以減少後續計算；實際門檻與后端實現有關。完整時間包含extractor、資料搬移、matcher及幾何估計，不能只用名稱宣稱更快。

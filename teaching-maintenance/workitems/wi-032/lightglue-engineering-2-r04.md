# WI-032 lightglue-engineering-2 r01
- lesson objective: 不是每個點都必須硬配到另一張圖。
- page type: C
- primary reading path: 圖內注意力 → 跨圖注意力 → 可匹配性與分配 → 工作核對與接手
- major visual nodes:
  1. 圖內注意力
  2. 跨圖注意力
  3. 可匹配性與分配
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-21-alignment-to-measurement_v01.png`
- pale-yellow takeaway: #FFF4CC：不是每個點都必須硬配到另一張圖。
- generation: 新建精確SVG→PNG，桌機1672×941、手機直向；actual PNG review pending，user approval pending。與首讀PNG分開。
- source: https://github.com/cvg/LightGlue
- evidence: LightGlue交替使用self-/cross-attention更新局部表示，再結合匹配分配與matchability；一些点没有可靠对应时允许不匹配。图为机制示意，无真实注意力或信心数值。

## r02 prototype correction
保持ChArUco同標靶到重投影，不混入金屬工件；相機軸標示與取樣方向分開。原生與頁內pending。
## r03 審查後修正
棋盤交點修正為兩黑兩白；ECC影像座標僅2D，插值用四像素數值示例；SIFT幾何圖避免重複，新增候選外點與8方向；LightGlue修剪移除後續邊，注意力點不共線；DINO位置初始化與decoder更新分開，正負訓練目標不串成時序；YOLO-World矩陣列／欄與文字引導權重有可核對意義。原生與頁內pending，user approval pending。
## r04 最終候選
已依實圖修正對應、2D座標、八方向、正負分支及有標籤矩陣。桌機與手機原生／實頁核對仍需完成。來源：https://github.com/cvg/LightGlue
LightGlue交替使用self-/cross-attention更新局部表示，再結合匹配分配與matchability；一些點沒有可靠對應時允許不匹配。圖為機制示意，無真實注意力或信心數值。

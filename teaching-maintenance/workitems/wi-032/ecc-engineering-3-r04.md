# WI-032 ecc-engineering-3 r01
- lesson objective: 先寫清楚映射方向，再決定反矩陣與取樣設定。
- page type: C
- primary reading path: 定義座標與方向 → 明確定義W → 取樣旗標須相符 → 工作核對與接手
- major visual nodes:
  1. 定義座標與方向
  2. 明確定義W
  3. 取樣旗標須相符
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-21-alignment-to-measurement_v01.png`
- pale-yellow takeaway: #FFF4CC：先寫清楚映射方向，再決定反矩陣與取樣設定。
- generation: 新建精確SVG→PNG，桌機1672×941、手機直向；actual PNG review pending，user approval pending。與首讀PNG分開。
- source: https://docs.opencv.org/4.13.0/dc/d6b/group__video__track.html
- evidence: OpenCV findTransformECC的warp常配warpAffine/warpPerspective及WARP_INVERSE_MAP，把input重採樣至template座標。若交換角色或自行取逆矩陣，旗標也必須一致；用已知平移點做驗證，不憑圖看起來像就認為方向正確。

## r02 prototype correction
保持ChArUco同標靶到重投影，不混入金屬工件；相機軸標示與取樣方向分開。原生與頁內pending。
## r03 審查後修正
棋盤交點修正為兩黑兩白；ECC影像座標僅2D，插值用四像素數值示例；SIFT幾何圖避免重複，新增候選外點與8方向；LightGlue修剪移除後續邊，注意力點不共線；DINO位置初始化與decoder更新分開，正負訓練目標不串成時序；YOLO-World矩陣列／欄與文字引導權重有可核對意義。原生與頁內pending，user approval pending。
## r04 最終候選
已依實圖修正對應、2D座標、八方向、正負分支及有標籤矩陣。桌機與手機原生／實頁核對仍需完成。來源：https://docs.opencv.org/4.13.0/dc/d6b/group__video__track.html
OpenCV findTransformECC的warp常配warpAffine/warpPerspective及WARP_INVERSE_MAP，把input重採樣至template座標。若交換角色或自行取逆矩陣，旗標也必須一致；用已知平移點做驗證，不憑圖看起來像就認為方向正確。

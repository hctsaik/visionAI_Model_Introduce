# WI-032 ecc-engineering-4 r01
- lesson objective: 用獨立幾何與完整失敗成本決定是否採用。
- page type: D
- primary reading path: 同身份地標核對 → 遠起點或遮擋 → 保留失敗案例 → 工作核對與接手
- major visual nodes:
  1. 同身份地標核對
  2. 遠起點或遮擋
  3. 保留失敗案例
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-21-alignment-to-measurement_v01.png`
- pale-yellow takeaway: #FFF4CC：用獨立幾何與完整失敗成本決定是否採用。
- generation: 新建精確SVG→PNG，桌機1672×941、手機直向；actual PNG review pending，user approval pending。與首讀PNG分開。
- source: https://docs.opencv.org/4.13.0/dc/d6b/group__video__track.html
- evidence: 既有32/12平移及遠起點失敗案例保留在舊正式圖及來源紀錄，並非本輪重新執行。這張圖補說如何核對孔位身份、外框與失敗處理，不用單一相關值放行。

## r02 prototype correction
保持ChArUco同標靶到重投影，不混入金屬工件；相機軸標示與取樣方向分開。原生與頁內pending。
## r03 審查後修正
棋盤交點修正為兩黑兩白；ECC影像座標僅2D，插值用四像素數值示例；SIFT幾何圖避免重複，新增候選外點與8方向；LightGlue修剪移除後續邊，注意力點不共線；DINO位置初始化與decoder更新分開，正負訓練目標不串成時序；YOLO-World矩陣列／欄與文字引導權重有可核對意義。原生與頁內pending，user approval pending。
## r04 最終候選
已依實圖修正對應、2D座標、八方向、正負分支及有標籤矩陣。桌機與手機原生／實頁核對仍需完成。來源：https://docs.opencv.org/4.13.0/dc/d6b/group__video__track.html
既有32/12平移及遠起點失敗案例保留在舊正式圖及來源紀錄，並非本輪重新執行。這張圖補說如何核對孔位身份、外框與失敗處理，不用單一相關值放行。

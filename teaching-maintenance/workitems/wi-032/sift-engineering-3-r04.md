# WI-032 sift-engineering-3 r01
- lesson objective: 數量、正確性與分布要一起看。
- page type: C
- primary reading path: 正確且分散的點對 → 幾何估計與內點 → 獨立位置再核對 → 工作核對與接手
- major visual nodes:
  1. 正確且分散的點對
  2. 幾何估計與內點
  3. 獨立位置再核對
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-21-alignment-to-measurement_v01.png`
- pale-yellow takeaway: #FFF4CC：數量、正確性與分布要一起看。
- generation: 新建精確SVG→PNG，桌機1672×941、手機直向；actual PNG review pending，user approval pending。與首讀PNG分開。
- source: https://docs.opencv.org/4.13.0/da/df5/tutorial_py_sift_intro.html
- evidence: 四組合適的非退化平面對應可求單應；大量共線或錯配點仍可能不可用。需要按工作選模型，RANSAC筛选内点后仍看空间覆盖与独立地标误差。

## r02 prototype correction
保持ChArUco同標靶到重投影，不混入金屬工件；相機軸標示與取樣方向分開。原生與頁內pending。
## r03 審查後修正
棋盤交點修正為兩黑兩白；ECC影像座標僅2D，插值用四像素數值示例；SIFT幾何圖避免重複，新增候選外點與8方向；LightGlue修剪移除後續邊，注意力點不共線；DINO位置初始化與decoder更新分開，正負訓練目標不串成時序；YOLO-World矩陣列／欄與文字引導權重有可核對意義。原生與頁內pending，user approval pending。
## r04 最終候選
已依實圖修正對應、2D座標、八方向、正負分支及有標籤矩陣。桌機與手機原生／實頁核對仍需完成。來源：https://docs.opencv.org/4.13.0/da/df5/tutorial_py_sift_intro.html
四組合適的非退化平面對應可求單應；大量共線或錯配點仍可能不可用。需要按工作選模型，RANSAC篩選內點后仍看空間覆蓋與獨立地標誤差。

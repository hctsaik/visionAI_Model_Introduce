# WI-032 sift-engineering-4 r01
- lesson objective: 匹配失敗與幾何模型不適用，要分開診斷。
- page type: D
- primary reading path: 同場景不同深度 → 點對可能仍正確 → 改選幾何假設 → 工作核對與接手
- major visual nodes:
  1. 同場景不同深度
  2. 點對可能仍正確
  3. 改選幾何假設
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-21-alignment-to-measurement_v01.png`
- pale-yellow takeaway: #FFF4CC：匹配失敗與幾何模型不適用，要分開診斷。
- generation: 新建精確SVG→PNG，桌機1672×941、手機直向；actual PNG review pending，user approval pending。與首讀PNG分開。
- source: https://docs.opencv.org/4.13.0/da/df5/tutorial_py_sift_intro.html
- evidence: SIFT可提供局部對應，但場景有非平面視差時，單一單應未必能同時對齊全部深度。不能把此時的殘差全部解釋成特徵錯配，需检查模型适用范围。

## r02 prototype correction
保持ChArUco同標靶到重投影，不混入金屬工件；相機軸標示與取樣方向分開。原生與頁內pending。
## r03 審查後修正
棋盤交點修正為兩黑兩白；ECC影像座標僅2D，插值用四像素數值示例；SIFT幾何圖避免重複，新增候選外點與8方向；LightGlue修剪移除後續邊，注意力點不共線；DINO位置初始化與decoder更新分開，正負訓練目標不串成時序；YOLO-World矩陣列／欄與文字引導權重有可核對意義。原生與頁內pending，user approval pending。
## r04 最終候選
已依實圖修正對應、2D座標、八方向、正負分支及有標籤矩陣。桌機與手機原生／實頁核對仍需完成。來源：https://docs.opencv.org/4.13.0/da/df5/tutorial_py_sift_intro.html
SIFT可提供局部對應，但場景有非平面視差時，單一單應未必能同時對齊全部深度。不能把此時的殘差全部解釋成特徵錯配，需檢查模型適用范圍。

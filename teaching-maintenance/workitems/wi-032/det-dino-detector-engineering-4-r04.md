# WI-032 det-dino-detector-engineering-4 r01
- lesson objective: 按類別變更與資料成本選方法，不按模型新舊。
- page type: D
- primary reading path: 原本固定類別 → 新類別與新場景 → 用錯誤與成本比較 → 工作核對與接手
- major visual nodes:
  1. 原本固定類別
  2. 新類別與新場景
  3. 用錯誤與成本比較
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-21-alignment-to-measurement_v01.png`
- pale-yellow takeaway: #FFF4CC：按類別變更與資料成本選方法，不按模型新舊。
- generation: 新建精確SVG→PNG，桌機1672×941、手機直向；actual PNG review pending，user approval pending。與首讀PNG分開。
- source: https://arxiv.org/abs/2203.03605
- evidence: 与YOLO-World开放词汇路线相比，DINO固定类别通常需相应模型头与监督训练/微调。二者都需现场独立数据验证；改变标注或阈值也应重新量测错误与完整成本。

## r02 prototype correction
保持ChArUco同標靶到重投影，不混入金屬工件；相機軸標示與取樣方向分開。原生與頁內pending。
## r03 審查後修正
棋盤交點修正為兩黑兩白；ECC影像座標僅2D，插值用四像素數值示例；SIFT幾何圖避免重複，新增候選外點與8方向；LightGlue修剪移除後續邊，注意力點不共線；DINO位置初始化與decoder更新分開，正負訓練目標不串成時序；YOLO-World矩陣列／欄與文字引導權重有可核對意義。原生與頁內pending，user approval pending。
## r04 最終候選
已依實圖修正對應、2D座標、八方向、正負分支及有標籤矩陣。桌機與手機原生／實頁核對仍需完成。來源：https://arxiv.org/abs/2203.03605
與YOLO-World開放詞匯路線相比，DINO固定類別通常需相應模型頭與監督訓練/微調。二者都需現場獨立數據驗證；改變標注或閾值也應重新量測錯誤與完整成本。

# WI-032 yolo-world-engineering-1 r01
- lesson objective: 詞彙可變，但現場辨識能力仍需驗證。
- page type: C
- primary reading path: 文字詞彙與預訓練 → 區域與文字表示 → 交付詞彙對應框 → 工作核對與接手
- major visual nodes:
  1. 文字詞彙與預訓練
  2. 區域與文字表示
  3. 交付詞彙對應框
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-21-alignment-to-measurement_v01.png`
- pale-yellow takeaway: #FFF4CC：詞彙可變，但現場辨識能力仍需驗證。
- generation: 新建精確SVG→PNG，桌機1672×941、手機直向；actual PNG review pending，user approval pending。與首讀PNG分開。
- source: https://arxiv.org/abs/2401.17270
- evidence: YOLO-World利用预训练视觉语言表示进行开放词汇检测，文字不是直接搜索像素的规则。提示类别的粒度、视觉可见性和训练分布都会影响现场结果。

## r02 prototype correction
保持ChArUco同標靶到重投影，不混入金屬工件；相機軸標示與取樣方向分開。原生與頁內pending。
## r03 審查後修正
棋盤交點修正為兩黑兩白；ECC影像座標僅2D，插值用四像素數值示例；SIFT幾何圖避免重複，新增候選外點與8方向；LightGlue修剪移除後續邊，注意力點不共線；DINO位置初始化與decoder更新分開，正負訓練目標不串成時序；YOLO-World矩陣列／欄與文字引導權重有可核對意義。原生與頁內pending，user approval pending。
## r04 最終候選
已依實圖修正對應、2D座標、八方向、正負分支及有標籤矩陣。桌機與手機原生／實頁核對仍需完成。來源：https://arxiv.org/abs/2401.17270
YOLO-World利用預訓練視覺語言表示進行開放詞匯檢測，文字不是直接搜索像素的規則。提示類別的粒度、視覺可見性和訓練分布都會影響現場結果。

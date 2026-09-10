# WI-032 det-dino-detector-engineering-1 r01
- lesson objective: DINO detector是偵測器，不是DINOv2特徵骨幹。
- page type: C
- primary reading path: 逐件框與類別 → 查詢更新框與類別 → 交付候選物件 → 工作核對與接手
- major visual nodes:
  1. 逐件框與類別
  2. 查詢更新框與類別
  3. 交付候選物件
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-21-alignment-to-measurement_v01.png`
- pale-yellow takeaway: #FFF4CC：DINO detector是偵測器，不是DINOv2特徵骨幹。
- generation: 新建精確SVG→PNG，桌機1672×941、手機直向；actual PNG review pending，user approval pending。與首讀PNG分開。
- source: https://arxiv.org/abs/2203.03605
- evidence: 本课讨论DINO DETR系检测器。模型交付物件框、类别与分数，而像素分割、毫米尺寸及业务计数规则需其他流程；训练/验证分组应避免同工件或连续影像泄漏。

## r02 prototype correction
保持ChArUco同標靶到重投影，不混入金屬工件；相機軸標示與取樣方向分開。原生與頁內pending。
## r03 審查後修正
棋盤交點修正為兩黑兩白；ECC影像座標僅2D，插值用四像素數值示例；SIFT幾何圖避免重複，新增候選外點與8方向；LightGlue修剪移除後續邊，注意力點不共線；DINO位置初始化與decoder更新分開，正負訓練目標不串成時序；YOLO-World矩陣列／欄與文字引導權重有可核對意義。原生與頁內pending，user approval pending。
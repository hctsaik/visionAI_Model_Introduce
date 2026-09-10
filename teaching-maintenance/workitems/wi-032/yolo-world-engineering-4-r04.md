# WI-032 yolo-world-engineering-4 r01
- lesson objective: 先定義要框物件還是判缺陷，再選後續流程。
- page type: D
- primary reading path: 詞彙描述目標 → 輸出仍有觀測限制 → 接專用檢查與覆核 → 工作核對與接手
- major visual nodes:
  1. 詞彙描述目標
  2. 輸出仍有觀測限制
  3. 接專用檢查與覆核
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-21-alignment-to-measurement_v01.png`
- pale-yellow takeaway: #FFF4CC：先定義要框物件還是判缺陷，再選後續流程。
- generation: 新建精確SVG→PNG，桌機1672×941、手機直向；actual PNG review pending，user approval pending。與首讀PNG分開。
- source: https://arxiv.org/abs/2401.17270
- evidence: 物件框不证明细裂纹或缺陷存在，也不直接给尺寸或根因。若任务要求细缺陷，应先检查取像像素和光照，再准备适合缺陷任务的标注与验证流程。

## r02 prototype correction
保持ChArUco同標靶到重投影，不混入金屬工件；相機軸標示與取樣方向分開。原生與頁內pending。
## r03 審查後修正
棋盤交點修正為兩黑兩白；ECC影像座標僅2D，插值用四像素數值示例；SIFT幾何圖避免重複，新增候選外點與8方向；LightGlue修剪移除後續邊，注意力點不共線；DINO位置初始化與decoder更新分開，正負訓練目標不串成時序；YOLO-World矩陣列／欄與文字引導權重有可核對意義。原生與頁內pending，user approval pending。
## r04 最終候選
已依實圖修正對應、2D座標、八方向、正負分支及有標籤矩陣。桌機與手機原生／實頁核對仍需完成。來源：https://arxiv.org/abs/2401.17270
物件框不證明細裂紋或缺陷存在，也不直接給尺寸或根因。若任務要求細缺陷，應先檢查取像像素和光照，再準備適合缺陷任務的標注與驗證流程。

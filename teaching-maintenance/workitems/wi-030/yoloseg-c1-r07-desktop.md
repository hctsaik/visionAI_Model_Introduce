# WI-030 YOLO-Seg：每個物件，都有自己的遮罩 — desktop
- lesson objective: 每件一張遮罩；漏檢與重疊仍要逐件核對。
- page type: C
- primary reading path: 先有實例標註 → 共享底圖，各自組合 → 分開每一件 → 核對輸出與工作條件
- major visual nodes:
  1. 先有實例標註
  2. 共享底圖，各自組合
  3. 分開每一件
- named guide-conformant reference page: teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png
- pale-yellow takeaway: #FFF4CC：每件一張遮罩；漏檢與重疊仍要逐件核對。
- source: https://github.com/ultralytics/ultralytics/blob/v8.3.0/ultralytics/nn/modules/head.py
- generation: built-in imagegen；教學示意非模型實測。
- actual PNG review: reviewed；原生與936/328px證據見prototype-review.md；這是候選選定，不是使用者核准。
- user approval: pending

## 版本與生成意圖
產物：yoloseg-c1-r07-desktop.png。原型生成前已有同故事r01及逐版preflight，本檔彙整實際選用版本，保留歷史。

{"prompt":"只修改中區藍色線路，其他完全不變。共享原型P上方那個向上小三角箭頭是錯的：把該三角和它的短豎線完整擦掉，P盒上方留白。改從P盒左邊已有的藍色垂直線（共享特徵往上那條）往右拉一条短水平箭頭，箭頭朝右，直接接入『共享原型P』框左邊緣，高度在P標題左側。这样共享特徵从左側餵入P，頂部線只餵入右邊A係數。保留P和係數向下進加權組合的線。請不要再畫P往上的任何箭頭。","reference":"yoloseg-c1-r06-desktop.png"}


# WI-030 YOLO-Seg：每個物件，都有自己的遮罩 — mobile
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
產物：yoloseg-c1-r06-mobile.png。原型生成前已有同故事r01及逐版preflight，本檔彙整實際選用版本，保留歷史。

{"prompt":"只刪三個主區標題前的序號『1.』『2.』『3.』，保留先有實例標註、共享底圖各自組合、分開每一件。把中區特徵立方旁『共享特徵(Backbone)』改『共享影像特徵』，立方不是骨幹本身。所有照片箭頭兩支加權流程和结論保持原樣，不重排不加其他文字。","reference":"yoloseg-c1-r05-mobile.png"}


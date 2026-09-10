# WI-030 AnomalyDINO：用預訓練特徵找正常先例 — mobile
- lesson objective: 免額外微調，仍要正常參考與工作驗證。
- page type: C
- primary reading path: 正常圖建立參考 → 待測圖找相似特徵 → 距離回到位置 → 核對輸出與工作條件
- major visual nodes:
  1. 正常圖建立參考
  2. 待測圖找相似特徵
  3. 距離回到位置
- named guide-conformant reference page: teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png
- pale-yellow takeaway: #FFF4CC：免額外微調，仍要正常參考與工作驗證。
- source: https://arxiv.org/abs/2405.14529
- generation: built-in imagegen；教學示意非模型實測。
- actual PNG review: reviewed；原生與936/328px證據見prototype-review.md；這是候選選定，不是使用者核准。
- user approval: pending

## 版本與生成意圖
產物：dino-c1-r05-mobile.png。原型生成前已有同故事r01及逐版preflight，本檔彙整實際選用版本，保留歷史。

{"prompt":"刪除第一區右側兩張孔口／平面照片，以及『孔特徵』『平面裁片特徵』標籤；照片不能冒充特徵。刪除右側豎分隔線，將現有左側完整正常板→DINOv2→正常特徵藍色方塊上下流程移到第一區正中央。第一區的『區塊帶有全圖情境』短標可保留。第二第三區一律不改；不要重新新增裁片或圖。底部空白角落補小字『教學示意』，唯一黃色結論保持完整。"}


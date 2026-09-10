# WI-030 AnomalyDINO：用預訓練特徵找正常先例 — desktop
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
產物：dino-c1-r03-desktop.png。原型生成前已有同故事r01及逐版preflight，本檔彙整實際選用版本，保留歷史。

{"prompt":"只重排中央比較小框消除文字疊圖。『平面特徵：相似』下方藍／橘兩列，每列左方保留短標『參考』『待測』，色塊一律在文字右邊。『刮傷特徵：落差大』下方也同樣兩列短標，刪目前和蓝色块重疊的『庫中參考』長字。用短連線／長括號表示相似和落差，不能擋文字。其他圖及位置、全圖進DINOv2、底部結論不變。","reference":"dino-c1-r02-desktop.png"}


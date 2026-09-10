# WI-030 SegFormer：融合不同尺度，判斷每個位置 — desktop
- lesson objective: 多尺度提供上下文；細小邊界仍要靠實際資料驗證。
- page type: C
- primary reading path: 整體與局部都重要 → 多尺度特徵融合 → 逐像素類別 → 核對輸出與工作條件
- major visual nodes:
  1. 整體與局部都重要
  2. 多尺度特徵融合
  3. 逐像素類別
- named guide-conformant reference page: teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png
- pale-yellow takeaway: #FFF4CC：多尺度提供上下文；細小邊界仍要靠實際資料驗證。
- source: https://arxiv.org/abs/2105.15203
- generation: built-in imagegen；教學示意非模型實測。
- actual PNG review: reviewed；原生與936/328px證據見prototype-review.md；這是候選選定，不是使用者核准。
- user approval: pending

## 版本與生成意圖
產物：segformer-c1-r02-desktop.png。原型生成前已有同故事r01及逐版preflight，本檔彙整實際選用版本，保留歷史。

{"prompt":"中央資料路徑改清楚：完整原圖先箭頭進一個『階層Transformer編碼器』抽象模型框，再由該編碼器產生四種尺度特徵（細到粗1/4、1/8、1/16、1/32），每個尺度單獨箭頭送『對齊尺度＋輕量MLP融合』。不要讓原圖直接只進1/32而其他特徵無來源。可刪現在第二列重複同色細節放大圖，放大真正四尺度特徵；整合後→像素遮罩。左訓練配對與右同焊縫區域保留，原圖不是特徵，四尺度箭頭不串錯。","reference":"segformer-c1-r01-desktop.png"}


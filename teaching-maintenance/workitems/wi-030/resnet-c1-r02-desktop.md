# WI-030 ResNet：保留原有線索，再學需要的修正 — desktop
- lesson objective: 殘差幫助深層訓練；分類答案仍限於學過的類別。
- page type: C
- primary reading path: 已知類別工件 → 殘差兩路相加 → 分類後接工作 → 核對輸出與工作條件
- major visual nodes:
  1. 已知類別工件
  2. 殘差兩路相加
  3. 分類後接工作
- named guide-conformant reference page: teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png
- pale-yellow takeaway: #FFF4CC：殘差幫助深層訓練；分類答案仍限於學過的類別。
- source: https://arxiv.org/abs/1512.03385
- generation: built-in imagegen；教學示意非模型實測。
- actual PNG review: reviewed；原生與936/328px證據見prototype-review.md；這是候選選定，不是使用者核准。
- user approval: pending

## 版本與生成意圖
產物：resnet-c1-r02-desktop.png。原型生成前已有同故事r01及逐版preflight，本檔彙整實際選用版本，保留歷史。

{"prompt":"精準修正：輸入內六角照片的箭頭必須先連到中央左上『特徵示意(x)』，不可直接連下方卷積。請刪除目前跨區大箭頭，改一條細藍線由輸入照片右側沿中央頂部折到x。x分兩路一直接加號一兩次卷積再加號，保留。分類區刪掉三個無數值條狀分數，只保留三類候選及內六角橘框。料盒內六角不要畫螺帽，畫跟輸入一樣內六角螺絲。其它版面不變。","reference":"resnet-c1-r01-desktop.png"}


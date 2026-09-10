# WI-030 ViT：把影像變成可互相參照的區塊 — desktop
- lesson objective: 區塊互相提供線索；注意力不是缺陷位置真值。
- page type: C
- primary reading path: 影像切塊 → 帶位置的特徵互看 → 匯整成類別 → 核對輸出與工作條件
- major visual nodes:
  1. 影像切塊
  2. 帶位置的特徵互看
  3. 匯整成類別
- named guide-conformant reference page: teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png
- pale-yellow takeaway: #FFF4CC：區塊互相提供線索；注意力不是缺陷位置真值。
- source: https://arxiv.org/abs/2010.11929
- generation: built-in imagegen；教學示意非模型實測。
- actual PNG review: reviewed；原生與936/328px證據見prototype-review.md；這是候選選定，不是使用者核准。
- user approval: pending

## 版本與生成意圖
產物：vit-c1-r02-desktop.png。原型生成前已有同故事r01及逐版preflight，本檔彙整實際選用版本，保留歷史。

{"prompt":"右區改清楚原始ViT分類頭：把『所有區塊token（含位置）』那一排改成『匯整的分類表示』一個含多色訊息的CLS token，接分類頭，三類候選保留。可註『經區塊互看更新』。刪右下『模型從區塊特徵中學習形狀與外觀，而非輸入螺絲的輪廓或邊緣』整段，這句不準確。中央關係和左區來源保持，無額外數值。","reference":"vit-c1-r01-desktop.png"}


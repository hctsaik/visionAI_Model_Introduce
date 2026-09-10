# WI-030 ViT：把影像變成可互相參照的區塊 — mobile
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
產物：vit-c1-r02-mobile.png。原型生成前已有同故事r01及逐版preflight，本檔彙整實際選用版本，保留歷史。

{"prompt":"獨立重排成768x2048手機直向三區，不把橫圖縮窄。第一區同一內六角螺絲切塊編碼＋位置，代表頭部／孔口／背景三token，可圖像上方tokens下方；第二區抽象tokens不同粗線互相參照，示意一個更新token帶別處線索，註非解釋熱圖；第三區經注意力更新的CLS分類表示→分類頭→三類候選內六角選中。刪冗長段落，保留必要短標和預訓練＋工作標註。328px繁體粗字清楚，無序號徽章，唯一#FFF4CC燈泡原結論，教學示意。","reference":"vit-c1-r02-desktop.png"}


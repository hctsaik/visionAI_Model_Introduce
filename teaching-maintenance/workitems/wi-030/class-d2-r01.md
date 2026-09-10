# WI-030 模型認的是工件，還是拍攝背景？
- lesson objective: 分類要學工件差異；換背景測一次，才知道能否搬到現場。
- page type: D — 依具體因果／條件差異教工作判斷。
- primary reading path: 訓練資料偏了 → 換背景露出問題 → 交叉取樣再驗 → 依輸出界線核對原圖與工作條件
- major visual nodes:
  1. 訓練資料偏了
  2. 換背景露出問題
  3. 交叉取樣再驗
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看材質與細框；內容另設計。
- pale-yellow takeaway: #FFF4CC：分類要學工件差異；換背景測一次，才知道能否搬到現場。
- source: https://arxiv.org/abs/1512.03385
- evidence: AI生成教學示意，非模型推論與效能實測。
- generation: built-in imagegen，桌面16:9，手機獨立重排；actual PNG review pending；user approval pending。

## Visual brief
金屬十字螺絲全放藍墊、內六角全放橘墊作訓練偏差例。第二區同一十字螺絲放橘墊，分類候選錯成「內六角？」但實物頭始終十字；不要把照片變內六角。第三區兩類螺絲都在藍和橘背景的四個清楚小物件，大標「兩類都跨背景」，另封存未見批次資料夾「獨立測試」，不能重複訓練照片冒充獨立測試。

## Validation intent
查來源定位、同物件不變量、訓練／推論兩路、輸出責任；原生與936/328px實看，按v1.0逐圖分項，不能以正文補分。

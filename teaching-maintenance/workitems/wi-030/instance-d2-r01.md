# WI-030 兩件靠在一起，遮罩可能合錯或漏掉
- lesson objective: 先查漏檢與分件，再把遮罩交給計數或抓取。
- page type: D — 依具體因果／條件差異教工作判斷。
- primary reading path: 兩件原物體 → 輸出只剩一件 → 逐件回查 → 依輸出界線核對原圖與工作條件
- major visual nodes:
  1. 兩件原物體
  2. 輸出只剩一件
  3. 逐件回查
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看材質與細框；內容另設計。
- pale-yellow takeaway: #FFF4CC：先查漏檢與分件，再把遮罩交給計數或抓取。
- source: https://github.com/ultralytics/ultralytics/blob/v8.3.0/ultralytics/nn/modules/head.py
- evidence: AI生成教學示意，非模型推論與效能實測。
- generation: built-in imagegen，桌面16:9，手機獨立重排；actual PNG review pending；user approval pending。

## Visual brief
兩個金屬墊圈在輸送帶略重疊，始終保留兩個可見孔，右件遮住左件小邊。中區同原圖只左件得到藍框與藍預測mask、右件沒有，標「漏掉右件」；不能把原物件畫消失。第三區原圖兩件仍在，橘框只是人工覆核提示標「人工核對區」，示意收集重疊標註與改善視角，沒有第二模型自動修好。

## Validation intent
查來源定位、同物件不變量、訓練／推論兩路、輸出責任；原生與936/328px實看，按v1.0逐圖分項，不能以正文補分。

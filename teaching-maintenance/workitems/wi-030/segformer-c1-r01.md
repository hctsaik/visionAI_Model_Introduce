# WI-030 SegFormer：融合不同尺度，判斷每個位置
- lesson objective: 多尺度提供上下文；細小邊界仍要靠實際資料驗證。
- page type: C — 依具體因果／條件差異教工作判斷。
- primary reading path: 整體與局部都重要 → 多尺度特徵融合 → 逐像素類別 → 依輸出界線核對原圖與工作條件
- major visual nodes:
  1. 整體與局部都重要
  2. 多尺度特徵融合
  3. 逐像素類別
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看材質與細框；內容另設計。
- pale-yellow takeaway: #FFF4CC：多尺度提供上下文；細小邊界仍要靠實際資料驗證。
- source: https://arxiv.org/abs/2105.15203
- evidence: AI生成教學示意，非模型推論與效能實測。
- generation: built-in imagegen，桌面16:9，手機獨立重排；actual PNG review pending；user approval pending。

## Visual brief
同一金屬工件有大面積灰底和彎曲深色焊縫，背景有相似細紋。第一區輸入與人工焊縫標註分清。第二區階層Transformer輸出四尺度特徵網格，畫一組大的細節圖和較小整體圖，中間兩尺度以明確小格但不密密文字；每尺度獨立箭頭送輕量融合頭，放到同尺度再合併，標「不同尺度一起看」「輕量融合」。第三區原圖上的焊縫區域候選，旁邊同類像素同色的小圖例，標「語意區域，不是物件編號」「回看細邊界」。沒有物件框、mask數量/實例ID、快準排名。

## Validation intent
查來源定位、同物件不變量、訓練／推論兩路、輸出責任；原生與936/328px實看，按v1.0逐圖分項，不能以正文補分。

# WI-030 AnomalyDINO：用預訓練特徵找正常先例
- lesson objective: 免額外微調，仍要正常參考與工作驗證。
- page type: C — 依具體因果／條件差異教工作判斷。
- primary reading path: 正常圖建立參考 → 待測圖找相似特徵 → 距離回到位置 → 依輸出界線核對原圖與工作條件
- major visual nodes:
  1. 正常圖建立參考
  2. 待測圖找相似特徵
  3. 距離回到位置
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看材質與細框；內容另設計。
- pale-yellow takeaway: #FFF4CC：免額外微調，仍要正常參考與工作驗證。
- source: https://arxiv.org/abs/2405.14529
- evidence: AI生成教學示意，非模型推論與效能實測。
- generation: built-in imagegen，桌面16:9，手機獨立重排；actual PNG review pending；user approval pending。

## Visual brief
正常金屬方板只有中央圓孔無缺陷。第一區完整正常板進有鎖的DINOv2，產生藍色token小方塊，旁邊用來源框連回圓孔和平面，不把裁片當模型輸入；token進正常參考庫。第二區同板右下多一道刮傷，整圖進同DINOv2，橘色待測token與庫中藍色token兩列對照；一組平面相似短連線，一組刮傷落差大長括號，標「局部帶有全圖情境」「不限同座標查找」。第三區同板右下熱區，放大仍同刮傷，標「回原圖核對」「少樣本仍須涵蓋正常變化」。參考不是文字提示，不畫chatbot、訓練更新。

## Validation intent
查來源定位、同物件不變量、訓練／推論兩路、輸出責任；原生與936/328px實看，按v1.0逐圖分項，不能以正文補分。

# WI-030 YOLO-Seg：每個物件，都有自己的遮罩
- lesson objective: 每件一張遮罩；漏檢與重疊仍要逐件核對。
- page type: C — 依具體因果／條件差異教工作判斷。
- primary reading path: 先有實例標註 → 共享底圖，各自組合 → 分開每一件 → 依輸出界線核對原圖與工作條件
- major visual nodes:
  1. 先有實例標註
  2. 共享底圖，各自組合
  3. 分開每一件
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看材質與細框；內容另設計。
- pale-yellow takeaway: #FFF4CC：每件一張遮罩；漏檢與重疊仍要逐件核對。
- source: https://github.com/ultralytics/ultralytics/blob/v8.3.0/ultralytics/nn/modules/head.py
- evidence: AI生成教學示意，非模型推論與效能實測。
- generation: built-in imagegen，桌面16:9，手機獨立重排；actual PNG review pending；user approval pending。

## Visual brief
俯視輸送帶上兩個相同金屬墊圈，不重疊、一左一右，孔不能填實。第一區原圖與每實例人工遮罩藍A橘B小配對，標「實例標註」。第二區YOLOv8-seg共同特徵分成共享原型遮罩（抽象灰階分布不是完整物件），和兩個偵測框各自一組係數；原型加A係數→A遮罩，原型加B係數→B遮罩，清楚兩支平行不串接；裁回各自框，標「原型＋每件係數」。第三區同兩墊圈分別藍橘透明覆蓋、中央孔仍空，圖例A/B是實例非類別，標「分件後再計數」「以YOLOv8-seg機制為例」。

## Validation intent
查來源定位、同物件不變量、訓練／推論兩路、輸出責任；原生與936/328px實看，按v1.0逐圖分項，不能以正文補分。

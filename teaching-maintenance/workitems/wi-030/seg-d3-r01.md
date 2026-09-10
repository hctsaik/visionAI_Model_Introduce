# WI-030 要同類區域，還是每件各一張遮罩？
- lesson objective: 先決定輸出責任；同類區域不等於每件身分。
- page type: D — 依具體因果／條件差異教工作判斷。
- primary reading path: 共同兩件输入 → 語意分割 → 實例分割 → 依輸出界線核對原圖與工作條件
- major visual nodes:
  1. 共同兩件输入
  2. 語意分割
  3. 實例分割
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看材質與細框；內容另設計。
- pale-yellow takeaway: #FFF4CC：先決定輸出責任；同類區域不等於每件身分。
- source: https://arxiv.org/abs/1505.04597
- evidence: AI生成教學示意，非模型推論與效能實測。
- generation: built-in imagegen，桌面16:9，手機獨立重排；actual PNG review pending；user approval pending。

## Visual brief
兩個同類金屬墊圈左右不重疊，原圖孔清楚。分兩平行分支不串接：U-Net／SegFormer語意分割兩個環形區同藍色，標「同類像素同色」；YOLO-Seg兩件分藍橘不同mask，標「同類也分開每件」。所有孔留空、相對位置不改。底部標「區域標註」與「實例標註」資料不同，量測仍另校正。

## Validation intent
查來源定位、同物件不變量、訓練／推論兩路、輸出責任；原生與936/328px實看，按v1.0逐圖分項，不能以正文補分。

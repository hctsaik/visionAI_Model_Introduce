# WI-030 ResNet：保留原有線索，再學需要的修正
- lesson objective: 殘差幫助深層訓練；分類答案仍限於學過的類別。
- page type: C — 依具體因果／條件差異教工作判斷。
- primary reading path: 已知類別工件 → 殘差兩路相加 → 分類後接工作 → 依輸出界線核對原圖與工作條件
- major visual nodes:
  1. 已知類別工件
  2. 殘差兩路相加
  3. 分類後接工作
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看材質與細框；內容另設計。
- pale-yellow takeaway: #FFF4CC：殘差幫助深層訓練；分類答案仍限於學過的類別。
- source: https://arxiv.org/abs/1512.03385
- evidence: AI生成教學示意，非模型推論與效能實測。
- generation: built-in imagegen，桌面16:9，手機獨立重排；actual PNG review pending；user approval pending。

## Visual brief
固定俯視金屬螺絲三類範例，十字頭、一字頭、內六角頭，每類一張帶短標籤；中央主輸入一顆內六角螺絲。第二區來源影像先轉藍色特徵格x；從x分兩路，一路藍線直達加號，另一經兩個卷積操作畫出局部特徵改變F，兩路在加號合併成更新特徵；標「直接路徑」「學修正」「特徵示意」。不得把旁路畫成原始照片疊回照片，不用訓練曲線。第三區更新特徵逐層匯整到分類頭，三類可見候選卡中內六角被框起，旁邊分類料盒圖「交給分流規則」。小註「需類別標註訓練」。

## Validation intent
查來源定位、同物件不變量、訓練／推論兩路、輸出責任；原生與936/328px實看，按v1.0逐圖分項，不能以正文補分。

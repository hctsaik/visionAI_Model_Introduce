# WI-030 EfficientAD：學正常回應，再查兩種落差
- lesson objective: 局部差異與整體關係一起查；快不等於免驗證。
- page type: C — 依具體因果／條件差異教工作判斷。
- primary reading path: 正常資料教學生 → 局部與全域兩路 → 校準後回查 → 依輸出界線核對原圖與工作條件
- major visual nodes:
  1. 正常資料教學生
  2. 局部與全域兩路
  3. 校準後回查
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看材質與細框；內容另設計。
- pale-yellow takeaway: #FFF4CC：局部差異與整體關係一起查；快不等於免驗證。
- source: https://arxiv.org/abs/2303.14535
- evidence: AI生成教學示意，非模型推論與效能實測。
- generation: built-in imagegen，桌面16:9，手機獨立重排；actual PNG review pending；user approval pending。

## Visual brief
工作例灰色托盤固定三槽，正常有三顆相同金屬圓柱，待測中間缺一顆且右柱有污點。第一區正常完整托盤進固定教師PDN藍色網格、学生橘色網格，正常訓練迴圈只更新學生；正常兩特徵逐步接近。第二區待測完整托盤分兩個獨立路徑：局部教師與學生特徵差（污點位置有橘落差）；全域autoencoder從完整表示重建教師特徵，再與學生另一輸出比較（中間空槽有落差）。autoencoder输出畫抽象特徵網格，不畫正常補圖。第三區兩落差圖各調整色階後合併候選熱圖，原圖保留空槽與污點，標「校準兩路尺度」「回看缺位與污點」。小註「完整方法示意／非實测」，無速度數字。

## Validation intent
查來源定位、同物件不變量、訓練／推論兩路、輸出責任；原生與936/328px實看，按v1.0逐圖分項，不能以正文補分。

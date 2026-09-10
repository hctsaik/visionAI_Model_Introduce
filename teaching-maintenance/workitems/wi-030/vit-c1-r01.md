# WI-030 ViT：把影像變成可互相參照的區塊
- lesson objective: 區塊互相提供線索；注意力不是缺陷位置真值。
- page type: C — 依具體因果／條件差異教工作判斷。
- primary reading path: 影像切塊 → 帶位置的特徵互看 → 匯整成類別 → 依輸出界線核對原圖與工作條件
- major visual nodes:
  1. 影像切塊
  2. 帶位置的特徵互看
  3. 匯整成類別
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看材質與細框；內容另設計。
- pale-yellow takeaway: #FFF4CC：區塊互相提供線索；注意力不是缺陷位置真值。
- source: https://arxiv.org/abs/2010.11929
- evidence: AI生成教學示意，非模型推論與效能實測。
- generation: built-in imagegen，桌面16:9，手機獨立重排；actual PNG review pending；user approval pending。

## Visual brief
同一內六角螺絲俯視輸入，清楚切成3x3示意區塊，不聲稱固定九token。第一區完整螺絲圖有淡格線，三個代表來源塊（頭部、孔口、背景）用細線到各自抽象token不同符號，標「區塊編碼＋位置」。第二區token間有不同粗細連線，頭部token從孔口等token加權取訊息後顏色組成改變，標「互相參照」「示意關係，非解釋熱圖」；位置標記保留。第三區匯整token交分類頭，內六角類別候選；旁邊小標「預訓練＋工作標註」「不直接給輪廓」。不要用一堆文字框冒充attention，線粗不同但無假數字。

## Validation intent
查來源定位、同物件不變量、訓練／推論兩路、輸出責任；原生與936/328px實看，按v1.0逐圖分項，不能以正文補分。

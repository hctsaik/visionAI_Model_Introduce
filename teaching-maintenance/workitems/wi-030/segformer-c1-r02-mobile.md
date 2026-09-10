# WI-030 SegFormer：融合不同尺度，判斷每個位置 — mobile
- lesson objective: 多尺度提供上下文；細小邊界仍要靠實際資料驗證。
- page type: C
- primary reading path: 整體與局部都重要 → 多尺度特徵融合 → 逐像素類別 → 核對輸出與工作條件
- major visual nodes:
  1. 整體與局部都重要
  2. 多尺度特徵融合
  3. 逐像素類別
- named guide-conformant reference page: teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png
- pale-yellow takeaway: #FFF4CC：多尺度提供上下文；細小邊界仍要靠實際資料驗證。
- source: https://arxiv.org/abs/2105.15203
- generation: built-in imagegen；教學示意非模型實測。
- actual PNG review: reviewed；原生與936/328px證據見prototype-review.md；這是候選選定，不是使用者核准。
- user approval: pending

## 版本與生成意圖
產物：segformer-c1-r02-mobile.png。原型生成前已有同故事r01及逐版preflight，本檔彙整實際選用版本，保留歷史。

{"prompt":"依附圖重製手機教學PNG。畫布768x2304，三個主區上下依序、每區佔整個寬度。不是把橫版拉長！繁體中文字每個必要標籤至少32px，328px顯示能讀。白底淡藍標題薄框，工件材質和幾何保持。無編號。底部唯一#FFF4CC燈泡結論保留附圖文字，四邊留安全邊距。獨立手機重排為上中下三個全寬區：整體與局部、多尺度融合、逐像素輸出。中區編碼器→四尺度特徵→融合→遮罩，四尺度可橫排但短標籤，其餘上下排。 教學示意非實測。","reference":"segformer-c1-r02-desktop.png"}


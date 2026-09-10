# WI-030 ConvNeXt：用現代卷積整理局部與通道線索 — mobile
- lesson objective: 仍是卷積模型；是否值得換，要連品質與成本一起測。
- page type: C
- primary reading path: 有標註的工件 → 空間與通道分工 → 分類與成本核對 → 核對輸出與工作條件
- major visual nodes:
  1. 有標註的工件
  2. 空間與通道分工
  3. 分類與成本核對
- named guide-conformant reference page: teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png
- pale-yellow takeaway: #FFF4CC：仍是卷積模型；是否值得換，要連品質與成本一起測。
- source: https://arxiv.org/abs/2201.03545
- generation: built-in imagegen；教學示意非模型實測。
- actual PNG review: reviewed；原生與936/328px證據見prototype-review.md；這是候選選定，不是使用者核准。
- user approval: pending

## 版本與生成意圖
產物：convnext-c1-r02-mobile.png。原型生成前已有同故事r01及逐版preflight，本檔彙整實際選用版本，保留歷史。

{"prompt":"獨立重排為768x2048手機三區。第一區三已知螺絲類別、內六角待測。第二區從照片建立特徵x再分两通道A/B，兩張同大小特徵平面用相同大視窗各看鄰域，標『各通道看鄰域』，再混合通道；從x旁路到混合後加號，不能原照片直接加。两平面都抽象特徵，不分空間vs通道兩種。第三區內六角候選與同資料測錯誤／耗時／記憶體。各區內盡量上下排，繁體中文粗體328px能讀，白底淡藍細框無序號，唯一#FFF4CC燈泡結論保留。","reference":"convnext-c1-r02-desktop.png"}


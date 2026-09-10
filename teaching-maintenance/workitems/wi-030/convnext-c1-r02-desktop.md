# WI-030 ConvNeXt：用現代卷積整理局部與通道線索 — desktop
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
產物：convnext-c1-r02-desktop.png。原型生成前已有同故事r01及逐版preflight，本檔彙整實際選用版本，保留歷史。

{"prompt":"修正兩點：中央兩張特徵平面應各標『通道A（示意）』『通道B（示意）』，刪『空間特徵如邊緣形狀』『通道特徵如材質紋理』錯誤二分。照片先經『特徵x』小堆疊再分到A/B；殘差旁路只能從特徵x分支到最後加號，絕不能從原照片直接分出旁路。两通道同尺寸較大視窗分别看鄰域，再混合通道。其餘保留，無多尺度平行窗口，無文字堆疊。","reference":"convnext-c1-r01-desktop.png"}


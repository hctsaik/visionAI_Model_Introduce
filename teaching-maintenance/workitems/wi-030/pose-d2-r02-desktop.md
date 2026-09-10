# WI-030 對稱或遮住時，完整的點也可能配錯 — desktop
- lesson objective: 低誤差不保證點配對正確；有多解就補證據。
- page type: D
- primary reading path: 可辨認的方向 → 遮住方向線索 → 保留疑問再補觀測 → 核對輸出與工作條件
- major visual nodes:
  1. 可辨認的方向
  2. 遮住方向線索
  3. 保留疑問再補觀測
- named guide-conformant reference page: teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png
- pale-yellow takeaway: #FFF4CC：低誤差不保證點配對正確；有多解就補證據。
- source: https://docs.opencv.org/4.13.0/d5/d1f/calib3d_solvePnP.html
- generation: built-in imagegen；教學示意非模型實測。
- actual PNG review: reviewed；原生與936/328px證據見prototype-review.md；這是候選選定，不是使用者核准。
- user approval: pending

## 版本與生成意圖
產物：pose-d2-r02-desktop.png。原型生成前已有同故事r01及逐版preflight，本檔彙整實際選用版本，保留歷史。

{"prompt":"修訂教學圖，保留白底淡藍細框、繁體粗體與底部唯一#FFF4CC燈泡結論。保留三區故事。第二區下方兩種方向候選必須是180度旋轉而非鏡射：第一候選左上A右上B左下D右下C；第二候選左上C右上D左下B右下A。精確畫四點標籤，不准B A/C D鏡射。兩候選矩形工件相同，差別只有點名，不顯示缺口。刪『区一』，第一區標『可辨認的方向』。第三區刪底部相機工站流程（本圖專注點身份歧義）。保留換視角或加非對稱標記，底部結論低誤差不保證點配對正確。 無編號、教學示意非實測。","reference":"pose-d2-r01-desktop.png"}


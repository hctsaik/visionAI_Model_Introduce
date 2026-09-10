# WI-030 Keypoint R-CNN：先分物件，再找有名字的點 — mobile
- lesson objective: 點有身分與所屬物件；2D點還不是3D姿態。
- page type: C
- primary reading path: 每件定義相同點 → 框內預測位置 → 映回原圖 → 核對輸出與工作條件
- major visual nodes:
  1. 每件定義相同點
  2. 框內預測位置
  3. 映回原圖
- named guide-conformant reference page: teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png
- pale-yellow takeaway: #FFF4CC：點有身分與所屬物件；2D點還不是3D姿態。
- source: https://docs.pytorch.org/vision/main/_modules/torchvision/models/detection/keypoint_rcnn.html
- generation: built-in imagegen；教學示意非模型實測。
- actual PNG review: reviewed；原生與936/328px證據見prototype-review.md；這是候選選定，不是使用者核准。
- user approval: pending

## 版本與生成意圖
產物：key-c1-r05-mobile.png。原型生成前已有同故事r01及逐版preflight，本檔彙整實際選用版本，保留歷史。

{"prompt":"只刪第二區左上的小燈泡卡『教學示意／資料路徑從上到下！』，這是多餘說明。保留目前正確完整原圖→共享特徵→整件ROI→三熱圖的全部箭頭和其他內容。底部唯一淡黃色燈泡結論要完整置於畫布內，增加白色底邊距，不能裁到燈泡或文字。角落小註『教學示意』。原手機直向三區維持，不新增任何其他文字或圖。"}


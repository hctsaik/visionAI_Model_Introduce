# WI-030 Keypoint R-CNN：先分物件，再找有名字的點 — desktop
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
產物：key-c1-r04-desktop.png。原型生成前已有同故事r01及逐版preflight，本檔彙整實際選用版本，保留歷史。

{"prompt":"只修正中央ROI表示：完整件寫實照片加格線不可當特徵。改用藍色抽象平面，淡L形輪廓和A/B/C位置只供對應，標『物件1 ROI位置示意』。共享特徵向下箭頭進整體ROI，ROI向下到A/B/C熱圖，依現有正確順序。移除跨區大裝飾箭頭，避免原圖直接進ROI之誤讀。左區可用小細線沿上方直接接『共享特徵』，不接ROI。其餘兩件同方向和三熱圖位置不變，右區同點映回原圖不變。","reference":"key-c1-r03-desktop.png"}


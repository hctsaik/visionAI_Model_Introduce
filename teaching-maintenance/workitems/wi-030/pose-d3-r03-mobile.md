# WI-030 找點與求姿態，是不同的工作責任 — mobile
- lesson objective: 只需2D位置可先找點；需要3D姿態再接幾何與校正。
- page type: D
- primary reading path: 影像找點 → 幾何求姿態 → 依需求選接法 → 核對輸出與工作條件
- major visual nodes:
  1. 影像找點
  2. 幾何求姿態
  3. 依需求選接法
- named guide-conformant reference page: teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png
- pale-yellow takeaway: #FFF4CC：只需2D位置可先找點；需要3D姿態再接幾何與校正。
- source: https://docs.opencv.org/4.13.0/d5/d1f/calib3d_solvePnP.html
- generation: built-in imagegen；教學示意非模型實測。
- actual PNG review: reviewed；原生與936/328px證據見prototype-review.md；這是候選選定，不是使用者核准。
- user approval: pending

## 版本與生成意圖
產物：pose-d3-r03-mobile.png。原型生成前已有同故事r01及逐版preflight，本檔彙整實際選用版本，保留歷史。

{"prompt":"依附圖製作新版教學PNG，白底淡藍細框、繁體粗體、無編號，唯一#FFF4CC燈泡結論保留。重排768x2304手機，三個全寬上下區：影像找點、幾何求姿態、依需求接法。每區都是同四孔U形件，A左上B左下C右下D右上；第一區兩件各四點。第一區輸出2D點，第二區它與同件CAD3D點、相機K畸變三資料進PnP求解，不把2D接到CAD。输出R,t物體→相機；另外外參接工站。第三區左右對照2D位置覆核與3D姿態接手；標足夠且正確2D3D對應，沒有保證唯一解。必要標籤至少32px，刪重複長句。 教學示意非實測，四邊安全留白。","reference":"pose-d3-r03-desktop.png"}


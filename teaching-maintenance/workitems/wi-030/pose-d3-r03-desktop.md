# WI-030 找點與求姿態，是不同的工作責任 — desktop
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
產物：pose-d3-r03-desktop.png。原型生成前已有同故事r01及逐版preflight，本檔彙整實際選用版本，保留歷史。

{"prompt":"精確修訂附圖。繁體粗體、白底淡藍細框、唯一#FFF4CC燈泡結論。案例必須同一四孔U形件走到底。把第一區的兩件L形件、第三區上方2D核對L形件全部改成和中區CAD完全一樣的四孔U形件，A左上B左下C右下D右上，第一區標每件相同點A/B/C/D。第一區到中區的2D點箭頭從影像點直接接『Pose Pipeline幾何求解』盒左邊，不接CAD。底部中區『需足夠且正確...』黃色小條改淡藍，唯一黃底為最下面燈泡結論。其餘保留，避免照片幾何中途變形。 教學示意非實測。","reference":"pose-d3-r02-desktop.png"}


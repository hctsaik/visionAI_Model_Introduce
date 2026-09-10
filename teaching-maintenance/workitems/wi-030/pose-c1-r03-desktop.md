# WI-030 Pose Pipeline：點、幾何與相機一起求姿態 — desktop
- lesson objective: 點找對還不夠；幾何、校正與解的可信度都要核對。
- page type: C
- primary reading path: 同名2D與3D點 → 相機模型求解 → 重投影與座標接手 → 核對輸出與工作條件
- major visual nodes:
  1. 同名2D與3D點
  2. 相機模型求解
  3. 重投影與座標接手
- named guide-conformant reference page: teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png
- pale-yellow takeaway: #FFF4CC：點找對還不夠；幾何、校正與解的可信度都要核對。
- source: https://docs.opencv.org/4.13.0/d5/d1f/calib3d_solvePnP.html
- generation: built-in imagegen；教學示意非模型實測。
- actual PNG review: reviewed；原生與936/328px證據見prototype-review.md；這是候選選定，不是使用者核准。
- user approval: pending

## 版本與生成意圖
產物：pose-c1-r03-desktop.png。原型生成前已有同故事r01及逐版preflight，本檔彙整實際選用版本，保留歷史。

{"prompt":"精確修訂附圖。繁體粗體、白底淡藍細框、唯一#FFF4CC燈泡結論。只修第一區左下2D像素座標軸：u向右，v向下（OpenCV影像座標）。移除中區『K內部不含畸變』粉紅說明框；內參K＋畸變參數標籤已足夠。所有其他內容保持，四點U形件保持。 教學示意非實測。","reference":"pose-c1-r02-desktop.png"}


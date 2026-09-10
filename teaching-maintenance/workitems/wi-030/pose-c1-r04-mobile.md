# WI-030 Pose Pipeline：點、幾何與相機一起求姿態 — mobile
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
產物：pose-c1-r04-mobile.png。原型生成前已有同故事r01及逐版preflight，本檔彙整實際選用版本，保留歷史。

{"prompt":"修訂附圖，繁體中文、白底淡藍薄框，保留唯一#FFF4CC燈泡結論與教學示意。只改中區資料流：刪掉『相機內參K＋畸變參數』向下指向相機照片的箭頭。保留此參數向上進PnP箭頭。從PnP盒右側畫一條向右再向下的藍箭頭，直接進右下『輸出：物體→相機 R,t』框。PnP才產生R,t，相機照片只是參數來源。第三區刪『兩端精確到中心』製作指示文字，保留誤差沿兩點連線（像素距離）。其餘完全不動。","reference":"pose-c1-r03-mobile.png"}


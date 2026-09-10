# WI-030 Pose Pipeline：點、幾何與相機一起求姿態
- lesson objective: 點找對還不夠；幾何、校正與解的可信度都要核對。
- page type: C — 依具體因果／條件差異教工作判斷。
- primary reading path: 同名2D與3D點 → 相機模型求解 → 重投影與座標接手 → 依輸出界線核對原圖與工作條件
- major visual nodes:
  1. 同名2D與3D點
  2. 相機模型求解
  3. 重投影與座標接手
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看材質與細框；內容另設計。
- pale-yellow takeaway: #FFF4CC：點找對還不夠；幾何、校正與解的可信度都要核對。
- source: https://docs.opencv.org/4.13.0/d5/d1f/calib3d_solvePnP.html
- evidence: AI生成教學示意，非模型推論與效能實測。
- generation: built-in imagegen，桌面16:9，手機獨立重排；actual PNG review pending；user approval pending。

## Visual brief
不對稱金屬L形件有4個已知幾何角點A/B/C/D，第一區相機影像的2D點與旁邊同件3D CAD對照同名點；不鏡射，幾何保持。第二區两路與相機內參小相機圖進PnP求解，輸出三軸旋轉和平移箭頭，標「物體→相機」。第三區同原圖藍色觀測點與橘色重投影點小偏移比較，局部放大源框標「核對誤差與多解」，下方相機座標→工站座標另接外參，標「接手前再校正」，不得只三點宣稱唯一解或直接畫機器人抓取成功。

## Validation intent
查來源定位、同物件不變量、訓練／推論兩路、輸出責任；原生與936/328px實看，按v1.0逐圖分項，不能以正文補分。

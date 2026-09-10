# WI-030 找點與求姿態，是不同的工作責任
- lesson objective: 只需2D位置可先找點；需要3D姿態再接幾何與校正。
- page type: D — 依具體因果／條件差異教工作判斷。
- primary reading path: 影像找點 → 幾何求姿態 → 依需求選接法 → 依輸出界線核對原圖與工作條件
- major visual nodes:
  1. 影像找點
  2. 幾何求姿態
  3. 依需求選接法
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看材質與細框；內容另設計。
- pale-yellow takeaway: #FFF4CC：只需2D位置可先找點；需要3D姿態再接幾何與校正。
- source: https://docs.opencv.org/4.13.0/d5/d1f/calib3d_solvePnP.html
- evidence: AI生成教學示意，非模型推論與效能實測。
- generation: built-in imagegen，桌面16:9，手機獨立重排；actual PNG review pending；user approval pending。

## Visual brief
同一不對稱L件與三孔，第一區Keypoint R-CNN找點每件框內A/B/C清楚，標「需點標註與訓練」。第二區不是另一個替代神經網路：箭頭从第一區2D點，加上CAD已知3D多點與相機校正送幾何求解，標「Pose Pipeline」「物體到相機」。第三區二路工作需求：像素位置核對的2D圖與相機座標姿態三軸，標「2D核對」「3D再校正」，無性能排行、無抓取成功。

## Validation intent
查來源定位、同物件不變量、訓練／推論兩路、輸出責任；原生與936/328px實看，按v1.0逐圖分項，不能以正文補分。

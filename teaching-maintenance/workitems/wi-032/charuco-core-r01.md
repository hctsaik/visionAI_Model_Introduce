# WI-032 ChArUco：用已知角點，建立相機幾何
- lesson objective: 先用多視角建立內參；已知內參後才另外求姿態。
- page type: C — 以具體機制或同條件對照說明工作選擇。
- primary reading path: 已知標靶 → 跨視角對應 → 估參數與驗證 → 依可見證據採取下一步
- major visual nodes:
  1. 已知標靶
  2. 跨視角對應
  3. 估參數與驗證
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，借材質、細框、主體比例；模型內容另設計。
- pale-yellow takeaway: #FFF4CC：先用多視角建立內參；已知內參後才另外求姿態。
- source: https://docs.opencv.org/4.13.0/da/d13/tutorial_aruco_calibration.html
- evidence: AI生成教學示意；不冒充模型輸出、效能比較或可列印標靶。
- generation: built-in imagegen；桌機16:9／手機直向另排；actual PNG review pending；user approval pending。

## Visual brief／不變條件與可見證據
Three stages. Left: plausible camera lens and one printed ChArUco board, checkerboard with square fiducials inside white squares, no meaningless PCB. Enlarge ONE chessboard intersection, NOT marker center, with label「角點A」 and known board coordinates「板上位置已知」. Mid: same board photographed at 3 different tilts/positions inside same camera image boundary; same A corner marked. Connect board corner identity to image A identity using dotted correspondence lines, not temporal arrows. Label「多視角角點對應」. Right: clearly separated vertical substeps: calibration gives「相機內參＋畸變」beside a camera and distorted grid becoming rectified grid; then a SEPARATE arrow labeled「內參固定後」into pose estimation using one observed board and known board points, outputs board axes labeled「姿態R/t」. A small same-corner observed dot vs projected hollow dot pair labeled「重投影核對」joins validation, no invented precision. Calibration is not registration of daily product images. Board illustrations are conceptual, not printable calibration targets. Concrete board and visible corner identities occupy most area.

## Validation
WI-031缺口轉換：方法造成的變化要能在圖上定位，不能重複同圖只换名稱；比較分支不串接。核對重複工件身份、來源箭頭、輸出責任、圖說／原生／桌機頁內／360px手機，固定v1.0逐項評。

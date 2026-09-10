# WI-032 只拍中心，邊角誤差可能沒有被看見
- lesson objective: 校正要涵蓋位置與傾角；再用獨立視角查邊角誤差。
- page type: D — 以具體機制或同條件對照說明工作選擇。
- primary reading path: 同一相機與標靶 → 中心集中與廣泛覆蓋 → 用未參與校正的視角核對 → 依可見證據採取下一步
- major visual nodes:
  1. 同一相機與標靶
  2. 中心集中與廣泛覆蓋
  3. 用未參與校正的視角核對
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，借材質、細框、主體比例；模型內容另設計。
- pale-yellow takeaway: #FFF4CC：校正要涵蓋位置與傾角；再用獨立視角查邊角誤差。
- source: https://docs.opencv.org/4.13.0/da/d13/tutorial_aruco_calibration.html
- evidence: AI生成教學示意；不冒充模型輸出、效能比較或可列印標靶。
- generation: built-in imagegen；桌機16:9／手機直向另排；actual PNG review pending；user approval pending。

## Visual brief／不變條件與可見證據
Same ChArUco board same camera lens. Three conceptual regions: common camera/board input, large paired image-coordinate maps, independent check. In paired maps identical rectangular field-of-view: LEFT all small board corner observations clustered near center; RIGHT corner observations cover center and four outer regions with several tilts. Draw clearly different coverage, not different color of same dots. Label「只拍中心」「位置＋傾角都涵蓋」. Same unseen tilted board at field edge in final region with enlarged corner observed dot vs projected ring separated, label「邊角獨立核對」and action「不足就補拍」. Do NOT promise widespread coverage always passes; all results are conceptual. No exact score or invented statistics, no guarantee of metric measurement.

## Validation
WI-031缺口轉換：方法造成的變化要能在圖上定位，不能重複同圖只换名稱；比較分支不串接。核對重複工件身份、來源箭頭、輸出責任、圖說／原生／桌機頁內／360px手機，固定v1.0逐項評。

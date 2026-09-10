# WI-032 模糊會抹掉SIFT需要的局部線索
- lesson objective: 局部線索消失時，先改善影像，再談匹配數量。
- page type: D — 以具體機制或同條件對照說明工作選擇。
- primary reading path: 同一工件兩視圖 → 清楚與模糊局部 → 重新取像或改定位線索 → 依可見證據採取下一步
- major visual nodes:
  1. 同一工件兩視圖
  2. 清楚與模糊局部
  3. 重新取像或改定位線索
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，借材質、細框、主體比例；模型內容另設計。
- pale-yellow takeaway: #FFF4CC：局部線索消失時，先改善影像，再談匹配數量。
- source: https://docs.opencv.org/4.13.0/da/df5/tutorial_py_sift_intro.html
- evidence: AI生成教學示意；不冒充模型輸出、效能比較或可列印標靶。
- generation: built-in imagegen；桌機16:9／手機直向另排；actual PNG review pending；user approval pending。

## Visual brief／不變條件與可見證據
Same two-hole asymmetric bracket, same camera viewpoints, compare clear vs only moving image blurred. Show two large equal-scale notch patch comparisons. Clear patch retains sharp notch and directional gradient arrows with distinctive histogram peaks. Blurred patch genuinely loses notch detail, flatter weaker gradient evidence, candidate correspondence to multiple similar edge patches shown dashed orange. Label「清楚：局部可區分」「模糊：候選變含糊」. Keep bracket geometry in raw image same, blur is the only changed condition; no missing metal. End with focus/exposure setting and a sharp recaptured notch, labeled「先重拍／調整光學」, or if texture absent use known target. No invented counts, no statement four matches inherently insufficient. The matching task and subsequent geometry verification separate.

## Validation
WI-031缺口轉換：方法造成的變化要能在圖上定位，不能重複同圖只换名稱；比較分支不串接。核對重複工件身份、來源箭頭、輸出責任、圖說／原生／桌機頁內／360px手機，固定v1.0逐項評。

## 精確原生幾何版本r03
New SVG→browser PNG, not editing existing raster. 同物件與A/B/C位置使用單一定義；ECC整件平移一致。桌機1672×941，手機768×3050直向。原生／頁內尚待審查，user approval pending。圖內描述子與候選連線為機制示意，非執行結果。

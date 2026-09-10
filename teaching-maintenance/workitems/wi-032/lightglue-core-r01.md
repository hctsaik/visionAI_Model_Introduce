# WI-032 LightGlue：借周圍關係，把含糊配對分清
- lesson objective: LightGlue學的是配對；找點與求變換仍各有負責者。
- page type: C — 以具體機制或同條件對照說明工作選擇。
- primary reading path: 上游提供點與描述 → 互看上下文並修剪 → 匹配交給幾何估計 → 依可見證據採取下一步
- major visual nodes:
  1. 上游提供點與描述
  2. 互看上下文並修剪
  3. 匹配交給幾何估計
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，借材質、細框、主體比例；模型內容另設計。
- pale-yellow takeaway: #FFF4CC：LightGlue學的是配對；找點與求變換仍各有負責者。
- source: https://github.com/cvg/LightGlue
- evidence: AI生成教學示意；不冒充模型輸出、效能比較或可列印標靶。
- generation: built-in imagegen；桌機16:9／手機直向另排；actual PNG review pending；user approval pending。

## Visual brief／不變條件與可見證據
Same asymmetric two-hole bracket in two views, point identities A at unique notch, B/C at two similar holes. First region show extractor detecting A B C on both images and descriptor strips, label「上游extractor」. Center dominant wide evidence: query B in left view initially connects with equally thin orange dashed links to two right hole candidates B and C. Unique notch A-A is solid blue contextual anchor. After attention refinement, B-B thick blue, wrong B-C fades gray and terminates with cross at its target; A-A maintained. SAME coordinates and holes remain before/after. Label「圖內關係＋跨圖訊息」「含糊候選 → 更新配對」; small faint difficult point removed and labeled「低可匹配點修剪」, not all unmatched points deleted from source photo. Last output two image strips with stable match lines; separate arrow to a simple geometric projected quadrilateral labeled「RANSAC／幾何估計另做」. Training weights acknowledged subtitle「學習式配對器｜教學示意」. Do not depict LightGlue finding keypoints or directly warping images. No fake numeric confidences.

## Validation
WI-031缺口轉換：方法造成的變化要能在圖上定位，不能重複同圖只换名稱；比較分支不串接。核對重複工件身份、來源箭頭、輸出責任、圖說／原生／桌機頁內／360px手機，固定v1.0逐項評。

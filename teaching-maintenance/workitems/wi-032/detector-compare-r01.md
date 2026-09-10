# WI-032 找同一批零件：類別從哪裡來？
- lesson objective: 用類別與資料維護需求選候選，再以同批影像比較。
- page type: D — 以具體機制或同條件對照說明工作選擇。
- primary reading path: 同一螺栓與墊圈 → 固定類別與文字詞彙 → 核對結果與維護成本 → 依可見證據採取下一步
- major visual nodes:
  1. 同一螺栓與墊圈
  2. 固定類別與文字詞彙
  3. 核對結果與維護成本
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，借材質、細框、主體比例；模型內容另設計。
- pale-yellow takeaway: #FFF4CC：用類別與資料維護需求選候選，再以同批影像比較。
- source: https://arxiv.org/abs/2203.03605 ; https://arxiv.org/abs/2401.17270
- evidence: AI生成教學示意；不冒充模型輸出、效能比較或可列印標靶。
- generation: built-in imagegen；桌機16:9／手機直向另排；actual PNG review pending；user approval pending。

## Visual brief／不變條件與可見證據
Same tabletop one bolt and one washer. Two clearly parallel alternatives within central group, no arrow between methods. DINO detector: annotated training photos with class ids bolt/washer → trained class head → bounding boxes in image, labeled「固定類別訓練」「換類別：標註／訓練」。YOLO-World: pretrained weights plus two text chips bolt/washer→ cached descriptor strips→ region-text matching→same-format boxes, labeled「文字詞彙提示」「换詞彙：重編／重新驗證」. DINO is not DINOv2 and no textual prompt input; YOLOWorld still pretrained, do not say no training ever. End common same-batch acceptance panel shows input file stack, box-to-human-label correspondence and stopwatch alongside manual review pile, label「同資料查漏檢、錯類與完整時間」. No fake timing bars or different heatmaps to rank quality. Three main groups common task, two alternatives, joint verification. Clear material details and class-origin flows, few words.

## Validation
WI-031缺口轉換：方法造成的變化要能在圖上定位，不能重複同圖只换名稱；比較分支不串接。核對重複工件身份、來源箭頭、輸出責任、圖說／原生／桌機頁內／360px手機，固定v1.0逐項評。

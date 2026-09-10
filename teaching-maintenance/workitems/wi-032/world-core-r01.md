# WI-032 YOLO-World：把詞彙表示接到找框流程
- lesson objective: 詞彙可預先編碼；能否找到現場物件仍要驗證。
- page type: C — 以具體機制或同條件對照說明工作選擇。
- primary reading path: 先準備詞彙表示 → 影像與文字共同整理 → 區域對詞彙出框 → 依可見證據採取下一步
- major visual nodes:
  1. 先準備詞彙表示
  2. 影像與文字共同整理
  3. 區域對詞彙出框
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，借材質、細框、主體比例；模型內容另設計。
- pale-yellow takeaway: #FFF4CC：詞彙可預先編碼；能否找到現場物件仍要驗證。
- source: https://arxiv.org/abs/2401.17270
- evidence: AI生成教學示意；不冒充模型輸出、效能比較或可列印標靶。
- generation: built-in imagegen；桌機16:9／手機直向另排；actual PNG review pending；user approval pending。

## Visual brief／不變條件與可見證據
Same tabletop one bolt and one washer on gray mat. THREE groups, clear offline top row and online bottom row inside structure. Left vocabulary chips「螺栓」「墊圈」→ text encoder → two distinct descriptor strips labeled「預先編碼／快取」, file persists. Separately raw unboxed tabletop image enters visual backbone. Center feature patches from bolt/washer image interact with cached TEXT descriptors via arrows entering a grouped vision-language neck labeled「文字參與特徵整理」; keep text cache and image separate until this real interaction. Right show two region descriptor strips compared against SAME two vocabulary strips, matching cell highlighted, then original image with class-labeled rectangles bolt and washer. Text output is label+box, not freeform answer, no arrows from raw image directly to answer bypassing model. Weight training already done subtitle「預訓練開放詞彙偵測器｜教學示意」. Small note「固定詞彙可預計算；不是每張重編文字」. No exact scores, no quality superiority.

## Validation
WI-031缺口轉換：方法造成的變化要能在圖上定位，不能重複同圖只换名稱；比較分支不串接。核對重複工件身份、來源箭頭、輸出責任、圖說／原生／桌機頁內／360px手機，固定v1.0逐項評。

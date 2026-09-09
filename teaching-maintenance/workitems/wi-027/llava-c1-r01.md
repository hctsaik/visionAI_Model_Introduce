# WI-027 LLaVA：把看見的線索接進語言模型 r01
- lesson objective: 視覺特徵接上問題，才形成可以追問的回答。
- page type: C — 依本圖解釋或對比責任選用。
- primary reading path: 工作輸入 → 方法／條件改變 → 可見結果與限制 → 下一步核對。
- major visual nodes:
  1. 影像加問題
  2. 抽取視覺特徵
  3. 投影到語言上下文
  4. 生成可核對回答
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，沿用物件質感、就近對應及淡細框。
- pale-yellow takeaway: #FFF4CC：視覺特徵接上問題，才形成可以追問的回答。
- source: https://llava-vl.github.io/
- evidence: AI生成教學示意，不是實際模型輸出或性能比較。
- generation: built-in imagegen；desktop 16:9，mobile 1:3 區內獨立重排，原生與頁內實看；actual review pending；user approval pending。
- learning applied: WI-026 來源／位置保持、候選非真值、訓練和部署分開、比較替代路線不串接。

## 視覺因果、資料身分、逐字短標籤及禁項

4major nodes, a realistic two-position electrical terminal block; left silver screw present, right circular screw socket EMPTY. 1 image labelled '原圖 A' plus question '哪一側需要檢查？'. 2 '視覺編碼器' shows image→spatial feature tiles, maintaining left screw/right empty position. 3 '投影橋接＋語言模型': feature tiles map to visual token sequence via '投影'; question text goes separately into LLM context alongside visual sequence. Draw actual distinct paths merging only into language model. Concise lower label '圖文對齊與指令微調，讓模型學會回答'. 4 answer bubble labelled '回答示意' exact text '右側端子未見螺絲，請核對原圖。' Under it show localized crop of actual right EMPTYsocket matched by source locator, label '回看原圖 A'. No torque/root cause claim. Footnote '以原始 LLaVA 投影橋接為例'. Do not depict output as guaranteed JSON or calibration. No textencoder-to-similarity ranking because this is generative LLM.

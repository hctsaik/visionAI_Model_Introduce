# WI-027 Qwen-VL：依影像形狀保留閱讀線索 r03
- lesson objective: 保留足夠影像細節，也要一起衡量 token 與處理成本。
- page type: C — 依本圖解釋或對比責任選用。
- primary reading path: 工作輸入 → 方法／條件改變 → 可見結果與限制 → 下一步核對。
- major visual nodes:
  1. 長銘牌與讀取問題
  2. 依解析度處理
  3. 帶位置的視覺序列
  4. 結合問題生成回答
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，沿用物件質感、就近對應及淡細框。
- pale-yellow takeaway: #FFF4CC：保留足夠影像細節，也要一起衡量 token 與處理成本。
- source: https://qwenlm.github.io/blog/qwen2-vl/
- evidence: AI生成教學示意，不是實際模型輸出或性能比較。
- generation: built-in imagegen；desktop 16:9，mobile 1:3 區內獨立重排，原生與頁內實看；actual review pending；user approval pending。
- learning applied: WI-026 來源／位置保持、候選非真值、訓練和部署分開、比較替代路線不串接。

## 視覺因果、資料身分、逐字短標籤及禁項

4major groups. Use realistic wide silver industrial nameplate with only clearly printed fields '型號 A17' on left, '批次 B08' on right, two screws extremeends. 1 large plate plus question '型號與批次是什麼？'. 2 '動態解析度' plate remains wide after processing, visually partitioned tiles along width, no forced square distortion. Show underneath a separate square-image comparison explicitly labelled '另一種輸入形狀' with fewer illustrative tiles, not another output for same input. 3 '位置＋視覺 tokens' show row-sequence of feature tiles with left/right labels mapping A17/B08 regions, short '位置資訊跟著走', plus question text entering Qwen2-VL LLM. Avoid numeric token count formula; label '數量示意，實際由 processor 決定'. 4 response '型號：A17\n批次：B08' paired to original exact two fields with locators. Small clear subtitle '以 Qwen2-VL 為例；不同家族版本需另核對'. No invented network internals beyond published dynamicresolution andpositionrepresentation; title uses family Qwen-VL.

## Correction and pending generation
Rebuild causal path with exactly 4 groups. 1 Wide industrial plate with MODEL A17 left and BATCH B08 right, question 型號是什麼？ label 銘牌影像示意 (never real photographed). 2 preserve aspect ratio; raw image patches → 視覺編碼器 → abstract nonphotographic colored feature tokens. No square image comparison or claim square necessarily fewer tokens. 3 encoded visual tokens with position → 語言模型, separate question-text arrow → same LLM; NEVER tokens entering question box. Explain M-ROPE records visual positions, not output bounding box. 4 回答示意：型號 A17，需核對原圖, sourcecrop linked to A17 left. Qwen2-VL example not all versions.
Native and CSS-size reviews pending; user approval pending.

## r03 observed defect and exact edit
Edit supplied image with ONLY the following exact text replacements; preserve mechanisms, originalplate A17/B08, encoder/tokens and separate LLM inputs and allother layout. In firstpanel DELETE ENTIRE sentence containing 真實拍攝 and replace with 「AI生成銘牌示意，非實際拍攝。」. Firstpanel heading must be 「1 輸入：銘牌影像示意」, never 實際銘牌. Panel4 title replace 正確讀取 with 回答示意, fullheading 「4 回答示意：對回原圖」. Rightanswer heading 「回答示意，需核對原圖」, never imply actualQweninference. Small 'AI生成教學示意，非模型實測' preserved. Keep exact same aspectratio/dimensions, allother objects/labels unchanged.
Review pending; generation-batch8.json.

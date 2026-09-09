# WI-027 Qwen-VL：依影像形狀保留閱讀線索 r01
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

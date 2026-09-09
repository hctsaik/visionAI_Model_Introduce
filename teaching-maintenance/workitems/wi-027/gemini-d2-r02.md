# WI-027 JSON 格式正確，內容仍可能看錯 r01
- lesson objective: 格式檢查與內容核對，要分成兩個步驟。
- page type: D — 依本圖解釋或對比責任選用。
- primary reading path: 工作輸入 → 方法／條件改變 → 可見結果與限制 → 下一步核對。
- major visual nodes:
  1. 原始影像與格式要求
  2. 可解析但錯誤的回覆
  3. 逐欄對回原圖
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，沿用物件質感、就近對應及淡細框。
- pale-yellow takeaway: #FFF4CC：格式檢查與內容核對，要分成兩個步驟。
- source: https://ai.google.dev/gemini-api/docs/structured-output
- evidence: AI生成教學示意，不是實際模型輸出或性能比較。
- generation: built-in imagegen；desktop 16:9，mobile 1:3 區內獨立重排，原生與頁內實看；actual review pending；user approval pending。
- learning applied: WI-026 來源／位置保持、候選非真值、訓練和部署分開、比較替代路線不串接。

## 視覺因果、資料身分、逐字短標籤及禁項

3major groups. 1 same two-terminal connector leftscrew present rightempty, small request '回傳左右端子的螺絲狀態'. 2 clean JSON text {"left":"present","right":"present"} with short label '格式可解析' blue, below orange 'right 內容可能錯誤'; '回覆示意'. 3 compare originalrightemptyhole crop to JSON rightfield crossed out and corrected "right":"missing" labelled '人工核對示例'. Clear direction originalimage→evidencecheck as well as response→evidencecheck. Don't green-checkmodelquality just because validJSON. No Gemini internalstructure. Existing rawimagereview remains essential.

## r02 correction
Edit supplied image ONLY needed fixes, preserve correct rest. Replace ENTIRE bottom yellowbanner text with exactly: 「格式檢查與內容核對，要分成兩個步驟。」. Completely remove all words about contract or modelscorecomparison; they are from a different lesson. Keep lightbulb and single #FFF4CC banner. First heading 原始影像（教學示意） instead of 事實依據. In thirdgroup label 「原圖可見：無螺絲」 instead of 事實. Sameleftscrew/rightemptycrop, right presentinvalidcontent despite validJSON correctedmissing. Mainheading 格式正確 ≠ 內容正確. Preserve exact original aspectratio and size. Keep all text TraditionalChinese.
Generation-batch9.json; native and CSS-size review pending; user approval pending.

# WI-027 壓低像素預算，小字可能先消失 r01
- lesson objective: 比較答案時，同時比較細節覆蓋、token 與完整耗時。
- page type: D — 依本圖解釋或對比責任選用。
- primary reading path: 工作輸入 → 方法／條件改變 → 可見結果與限制 → 下一步核對。
- major visual nodes:
  1. 原始長銘牌
  2. 低預算的可見損失
  3. 保留原始局部再比較
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，沿用物件質感、就近對應及淡細框。
- pale-yellow takeaway: #FFF4CC：比較答案時，同時比較細節覆蓋、token 與完整耗時。
- source: https://qwenlm.github.io/blog/qwen2-vl/
- evidence: AI生成教學示意，不是實際模型輸出或性能比較。
- generation: built-in imagegen；desktop 16:9，mobile 1:3 區內獨立重排，原生與頁內實看；actual review pending；user approval pending。
- learning applied: WI-026 來源／位置保持、候選非真值、訓練和部署分開、比較替代路線不串接。

## 視覺因果、資料身分、逐字短標籤及禁項

3major groups. 1 large SAMEsilver longnameplate ascore with '型號 A17' left and '批次 B08' right. 2 '降低像素上限' show wholeplate stronglydownscaled then enlargeddisplay causing B08 to be blurry, response shows '批次：B0?' orange label '讀取不確定'. Do not show clearcorrect text in blurredregion; modelresponse notmeasurement. 3 '改用原始局部' correct originalrightfield crop clear '批次 B08' sourcebox on originalrightside, response '批次：B08' tagged '理想結果示意'; add time/token pairedicon label '多看細節，也可能多花時間'. Show entire-input vs sourceROI visualdifference; don't imply generated superresolution restores data. Subtitle '以 Qwen2-VL 像素預算為例；非實測'.

## r02 correction
Edit supplied image ONLY needed fixes, preserve correct rest. Replace ENTIRE bottom yellowbanner text with exactly: 「比較答案時，同時比較細節覆蓋、token 與完整耗時。」. Completely remove all words about contract or modelscorecomparison; they are from a different lesson. Keep lightbulb and single #FFF4CC banner. First originalplate and all later copies/crops must have EXACT same rightbottom screw location; the finalsourcecrop contains ONLY rightfield 批次 B08 and its actual bottom-right screw atBOTTOMRIGHT, notnewtopscrew. Remove any invented manufacturer's name. In finalcostnote change 生成 tokens to 影像 tokens. Keep lowresolutiontext visibly pixelated and originalROIclear; sourceROI fromoriginal, not enhancedlowres. Preserve exact original aspectratio and size. Keep all text TraditionalChinese.
Generation-batch9.json; native and CSS-size review pending; user approval pending.

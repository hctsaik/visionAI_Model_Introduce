# WI-027 Gemini Vision：把影像與問題交給多模態服務 r01
- lesson objective: 多模態回覆提供整理線索，關鍵內容仍要對回原始資料。
- page type: C — 依本圖解釋或對比責任選用。
- primary reading path: 工作輸入 → 方法／條件改變 → 可見結果與限制 → 下一步核對。
- major visual nodes:
  1. 選擇影像與問題
  2. 組成同一請求
  3. 服務生成回覆
  4. 對回影像再使用
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，沿用物件質感、就近對應及淡細框。
- pale-yellow takeaway: #FFF4CC：多模態回覆提供整理線索，關鍵內容仍要對回原始資料。
- source: https://ai.google.dev/gemini-api/docs/image-understanding
- evidence: AI生成教學示意，不是實際模型輸出或性能比較。
- generation: built-in imagegen；desktop 16:9，mobile 1:3 區內獨立重排，原生與頁內實看；actual review pending；user approval pending。
- learning applied: WI-026 來源／位置保持、候選非真值、訓練和部署分開、比較替代路線不串接。

## 視覺因果、資料身分、逐字短標籤及禁項

4major groups. Realistic two-terminal connector left screw present right missing, clearly empty right circularsocket. Node1 '影像＋問題' originalimage A and question '請列出需要檢查的位置'. Node2 '組成請求' image thumbnail and text question bundled in one visible envelope/frame with small label '指定模型與輸入設定'; not data compliance checklist. Node3 'Gemini API' closed service block with visible input image/text and output generated response text '右側端子未見螺絲' labelled '回覆示意'. DO NOT draw private encoders/projectors/architectures. Node4 '回看原始影像' enlarged right emptysocket with source marker A-right and worksheet '觀察：未見螺絲\n下一步：現場確認'. show source originalimage directly feeding review as well as response. Short subtitle 'Gemini Vision 是影像能力稱呼；此圖示 API 工作流程'. Avoid naming latestmodel/performance, no unsupported citation automaticguarantee.

# WI-027 DINOv2 與 DINOv3：比較的是整套用途 r01
- lesson objective: 換骨幹時，下游也要重新配好，再用同一測試集比較。
- page type: D — 依本圖解釋或對比責任選用。
- primary reading path: 工作輸入 → 方法／條件改變 → 可見結果與限制 → 下一步核對。
- major visual nodes:
  1. 同一批影像與任務
  2. 各自抽特徵並重建下游
  3. 比較結果與完整成本
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，沿用物件質感、就近對應及淡細框。
- pale-yellow takeaway: #FFF4CC：換骨幹時，下游也要重新配好，再用同一測試集比較。
- source: https://arxiv.org/html/2508.10104v1
- evidence: AI生成教學示意，不是實際模型輸出或性能比較。
- generation: built-in imagegen；desktop 16:9，mobile 1:3 區內獨立重排，原生與頁內實看；actual review pending；user approval pending。
- learning applied: WI-026 來源／位置保持、候選非真值、訓練和部署分開、比較替代路線不串接。

## 視覺因果、資料身分、逐字短標籤及禁項

3major visualgroups. 1 same reference collection realistic brackets+gears, separate testimage of abracket labelled '獨立測試影像'; referencesnotmixedwithtest. 2 within one broad comparison group two independent horizontal routes labelled DINOv2 and DINOv3; each referenceimages→itsownfeaturestrips→itsownfeaturelibrary, testimage→same respectiveencoder→query; draw paths nofeaturelibraryshared. Small notes '重新抽參考特徵' and '各自調整下游'. Do not require same exactlayer or swap incompatiblevector dimensions. 3 two retrievaloutputlists with realistic thumbnails same format, no fabricatedwinner; comparison sheet labels '找對候選？','漏掉小缺口？','建庫／記憶體／耗時'. Show DINOv2 andDINOv3 as alternatives notserial; textlimited, realthumbnails. Add '資料、任務與調整預算固定；結果需實測'. No inventedranking superiority.

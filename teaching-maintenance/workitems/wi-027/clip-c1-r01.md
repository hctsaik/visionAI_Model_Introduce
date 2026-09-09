# WI-027 CLIP：讓影像和文字可以比相似 r01
- lesson objective: CLIP 比的是圖文相似度，候選文字決定你在問什麼。
- page type: C — 依本圖解釋或對比責任選用。
- primary reading path: 工作輸入 → 方法／條件改變 → 可見結果與限制 → 下一步核對。
- major visual nodes:
  1. 從圖文配對學習
  2. 影像與文字各自編碼
  3. 比較同一空間的表示
  4. 依候選文字排序
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，沿用物件質感、就近對應及淡細框。
- pale-yellow takeaway: #FFF4CC：CLIP 比的是圖文相似度，候選文字決定你在問什麼。
- source: https://arxiv.org/abs/2103.00020
- evidence: AI生成教學示意，不是實際模型輸出或性能比較。
- generation: built-in imagegen；desktop 16:9，mobile 1:3 區內獨立重排，原生與頁內實看；actual review pending；user approval pending。
- learning applied: WI-026 來源／位置保持、候選非真值、訓練和部署分開、比較替代路線不串接。

## 視覺因果、資料身分、逐字短標籤及禁項

Four major groups. 1 header '訓練：找正確配對', realistic metal L bracket caption '金屬支架', toothed steel gear caption '齒輪'; blue paired image-caption links, one muted crossed mismatch link, short '拉近配對，區分錯配'. 2 header '部署：分別編碼', new bracket image enters '影像編碼器' and candidate words '金屬支架' / '齒輪' enter separate '文字編碼器'; both exit feature strips, no text enters imageencoder. 3 header '在共同空間比較', illustration bracket-image point near bracket-text point and far from gear-text point, qualitative only, labeled '示意位置，非實測'. Clearly both modalities entering this node. 4 header '輸出：文字候選排序', short list '金屬支架' first with orange candidate border, '齒輪' second; small bracket source repeated only for grounding. No generated sentence, no bbox, no percentage defect confidence. Body predominantly realistic objects and visible matching comparison.

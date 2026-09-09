# WI-027 CLIP 與 SigLIP：訓練不同，選型要同題 r01
- lesson objective: 訓練目標說明差異，自己的測試才決定選用。
- page type: D — 依本圖解釋或對比責任選用。
- primary reading path: 工作輸入 → 方法／條件改變 → 可見結果與限制 → 下一步核對。
- major visual nodes:
  1. 共同圖文配對資料
  2. 批次對比或逐對判別
  3. 同條件驗證圖文排序
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，沿用物件質感、就近對應及淡細框。
- pale-yellow takeaway: #FFF4CC：訓練目標說明差異，自己的測試才決定選用。
- source: https://arxiv.org/abs/2303.15343
- evidence: AI生成教學示意，不是實際模型輸出或性能比較。
- generation: built-in imagegen；desktop 16:9，mobile 1:3 區內獨立重排，原生與頁內實看；actual review pending；user approval pending。
- learning applied: WI-026 來源／位置保持、候選非真值、訓練和部署分開、比較替代路線不串接。

## 視覺因果、資料身分、逐字短標籤及禁項

3major groups. 1 matched realistic bracket/gear photos and corresponding captionlabels, same dataset. 2 within one wide group two clearly separate comparisonrows: 'CLIP：批次 softmax' with 2x2 image/textsimilarity grid correct pairs diagonalemphasized and row/columncompetition arrows labelled '在批次中比配對'; 'SigLIP：逐對 sigmoid' with the SAMEfour pairings each independently '配對／不配對', labelled '每對各算損失'. No sum-to100forSigLIP. Connect sameinputs into bothrows independently. 3 same bracket testphoto+samecandidate words enters two independent pretrainedmodels producing two ranking lists, no winner or inventedprecision. Short controls '相同圖文、硬體與測試集' and metrics '排序錯誤／拒答／完整耗時'. Important featuretraining and deploymentseparated; don't turnmodelsinto serialstages or classifiers ofdefects.

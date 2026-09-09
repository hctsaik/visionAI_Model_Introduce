# WI-027 SigLIP：逐對學會圖文是否配合 r02
- lesson objective: 逐對學配合程度，分數仍要用自己的資料驗證。
- page type: C — 依本圖解釋或對比責任選用。
- primary reading path: 工作輸入 → 方法／條件改變 → 可見結果與限制 → 下一步核對。
- major visual nodes:
  1. 準備圖文配對
  2. 每對分別計算目標
  3. 共同更新兩個編碼器
  4. 部署時再比圖文
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，沿用物件質感、就近對應及淡細框。
- pale-yellow takeaway: #FFF4CC：逐對學配合程度，分數仍要用自己的資料驗證。
- source: https://arxiv.org/abs/2303.15343
- evidence: AI生成教學示意，不是實際模型輸出或性能比較。
- generation: built-in imagegen；desktop 16:9，mobile 1:3 區內獨立重排，原生與頁內實看；actual review pending；user approval pending。
- learning applied: WI-026 來源／位置保持、候選非真值、訓練和部署分開、比較替代路線不串接。

## 視覺因果、資料身分、逐字短標籤及禁項

4 major groups. 1 '訓練資料': two realistic source images bracket and gear, captions '金屬支架' and '齒輪' linked correctly. 2 '逐對 sigmoid': display two larger sample pairs bracket-image with '金屬支架' labelled '配對', same bracket-image with '齒輪' labelled '不配對'; each has its own sigmoid-symbol-less small compatibility bar, targets '拉近' and '推遠'. No softmax shares or sum100%. Note '也包含不配對樣本'. 3 '一起更新編碼器': the pair losses clearly converge to ONE shared imageencoder and ONE shared textencoder, a training return arrow labelled '共同學習'; show their two feature strips as common output space. 4 '部署：比相似度': new bracket enters learned imageencoder while two text candidates enter learned textencoder, converge into comparison and show bracket-text candidate selected orange. No independent model per pair. Short callout '原始 SigLIP；不同於批次 softmax 正規化'. No claims always faster/moreaccurate, no defect probability.

## Correction and pending generation
Fix learning semantics: positive pair is bracket photo + text 金屬支架; negative pair is SAME bracket photo + text 齒輪. Positive 拉近，降低損失; negative 推遠，降低損失. NEVER 增加損失 as desired result. Show pair losses jointly update shared image/text encoders, not arrows between the encoders. Training and inference visibly separated. Images are AI teaching illustrations; no claim real captured data.
Native and CSS-size reviews pending; user approval pending.

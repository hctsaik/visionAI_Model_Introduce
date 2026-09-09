# WI-027 候選沒有正確答案，第一名也可能錯 r01
- lesson objective: 第一名只是候選中的相對結果，不能直接當作正確答案。
- page type: D — 依本圖解釋或對比責任選用。
- primary reading path: 工作輸入 → 方法／條件改變 → 可見結果與限制 → 下一步核對。
- major visual nodes:
  1. 同一張工件影像
  2. 候選集合限制了排序
  3. 補齊候選並檢查拒答
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，沿用物件質感、就近對應及淡細框。
- pale-yellow takeaway: #FFF4CC：第一名只是候選中的相對結果，不能直接當作正確答案。
- source: https://github.com/openai/CLIP
- evidence: AI生成教學示意，不是實際模型輸出或性能比較。
- generation: built-in imagegen；desktop 16:9，mobile 1:3 區內獨立重排，原生與頁內實看；actual review pending；user approval pending。
- learning applied: WI-026 來源／位置保持、候選非真值、訓練和部署分開、比較替代路線不串接。

## 視覺因果、資料身分、逐字短標籤及禁項

3major groups. 1 large realistic toothed steel gear, label '待查影像：齒輪'. 2 header '候選只有兩種' candidate text '金屬支架' and '軸承', simple rank shows '軸承' top orange badge '仍可能排第一', bracketbelow. Show inputgear→image/textcomparison→ranking. The word gear MUST NOT be in this candidatepool. 3 '加入齒輪＋非上述類別' show revised candidate textpool includes '齒輪','軸承','金屬支架','其他'; qualitative gear candidate highlighted with note '重新驗證，不保證成功'; nearby real gear detail paired to label. No fabricated logits or direct claim addingunknown solvesopenset. Include 'CLIP／SigLIP 排序風險示意'. Show how answerpool changed, not actualmodel inference. Single yellowtakeaway.

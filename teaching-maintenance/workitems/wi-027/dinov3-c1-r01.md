# WI-027 DINOv3：把局部之間的關係學穩 r01
- lesson objective: Gram anchoring 穩住局部關係，實際用途仍由下游決定。
- page type: C — 依本圖解釋或對比責任選用。
- primary reading path: 工作輸入 → 方法／條件改變 → 可見結果與限制 → 下一步核對。
- major visual nodes:
  1. 選定影像局部
  2. 保留早期特徵關係
  3. 訓練中對齊關係
  4. 部署後交給下游
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，沿用物件質感、就近對應及淡細框。
- pale-yellow takeaway: #FFF4CC：Gram anchoring 穩住局部關係，實際用途仍由下游決定。
- source: https://arxiv.org/html/2508.10104v1
- evidence: AI生成教學示意，不是實際模型輸出或性能比較。
- generation: built-in imagegen；desktop 16:9，mobile 1:3 區內獨立重排，原生與頁內實看；actual review pending；user approval pending。
- learning applied: WI-026 來源／位置保持、候選非真值、訓練和部署分開、比較替代路線不串接。

## 視覺因果、資料身分、逐字短標籤及禁項

Use a realistic black electrical connector with two silver pins. Four left-to-right major groups. 1 same connector with A marked on left silver pin, B on right silver pin, C on black body; three large corresponding crops with letter anchors. 2 header '訓練：早期模型', show A/B visually similar silver features and C distinct dark feature, paired with a simple symmetric 3x3 relationship matrix labelled A B C both axes: diagonal and A-B/B-A blue, A-C/B-C/C-A/C-B pale grey; legend '藍：較相近'. Label matrix '局部兩兩關係'. 3 header 'Gram anchoring', show current Student relationship matrix with identical axis order; amber outline on offdiagonal A/B cells where reference guides alignment. Arrow from earlier relationship matrix to student matrix labelled '對齊關係'; short label '保留局部一致性'. DO NOT imply matching exact raw RGB features or runtime anomaly score. 4 header '部署：局部特徵', new connector image enters a single DINOv3 block then spatial feature map with marked A/B/C corresponding pin/body locations, ends at '下游配對／分類'. No fabricated accuracy comparison, no defect mask. Main teaching is relationships vs rawfeature copying. Give groups2/3 ample width, concise labels. Include '以 DINOv3 ViT 為例' and '關係矩陣為教學示意'.

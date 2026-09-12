# DINOv2 (`dinov2`)

- roadmap family: `foundation-vlm-open-world`
- roadmap model: `DINOv2`
- Markdown pages: `06-10` to `06-13`
- content coverage status: `complete`
- generation status: `ready-for-visual-production`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/dinov2.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
工件照片很多，類別標註卻很少；你想先找出相似支架，或為後續分類與異常檢查建立起點。

### 它交出什麼，也不交出什麼
本課交出影像特徵；範例由下游查庫回傳相似工件候選。若要異常分數或定位，另接並驗證相應方法。

### 一句心智模型
DINOv2 從大量無人工類別標籤的影像學可重用表示：訓練時，Student 對齊 Teacher 的整圖與局部特徵目標，讓不同視圖仍能保留有用線索。部署時只需選定的預訓練骨幹，把新影像轉成整圖及局部特徵；圖中的查庫再拿整圖特徵與參考庫比較，找出相似工件。

**限制：** 換一個墊圈案例：右側小缺口在原圖可見，整張縮小後卻可能變弱。相近的特徵不能證明工件無缺陷；DINOv2 本身也不自動輸出缺陷輪廓。

### 換一個現場再推理
你只有新零件的正常照片，需要找異常位置，現有系統只輸出整圖相似度。

**問題：** 沿用查庫就能得到精確缺陷輪廓嗎？你會先改哪一步？

**核對：** 不能。可從凍結骨幹＋正常局部參考方法起步，先確認細節可見並補局部特徵／異常比較，再以獨立正常與缺陷樣本驗證。若已有可靠的專用定位器，也可先用它做基準；選擇要對應需要的輸出。
<!-- topic-learning-bridge:end -->
<!-- wi027-model-core:start -->
## WI-027 核心做法與工作取捨

DINOv2 從大量無人工類別標籤的影像學可重用表示：訓練時，Student 對齊 Teacher 的整圖與局部特徵目標，讓不同視圖仍能保留有用線索。部署時只需選定的預訓練骨幹，把新影像轉成整圖及局部特徵；圖中的查庫再拿整圖特徵與參考庫比較，找出相似工件。

換一個墊圈案例：右側小缺口在原圖可見，整張縮小後卻可能變弱。相近的特徵不能證明工件無缺陷；DINOv2 本身也不自動輸出缺陷輪廓。

只有未標類別或正常影像時，可先用凍結 DINOv2 做檢索或搭配正常參考方法；仍需整理參考資料與留出測試。DINOv3 也是特徵起點，新增局部關係穩定的訓練設計，是否值得更換要看自己的任務。

換產品要補足新外觀的參考與測試資料；換骨幹要重新抽取整個參考庫，重新調整下游，不能混用不相容特徵。固定任務、測試集與調整預算，同看候選命中、微小缺陷錯誤、建庫時間、記憶體和完整推論耗時。

先收集代表性的支架／齒輪原圖，按實體工件分開參考與測試集，固定模型權重及取像／前處理。

和原有查庫流程比較候選是否找對；若接異常檢查，再看正常誤報、缺陷漏檢及人工覆核量，並計入建庫和查詢成本。

來源：https://arxiv.org/abs/2304.07193

版本及示意界線見工作項目 sources.md。使用者成品核准pending。
<!-- wi027-model-core:end -->
## Identity and engineering boundary

完整的白話模型介紹與來源，請見 [DINOv2_MODEL_CONCEPT.md](DINOv2_MODEL_CONCEPT.md)。這份文件明確分開了訓練中的 Teacher／Student 自監督機制、部署時 encoder 的 global／patch feature 輸出，以及 Good／Bad patch heatmap 的下游責任。

DINOv2 is a self-supervised visual foundation **ViT encoder**. It produces all-purpose visual representations: a global/CLS representation and a grid of patch features that can be consumed by retrieval, nearest-neighbour support, few-shot anomaly detection, transfer learning or an explicit downstream head.

It is **not** the DINO detector family, a text-conditioned VLM, a generative model, a detector head, a pixel mask, a metrology measurement or an automatic tiny-defect locator. The backbone only exposes features; a named layer, pooling/aggregation policy and downstream NN/PCA/classifier/AD/detector head must make the score, map or box responsibility explicit.

## Reproducible engineering contract

### `architecture_path`

`timestamped image → fixed ROI/tile → declared resize/normalize → patchify + position → ViT self-attention blocks → CLS/global feature + patch-token grid`. The downstream owner then declares layer selection, CLS/pooling or patch aggregation, optional support bank/PCA/head and candidate/score/map action. There is no text encoder or image decoder in this path.

### `representation_or_score`

- global/CLS feature: a versioned image descriptor that can feed retrieval, NN or a named classifier/linear head.
- patch features: versioned spatial-grid representations; their selected layer, patch size, tile coverage and aggregation govern what local evidence remains observable.
- score/map/box: not DINOv2 output by default. A downstream NN distance, AD head, detector or calibration policy owns it and must be separately versioned.
- a high-dimensional feature is neither a defect class proof nor a calibrated release probability.

### `cost_and_operating_point`

Lock model size, patch size, checkpoint/hash/license, input resolution, ROI/tile policy, normalization, layer and feature postprocess. Measure token count, VRAM, image-to-feature P95/P99, support-bank/head latency and the downstream action path. Measure the full path when DINOv2 feeds a human or specialist queue, not backbone forward time alone.

### `failure_boundary`

- Small evidence can be diluted by optics, resize, tile coverage, patch size or chosen feature layer before the downstream feature operation.
- Domain/material/illumination/recipe shift may make features non-separable despite generic representation strength.
- Wrong layer, pooling, normal bank, NN/PCA/head or aggregation can manufacture a poor score from a capable backbone.
- Patch features do not by themselves prove localization, defect size or calibrated release probability.
- DINOv2 must never be described as the distinct DINO detector family or as a generative VLM.

### `selection_gate`

Select DINOv2 as a visual feature backbone only after fixing input/ROI/tile/patch policy, feature layer, downstream head/support procedure and decision evidence. Verify same-optics local separability, patch dilution, OOD/drift, target truth and full P95. Use a named downstream route such as AnomalyDINO, SubspaceAD, nearest-neighbour retrieval or a linear head; do not release an embedding as if it were a class, defect probability or pixel decision.

### `evidence_bundle`

Store image/ROI/tile provenance, resize/normalization checksum, model size/patch size/checkpoint hash/license, chosen layer and feature shape, pooling/aggregation, support-bank or head version, token count/VRAM, target truth, OOD/drift outcome, score/map owner, specialist decision and end-to-end P95/P99.

## Required C / D visual pages

| page | lesson | archetype | visible causal story |
| --- | --- | --- | --- |
| `06-10` | identity and problem | C | Engineer asks what a visual feature backbone can help with; fixed ROI becomes global/patch features, then an explicit downstream route—not a detector claim. |
| `06-11` | architecture | C | Image patchification and ViT blocks produce global/patch features; layer/pool/head selection owns every score/map/box. |
| `06-12` | build and inference | C | Lock checkpoint/patch/input/layer/postprocess, measure tokens/VRAM/P95 and verify same-optics feature separability and drift. |
| `06-13` | engineering selection | D | Reject “embedding equals defect proof”; compare named DINOv2 downstream routes under one feature/input contract. |

## Sources

- Oquab et al., *DINOv2: Learning Robust Visual Features without Supervision* (2023), [arXiv:2304.07193](https://arxiv.org/abs/2304.07193).
- `full-model-course/06-foundation-vision-and-vlm.md` for course-scoped claims and page order.

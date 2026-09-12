# DINOv3 (`dinov3`)

- roadmap family: `foundation-vlm-open-world`
- roadmap model: `DINOv3`
- Markdown pages: `06-14` to `06-17`
- content coverage status: `complete`
- generation status: `ready-for-visual-production`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/dinov3.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
你要比較接頭上不同位置的線索，既希望整件可辨識，也希望局部特徵在長時間預訓練後仍保留一致的關係。

### 它交出什麼，也不交出什麼
提供可供檢索、局部配對或任務頭使用的整圖與局部特徵；本課不把特徵色圖當成精確輪廓。

### 一句心智模型
DINOv3 延續大規模自監督特徵學習。本課以 ViT 版本的 Gram anchoring 說明關鍵設計：訓練時，不只關心整圖表現，也讓目前模型的局部特徵兩兩關係，接近較早模型提供的關係目標，以緩解長訓練中局部一致性退化。部署得到的是特徵，配對、分類或異常判斷仍由下游完成。

**限制：** 更好的局部表示仍受到影像細節限制。墊圈右側小缺口若在縮圖後變弱，DINOv3 的名稱或漂亮特徵色圖，都不能代替輸入可見性與下游漏檢測試。

### 換一個現場再推理
DINOv3 的局部色圖更整齊，但在相同資料上重新建庫需要更久，候選命中尚未測量。

**問題：** 現在應直接更換，還是先比較什麼？

**核對：** 先保留基準，以同一留出集比較實際命中或定位錯誤，再把重新建庫、記憶體、查詢時間算進去。只有當改善符合工作需求，且維護代價可接受時才換；保留 DINOv2 也可能合理。
<!-- topic-learning-bridge:end -->
<!-- wi027-model-core:start -->
## WI-027 核心做法與工作取捨

DINOv3 延續大規模自監督特徵學習。本課以 ViT 版本的 Gram anchoring 說明關鍵設計：訓練時，不只關心整圖表現，也讓目前模型的局部特徵兩兩關係，接近較早模型提供的關係目標，以緩解長訓練中局部一致性退化。部署得到的是特徵，配對、分類或異常判斷仍由下游完成。

更好的局部表示仍受到影像細節限制。墊圈右側小缺口若在縮圖後變弱，DINOv3 的名稱或漂亮特徵色圖，都不能代替輸入可見性與下游漏檢測試。

與 DINOv2 比較時，固定相同影像、工作任務、留出測試集與調整預算；允許各自使用相容的前處理與下游設定，並如實記錄。不要要求不同模型硬接同一維度的參考庫。

更換骨幹後，重新抽取參考特徵、調整下游和驗證新門檻；換產品也需補參考及失敗案例。比較候選命中或定位誤差、正常誤報／缺陷漏檢，以及建庫、記憶體和完整耗時；局部圖好看不等於工作改善。

保留既有 DINOv2 基準，選定一個 DINOv3 ViT 權重；用相同實體隔離的參考／測試資料，為兩者各自建立相容的下游。

在同一留出集比較任務錯誤與完整成本；若要局部配對，用可核對的點位或對應標註驗證，不以彩色特徵圖評輸贏。

來源：https://arxiv.org/html/2508.10104v1

版本及示意界線見工作項目 sources.md。使用者成品核准pending。
<!-- wi027-model-core:end -->
## Identity and engineering boundary

DINOv3 is a distinct self-supervised visual foundation model generation, not an alias for DINOv2 or the DINO detector family. It produces global and dense patch representations. Its training explicitly addresses dense feature degradation during long schedules through **Gram anchoring**, and it includes post-hoc strategies for resolution, model-size and text-alignment flexibility.

It remains a feature backbone. It is not a detector, pixel-mask decoder, generative VLM, calibrated defect probability or release authority. A deployed score, map, box or action still belongs to a versioned layer/patch policy plus an explicit retrieval, AD, NN/PCA or task-head route.

## Reproducible engineering contract

### `architecture_path`

`timestamped image → fixed ROI/tile → declared resize/normalize → patch tokens → long-trained self-supervised ViT → global/patch embeddings → optional resolution or text-alignment postprocess → named downstream retrieval/AD/head`. Gram anchoring belongs to training: it constrains the patch-feature similarity structure to preserve dense local geometry during long training. It is not an inference head, pixel mask, or automatic production proof.

### `representation_or_score`

- global and patch embeddings are versioned representations tied to release/checkpoint, preprocessing, patch grid, selected layer and optional postprocess.
- Gram anchoring is a training mechanism for dense feature quality; it does not supply a runtime anomaly score.
- resolution/text-alignment postprocess changes the feature contract and must be recorded; it does not turn DINOv3 into a text-generative VLM.
- a score/map/box is produced only by a named downstream route and local decision policy.

### `cost_and_operating_point`

Lock release/checkpoint, license, model size, preprocessing, resolution/tile policy, patch size, feature layer, resolution/text-alignment postprocess and downstream adaptor. Measure tokens, VRAM, feature/adaptor latency and full P95/P99 from capture to evidence action. A new release also requires reproducibility, security, compatibility and drift baselines.

### `failure_boundary`

- Patch dilution, optics, resize, tile coverage or selected layer can still erase small local evidence before a downstream head consumes it.
- Dense-feature improvement is not evidence that a target production defect is separable under local material, illumination, recipe or OOD conditions.
- Release/weights/API/license changes, postprocess changes and token cost can invalidate a DINOv2 comparison or deployed operating point.
- DINOv3 is not DINOv2, DINO detector, a generative VLM, a defect mask or a release decision.

### `selection_gate`

Compare DINOv3 with the DINOv2 baseline on the same original images, held-out task data, hardware and tuning budget. Use each model's compatible preprocessing, feature extraction and downstream settings; document the differences and rebuild each reference bank separately. Measure task errors, reference-building cost, memory and end-to-end latency. Validate the chosen release and real target data; a newer name or a cleaner feature visualization alone does not justify replacement.

### `evidence_bundle`

Preserve image/ROI/tile provenance, preprocess checksum, release/checkpoint hash/license, model/patch/layer/feature shape, resolution/text-alignment postprocess, downstream adaptor/head, token/VRAM/P95, DINOv2 baseline configuration, target truth, drift/OOD evidence, security/compatibility qualification and specialist decision.

## Required C / D visual pages

| page | lesson | archetype | visible causal story |
| --- | --- | --- | --- |
| `06-14` | identity and problem | C | Engineer distinguishes DINOv3 from DINOv2; fixed ROI reaches dense features under a named route, not an automatic detector claim. |
| `06-15` | architecture | C | Patch tokens flow through the long-trained ViT; Gram anchoring preserves dense similarity in training and optional postprocess remains a versioned feature contract. |
| `06-16` | build and inference | C | Lock release/license/preprocess/layer/tile/postprocess/adaptor; compare with DINOv2 on same pixels and measure security, drift and P95. |
| `06-17` | engineering selection | D | Reject “newer DINO”; select only on reproducible local evidence over DINOv2 under one fixed contract. |

## Sources

- Siméoni et al., *DINOv3* (2025), [arXiv:2508.10104](https://arxiv.org/abs/2508.10104).
- `full-model-course/06-foundation-vision-and-vlm.md` for course-scoped claims and page order.

<!-- wi033-engineering:start -->
## WI-033 工程圖修正

### DINOv3：一張圖保留多個局部表示

以ViT骨幹為例，影像轉成patch token並與其他位置交換資訊，輸出局部及全局表示。局部表示保留對應位置，但每個向量包含上下文，不等於該格像素值。異常判斷、分類或匹配要接下游方法；特徵色圖不是現成缺陷分數。

骨幹交出特徵，局部位置與下游工作仍要對齊。

來源：https://arxiv.org/html/2508.10104v1

### DINOv3：訓練時守住局部關係

Gram矩陣記錄同圖patch特徵的兩兩內積；以較早教師的關係當目標，約束目前學生，並保留原有自監督訓練目標。這不是把特徵逐點鎖成相同數值，也不是推論時要額外跑的模組。本圖數字為二維單位向量算例。

Gram 只約束訓練，部署仍輸出特徵。

來源：https://arxiv.org/html/2508.10104v1

### DINOv3：換骨幹也要重建相容參考

部署不跑Gram教師；用固定權重與前處理抽取表示，再建相容特徵庫或訓練下游頭。不能把DINOv2庫直接當DINOv3庫查詢。以同一留出集核對命中／漏檢、抽特徵和查庫時間、記憶體與重建成本，不能只比較色圖漂亮程度。

保存權重與前處理，同條件重建庫並量完整成本。

來源：https://arxiv.org/html/2508.10104v1

### DINOv3：以工作結果決定是否換骨幹

工程4不重複主反例。固定同一批正常與缺口墊圈及取像，各自使用相容骨幹與參考表示；記錄下游漏檢/誤報、抽特徵/查庫時間與重建負擔。新骨幹訓練機制不同，不代表每項域內指標一定進步。

同題比較效果與重建代價，保留基準也合理。

來源：https://arxiv.org/html/2508.10104v1

<!-- wi033-engineering:end -->

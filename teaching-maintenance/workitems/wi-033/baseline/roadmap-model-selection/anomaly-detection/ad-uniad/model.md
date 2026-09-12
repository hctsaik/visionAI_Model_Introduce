# UniAD (`ad-uniad`)

- roadmap category: `anomaly-detection`
- course pages: `04-39` through `04-42`
- research status: `complete`
- visual status: `ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/ad-uniad.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
多種產品想共用模型：用正常資料學特徵重建，避免缺陷被原樣照抄。

### 它交出什麼，也不交出什麼
提供可疑位置與候選分數；不直接交付尺寸、根因或放行判定。

### 一句心智模型
多類正常影像共訓重建模型，骨幹固定。UniAD 在注意力中遮住自己與近鄰，配合逐層查詢與訓練時特徵擾動，減少從輸入直接複製；推論比較原始與重建特徵，將差異排回位置圖。

**限制：** 正常外觀可能誤報，缺陷也可能被重建；按產品保留未見資料驗證。

### 換一個現場再推理
加入外觀不同的新產品，想沿用既有模型和門檻。

**問題：** 共用模型是否代表不需新資料？

**核對：** 仍需新產品正常涵蓋、獨立驗證與適配評估；更新後同時重驗既有產品，避免平均分掩蓋退步。
<!-- topic-learning-bridge:end -->
## Model identity

This course's UniAD is **"A Unified Model for Multi-class Anomaly Detection" (NeurIPS 2022)**, not the autonomous-driving project or later same-name papers. It aims to replace separate per-category normal-only anomaly models with one shared multi-class feature-reconstruction model. Plain reconstruction can learn an *identity shortcut* that reconstructs both normal and anomalous features; UniAD counteracts that risk through layer-wise query decoding, neighbor-masked attention, and feature jittering.

## Architecture path

### Build

Multi-class clean normal ROI -> versioned resize / normalize -> pretrained visual backbone -> selected multi-layer feature maps -> feature jittering during training -> layer-wise query decoder -> neighbor-masked attention -> reconstructed feature maps -> layer-wise feature residual -> resize / fuse / aggregate -> image score.

The trainable decoder has layer-specific learned queries that model the distinct feature layers rather than applying one undifferentiated reconstruction head. Neighbor-masked attention prevents nearby input features from leaking directly into the reconstruction, so the decoder cannot trivially copy the anomalous feature. Feature jittering perturbs training features and forces recovery of the intended normal message. Retain the backbone checkpoint and frozen-state audit, selected feature layers and shapes, query count / dimensions, attention mask definition, jitter distribution, feature normalization, losses, seed, optimizer, schedule, decoder checkpoint, and calibration state.

### Inference

Test ROI -> the same backbone / layer selection / normalization -> layer-wise query decoder with neighbor masking -> reconstructed feature maps -> feature residual at each layer -> locked spatial resize / fusion -> anomaly map -> image aggregation -> threshold -> PASS / REVIEW / HOLD.

The score is an input-feature versus reconstructed-feature discrepancy, not a class probability. The aggregation is part of the deployed definition: the official implementation documents mean, max of an averaged-pool map, and standard-deviation alternatives; a course or deployment must state which one is used, rather than carrying over a benchmark default silently.

## Representation and score

- Normality representation: one shared decoder, layer-wise queries, and neighbor-masked reconstruction state fitted over the declared set of normal product categories.
- Multi-class control: the category roster, examples per category, normal-mode / lot / view coverage, and sampling policy are part of the normal distribution—not bookkeeping outside the model.
- Local evidence: per-layer feature reconstruction residual, under fixed backbone, selected tensor, feature normalization, decoder, query, and neighbor-mask state.
- Final map and image score: versioned resize / fusion of residual maps, followed by a named mean / max / standard-deviation or other aggregation and threshold policy.
- The score is an anomaly operating signal; it does not identify a class or constitute a calibrated defect probability.

## Cost and operating contract

Version together:

- exact NeurIPS-2022 UniAD implementation / commit, backbone architecture and checkpoint, frozen-state audit, selected feature layers, tensor shapes, feature normalization, and input image recipe;
- decoder architecture, layer-wise query count / dimensions / initialization, neighbor-masked attention geometry, feature-jitter distribution / rate, hidden dimensions, losses, optimizer, schedule, seeds, precision, and decoder checkpoint;
- multi-class normal IDs, class roster, sample balance / sampler, split, contamination audit, normal modes, lot / view / illumination coverage, and validation partition;
- ROI, registration, input size, crop / padding, colour conversion, transforms, feature extraction pre-processing, and order of every augmentation;
- per-layer residual definition, map resize / fusion weights, smoothing / masks, image aggregation policy, calibration / threshold revision, and decision unit;
- per-category and pooled local/global localization, low-FPR escape, false reject / review load, query / mask / jitter ablation, hold-out classes or future product evidence, drift results, and reconstruction-feature visual review;
- pre-processing, backbone, decoder, post-processing, tiling, complete image-to-decision P50 / P95 / P99, VRAM / RAM, state size, batch policy, export engine, and hardware.

## Failure boundary

- If the query decoder or neighbor mask is weakened, input information can leak into reconstruction and recreate anomalous features—an identity shortcut that suppresses residuals.
- Overly strong masking, jitter, or insufficient decoder capacity can erase normal microstructure and increase false rejects; these are operating parameters, not cosmetic regularizers.
- A shared model can suffer inter-class imbalance or under-covered normal modes: common categories may dominate the normal representation while rare categories drift into anomaly score tails.
- A pretrained backbone, feature layer, stride, ROI, registration, crop, input resolution, illumination, focus, or colour shift can destroy effective-pixel evidence or look anomalous independent of product quality.
- Residual maps can miss globally illogical assemblies when local backbone features remain plausible; conversely fine defects can disappear below feature stride.
- Per-layer fusion, resize, aggregation, calibration, and threshold can alter low-FPR behaviour. A good-looking residual map is not release evidence.
- A unified-model benchmark number does not prove a factory can retire its per-class models: the actual category roster, support coverage, class balance, latency, review burden, and drift must be measured.

## Selection gate

Consider UniAD when several product categories can share one governed anomaly-detection pipeline, clean normal support is available across that class roster, and the expected value of reduced model operations outweighs the validation burden of a shared distribution. First reproduce the pinned official configuration; then validate every category and future / drift split under a fixed ROI, effective-pixel, score, threshold, and decision contract.

Hold or compare alternatives when product categories are not governed, rare-class normal coverage is poor, small defects fall below the selected feature stride, global logical faults dominate, the identity-shortcut controls are unpinned, or pooled benchmark results mask per-category low-FPR failure. Compare with DRAEM and Dinomaly using the same category roster, normal-fit / challenge / future split, ROI / registration, effective pixels, input, aggregation, threshold, hardware, and decision unit.

## Visual primitives

- `multiclass_support`: normal product categories, balance / sampler, clean support, rare-mode coverage, contamination, and future drift.
- `feature_path`: ROI -> frozen pretrained backbone -> selected multi-layer feature tensors -> feature normalization.
- `shortcut_controls`: feature jittering, layer-wise query decoder, neighbor-masked attention, and the blocked identity-copy path.
- `reconstruction_score`: reconstructed layer features, per-layer residuals, resize / fusion, anomaly map, aggregation, threshold, and PASS / REVIEW / HOLD.
- `evidence_review`: reconstructed-feature visualization, query / mask / jitter ablations, category-level and pooled low-FPR / review-load evidence, full P95/P99, and drift.
- `selection_gate`: category governance, class imbalance, effective pixels, global logic, shortcut-control audit, shared-pipeline value, and per-category future evidence.

## Evidence bundle

Keep the exact UniAD version / commit and official config; backbone and decoder checkpoints; feature-layer / tensor / normalization definition; layer queries, neighbor-mask, jitter, loss, and seed state; category roster and normal-fit IDs; sample balance and contamination audit; ROI / registration / transform / input contract; reconstructed-feature and residual visualizations; per-layer residual / fusion / aggregation / calibration / threshold revisions; query / mask / jitter ablations; category-level plus pooled low-FPR escape, false reject / review load, local/global localization, P50/P95/P99, memory / state; future / drift results; and a rebuild trigger.

## Sources

- You et al., "A Unified Model for Multi-class Anomaly Detection," NeurIPS 2022 / arXiv:2206.03687.
- Official implementation: https://github.com/zhiyuanyou/UniAD
- Course source: `full-model-course/04-anomaly-detection.md`, pages 04-39 through 04-42.

## Production gate

Research contract and visual primitives are complete. Pages 04-39 through 04-42 may proceed to white high-density C / D visual production and model-local QA.

## F01 模型中心思想與來源核對

產品種類多，不想每類維護一個模型；但共享重建器容易直接抄回異常。UniAD限制偷看鄰近答案的路徑，讓一個模型學多類正常特徵的共同規律。

**共享正常訓練**：多類正常影像進同一特徵重建模型；共享模型不代表各類資料都已充分覆蓋。

**阻止恆等映射**：Feature jitter 擾動訓練特徵，neighbor mask 限制近鄰連線，layer-wise queries 幫助各層重建，降低直接複製。

**對應特徵比較**：原特徵與重建特徵的差異回映位置；遮住的是特徵路徑，不是把原照片塗黑當正式輸入。

**移除設計自測**：解除近鄰遮罩，重建誤差更低就代表偵測更好嗎？

不一定；模型若學到直接複製，連異常也能重建，殘差變低反而漏檢。需要以未见異常驗證，而不只看正常訓練 loss。

**選型**：多產品共享訓練可列候選；各產品分開量誤報和漏檢。新類別加入後檢查旧類別，避免大宗產品掩蓋少數類別。

[原論文／官方來源](https://arxiv.org/abs/2206.03687)。本輪原生 SVG 結合既有生成金屬件；特徵與差異為教學設定，沒有新增推論。先前章節如描述應用擴充，不應解讀為原模型必需步驟。

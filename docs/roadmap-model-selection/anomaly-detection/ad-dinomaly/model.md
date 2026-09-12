# Dinomaly (`ad-dinomaly`)

- roadmap category: `anomaly-detection`
- course pages: `04-43` through `04-46`
- research status: `complete`
- visual status: `ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/ad-dinomaly.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
多類產品共用檢測：用強特徵與受限制的重建，追查細刮傷及正常外觀。

### 它交出什麼，也不交出什麼
提供可疑位置與候選分數；不直接交付尺寸、根因或放行判定。

### 一句心智模型
本課採原版 Dinomaly。固定 DINOv2 提取特徵，多類正常資料訓練瓶頸與解碼器；Dropout 在訓練時擾動表示，線性注意力分散聚合，多層分組與寬鬆重建減少硬性逐層逐點照抄。推論關閉 Dropout，比較特徵差異後回看 p。

**限制：** 正常外觀可能誤報，缺陷也可能被重建；按產品保留未見資料驗證。

### 換一個現場再推理
加入外觀不同的新產品，想沿用既有模型和門檻。

**問題：** 共用模型是否代表不需新資料？

**核對：** 仍需新產品正常涵蓋、獨立驗證與適配評估；更新後同時重驗既有產品，避免平均分掩蓋退步。
<!-- topic-learning-bridge:end -->
## Model identity

Dinomaly is the pure-Transformer reconstruction framework introduced as a 2024 preprint and published at CVPR 2025, **not** a DINO detector and not Dinomaly2. It targets multi-class unsupervised anomaly detection with a minimal encoder, bottleneck, and Transformer decoder. Its four stated ingredients are Foundation Transformers, a Noisy Bottleneck, Linear Attention, and Loose Reconstruction; together they aim to prevent feature identity mapping while retaining a comparatively efficient adapted anomaly-detection path.

## Architecture path

### Build

Multi-class clean normal ROI -> fixed image recipe -> Foundation Transformer patch tokens / selected intermediate features -> trainable adapter or encoder -> Noisy Bottleneck with dropout -> Linear-Attention Transformer decoder -> loosely reconstructed normal feature tokens -> token-wise residual -> multi-layer map and image aggregation.

The Foundation Transformer supplies universal discriminative features. Dropout in the Noisy Bottleneck injects noise so the decoder must recover normal representations instead of reproducing every input token. Linear Attention is intentionally less able to focus on individual tokens than softmax attention, limiting direct copying. Loose Reconstruction does not force dense layer-to-layer or point-to-point identity reconstruction; retain the exact layer grouping / loose-constraint and loss definition. Lock backbone checkpoint and frozen/adapted state, feature layers and shapes, adapter / decoder dimensions, dropout placement / probability, linear-attention version, loose reconstruction grouping / loss, feature normalization, optimizer, seed, schedule, checkpoint, and normal category roster.

### Inference

Test ROI -> same Foundation Transformer features -> adapted encoder / noisy-bottleneck path in its configured inference state -> Linear-Attention decoder -> reconstructed normal tokens -> input-versus-reconstruction token residual -> layer fusion / resize -> anomaly map -> named map-to-image aggregation -> threshold -> PASS / REVIEW / HOLD.

The score is feature-token reconstruction discrepancy, not a class or defect probability. The adapted path is part of the model: do not call it training-free merely because the Foundation Transformer is frozen. Distinguish its adaptation cost and latency from AnomalyDINO's training-free path.

## Representation and score

- Normality representation: Foundation-Transformer features plus the fitted noisy-bottleneck / decoder state under a declared multi-class normal support.
- Shortcut controls: dropout/noise, unfocused Linear Attention, and loose reconstruction constraints prevent the decoder from learning an identity path; their configuration is part of the anomaly detector.
- Local evidence: per-token / per-layer feature reconstruction residual under fixed layer, stride, normalization, decoder, and loss state.
- Final map and image score: versioned layer resize / fusion and a named aggregation rule with calibration, threshold, and decision unit.
- The score is an operating signal, not evidence of root cause, product class, or calibrated defect probability.

## Cost and operating contract

Version together:

- exact Dinomaly release / commit, Foundation Transformer architecture and checkpoint, selected layers, frozen/adapted modules, input recipe, feature normalization, and extraction state;
- adapter / encoder / decoder architecture, layer grouping, token dimensions, dropout placement and rate, Linear-Attention implementation / numerical settings, loose constraint / loss definition and weights, optimizer, schedule, precision, seeds, and checkpoint;
- multi-class normal IDs, class roster, sampling / balance, contamination audit, normal modes, lot / view / illumination coverage, and validation partition;
- ROI, registration, image size, crop / padding, colour conversion, transforms, patch stride, effective pixels, tiling, and every augmentation order;
- per-layer residual, resize / fusion, map smoothing / mask, aggregation, calibration / threshold revision, and decision unit;
- per-category and pooled low-FPR escape, false reject / review load, localization, dropout / attention / loose-reconstruction ablations, future / drift results, feature-reconstruction review, and failure images;
- adaptation / training cost, pre / feature / decoder / post and complete image-to-decision P50/P95/P99, VRAM/RAM, state size, export engine, batch policy, and exact hardware.

## Failure boundary

- Feature-domain mismatch, unsuitable Foundation Transformer layer, stride, ROI, resolution, registration, colour, focus, or illumination can make normal variation look anomalous or erase small defects.
- Too little bottleneck noise, attention that can focus too directly, or overly strict point-wise reconstruction can restore anomalous tokens and suppress residuals; too much noise or loose reconstruction can erase normal structure and elevate false rejects.
- A unified multi-class support can under-cover rare classes or normal modes, causing class-specific score tails and drift that pooled metrics conceal.
- Loose layer grouping, layer fusion, aggregation, calibration, and threshold can change low-FPR behaviour even when maps appear plausible.
- Token residuals may not detect globally incorrect assemblies if local tokens remain familiar, and fine defects can fall below patch / feature stride.
- Benchmark-only results or a frozen-backbone claim do not cover adaptation cost, complete latency, review load, or factory drift.

## Selection gate

Consider Dinomaly when Foundation Transformer features are already demonstrably useful for the visual domain, a multi-class normal roster is governed, and engineering is willing to validate the adapted noisy-bottleneck / decoder path rather than assume a training-free DINO solution. Start from the pinned official configuration; then measure every category under a fixed ROI, effective-pixel, aggregation, threshold, hardware, and decision contract.

Hold or compare alternatives when feature-domain fit is unclear, rare-class coverage is weak, patch stride misses critical defects, global logical anomalies dominate, shortcut-control configuration is unpinned, or adaptation cost and per-category low-FPR are not measured. Compare with UniAD and DRAEM under the same roster, normal-fit / challenge / future split, image recipe, effective pixels, threshold, hardware, and decision unit.

## Visual primitives

- `multiclass_support`: category roster, sample balance, clean normal modes, contamination, rare category, and future drift.
- `foundation_feature_path`: ROI -> Foundation Transformer -> selected patch tokens / layers -> feature normalization.
- `shortcut_controls`: dropout Noisy Bottleneck, Linear Attention, Loose Reconstruction grouping / loss, and blocked identity-token path.
- `reconstruction_score`: loosely reconstructed token features, token residual, layer fusion, anomaly map, image aggregation, threshold, and gate.
- `evidence_review`: adapted versus training-free path, dropout / attention / loose-loss ablations, reconstructed-feature review, per-category low-FPR, review load, P95/P99, and drift.
- `selection_gate`: feature-domain fit, category governance, effective pixels, global logic, adaptation cost, shortcut audit, and rebuild trigger.

## Evidence bundle

Keep Dinomaly version and official config; Foundation checkpoint and adapter/decoder checkpoints; dropout, Linear-Attention, loose grouping/loss, token/layer/normalization state; category roster and normal IDs; support balance and contamination audit; ROI / registration / transform / patch contract; reconstructed token and residual visualizations; layer fusion / aggregation / calibration / threshold revisions; component ablations; per-category plus pooled low-FPR / false reject / review load / localization; adaptation and complete P50/P95/P99 cost; memory/state; future/drift splits; and a rebuild trigger.

## Sources

- Guo et al., "Dinomaly: The Less Is More Philosophy in Multi-Class Unsupervised Anomaly Detection," CVPR 2025 / arXiv:2405.14325.
- Official implementation: https://github.com/guojiajeremy/Dinomaly
- Course source: `full-model-course/04-anomaly-detection.md`, pages 04-43 through 04-46.

## Production gate

Research contract and visual primitives are complete. Pages 04-43 through 04-46 may proceed to white high-density C / D visual production and model-local QA.

## F01 模型中心思想與來源核對

多產品異常檢測想共享強表徵，又不希望重建器把異常照抄。Dinomaly把基礎 Transformer 特徵與刻意不精細照抄的重建設計結合。

**基礎表徵**：固定預訓練 Transformer 提供可跨產品的 tokens；這和 AnomalyDINO 的直接查庫不同，後面仍要訓練重建器。

**打散直接複製**：Noisy bottleneck 用 dropout 擾動；linear attention 不容易只聚焦單一輸入 token，鼓勵利用較廣資訊。

**寬鬆重建**：Loose reconstruction 不強求逐層逐點精確照抄；組合多層特徵作重建比較，用落差找可疑局部。

**移除設計自測**：把重建訓練完全拿掉，只保留 DINO 特徵，還是 Dinomaly 嗎？

不是；還需另一個比較方法才能形成異常分數。若改查正常 token 庫，流程更接近 AnomalyDINO，維護成本與正常知識保存位置都改變。

**選型**：有多類正常資料且願意訓練共享 decoder 時可試；與 UniAD 比較防照抄設計，也與 AnomalyDINO 比建庫和訓練成本。此題限原版 Dinomaly。

[原論文／官方來源](https://github.com/guojiajeremy/Dinomaly)。本輪原生 SVG 結合既有生成金屬件；特徵與差異為教學設定，沒有新增推論。先前章節如描述應用擴充，不應解讀為原模型必需步驟。

<!-- wi033-engineering:start -->
## WI-033 工程圖修正

### Dinomaly：多类正常，共用重建路徑

固定DINOv2，多類正常共同訓練MLP及解碼器；位置差異是覆核線索。各類正常變化與真缺陷分開留出，不用整體平均掩蓋弱類。

共同訓練仍需逐產品驗證。

來源：https://arxiv.org/html/2405.14325v5

### Dinomaly：限制照抄，再分組比較

固定DINOv2，用正常特徵訓練瓶頸及解碼器；訓練MLP Dropout阻止直接照抄，eval關閉。線性注意力降低聚焦相同位置的捷徑；多層按組相加後比較，放寬逐層對應。訓練另降低已重建良好位置的梯度影響。圖中兩組/小格為機制示意，不是固定層號或維度。

訓練擾動與分組對照，要和推論設定分開。

來源：https://arxiv.org/html/2405.14325v5

### Dinomaly：訓練擾動，部署要關閉

保存骨幹、MLP、解碼器、使用層和分組、前處理及評分。Dropout只於訓練；放鬆逐層配對與難位置訓練策略不等於省略驗證。部署需eval，變更分組後重新驗。

保存層分組與eval設定，才可重現差異。

來源：https://arxiv.org/html/2405.14325v5

### Dinomaly：低重建差，不保證無刮傷

給定原與重建表示同為[.6,.8]，餘弦差0；原圖刮傷仍在。Dropout和線性注意力針對照抄捷徑，不保證每个缺陷有大差異。

限制照抄是手段，缺陷仍要用真例驗證。

來源：https://arxiv.org/html/2405.14325v5

<!-- wi033-engineering:end -->

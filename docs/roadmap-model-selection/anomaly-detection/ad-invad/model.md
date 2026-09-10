# InvAD (`ad-invad`)

- roadmap category: `anomaly-detection`
- course pages: `04-55` through `04-58`
- research status: `complete`
- visual status: `ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/ad-invad.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
想保留多產品正常細節：以輸入條件調制特徵重建，再用差異找可疑處。

### 它交出什麼，也不交出什麼
提供可疑位置與候選分數；不直接交付尺寸、根因或放行判定。

### 一句心智模型
固定影像骨幹提取特徵，經融合、重新縮放與風格轉換得到空間條件。解碼器從共享起始特徵出發，以 SSM 空間風格調制各位置的表示；用正常資料學重建路徑，推論比較原始與生成特徵的差異。

**限制：** 正常外觀可能誤報，缺陷也可能被重建；按產品保留未見資料驗證。

### 換一個現場再推理
加入外觀不同的新產品，想沿用既有模型和門檻。

**問題：** 共用模型是否代表不需新資料？

**核對：** 仍需新產品正常涵蓋、獨立驗證與適配評估；更新後同時重驗既有產品，避免平均分掩蓋退步。
<!-- topic-learning-bridge:end -->
## Model identity

This course's InvAD is the 2024 **feature-inversion** model from *Learning Feature Inversion for Multi-class Anomaly Detection under General-purpose COCO-AD Benchmark*. It learns a forward network that reconstructs normal-like encoder features from a constant query under input-dependent spatial style modulation. Anomaly evidence is the reconstruction residual of features.

The word *inversion* refers to this learned forward feature-reconstruction design inspired by GAN inversion; it does **not** mean running per-image latent optimization at inference. Do not substitute the later same-name diffusion latent-inversion work as its source, architecture, or latency contract.

## Architecture path

### Build

Declared multi-class normal roster -> fixed ROI / registration / resize / colour / normalization -> image encoder -> multi-scale input features -> rescaling upsampler -> style translator -> spatial style features -> constant feature query -> stacked Spatial Style Modulation (SSM) feature decoder -> recovered normal-like features. Optimize the declared feature reconstruction objective on normal data and version the residual / map aggregation rule.

The rescaling upsampler aligns feature scales; the style translator makes reduced style features; the feature decoder receives constant-query features and is dynamically modulated by these spatial style features. Version the image encoder and selected layers, rescaling channels / operations, style-translator definition, constant-query shape / initialization, every SSM block and normalization operation, decoder channels / stack counts, normal categories and balance, loss, image recipe, residual distance, map resize / smoothing / aggregation, calibration, threshold, decision unit, seed, optimizer, and checkpoint selection.

### Inference

Test ROI -> same preprocessing -> image encoder -> rescaling upsampler -> style translator -> constant query plus SSM feature decoder -> reconstructed normal-like features -> versioned feature residual map / score -> aggregation -> threshold -> PASS / REVIEW / HOLD.

Record input, input feature, style feature, reconstructed feature, residual map, and final decision together. InvAD is a single learned encoder-to-decoder forward path: measure complete P50/P95/P99 from acquisition / preprocessing through encoder, rescaling, style translation, SSM decoder, residual / aggregation, and hand-off. Do not add fictional per-image inversion iterations to P95 or claim a feature reconstruction is a pixel-space repair image.

## Representation and score

- Normality representation: the normal-trained feature-inversion path, including selected encoder features, style translation, constant query, SSM decoder state, and residual rule.
- Local evidence: feature reconstruction discrepancy, typically a declared distance between input and recovered normal-like features at each selected scale; a reconstruction or residual visualization alone is not final evidence.
- Image score: a versioned map resize / smoothing / masking / aggregation / threshold rule under a declared decision unit.
- The score is an anomaly operating signal, not a calibrated defect probability, root-cause label, proof that all normal styles are covered, or proof that a strong decoder cannot reconstruct anomalous features.

## Cost and operating contract

Version together:

- InvAD release / commit, image-encoder checkpoint / layers / freeze policy, rescaling upsampler, style translator, constant-query initialization, SSM equations / stack counts / channels, decoder checkpoint, precision, optimizer, schedule, loss, seed, and checkpoint hashes;
- normal-fit IDs, split, contamination audit, category balance / sampling policy, normal modes, lots, views, illumination, and normal validation used for calibration;
- ROI, registration, input resolution, crop / padding, colour conversion, transforms, normalization, feature-layer selection / scale alignment, and augmentation order;
- residual distance / normalization / scale weights, map resize / smoothing / masking / aggregation, calibration / threshold revision, decision unit, and review policy;
- reconstruction residual, anomaly-reconstructed false negative, normal-style false reject, low-FPR, review load, local/global localization, per-class evidence, and real challenge / future / drift results;
- training cost and complete single-forward image-to-decision P50/P95/P99, VRAM/RAM, state size, batch policy, repeatability, and hardware.

## Failure boundary

- A high-capacity feature decoder can reconstruct anomalous feature patterns, reducing residuals and hiding a defect; inspect real escaped defects, not only mean reconstruction loss.
- Encoder domain mismatch, style / illumination / view shifts, and under-covered normal categories can change features or style controls and create false rejects.
- Rescaling, layer selection, style-feature channel reduction, SSM stack count, constant-query initialization, and residual distance change both compute and localization behavior.
- Pixel-scale tiny defects may fall below effective feature resolution; map interpolation, smoothing, aggregation, calibration, and threshold can hide them further.
- A credible local feature residual does not solve global assembly / count / sequence / relational logic anomalies.
- Do not confuse the model identity with same-name diffusion inversion work, and do not report a per-image optimization loop as this model's cost.

## Selection gate

Consider InvAD for a multi-class AD research path when a team wants to validate input-dependent feature reconstruction using SSM and can govern the feature architecture, category support, effective pixels, residual rule, and real holdout. Verify escaped defects, normal-style false rejects, low-FPR / review load, per-class balance, drift, and complete single-forward P95.

Hold or compare alternatives when encoder / style domain stability is unknown, a high-capacity decoder recreates defects, critical targets are below effective pixels, global logic dominates, the category roster is unbalanced, or the version identity is unclear. Compare DDAD, DiffusionAD, AE-family methods, and InvAD under the same normal support, ROI, effective pixels, image recipe, threshold policy, hardware, decision unit, real escapes, P95, and error taxonomy.

## Visual primitives

- `feature_inversion_path`: image encoder -> rescaling upsampler -> style translator -> constant query -> SSM decoder -> recovered normal-like features.
- `spatial_style_modulation`: style feature supplies space-aware scale / shift controls to the normalized decoder feature, not a generic latent optimization loop.
- `feature_residual_score`: selected input / recovered features -> residual map -> aggregation -> decision.
- `forward_cost_contract`: encoder-to-decoder one-pass state, complete P95/P99, hardware, repeatability, and excluded fictional inversion iterations.
- `selection_gate`: decoder-over-reconstruction, encoder / style drift, category balance, effective pixels, global logic, and fair DDAD/DiffusionAD/AE comparison.

## Evidence bundle

Keep normal IDs and contamination audit; category roster / balance; image recipe; encoder / upsampler / style-translator / constant-query / SSM decoder definitions and checkpoints; selected feature layers / residual state; input / feature / style / recovered-feature / residual-map / decision records; escaped-defect and normal-style false-reject examples; per-class / per-mode evidence; low-FPR, review-load, localization, calibration, and threshold revisions; single-forward P95/P99 / state / hardware records; real future / drift split; and a rebuild trigger.

## Sources

- Zhang et al., "Learning Feature Inversion for Multi-class Anomaly Detection under General-purpose COCO-AD Benchmark," arXiv:2404.10760 (2024), [official InvAD project](https://zhangzjn.github.io/projects/InvAD/).
- Course source: `full-model-course/04-anomaly-detection.md`, pages 04-55 through 04-58.

## Production gate

Research contract and visual primitives are complete. Pages 04-55 through 04-58 may proceed to white high-density C / D visual production and model-local QA.

## F01 模型中心思想與來源核對

多類產品既有形狀又有細節，單純重建可能還原得不合適。InvAD學習把編碼特徵反演回去，用空間相關的樣式資訊控制特徵重建。

**特徵作為輸入條件**：影像 encoder 提供多尺度特徵；rescaling 和 style translator 將它們轉為重建的控制資訊。

**從固定 query 重建**：解碼端從可學習的固定輸入出發，以空間樣式調制引導生成特徵；這裡的 SSM 指 Spatial Style Modulation。

**比较特徵差異**：原始與反演特徵逐尺度比較形成線索；模型訓練後是前向運算，不是每張測試圖再做反覆最佳化。

**移除設計自測**：拿掉空間樣式條件，只讓 decoder 從同一固定 query 生成，會失去什麼？

會失去依待測內容在不同位置調整重建的資訊，難以對應不同產品。固定 query 不是從資料庫選一張正常照片。

**選型**：多類共享特徵重建的候選；和 RD4AD 比瓶頸反向重建、和 UniAD 比防照抄。分別驗證背景、正常細節與小缺陷。

[原論文／官方來源](https://arxiv.org/abs/2404.10760)。本輪原生 SVG 結合既有生成金屬件；特徵與差異為教學設定，沒有新增推論。先前章節如描述應用擴充，不應解讀為原模型必需步驟。

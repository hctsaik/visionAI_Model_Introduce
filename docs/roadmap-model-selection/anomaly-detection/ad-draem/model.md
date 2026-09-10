# DRAEM (`ad-draem`)

- roadmap category: `anomaly-detection`
- course pages: `04-35` through `04-38`
- research status: `complete`
- visual status: `ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/ad-draem.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
同一兩孔金屬板有很多正常照片，真實刮傷種類收不齊。先從正常圖製作合成練習題，再驗證是否真的能找出待測板 A 的刮傷 p。

### 它交出什麼，也不交出什麼
原始影像、重建估計與判別網路的可疑位置圖，用於定位覆核；不直接提供真實缺陷機率、精密輪廓、尺寸或自動放行。

### 一句心智模型
正常原圖提供重建目標，合成區域 mask 提供定位目標。推論把待測原圖與重建一起交給判別器，不需要提供 mask。

**限制：** 合成外觀可能與真實缺陷不同；重建和判別都可能失敗，必須用未見真實影像查誤報與漏檢。

### 換一個現場再推理
產線下一個需求是找漏裝零件，不只是表面紋理異常。

**問題：** 在正常照片貼紋理，能證明模型會理解零件存在與裝配關係嗎？

**核對：** 不能。需收集代表性的漏裝與正常變化驗證，考慮物件偵測或幾何關係檢查；DRAEM 仍可測，但不能把局部合成污點成績當成漏裝能力。
<!-- topic-learning-bridge:end -->
## Model identity

DRAEM (Discriminatively Trained Reconstruction Anomaly Embedding Model) is a normal-only surface-anomaly method that creates *synthetic* anomalous images during training. A reconstruction sub-network learns to turn the corrupted image back toward normal appearance; a discriminative sub-network then sees the original corrupted image together with its reconstruction and learns a per-pixel anomaly decision boundary. It is not a generic reconstruction-error baseline, and synthetic defects are training supervision—not proof that the simulator matches a factory's real defect mechanism.

## Architecture path

### Build

Clean nominal ROI -> versioned registration / resize / colour / normalization -> sampled external anomaly texture or noise -> Perlin-noise-derived mask -> augmentation / opacity / blending -> synthetic corrupted image `I_a` and pixel mask `M_a`.

`I_a` enters the reconstruction encoder-decoder, which produces a normal-looking reconstruction `I_r`. The original corrupted appearance and the reconstruction are concatenated into a joint reconstruction-anomaly embedding. A discriminative segmentation network produces the pixel anomaly map `M_o`. Training couples the reconstruction objective (the paper uses SSIM plus L2) with the discriminative segmentation loss. Retain exact normal IDs, anomaly-texture provenance, mask generator, threshold / blend ranges, augmentations, reconstruction and segmentation definitions, loss weights, seeds, and checkpoints.

### Inference

Real test ROI -> the same registration / resize / colour / normalization -> reconstruction network -> reconstructed image -> concatenate test image and reconstruction -> discriminative segmentation network -> anomaly probability map -> locked smoothing / aggregation -> image score -> threshold -> PASS / REVIEW / HOLD.

At deployment, no synthetic corruption is supplied. The synthetic generator affects the model indirectly through its trained decision boundary and must remain part of the released model state. A bright reconstruction residual alone is not the DRAEM decision; the discriminative map is the primary localization output.

## Representation and score

- Normality representation: the reconstruction weights plus a discriminator trained on the joint original/reconstruction appearance, under a locked synthetic-anomaly recipe and normal-fit recipe.
- Synthetic training evidence: source texture or noise, Perlin / mask generator, geometric and colour augmentation, mask occupancy, opacity / blend distribution, and the generated `I_a, M_a` pairs.
- Local evidence: the discriminative segmentation map from the joint `I_a` / `I_r` (or real test image / reconstruction) embedding.
- Image score: a versioned aggregation of the predicted pixel anomaly map; smoothing, resize, ROI masking, aggregation, threshold, and decision unit must be explicit.
- The output is an anomaly operating signal, not a calibrated defect probability or a demonstration that the simulator covers real failures.

## Cost and operating contract

Version together:

- reconstruction and discriminative network architectures, input size, channels, SSPCAB setting if enabled, precision, optimizer, schedule, epochs, seeds, checkpoint hashes, and loss weights;
- normal-fit IDs, contamination audit, lot / view / illumination coverage, split and real normal validation partition;
- anomaly-source dataset or random-noise configuration, its provenance / licence, Perlin mask parameters, mask-area distribution, texture transforms, rotation, blending / opacity range, and synthetic-generation seed;
- registration, ROI / mask, input resolution, crop / padding, colour conversion, transforms, and all normal and synthetic augmentation order;
- reconstruction target, SSIM / L2 recipe, discriminative segmentation target / loss, predicted-map smoothing / resize / aggregation, calibration, threshold revision, and decision unit;
- synthetic-to-real challenge set, real failure images, mask quality, critical-defect recall, low-FPR escape, false reject / review load, local / global localization, seed spread, and future / drift results;
- training time, pre / forward / post and complete image-to-decision P50 / P95 / P99, VRAM / RAM, state size, batch policy, and exact hardware.

## Failure boundary

- Synthetic texture, mask shape, opacity, blending, or augmentation can bias the discriminator toward simulator artefacts rather than real defect mechanisms.
- A simulator that fails to cover subtle, low-contrast, structured, or process-specific defects can look strong on synthetic masks yet miss production failures.
- Synthetic masks supervise local visual anomalies; missing parts, semantic assembly errors, and long-range logical inconsistencies may remain weak when their local appearance resembles normal background.
- Registration, illumination, focus, texture, compression, crop, colour, and background changes can resemble synthetic corruptions and inflate false rejects.
- The reconstruction network can remove a meaningful real feature, preserve a synthetic-looking artefact, or create texture differences; inspect input, reconstruction, discriminative map, and final decision together.
- Normal-support contamination and under-covered normal modes distort both reconstruction and the synthetic-vs-normal boundary.
- Post-map smoothing, aggregation, calibration, and threshold can hide small anomalies or change low-FPR behaviour even when the visual map looks plausible.
- A paper or model-forward timing number excludes acquisition, transfer, ROI, synthetic-free preprocessing, post-processing, PLC hand-off, and queueing unless these are measured explicitly.

## Selection gate

Consider DRAEM when real defect examples are scarce, clean nominal support exists, and engineering can specify a controlled synthetic anomaly recipe that is plausibly useful for the surface task. Require a held-out real challenge set and inspect synthetic-to-real gap, pixel-mask behaviour, critical recall, low-FPR escape, false reject / review load, and complete P95 before release.

Hold or compare alternatives when the simulator cannot be governed, real faults are primarily global / logical, critical defects are below the effective pixel budget, optical stability is poor, or score calibration and real-holdout evidence are missing. Compare DRAEM with AE and SimpleNet under the same normal-fit / challenge / future split, ROI / registration, effective pixels, input, threshold policy, hardware, and decision unit. Report real—not synthetic-only—challenge behaviour.

## Visual primitives

- `synthetic_recipe`: clean normal ROI, anomaly-source texture or noise, Perlin mask, transform, opacity / blending, corrupted image, and pixel mask.
- `reconstruction_path`: corrupt image -> encoder-decoder -> normal-looking reconstruction, with SSIM + L2 reconstruction contract.
- `joint_embedding`: original corrupted or test image concatenated with reconstruction before the discriminative segmentation network.
- `score_map`: discriminative pixel anomaly map, smoothing / ROI mask / aggregation, image score, threshold, and PASS / REVIEW / HOLD gate.
- `evidence_review`: synthetic-to-real comparison, input / reconstruction / map triplet, real failure images, mask quality, critical recall, low-FPR, review load, and full latency.
- `selection_gate`: simulator governance, texture bias, global logical anomaly, effective pixels, optics / registration, real challenge evidence, and drift rebuild trigger.

## Evidence bundle

Keep normal-fit IDs and contamination audit; external texture / noise provenance and licence; Perlin / mask, augmentation, opacity, blending, and seed recipe; synthetic `I_a, M_a` examples; network and loss definitions; input / reconstruction / discriminator-map triplets; real challenge / future / drift splits; synthetic-to-real gap; mask quality; low-FPR escape; false reject / review load; local / global localization; critical-defect recalls; map aggregation / calibration / threshold revisions; complete P50/P95/P99; memory / state size; and a drift rebuild trigger.

## Sources

- Zavrtanik, Kristan, and Skočaj, "DRAEM: A Discriminatively Trained Reconstruction Embedding for Surface Anomaly Detection," ICCV 2021 / arXiv:2108.07610.
- Anomalib DRAEM reference documentation: https://anomalib.readthedocs.io/en/v2.1.0/markdown/guides/reference/models/image/draem.html
- Course source: `full-model-course/04-anomaly-detection.md`, pages 04-35 through 04-38.

## Production gate

Research contract and visual primitives are complete. Pages 04-35 through 04-38 may proceed to white high-density C / D visual production and model-local QA.

## F01 模型中心思想與來源核對

單純相減容易把重建的小誤差也當缺陷。DRAEM先用合成破壞製作練習題，讓重建網路和判別網路一起學哪些差異值得標出。

**正常圖造練習題**：正常影像加合成異常，同時知道未破壞的影像及合成區域 mask；不需先收齊真實缺陷標籤。

**重建正常外觀**：重建網路學把受損影像還原成正常目標；這只是第一個子網路。

**學習判讀差異**：判別網路同時看受損原圖與重建圖，用合成 mask 監督位置預測；推論不需要提供這張 mask。

**移除設計自測**：拿掉判別網路，只做原圖減重建，會少什麼？

會失去學習式差異判讀，退回殘差基準。反之，即使有判別網路，若只記住合成紋理，對真實新缺陷仍可能漏檢。

**選型**：能設計代表性合成破壞並訓練時可試；務必以未參與訓練的真實正常／缺陷驗證，不能拿合成成功率當現場成績。

[原論文／官方來源](https://arxiv.org/abs/2108.07610)。本輪原生 SVG 結合既有生成金屬件；特徵與差異為教學設定，沒有新增推論。先前章節如描述應用擴充，不應解讀為原模型必需步驟。

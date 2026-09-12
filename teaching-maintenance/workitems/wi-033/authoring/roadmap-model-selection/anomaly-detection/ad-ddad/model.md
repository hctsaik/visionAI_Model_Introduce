# DDAD (`ad-ddad`)

- roadmap category: `anomaly-detection`
- course pages: `04-51` through `04-54`
- research status: `complete`
- visual status: `ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/ad-ddad.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
金屬板表面有刮傷 p，正常孔邊 q 也會反光；需要定位線索並控制誤報、漏檢與時間。

### 它交出什麼，也不交出什麼
輸出候選異常位置和分數；不是正常真值、尺寸或自動放行結果。

### 一句心智模型
先以正常資料訓練去噪模型，並用正常／近似恢復影像做特徵適配。測試時以原圖 A 為條件，逐步去噪得到恢復估計 R；像素差異與適配特徵差異加權整合，產生異常位置圖。原圖條件不是正常真值，也沒有額外學習式分割頭。

**限制：** 恢復可能保留缺陷或改動正常外觀，需以獨立資料驗證。

### 換一個現場再推理
從霧面金屬換到鏡面金屬。

**問題：** 原有正常知識和門檻可直接沿用嗎？

**核對：** 先核對光照及允收反光，補正常涵蓋並評估重訓／適配；再用未見正常和真缺陷重驗，不能把反光熱點直接當缺陷。
<!-- topic-learning-bridge:end -->
## Model identity

This course's DDAD is **Denoising Diffusion Anomaly Detection** from *Anomaly Detection with Conditioned Denoising Diffusion Models* (2023). It uses the test image as a **target condition** during conditional diffusion denoising to produce a defectless reconstruction that preserves nominal pattern and structure. An anomaly map comes from pixel-wise and feature-wise differences between the input and that reconstruction.

It is distinct from DiffusionAD: DDAD is a conditioned reconstruction-and-residual path with configurable diffusion sampling, rather than a norm-guided one-step restoration plus discriminative segmentation head. Its feature extractor may be domain-adapted with near-identical generated examples; it is not a zero-cost frozen feature comparison.

## Architecture path

### Build

Normal (and declared defect / synthetic) image protocol -> fixed ROI / registration / resize / colour / normalization -> configure conditional diffusion schedule, noise start and sampling steps -> train conditional denoiser that is guided toward target condition `x` -> defectless reconstruction `x-hat` while preserving nominal pattern. Generate near-identical examples under the recorded protocol and, where configured, fine-tune the pretrained feature extractor for domain-relevant feature comparison.

Version normal IDs, defect / synthetic protocol, conditioning definition and strength, noise schedule / beta range / start state, number and rule of sampling steps, denoiser checkpoint and loss, generated-example policy, feature-extractor checkpoint and domain-adaptation epochs / loss, pixel and feature residual normalization / weights, image recipe, map fusion / smoothing / aggregation, calibration, threshold, decision unit, seed, optimizer, and checkpoint selection.

### Inference

Test ROI `x` -> same preprocessing -> noisy source plus `x` as target condition -> conditional diffusion denoising for the locked sampling schedule -> defectless reconstruction `x-hat` -> pixel residual `|x - x-hat|` and feature residual `|phi(x) - phi(x-hat)|` -> versioned pixel / feature fusion -> localization map -> image aggregation -> threshold -> PASS / REVIEW / HOLD.

Store input, reconstruction, pixel map, feature map, fused map, sampling configuration, and final decision together. DDAD latency includes acquisition / preprocessing, all configured sampling steps, residual extraction, feature inference, fusion, aggregation, and hand-off. Do not replace its reported P95 with a single denoiser step, nor call a raw reconstruction residual the full score.

## Representation and score

- Normality representation: the conditioned diffusion reconstruction state plus the adapted (if configured) feature-comparison state fitted to the locked support and image recipe.
- Local evidence: both a pixel residual and a feature residual comparing `x` with `x-hat`; record their normalization, fusion weights, resize / smoothing, and masks.
- Image score: a versioned aggregation of the fused localization map, calibrated and thresholded under a declared decision unit.
- The score is an anomaly operating signal, not a calibrated defect probability, a root-cause label, proof that a visually plausible reconstruction is correct, or proof that the target condition has not preserved a defect.

## Cost and operating contract

Version together:

- DDAD release / commit; denoiser, diffusion schedule, start noise, target-conditioning rule / strength, sampler, number of steps, precision, checkpoint hashes, training loss, optimizer, schedule, and seeds;
- normal-fit IDs and contamination audit; declared defective / synthetic protocol; train / calibration / real challenge / future split; normal modes, lots, views, illumination, and defect taxonomy;
- ROI, registration, input resolution, crop / padding, colour conversion, transforms, normalization, target-condition construction, and augmentation order;
- generated-example recipe; feature-extractor checkpoint; feature domain-adaptation data, epochs, loss, and freeze policy; pixel / feature residual normalization and fusion;
- reconstruction, pixel map, feature map, fused map, image score, calibration / threshold revisions, decision unit, low-FPR, false reject / review load, escaped defects, local/global localization, and real future / drift results;
- training cost and complete image-to-decision P50/P95/P99 for each locked sampling-step setting, VRAM/RAM, batch policy, repeatability, state size, and hardware.

## Failure boundary

- Target conditioning can preserve or hallucinate a defect; a smooth / beautiful reconstruction is not acceptance evidence.
- Sampling schedule, noise start, and number of steps trade off cost, repeatability, and reconstruction behavior. A different sampler or step count is a different operating point.
- Normal-support contamination, defect-protocol leakage, or generated-example bias can make the model treat unwanted variation as nominal.
- Pixel residual is sensitive to registration, focus, illumination, colour, compression, resize, crop, and background; feature residual can instead hide fine defects or inherit feature-domain mismatch.
- Feature domain adaptation can overfit generated examples or leak taxonomy assumptions; validate it against a real held-out challenge set and preserve no-adaptation ablations.
- Pixel / feature residual normalization, fusion, smoothing, aggregation, calibration, and threshold can move low-FPR behavior even when component maps look credible.
- Large missing components, rare defect morphology, support drift, defects below effective pixels, and global logic errors can still escape a local reconstruction-comparison path.

## Selection gate

Consider DDAD for a research POC that specifically wants to evaluate conditional diffusion separation: target-conditioned defectless reconstruction plus declared pixel / feature residual fusion. The team must govern schedule cost, sampling-step P95, target-conditioning state, generated-feature adaptation, and real reconstruction / escape evidence.

Hold or choose another path when no latency budget exists, normal support / image registration is unstable, reconstruction bias is unmeasured, feature adaptation is benchmark-only, critical defects are below effective pixels, or global logic dominates. Compare DiffusionAD and InvAD under the same normal support, ROI, effective pixels, image recipe, threshold policy, decision unit, hardware, full P95, real escapes, and error taxonomy.

## Visual primitives

- `target_conditioning_path`: noisy source plus input-as-target condition -> conditional denoiser -> defectless reconstruction.
- `dual_residual_score`: pixel residual and domain-adapted feature residual -> normalization / fusion -> map / decision.
- `sampling_contract`: fixed schedule, noise start, sampler, number of steps, hardware, repeatability, and complete P95/P99.
- `reconstruction_evidence`: input / reconstruction / pixel-map / feature-map / fused-map quintet; defect persistence / erasure, false reject, low-FPR, and real holdout.
- `selection_gate`: schedule cost, generated-example / feature-adaptation bias, support drift, effective pixels, global logic, and fair DDAD/DiffusionAD/InvAD contract.

## Evidence bundle

Keep normal IDs and contamination audit; defect / synthetic / generated-example policy; condition, diffusion schedule, noise start, sampler and step state; denoiser / feature-extractor / adaptation checkpoints and losses; image recipe; input / reconstruction / pixel / feature / fused-map / decision sets; sampling-step cost traces; reconstruction failure and escaped-defect images; residual / fusion ablations; low-FPR, false reject, review load, localization, and future / drift evidence; calibration / threshold revisions; state and hardware records; and a rebuild trigger.

## Sources

- Mousakhan, Brox, and Tayyub, "Anomaly Detection with Conditioned Denoising Diffusion Models," arXiv:2305.15956 (2023; revised 2023, GCPR 2024 proceedings / 2025 volume).
- Course source: `full-model-course/04-anomaly-detection.md`, pages 04-51 through 04-54.

## Production gate

Research contract and visual primitives are complete. Pages 04-51 through 04-54 may proceed to white high-density C / D visual production and model-local QA.

## F01 模型中心思想與來源核對

想產生與待測工件對得上的正常對照，又怕只看像素差會受細微對位影響。DDAD用待測影像條件引導去噪，結合像素與特徵兩種差異。

**正常資料學去噪**：擴散模型以正常影像學習；推論從帶噪狀態出發，由待測影像提供條件以保留相應結構。

**條件式復原**：採樣逐步產生較正常的重建；條件太強可能保留異常，太弱則可能改掉正常結構。

**兩種差異互補**：像素差和經域適應的特徵差共同形成定位線索；特徵模型的域適應也是方法一部分，不只換一張差分圖。

**移除設計自測**：只追求重建和輸入完全相同，對异常偵測有什麼風險？

如果連異常也保留，兩種差異都可能縮小。正常保真與異常移除需要一起驗證，不能用重建越像越好作唯一目標。

**選型**：可負擔條件採樣及特徵差計算時可試；與 DiffusionAD 固定影像和硬體量端到端時間，也看對位漂移時的誤報。

[原論文／官方來源](https://arxiv.org/abs/2305.15956)。本輪原生 SVG 結合既有生成金屬件；特徵與差異為教學設定，沒有新增推論。先前章節如描述應用擴充，不應解讀為原模型必需步驟。

<!-- wi033-engineering:start -->
## WI-033 工程圖修正

### DDAD：恢復估計作為檢查對照

正常資料訓練擴散去噪與特徵適配，推論由待測影像引導恢復並比像素與特徵差。交付原圖、恢復估計及分數，R不能取代原圖作正常真值。

正常資料教恢復，原圖保留作比較。

來源：https://arxiv.org/abs/2305.15956

### DDAD：原圖引導，每步逐漸去噪

正常影像訓練去噪及適配特徵比較；測試以待測原圖引導每步去噪，得到恢復估計R。原A與R同位置的像素差和適配特徵差加權形成位置線索；恢復不是正常真值，圖中三狀態不是固定採樣步數，也不是本輪模型結果。

恢復估計與原圖的兩種差異，共同提供線索。

來源：https://arxiv.org/abs/2305.15956

### DDAD：採樣成本要計完整流程

保存噪聲/採樣/引導強度、特徵適配和整合權重。給定每步4ms，20步80ms、50步200ms，只是去噪呼叫算例，未含前後處理；不保證增加步數提高檢測。

步數是設定，速度與檢查錯誤要一起驗。

來源：https://arxiv.org/abs/2305.15956

### DDAD：恢復若保留刮傷，也可能漏檢

給定原p=40、恢復p=40，像素差0仍有刮傷；特徵差可能補充，也可能同樣小。原與恢復的相似並不是檢出證據，獨立驗漏檢。

恢復得像，不代表原圖沒有缺陷。

來源：https://arxiv.org/abs/2305.15956

<!-- wi033-engineering:end -->

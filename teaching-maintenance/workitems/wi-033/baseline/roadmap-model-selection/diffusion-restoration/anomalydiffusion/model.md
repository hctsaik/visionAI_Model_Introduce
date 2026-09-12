# AnomalyDiffusion (`anomalydiffusion`)

- roadmap family: `diffusion-restoration`
- roadmap model: `AnomalyDiffusion`
- Markdown pages: `07-06` to `07-09`
- content coverage status: `complete`
- generation status: `ready-for-visual-production`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/anomalydiffusion.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
少量刮傷總出現在相近位置，訓練資料卻需要不同位置和大小的案例。

### 它交出什麼，也不交出什麼
合成異常影像及對應遮罩；逐區核對後交給下游檢測模型。

### 一句心智模型
方法把『刮傷長什麼樣』與『要放在哪裡』拆開：用少量缺陷學外觀嵌入，另把遮罩編成位置訊號，一起引導擴散生成。去噪中比較暫時結果與正常影像，對尚不明顯的預定缺陷區加強注意力，減少小區域被忽略。

**限制：** 第二圖另換大、小菱形遮罩測試。圖中預定生成大、小兩處刮傷，假設結果只出現大刮傷。小區放大仍平整，卻保留了缺陷標註，會給下游錯誤監督。適應性注意力的設計目的就是改善這類對應，但不是逐張成功保證。

### 換一個現場再推理
生成一個大孔很穩定；改成三個小孔的遮罩後，整圖仍逼真，但部分小孔沒有出現。

**問題：** 應增加同一批影像的訓練權重，還是先改生成與資料核對？

**核對：** 先核對每個遮罩區與生成外觀，剔除錯配樣本，檢查位置條件、尺寸和注意力調整，再重產少量比較。增加錯配樣本權重會加強錯誤監督；也可測不同生成方法，但用同真實留出資料決定。
<!-- topic-learning-bridge:end -->
<!-- wi026-model-core:start -->
## WI-026 核心做法與工作取捨

方法把『刮傷長什麼樣』與『要放在哪裡』拆開：用少量缺陷學外觀嵌入，另把遮罩編成位置訊號，一起引導擴散生成。去噪中比較暫時結果與正常影像，對尚不明顯的預定缺陷區加強注意力，減少小區域被忽略。

第二圖另換大、小菱形遮罩測試。圖中預定生成大、小兩處刮傷，假設結果只出現大刮傷。小區放大仍平整，卻保留了缺陷標註，會給下游錯誤監督。適應性注意力的設計目的就是改善這類對應，但不是逐張成功保證。

希望外觀概念與位置控制分開，可選AnomalyDiffusion做候選；重視填補模型的局部概念適配可比較DefectFill；不做案例微調可比較TF-IDG。只有正常品而無缺陷參考時，先用正常性方法建立偵測基準，別把少樣本生成當成已知道所有缺陷。

新材質或缺陷型態可能需要重新學外觀並驗證位置條件。影像與遮罩是訓練候選，不是產線自動分割結果。用相同合成量、下游模型與真實留出集，比漏檢、誤報、標註一致性、生成與覆核時間。

來源：https://arxiv.org/abs/2312.05767

圖為AI生成教學示意；原工程段落為補充，首讀新版以本段及topic為準。使用者成品核准pending。
<!-- wi026-model-core:end -->
## Identity and engineering boundary

AnomalyDiffusion is a **few-shot anomaly-image generation** research method for synthetic training-data augmentation. It uses a latent-diffusion prior with a Spatial Anomaly Embedding: a learnable anomaly embedding represents appearance, while an embedding encoded from an anomaly mask represents location. An Adaptive Attention Re-weighting mechanism is proposed to improve alignment between the generated anomaly and its mask.

Its role is to create labeled synthetic anomaly candidates for a controlled downstream inspection experiment when real anomaly samples are scarce. It is not an anomaly detector, anomaly score, physical measurement, calibrated defect probability, source of production labels, or automated PASS/HOLD authority. A visually aligned generated image/mask pair still needs real-holdout, provenance, and domain-owner evidence.

## Reproducible engineering contract

### `architecture_path`

`few real anomaly image/mask references + normal target image + planned anomaly mask → named latent-diffusion checkpoint + learnable anomaly appearance embedding + mask-encoded spatial embedding → conditional denoising with adaptive attention re-weighting → synthetic anomaly image/mask/provenance → quality/domain review → fixed downstream training → stratified real-holdout evaluation and named owner action`.

### `representation_or_score`

- Appearance embedding, spatial/mask embedding, attention weights, latent denoising sample, generated image, generated mask, and a downstream classifier/segmenter score are separate representations.
- The spatial embedding and attention re-weighting target synthetic image-mask alignment. They are not a proof of physical defect geometry, sensor fidelity, defect severity, or production truth.
- Generated image/mask pairs remain synthetic training candidates; an anomaly map or score is only produced by a separately named downstream model and requires real validation.
- Preserve reference/mask source, normal target, recipe/ROI, prompt/condition, model and code revision, scheduler, guidance, seed, quality review, and real/synthetic split.

### `cost_and_operating_point`

Lock checkpoint/license/hash, data and split, reference image/mask set, normal image source/ROI, anomaly category, mask source and spatial policy, anomaly embedding training/fine-tuning revision, attention re-weighting configuration, scheduler, steps, guidance, seed, resolution/tile/blend, synthetic volume, quality filters, storage, GPU/VRAM, throughput and full experiment P95/cost. Measure the whole route from generation through review, downstream training and **real** holdout, not a single image-generation latency.

### `failure_boundary`

- Generated anomaly location can align to a mask while appearance, texture, scale, illumination, sensor noise, process semantics, or label meaning remains implausible.
- Few references can leak identities or overfit; mask policy, synthetic style, duplicated sources, and a contaminated holdout can create false downstream gains.
- Attention re-weighting and visual quality do not guarantee fine physical detail, cross-recipe transfer, rare safety modes, or an appropriate defect taxonomy.
- Model/data/license/version drift, provenance gaps, and unreviewed synthetic labels invalidate reproducibility.
- AnomalyDiffusion cannot release an asset, replace real capture, certify a part, or trigger a production action.

### `selection_gate`

Select AnomalyDiffusion only for an augmentation experiment with fixed real train/holdout, anomaly taxonomy, normal-image and mask policy, synthetic budget, downstream model, domain review, provenance/license record, and no-go action. Compare it with DefectFill/TF-IDG under the same real split, synthetic volume, placement/mask constraints, downstream training, human review, and full cost. Advance only with stratified real-holdout benefit, label integrity, mode coverage, failure-gallery review, and specialist acceptance; synthetic authenticity or mask alignment alone never passes.

### `evidence_bundle`

Preserve reference anomaly image/mask and normal-source hashes, recipe/ROI, split assignment, anomaly taxonomy, placement/mask policy, checkpoint/license/hash, code and embedding/attention revisions, prompts/conditions, scheduler/steps/guidance/seeds, generated image/mask/provenance manifest, quality and failure review, synthetic volume, downstream training configuration, real-holdout metrics by recipe/category, GPU/P95/cost traces, domain-owner review, no-go rule, and final decision.

## Required C / D visual pages

| page | lesson | archetype | visible causal story |
| --- | --- | --- | --- |
| `07-06` | identity and problem | C | Engineer has scarce anomaly samples; AnomalyDiffusion creates a synthetic image/mask training candidate, then a real-holdout and domain-review gate owns action. |
| `07-07` | architecture | C | Few anomaly references and a planned mask separate anomaly appearance and location; conditional denoising with attention re-weighting produces a traceable synthetic image/mask bundle. |
| `07-08` | build and inference | C | Engineer locks curation, checkpoint, condition/mask, embedding/attention revision, scheduler/seed, quality review and provenance before checking real downstream benefit. |
| `07-09` | engineering selection | D | Reject a synthetic-authenticity or mask-alignment shortcut; choose only with matched real-holdout benefit, integrity, provenance, review, cost and no-go evidence. |

## Sources

- Hu et al., *AnomalyDiffusion: Few-Shot Anomaly Image Generation with Diffusion Model* (AAAI 2024), [arXiv:2312.05767](https://arxiv.org/abs/2312.05767).
- [Official AnomalyDiffusion repository](https://github.com/sjtuplayer/anomalydiffusion) for the authors' reference implementation.
- `full-model-course/07-diffusion-generation-and-restoration.md` for course-scoped claims, page order, and release boundaries.

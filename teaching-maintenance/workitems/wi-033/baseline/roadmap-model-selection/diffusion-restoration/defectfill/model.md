# DefectFill (`defectfill`)

- roadmap family: `diffusion-restoration`
- roadmap model: `DefectFill`
- Markdown pages: `07-02` to `07-05`
- content coverage status: `complete`
- generation status: `ready-for-visual-production`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/defectfill.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
新產品正常品很多，刮傷樣本卻很少；希望補出位置和形狀不同的訓練候選。

### 它交出什麼，也不交出什麼
合成缺陷影像、對應的預定遮罩與生成設定；核對後可供另一個分類或分割模型訓練。

### 一句心智模型
先用少量真實缺陷照片及遮罩，微調預訓練填補模型的部分權重。學習同時關注刮傷細節、刮傷與物件的關係，以及缺陷詞應對應的位置。生成時給正常板與預定遮罩，逐步把缺陷填進去；LFS 再從多個候選挑出缺陷表現較明顯的一張。

**限制：** 本例把放置區移到孔邊。刮傷即使明顯，若在原本沒有材料的孔內長出橋接紋理，仍是幾何不合理的候選。LFS不負責檢查工件幾何；要先檢查位置、形狀與遮罩對應，再進資料集。

### 換一個現場再推理
只有五張刮傷照片與遮罩，已有正常性偵測基準；生成圖很逼真，但微調及篩圖耗時。

**問題：** 你會先擴大DefectFill資料量，還是比較TF-IDG與既有基準？

**核對：** 可以小規模比較：固定真實留出集、下游模型和合成預算，記錄各路徑的微調、生成與人工篩圖時間。若加入資料未改善真實漏檢或反而增誤報，就保留基準；不因影像逼真而擴量。TF-IDG免微調也要付迭代成本。
<!-- topic-learning-bridge:end -->
<!-- wi026-model-core:start -->
## WI-026 核心做法與工作取捨

先用少量真實缺陷照片及遮罩，微調預訓練填補模型的部分權重。學習同時關注刮傷細節、刮傷與物件的關係，以及缺陷詞應對應的位置。生成時給正常板與預定遮罩，逐步把缺陷填進去；LFS 再從多個候選挑出缺陷表現較明顯的一張。

本例把放置區移到孔邊。刮傷即使明顯，若在原本沒有材料的孔內長出橋接紋理，仍是幾何不合理的候選。LFS不負責檢查工件幾何；要先檢查位置、形狀與遮罩對應，再進資料集。

有少量缺陷與遮罩、願意支付微調及多候選選樣成本，可測DefectFill；想分開學外觀與位置，可比較AnomalyDiffusion；不想為新案例微調權重，可試TF-IDG，但仍有參考準備與迭代生成成本。只有正常品時，先建立正常性偵測基準或受控人工擾動，不能假定這些少樣本方法已學過真實刮傷。

換產品須重新核對參考材質、缺陷類型、放置區與適配權重。三者輸出都是資料候選，實際缺陷分數或輪廓由下游模型產生。固定真實切分、合成數量與下游設定，比生成、篩選、訓練及覆核的完整成本。

來源：https://arxiv.org/html/2503.13985v1

圖為AI生成教學示意；原工程段落為補充，首讀新版以本段及topic為準。使用者成品核准pending。
<!-- wi026-model-core:end -->
## Identity and engineering boundary

DefectFill is a **research candidate for synthetic defect-data augmentation**, not an anomaly detector, metrology model, or release decision system. The CVPR 2025 paper fine-tunes a pre-trained inpainting diffusion model from a small set of reference defect image/mask pairs. It learns a defect concept and fills that concept into a chosen masked region of a defect-free image so the resulting synthetic image and mask can be used to train a downstream inspection model.

The paper uses defect, object, and attention losses while adapting the text encoder and U-Net attention layers with LoRA. At sampling time it keeps the unmasked background from the normal image and proposes Low-Fidelity Selection (LFS) to choose a sample with stronger defect expression from multiple generated candidates. These are method details, not a proof that an invented defect is physically valid for a process, recipe, sensor, or defect taxonomy.

## Reproducible engineering contract

### `architecture_path`

`few reference defect image/mask pairs + normal target image + planned placement mask + defect/object prompt token → versioned inpainting diffusion checkpoint with LoRA-adapted text encoder and U-Net attention → conditioned denoising trajectory → synthetic defect image + placement/provenance mask → LFS/quality review → downstream classifier or segmentation training candidate → real-holdout evaluation and domain-owner decision`.

### `representation_or_score`

- The learned defect token, latent, cross-attention map, denoising sample, generated mask, LPIPS/PSNR/SSIM-style LFS score, and downstream score are different objects and must not be conflated.
- LFS selects a visually expressed synthetic candidate inside the planned mask; it is not an industrial fidelity certificate, physical measurement, anomaly score, calibrated probability, or production PASS.
- A synthetic image is a training candidate only. The downstream classifier/segmenter still needs an independently held real-data test and qualified label truth.
- Defect category, recipe, placement, mask, image source, model/version, condition, seed, sampling parameters, reviewer, and synthetic/real split must remain traceable.

### `cost_and_operating_point`

Lock base inpainting checkpoint/license/hash, code revision, defect references and mask policy, normal-image recipe/sensor/ROI, prompts/token, LoRA rank/weights, scheduler, steps, guidance, seed(s), resolution/tile/blend policy, sample count per placement, LFS metric and selection rule, post-processing, storage, GPU/VRAM, throughput and full P95. Profile the complete data-production path including generation, review, training, real holdout evaluation, and any downstream benefit—not only a single attractive image.

### `failure_boundary`

- A generated defect can have implausible physics, texture, scale, edge blend, illumination, sensor noise, placement, or process semantics even when it appears realistic.
- Reference leakage, mask leakage, synthetic-to-real style leakage, duplicated sources, bad provenance, license restrictions, or a contaminated real holdout can make reported gains invalid.
- A low-fidelity-selection metric can choose a stronger visual expression without establishing label integrity or manufacturing relevance.
- Cross-recipe/domain transfer, rare but safety-relevant defect modes, and fine local details can fail silently.
- DefectFill must not generate labels for production release, replace real defect capture, certify a part, or trigger automated PASS/HOLD action.

### `selection_gate`

Select DefectFill only for a controlled rare-defect augmentation experiment when a frozen real training baseline, synthetic volume, downstream architecture, real holdout, defect taxonomy, domain review, provenance/license record, and no-go policy are fixed first. Compare DefectFill with AnomalyDiffusion/TF-IDG only under the same real split, placement/mask policy, synthetic budget, downstream training recipe, human review, and end-to-end cost. Advance only when stratified **real** holdout benefit, mode coverage, label integrity, failure gallery, and specialist acceptance are demonstrated; image realism or one synthetic-only score does not pass the gate.

### `evidence_bundle`

Preserve source normal/defect image and mask hashes, sensor/recipe/ROI, split assignments, defect taxonomy and placement specification; base checkpoint/license/hash, code and LoRA revisions, prompt/token, scheduler/steps/guidance/seed, resolution/tile/blend and LFS configuration; generated image/mask/provenance manifest, quality and failure-review records, synthetic volume, downstream model/training configuration, real-holdout metrics by defect/recipe, calibration and P95/cost traces, domain-owner approval, no-go rule, and final decision.

## Required C / D visual pages

| page | lesson | archetype | visible causal story |
| --- | --- | --- | --- |
| `07-02` | identity and problem | C | An AOI engineer has too few rare-defect references; DefectFill learns a local defect concept and produces a **synthetic training candidate**, which still passes real-holdout and domain-review gates. |
| `07-03` | architecture | C | Reference image/mask, normal image, and placement mask feed a LoRA-adapted inpainting diffusion path; defect/object/attention learning and masked denoising produce synthetic image, mask, and provenance—not a defect verdict. |
| `07-04` | build and inference | C | Engineer locks sources, mask/condition, base checkpoint, LoRA, scheduler/seed/steps, LFS/review, and provenance before measuring real-vs-synthetic benefit and complete P95/cost. |
| `07-05` | engineering selection | D | Reject attractive synthetic images as evidence; release an augmentation route only after same-contract comparison on real holdout, label integrity, mode coverage, license/provenance, domain review, and no-go action. |

## Sources

- Song et al., *DefectFill: Realistic Defect Generation with Inpainting Diffusion Model for Visual Inspection* (CVPR 2025), [arXiv:2503.13985](https://arxiv.org/abs/2503.13985).
- `full-model-course/07-diffusion-generation-and-restoration.md` for course-scoped claims, page order, and release boundaries.

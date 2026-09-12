# TF-IDG (`tf-idg`)

- roadmap family: `diffusion-restoration`
- roadmap model: `TF-IDG`
- Markdown pages: `07-10` to `07-13`
- content coverage status: `complete`
- generation status: `ready-for-visual-production`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/tf-idg.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
要把少量刮傷參考放到新正常板，不希望每個案例都另做模型微調。

### 它交出什麼，也不交出什麼
帶有合成缺陷的影像及目標遮罩；核對後作下游訓練候選。

### 一句心智模型
TF-IDG建立在預訓練影像編修框架上：缺陷參考提供外觀，目標遮罩提供形狀與位置。生成初期讓局部特徵向參考對齊；再找出遮罩內仍像正常面的區域，補強容易漏掉的小缺陷；後期引入原背景資訊，維持紋理連續。它調整生成中的表示，保持模型權重固定。

**限制：** 本例把黑色粗糙表面的刮傷轉到銀色拉絲板。假設刮傷長出來，卻把一塊黑色粗紋理也帶入，接縫明顯不自然。紋理保存能提供背景約束，仍要檢查跨材質參考是否合適。

### 換一個現場再推理
你有缺陷參考和正常板，每週換材質；TF-IDG不用微調，但每張生成慢且有接縫需要人工核對。

**問題：** 應因免微調而直接選它，還是比較另一種準備成本？

**核對：** 若每批量少，免微調可能節省準備時間；若需要大量生成，適配一次後的路徑也可能划算。固定真實留出集，實測總生成量下的準備、迭代及覆核時間，並檢查跨材質紋理和下游錯誤；不能只計權重更新時間。
<!-- topic-learning-bridge:end -->
<!-- wi026-model-core:start -->
## WI-026 核心做法與工作取捨

TF-IDG建立在預訓練影像編修框架上：缺陷參考提供外觀，目標遮罩提供形狀與位置。生成初期讓局部特徵向參考對齊；再找出遮罩內仍像正常面的區域，補強容易漏掉的小缺陷；後期引入原背景資訊，維持紋理連續。它調整生成中的表示，保持模型權重固定。

本例把黑色粗糙表面的刮傷轉到銀色拉絲板。假設刮傷長出來，卻把一塊黑色粗紋理也帶入，接縫明顯不自然。紋理保存能提供背景約束，仍要檢查跨材質參考是否合適。

不想為案例微調時，可先試TF-IDG；願意學外觀嵌入可比較AnomalyDiffusion；願意適配填補模型可比較DefectFill。TF-IDG原方法需要正常影像、缺陷參考及遮罩，不能簡化成『只輸入一句文字』。只有正常品時，先建正常性基準或取得參考。

換產品至少要核對參考材質、遮罩和背景，不更新權重也不代表可直接沿用。比較相同真實切分、合成量與下游輸出需求，記完整生成、人工核對及訓練時間；免微調不等於端到端最快。

來源：https://openaccess.thecvf.com/content/ICCV2025/html/Xu_Training-Free_Industrial_Defect_Generation_with_Diffusion_Models_ICCV_2025_paper.html

圖為AI生成教學示意；原工程段落為補充，首讀新版以本段及topic為準。使用者成品核准pending。
<!-- wi026-model-core:end -->
## Identity and engineering boundary

TF-IDG is a **training-free industrial-defect generation** research candidate. It uses a pre-trained AnyDoor-based image-editing framework with a normal image, a defect reference and masks. DINOv2 appearance conditioning and ControlNet shape conditioning support generation; latent feature alignment, an adaptive anomaly mask and background texture preservation guide the trajectory without case-specific weight fine-tuning. Its intended role is a controlled augmentation experiment when anomaly references are extremely scarce; training-free means a base model and its prompts/conditions still determine what is generated, not that the output is trustworthy by default.

TF-IDG is not an anomaly detector, anomaly score, physical measurement, defect ground truth, production label source, or automatic PASS/HOLD authority. Generated variants remain synthetic training candidates until a fixed real-data experiment demonstrates downstream benefit and a domain owner accepts label, provenance, license, and no-go evidence.

## Reproducible engineering contract

### `architecture_path`

`normal industrial image + defect reference and reference mask + target mask + frozen pretrained editing checkpoint → inversion, feature alignment, adaptive anomaly mask and background texture preservation during generation → synthetic defect image plus planned-region/provenance record → quality and domain review → fixed downstream classifier/segmenter training → stratified real-holdout evaluation and owner decision`.

### `representation_or_score`

- Prompt/text, reference feature, region/mask condition, latent sample, guidance path, generated image, quality-filter score, and downstream model score are distinct objects.
- Training-free generation means no adaptation weights are fitted for the run; it does not remove the need to pin base model, tokenizer, prompt/negative prompt, condition extraction, seed, scheduler, steps, resolution, or data policy.
- A generated image is a synthetic training candidate. It is not proof of defect presence, shape, severity, sensor response, physical mechanism, or inspection performance.
- Preserve source normal image/ROI/recipe, requested defect taxonomy and region, all conditions, model/version/license, random seeds, outputs, review and real/synthetic splits.

### `cost_and_operating_point`

Lock base checkpoint/license/hash, pipeline/code revision, image/ROI and condition extraction, prompts/negative prompts, feature/region/mask policy, scheduler, steps, guidance, seeds, resolution/tile/blend, candidate count, quality filters, storage, GPU/VRAM, throughput and complete experiment P95/cost. Measure the whole augmentation route including generation, review, downstream training and stratified real holdout—not the absence of fine-tuning alone.

### `failure_boundary`

- A frozen base model can hallucinate visual physics, textures, scale, boundaries, illumination, sensor noise, recipe semantics, or unseen defect categories.
- Prompt bias, source/mask leakage, duplicated synthetic styles, selected seeds, contaminated real holdouts, bad provenance, and license restrictions can fabricate apparent gain.
- No fine-tuning does not guarantee domain alignment, safe data governance, reproducibility, low cost, or useful tiny/multiple/complex defect detail.
- TF-IDG cannot replace real capture, validate a defect label, certify a part, issue a metrology result, or trigger automated production action.

### `selection_gate`

Select TF-IDG only for a bounded POC when real train/holdout, normal-image and ROI policy, defect taxonomy/region condition, synthetic budget, downstream model, review, provenance/license and no-go rule are fixed. Compare against DefectFill/AnomalyDiffusion using the same real split, synthetic volume, downstream recipe, human review, and full cost. Proceed only if stratified real-holdout benefit, label integrity, mode coverage, failure review, reproducibility and domain-owner acceptance are demonstrated; a training-free claim or attractive samples does not pass.

### `evidence_bundle`

Preserve source-image/ROI/recipe hashes, split assignment, defect taxonomy and region policy, base checkpoint/license/hash, code revision, prompt/negative prompt, text/feature/region conditions, scheduler/steps/guidance/seeds, resolution/tile/blend, generated asset/provenance manifest, quality/failure review, synthetic count, downstream configuration, real-holdout metrics by recipe/category, GPU/P95/cost traces, domain-owner review, no-go rule and decision.

## Required C / D visual pages

| page | lesson | archetype | visible causal story |
| --- | --- | --- | --- |
| `07-10` | identity and problem | C | Engineer has a rare-defect experiment and uses a frozen diffusion route to create synthetic training candidates; real holdout and domain review own the action. |
| `07-11` | architecture | C | Normal image, defect reference and masks feed frozen guided denoising with feature alignment and texture preservation; output carries a synthetic asset and provenance bundle, not an anomaly verdict. |
| `07-12` | build and inference | C | Engineer locks base/checkpoint, prompts/conditions, seeds, steps, filters, provenance and real-holdout before quantifying downstream benefit. |
| `07-13` | engineering selection | D | Reject “training-free” or image aesthetics as a shortcut; choose only with a same-contract real-holdout, integrity, license, cost, review and no-go comparison. |

## Sources

- Xu et al., *Training-Free Industrial Defect Generation with Diffusion Models* (ICCV 2025), [CVF Open Access](https://openaccess.thecvf.com/content/ICCV2025/html/Xu_Training-Free_Industrial_Defect_Generation_with_Diffusion_Models_ICCV_2025_paper.html).
- `full-model-course/07-diffusion-generation-and-restoration.md` for course-scoped claims, page order, and release boundaries.

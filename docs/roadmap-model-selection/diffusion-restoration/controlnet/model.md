# ControlNet (`controlnet`)

- roadmap family: `diffusion-restoration`
- roadmap model: `ControlNet`
- Markdown pages: `07-14` to `07-17`
- content coverage status: `complete`
- generation status: `ready-for-visual-production`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/controlnet.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
文字可以說『兩孔金屬板』，但無法穩定指定兩孔位置；希望用輪廓圖約束布局。

### 它交出什麼，也不交出什麼
受條件引導的新影像；比對布局與細節後用於展示或受控資料增強。

### 一句心智模型
ControlNet增加可訓練的控制分支，把邊緣、深度或姿態等空間條件轉成訊號，注入基礎擴散模型的去噪過程。原論文訓練時固定基礎模型權重，以零初始化連接逐步學會利用條件；使用時載入對應條件類型的權重，讓生成布局跟著條件走。

**限制：** 輪廓只包含外框與孔，沒描述細裂紋。相同輪廓可能生成有裂紋或沒有裂紋的外觀；條件滿足與原細節忠實是不同問題。本圖是可能情況示意，不是兩次實測輸出。

### 換一個現場再推理
需要把整張板改成另一種材質，兩孔布局要相近；另一項需求只想移除中央污漬。

**問題：** 兩個需求分別選ControlNet、Inpainting，或組合？

**核對：** 整體材質變化可用輪廓ControlNet約束布局；只改污漬可用Inpainting指定區域。若局部生成也要遵守結構，可測支援兩者的管線。各自核對布局偏差、遮罩外變化與生成成本；不能因輪廓吻合就認定微裂紋被保留。
<!-- topic-learning-bridge:end -->
<!-- wi026-model-core:start -->
## WI-026 核心做法與工作取捨

ControlNet增加可訓練的控制分支，把邊緣、深度或姿態等空間條件轉成訊號，注入基礎擴散模型的去噪過程。原論文訓練時固定基礎模型權重，以零初始化連接逐步學會利用條件；使用時載入對應條件類型的權重，讓生成布局跟著條件走。

輪廓只包含外框與孔，沒描述細裂紋。相同輪廓可能生成有裂紋或沒有裂紋的外觀；條件滿足與原細節忠實是不同問題。本圖是可能情況示意，不是兩次實測輸出。

要控制整體布局，考慮ControlNet；要指定局部重畫，考慮Inpainting。前者是控制機制，後者是任務，支援的管線可以搭配兩者。要學真實缺陷外觀再放入正常品，可另外比較DefectFill等少樣本生成方法。

只有正常圖也能抽輪廓做布局探索，卻不足以證明生成缺陷真實。換產品先查輪廓、條件抽取與權重適用性；比較前處理、生成、人工核對時間。兩者主要交付影像，不直接交付真實缺陷輪廓或尺寸。

來源：https://arxiv.org/abs/2302.05543

圖為AI生成教學示意；原工程段落為補充，首讀新版以本段及topic為準。使用者成品核准pending。
<!-- wi026-model-core:end -->
## Identity and engineering boundary

ControlNet is an architecture for adding spatial conditions such as edge, segmentation, depth, pose, or other control maps to a pre-trained text-to-image diffusion backbone. The original method uses trainable conditional branches connected with zero-initialized convolutions while retaining the large diffusion backbone. In this course, it is a controlled **editing/generation tool family**, not a defect detector, anomaly score, measurement system, physical simulator, or production decision authority.

For industrial imagery, a condition map constrains a generated or edited image but does not validate the map, preserve sensor fidelity, prove a defect, or certify a part. A ControlNet experiment must pin the named base model and control model, condition extractor/version, prompts, seed/sampling, scale, image/ROI, data policy, provenance, output review, and safe downstream handoff.

## Reproducible engineering contract

### `architecture_path`

`source image/ROI + versioned condition map (edge/segmentation/depth/etc.) + prompt/negative prompt → named base diffusion checkpoint plus matched ControlNet weights and control scale → conditional denoising → generated/edited image plus condition/provenance bundle → fidelity/review gate → assistive training/editing candidate or human handoff`.

### `representation_or_score`

- A control map, ControlNet residual/control signal, latent sample, output image, difference map, and downstream detector/measurement score are different objects.
- A spatially adhered output does not prove the condition map is correct, that new pixels represent observed physics, or that the output is a defect/anomaly measurement.
- Generated/edited pixels are synthetic content. They require an explicit synthetic/edit label and cannot overwrite raw evidence or become automatic PASS/HOLD input.

### `cost_and_operating_point`

Pin base checkpoint/license/hash, ControlNet weights/revision, condition extractor and preprocessing, source ROI/resolution, prompts, negative prompts, control type/scale/start/end, sampler/steps/guidance/seed, tile/blend, GPU/VRAM, full P95/cost, output storage and review. Qualification must include condition adherence, raw-vs-edit distinction, hallucinated detail, data governance and task-specific human review.

### `failure_boundary`

- Wrong or lossy control extraction, control-scale drift, prompt bias, base/control mismatch, seed/sampler variation and domain shift can fabricate or erase meaningful detail.
- Spatial alignment does not establish physical validity, metrology, label truth, detector performance or safe production action.
- License, source provenance, data egress, untracked edits, raw/synthetic mixing and output reuse can invalidate the workflow.
- ControlNet must not replace raw sensor evidence, certify a defect, control machinery or automatically release/hold production.

### `selection_gate`

Select a named ControlNet route only after a fixed source/condition/base/prompt/sampling/review contract shows usable condition adherence, raw-vs-synthetic traceability, fidelity on target imagery, complete P95/cost and specialist acceptance. Compare it with inpainting/restoration only under a shared input, evidence, data-boundary and action contract. A visually plausible controlled image is insufficient.

### `evidence_bundle`

Preserve raw source/ROI and condition-map hashes, extractor/version/preprocessing, base and ControlNet checkpoint/license/hash, prompts, control type/scale, sampler/steps/guidance/seed, resolution/tile/blend, output and edit manifest, condition-adherence/failure review, raw/synthetic separation, latency/VRAM/cost, data-policy checks, human review, safe fallback and final action.

## Required C / D visual pages

| page | lesson | archetype | visible causal story |
| --- | --- | --- | --- |
| `07-14` | identity and problem | C | Engineer turns a versioned AOI ROI into a condition-controlled editing candidate, then blocks it from becoming physical/production evidence. |
| `07-15` | architecture | C | Source/condition/prompt feed matched base plus ControlNet branch and conditional denoising, producing a traceable generated image. |
| `07-16` | build and inference | C | Engineer locks source/condition/base/control/prompt/seed/sampling and measures adherence, fidelity, P95 and safe review. |
| `07-17` | engineering selection | D | Reject controlled-image plausibility; select only with fixed contracts, traceability, fidelity, cost and specialist review. |

## Sources

- Zhang, Rao, and Agrawala, *Adding Conditional Control to Text-to-Image Diffusion Models*, [arXiv:2302.05543](https://arxiv.org/abs/2302.05543).
- `full-model-course/07-diffusion-generation-and-restoration.md` for course-scoped claims and page order.

<!-- wi033-engineering:start -->
## WI-033 工程圖修正

### ControlNet：條件圖與文字共同交付

輪廓抽取版本、解析度與對應ControlNet checkpoint需匹配。輸出是合成板，不是實拍檢測或尺寸量測。

先定義控制什麼，再檢查生成是否遵守。

來源：https://arxiv.org/abs/2302.05543

### ControlNet：控制殘差接入去噪主幹

同上方雙孔矩形板，輪廓圖含外框/兩孔，文字指定銀色金屬。預訓練主幹固定，可訓練編碼副本接條件，zero convolution初始化0以殘差連接主幹；訓練後連接通常不為0。每步讀時間/噪聲latent與條件；不把輪廓輸出當缺陷熱點。 r01實看修正：輪廓外框與孔框同用白線。

條件控制布局，細節仍要回原條件核對。

來源：https://arxiv.org/abs/2302.05543

### ControlNet：控制強度要配採樣驗證

保存前處理器、控制強度/起止步、基模、文字與採樣。強度增大不保證所有細節更真；用同輪廓檢孔位/外框及材質。

強度只是設定，遵守條件與品質要同時看。

來源：https://arxiv.org/abs/2302.05543

### ControlNet：相同輪廓，不限定有無刮傷

同上方兩孔，外框與孔位不變，表面刮傷可不同；輪廓相符不能證明生成裂紋真實存在。

條件未描述的細節，不能當成觀測證據。

來源：https://arxiv.org/abs/2302.05543

<!-- wi033-engineering:end -->

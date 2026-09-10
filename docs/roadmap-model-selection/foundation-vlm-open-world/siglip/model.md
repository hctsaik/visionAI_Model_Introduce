# SigLIP (`siglip`)

- roadmap family: `foundation-vlm-open-world`
- roadmap model: `SigLIP`
- Markdown pages: `06-06` to `06-09`
- content coverage status: `complete`
- generation status: `ready-for-visual-production`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/siglip.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
你也需要用文字搜尋工件，但想了解 SigLIP 和 CLIP 的差異究竟發生在哪一步，而不是只比較模型名稱。

### 它交出什麼，也不交出什麼
交出圖文表示及配合分數／排序，供語意檢索或分類；本課不把 sigmoid 分數當作缺陷機率或位置。

### 一句心智模型
原始 SigLIP 同樣學影像和文字的共同表示，但在預訓練時，對每一個配對或不配對的圖文組合分別計算 sigmoid 損失，無需用全批次相似度做 softmax 正規化。這些學習訊號仍共同更新編碼器；部署時再比較新影像與候選文字的配合程度。

**限制：** SigLIP 也會受到候選內容限制：齒輪影像面對只有支架、軸承的集合，仍可能選錯。逐對訓練目標不會替你補齊遺漏詞彙，也不保證知道何時拒答。

### 換一個現場再推理
同一批圖上 SigLIP 的分數普遍高於 CLIP，但兩者最高候選大致相同。

**問題：** 可以沿用 CLIP 門檻並宣稱 SigLIP 更準嗎？

**核對：** 不行。兩者的分數尺度與轉換不同；應在固定留出集各自驗證拒答／門檻，再比實際排序錯誤及成本。如果結果相當，維護和延遲也可以決定選擇。
<!-- topic-learning-bridge:end -->
<!-- wi027-model-core:start -->
## WI-027 核心做法與工作取捨

原始 SigLIP 同樣學影像和文字的共同表示，但在預訓練時，對每一個配對或不配對的圖文組合分別計算 sigmoid 損失，無需用全批次相似度做 softmax 正規化。這些學習訊號仍共同更新編碼器；部署時再比較新影像與候選文字的配合程度。

SigLIP 也會受到候選內容限制：齒輪影像面對只有支架、軸承的集合，仍可能選錯。逐對訓練目標不會替你補齊遺漏詞彙，也不保證知道何時拒答。

與 CLIP 比較時，先認清批次 softmax 和逐對 sigmoid 是訓練差異；再固定相同工件、候選文字與測試條件，比實際排序品質與成本。本課介紹原始 SigLIP，不把 SigLIP 2 的新增能力混在一起。

可先用預訓練權重和文字探索，仍要準備相關性／類別驗證資料；換產品需補詞彙、難例及未知圖。各模型使用正確的 tokenizer／前處理，記錄快取、輸入解析度、完整耗時及人工覆核量，不能只比一個絕對分數。

選定原始 SigLIP 權重及配套前處理，沿用一組固定的工件影像與候選文字，同時保留 CLIP 基準和未知樣本。

同條件看候選命中、錯誤拒答與未知誤選，另量影像處理和文字快取後的完整時間；分數高低本身不是選型結果。

來源：https://arxiv.org/abs/2303.15343

版本及示意界線見工作項目 sources.md。使用者成品核准pending。
<!-- wi027-model-core:end -->
## Identity and engineering boundary

SigLIP is an image encoder plus text encoder dual-encoder family. It learns image-text alignment with a **pairwise sigmoid loss**, rather than CLIP's batch-wide softmax-style contrastive normalization. At inference its practical output remains versioned image/text embeddings and a similarity-derived candidate rank.

It can support retrieval, zero-shot candidate classification, and low-label exploration. It is **not** a chat VLM, detector, pixel-localization system, calibrated defect probability, or release decision. The loss name does not grant an operating claim; the local ROI, prompt ontology, score/threshold policy, and evidence gate still determine whether it is useful.

## Reproducible engineering contract

### `architecture_path`

`timestamped image → fixed ROI/tile → declared resize/normalize → vision encoder → image embedding v`; in parallel, `prompt ontology/template → tokenizer → text encoder → text embedding t`. The pretraining distinction is the sigmoid pairwise image-text objective. In deployment a versioned similarity/ranking policy consumes `v` and `t`; it does not create a multimodal bridge, free-form answer, box, mask, or metrology value.

### `representation_or_score`

- `v`: image embedding, tied to checkpoint, image preprocessing, ROI/tile, resolution and aggregation.
- `t`: text embedding, tied to prompt template, vocabulary/synonyms, tokenizer and text checkpoint.
- similarity/rank: a versioned comparison result. Its scale and threshold are local operating choices; it is not automatically comparable across checkpoints, prompt pools or deployment domains.
- SigLIP's pairwise sigmoid training objective is a training distinction, not proof that a score is calibrated or that local semantic wording is robust.

### `cost_and_operating_point`

Record checkpoint/backbone, image resolution and tile policy, preprocessing, prompt pool, tokenizer, candidate aggregation, cache behaviour, score policy, calibration, abstain path and downstream specialist. Measure end-to-end P95/P99 from capture through image encode, text-cache/encode, similarity/ranking, queue, evidence review and action—not only one image forward pass.

### `failure_boundary`

- Tiny defects can disappear through optics, resize, ROI/tile coverage or encoder patch resolution before semantic similarity is calculated.
- Prompt wording, rare production vocabulary and domain language can change `t` and therefore the candidate rank.
- Domain, material, illumination and recipe shifts can be OOD even when a generic zero-shot example appears plausible.
- Global embedding similarity does not yield a pixel mask, defect size, causal diagnosis, calibrated release probability or specialist evidence.
- A training-objective comparison with CLIP does not substitute for same-contract retrieval/grounding truth, prompt-variance and full-P95 measurement.

### `selection_gate`

Use SigLIP only when the local problem is semantic retrieval/candidate exploration and all image, text and score inputs can be locked. Compare against CLIP with the **same** ROI/tile policy, preprocessing, prompt ontology, candidate labels, cache policy, hardware and end-to-end measurement. Select only if local retrieval/grounding truth, prompt robustness, abstain behaviour and P95 support it; otherwise keep it as a candidate route or escalate to a specialist/detector/localization workflow.

### `evidence_bundle`

Preserve image/ROI/tile provenance, preprocessing checksum, checkpoint hash, prompt templates and synonym pool, tokenizer, score/threshold and aggregation settings, top-k similarities, prompt-variance distribution, OOD/abstain outcome, retrieval/grounding truth, specialist decision, queue load and end-to-end P95/P99.

## Required C / D visual pages

| page | lesson | archetype | visible causal story |
| --- | --- | --- | --- |
| `06-06` | identity and problem | C | Engineer asks whether a second dual encoder helps local semantic retrieval; fixed ROI/prompt become candidate rank, not a detector claim. |
| `06-07` | architecture | C | Image path `v` and text path `t` meet through the pairwise-sigmoid training distinction and deployment ranking boundary. |
| `06-08` | build and inference | C | Lock checkpoint/input/prompt/score, measure local calibration/OOD/prompt robustness and complete P95. |
| `06-09` | engineering selection | D | Reject objective-name selection; compare SigLIP with CLIP under one fixed evidence contract. |

## Sources

- Zhai et al., *Sigmoid Loss for Language Image Pre-Training* (2023), [arXiv:2303.15343](https://arxiv.org/abs/2303.15343).
- `full-model-course/06-foundation-vision-and-vlm.md` for course-scoped claims and page order.

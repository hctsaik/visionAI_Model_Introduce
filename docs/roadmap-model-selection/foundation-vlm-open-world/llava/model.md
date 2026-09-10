# LLaVA (`llava`)

- roadmap family: `foundation-vlm-open-world`
- roadmap model: `LLaVA`
- Markdown pages: `06-18` to `06-21`
- content coverage status: `complete`
- generation status: `ready-for-visual-production`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/llava.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
檢查人員希望對一張端子照片追問「哪一側需要檢查」，並得到可回看原圖的文字說明，而不只是固定類別。

### 它交出什麼，也不交出什麼
生成對影像與問題的文字回答；本例描述右側未見螺絲，交由檢查人員核對和追問。不是實際 LLaVA 推論結果。

### 一句心智模型
本課以原始 LLaVA 為例：視覺編碼器先把照片轉成視覺特徵，學習到的投影把它們接到語言模型能使用的表示，再和問題文字一起產生回答。圖文對齊及指令微調讓這個橋接能支援看圖問答；這不同於 CLIP 只在候選文字間比相似度。

**限制：** 從空螺絲座可以提出「未見螺絲」的觀察，卻無法只靠這張照片知道是漏裝還是振動鬆脫。流暢的原因說明可能跨過影像支持的範圍。

### 換一個現場再推理
模型說「端子因振動鬆脫」，照片只顯示螺絲座是空的。你需要填維修單。

**問題：** 可以保留哪些內容？還應準備什麼？

**核對：** 可保留經原圖核對的未見螺絲現象，原因先標待查，再補裝配紀錄或現場檢查。若工作只需固定的缺件分流，專用檢測流程也可能更直接；VLM 的追問能力不等於根因證據。
<!-- topic-learning-bridge:end -->
<!-- wi027-model-core:start -->
## WI-027 核心做法與工作取捨

本課以原始 LLaVA 為例：視覺編碼器先把照片轉成視覺特徵，學習到的投影把它們接到語言模型能使用的表示，再和問題文字一起產生回答。圖文對齊及指令微調讓這個橋接能支援看圖問答；這不同於 CLIP 只在候選文字間比相似度。

從空螺絲座可以提出「未見螺絲」的觀察，卻無法只靠這張照片知道是漏裝還是振動鬆脫。流暢的原因說明可能跨過影像支持的範圍。

需要開放式問答與本機部署時，可評估具體 LLaVA 或 Qwen-VL 權重；需要託管工作流程時，可評估 Gemini API。圖中比較的是部署範例，並不表示每個家族只准用這一種部署方式。

準備代表影像、真實問題、可接受答案和不確定案例；換產品需重測用詞、可見細節與回答。自建要計入 GPU、模型／前處理維護，託管要計入請求、網路和重試；兩者都看錯答、漏答、人工覆核及完整耗時。

固定一個 LLaVA 版本與配套處理器，準備端子影像、問題及人工核對答案；測試集包含缺件、遮擋和看不清楚的情況。

逐項核對回答是否被原圖支持，統計漏掉的現象、捏造的原因及合理拒答；和人工直接讀圖的時間與錯誤比較，算入覆核。

來源：https://llava-vl.github.io/

版本及示意界線見工作項目 sources.md。使用者成品核准pending。
<!-- wi027-model-core:end -->
## Identity and engineering boundary

LLaVA is a multimodal generative VLM family: a vision encoder produces visual tokens, a learned projector maps them into the language-model context, and multimodal instruction tuning lets the language model generate an autoregressive answer. Its engineering role is explainable, follow-up-capable assistance such as SOP question answering, review summaries and exploration.

It is not a tiny-defect detector, metrology instrument, grounded localization guarantee, calibrated defect probability, or automatic PASS/release authority. A fluent answer is only a claim. A production action still belongs to a named high-resolution detector/AD/metrology route plus an evidence owner and human or specialist review.

## Reproducible engineering contract

### `architecture_path`

`timestamped image + question → fixed ROI/tile and visual preprocessing → versioned vision encoder visual tokens → learned projector/bridge → versioned LLM context + instruction/system schema → autoregressive structured answer → cited evidence request / abstain / specialist route`.

The projector maps visual features into the LLM language space. It does not create a defect box, measurement, physical proof, or release decision. The output is a token sequence; a schema and grounding gate must make every claim, source, uncertainty and allowed next action explicit.

### `representation_or_score`

- visual tokens depend on the vision encoder, checkpoint, image preprocessing, resize/tile policy and token budget.
- projected tokens and LLM hidden state are not detector scores or defect probabilities.
- the generated answer, JSON field or cited claim is language output; it must be validated against supplied evidence and its named source/version.
- any candidate ROI, heatmap, score, measurement or PASS/HOLD action must remain owned by a separate named grounding, detector, AD, metrology or human-review route.

### `cost_and_operating_point`

Lock vision encoder, projector, LLM/model revision, quantization, image resize/tile policy, visual-token cap, text-context cap, system prompt, instruction template, decoding temperature, output schema, RAG corpus/version, ACL and tool permission. Measure image encoding, projector, prefill, decoding, retrieval/tool calls, validation, human/specialist action and full P95/P99 separately. Token count, context length, concurrency and provider/on-prem topology are operating-point variables, not implementation detail.

### `failure_boundary`

- Resize, patching or visual-token compression can erase a tiny defect before the VLM sees it.
- Generated wording can hallucinate a cause, claim, citation or evidence region; grounded-looking language is not proof.
- Prompt injection, unversioned SOP/RAG documents, missing ACL/redaction, tool overreach and sensitive image egress can invalidate the workflow.
- Long context, latency, cost, stale model revisions and OOD material/illumination can change answer quality or availability.
- LLaVA cannot autonomously issue PASS, release, metrology, physical root cause or safety action.

### `selection_gate`

Use LLaVA only for an assist workflow after a fixed local contract shows schema-valid, grounded answers with source/evidence coverage, correct abstention and acceptable full P95/cost on the target question and image set. Qualification also requires replayable model/prompt/RAG versions, injection tests, data/ACL review, specialist acceptance and a safe fallback. A visually plausible or fluent answer never authorizes an automatic PASS.

### `evidence_bundle`

Preserve image/ROI/tile provenance and redaction state; vision-encoder/projector/LLM checkpoint or revision; preprocessing and token/cost settings; system/instruction prompt and decoding policy; schema version; RAG corpus/document/source version and ACL; request/response hashes; cited evidence; grounding and abstain result; detector/AD/metrology confirmation where applicable; prompt-injection/security checks; latency/cost; specialist review and final action.

## Required C / D visual pages

| page | lesson | archetype | visible causal story |
| --- | --- | --- | --- |
| `06-18` | identity and problem | C | Engineer asks an AOI-image question; image and question become visual tokens, then a structured LLaVA claim that must pass evidence/human review. |
| `06-19` | architecture | C | Fixed image is tokenized by a vision encoder, bridged by a projector into LLM context, and rendered as a schema-controlled answer with grounding/abstain boundary. |
| `06-20` | build and inference | C | Engineer locks vision/projector/LLM, prompt/schema/RAG/ACL and token/P95 controls before replaying grounded answers through human/specialist governance. |
| `06-21` | engineering selection | D | Reject a fluent-answer shortcut; compare the same image/question/evidence contract with structured grounding, abstention and specialist confirmation before any action. |

## Sources

- Liu et al., *Visual Instruction Tuning* (LLaVA, 2023), [arXiv:2304.08485](https://arxiv.org/abs/2304.08485).
- Liu et al., *Improved Baselines with Visual Instruction Tuning* (LLaVA-1.5, 2023), [arXiv:2310.03744](https://arxiv.org/abs/2310.03744).
- `full-model-course/06-foundation-vision-and-vlm.md` for course-scoped claims and page order.

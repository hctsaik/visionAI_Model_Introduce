# Qwen-VL (`qwen-vl`)

- roadmap family: `foundation-vlm-open-world`
- roadmap model: `Qwen-VL`
- Markdown pages: `06-22` to `06-25`
- content coverage status: `complete`
- generation status: `ready-for-visual-production`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/qwen-vl.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
你要從細長設備銘牌讀出型號與批次；把所有圖片硬壓成同樣大小，可能先失去小字，而保留更多像素又會增加處理負擔。

### 它交出什麼，也不交出什麼
生成銘牌內容的文字回答，本例為型號 A17、批次 B08；需和原圖核對。不同家族版本的能力及輸入策略各自確認。

### 一句心智模型
Qwen-VL 是家族名稱，本課沿用 Qwen2-VL 作具體範例：動態解析度處理讓不同尺寸／長寬比的影像形成可變數量的視覺 tokens，再把空間位置資訊與問題一起交給語言模型。這讓模型能處理多樣影像，但實際保留的細節仍受處理器和像素預算限制。

**限制：** 當像素上限太低，批次 B08 可能模糊到只剩 B0?。回答流暢不代表小字真的被保留；重新放大縮圖也不能恢復原始資料。

### 換一個現場再推理
每張銘牌位置固定，只需讀型號與批次；Qwen-VL 能答長段說明，但延遲偏高。

**問題：** 你會優先調整什麼，又會加入哪個基準？

**核對：** 先用原始局部保留必要小字，調整像素預算並量欄位錯誤及延遲；把固定欄位 OCR 納入比較。如果還需要跨欄理解或開放式問題，VLM 仍有價值，但不必為了流暢說明支付不需要的成本。
<!-- topic-learning-bridge:end -->
<!-- wi027-model-core:start -->
## WI-027 核心做法與工作取捨

Qwen-VL 是家族名稱，本課沿用 Qwen2-VL 作具體範例：動態解析度處理讓不同尺寸／長寬比的影像形成可變數量的視覺 tokens，再把空間位置資訊與問題一起交給語言模型。這讓模型能處理多樣影像，但實際保留的細節仍受處理器和像素預算限制。

當像素上限太低，批次 B08 可能模糊到只剩 B0?。回答流暢不代表小字真的被保留；重新放大縮圖也不能恢復原始資料。

要處理長銘牌或文件問答，可把具體 Qwen-VL 版本納入候選；LLaVA 可作另一自建問答基準，Gemini API 可作託管基準。各自用適配的處理器，以同一原始資料和問題比較，而非假定家族名稱代表固定品質。

準備不同字級、長寬比、反光與遮擋的原圖及人工抄錄答案；換產品先查新欄位與格式。增加細節可能提高 token、記憶體或時間；若只讀固定字欄，傳統 OCR 也應作基準，連同覆核與重試評估。

選定 Qwen2-VL 權重及處理器作本課實作範例，保留原始銘牌與正確抄錄；先比較兩個像素預算或原圖局部，不同模型版本不可混用設定。

逐欄比型號／批次的正確與漏讀，並量實際 token、GPU 記憶體及端到端耗時；只有細節與成本一起改善到需求範圍才採用。

來源：https://qwenlm.github.io/blog/qwen2-vl/

版本及示意界線見工作項目 sources.md。使用者成品核准pending。
<!-- wi027-model-core:end -->
## Identity and engineering boundary

Qwen-VL is a generative multimodal-model family, not one fixed checkpoint. This course uses a **named, dated Qwen2-VL-class deployment** to teach its characteristic dynamic-resolution, variable-visual-token route. Qwen2-VL maps images at varying resolutions to varying numbers of visual tokens and uses multimodal positional handling before a multimodal language model emits a text or structured response.

Its engineering role is multi-image/document/SOP question answering and assistive review when token, data and output governance are explicit. It is not a tiny-defect detector, calibrated physical measurement, guaranteed grounding mechanism, automatic PASS/release authority, or a justification to name an unpinned `Qwen-VL` family member as though it were reproducible.

## Reproducible engineering contract

### `architecture_path`

`timestamped image(s)/document/video + question → declared dynamic-resolution preprocessing → variable visual-token sequence + visual positional representation → versioned multimodal bridge/LLM → schema-controlled autoregressive text or structured output → cited evidence request / abstain / specialist route`.

The exact visual-token count depends on the chosen Qwen model revision and image/video pixel constraints. It must be measured and logged from the deployed processor; it must not be replaced with a generic `H×W/P²` claim about final LLM context.

### `representation_or_score`

- visual tokens are versioned representations tied to the exact model revision, processor, aspect ratio, min/max pixel constraints, resize/tile policy and image/video inputs.
- M-ROPE/dynamic-resolution processing describes a representation path, not a defect probability, measurement, box or release score.
- the generated text/JSON/tool argument is a language output. A schema can constrain fields but cannot prove its claim, citation or localization.
- any candidate ROI, anomaly map, score, measurement and PASS/HOLD decision remains owned by a named grounder, detector/AD/metrology route and specialist decision policy.

### `cost_and_operating_point`

Lock model/revision/weight hash or service date, processor, min/max pixels per visual input, image/video frame sampling, visual-token cap, text-context cap, quantization, hardware, prompt/system schema, decoding, RAG/tool policy, ACL/redaction and concurrency. Profile variable visual-token count against VRAM, prefill, decode, retrieval/tool calls, specialist action and full P95/P99. Token count, image aspect ratio and multi-image/document length are deployment controls rather than hidden implementation detail.

### `failure_boundary`

- Small defects can be lost or distorted by dynamic preprocessing, token constraints, image/video sampling or insufficient local resolution.
- Variable token count can push context, latency, memory, cost or truncation into a different operating point.
- Generated claims can hallucinate evidence, citations, causes or grounding; unverified structured output is still unverified.
- Model/revision/processor changes, quantization, prompt injection, stale RAG/SOP, ACL/redaction failures, data egress and vendor/service drift can invalidate the qualification.
- Qwen-VL cannot autonomously issue PASS, physical measurement, safety action or release.

### `selection_gate`

Select a specifically named Qwen deployment only after a fixed local image/question/schema/data contract demonstrates grounded schema validity, source/evidence coverage, correct abstention, visual-token-to-P95/VRAM/cost behavior and specialist acceptance on target multi-image/document workloads. Compare it against LLaVA/Gemini or another candidate only under the same input, token/pixel, data-boundary, grounding and action contract. A broad family name, benchmark slogan or fluent answer never authorizes production release.

### `evidence_bundle`

Preserve image/document/video provenance; ROI, resize and pixel/token settings; model/revision/weight or service date; processor and quantization; hardware/concurrency; system prompt/schema/decoding; RAG corpus/source/version/ACL; request and response hashes; generated claim/citation; grounding/abstain result; token/VRAM/P95/cost traces; injection/security/data-egress checks; named detector/AD/metrology confirmation; specialist review and final action.

## Required C / D visual pages

| page | lesson | archetype | visible causal story |
| --- | --- | --- | --- |
| `06-22` | identity and problem | C | Engineer compares aspect-ratio-diverse AOI/document inputs; exact Qwen2-VL deployment turns them into variable visual tokens and an assist-only structured response. |
| `06-23` | architecture | C | Dynamic-resolution processor produces a versioned variable token sequence; positional bridge and multimodal LLM produce a governed text/JSON response, not a generic patch-count claim. |
| `06-24` | build and inference | C | Engineer locks model/processor/pixel caps/quantization, then profiles token-to-VRAM/P95/cost and validates grounding, abstention, data boundary and human action. |
| `06-25` | engineering selection | D | Reject the broad-family or fluent-answer shortcut; choose only a named Qwen deployment that wins a same-contract local comparison on evidence, tokens, P95, cost and governance. |

## Sources

- Wang et al., *Qwen2-VL: Enhancing Vision-Language Model's Perception of the World at Any Resolution* (2024), [arXiv:2409.12191](https://arxiv.org/abs/2409.12191).
- [Official Qwen-VL repository](https://github.com/QwenLM/Qwen-VL) for the Qwen-VL family and deployment lineage.
- `full-model-course/06-foundation-vision-and-vlm.md` for course-scoped claims and page order.

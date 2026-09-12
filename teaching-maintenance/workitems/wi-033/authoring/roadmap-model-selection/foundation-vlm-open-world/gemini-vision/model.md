# Gemini Vision (`gemini-vision`)

- roadmap family: `foundation-vlm-open-world`
- roadmap model: `Gemini Vision`
- Markdown pages: `06-26` to `06-29`
- content coverage status: `complete`
- generation status: `ready-for-visual-production`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/gemini-vision.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
你希望把端子照片和檢查問題送給託管服務，先產生待核對的觀察清單，減少逐張整理文字的工作。

### 它交出什麼，也不交出什麼
提供文字或所選模型支援的結構化回答，供人工核對或接入資料整理；本例回覆僅為教學示意，未呼叫 Gemini 做模型實測。

### 一句心智模型
Gemini Vision 是 Gemini 影像理解能力的稱呼，本課用 API 工作流程說明：把影像與問題放在同一請求，指定模型和輸入設定，服務再生成文字或支援的結構化回覆。圖中以封閉服務區表示；公開介面能說明輸入輸出，不足以推定其私有編碼器或橋接架構。

**限制：** 若回覆 JSON 把左、右螺絲都填成 present，語法仍可能完全可解析；原圖右側卻是空座。通過格式檢查，不能直接變成通過內容檢查。

### 換一個現場再推理
JSON 全部可解析，某批反光照片卻頻繁把空螺絲座說成有螺絲。

**問題：** 先改 schema、取像，還是模型？如何判斷？

**核對：** 先回看原圖和失敗局部，確認是否反光遮住線索；若資料不足先改善取像，再用同一批核對資料比較模型／輸入設定。schema 只能處理格式，不能修復看錯的內容；必要時保留人工覆核。
<!-- topic-learning-bridge:end -->
<!-- wi027-model-core:start -->
## WI-027 核心做法與工作取捨

Gemini Vision 是 Gemini 影像理解能力的稱呼，本課用 API 工作流程說明：把影像與問題放在同一請求，指定模型和輸入設定，服務再生成文字或支援的結構化回覆。圖中以封閉服務區表示；公開介面能說明輸入輸出，不足以推定其私有編碼器或橋接架構。

若回覆 JSON 把左、右螺絲都填成 present，語法仍可能完全可解析；原圖右側卻是空座。通過格式檢查，不能直接變成通過內容檢查。

託管服務可減少自建模型與 GPU 的維護工作；具體 LLaVA／Qwen-VL 自建方案可提供不同的部署控制。以同一影像、問題與答案核對方式比較，不能把託管等同零維護，也不預設哪個家族最好。

準備代表影像、問題和可核對答案，選定實際 model ID／API 設定並確認資料可送出。換模型、輸入策略或產品時重新測量錯答／漏答；成本包括上傳、服務回應、重試、用量和人工覆核，這裡不引用易變的價格或限額。

挑一小批允許送出的代表影像，準備問題及人工核對表；固定實際模型識別與請求設定，先用低量測試驗證輸出。

分別統計格式可解析、欄位內容正確、漏掉觀察及不確定時的處理，再比較完整耗時、重試量、用量費用與覆核時間。

來源：https://ai.google.dev/gemini-api/docs/image-understanding

版本及示意界線見工作項目 sources.md。使用者成品核准pending。
<!-- wi027-model-core:end -->
## Identity and engineering boundary

Gemini Vision is a provider multimodal service/model series, not one static, locally reproducible checkpoint. This course treats it as a service-integration route: image/document/video plus prompt and optional tools are sent under a declared API model ID, API version, region and data policy; the provider returns generated text, structured output or a tool-call request.

Its role can be assistive review, document/SOP extraction or non-real-time multimodal integration when data egress and service change are acceptable. The service output is not an AOI detector, metrology measurement, guaranteed grounding, physical evidence, calibrated defect probability or automatic PASS/release authority. Internal encoder/bridge details are provider implementation details and must not be invented in teaching material.

## Reproducible engineering contract

### `architecture_path`

`timestamped image/document/video + question + system schema/tool policy → client-side redaction/ACL/egress gate → declared Gemini API model ID and API version → provider multimodal service → generated response / structured JSON / tool call → citation/evidence validation, abstain, audit log and specialist route`.

The request contract, model ID/version, region, retention setting, file/token limits, rate-limit and retry behavior are the architecture that the production owner can control. A service alias can move to a different release; production qualification must record and monitor the exact request and response behavior rather than assume a static model weight.

### `representation_or_score`

- request content, attached file/image/document/video, prompt, system instruction, schema and tool result are versioned service inputs.
- a response text, JSON field or function call is a generated claim; structured output makes parsing predictable but does not prove factual grounding, citation, localization or physical measurement.
- provider model metadata and token limits must be queried/recorded for the deployment; an alias or “Gemini Vision” label is insufficient.
- a score/map/ROI/measurement/PASS action remains owned by a named detector, AD/metrology route and specialist decision policy.

### `cost_and_operating_point`

Lock API model ID and dated revision, API version, region, project/account, request/file/token constraints, prompt/schema/tool policy, grounding/caching features, retry/backoff, rate limits, concurrency, price version, data-retention choice and fallback. Measure request preparation, upload, provider latency, generation, tool/retrieval, validation, human/specialist action and full P95/P99; log errors, retries, 429s, cost and fallback separately. Preview, latest or experimental aliases require change monitoring and requalification.

### `failure_boundary`

- Provider alias, model, endpoint, feature, safety filter, rate limit, price or deprecation change can modify availability, answer behavior, latency or cost.
- Network, quota, retries, file/token limits and service-region failures can prevent or delay an otherwise valid engineering workflow.
- Prompts, responses, files, cache and state can have retention or egress implications; ACL, redaction, region and user-controlled deletion must be reviewed before production use.
- Generated text/JSON/tool calls can hallucinate claims, citations or causal explanations; injection and untrusted document content can redirect the workflow.
- Gemini Vision cannot issue automatic PASS, safety action, physical measurement or final production release.

### `selection_gate`

Select a specifically named Gemini service route only after a replay set proves grounded schema validity, source/evidence coverage, abstention, auditability, data-boundary compliance, target P95/cost and safe fallback under the exact model ID/API version/region/feature policy. Use a fixed question, image evidence, schema, retrieval/grounding and action contract when comparing it with LLaVA/Qwen or another service. A fluent vendor response or broad service brand never authorizes an automatic action.

### `evidence_bundle`

Preserve image/document/video provenance and redaction state; API model ID/version/alias resolution; API version, region, project and policy configuration; request/file/token parameters; system prompt/schema/tool policy; retrieval/grounding/caching configuration; request/response/tool hashes; citations/evidence and abstention; rate-limit/retry/error/fallback traces; P95/cost; data-retention/deletion/ACL evidence; detector/AD/metrology confirmation; specialist review and final action.

## Required C / D visual pages

| page | lesson | archetype | visible causal story |
| --- | --- | --- | --- |
| `06-26` | identity and problem | C | Engineer holds an AOI image at an egress gate; a named provider service gives an assistive response only after API/version/region/data policy and evidence owner are visible. |
| `06-27` | architecture | C | File/prompt/tool request passes client-side governance to the provider service, then returns structured response/tool call with validation, audit and abstain boundary; internal encoder is intentionally opaque. |
| `06-28` | build and inference | C | Engineer locks API model/version/region/schema/ACL/rate-limit/retry/cost, replays a test set and records request/response/P95/error/fallback before specialist action. |
| `06-29` | engineering selection | D | Reject a broad vendor-answer shortcut; choose a named service route only through same-contract evidence, data-boundary, P95/cost and fallback qualification. |

## Sources

- [Gemini API model naming and versioning](https://ai.google.dev/gemini-api/docs/models).
- [Gemini API structured outputs](https://ai.google.dev/gemini-api/docs/structured-output).
- [Gemini Developer API zero data retention](https://ai.google.dev/gemini-api/docs/zdr).
- [Gemini API rate limits](https://ai.google.dev/gemini-api/docs/rate-limits).
- `full-model-course/06-foundation-vision-and-vlm.md` for course-scoped claims and page order.

<!-- wi033-engineering:start -->
## WI-033 工程圖修正

### Gemini Vision：交付可以核對的欄位

依公開影像API的輸入與輸出介面設計工作欄位，未呼叫服務或猜測私有骨幹。先固定接頭與問題，定義left/right可見狀態及cause未知欄位，再回原圖核對；欄位設計不是API回覆，格式不能保證內容。工程2才深入請求與錯誤JSON處理。

要求欄位能幫助核對，但不保證內容正確。

來源：https://ai.google.dev/gemini-api/docs/structured-output

### Gemini影像介面：請求、回覆、查證

依公開Gemini API說明輸入/輸出，不臆測私有編碼器。以同一左右圓接頭，左有螺絲右空座，示意JSON先錯填兩側present；解析成功後逐欄對照原圖，右側應記not_visible且原因unknown。所有回覆為作者設計反例，未呼叫API；實際部署另固定可用模型、schema與輸入設定。

JSON能解析，只代表格式；內容仍要對原圖。

來源：https://ai.google.dev/gemini-api/docs/structured-output

### Gemini Vision：格式與內容分開驗

部署時固定可用模型標識、請求設定與schema，記錄服務版本變動和原始回覆。JSON/schema通過只證明格式，仍逐欄對照影像；低可信、拒答、缺欄位及服務失敗都需要可追溯處理。

版本、請求與回覆都保存，異常欄位交覆核。

來源：https://ai.google.dev/gemini-api/docs/structured-output

### 雲端VLM與專用模型：同件比較

以相同接頭和允收定義比較雲端API與本機專用視覺；包含網路耗時、資料流、服務可用性、維護與逐項錯誤。不能將API便利性或固定格式當自動放行證據，也不虛構內部架構。

按問題彈性、資料流與錯誤成本選擇。

來源：https://ai.google.dev/gemini-api/docs/structured-output

<!-- wi033-engineering:end -->

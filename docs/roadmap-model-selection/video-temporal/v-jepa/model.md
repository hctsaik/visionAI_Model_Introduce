# V-JEPA `v-jepa`

- roadmap category: `video-temporal`
- course pages: `05-30` through `05-33`
- research status: `complete`
- visual status: `ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/v-jepa.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
你有許多未標動作的工業影片，想先學可以交給不同工作任務使用的表示，而不是要求模型逐像素重畫每段影片。

### 它交出什麼，也不交出什麼
影片表示與下游任務候選。本課不把特徵差直接命名為缺陷機率，也不宣稱輸出未來影片、精密位置或動作指令。

### 一句心智模型
本課講2024原版V-JEPA：上下文編碼器看未被遮住的影片部分，預測器估計被遮區的特徵，對齊另一個目標編碼器從完整影片提供的對應特徵。訓練比較發生在表示空間，不是把缺少的像素或未來影片重畫出來。

**限制：** 若輸入時間窗漏掉短暫滑落，預測特徵也可能保留不了工作需要的事件；預訓練可遷移性不能取代域內驗證。

### 換一個現場再推理
同事看到V-JEPA的預測二字，想直接輸出下一秒的影像給操作員。

**問題：** 本課原版能直接接成這個功能嗎？

**核對：** 不能；這裡預測的是被遮區的特徵，不是像素影片。若要未來影像須另選生成／預測方案並驗證；若要判目前動作，則可用原版特徵搭配任務頭。
<!-- topic-learning-bridge:end -->
<!-- wi028-model-core:start -->
## WI-028 核心做法與工作取捨

本課講2024原版V-JEPA：上下文編碼器看未被遮住的影片部分，預測器估計被遮區的特徵，對齊另一個目標編碼器從完整影片提供的對應特徵。訓練比較發生在表示空間，不是把缺少的像素或未來影片重畫出來。

若輸入時間窗漏掉短暫滑落，預測特徵也可能保留不了工作需要的事件；預訓練可遷移性不能取代域內驗證。

VideoMAE在預訓練補像素，V-JEPA預測特徵；兩者是否有利要看同一工作任務與成本。若少量時間狀態已足夠，也可先比較簡單規則或ConvLSTM。

可用2024原版相容預訓練權重起步，仍需下游標註與測試；換場景、視角或動作後重驗特徵與任務頭。比較凍結或微調方案時記錄調整預算，不混入V-JEPA2／2.1能力。

先定義工作要判斷的動作與時間範圍，準備完整作業影片、少量下游標註與獨立測試，再固定原版權重與取樣。

在相同影片／標註預算下比較任務錯誤、短事件漏報、片段等待、完整推論成本及換產品後維護量；不以特徵圖漂亮排名。

來源：https://arxiv.org/abs/2404.08471

版本及示意界線見工作項目 sources.md。使用者成品核准pending。
<!-- wi028-model-core:end -->
## Model identity

V-JEPA is a video joint-embedding predictive architecture. A context encoder receives visible spatiotemporal tokens, a predictor estimates the latent representations for masked target regions, and a target encoder supplies stop-gradient latent targets. It learns a video representation in feature space, not pixels; it is not direct video generation, detection, identity tracking, anomaly release or proof that a small target event was retained.

The pretraining loss measures agreement between predicted and target latent features under a declared clip, context/target-mask design, encoder / predictor / target-encoder update policy and checkpoint. Operational scores must come from a separately governed embedding-distance or fine-tuned downstream head, temporal aggregation, calibration and action contract. Latent prediction may prioritize higher-level structure, but it does not guarantee coverage of micro-events, future production drift or timely deployment decisions.

## Required fields

### architecture_path

Timestamped video frames -> fixed ROI / preprocessing / frame sampling -> declared clip length and temporal-token policy -> context / target multi-block mask design -> context video tokens -> context encoder -> predictor conditioned on target positions -> predicted target latent tokens -> target encoder on target regions -> stop-gradient target latent tokens -> latent prediction objective -> learned context representation -> frozen or fine-tuned downstream embedding-distance / prediction / classification head -> temporal aggregation -> calibrated event candidate -> PASS / REVIEW / HOLD or human action.

Store source frames / timestamps, clip membership and overlap, ROI / normalization, clip / token configuration, context / target mask locations and policy, encoder / predictor / target-encoder revisions and target-update policy, checkpoint, latent prediction summaries, downstream-head revision, per-window outputs, aggregation, threshold, event boundary and action. Predicted target latents and their training loss do not prove a semantic class, anomaly, object identity, cause, future pixel content or alert release.

### representation_or_score

- Representation: contextual video-token embeddings produced by the declared context encoder and clip / mask policy.
- Prediction target: stop-gradient target-encoder latent representation for target regions; it is a feature-space supervision target rather than pixels.
- Pretraining objective: distance / loss between predictor outputs and target latents under the declared target-update and mask policy; it is not an event or anomaly score.
- Downstream score: separately versioned embedding distance or frozen / fine-tuned task-head output with temporal aggregation and calibration to the decision unit.
- Reliability evidence: clip / target temporal coverage, context-target policy, checkpoint provenance, target event truth, micro-event sampling response, domain drift and downstream-head evidence.

### cost_and_operating_point

Lock camera / timestamp / missing-frame policy, ROI / preprocessing, clip length / sampling / stride / overlap, token / positional encoding, context / target mask block count, size, temporal location and seed policy, context encoder, predictor, target encoder and stop-gradient / target-update policy, checkpoint, downstream head / loss / aggregation / threshold, batch / precision / token budget, inference buffering, hardware and action owner.

Report pretraining / fine-tuning cost separately from inference. For deployment, report complete capture-to-event P50/P95/P99 including clip buffer, decode, preprocessing, tokenization, context encoder, predictor or downstream head as used, aggregation, queue and hand-off. Measure clip / target event coverage, event recall / false alert / delay, micro-event miss, frame-drop / variable-rate / camera / process-drift cases, train-test adjacent-clip leakage, token / VRAM / RAM, review load and future results. Latent prediction loss, one embedding visualization or encoder-only timing is not operational performance.

### failure_boundary

- A target latent is not a pixel target; latent invariance can discard small pixel details or micro-events that have no downstream-head evidence.
- Clip sampling, context / target block geometry, tokenization, predictor, target-update policy and checkpoint change visible temporal coverage and learned representation; any change is a new operating point.
- Long dependencies beyond validated clip coverage, variable frame rate, missing frames, camera / process changes and train-test adjacent-clip overlap can invalidate latent-prediction assumptions or leak temporal context.
- Foundation pretraining requires data / compute / token / VRAM / latency budget and target-domain verification; a general representation does not automatically transfer to event semantics.
- Pretraining loss, target-latent similarity or public frozen evaluation must not be called anomaly score, event recall or release evidence without a declared downstream head and event truth.

### selection_gate

Use V-JEPA when research or product scope can support a foundation-style video representation pipeline, target temporal pixels and clips are governed, context-target latent prediction has a named downstream embedding / task-head owner, and token / VRAM / complete P95 fit the deployment budget. Validate micro-event coverage, clip sampling, domain transfer, downstream event timing and real process drift.

Hold or choose VideoMAE, ConvLSTM, a simpler baseline, detector / tracker or human review when the decision depends on micro-events absent from clip / token coverage, no accountable task head or event truth exists, data / pretraining scale is unjustified, long temporal dependency / sampling is unstable, target-domain drift is ungoverned or complete latency cannot meet budget. Compare V-JEPA and VideoMAE only with the same clip / temporal pixels, ROI / preprocessing, timestamp / sampling / coverage, train-test sequence isolation, downstream label head, aggregation, event truth, hardware and action contract; never rank pretraining objectives as event outcomes.

### evidence_bundle

Keep camera / lens / timestamp / frame-rate / missing-frame records; ROI / preprocessing; sequence / lot membership and split audit; clip length / stride / overlap / temporal tokens; context-target mask policy / locations / seeds; context encoder, predictor, target encoder, target-update / stop-gradient and checkpoint provenance; latent prediction / target summaries and downstream head / aggregation; event truth / action traces; clip / target coverage, micro-event miss, event recall / false alert / delay; token / VRAM / RAM / complete P95/P99; frame-drop, camera, compression, process-drift and future sets; review owner and rebuild evidence.

## Visual primitives

- `context_target_mask`: timestamped clip tokens are split into visible context and target blocks with an explicit temporal / spatial policy.
- `dual_encoder_latent_target`: context encoder / predictor path and target encoder / stop-gradient latent-target path are separate and directional.
- `latent_prediction_not_pixel_generation`: predicted target feature is matched in latent space; no decoder / pixel reconstruction or event implication is inferred.
- `downstream_embedding_head_boundary`: learned representation connects to a separately governed embedding-distance or fine-tuned task head and event aggregation.
- `coverage_drift_latency_gate`: micro-event / target coverage, clip leakage, token / VRAM, complete P95, process drift and controlled VideoMAE comparison are explicit.

## Comparison contract

- comparison ID: `video-temporal-representation-contract`
- layout: `D-2` controlled temporal-representation comparison.
- fixed conditions: same timestamped temporal pixels / ROI / preprocessing, clip / window coverage, frame-drop policy, train / validation / test sequence or lot isolation, downstream label head, aggregation / threshold, event truth, hardware and decision unit.
- common outputs: event recall / false alert / delay, temporal / micro-event coverage, frame-drop / variable-rate / camera / process-drift / leakage failure, token / VRAM / RAM, complete P95/P99 and review load.
- Without this common contract, latent prediction loss, embedding visualization, checkpoint name or public frozen evaluation is not an operational ranking.

## Sources

- Adrien Bardes et al., *Revisiting Feature Prediction for Learning Visual Representations from Video*, arXiv:2404.08471, 2024.
- Course source: `full-model-course/05-video-and-temporal.md`, pages 05-30 through 05-33.

## Production gate

The six model-specific fields, comparison contract and required visual primitives are complete. Pages 05-30 through 05-33 may proceed to versioned white high-density C / D visual production. Final assets must pass Chinese readability, engineering causality, no-fabricated-performance, manifest, QA and style validation before approval.

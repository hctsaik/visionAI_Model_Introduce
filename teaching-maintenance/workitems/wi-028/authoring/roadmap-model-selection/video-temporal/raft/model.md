# RAFT（`raft`）

- roadmap category: `video-temporal`
- course pages: `05-14` through `05-17`
- research status: `complete`
- visual status: `ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/raft.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
你想知道移動金屬板上不同區域如何移動，而不只追三個角點；需要一張可以往下游取樣的稠密位移圖。

### 它交出什麼，也不交出什麼
每個像素的水平／垂直影像位移估計。本課箭頭只是示意；物件身分、速度、形變量測與事件判定要另有分群、校正與驗證。

### 一句心智模型
原始 RAFT 先對兩張影格各自抽特徵，建立所有位置配對的相似線索；再反覆查詢多尺度相關性，用更新單元修正目前的光流估計。全配對提供廣泛的候選位置，反覆更新把這些線索逐步轉成每個像素的二維位移。

**限制：** 金屬反光或遮擋讓某些像素在下一影格沒有可靠可見對應；RAFT仍可能輸出數值，但這是估計，不是觀測真值。

### 換一個現場再推理
現場CPU即可，工作只需三個角點是否偏移，位移很小、紋理清楚。

**問題：** 為了稠密輸出一定要選RAFT嗎？

**核對：** 不必；先以LK或既有對位法作基準，測角點誤差與漂移。只有下游確實需要更廣位移覆蓋，且效果改善值得運算代價時，再採用RAFT。
<!-- topic-learning-bridge:end -->
<!-- wi028-model-core:start -->
## WI-028 核心做法與工作取捨

原始 RAFT 先對兩張影格各自抽特徵，建立所有位置配對的相似線索；再反覆查詢多尺度相關性，用更新單元修正目前的光流估計。全配對提供廣泛的候選位置，反覆更新把這些線索逐步轉成每個像素的二維位移。

金屬反光或遮擋讓某些像素在下一影格沒有可靠可見對應；RAFT仍可能輸出數值，但這是估計，不是觀測真值。

需要全圖位移時比較RAFT與傳統稠密光流；只需少量角點可先試LK。RAFT要權重與較多運算預算，是否值得取決於域內位移品質和下游任務。

先固定具體權重、前處理、影像解析度與更新次數。換相機／材質需測域落差，必要時另準備配對監督資料微調；同看誤差、遮擋錯誤、記憶體與端到端耗時。

先收集成對且有時間戳的影片，選定原始RAFT權重與解析度，準備可信點對／已知移動作驗證。

在相同影片和校對位置比較位移誤差、有效覆蓋、遮擋表現、完整耗時和記憶體；圖中無現場模型成績。

來源：https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123470392.pdf

版本及示意界線見工作項目 sources.md。使用者成品核准pending。
<!-- wi028-model-core:end -->
## Model identity

RAFT (Recurrent All-Pairs Field Transforms) is a learned dense optical-flow architecture.  It encodes the two frames, constructs an all-pairs correlation volume, then recurrently updates one high-resolution flow field using local correlation lookups and context.  It is a dense `(u,v)` estimator, not an object detector, identity tracker, event-release model, or a guarantee that a learned flow transfers to target optics.

All-pairs matching expands correspondence candidates; recurrent iteration refines a flow field.  The operating point therefore includes checkpoint, resize / padding, frame interval, correlation implementation, iteration count, mixed precision, postprocess, VRAM / latency and confidence / reject behavior.  A single GPU forward or a colourful flow visualization cannot stand in for complete capture-to-result P95 or target-domain evidence.

## Required fields

### architecture_path

Timestamped frame pair -> fixed ROI / registration / preprocessing / resize-padding -> feature encoder on both frames plus context encoder -> all-pairs correlation volume / named correlation implementation -> initialise flow field -> recurrent update block with context and correlation lookup -> iterative dense flow refinement for declared iterations -> upsample / postprocess -> uncertainty proxy / consistency / declared reject gate -> camera-motion separation / aggregation -> event, measurement or REVIEW action.

Store frame pair, checkpoint and encoder revisions, resize / padding, correlation configuration, iteration count, precision, intermediate / final flow, confidence or consistency signal, rejected pixels / vectors, global-motion record, downstream aggregation and final action.  Dense flow does not supply semantic class, object identity, physical velocity without calibration, root cause or release evidence.

### representation_or_score

- Motion representation: a dense two-channel flow field `(u,v)` at the declared output resolution, produced after the declared number of recurrent updates.
- Matching representation: all-pairs feature correlation plus context state; its memory and correspondence behavior are checkpoint / implementation / resolution dependent.
- Reliability evidence: a declared uncertainty proxy, forward-backward or consistency policy where configured, occlusion / out-of-domain review, and target-domain error / coverage measurement.
- Event / image score: a separately versioned aggregation of valid flow, not raw magnitude, a colour wheel, correlation peak, or public-benchmark score.

### cost_and_operating_point

Lock checkpoint / code revision, feature and context encoder, input colour / normalization, resize / padding / aspect policy, frame interval / timestamps, correlation volume implementation / precision, recurrent update iterations, mixed precision, batch / stream policy, upsampling / postprocess, confidence / reject / occlusion policy, global-motion treatment, aggregation / decision unit, hardware and owner action.

Report full capture-to-result P50/P95/P99 including capture buffer / decode, preprocessing / padding, feature / context encoders, correlation construction / lookup, every recurrent update, upsample / postprocess, consistency / reject, global-motion separation, aggregation, queue and hand-off.  Measure target-optics endpoint error or declared proxy, dense-valid coverage, reject rate, event utility, camera-motion / reflection / occlusion / frame-gap failures, VRAM / RAM, state / batch policy, review load and future / drift results; do not transplant public benchmark values as production performance.

### failure_boundary

- Learned features / correlations can shift under target texture, lighting, optics, compression, reflection, frame interval and process domain; a checkpoint does not make correspondence observable.
- Occlusion, disocclusion, repeated texture, transparency, reflection and motion boundaries can produce confident but wrong dense vectors.
- Large resolution / correlation volume and iteration count change VRAM, latency and output behavior; reducing iterations or padding policy is a new operating point.
- Frame drop / variable frame rate / long gap can make correspondence ambiguous even for a learned model.
- Camera motion / registration error creates broad flow that must be separated before local event interpretation.
- Dense flow remains neither semantic class nor track identity; it cannot replace detector / tracker evidence when the decision depends on entity or cause.

### selection_gate

Consider RAFT when target conditions justify dense flow over a lightweight local baseline: complex or larger motion, a dense motion field has a defined downstream owner, target-domain flow / proxy truth exists, and measured VRAM plus complete P95 fit the real-time budget.  Validate occlusion, reflection, camera motion and frame-gap cases explicitly.

Hold or choose Lucas–Kanade, tracking, a semantic model or human review when no dense-flow owner exists, target optics lack validation evidence, VRAM / P95 cannot meet budget, global camera motion is ungoverned, semantic identity is required, or complex motion is merely assumed.  Compare RAFT and Lucas–Kanade under the same frame pair, timestamps, ROI / registration, resolution / preprocessing, target truth or proxy, reject policy, aggregation, hardware and downstream event contract; do not compare public benchmarks or colour fields alone.

### evidence_bundle

Keep camera / lens / exposure / timestamp / frame-drop records; frame-pair / ROI / registration / preprocessing / resize-padding policy; RAFT release, checkpoint, feature / context encoder revision, correlation implementation, iterations, precision, batch / stream and postprocess; intermediate / final flow, confidence / rejected pixels and global-motion records; target-optics labelled / proxy flow and event truth; endpoint / coverage / reject / event utility / delay metrics; VRAM / RAM / complete P95/P99; occlusion, texture, reflection, frame-gap and camera-motion error sets; human owner and drift / rebuild evidence.

## Visual primitives

- `dual_encoder_pair`: frame pair -> feature encoder / context encoder with locked resize / padding and checkpoint.
- `all_pairs_correlation`: two feature grids -> correlation volume / lookup, visually distinct from local Lucas–Kanade solve.
- `recurrent_flow_refinement`: initial flow -> declared recurrent iterations -> dense field / upsample / postprocess.
- `dense_flow_cost_gate`: correlation / iterations / resolution -> VRAM and complete P95, plus confidence / occlusion / global-motion review.
- `selection_contract`: target-optics flow truth, dense-valid coverage, reject / event aggregation, hardware budget and controlled Lucas–Kanade comparison.

## Comparison contract

- comparison ID: `video-lucas-kanade-raft`
- layout: `D-2` controlled comparison.
- fixed conditions: same frame pair / timestamps / interval, ROI / registration, resolution / resize-padding, preprocessing, target-domain truth or proxy, reject / confidence policy, aggregation, hardware and decision unit.
- common outputs: endpoint / proxy error, dense-valid coverage, reject rate, event utility, occlusion / reflection / camera-motion / frame-gap failure, VRAM / RAM, complete P95/P99 and review load.
- Without this common contract, public benchmark, correlation-size claim or flow visual appearance is not a production ranking.

## Sources

- Zachary Teed and Jia Deng, “RAFT: Recurrent All-Pairs Field Transforms for Optical Flow,” ECCV 2020, arXiv:2003.12039.
- Course source: `full-model-course/05-video-and-temporal.md`, pages 05-14 through 05-17.

## Production gate

The six model-specific fields, comparison contract and required visual primitives are complete. Pages 05-14 through 05-17 may proceed to versioned white high-density C / D visual production. Final assets must pass Chinese readability, engineering-causality, no-fabricated-performance, manifest, QA and style validation before approval.

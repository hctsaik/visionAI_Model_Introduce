# ConvLSTM `convlstm`

- roadmap category: `video-temporal`
- course pages: `05-22` through `05-25`
- research status: `complete`
- visual status: `ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/convlstm.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
夾爪的單張照片看不出動作經過；你想結合前幾張畫面，判斷目前較像接近、夾取還是移開的階段。

### 它交出什麼，也不交出什麼
本例將時序狀態交給另行訓練的任務頭，產生夾取階段候選；其他接法可預測影像等，但不是單元自動具有的所有能力。

### 一句心智模型
ConvLSTM 在每個時間點把新輸入與舊狀態一起處理，以卷積更新保留空間結構的記憶，選擇保留、加入或忘掉哪些線索。相較把整張攤平處理，它保留鄰近位置的關係；相較只看單張，它可以利用前面看到的變化。

**限制：** 一段影片結束後直接沿用記憶到另一段，舊的已夾住狀態可能干擾新片段；掉幀、順序錯誤或取樣間隔改變也會改變時間意義。

### 換一個現場再推理
服務交替收到機台A和B的片段，夾爪姿態不同。

**問題：** 可以共用上一段的記憶嗎？

**核對：** 不能不加區分地共用；應按相機／連續片段隔離或重置狀態，按真正任務訓練並測邊界。若單張已足以判階段，先比較較簡單且無狀態維護的基準。
<!-- topic-learning-bridge:end -->
<!-- wi028-model-core:start -->
## WI-028 核心做法與工作取捨

ConvLSTM 在每個時間點把新輸入與舊狀態一起處理，以卷積更新保留空間結構的記憶，選擇保留、加入或忘掉哪些線索。相較把整張攤平處理，它保留鄰近位置的關係；相較只看單張，它可以利用前面看到的變化。

一段影片結束後直接沿用記憶到另一段，舊的已夾住狀態可能干擾新片段；掉幀、順序錯誤或取樣間隔改變也會改變時間意義。

少量明確動作任務，可比較單張分類、簡單時序規則與ConvLSTM；較通用影片表示可比較VideoMAE或V-JEPA。後兩者提供預訓練表示，不是免標註的現成夾爪判定器。

需準備符合任務的連續片段與標註，按完整作業／實體分開訓練與測試。換動作、相機或取樣頻率要重新驗證，必要時重訓；成本含序列等待與狀態管理。

先定義動作階段標註，保存完整循環與時間戳，依作業批次切分資料，建立單張或規則基準。

比較漏掉的階段、錯誤切換、事件延遲和完整運算成本；用丟幀／片段邊界負例檢查模型是否依賴正確時間線索。

來源：https://arxiv.org/abs/1506.04214

版本及示意界線見工作項目 sources.md。使用者成品核准pending。
<!-- wi028-model-core:end -->
## Model identity

ConvLSTM replaces the matrix products of LSTM gates with convolutions, so a recurrent hidden state and cell state retain spatial layout while a short-to-medium clip evolves. It is a temporal representation / prediction / classification or anomaly-candidate component, not an unlimited-memory mechanism, a detector, a tracking identity guarantee or an event-release decision.

The useful unit is a declared sequence window together with frame timestamps, feature encoder, spatial resolution, gate channels, state initialization / reset and downstream head. A recurrent state can carry useful motion and appearance context, but it can also warm up, drift, leak across related sequences or become invalid after a frame-rate / camera regime change. The head, aggregation, threshold and action remain separate versioned contracts.

## Required fields

### architecture_path

Timestamped frames -> fixed camera / ROI / preprocessing / frame sampling -> sequence windows of declared length and stride -> optional feature encoder -> spatial feature `x_t` plus prior hidden / cell states `(h_{t-1}, c_{t-1})` -> convolutional input, forget, output and candidate gates `(i,f,o,g)` -> updated cell and hidden states `(c_t,h_t)` -> prediction / classification / temporal map head -> window / stream aggregation -> calibrated event candidate -> PASS / REVIEW / HOLD or human action.

Store source frames and timestamps, clip membership, encoder / normalization revision, sequence length / stride, gate / hidden-channel / kernel configuration, initial / carried / reset state, warm-up markers, per-window head output, aggregation, threshold, event boundary and action. A hidden state does not itself prove an event, semantic class, object identity, root cause or future performance.

### representation_or_score

- State representation: spatial hidden state `h_t` and cell memory `c_t` at the declared feature resolution, updated only from the declared prior state and current feature.
- Gate evidence: input / forget / output / candidate activations or their governed summaries, state-reset reason and valid sequence context.
- Task score: output from a separately versioned prediction, classification or anomaly head and temporal aggregation; it is not raw gate activity, loss, hidden-state norm or a reconstructed frame alone.
- Reliability evidence: valid timestamp / sampling continuity, warm-up / reset coverage, temporal-window coverage, target event truth and drift / camera-change response.

### cost_and_operating_point

Lock camera / timestamp policy, frame rate and missing-frame rule, ROI / registration / preprocessing, encoder and normalization, spatial feature resolution, sequence length / stride / overlap, hidden channels, convolution kernel / layers, state carry and reset rule, teacher forcing / loss / training schedule, batch sequence grouping, inference buffering, downstream head / aggregation / threshold, hardware and action owner.

Report training and inference memory, clip-buffer / warm-up time, complete capture-to-event P50/P95/P99, window scheduling, encoder, every recurrent update, head, aggregation, queue and alert hand-off. Measure event recall / false alerts / delay, sequence / lot-isolated validation, frame-drop / variable-rate / camera-change / state-drift failures, state reset rate, review load and future / process-drift results. A one-step forward, training loss or frame-level accuracy is not the production event outcome.

### failure_boundary

- Long-range dependence beyond the declared receptive temporal window can be forgotten or represented unreliably; recurrent state is not a guarantee of unlimited memory.
- Variable frame rate, dropped frames, missing timestamps, scene / camera changes and uncontrolled state carry alter the semantics of every update and can cause drift.
- Sequence overlap, adjacent clips or mixed lots can leak temporal context across train / validation / test; isolation must be at sequence or lot level.
- Warm-up, reset policy, hidden channels, stride, loss and teacher forcing alter state behavior and are new operating points.
- A prediction / classification / anomaly head can fail independently of a useful temporal representation; do not promote a recurrent feature or loss to an event release.

### selection_gate

Use ConvLSTM when target motion / appearance evolves within a governed short-to-medium temporal window, spatial state has a named downstream prediction or classification owner, timestamped sequences and event truth exist, and buffer / state / complete P95 fit the operating budget. Explicitly validate warm-up, state carry, frame drops, frame-rate changes, camera changes and target process drift.

Hold or choose VideoMAE, V-JEPA, a simpler temporal baseline, a detector / tracker or human review when the required dependency is longer than the validated window, sampling is unstable, reset policy is ungoverned, camera change dominates, temporal labels / action are absent or complete P95 cannot meet budget. Compare ConvLSTM, VideoMAE and V-JEPA only with the same temporal pixels / ROI, timestamps, window / clip coverage, train-test isolation, downstream label head, aggregation, event truth, hardware and action contract; never rank a pretraining or recurrent loss as event performance.

### evidence_bundle

Keep camera / lens / timestamp / frame-rate / frame-drop records; ROI / preprocessing / encoder revision; sequence / lot membership and split audit; sequence length / stride / overlap; gate, hidden-channel, kernel, layer, state-carry / reset and warm-up configuration; training loss / teacher-forcing / checkpoint records; per-window features / states / head outputs / aggregation and reset reasons; event truth / action traces; event recall / false alert / alert delay, state reset / drift and camera-change evidence; full VRAM / RAM / P95/P99; review owner and rebuild / future-drift evidence.

## Visual primitives

- `spatial_sequence_window`: timestamped frames and fixed ROI form a declared window rather than an unbounded stream.
- `conv_gate_state_update`: current spatial feature and prior `(h,c)` drive convolutional `i,f,o,g` gates and an updated spatial state.
- `state_reset_and_warmup`: state carry, reset / missing-frame rule and warm-up are visible beside the recurrent path.
- `temporal_head_boundary`: prediction / class / map head and event aggregation are separate from recurrent-state evidence.
- `sequence_split_latency_gate`: sequence / lot isolation, temporal coverage, complete P95, drift and controlled VideoMAE / V-JEPA comparison are explicit.

## Comparison contract

- comparison ID: `video-temporal-representation-contract`
- layout: `D-2` controlled temporal-representation comparison.
- fixed conditions: same timestamped temporal pixels / ROI / preprocessing, temporal window / clip coverage, frame-drop policy, train / validation / test sequence or lot isolation, downstream label head, aggregation / threshold, event truth, hardware and decision unit.
- common outputs: event recall / false alert / delay, temporal coverage, warm-up / reset rate, frame-drop / variable-rate / camera-change / drift failure, VRAM / RAM, complete P95/P99 and review load.
- Without this common contract, a recurrent loss, representation score, checkpoint size or public pretraining metric is not an operational ranking.

## Sources

- Xingjian Shi et al., *Convolutional LSTM Network: A Machine Learning Approach for Precipitation Nowcasting*, NeurIPS 2015, arXiv:1506.04214.
- Course source: `full-model-course/05-video-and-temporal.md`, pages 05-22 through 05-25.

## Production gate

The six model-specific fields, comparison contract and required visual primitives are complete. Pages 05-22 through 05-25 may proceed to versioned white high-density C / D visual production. Final assets must pass Chinese readability, engineering causality, no-fabricated-performance, manifest, QA and style validation before approval.

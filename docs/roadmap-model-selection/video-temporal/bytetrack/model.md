# ByteTrack（`bytetrack`）

- roadmap category: `video-temporal`
- course pages: `05-18` through `05-21`
- research status: `complete`
- visual status: `ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/bytetrack.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
輸送帶上同一工件連續出現很多張，遮擋時偵測分數又會下降；你要維持它的軌跡，避免跨線計數時重複。

### 它交出什麼，也不交出什麼
帶追蹤編號的框與軌跡。跨線、停留和去重計數是應用另外設定的事件規則；ID只表示追蹤關聯，不是永久實體序號。

### 一句心智模型
ByteTrack 接收偵測器交出的框，先用高分框和既有軌跡做關聯，再拿低分框和仍未配對的軌跡比較。被遮一部分的真工件可能分數低，但位置仍符合預測；保留這條線索有機會接回同一軌跡，無法合理配對的低分噪聲則捨棄。

**限制：** 工件完全躲進遮擋後沒有任何偵測框，追蹤只能暫時預測位置；時間太久或多件交會後再出現，可能斷軌或換ID。

### 換一個現場再推理
工件進入不透明隧道，十秒後才再出現，而且外觀都一樣。

**問題：** 把低分門檻再降低就能保證原ID嗎？

**核對：** 不能；沒有框就沒有可關聯觀測。可先改善視角或增加感測／編碼標記，也可用已知通道順序設計額外規則，但要測交會和丟件；不能讓追蹤器保證永久身分。
<!-- topic-learning-bridge:end -->
<!-- wi028-model-core:start -->
## WI-028 核心做法與工作取捨

ByteTrack 接收偵測器交出的框，先用高分框和既有軌跡做關聯，再拿低分框和仍未配對的軌跡比較。被遮一部分的真工件可能分數低，但位置仍符合預測；保留這條線索有機會接回同一軌跡，無法合理配對的低分噪聲則捨棄。

工件完全躲進遮擋後沒有任何偵測框，追蹤只能暫時預測位置；時間太久或多件交會後再出現，可能斷軌或換ID。

只需單幀有沒有工件，可先用偵測；需要跨幀身分再加ByteTrack。SORT可作較簡單關聯基準，ByteTrack的差別在利用部分低分框補回線索；效果仍受偵測器影響。

追蹤器本身可直接套設定，但工件偵測器可能需要框標註與訓練。換產品要重驗偵測；換速度、幀率和遮擋要重驗關聯，總成本包含偵測和追蹤。

先準備含交會、部分／完全遮擋的工件影片，確認偵測器，人工標記一批跨幀ID與跨線事件。

固定同一偵測器，比較既有追蹤或SORT與ByteTrack的斷軌、ID切換、重複／漏計及端到端耗時；不只看偵測框是否存在。

來源：https://arxiv.org/abs/2110.06864

版本及示意界線見工作項目 sources.md。使用者成品核准pending。
<!-- wi028-model-core:end -->
## Model identity

ByteTrack is a multi-object tracking association method that consumes detector boxes and scores.  It associates high-score detections with track predictions first, then uses lower-score detections to recover track continuity before deciding unmatched / new tracks.  It is not a detector, an optical-flow replacement, a semantic classifier or proof that a missed object was detected.

Track quality is bounded by detector recall, input frame sampling, camera / ROI policy and association / lifecycle state.  ByteTrack can preserve identity through a lower-score detection when it matches an existing track, but it cannot create a measurement for an object for which the detector supplied no usable candidate.  Track IDs, box history, score, association cost, unmatched state and event timing must be recorded together.

## Required fields

### architecture_path

Timestamped frame -> fixed ROI / preprocess -> declared detector version -> boxes, scores and detector class policy -> detector-score partition into high / low candidates -> Kalman prediction / track state -> high-score association with declared IoU / motion / cost gate -> low-score recovery association -> unmatched / new / lost / removed lifecycle update -> versioned track IDs / box histories -> track-to-event aggregation / queue -> PASS / REVIEW / HOLD or human action.

Keep input detections, high / low partitions, track predictions, association matrix or costs, matches / unmatched, lifecycle transitions, ID changes / fragmentations, event boundaries and final action.  A track ID is identity bookkeeping under the declared detector / association contract, not a verified physical identity, class-quality improvement or detection recall gain.

### representation_or_score

- Track representation: per-track state (box / motion state, age, history, lifecycle) plus declared detector confidence and association cost.
- Association evidence: high-score matches, low-score recovery matches, unmatched detections / tracks, IoU / motion / appearance cost where configured, and Kalman prediction residual.
- Event score: a separately versioned aggregation of track presence / dwell / trajectory / ID continuity; not detector score, MOTA / HOTA / IDF1 alone, or a proof of object semantics.
- ID quality cannot exceed the coverage provided by the upstream detector and input sampling; a tracking metric must not be described as detector precision / recall.

### cost_and_operating_point

Lock camera / timestamps / frame rate / drops, ROI / registration / preprocess, detector architecture / weights / classes / decode / NMS / score calibration, high and low detection thresholds, class handling, Kalman model / state / process noise, association cost and gate, track buffer / lifecycle, frame sampling, dedup / event window / queue, decision unit, hardware and human owner.

Report full capture-to-track-event P50/P95/P99 including capture / decode, detector, NMS / score partition, Kalman prediction, high / low association, lifecycle, track aggregation, queue and alert hand-off.  Measure detector recall separately; then MOTA / HOTA / IDF1, ID switches, fragmentation, unmatched rate, event recall / false alert / alert delay, dense-crossing / occlusion / frame-drop failures, review load and future / drift results.  Detector-only timing or IDF1 alone is not the production outcome.

### failure_boundary

- Detector miss, class confusion, poor box localization, score shift or NMS loss limits all downstream track continuity; ByteTrack cannot recover a nonexistent detection.
- Prolonged occlusion, dense crossings, look-alike entities, abrupt motion, frame drop, low frame rate and camera motion can produce ID switches, merges or fragments.
- High / low score thresholds, IoU / motion gate, Kalman noise, track buffer and frame sampling alter association and lifecycle behavior; a threshold change is a new operating point.
- Low-score recovery can preserve valid tracks but can also attach clutter / false detections; inspect association evidence and event consequence.
- Track IDs do not establish semantic class, cause, defect, physical identity or a production release decision.

### selection_gate

Use ByteTrack when an upstream detector already has sufficient recall in the target view, the system requires continuous entity identity or dwell / trajectory event logic, and detector / association / lifecycle / event contracts can be jointly versioned.  Validate occlusion, crossing, detector-score shift and frame-drop challenges with event-level timing evidence.

Hold or choose an alternate detector, flow, semantic path or human review when detector coverage is unproven, identity is not observable, occlusion / crossing dominates, frame sampling is unstable, camera motion is ungoverned, or complete detector-to-event P95 cannot meet the alert budget.  Compare trackers only with the same detector, weights, classes, NMS, ROI, frame sampling, association truth, event rule, hardware and allowed action; never call a tracking gain detector accuracy.

### evidence_bundle

Keep camera / lens / timestamps / frame-rate / frame-drop records; ROI / preprocessing; detector / weights / class / decode / NMS / calibration revision and detector recall evidence; score partitions; Kalman / association / gate / buffer / lifecycle settings; detections, predictions, match / unmatched matrices, track histories and ID switches; event truth, timing and action traces; MOTA / HOTA / IDF1 with detector metrics held separately; occlusion, crossing, clutter, score shift, camera-motion and frame-drop galleries; full P95/P99 / hardware; review owner and drift / rebuild evidence.

## Visual primitives

- `detector_dependency`: fixed frame / ROI -> external detector boxes and scores, explicitly upstream of tracking.
- `two_stage_association`: high-score association -> low-score recovery -> matched / unmatched / lifecycle state.
- `track_kalman_state`: predicted box / association cost / track ID and buffer / lost / removed transitions.
- `detector_vs_tracking_boundary`: detector miss / class / NMS boundary distinct from ID switch / fragmentation / event timing.
- `track_event_contract`: same detector / frame sampling / ROI, track-event aggregation, complete P95 and review / HOLD action.

## Comparison contract

- comparison ID: `video-tracker-detector-contract`
- layout: `D-2` controlled tracker / detector-association comparison.
- fixed conditions: same camera / timestamps / frame sampling, ROI / preprocess, detector architecture / weights / classes / decode / NMS / calibration, association truth, event rule, hardware and decision unit.
- common outputs: detector recall (separate), MOTA / HOTA / IDF1, ID switches / fragmentation / unmatched rate, event recall / false alert / delay, dense-crossing / occlusion / frame-drop failures and complete P95/P99.
- Without this contract an ID metric must not be reported as detector accuracy or production event performance.

## Sources

- Yifu Zhang et al., “ByteTrack: Multi-Object Tracking by Associating Every Detection Box,” ECCV 2022, arXiv:2110.06864.
- Course source: `full-model-course/05-video-and-temporal.md`, pages 05-18 through 05-21.

## Production gate

The six model-specific fields, comparison contract and required visual primitives are complete. Pages 05-18 through 05-21 may proceed to versioned white high-density C / D visual production. Final assets must pass Chinese readability, engineering-causality, no-fabricated-performance, manifest, QA and style validation before approval.

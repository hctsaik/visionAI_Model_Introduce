# Background Subtraction（`background-subtraction`）

- roadmap category: `video-temporal`
- course pages: `05-06` through `05-09`
- research status: `complete`
- visual status: `ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/background-subtraction.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
固定相機監看工位，工件進入後可能停一下；你想知道哪些區域不同於平常，而不只知道它剛剛有沒有動。

### 它交出什麼，也不交出什麼
相對背景模型的前景候選遮罩。下游可另做區域、占位或停留判定；遮罩本身不是產品種類、缺陷或物件編號。

### 一句心智模型
背景相減先用一段影片累積各位置常見的外觀，再拿目前影格和背景模型比較，找出不符合常態的前景。以 MOG2 為例，背景是會更新的統計模型，不只是永遠不變的一張空景照片；這讓它能適應緩慢變化，也會帶來把停住物件學成背景的風險。

**限制：** 一片金屬停在同一位置，模型持續更新後可能逐漸把它學成背景，前景減少；工件實際仍在。反光、陰影或相機移動也會干擾前景。

### 換一個現場再推理
每天治具位置都會調整，工件常常放著不動。

**問題：** 要直接沿用昨天的背景嗎？

**核對：** 不宜直接沿用；先重建背景並測初始化，另外設計停留狀態。若布局改動頻繁且目標類別固定，可比較偵測器或占位感測器，以維護量和漏報決定。
<!-- topic-learning-bridge:end -->
<!-- wi028-model-core:start -->
## WI-028 核心做法與工作取捨

背景相減先用一段影片累積各位置常見的外觀，再拿目前影格和背景模型比較，找出不符合常態的前景。以 MOG2 為例，背景是會更新的統計模型，不只是永遠不變的一張空景照片；這讓它能適應緩慢變化，也會帶來把停住物件學成背景的風險。

一片金屬停在同一位置，模型持續更新後可能逐漸把它學成背景，前景減少；工件實際仍在。反光、陰影或相機移動也會干擾前景。

相鄰影格差分適合瞬間改變；背景相減能以常態為參考看新前景，但要維護背景更新。要知道是哪一類工件，仍需另加分類或偵測。

不需先為神經網路標註訓練，仍要代表性啟動片、正常背景與事件標記。換視角通常要重建背景；同測陰影誤報、停留漏報、恢復時間和維護成本。

先保存空工位、工件進入／停留／離開及光照變化影片，固定相機，再決定初始化和背景更新設定。

按完整事件比較前景與人工占位紀錄，測短停／長停、光照和啟動期，記錄誤報、漏報及重建背景的成本。

來源：https://docs.opencv.org/4.13.0/d1/dc5/tutorial_background_subtraction.html

版本及示意界線見工作項目 sources.md。使用者成品核准pending。
<!-- wi028-model-core:end -->
## Model identity

Background Subtraction maintains a versioned background-state model over a frame stream and marks pixels that are unlikely under that state as foreground candidates.  A running background, a mixture-of-Gaussians-style state, or another declared update rule may be used; these are not interchangeable operating points.

It is a long-sequence foreground proposal path for a relatively stable view.  It is not static-defect AD, semantic classification, object detection, identity tracking, or evidence that a pixel is a physical moving object.  The update / learning-rate rule determines whether a long-stopped object or persistent process change is preserved as foreground, absorbed into background, or routed to HOLD.

## Required fields

### architecture_path

Background initialization / declared empty-scene evidence -> fixed capture, timestamp, ROI and optional registration -> photometric preprocessing -> versioned background-state model (running statistics, GMM-style modes, or named implementation) plus learning-rate / update mask -> foreground likelihood / distance -> threshold / shadow rule -> morphology -> connected components -> event aggregation / queue -> PASS / REVIEW / HOLD or reset.

Store input frame, background estimate or state snapshot, foreground likelihood, mask, post-morphology mask, components, event window and final action together.  A foreground component is a candidate region, not a semantic object class or an identity.

### representation_or_score

- Background representation: per-pixel or per-region background statistics / mode state, initialization identity, update rate and update eligibility.
- Local evidence: foreground likelihood or distance, binary mask, shadow classification rule, component area / location / persistence.
- Event score: a versioned component / temporal aggregation under the declared event and dedup policy.
- The foreground score is not a defect probability, object class, causal explanation, track ID, velocity estimate, or proof that a persistent foreground object was not silently absorbed by the background model.

### cost_and_operating_point

Version camera / lens / exposure, timestamps / frame drops, background initialization source and date, ROI / registration, colour / normalization, background algorithm and implementation, learning rate / history / mode policy, update mask, shadow rule, likelihood / threshold, morphology kernel / iterations, component filter, persistence / event window, dedup / queue, reset / HOLD policy, decision unit and owner action.

Report full capture-to-event P50/P95/P99: capture buffer / decode, preprocessing / registration, background-state update, likelihood / mask, morphology / components, event aggregation, queue and alert delivery.  Measure event recall, false alarm, alert delay, review load, long-stopped-object absorption, camera-motion failure, illumination / shadow failure, scene-change reset, state-size / update cost and future / drift results; do not claim production behavior from a single foreground mask or background update time.

### failure_boundary

- Background initialization contamination or an incorrect empty-scene assumption can mark useful structure as background from the first frame.
- Learning rate / history can absorb long-stopped objects, gradual process changes or persistent defects; making the rate smaller can conversely leave stale background ghosts.
- Camera vibration, zoom, focus, registration error, scene reconfiguration and broad global motion invalidate the background state and require reset / HOLD rather than silent adaptation.
- Illumination drift, flicker, shadow, reflection, weather / steam, compression noise and auto-exposure can dominate foreground likelihood.
- The threshold, shadow rule, morphology, component filtering, persistence and dedup policies change event behavior even with the same background model.
- No semantic class, identity through occlusion, static tiny-defect evidence or physical root cause follows from a foreground mask alone.

### selection_gate

Consider it when view / ROI are fixed, the background is relatively stable but the task needs continuous foreground candidates over longer sequences, background initialization and update behavior can be inspected, and reset/HOLD has an owner.  Verify that stationary-event dwell time and expected illumination / scene changes are represented in challenge data.

Hold or choose Frame Difference, flow, tracking, a semantic model, or human review when camera motion or scene changes are ungoverned, long-stopped objects are critical, illumination drift dominates, the decision requires class / identity, or reset evidence / complete P95 cannot be measured. Compare with Frame Difference under identical capture, timestamps, ROI, event truth, component / aggregation rule, hardware, alert policy and drift challenge; never rank them from foreground mask appearance alone.

### evidence_bundle

Keep camera / lens / exposure / frame-rate settings; timestamp and frame-drop records; background initialization frames and audit; named background-state implementation, parameters, learning-rate / history / update-mask / shadow-rule revision; ROI / registration / preprocessing; input / background estimate / likelihood / mask / components / event traces; event-level truth split by camera / lot / shift / illumination / scene; false alarms, stopped-object absorption, stale background, camera motion, shadow and scene-change examples; reset / rollback decisions; complete P95/P99 / state size; human review and allowed-action record; future / drift rebuild evidence.

## Visual primitives

- `background_state_build`: initialization frames -> running / multi-mode background state plus explicit update rate.
- `frame_to_foreground`: current frame -> background likelihood -> foreground mask -> morphology -> component / event flow.
- `absorption_boundary`: stationary / persistent change routed through update-rate, freeze / reset / HOLD evidence rather than silently becoming normal.
- `camera_scene_gate`: global motion, registration residual, scene change, illumination / shadow and reset decision distinct from local foreground components.
- `event_and_latency_contract`: state update, component persistence, dedup / queue, complete capture-to-event P95/P99 and owner action.

## Comparison contract

- comparison ID: `video-frame-difference-background-subtraction`
- layout: `D-2` controlled comparison.
- fixed conditions: same capture / timestamp / frame rate, ROI / registration, photometric rule, event truth, resolution, component filtering, temporal aggregation, hardware, alert policy and decision unit.
- common outputs: event recall, false alarm, alert delay, review load, camera-motion / illumination robustness, long-stopped-object behavior, reset evidence and complete P95/P99.
- Without the common contract a foreground-mask or update-cost comparison has no production ranking meaning.

## Sources

- Richard Szeliski, *Computer Vision: Algorithms and Applications*, 2nd ed., motion-detection / background-modelling foundations.
- Course source: `full-model-course/05-video-and-temporal.md`, pages 05-06 through 05-09.

## Production gate

The six model-specific fields, comparison contract, and required visual primitives are complete. Pages 05-06 through 05-09 may proceed to versioned white high-density C / D visual production. Final assets must pass Chinese readability, engineering-causality, no-fabricated-performance, manifest, QA and style validation before approval.

<!-- wi033-engineering:start -->
## WI-033 工程圖修正

### 背景相減：先建立场景常態

固定相機常用MOG2累積背景，交付前景mask。mask不自帶類別或永久ID；後段需處理陰影/雜訊、連通區或偵測與追蹤。

前景是相對背景的變化，不是物件類別。

來源：https://docs.opencv.org/4.x/d1/dc5/tutorial_background_subtraction.html

### 背景相減：累積常態，再比較現在

以MOG2為例，同位置累積常見外觀的混合高斯模型，當前影像相對背景分類前景。方件長期停留時可能成為背景，前景遮罩下降；不是只和上一幀相減。更新速率/歷史/陰影處理影響結果，圖中示意不是固定吸收時間。

前景依賴背景歷史，停留物件也可能被吸收。

來源：https://docs.opencv.org/4.x/d1/dc5/tutorial_background_subtraction.html

### 背景相減：啟動與更新速度都要驗

相機重置或場景切换須重建背景。較快更新能適應變化，也可能較快吸收停留物；較慢更新可能留下照明變化前景。保存history/learningRate、陰影標籤處理與重置規則，實際驗證，不給固定適用參數。

先穩定背景，再評停留和光照變化。

來源：https://docs.opencv.org/4.x/d1/dc5/tutorial_background_subtraction.html

### 背景相減：物件沒動，不保證一直亮

前景mask空不代表現場無物件。停留物件可能被模型吸收；需保存事件/狀態並視任務接偵測追蹤，而追蹤本身也有丟失限制。

背景模型會更新，遮罩不等於物件存在。

來源：https://docs.opencv.org/4.x/d1/dc5/tutorial_background_subtraction.html

<!-- wi033-engineering:end -->

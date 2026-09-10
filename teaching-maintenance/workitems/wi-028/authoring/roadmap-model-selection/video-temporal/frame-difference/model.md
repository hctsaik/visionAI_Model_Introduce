# Frame Difference（`frame-difference`）

- roadmap category: `video-temporal`
- course pages: `05-02` through `05-05`
- research status: `complete`
- visual status: `ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/frame-difference.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
固定相機看輸送帶，你只想在畫面有明顯變化時保留事件片段，減少人工從頭看完整段影片。

### 它交出什麼，也不交出什麼
變化遮罩、變化區域及應用整合的事件片段。交給人回看或接後段偵測；不直接交出類別、穩定身分或完整輪廓。

### 一句心智模型
Frame Difference 比較兩個時間點同一位置的像素亮度，再把差得夠大的位置標出來。方片向右移時，原本有片、後來沒片的左帶，以及新進入的右帶會亮起；重疊且亮度相同的中央可能不亮。它便宜直接，因為不需要先學物件種類；也因此只知道變了，不知道是什麼。

**限制：** 工件位置不動，只有燈光閃一下，整幅亮度改變仍可能讓差分大片亮起。反過來，工件已停住且與上一影格相同時，差分可能全黑。

### 換一個現場再推理
料盤進站後停十秒，你要知道它是否仍占著工位。

**問題：** 只用相鄰影格差分夠嗎？

**核對：** 不夠；停住後變化會減少。可試背景相減加停留計時，但需避免停留時被背景吸收；若已有可靠的占位感測器或偵測器，也可作更直接基準。
<!-- topic-learning-bridge:end -->
<!-- wi028-model-core:start -->
## WI-028 核心做法與工作取捨

Frame Difference 比較兩個時間點同一位置的像素亮度，再把差得夠大的位置標出來。方片向右移時，原本有片、後來沒片的左帶，以及新進入的右帶會亮起；重疊且亮度相同的中央可能不亮。它便宜直接，因為不需要先學物件種類；也因此只知道變了，不知道是什麼。

工件位置不動，只有燈光閃一下，整幅亮度改變仍可能讓差分大片亮起。反過來，工件已停住且與上一影格相同時，差分可能全黑。

只需抓瞬間改變，可先用影格差分；要相對常態背景找新出現且暫時停住的工件，可比較背景相減。若要物件身分與跨線計數，需要另有偵測與追蹤。

不用標註訓練網路，仍需包含正常運轉、停留、閃光和晃動的影片作調整與獨立測試。換產品、光源或相機後重驗門檻；同看漏掉的事件、每小時誤觸發及回看量。

先收集固定相機的正常／停留／閃光短片，保存時間戳，選定比較間隔和監看區域。

把人工標記的事件當對照，比較差分與背景相減的事件漏報、誤報、事件延遲和完整處理成本；不把兩白帶算兩件產品。

來源：https://docs.opencv.org/4.x/d2/de8/group__core__array.html

版本及示意界線見工作項目 sources.md。使用者成品核准pending。
<!-- wi028-model-core:end -->
## Model identity

Frame Difference is a classical motion baseline: it compares a frame `I_t` with a declared reference frame `I_{t-k}` (or a separately governed reference), then thresholds changed pixels into candidate motion regions.  It is a foreground-event proposal path for a fixed camera; it is neither an object detector, an identity tracker, a semantic class model, nor a static-defect anomaly detector.

The operational model is not merely `abs(I_t - I_{t-1})`.  Frame interval, ROI, photometric normalization, threshold, morphology, connected-component rule, temporal event aggregation and reset/HOLD policy jointly define the deployed score and event output.

## Required fields

### architecture_path

Versioned capture stream and timestamps -> chosen frame interval / reference policy -> fixed ROI / optional registration and photometric normalization -> absolute pixel difference `D_t = |I_t - I_{t-k}|` -> threshold -> morphology -> connected components / region features -> temporal event aggregation -> PASS / REVIEW / HOLD or event queue.

Keep raw frame pair, difference image, binary mask, post-morphology mask, component records, event window and final action together.  A component is a candidate region; it is not a detected object class and does not establish object identity.

### representation_or_score

- Motion representation: per-pixel or per-region frame-change magnitude under the declared frame interval and ROI.
- Local evidence: binary change mask plus connected-component area, location, duration and optional persistence.
- Event score: a versioned component / event aggregation of changed pixels across the specified temporal window.
- The score is not a defect probability, object class, velocity estimate, causal explanation, track ID, or proof that foreground is physically meaningful rather than illumination/camera change.

### cost_and_operating_point

Lock camera / exposure settings, frame rate and timestamp policy, reference interval, ROI / registration, colour space and normalization, difference operator, threshold, morphology kernel / iterations, component filtering, event window / persistence rule, dedup / queue policy, threshold, decision unit, reset and HOLD policy.

Report complete capture-to-event P50/P95/P99: capture buffer / decode, preprocessing / registration, difference, morphology / components, temporal aggregation, queue and alert hand-off.  Report event-level recall, false alarm, alert delay, review load, camera-motion failure, illumination failure, missed slow motion, and future / drift results; a single-frame binary mask or operation time is not the production latency or event result.

### failure_boundary

- Illumination flicker, shadow, reflection, auto-exposure, compression noise and background texture can create foreground without physical motion.
- Camera jitter, vibration, zoom, focus and registration error move broad regions together; without a camera-motion gate the path invents many local events.
- Slow motion can vanish when `k` is too short, while a long interval can merge unrelated motion or create large trails.
- Threshold, blur / normalization, morphology and component rules can erase tiny events or inflate noise; changing any of them is a new operating point.
- Repeated background change, scene reconfiguration, dropped frames, variable frame rate and timestamp mismatch invalidate a fixed event window.
- It cannot maintain identity through occlusion, distinguish a moving part from a moving reflection, or decide semantic defect / process cause without a downstream model or human evidence.

### selection_gate

Use Frame Difference as a transparent low-cost event-candidate baseline when camera pose, ROI, exposure, frame interval and event definition are stable, and a human or downstream stage can review the candidate mask / component.  First prove the intended event remains visible at the effective pixels and target frame interval.

Hold or choose a different path for ungoverned camera motion, unstable illumination, semantic class / identity requirements, long occlusion, global scene change, or when event-level false alarms and delay cannot be measured.  Compare it with Background Subtraction under the same capture, timestamps, ROI, event truth, component / aggregation rule, hardware and alert policy; do not compare single-frame masks alone.

### evidence_bundle

Keep camera / lens / exposure / frame-rate settings; timestamp and frame-drop records; frame interval / reference policy; ROI / registration / normalization revision; frame pairs, difference images, masks and components; threshold / morphology / component / event-window / dedup / queue configuration; event-level truth and split by camera / lot / shift / illumination; false alarms, missed slow events, camera-motion and flicker examples; alert delay and complete P95/P99; human review / allowed action; drift / reset / rollback evidence.

## Visual primitives

- `frame_sequence`: two timestamped ROI frames, moving region, and declared interval `k`.
- `difference_to_event`: absolute difference -> threshold -> morphology -> component -> event-window / queue flow.
- `camera_motion_gate`: global jitter / registration residual distinct from local component evidence.
- `event_contract`: component area / persistence / aggregation / dedup / alert ownership as a versioned decision contract.
- `failure_and_hold_gate`: flicker, shadows, slow motion, background noise, dropped frame and camera motion route to REVIEW or HOLD rather than invented physical events.

## Comparison contract

- comparison ID: `video-frame-difference-background-subtraction`
- layout: `D-2` controlled comparison.
- fixed conditions: same capture / timestamps, frame rate / interval, ROI / registration, event truth, resolution, hardware, component and temporal aggregation, alert policy and decision unit.
- common outputs: event recall, false alarm, alert delay, review load, camera-motion robustness, illumination robustness, complete P95/P99 and rebuild / reset evidence.
- Without this common contract neither the foreground masks nor processing time establish a ranking.

## Sources

- Richard Szeliski, *Computer Vision: Algorithms and Applications*, 2nd ed., motion-detection / background-modelling foundations.
- Course source: `full-model-course/05-video-and-temporal.md`, pages 05-02 through 05-05.

## Production gate

The six model-specific fields, comparison contract, and required visual primitives are complete. Pages 05-02 through 05-05 may proceed to versioned white high-density C / D visual production. Final assets must pass Chinese readability, engineering-causality, no-fabricated-performance, manifest, QA and style validation before approval.

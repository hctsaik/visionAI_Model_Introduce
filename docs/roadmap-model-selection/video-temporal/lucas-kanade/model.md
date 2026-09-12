# Lucas–Kanade（`lucas-kanade`）

- roadmap category: `video-temporal`
- course pages: `05-10` through `05-13`
- research status: `complete`
- visual status: `ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/lucas-kanade.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
相機看金屬板移動，你只需要幾個清楚角點的影像位移，作為運動監看或後續對位線索。

### 它交出什麼，也不交出什麼
選定點在下一影格的位置、追蹤狀態及可由座標差得到的位移；不直接提供整張光流、物件身分或毫米速度。

### 一句心智模型
本課用金字塔 Lucas–Kanade 的稀疏追點形式：先選可辨認的角點，再在下一影格的局部鄰域找能讓亮度變化最一致的小位移。附近像素提供共同線索，比單一像素更能約束移動方向；金字塔先在縮小影像抓粗位移，再逐層修細。

**限制：** L形刻痕被反光或遮擋蓋住，下一影格失去可對應紋理，點可能追丟或追錯。漂亮的箭頭本身不能證明對應正確。

### 換一個現場再推理
鏡面表面很平，只有少量邊角偶爾可見，你只需要判斷整件是否移動。

**問題：** 一定要改用RAFT嗎？

**核對：** 不一定；可先改善光照或加可追蹤標記，再用LK驗證少量點；也可比較整體對位。RAFT能給稠密估計，但不能創造被反光或遮擋抹掉的真實對應。
<!-- topic-learning-bridge:end -->
<!-- wi028-model-core:start -->
## WI-028 核心做法與工作取捨

本課用金字塔 Lucas–Kanade 的稀疏追點形式：先選可辨認的角點，再在下一影格的局部鄰域找能讓亮度變化最一致的小位移。附近像素提供共同線索，比單一像素更能約束移動方向；金字塔先在縮小影像抓粗位移，再逐層修細。

L形刻痕被反光或遮擋蓋住，下一影格失去可對應紋理，點可能追丟或追錯。漂亮的箭頭本身不能證明對應正確。

只需少量穩定點，可先用LK，通常準備與計算較簡單；需要全畫面位移時可比較RAFT或傳統稠密光流。全圖覆蓋不代表每點都可信。

不用網路權重，仍需固定窗口、層數、角點選擇與時間戳。換材質與速度要重驗可追點比例、錯配、漂移及完整耗時；不要只比每秒張數。

先取有清楚角點及反光／遮擋的影片，固定幀間隔，人工核對一批點對，再選窗口和金字塔。

在同影片上比點對誤差、追丟比例、長序列漂移與成本；若與稠密方法比較，於相同點位置採樣並另外記錄覆蓋範圍。

來源：https://docs.opencv.org/4.x/d4/dee/tutorial_optical_flow.html

版本及示意界線見工作項目 sources.md。使用者成品核准pending。
<!-- wi028-model-core:end -->
## Model identity

Lucas–Kanade is a local optical-flow estimator.  It solves a small least-squares motion problem around a feature / patch under brightness constancy, small displacement and locally coherent motion assumptions.  Sparse feature tracking and dense patch-grid variants are different sampling / operating choices, not a claim that it maintains semantic identity over long occlusion.

It outputs a two-dimensional displacement `(u, v)` plus evidence for whether that local solve is trustworthy.  A colour flow field is visualization only: the deployable result must retain feature / patch location, frame pair, pyramid level, local matrix conditioning or residual, outlier gate, camera-motion treatment and downstream event / owner action.

## Required fields

### architecture_path

Timestamped frame pair -> fixed ROI / optional registration and photometric rule -> selected feature points or patch grid -> image gradients `I_x, I_y` and temporal gradient `I_t` -> local normal equation / least-squares solve -> optional coarse-to-fine pyramid update -> local flow vectors `(u,v)` -> conditioning / photometric residual / forward-backward or declared outlier confidence -> camera-motion separation or registration -> event / measurement / review action.

Preserve frame pair, feature / patch IDs, pyramid levels, gradients or declared implementation, flow, condition number / residual, rejected vectors, global-motion estimate and downstream action.  The flow vector does not by itself provide object class, causal label, long-term track ID or acceptance decision.

### representation_or_score

- Motion representation: local two-dimensional flow vector `(u,v)` at each declared feature or patch location and pyramid level.
- Solve evidence: spatial-gradient matrix conditioning / texture support, brightness / photometric residual and any forward-backward or outlier-consistency gate.
- Event / image score: a separately versioned aggregation of valid local vectors; not the raw vector magnitude alone.
- Flow is not a defect probability, class, identity, depth, physical velocity without camera calibration, proof of correct registration, or proof that a colourful visualization is accurate.

### cost_and_operating_point

Lock capture / timestamps / frame interval, ROI / registration, colour / illumination normalization, feature detector or patch-grid rule, window size / weighting, pyramid levels / scale, iterations / termination, solver / precision, conditioning or residual threshold, outlier / forward-backward gate, global-motion estimator, vector aggregation, event / decision unit, hardware and owner action.

Report full capture-to-result P50/P95/P99 for capture buffer / decode, preprocessing / registration, feature selection, pyramid / gradient / solve, outlier / global-motion separation, aggregation, queue and hand-off.  Measure target-domain endpoint error or proxy flow truth, valid-vector coverage, reject rate, event utility, false alert, alert delay, camera-motion error, illumination / texture / occlusion failures and future / drift results.  A per-vector solve time or colour wheel image is not an operational P95 or event result.

### failure_boundary

- Near-uniform or repeated texture makes the local gradient matrix ill-conditioned; a vector can be numerically produced without being supported by observable texture.
- Large displacement, low frame rate / dropped frames or insufficient pyramid coverage violate local linearization and can converge to a wrong motion.
- Brightness change, reflection, flicker, shadow, blur, focus change and compression violate photometric consistency.
- Occlusion, disocclusion and motion boundary crossings mix unrelated pixels in one window; LK does not preserve identity through them.
- Camera jitter / global motion dominates local flow unless registration or a declared global-motion model is separated first.
- Window, pyramid, termination, confidence / residual gate, vector aggregation and frame interval each change the operating point; flow magnitude alone is not comparable across them.

### selection_gate

Use Lucas–Kanade when the camera and capture contract are governed, frame rate makes displacement locally small, target texture supports local solves, and a lightweight sparse / local flow signal is useful for a downstream event or measurement owner.  Prove valid-vector coverage and reject behavior in target optics before deployment.

Hold or choose RAFT, a tracking path, semantic model or human review when large / complex motion, weak / repetitive texture, long occlusion, unstable illumination, unknown camera motion, identity requirement or unmeasured P95 dominates.  Compare with RAFT under identical frame pair, timestamps, ROI, resolution, preprocessing, target-domain truth / proxy, confidence / reject policy, hardware, aggregation and downstream event contract; do not rank coloured flow pictures.

### evidence_bundle

Keep camera / lens / exposure / frame-rate / timestamp and frame-drop records; frame-pair / ROI / registration / normalization revision; feature or grid policy; pyramid / window / weighting / solver / termination / precision settings; flow vectors, feature IDs, condition / residual / confidence, rejected vectors and global-motion records; target-domain flow or proxy truth; endpoint / coverage / reject / event utility / delay metrics; texture, blur, flicker, large displacement, occlusion and camera-motion failure examples; full P95/P99 / hardware / state records; owner action and drift / rebuild evidence.

## Visual primitives

- `frame_pair_and_features`: timestamped frames, local texture points or patch grid and declared frame interval.
- `gradient_window_solve`: `I_x`, `I_y`, `I_t` in a local window -> normal equation -> `(u,v)` vector.
- `pyramid_and_confidence`: coarse-to-fine levels plus condition / residual / outlier gate rather than a decorative colour field.
- `camera_motion_separation`: global-motion / registration evidence distinct from local vectors.
- `flow_to_action_contract`: valid-vector coverage, aggregation, event / measurement owner, complete P95 and HOLD path.

## Comparison contract

- comparison ID: `video-lucas-kanade-raft`
- layout: `D-2` controlled comparison.
- fixed conditions: same frame pair / timestamps / interval, ROI / registration, resolution, colour / preprocessing, target-domain truth or proxy, reject / confidence policy, aggregation, hardware and decision unit.
- common outputs: endpoint / proxy error, valid-vector coverage, reject rate, event utility, camera-motion robustness, occlusion / illumination failure, complete P95/P99 and review load.
- Without this common contract no flow-field appearance, average operation cost or public benchmark is a production ranking.

## Sources

- Bruce D. Lucas and Takeo Kanade, “An Iterative Image Registration Technique with an Application to Stereo Vision,” 1981.
- Course source: `full-model-course/05-video-and-temporal.md`, pages 05-10 through 05-13.

## Production gate

The six model-specific fields, comparison contract and required visual primitives are complete. Pages 05-10 through 05-13 may proceed to versioned white high-density C / D visual production. Final assets must pass Chinese readability, engineering-causality, no-fabricated-performance, manifest, QA and style validation before approval.

<!-- wi033-engineering:start -->
## WI-033 工程圖修正

### Lucas–Kanade：先讓角點有可追的鄰域

同一L形標记随工件平移；先固定相機、時間間隔及取像，選有雙方向梯度的角點。金字塔由粗到細估計位移，傳遞估計再修細；它擴大可處理位移，但不能補回被反光遮住的內容。

清楚角點、穩定影格與小位移，是局部解的起點。

來源：https://docs.opencv.org/4.13.0/d4/dee/tutorial_optical_flow.html

### Lucas–Kanade：多個像素一起限制位移

在小位移、局部共同運動與亮度一致假設下，每個像素給Ix·u+Iy·v+It≈0。教學給定三組梯度(1,0,-2)、(0,1,-1)、(1,1,-3)，共同解u=2、v=1，單位是影格間像素位移。真實資料以最小平方近似求解，再查矩陣條件、殘差及往返一致性；示意數值不是對插圖執行光流的結果。

局部梯度支持共同位移，解出數字後仍要檢查。

來源：https://docs.opencv.org/4.13.0/d4/dee/tutorial_optical_flow.html

### Lucas–Kanade：把可追的點與失效分開

保存前後影格ID、座標、時間差、狀態與殘差；追丟或一致性差的點不可沿用舊箭頭。需要物理位移或速度時，另有相機運動處理、平面/深度條件與尺度校正，不能把像素向量直接標成毫米或物件ID。

保存點對、時間與有效性，再決定能否接量測。

來源：https://docs.opencv.org/4.13.0/d4/dee/tutorial_optical_flow.html

### Lucas–Kanade：同題比較稀疏與稠密

同一L形工件、影格間隔和原圖；若工作只需少數穩定角點，LK可作基準。需要稠密場時加入RAFT；在共同可評位置比較位移錯誤，另報各自覆蓋率和端到端耗時，不能把不同輸出數量當成精度優勢。

先確定需要哪些位置，再比較錯誤與完整成本。

來源：https://docs.opencv.org/4.13.0/d4/dee/tutorial_optical_flow.html

<!-- wi033-engineering:end -->

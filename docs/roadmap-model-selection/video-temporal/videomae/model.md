# VideoMAE `videomae`

- roadmap category: `video-temporal`
- course pages: `05-26` through `05-29`
- research status: `complete`
- visual status: `ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/videomae.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
夾爪影片很多，人工動作標註卻少；你希望先利用影片本身學有用表示，再訓練一個符合工作的階段判斷器。

### 它交出什麼，也不交出什麼
影片特徵，以及本例下游任務頭的夾取階段候選。不是原生缺陷mask、物件ID或未經訓練的異常分數。

### 一句心智模型
原始 VideoMAE 把影片切成時空小塊，遮住大部分塊，只將可見部分送進編碼器，再用解碼器學著補回遮蔽位置的像素。跨影格相同位置的遮蔽降低直接抄鄰幀的捷徑，讓預訓練練習推動編碼器學習時空線索。

**限制：** 稀疏取樣剛好漏掉瞬間滑落，模型輸入只有前後看似正常的姿態；即使編碼器預訓練很強，也不能據此保證發現沒看見的事件。

### 換一個現場再推理
每段只抽幾張，滑落只維持很短時間，大部分取樣都避開它。

**問題：** 換更大的VideoMAE就夠了嗎？

**核對：** 先改善取樣讓事件可見，再比較模型與任務頭。可增加局部高頻觸發或調整窗口，但需衡量延遲和資料量；不能以預訓練重建能力代替事件召回驗證。
<!-- topic-learning-bridge:end -->
<!-- wi028-model-core:start -->
## WI-028 核心做法與工作取捨

原始 VideoMAE 把影片切成時空小塊，遮住大部分塊，只將可見部分送進編碼器，再用解碼器學著補回遮蔽位置的像素。跨影格相同位置的遮蔽降低直接抄鄰幀的捷徑，讓預訓練練習推動編碼器學習時空線索。

稀疏取樣剛好漏掉瞬間滑落，模型輸入只有前後看似正常的姿態；即使編碼器預訓練很強，也不能據此保證發現沒看見的事件。

與V-JEPA相比，VideoMAE預訓練重建像素，V-JEPA預測特徵；兩者都要對應下游任務。ConvLSTM適合比較如何維持連續狀態，但不是相同的預訓練方法。

可先使用相容預訓練權重，不必自行從零預訓練；仍需標註下游任務和留出完整事件測試。換產品或動作後重新驗證／微調，計入影片解碼、片段等待、記憶體與分類耗時。

先定義片段長度、取樣及動作類別，整理未標影片與較小的標註集，按完整作業切分，選定2022原版相容權重。

固定工作資料與時間窗口，和單張、簡單時序及其他影片特徵基準比較動作混淆、短事件漏報、延遲和標註維護量。

來源：https://arxiv.org/abs/2203.12602

版本及示意界線見工作項目 sources.md。使用者成品核准pending。
<!-- wi028-model-core:end -->
## Model identity

VideoMAE is a masked-video-autoencoder pretraining family. It turns a sampled clip into spatiotemporal tubelet / patch tokens, masks a large declared fraction, encodes visible tokens with a video transformer, and uses a lightweight decoder to reconstruct masked targets. The resulting encoder representation is normally transferred or fine-tuned for a downstream task; it is not itself a deployed event detector, an anomaly score, a tracker or proof that a short event was observed.

Its operating point is defined by timestamped clip coverage, spatial preprocessing, frame sampling, tubelet / patch shape, clip length, visible-token mask design and ratio, checkpoint / pretraining data provenance, fine-tuned downstream head, sliding-window aggregation and complete buffer-to-action latency. A reconstruction objective evaluates the self-supervised training task. It must not be promoted to target anomaly / event performance without a declared task head and event-level evidence.

## Required fields

### architecture_path

Timestamped video frames -> fixed ROI / preprocessing / frame sampling -> declared clip length and sliding-window policy -> tubelet / patch tokenization with positional / temporal encoding -> high-ratio mask sampled under a declared policy -> visible-token transformer encoder -> lightweight decoder reconstructs masked tokens / pixels / features -> learned video representation -> frozen or fine-tuned downstream prediction / classification / anomaly head -> temporal aggregation -> calibrated event candidate -> PASS / REVIEW / HOLD or human action.

Store source frames / timestamps, clip membership and overlap, ROI / augmentation / normalization, tubelet / patch and positional encoding configuration, mask ratio / shape / seed policy, pretraining checkpoint / data revision, encoder / decoder and fine-tune-head revision, visible / masked token records or summaries, clip buffering, per-window outputs, aggregation, threshold, event boundary and action. A masked-token reconstruction loss or image reconstruction does not prove detection, anomaly, semantic class, cause or event release.

### representation_or_score

- Representation: contextual visible tubelet / patch tokens and clip embedding produced by the declared encoder / checkpoint / clip sampling policy.
- Pretraining objective: reconstruction of masked targets under declared tubelet, mask and decoder policy; it is a training signal, not an operational anomaly / event score.
- Downstream score: a separately versioned fine-tuned or frozen-head output and temporal aggregation calibrated to the target decision unit.
- Reliability evidence: clip / event temporal coverage, mask and checkpoint provenance, train / validation / test clip isolation, target event truth, sampling / short-event-miss and domain-shift response.

### cost_and_operating_point

Lock camera / timestamp and missing-frame policy, ROI / preprocessing / augmentation, clip length / frame sampling / stride / overlap, tubelet / patch size, positional / temporal encoding, mask ratio / shape / sampling policy, pretraining corpus / checkpoint, encoder / decoder, fine-tune head / loss, batch / mixed precision / token budget, inference clip buffer / sliding window / aggregation / threshold, hardware and action owner.

Report pretraining and fine-tuning cost separately from inference. For deployment, report capture-to-event P50/P95/P99 including clip buffer, decode, preprocessing, tokenization, encoder, downstream head, sliding-window aggregation, queue and hand-off. Measure clip / event coverage, event recall / false alert / delay, short-event miss, frame-drop / variable-rate / domain-shift cases, train-test adjacent-clip leakage, token count / VRAM / RAM, review load and future / drift results. Encoder-only throughput or masked reconstruction loss is not deployment performance.

### failure_boundary

- Sparse / coarse frame sampling or long tubelets can omit a micro-event before the encoder sees it; a high reconstruction score cannot recover unobserved pixels / time.
- Clip length, stride, overlap, mask ratio / shape, tokenization and checkpoint alter visible context, compute and representation behavior; any change is a new operating point.
- Adjacent / overlapping clips, shared sequences or lots can leak temporal evidence across train / validation / test; data isolation must be by sequence / lot and temporal neighborhood.
- Pretraining data and checkpoint can shift under target optics, motion, camera, compression, process and label semantics; self-supervised transfer is not automatic.
- Reconstruction objective, encoder embedding or public pretraining metric does not establish an anomaly score, event head, alert timing or release action.

### selection_gate

Use VideoMAE when there is sufficient timestamped video data, a self-supervised video representation can be reused or fine-tuned for a named downstream head, clip coverage includes the target process temporal scale, and clip buffer / token / VRAM / complete P95 fit the operating budget. Validate target-domain event coverage, adjacent-clip isolation, short-event sampling, domain transfer and event-level timing.

Hold or choose ConvLSTM, V-JEPA, a simpler video baseline, a detector / tracker or human review when events are shorter than sampling / tubelet coverage, task labels or an accountable head are missing, domain mismatch dominates, clip latency cannot meet budget, temporal leakage cannot be ruled out or a reconstruction objective is being used as an event claim. Compare VideoMAE, ConvLSTM and V-JEPA only with the same temporal pixels / ROI, timestamps, clip / window coverage, train-test sequence isolation, downstream label head, event truth, aggregation, hardware and action contract; never rank methods by pretraining objective alone.

### evidence_bundle

Keep camera / lens / timestamps / frame-rate / missing-frame records; ROI / preprocessing / augmentation; sequence / lot membership and split audit; clip length / stride / overlap and sliding-window policy; tubelet / patch / positional encoding; mask ratio / shape / seed; pretraining data / checkpoint / decoder / encoder / fine-tune-head revisions; visible / masked token summaries, per-window head outputs and aggregation; target event truth / action traces; event recall / false alert / delay / short-event-miss evidence; token / VRAM / RAM / complete P95/P99; frame-drop, compression, optics, domain-shift and future-drift sets; review owner and rebuild evidence.

## Visual primitives

- `clip_tubelet_window`: timestamped frames are sampled into a declared clip, tubelet and temporal-token coverage.
- `high_ratio_mask`: visible and masked spatiotemporal tokens are visibly separated with a mask policy rather than random decorative holes.
- `encoder_decoder_reconstruction`: visible tokens drive transformer encoder, lightweight decoder and masked-target reconstruction, distinct from the downstream head.
- `downstream_head_boundary`: learned representation feeds a named fine-tuned / frozen task head and temporal event aggregation; reconstruction loss is not the event score.
- `clip_split_latency_gate`: adjacent-clip / lot isolation, short-event coverage, token / VRAM, complete P95 and controlled ConvLSTM / V-JEPA comparison are explicit.

## Comparison contract

- comparison ID: `video-temporal-representation-contract`
- layout: `D-2` controlled temporal-representation comparison.
- fixed conditions: same timestamped temporal pixels / ROI / preprocessing, clip or window temporal coverage, frame-drop policy, train / validation / test sequence or lot isolation, downstream label head, aggregation / threshold, event truth, hardware and decision unit.
- common outputs: event recall / false alert / delay, clip / temporal coverage, short-event miss, frame-drop / variable-rate / domain-shift / leakage failure, token / VRAM / RAM, complete P95/P99 and review load.
- Without this common contract, masked-reconstruction loss, pretraining data size, checkpoint name or public pretraining score is not an operational ranking.

## Sources

- Zhan Tong et al., *VideoMAE: Masked Autoencoders are Data-Efficient Learners for Self-Supervised Video Pre-Training*, NeurIPS 2022, arXiv:2203.12602.
- Course source: `full-model-course/05-video-and-temporal.md`, pages 05-26 through 05-29.

## Production gate

The six model-specific fields, comparison contract and required visual primitives are complete. Pages 05-26 through 05-29 may proceed to versioned white high-density C / D visual production. Final assets must pass Chinese readability, engineering causality, no-fabricated-performance, manifest, QA and style validation before approval.

<!-- wi033-engineering:start -->
## WI-033 工程圖修正

### VideoMAE：預訓練與分類分工

重建預訓練不直接定義夾取失敗；下游以標註片段微調或固定編碼器學頭，必須明列模式。部署用新影片與分類路徑。

預訓練學表示，標註任務教答案。

來源：https://arxiv.org/abs/2203.12602

### VideoMAE：遮時空塊，訓練補像素

原版VideoMAE預訓練使用跨時間一致tube mask，通常90–95%高比例；圖中小格只示意對位，不代表實際比例。編碼器處理可見tokens，輕量解碼器加入mask tokens重建像素，以原遮蔽位置像素監督；下游動作分類使用編碼器及另外訓練任務頭，不使用預訓練解碼器。 r01實看修正：解碼重建格上移，與caption保留間距。

補像素訓練表示，部署另接任務頭。

來源：https://arxiv.org/abs/2203.12602

### VideoMAE：token與取樣決定成本

全注意力成對數約隨N平方；給定100與200 tokens，其N平方1萬/4萬只是計算量尺度示例，不是實測毫秒。取樣跨距大可能漏短失敗。 r01實看修正：时间刻度及標籤各自定位。

減少取樣可省成本，也可能漏掉短事件。

來源：https://arxiv.org/abs/2203.12602

### VideoMAE：補得像，不保證分類對

作者例：100格中99格平方差0、關鍵格100，平均1；平均重建差不能直接當事件成功率。少數關鍵動作需標註與下游驗證。 r01實看修正：99格/1格都明寫平方差，避免把差100誤讀成平方後1萬。

像素重建與任務判斷必須分開驗。

來源：https://arxiv.org/abs/2203.12602

<!-- wi033-engineering:end -->

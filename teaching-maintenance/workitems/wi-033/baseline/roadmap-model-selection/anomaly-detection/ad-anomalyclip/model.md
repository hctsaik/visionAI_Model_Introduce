# AnomalyCLIP (`ad-anomalyclip`)

- roadmap category: `anomaly-detection`
- course pages: `04-63` through `04-66`
- research status: `complete`
- visual status: `ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/ad-anomalyclip.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
金屬板的細痕 p 需要檢出，正常孔邊 q 又不能一直誤報；先確認資料與需要的位置或問答輸出。

### 它交出什麼，也不交出什麼
交付可疑位置線索；文字或熱圖都不能直接代表精密輪廓、尺寸、根因或自動放行。

### 一句心智模型
以輔助正常／異常資料和區域標註，聯合整圖與局部監督學習物件無關的狀態提示。CLIP 骨幹權重固定，文字提示可學，DPAM 調整注意力以保留局部語意；目標影像與兩種文字表示比較，再整合多層局部線索。目標零樣本不代表模型從未訓練。

**限制：** 語意與位置仍可能錯；必須用未見正常與真缺陷檢查適用範圍。

### 換一個現場再推理
新產品外觀、允收反光與缺陷型態都不同。

**問題：** 哪些準備與驗證不能直接沿用？

**核對：** 重新核對提示來源、正常參考或既有模型的適用範圍；有適配時另留驗證資料。分開檢查正常誤報、真缺陷漏檢與成本；需要對話時再驗文字是否有據。
<!-- topic-learning-bridge:end -->
## Model identity

This course's AnomalyCLIP is **Object-agnostic Prompt Learning for Zero-shot Anomaly Detection** (ICLR 2024). It adapts CLIP using auxiliary training data to learn object-agnostic normality / abnormality text prompts, then applies that learned prompt state to target-domain zero-shot anomaly detection and localization. Its goal is to focus vision-language alignment on abnormal regions rather than foreground object semantics.

“Zero-shot” here means no target-dataset training sample is required at evaluation, not no learned state exists. The CLIP base, prompt-learning data and split, learned prompt-token weights, text-encoder adaptation state, template / object-name policy, selected image / patch features, patch map aggregation, and local calibration are part of the release contract. It remains a vision-language similarity score, not specialist pixel metrology or a defect probability.

## Architecture path

### Build

Declare the auxiliary prompt-learning data / taxonomy / split and target-domain exclusion -> lock CLIP image and text base checkpoint / tokenizer / preprocessing -> train or load object-agnostic normal and anomaly prompt tokens (and the declared feature / text adaptation state) with recorded loss, steps, seed, optimizer, and checkpoint selection -> lock template / object-name policy, selected global and intermediate patch features, patch-to-map rule, similarity / normalization, aggregation, calibration, threshold, and decision unit.

Version auxiliary data IDs and licenses, target-leakage audit, prompt initialization / context length / tokens, learnable parameters, text-encoder freeze / adaptation scope, image feature layers / visual adaptation, prompt / feature losses and weights, training schedule, checkpoint hashes, input recipe, ROI / registration, map interpolation / smoothing / aggregation, calibration data and revision, and abstention / review owner.

### Inference

Test ROI -> same preprocessing -> frozen or declared adapted CLIP image encoder -> global image and intermediate patch features -> learned object-agnostic normal / anomaly prompt token embeddings -> normalized similarities / normal-anomaly margins -> versioned patch-map and image aggregation -> local calibration / threshold / abstain -> PASS / REVIEW / HOLD.

Record image, ROI, CLIP and prompt checkpoint revision, prompt-token / text-embedding hash, feature-layer state, local similarities, patch map, image score, calibration state, and decision. Runtime includes ROI / preprocessing, every selected image and intermediate feature extraction, prompt text embedding reuse / construction, similarity, map resize / aggregation, calibration, transfer, and hand-off; measure P50/P95/P99 under the declared precision / batch / hardware policy.

## Representation and score

- Normality representation: learned object-agnostic normal versus abnormal prompt embeddings aligned to global image and local patch features under a locked CLIP / adaptation state.
- Local evidence: a declared intermediate-feature / patch similarity margin mapped to pixels; it depends on patch receptive field, interpolation, feature layer, prompt adaptation, and aggregation.
- Image score: a versioned fusion of global and local normal-anomaly similarity terms, calibrated and thresholded under a declared decision unit.
- The score is an operating signal, not a defect probability, root-cause label, proof that auxiliary-data language matches production defects, or proof of resolution below the patch receptive field.

## Cost and operating contract

Version together:

- CLIP checkpoint / tokenizer / image and text preprocessing / precision; prompt initialization, learned normal / anomaly tokens, context length, templates, object-name policy, prompt / text encoder / image feature adaptation scope, training data / split / exclusion audit, loss, steps, seed, optimizer, schedule, and checkpoints;
- ROI, registration, input resolution, crop / padding, colour conversion, transforms, normalisation, selected global / intermediate feature layers, patch mapping / interpolation, and visual feature state;
- similarity metric / temperature / normalization, global-local fusion, map smoothing / masking / aggregation, calibration data / threshold revisions, decision unit, abstention, review owner, and output schema;
- auxiliary-to-target prompt transfer, prompt variance / sensitivity, layer and patch-resolution ablations, target-domain / language mismatch, low-FPR, false reject / review load, localization, real holdout, unseen product, future / drift results, and error taxonomy;
- prompt-learning / adaptation training cost, complete image-to-decision P50/P95/P99, memory, batch / cache policy, transfer / hand-off, repeatability, and hardware.

## Failure boundary

- Auxiliary prompt-learning data can leak target semantics, overfit prompts, or encode a language / defect taxonomy that does not transfer; maintain source IDs, split boundaries, and target exclusion evidence.
- Learned tokens, context length, template, object-name policy, tokenizer, CLIP revision, text-encoder adaptation, and checkpoint changes can shift normal-anomaly margins and require recalibration.
- Selected intermediate features and patch map resolution can miss tiny defects; interpolation, smoothing, aggregation, calibration, and threshold can further change low-FPR behavior.
- CLIP image / text domain mismatch, new material / illumination / view / camera / product language, and differences between auxiliary and target anomalies can cause false alarms or false normal scores.
- Local prompt-aligned heatmaps are not causal explanations and do not establish global counts, relationships, assembly sequence, or metrology.
- Do not compare AnomalyCLIP with WinCLIP as “more language ability”: the substantive trade-off is learned / adapted prompt state and transfer risk versus frozen prompt ensemble / reference policy.

## Selection gate

Consider AnomalyCLIP when an existing CLIP path has a governed auxiliary-data and prompt-learning program, target-data exclusion can be proven, the team accepts adaptation / prompt transfer risk, and real target holdout can measure local patch evidence, low-FPR, review load, prompt variance, unseen product, and complete P95.

Hold or use a specialist AD method when auxiliary data or source licensing is unclear, target leakage cannot be excluded, prompt transfer is unstable, defects are below patch effective pixels, low-FPR / traceable ROI requirements are critical, or global logic dominates. Compare WinCLIP and AnomalyCLIP under the same CLIP base where possible, prompt / class naming policy, ROI, image recipe, patch layout, calibration, threshold, decision unit, hardware, target holdout, and error taxonomy.

## Visual primitives

- `auxiliary_prompt_learning`: auxiliary-data split / target exclusion -> CLIP base -> learned normal / anomaly prompt tokens and declared text / feature adaptation state.
- `object_agnostic_alignment`: global and patch image features -> learned generic normal / anomaly embeddings -> similarity margins -> image score / patch map.
- `prompt_transfer_contract`: token weights / template / context / tokenizer / checkpoint / feature layer / calibration version and test-domain transfer evidence.
- `prompt_evidence_review`: auxiliary-to-target transfer, prompt variance, patch resolution, real holdout low-FPR / false reject / review load, unseen product, drift, and full P95/P99.
- `selection_gate`: prompt overfit / leakage, language-domain mismatch, patch effective pixels, global logic, and fair WinCLIP comparison.

## Evidence bundle

Keep auxiliary-data IDs, license / split / target-exclusion audit; CLIP / tokenizer / prompt / adaptation checkpoints and losses; prompt-token / text-embedding revisions; ROI / image recipe / selected feature-layer / patch-map state; input / features / similarities / map / score / calibration / decision traces; prompt-transfer and variance tests; tiny-defect / domain-language / drift failures; real target holdout, low-FPR, false reject, review load, abstention, and localization evidence; runtime / training cost / memory / hardware records; and a prompt-transfer rebuild trigger.

## Sources

- Zhou et al., "AnomalyCLIP: Object-agnostic Prompt Learning for Zero-shot Anomaly Detection," ICLR 2024, [arXiv:2310.18961](https://arxiv.org/abs/2310.18961), [official implementation](https://github.com/zqhang/AnomalyCLIP).
- Course source: `full-model-course/04-anomaly-detection.md`, pages 04-63 through 04-66.

## Production gate

Research contract and visual primitives are complete. Pages 04-63 through 04-66 may proceed to white high-density C / D visual production and model-local QA.

## F01 模型中心思想與來源核對

通用 CLIP 常先認出物件名稱，而不是細微正常與異常。AnomalyCLIP在輔助資料上學與物件類別無關的狀態提示，把注意重點轉向異常語意。

**提示由資料學習**：正常／異常提示包含可學習 tokens，在輔助資料上訓練；目標產品 zero-shot 不代表全流程從未訓練。

**全局和局部對齊**：共同學習整圖與局部的正常／異常語意，讓提示不只服務物件分類，也支持位置線索。

**轉移到目標產品**：目標影像與學到的提示比較，產生整圖與局部結果；提示能否跨到新材質仍需現場驗證。

**移除設計自測**：把學到的提示換成任意一句手寫描述，還是相同方法嗎？

不再是同一已學提示模型，結果需重驗。WinCLIP 偏固定模板組合，AnomalyCLIP 的重要差異是輔助資料學到的物件無關提示。

**選型**：有可用預訓練提示模型而目標標註稀少可試；核對輔助資料是否含目標評測資料，並以新產品正常／異常樣本測轉移。

[原論文／官方來源](https://arxiv.org/abs/2310.18961)。本輪原生 SVG 結合既有生成金屬件；特徵與差異為教學設定，沒有新增推論。先前章節如描述應用擴充，不應解讀為原模型必需步驟。

# EfficientAD (`ad-efficientad`)

- roadmap category: `anomaly-detection`
- course pages: `04-27` through `04-30`
- research status: `complete`
- visual status: `ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/ad-efficientad.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
托盤應有三顆零件，你既要找表面污點，也要找中間漏裝，並控制檢查耗時。

### 它交出什麼，也不交出什麼
合併的異常熱圖與影像分數，交人確認污點或漏裝；不保證所有邏輯錯誤都能找到。

### 一句心智模型
EfficientAD用正常資料讓小型學生學固定教師的特徵回應；待測局部的師生差異提供一種異常線索。完整方法另用autoencoder重建教師特徵，與學生另一輸出比較，補上整體關係。兩路尺度經校準後合併；autoencoder重建的是特徵，不是把缺件照片修成正常照片。

**限制：** 同一片沒有刮傷的金屬板，換成斜照後出現亮帶，也可能被標成可疑。分數反映與既有正常的差異，不直接證明工件損壞。

### 換一個現場再推理
產線同時要查表面污點與漏裝。完整EfficientAD候選的兩類驗證尚未齊全；另一方案是局部檢查加獨立的裝配規則。

**問題：** 先補完整方法的兩類測試，或把表面與裝配分開？如何比較兩方案？

**核對：** 若希望共用一套異常流程，先補正常變化、污點、漏裝與錯位資料，檢查兩路校準。若裝配幾何固定且規則可清楚驗證，分開檢查也合理，但要計入兩套流程的誤報、漏檢、延遲和維護。不能拿污點通過的證據代替漏裝驗證。
<!-- topic-learning-bridge:end -->
## Model identity

EfficientAD is a normal-only visual anomaly-detection method designed around a lightweight Patch Description Network (PDN).  Its local path compares a frozen PDN teacher with a trainable PDN student, while a compact autoencoder branch adds global-context evidence.  It is neither a generic autoencoder nor a supervised defect segmenter.  The well-known millisecond claim is a paper measurement under a specific model variant, input, runtime, and hardware; it is not a camera-to-PLC latency promise.

## Architecture path

### Build

Clean nominal ROI -> versioned resize / crop / normalization -> frozen, pretrained PDN teacher -> teacher feature map.  Train the PDN student on the nominal support to predict that teacher map.  Couple the student with the global autoencoder branch and retain the exact teacher / student / autoencoder weights, source of the hard-feature or penalty examples, seeds, transforms, image size, and selected checkpoint.

The paper trains a lightweight feature extractor by distilling a larger pretrained network, then trains the student on normal images.  Its additional loss limits the student from imitating the teacher outside the normal-support distribution.  A practical implementation must version the external/penalty-data provenance as well as the normal support; it cannot silently substitute an arbitrary public-image corpus.

### Inference

Test ROI -> frozen PDN teacher map and student map -> local discrepancy map; in parallel, test ROI -> global autoencoder -> autoencoder/student discrepancy map -> calibration / normalization fixed from valid normal data -> locked local/global fusion -> anomaly map and image aggregation -> threshold -> PASS / REVIEW / HOLD.

The local path is intended to retain fine anomaly evidence.  The global branch is intended to expose incompatible arrangements of otherwise locally normal features.  Map calibration, fusion, image-score aggregation, threshold, and decision unit are all part of the deployed model contract.

## Representation and score

- Normality representation: the normal-fit PDN student plus the global autoencoder, under a fixed frozen PDN teacher, image recipe, and calibration state.
- Local evidence: teacher/student feature discrepancy on the ROI grid.
- Global evidence: the discrepancy involving the autoencoder-produced global representation and the student feature path.
- Final heatmap: a versioned fusion of calibrated local and global maps; visualisation normalization is not evidence by itself.
- Image score: the locked map-to-image aggregation and threshold policy.  It is an operating signal, not a defect probability.

## Cost and operating contract

Version together:

- EfficientAD-S or EfficientAD-M variant; PDN teacher architecture, source distillation recipe, checkpoint hash, and frozen-state audit;
- student and global-AE architecture, seed, optimizer, schedule, checkpoint, and external penalty / hard-feature data provenance;
- normal-fit IDs, split, contamination audit, normal-mode / lot / view coverage, and validation set used for calibration;
- ROI, registration, input resolution, crop / padding policy, colour conversion, transforms, and any internal normalization;
- teacher statistics, local and global map calibration, fusion weights / rule, image aggregation, threshold revision, and decision unit;
- pre-processing, forward, post-processing, tile aggregation, end-to-end P50 / P95 / P99 latency, VRAM / RAM, state size, precision / export engine, and exact hardware;
- local-only, global-only, and fused ablations; low-FPR escape, false reject / review load, localization, seed spread, and future / drift results.

## Failure boundary

- Contaminated normal support teaches the student and autoencoder that a defect or wrong assembly is normal.
- A teacher distilled on an unsuitable image distribution or a PDN / ROI mismatch can erase useful micro-defect evidence.
- Input resolution, PDN stride, crop, padding, registration, and illumination changes can dilute or relocate small anomalies.
- The local path may miss an invalid global arrangement when each local patch appears normal; the global branch can conversely miss small local defects.
- The external penalty / hard-feature distribution and its preprocessing change the student's out-of-support boundary; unversioned substitutions invalidate a comparison.
- Map quantiles, calibration, fusion, aggregation, and threshold can create a good-looking heatmap while changing low-FPR decision behaviour.
- Deployment latency can be dominated by acquisition, transfer, ROI, preprocessing, tiling, calibration, and post-processing even when model forward time is low.
- New product, lot, view, illumination, or assembly modes require drift review and may require recalibration or a rebuild.

## Selection gate

Consider EfficientAD when latency and state size are hard constraints, nominal support is clean and representative, local and global anomaly paths are both relevant, and the complete image-to-decision latency can be measured on the intended hardware.  Hold or compare alternatives when support is contaminated, the critical defect is below the effective pixel / stride budget, global context is unimportant, map calibration is not governed, or the claimed runtime excludes the actual deployment path.

Compare EfficientAD with STFPM and RD4AD under the same nominal-fit / challenge / future split, ROI / mask / registration, effective pixels, input resolution, teacher capacity, normalisation, calibration, threshold policy, hardware, and decision unit.  Report local-only / global-only / fused results, low-FPR escape, false reject / review load, local / global localization, end-to-end P95 / P99, state size, contamination sensitivity, external-penalty provenance, and drift rebuild behaviour—not only public AUROC.

## Visual primitives

- `input_roi`: clean nominal support, test ROI, tiny local defect, wrong global arrangement, contamination, registration, illumination, view, and lot shifts.
- `teacher_path`: frozen distilled PDN teacher and its feature map.
- `student_path`: trainable PDN student, normal-fit path, and hard-feature / external-penalty boundary.
- `global_path`: compact global autoencoder branch and its global-context anomaly evidence.
- `score_map`: local and global discrepancy maps, normal-data calibration, locked fusion, map-to-image aggregation, and threshold gate.
- `selection_gate`: local/global ablation, end-to-end P95/P99, low-FPR, calibration, contamination, effective-pixel, and drift evidence.

## Evidence bundle

Keep PDN variant, teacher-source/distillation recipe, teacher / student / AE definitions and checkpoint hashes; normal-fit IDs and contamination audit; external-penalty / hard-feature data provenance; ROI / registration / input / transform / padding contract; feature statistics and map-calibration quantiles; local, global, and fused maps; fusion / aggregation / threshold revisions; local-only / global-only / fused ablations; low-FPR escape; false-reject / review load; localization; pre / forward / post / end-to-end P50/P95/P99; memory / state size; failure images; and a drift rebuild trigger.

## Sources

- Batzner, Heckler, and Koenig, "EfficientAD: Accurate Visual Anomaly Detection at Millisecond-Level Latencies," WACV 2024 / arXiv:2303.14535.
- Anomalib EfficientAd reference implementation: https://github.com/open-edge-platform/anomalib/tree/main/src/anomalib/models/image/efficient_ad
- Course source: `full-model-course/04-anomaly-detection.md`, pages 04-27 through 04-30.

## Production gate

Research contract and visual primitives are complete. Pages 04-27 through 04-30 may proceed to white high-density C / D visual production and model-local QA.

## F01 模型中心思想與來源核對

現場既要找到小瑕疵，也要跟上節拍。EfficientAD用輕量局部描述器與學生比較，再加上觀察整體關係的重建路徑，減少特徵計算負擔。

**輕量局部路徑**：小型 patch descriptor 教師與學生處理局部特徵；正常訓練和限制泛化的損失使陌生處可能留下落差。

**補整體關係**：Autoencoder 用較全局的資訊重建教師特徵；學生另一組輸出與它比較，補局部方法較弱的結構異常線索。

**校正後融合**：局部教師學生差與全局重建差先按正常驗證資料校正再結合；快來自特徵及模型設計，實際節拍仍需含前後處理測量。

**移除設計自測**：只留下局部教師學生路徑，完整而放錯位置的部件為何可能漏掉？

局部外觀可能仍像正常零件，單看局部缺少關係證據。全局重建路徑用來補這個盲點，但並不保證識別所有組裝邏輯。

**選型**：已有正常訓練資料且節拍緊可列候選；和建庫方法一起測輸入到覆核的時間、誤報及漏檢，不直接搬用論文毫秒數。

[原論文／官方來源](https://arxiv.org/abs/2303.14535)。本輪原生 SVG 結合既有生成金屬件；特徵與差異為教學設定，沒有新增推論。先前章節如描述應用擴充，不應解讀為原模型必需步驟。


<!-- wi030-model-core:start -->
## WI-030 核心做法與工作取捨

EfficientAD用正常資料讓小型學生學固定教師的特徵回應；待測局部的師生差異提供一種異常線索。完整方法另用autoencoder重建教師特徵，與學生另一輸出比較，補上整體關係。兩路尺度經校準後合併；autoencoder重建的是特徵，不是把缺件照片修成正常照片。

同一片沒有刮傷的金屬板，換成斜照後出現亮帶，也可能被標成可疑。分數反映與既有正常的差異，不直接證明工件損壞。

PatchCore保存CNN代表局部供查找；PaDiM估計每個位置的正常分布；AnomalyDINO用DINOv2特徵建立參考；EfficientAD用正常資料學教師／學生與全域特徵關係。先固定取像與缺陷需求，再比錯誤與完整成本。

需要正常訓練與驗證資料，保存教師、學生、autoencoder、前處理和校準版本。換產品評估重新訓練與校準；不要用論文的毫秒數替代現場量測。

先收齊正常托盤的允收變化，獨立保留污點、漏裝與正常樣本；與簡單占位／外觀基準比較。

保存真實原圖、版本、正常資料切分、熱圖與覆核結果；同批獨立正常／缺陷樣本分開計誤報、漏檢，並量包含取像、前處理、模型與交接的耗時及記憶體。圖中熱區不是模型推論。

來源：https://arxiv.org/abs/2303.14535

版本及示意界線見工作項目 sources.md。使用者成品核准pending。
<!-- wi030-model-core:end -->

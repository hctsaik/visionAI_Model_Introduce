# Autoencoder family (`ad-ae`)

- roadmap category: `anomaly-detection`
- course pages: `04-31` through `04-34`
- research status: `complete`
- visual status: `ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/ad-ae.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
固定相機檢查兩孔金屬板，先用允收正常影像學重建，再查看新板的刮傷 p 是否留下差異。

### 它交出什麼，也不交出什麼
原始影像、重建估計與差異圖；用來找值得回看的位置，不直接提供缺陷機率、精密邊界、尺寸或合格判定。

### 一句心智模型
AE 先用正常影像練習壓縮與還原；待測時比較原圖與生成的重建估計。不能被重建的差異是可疑線索，重建圖不是正常真值。

**限制：** 刮傷也被複製時，p 差異變小而可能漏檢；正常小孔被模糊時，q 差異變大而可能誤報。重建誤差小不等於異常檢測品質好。

### 換一個現場再推理
另一條產線希望輸出每條刮傷的實際寬度，而非可疑位置。

**問題：** AE 差異圖能直接滿足需求嗎？還需要哪種量測流程與驗證？

**核對：** 不能直接把熱區當精確輪廓。需要足夠影像解析度、穩定取像、幾何與像素尺度校正、可信邊界及獨立量測真值；AE 可提供候選位置，再交給適合的分割與量測流程。
<!-- topic-learning-bridge:end -->
## Model identity

`AE` is a reconstruction-method family, not one fixed anomaly detector.  Before it is shortlisted, the implementation must state whether it reconstructs pixels or extracted features, and lock the encoder, decoder, latent capacity, reconstruction loss, residual definition, aggregation, and threshold.  A normal-only AE makes the reconstruction residual an anomaly candidate; it does not prove a defect probability or guarantee that every anomaly will reconstruct poorly.

## Architecture path

### Build

Clean nominal ROI -> versioned registration / resize / colour / normalization / augmentation -> encoder -> latent state `z` -> decoder -> reconstructed target (`x_hat` for image AE, or `F_hat` for feature AE) -> locked reconstruction loss -> versioned checkpoint.

For an image AE, the target is the input image and the primary residual is a pixel-space difference.  For a feature AE, a fixed feature extractor and selected feature tensors are part of the target contract.  The family must not mix an image residual, a feature residual, and a perceptual loss in a chart without naming the exact recipe.

### Inference

Test ROI -> same preprocessing -> encoder -> latent `z` -> decoder -> reconstruction -> residual map (`|x - x_hat|`, a versioned structural / perceptual difference, or a feature difference) -> optional locked mask / smoothing / resize -> map aggregation -> image score -> threshold -> PASS / REVIEW / HOLD.

Normality is represented by the trained compression-and-reconstruction path under a specific normal-fit and transform recipe.  The residual should be reviewed with the input and reconstruction; a bright residual alone is not a root cause.

## Representation and score

- Normality representation: the encoder / latent / decoder weights and the exact input or feature target, trained on a controlled normal support.
- Local evidence: a residual map between the observed and reconstructed image or feature target.
- Image score: a versioned residual aggregation, such as a maximum, quantile, or ROI summary, with any mask / smoothing explicitly fixed.
- Decision evidence: residual, reconstruction-quality diagnostics, threshold revision, and failure images under the deployed decision unit.
- The residual is a reconstruction mismatch, not a calibrated defect probability.

## Cost and operating contract

Version together:

- image AE or feature AE scope; encoder / decoder architecture, latent dimensions, skip connections, seed, checkpoint, and training precision;
- for feature AE: feature extractor, checkpoint, selected levels / shapes, frozen-state audit, and feature normalization;
- normal-fit IDs, split, contamination audit, normal-mode / lot / view / illumination coverage, and validation partition;
- ROI, registration, input size, crop / padding, colour conversion, transforms, augmentation, and masks;
- target definition; L1, L2, SSIM, perceptual, or feature-loss recipe and weights; optimizer, schedule, epochs, and checkpoint selection;
- residual definition, map resize / smoothing / mask, aggregation, threshold / calibration revision, and decision unit;
- training time, pre / forward / post and end-to-end P50 / P95 / P99, VRAM / RAM, state size, seed spread, low-FPR escape, false reject / review load, and drift results.

## Failure boundary

- An AE with high capacity, skip paths, or an overly permissive loss can reconstruct an anomaly and suppress its residual.
- A bottleneck that is too restrictive, blurry decoder, or unsuitable perceptual loss can erase normal microstructure and create false rejects.
- Residuals can be dominated by illumination, registration, focus, texture, background, crop, compression, or colour shift rather than the critical defect.
- Normal-support contamination or under-covered normal modes teaches the reconstruction path that unwanted variation is normal.
- Pixel residuals can miss semantically incorrect but visually similar assemblies; feature residuals can lose fine defects below their effective stride.
- Map smoothing, masks, aggregation, calibration, and threshold can hide a local failure or change low-FPR behaviour.
- A reconstruction baseline needs new evidence when product, lot, recipe, camera, or environment drift changes.

## Selection gate

Use an AE first as an interpretable reconstruction-residual baseline when clean normal support is available, the target / loss / latent can be fixed, and engineering can inspect input, reconstruction, and residual together.  Hold or compare alternatives when required micro-defect resolution is below the AE budget, anomalies may reconstruct well, global logical anomalies matter, illumination or registration is uncontrolled, or low-FPR performance is not demonstrated.

Compare AE with DRAEM and UniAD under identical normal-fit / challenge / future splits, ROI / mask / registration, effective pixels, input, augmentation, loss target, residual aggregation, threshold policy, hardware, and decision unit.  Report low-FPR escape, false reject / review load, local / global localization, reconstruction quality, anomaly-reconstruction failures, end-to-end P95/P99, state size, and drift rebuild—not only AUROC.

## Visual primitives

- `input_roi`: clean normal support, test ROI, contamination, normal variation, registration / illumination shift, tiny defect, and global logical anomaly.
- `encoder_decoder_path`: image or feature target flows through encoder -> latent `z` -> decoder -> reconstruction.
- `normality_representation`: locked normal-fit data, target type, latent capacity, loss, and checkpoint.
- `score_map`: input / reconstruction comparison, residual image or feature map, mask / resize / smoothing, aggregation, and threshold.
- `evidence_review`: input, reconstruction, residual, false-reject, escaped anomaly, and low-FPR comparison evidence.
- `selection_gate`: capacity, blur, anomaly reconstruction, effective pixels, illumination / registration, global context, runtime, and drift evidence.

## Evidence bundle

Keep model-family scope; encoder / decoder / latent configuration and checkpoint hash; target type and loss recipe; normal-fit IDs and contamination audit; ROI / registration / transform / input contract; image or feature-extractor state; training curves and seed spread; input / reconstruction / residual triplets; residual aggregation / calibration / threshold revisions; low-FPR escape; false reject / review load; local / global localization; pre / forward / post / end-to-end latency; memory / state size; failure images; and a drift rebuild trigger.

## Sources

- Baur et al., "Semi-supervised Anomaly Detection using AutoEncoders," arXiv:2001.03674.
- Anomalib Feature Reconstruction Error reference: https://anomalib.readthedocs.io/en/v2.0.0/markdown/guides/reference/models/image/fre.html
- Course source: `full-model-course/04-anomaly-detection.md`, pages 04-31 through 04-34.

## Production gate

The family contract and visual primitives are complete.  Pages 04-31 through 04-34 may proceed to white high-density C / D visual production and model-local QA.

## F01 模型中心思想與來源核對

沒有各式缺陷標籤，想先學合格外觀。自編碼器把影像壓縮再重建，只練正常品時，不能還原的局部可能留下可疑差異。

**先限定重建目標**：本圖用 image-AE：输入像素和重建像素比較；feature-AE 則重建特徵，兩者不可混叫同一張殘差。

**瓶頸限制直接照抄**：encoder 壓縮，decoder 還原，正常訓練希望保住允收外觀；限制太強會連正常細節也丟失。

**殘差只是線索**：原圖減重建得到差異；若模型連刮傷也複製成功，差異反而小，所以重建品質不是偵測品質。

**移除設計自測**：拿掉容量限制，讓輸出直接等於輸入，異常分數會怎樣？

像素殘差會變成零，包括刮傷也沒有線索。相反地，過小瓶頸會令合格細節也重建不出來，造成誤報。

**選型**：可作容易理解的正常重建基準；若需要學習判讀原圖與重建的差，另比較 DRAEM。換產品要重訓或至少重新驗證。

[原論文／官方來源](https://arxiv.org/abs/1807.02011)。本輪原生 SVG 結合既有生成金屬件；特徵與差異為教學設定，沒有新增推論。先前章節如描述應用擴充，不應解讀為原模型必需步驟。

<!-- wi033-engineering:start -->
## WI-033 工程圖修正

### AE：用正常影像學壓縮與還原

正常訓練影像作為AE重建目標；測試原圖與重建估計同位置比較。保留40/150/110原算例，位置差異供原圖覆核；原圖不能在推論時被重建結果取代作真值。

重建提供對照，差異大小還須驗證。

來源：https://arxiv.org/html/2103.04257v3

### AE：同位置40與150，差值110

本課為影像自編碼器基線：正常圖訓練壓縮與重建，推論原圖與重建同位置取差。沿用首讀原圖p灰階40、重建150、絕對差110的作者算例；AE若連刮傷一起重建可能漏檢，正常小孔模糊也會誤報。這裡的絕對像素差是明確選定基線，不概括所有AE評分。

比較原圖與重建估計，重建不是正常真值。

來源：https://arxiv.org/html/2103.04257v3

### AE：前處理與重建誤差一起固定

保存模型、輸入灰階/RGB範圍、resize/裁切、差異定義與門檻。原圖和重建需要相同座標與像素範圍；既要看刮傷是否留下差異，也要驗正常孔被模糊的誤報，不能只看平均重建損失。

同座標、同尺度，差值才可比較。

來源：https://arxiv.org/html/2103.04257v3

### AE：重建得像，也可能漏掉刮傷

同刮傷p原40若被重建成40，絕對差0仍有刮傷；正常小孔q若由30模糊成100，差70可能誤報。後者是新增明示給定反例，非實測，與原主線保持同件大小孔身份。

差值小不是合格證明，要看差異從何而來。

來源：https://arxiv.org/html/2103.04257v3

<!-- wi033-engineering:end -->

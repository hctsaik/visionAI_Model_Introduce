# DiffusionAD (`ad-diffad`)

- roadmap category: `anomaly-detection`
- course pages: `04-47` through `04-50`
- research status: `complete`
- visual status: `ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/ad-diffad.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
金屬板表面有刮傷 p，正常孔邊 q 也會反光；需要定位線索並控制誤報、漏檢與時間。

### 它交出什麼，也不交出什麼
輸出候選異常位置和分數；不是正常真值、尺寸或自動放行結果。

### 一句心智模型
正常影像學去噪，合成異常及遮罩教定位。測試時同一原圖加入兩種尺度的噪聲，高噪聲分支的正常估計 N 引導低噪聲分支估計 R；原圖 A 與 R 一起輸入分割網路產生位置圖。每個尺度用單步估計，不代表整套只呼叫一次網路。

**限制：** 恢復可能保留缺陷或改動正常外觀，需以獨立資料驗證。

### 換一個現場再推理
從霧面金屬換到鏡面金屬。

**問題：** 原有正常知識和門檻可直接沿用嗎？

**核對：** 先核對光照及允收反光，補正常涵蓋並評估重訓／適配；再用未見正常和真缺陷重驗，不能把反光熱點直接當缺陷。
<!-- topic-learning-bridge:end -->
## Model identity

This course's DiffusionAD is **"Norm-guided One-step Denoising Diffusion for Anomaly Detection"** (2023). It reforms anomaly reconstruction as noise-to-norm restoration: anomalous regions are perturbed and restored toward normal appearance, then a discriminative segmentation path compares the input with the normal-like restoration. It is not a generic multi-step diffusion reconstruction model; the one-step denoiser and norm guidance are central deployment definitions.

## Architecture path

### Build

Clean nominal ROI -> fixed registration / resize / colour / normalization -> forward diffusion noise schedule -> noisy normal / anomaly-training states -> norm-guided one-step denoiser -> normal restoration target -> reconstruction objective. The input and normal-like restoration are concatenated for a discriminative segmentation sub-network that learns pixel anomaly maps.

Version the normal-fit IDs, noise schedule and timestep, norm-guidance definition / strength, one-step denoiser architecture and checkpoint, reconstruction and segmentation losses, image recipe, any anomalous or synthetic supervision used by the configured implementation, map aggregation, calibration, threshold, seed, optimizer, and checkpoint selection.

### Inference

Test ROI -> same preprocessing -> norm-guided **one-step** denoiser -> normal-like restoration `x-hat` -> concatenate test image and restoration -> segmentation head -> anomaly map -> locked smoothing / aggregation -> image score -> threshold -> PASS / REVIEW / HOLD.

One-step restoration is a normal reference for anomaly discrimination, not an aesthetic image-generation target. Record restoration, input, segmentation map, and final decision together. Do not report a conventional multi-step sampler's latency as this model's deployment P95.

## Representation and score

- Normality representation: the one-step norm-guided denoising state and segmentation state fitted to the locked normal support and image recipe.
- Local evidence: a pixel anomaly map predicted from the joint test-image / normal-restoration appearance, not a raw restoration residual alone.
- Image score: a versioned map smoothing / mask / resize / aggregation rule and threshold under the declared decision unit.
- The score is an anomaly operating signal, not a calibrated defect probability, a root-cause label, or proof that the restoration has preserved all normal texture.

## Cost and operating contract

Version together:

- DiffusionAD release / code commit, denoiser and segmentation architectures, checkpoint hashes, noise schedule, timestep, norm guidance, precision, optimizer, schedule, seeds, and reconstruction / segmentation loss weights;
- normal-fit IDs, split, contamination audit, normal-mode / lot / view / illumination coverage, and normal validation used for calibration;
- ROI, registration, input resolution, crop / padding, colour conversion, transforms, normalisation, synthetic/real anomaly supervision policy, and any augmentation order;
- restoration definition, joint segmentation input, map smoothing / resize / masking, image aggregation, calibration / threshold revision, and decision unit;
- restoration-quality review, restoration-caused false reject, defect-erasure escape, low-FPR, false reject / review load, local/global localization, real challenge and future/drift results;
- training cost and one-step pre / denoiser / segmentation / post / complete image-to-decision P50/P95/P99, VRAM/RAM, state size, batch policy, and hardware.

## Failure boundary

- A noise schedule, timestep, or guidance setting can restore anomalies poorly, preserve them, remove a normal microstructure, or introduce texture artefacts; output beauty is not an acceptance metric.
- Normal-support contamination or under-covered normal modes teaches the restoration path that unwanted variation is normal.
- Input resolution, ROI, registration, illumination, focus, colour, compression, crop, and background changes can dominate restoration or segmentation difference and create false rejects.
- The segmentation head can overfit configured synthetic anomalies or restoration artefacts rather than real production failures; evaluate a real holdout and error taxonomy.
- A one-step model must not be compared through multi-step sampler quality or latency. Conversely, a one-step forward number alone still omits acquisition, preprocessing, transfer, aggregation, and hand-off.
- Map smoothing, aggregation, calibration, and threshold can hide a small anomaly or change low-FPR behavior even when a restoration-map triplet looks plausible.
- Global logical anomalies may remain hard when locally restored regions look normal.

## Selection gate

Consider DiffusionAD when an engineering team specifically wants to validate a normal-restoration plus discriminative-segmentation path and can govern its noise schedule, norm guidance, one-step state, and real restoration evidence. Use real challenge / future splits to measure defect erasure, restoration-induced false reject, low-FPR, review load, and complete P95.

Hold or compare alternatives when normal support is unstable, restoration bias is unexplained, critical defects are below effective pixels, synthetic/real segmentation behavior is unverified, global logic dominates, or only multi-step diffusion numbers are available. Compare with DDAD and InvAD under the same support, ROI, effective pixels, input recipe, threshold policy, hardware, decision unit, real escapes, P95, and error taxonomy.

## Visual primitives

- `normal_diffusion_recipe`: clean normal support, forward noise schedule / timestep, norm guidance, one-step denoiser, and normal-like restoration.
- `joint_segmentation_path`: input plus restoration -> discriminative segmentation head -> anomaly map -> aggregation -> decision.
- `one_step_contract`: pinned one-step versus prohibited multi-step latency substitution, denoiser / segmentation state, and input recipe.
- `evidence_review`: input / restoration / map triplet, defect erasure, restoration artefact, low-FPR, false reject / review load, real holdout, P95/P99, and drift.
- `selection_gate`: normal stability, restoration bias, synthetic-to-real behavior, effective pixels, global logic, and calibration / rebuild trigger.

## Evidence bundle

Keep normal IDs and contamination audit; noise schedule / timestep / norm-guidance state; denoiser and segmentation definitions / checkpoints / losses; image recipe; input / restoration / map / decision triplets; one-step-only latency breakdown; restoration failure and escaped-defect images; synthetic-to-real evidence; low-FPR / false reject / review load / localization; map aggregation / calibration / threshold revisions; memory/state; real future/drift splits; and a rebuild trigger.

## Sources

- Zhang et al., "DiffusionAD: Norm-guided One-step Denoising Diffusion for Anomaly Detection," arXiv:2303.08730.
- Course source: `full-model-course/04-anomaly-detection.md`, pages 04-47 through 04-50.

## Production gate

Research contract and visual primitives are complete. Pages 04-47 through 04-50 may proceed to white high-density C / D visual production and model-local QA.

## F01 模型中心思想與來源核對

傳統重建可能留下異常，多步擴散又太慢。DiffusionAD讓加噪後的輸入朝正常外觀去噪，採一步去噪設計，再由分割網路判讀原圖與重建。

**加噪削弱異常訊號**：重建子網路學習從帶噪影像復原正常外觀；加噪也可能破壞正常細節，需用訓練與驗證控制。

**Norm-guided 一步去噪**：以不同噪聲尺度的引導改善正常復原，避免長鏈反覆採樣；一步不代表整個系統只有一次網路計算。

**學習式位置判讀**：分割子網路聯合看原圖和復原圖，預測局部異常分數；不是只取兩張圖的絕對相減。

**移除設計自測**：一步去噪變快，但復原圖仍保留刮傷，能直接宣稱改善嗎？

不能；重建未提供可靠正常對照，位置判讀可能漏檢。應同時比較正常細節保留、異常定位與含分割網路的整體耗時。

**選型**：能訓練且想降低擴散推論成本可試；與 DDAD 比一步／條件採樣和學習式分割／殘差融合，不從名称判速度勝負。

[原論文／官方來源](https://arxiv.org/abs/2303.08730)。本輪原生 SVG 結合既有生成金屬件；特徵與差異為教學設定，沒有新增推論。先前章節如描述應用擴充，不應解讀為原模型必需步驟。

<!-- wi033-engineering:start -->
## WI-033 工程圖修正

### DiffusionAD：去噪與定位要分別學

正常圖用於學習噪聲估計及恢復；合成異常與已知遮罩提供分割監督。兩個網路不能只用一張異常熱圖概括。合成資料仍需覆盖任務變化，最後以未見正常與真缺陷驗證。

正常資料教恢復，合成異常和遮罩教定位。

來源：https://github.com/HuiZhang0812/DiffusionAD

### DiffusionAD：恢復與定位分兩個工作

同一原圖A加入高低噪聲；高噪聲正常估計N引導低噪聲恢復R。各尺度用單步估計，不是整套只呼叫一次網路；A和R一起進學習的分割網路，不是直接拿R當最終檢測答案。

原圖與恢復圖一起進分割，最後才交出異常位置。

來源：https://github.com/HuiZhang0812/DiffusionAD

### DiffusionAD：要交付最後的位置結果

保存原圖A、恢復R與分割位置圖能追查恢復或定位失敗。位置圖須映回原始影像座標，配合域內門檻及覆核；延遲包含兩尺度估計、分割和前後處理，不能由單步估計直接宣稱整套最快。

保存 A／R／位置圖，連同完整耗時一起驗收。

來源：https://github.com/HuiZhang0812/DiffusionAD

### DiffusionAD：恢復變乾淨不等於漏檢

固定同一刮痕影像，比較恢復是否去除異常及最後分割是否找到位置。去掉異常本來就是恢復子任務的方向，不直接等於漏檢；缺陷留在R也不必然漏，但會改變可用線索。兩條示意結果需以真實留出集驗證。

檢查最後位置圖，分清恢復成功與定位失敗。

來源：https://github.com/HuiZhang0812/DiffusionAD

<!-- wi033-engineering:end -->

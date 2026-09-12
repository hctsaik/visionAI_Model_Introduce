# RD4AD (`ad-rd4ad`)

- roadmap category: `anomaly-detection`
- course pages: `04-23` through `04-26`
- research status: `complete`
- visual status: `ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/ad-rd4ad.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
固定相機檢查兩孔金屬板，想從正常資料學出可疑位置。必須理解刮傷 p 的特徵為何可能對不上，也要看正常孔邊 q 的誤報。

### 它交出什麼，也不交出什麼
多尺度特徵差異形成異常圖與候選分數；可協助定位覆核，不直接交付缺陷類型、精確輪廓、尺寸或放行結論。

### 一句心智模型
固定教師把影像轉成多尺度特徵；可訓練瓶頸與反向解碼器用正常資料學重建這些特徵。比較同位置特徵差異，再回到原圖。

**限制：** 細缺陷在兩份特徵中仍可能相似；正常光澤也可能造成差異。正常訓練對齊不保證異常檢測成功。

### 換一個現場再推理
另一條線要找孔位配置或裝配關係錯誤，而不只是表面刮傷。

**問題：** 局部特徵差異足以代表完整裝配關係嗎？如何驗證？

**核對：** 不能保證。補具代表性的錯裝與正常變化樣本，檢查整體關係是否可分；必要時加入物件、關鍵點或幾何關係檢查。仍可測 RD4AD 作候選，但不能把表面刮傷結果直接推廣到裝配判定。
<!-- topic-learning-bridge:end -->
## Model identity

RD4AD (Anomaly Detection via Reverse Distillation from One-Class Embedding) is a normal-only feature-reconstruction method. A frozen pretrained encoder is the teacher. A trainable one-class bottleneck embedding module and reverse decoder reconstruct the teacher's multi-scale features in the opposite direction. Anomaly evidence is the mismatch between teacher features and the reconstructed features; this is not a pixel autoencoder, memory bank, or supervised defect segmenter.

## Architecture path

### Build

Clean nominal ROI -> versioned resize / normalization / augmentation -> frozen pretrained encoder (official implementation: WideResNet50-2) -> multi-scale teacher features -> trainable one-class bottleneck embedding -> reverse decoder -> reconstructed multi-scale features -> cosine reconstruction loss over corresponding teacher / decoder levels -> versioned bottleneck and decoder checkpoint.

The official implementation freezes the encoder in evaluation mode and optimizes the bottleneck plus decoder. Its training objective sums `mean(1 - cosine(flatten(teacher_l), flatten(decoder_l)))` across feature levels.

### Inference

Test ROI -> frozen teacher features -> one-class bottleneck -> reverse decoder -> reconstructed feature pyramid -> per-location cosine discrepancy `D_l = 1 - cosine(F_teacher_l, F_decoder_l)` -> bilinear upsample each map to the image grid -> locked multi-level fusion (official evaluation path: addition) -> optional locked Gaussian smoothing (official evaluation uses sigma 4) -> image aggregation (official evaluation: maximum map value) -> threshold -> PASS / REVIEW / HOLD.

## Representation and score

- Normality representation: the trained one-class bottleneck and reverse decoder, conditioned on a fixed frozen teacher and feature recipe.
- Local anomaly evidence: per-location cosine discrepancy between each frozen teacher feature map and its reverse-decoder reconstruction.
- Final heatmap: resized multi-level discrepancy maps fused by the versioned aggregation rule.
- Image score: a locked map-to-image aggregation; the official evaluation uses the map maximum.
- The score is evidence under a particular recipe, not a calibrated defect probability.

## Cost and operating contract

Version together:

- exact teacher architecture, pretrained checkpoint, and frozen-state audit;
- bottleneck / decoder architecture, initialization, seed, and checkpoint;
- selected feature levels and tensor shapes;
- normal-fit IDs, split, contamination audit, and view / lot coverage;
- ROI, mask, registration, input size, normalization, and augmentation;
- cosine loss definition, level weights, optimizer, schedule, epochs, and checkpoint selection;
- discrepancy definition, resize alignment, fusion, smoothing, mask, and image aggregation;
- threshold / calibration revision, decision unit, precision / export engine, and hardware;
- training time, P95 latency, VRAM / RAM, state size, and seed spread.

## Failure boundary

- Normal-support contamination teaches the bottleneck / decoder to reconstruct anomalous patterns.
- Teacher pretraining or domain mismatch weakens useful feature evidence.
- A bottleneck that is too restrictive discards legitimate normal micro-features and raises false rejects.
- A decoder that reconstructs too broadly may also reconstruct anomalies and reduce separation.
- Multimodal normal variation not covered by the normal-fit split produces unstable discrepancy.
- Tiny defects can be diluted by feature stride, receptive field, resize, and Gaussian smoothing.
- ROI, background, registration, illumination, view, recipe, or lot shift can dominate the heatmap.
- Fusion, smoothing, and max aggregation can be noise-sensitive and must be qualified at low FPR.

## Selection gate

Consider RD4AD when clean normal-only data are available, a frozen teacher has adequate domain fit, and a compact one-class bottleneck plus reverse decoder can preserve relevant normal structure while rejecting abnormal structure. Hold or compare alternatives when support is contaminated, domain mismatch is high, tiny-defect recall is critical, normal modes are poorly covered, or runtime / training cost is too high.

Compare RD4AD with STFPM and EfficientAD under the same normal-fit / challenge / future split, ROI / mask / registration, effective pixels, input resolution, teacher / backbone capacity, selected layers, augmentation, map postprocess / fusion / aggregation, hardware, decision unit, and threshold policy. Report low-FPR escape, false reject / review load, local / global localization, training time, P95 / VRAM / RAM, state size, seed spread, contamination sensitivity, teacher mismatch, and drift rebuild behavior—not only public AUROC.

## Visual primitives

- `input_roi`: clean normal support, test ROI, contamination, view / illumination / registration shifts, tiny and global anomalies.
- `teacher_path`: frozen encoder and multi-scale teacher feature pyramid.
- `normal_state`: one-class bottleneck plus reverse-decoder checkpoint.
- `reverse_path`: compact embedding flows into a decoder that reconstructs features in reverse scale order.
- `score_map`: corresponding teacher / decoder cosine discrepancy maps, resize, addition, smoothing, and max score.
- `selection_gate`: compression, overgeneralization, domain, contamination, tiny-defect, runtime, low-FPR, and drift evidence.

## Evidence bundle

Keep teacher checkpoint / frozen audit, bottleneck and decoder definition / checkpoint, normal-fit IDs and contamination audit, transforms and ROI policy, feature levels / shapes, training loss and curves, optimizer / schedule / seed spread, per-level discrepancy maps, resize / fusion / smoothing / aggregation recipe, threshold revision, challenge / future / drift results, low-FPR escape, review load, localization, runtime / memory, failure images, and rebuild trigger.

## Sources

- Deng and Li, "Anomaly Detection via Reverse Distillation from One-Class Embedding," CVPR 2022 / arXiv:2201.10703.
- Official implementation: https://github.com/hq-deng/RD4AD
- Course source: `full-model-course/04-anomaly-detection.md`, pages 04-23 through 04-26.

## Production gate

Research contract and visual primitives are complete. Pages 04-23 through 04-26 may proceed to white high-density C / D visual production and model-local QA.

## F01 模型中心思想與來源核對

學生和教師走相同影像路徑時，異常也可能被一起描述得很像。RD4AD改讓學生從壓縮後的正常描述往回重建教師特徵，增加兩路反應的差異。

**教師先編碼**：固定教師把影像變成多尺度特徵；學生不直接接原始影像。

**瓶頸後反向重建**：可訓練的單類瓶頸壓縮正常資訊，學生 decoder 從高層往低層重建教師表示。

**比較重建前後**：教師特徵與重建特徵在對應位置的方向差異形成線索；重建目標是特徵，不是修復照片。

**移除設計自測**：把原圖直接餵給同架構學生，還是原來的反向蒸餾嗎？

不是；它更接近一般教師學生模仿。RD4AD 的關鍵是教師表示經瓶頸再由 decoder 還原，學生輸入與處理方向都不同。

**選型**：和 STFPM 比較正常訓練、模型容量及小缺陷反應；換產品需重新驗證正常訓練覆蓋，不能因重建逼真就判合格。

[原論文／官方來源](https://arxiv.org/abs/2201.10703)。本輪原生 SVG 結合既有生成金屬件；特徵與差異為教學設定，沒有新增推論。先前章節如描述應用擴充，不應解讀為原模型必需步驟。

<!-- wi033-engineering:start -->
## WI-033 工程圖修正

### RD4AD：正常資料教瓶頸與反向學生

教師固定，正常訓練更新單類瓶頸與反向學生。重建的是多尺度特徵，與同尺度教師表示比較形成位置線索；不是由模型修復物理工件，沒有尺寸或允收保證。

先固定教師，正常資料再訓練重建表示。

來源：https://openaccess.thecvf.com/content/CVPR2022/html/Deng_Anomaly_Detection_via_Reverse_Distillation_From_One-Class_Embedding_CVPR_2022_paper.html

### RD4AD：从瓶頸反向重建教師特徵

固定教師編碼器抽多尺度特徵，可訓練one-class瓶頸和反向學生解碼器以正常資料學重建。學生輸入是教師嵌入，不是原圖；對應尺度的教師與重建特徵以餘弦差異比較並映回位置。教師高低尺度與學生逆向重建對應清楚，不把輸出說成修復照片。

學生從教師嵌入重建，逐尺度對照教師。

來源：https://openaccess.thecvf.com/content/CVPR2022/html/Deng_Anomaly_Detection_via_Reverse_Distillation_From_One-Class_Embedding_CVPR_2022_paper.html

### RD4AD：教師、瓶頸、學生是一組

保存教師、瓶頸和學生權重及各層的配對、前處理、插值、餘弦差與彙整。避免只部署學生而沒有教師嵌入來源；域內正常光澤和小刮傷都需獨立驗。

三組權重與尺度配對固定，才能重現差異。

來源：https://openaccess.thecvf.com/content/CVPR2022/html/Deng_Anomaly_Detection_via_Reverse_Distillation_From_One-Class_Embedding_CVPR_2022_paper.html

### RD4AD與AE：重建的對象不同

在同檢查工件上，RD4AD重建特徵並比餘弦差；AE基線重建像素並在相同位置相減。像素差110和特徵差不是同一尺度的數字，不能直接比較大小判方法好壞。

特徵重建與像素重建，不能共用同一解讀。

來源：https://openaccess.thecvf.com/content/CVPR2022/html/Deng_Anomaly_Detection_via_Reverse_Distillation_From_One-Class_Embedding_CVPR_2022_paper.html

<!-- wi033-engineering:end -->

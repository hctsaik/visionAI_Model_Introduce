# PaDiM（`ad-padim`）

- roadmap 分類：`anomaly-detection`
- 講義對照：`04-07`～`04-10`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/ad-padim.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
相機和治具固定，板上孔口與平面本來就不同；你希望每個位置和自己的正常變化比較。

### 它交出什麼，也不交出什麼
每個位置的異常距離、可疑圖與影像分數，交原圖覆核；不自動辨認缺陷名稱。

### 一句心智模型
PaDiM對正常影像的每個空間位置，收集CNN局部特徵並估計多變量高斯分布。待測同位置特徵以馬氏距離對照該位置的平均與相關性：沿常見變化方向的偏移，和跨出狹窄正常範圍的偏移，意義不同。這是位置分布比較，不是找一張最像的正常片。

**限制：** 同一片沒有刮傷的金屬板，換成斜照後出現亮帶，也可能被標成可疑。分數反映與既有正常的差異，不直接證明工件損壞。 工件偏移也會讓孔口落到原本平面的位置。

### 換一個現場再推理
治具更換後板子會小幅旋轉。你可以增加對位步驟，也可以維持自由取像並比較查找式正常參考。

**問題：** 保留PaDiM加對位，或比較PatchCore／AnomalyDINO？哪種現場條件會讓你改選？

**核對：** 若幾何可穩定對位且新增耗時可接受，保留PaDiM並重估位置分布合理。若遮擋或姿態使對位不可靠，可比較查找式參考，但它們也不保證旋轉不變。用同批影像量對位失敗、誤報、漏檢與總耗時；不能把位置錯配一律當正常變化吸收。
<!-- topic-learning-bridge:end -->
## 模型定位

PaDiM（Patch Distribution Modeling）以 frozen pretrained CNN 的多層 patch embeddings，在每個對齊空間位置估計 normal multivariate Gaussian，並以 test embedding 對該位置 Gaussian 的 Mahalanobis distance 產生 anomaly map/score。它用 location-conditioned statistics 表示 normality，不是 exemplar memory bank、global embedding 或 calibrated defect probability；position alignment 與 covariance estimation 是核心前提。

## 必要欄位

### architecture_path

建 normal state：aligned nominal ROI → frozen CNN selected layers → resize/alignment＋concatenate multi-level feature maps → optional fixed dimension subset/projection → for each spatial position p collect normal embeddings z_p → estimate mean μ_p and regularized covariance Σ_p → versioned per-position Gaussian state。推論：aligned test ROI → same feature path → z_p → Mahalanobis distance sqrt((z_p−μ_p)^T Σ_p^-1 (z_p−μ_p)) → position score grid → upsample/smooth/mask → image aggregation → threshold/Gate。

### representation_or_score

Normality representation 是每個 feature-grid location 的 μ_p、Σ_p，而非全圖單一 Gaussian 或 exemplar bank。Score 是 test patch 對同一對齊位置 normal distribution 的 Mahalanobis distance；covariance conditioning/regularization與 support count直接影響距離。Upsampled map 是 encoder-grid statistical evidence，不是 native pixel mask；image score與 release probability需另行 calibration。

### cost_and_operating_point

鎖 backbone/checkpoint、feature layers、input/ROI/registration/mask、feature-map alignment、dimension subset/projection/seed、normal support IDs/count、covariance estimator/regularization/inversion、score-map upsample/smoothing、aggregation、threshold/calibration、precision/export/engine。端到端 P95包含 registration、feature extraction、per-position Mahalanobis、map postprocess/aggregation；同時治理 state size、conditioning、low-FPR escape、false reject/review load與 rebuild trigger。

### failure_boundary

Misregistration/ROI shift 會把正常 structure 移到錯誤 Gaussian position；normal multimodality/recipe/view variation不一定適合單一 Gaussian；support 太少或 feature dimension 過高會使 covariance不穩/病態。Support contamination、tiny defects低於feature-grid解析度、dimension sampling/regularization變動、background/mask shift與future drift都會改score。公開 AUROC不能代替低-FPR fab qualification。

### selection_gate

在 ROI位置高度可對齊、normal variability於各位置可由局部 Gaussian近似、可收集足夠 clean normal support，且希望以 compact statistical state取代 exemplar search時選用。與 PatchCore/SubspaceAD比較需固定 support/challenge/future split、ROI/registration/mask、effective pixels、encoder/features、dimension/state budget、map aggregation、hardware、decision unit、threshold/calibration，再比較 low-FPR escape、false reject/review load、P95/state size、conditioning與drift。

### evidence_bundle

保存 exact backbone/checkpoint/layers、input/ROI/registration/mask、normal support IDs/count/contamination audit、feature alignment、dimension subset/projection/seed、μ/Σ state checksum、covariance estimator/regularization/inversion diagnostics/condition number、map upsample/smoothing/aggregation、threshold/calibration revision、challenge/future/drift split、low-FPR escape/false reject/review load、P95/state size、failure images與 rebuild trigger。

## 視覺 primitive

- `input_roi`：aligned nominal/test ROI，含 local structure、合法 position variation、misregistration與 anomaly。
- `feature_or_patch_path`：frozen CNN multi-level maps → align/concatenate → fixed-dimensional position embeddings。
- `normality_representation`：每個 grid position 的 μ_p、Σ_p Gaussian state，顯示 support/count/conditioning。
- `score_map`：same-position Mahalanobis distance → feature grid → upsample/smooth/mask anomaly evidence。
- `aggregation`：versioned max/top-k/weighted map-to-image score＋threshold/calibration。
- `normal_state_gate`：registration、support count/contamination、covariance conditioning/regularization、low-FPR escape、drift/rebuild。

## 比較契約

- 比較 ID：`anomaly-detection-family-comparison`
- 固定條件：相同 nominal support/challenge/future split、ROI/registration/mask、effective pixels、encoder/features、dimension/state budget、score-map resolution/aggregation、hardware、decision unit、threshold/calibration policy。
- 共同比較輸出：low-FPR escape、false reject/review load、localization evidence、P95/state size、registration sensitivity、covariance conditioning、support contamination與 recipe/lot/view drift；不得以不同 alignment/support 或公開 AUROC 宣稱排名。

## 來源

- Defard et al., “PaDiM: a Patch Distribution Modeling Framework for Anomaly Detection and Localization,” arXiv:2011.08785（pretrained CNN patch embeddings、per-position multivariate Gaussian、Mahalanobis scoring）。
- `full-model-course/04-anomaly-detection.md` 的 04-07～04-10。

## 產生 gate

六個必要欄位與六個 visual primitives 已完成模型專屬遷移；可開始產生 04-07～04-10 的版本化 C/D 教學頁，逐張通過 QA 後才能 approved。

## F01 模型中心思想與來源核對

同樣的亮點，在孔邊可能正常，在平面卻可能異常。PaDiM替每個影像位置記住正常特徵的中心、變動幅度與共同變動方向。

**每個位置一份正常分布**：正常影像經固定 CNN 抽取並組合多層特徵；每個網格位置各自估計均值與共變異數。

**考慮變動方向**：Mahalanobis 距離會考慮正常分布的寬窄；常見方向的變動與罕見方向的變動，不因像素距離相等就同分。

**回到同一位置**：待測位置和該位置的分布比較，再組成位置圖。對位漂移會改變比較對象，需另外驗證。

**移除設計自測**：把每個位置的分布混成全圖一份，會失去什麼？

會失去位置條件：正常孔邊與平面可能互相掩護。這不是原本的 PaDiM；若工件漂移，先驗證對位或採較不依賴位置的候選方法。

**選型**：固定視角且對位可靠時適合起步；換產品重估分布。維度、位置數影響儲存與估計穩定性，不能只看正常樣本數。

[原論文／官方來源](https://arxiv.org/abs/2011.08785)。本輪原生 SVG 結合既有生成金屬件；特徵與差異為教學設定，沒有新增推論。先前章節如描述應用擴充，不應解讀為原模型必需步驟。


<!-- wi030-model-core:start -->
## WI-030 核心做法與工作取捨

PaDiM對正常影像的每個空間位置，收集CNN局部特徵並估計多變量高斯分布。待測同位置特徵以馬氏距離對照該位置的平均與相關性：沿常見變化方向的偏移，和跨出狹窄正常範圍的偏移，意義不同。這是位置分布比較，不是找一張最像的正常片。

同一片沒有刮傷的金屬板，換成斜照後出現亮帶，也可能被標成可疑。分數反映與既有正常的差異，不直接證明工件損壞。 工件偏移也會讓孔口落到原本平面的位置。

PatchCore保存CNN代表局部供查找；PaDiM估計每個位置的正常分布；AnomalyDINO用DINOv2特徵建立參考；EfficientAD用正常資料學教師／學生與全域特徵關係。先固定取像與缺陷需求，再比錯誤與完整成本。

正常資料需涵蓋各位置的允收變化；更換視角、尺寸或對位後需重估位置分布。比較特徵維度、位置數的儲存與計算成本。

先測治具與對位是否讓相同位置對得上，再收正常批次，分開估計和驗證資料。

保存真實原圖、版本、正常資料切分、熱圖與覆核結果；同批獨立正常／缺陷樣本分開計誤報、漏檢，並量包含取像、前處理、模型與交接的耗時及記憶體。圖中熱區不是模型推論。

來源：https://arxiv.org/abs/2011.08785

版本及示意界線見工作項目 sources.md。使用者成品核准pending。
<!-- wi030-model-core:end -->

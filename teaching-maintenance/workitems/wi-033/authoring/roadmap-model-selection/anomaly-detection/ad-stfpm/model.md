# STFPM（`ad-stfpm`）

- roadmap 分類：`anomaly-detection`
- 講義對照：`04-19`～`04-22`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/ad-stfpm.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
固定相機看兩孔金屬板，想找刮傷 p，但也怕正常孔邊 q 的光澤造成誤報。用同一影像走教師與學生，檢查多尺度反應差異。

### 它交出什麼，也不交出什麼
多尺度特徵差異整合成可疑位置圖與候選分數，不直接提供缺陷名稱、精密輪廓、尺寸或自動放行。

### 一句心智模型
兩路採同架構並讀同一影像。學生模仿正常影像的教師特徵；陌生局部可能產生兩路差異，整合後指向可疑位置。

**限制：** 缺陷也可能被兩路表示得相近，正常變化也可能有差異；需以未見正常與真缺陷驗證。

### 換一個現場再推理
下游希望得到裂縫的實際寬度與允收判定。

**問題：** 教師學生差異圖是否足夠？

**核對：** 不足。熱區只提供可疑位置，需要穩定取像、足夠解析度、幾何與像素尺度校正、可驗證的邊界或分割及量測真值；不能把特徵差異範圍直接當毫米寬度。
<!-- topic-learning-bridge:end -->
## 模型定位

STFPM（Student-Teacher Feature Pyramid Matching）以 frozen pretrained teacher 與相同架構、只用 anomaly-free data 訓練的 student 建立 normality：student 在多層 feature pyramid 學會模仿 teacher 的 normal features，推論時 teacher/student 在各位置的 normalized feature discrepancy 形成 anomaly evidence。它不是 exemplar retrieval、image reconstruction或 supervised defect segmentation；teacher domain、normal-fit cleanliness、layer/fusion recipe與 student training stability決定可見的 normality。

## 必要欄位

### architecture_path

建 normal model：clean nominal ROI → versioned resize/augmentation/mask → frozen pretrained teacher（原論文為 ImageNet ResNet-18）＋same-architecture randomly initialized student → select feature pyramid layers → per-position L2-normalize teacher/student feature vectors → minimize layerwise squared L2 matching loss over normal images → versioned student checkpoint。推論：test ROI → teacher＋student dual forward → same selected multi-scale features → per-layer normalized discrepancy maps → bilinear resize to common image grid → locked layer fusion（原論文為 element-wise product）→ anomaly map → locked image aggregation（原論文為 max）→ threshold/Gate。

### representation_or_score

Normality representation 是 trained student 對 frozen teacher normal feature pyramid 的可預測性，不是顯式 memory bank、Gaussian或 defect class。每層位置 score 是 L2-normalized teacher/student feature vectors 的 squared L2 distance（與 cosine distance成比例）；低 discrepancy表示 student能模仿normal teacher response，高 discrepancy表示超出已學 normal matching。Fused upsampled map是multi-scale feature evidence，不是 native pixel supervision；max或其他 image score不是 calibrated release probability。

### cost_and_operating_point

鎖 teacher exact checkpoint/pretraining、teacher frozen state、student architecture/init/seed、selected layers/receptive fields、input/ROI/mask、normal-fit IDs/split、augmentation、feature normalization、loss/layer weights、optimizer/schedule/epochs/early stop、checkpoint selection、map resize/smoothing/fusion、image aggregation、threshold/calibration、precision/export/engine。建置需報 training time與 seed spread；推論需 teacher＋student兩條 backbone forward，端到端 P95、VRAM/RAM與低-FPR operating point必須在目標硬體量測。

### failure_boundary

Contaminated normal會教 student模仿缺陷；normal support/recipe/view coverage不足會在合法變異上產生 discrepancy。Teacher pretraining/domain mismatch可能缺少工業細節；layer過淺易受texture/background/noise影響，layer過深可能稀釋tiny/local anomaly。Student capacity、random init、optimizer與seed造成fit variance；augmentation若改變應被判異常的語意會污染normality。ROI/background/registration/illumination shift、fusion/max聚合、resolution與recipe/lot/view drift都會改score；公開AUROC不能代替本地低-FPR qualification。

### selection_gate

在有足夠乾淨 normal-fit data、可接受模型訓練與 teacher＋student雙路推論，且需同時利用不同 receptive-field layers 偵測多尺度texture/structure discrepancy時進入候選。與 RD4AD/EfficientAD比較需固定 normal support/challenge/future split、ROI/mask/registration、effective pixels、input resolution、teacher/backbone capacity、feature layers、map fusion/aggregation、hardware、decision unit與 threshold/calibration，再比較 low-FPR escape、false reject/review load、local/global recall、training/P95/VRAM、seed spread與drift rebuild。

### evidence_bundle

保存 teacher checkpoint/pretraining/frozen audit、student architecture/init/seed/checkpoint、normal-fit IDs/split/contamination audit、ROI/mask/registration、input/augmentation recipe、selected layers/shapes/receptive fields、feature normalization、loss/layer weights、optimizer/schedule/epochs/training curves、checkpoint selection、per-layer discrepancy maps、resize/fusion/aggregation、threshold/calibration revision、challenge/future/drift split、seed spread、low-FPR escape/false reject/review load、training time/P95/VRAM/RAM、failure images與 rebuild trigger。

## 視覺 primitive

- `input_roi`：clean nominal training ROIs與test ROI，含合法texture/view/illumination variation、contamination、tiny/local與large/global anomaly。
- `feature_or_patch_path`：同一input並行通過frozen teacher與trained student，抽取對應multi-scale feature pyramid。
- `normality_representation`：student checkpoint對teacher normal pyramid的layerwise imitation ability，顯示teacher lock、student train與normal-fit split。
- `score_map`：per-position normalized teacher/student discrepancy → per-layer maps → resize → locked fusion heatmap。
- `aggregation`：versioned map-to-image max/top-k policy＋threshold/calibration/decision unit。
- `normal_state_gate`：normal contamination/coverage、teacher domain、layer choice、seed/training stability、low-FPR escape、drift/retrain。

## 比較契約

- 比較 ID：`ad-stfpm-vs-efficientad-vs-rd4ad`
- 固定條件：相同 normal-fit/challenge/future split、ROI/mask/registration、effective pixels、input resolution、teacher/backbone capacity、feature layers、augmentation、map postprocess/fusion/aggregation、hardware、decision unit、threshold/calibration policy。
- 共同比較輸出：low-FPR escape、false reject/review load、local/global localization evidence、training time、P95/VRAM/RAM/state size、seed spread、normal contamination、teacher mismatch與 recipe/lot/view drift；不得以不同teacher/support/runtime或公開AUROC宣稱排名。

## 來源

- Wang et al., “Student-Teacher Feature Pyramid Matching for Anomaly Detection,” BMVC 2021 / arXiv:2103.04257v3（same-architecture frozen teacher/trained student、multi-scale normalized feature matching、per-layer discrepancy、bilinear resize、product fusion與max image score）。
- Official implementation：`https://github.com/gdwang08/STFPM`。
- `full-model-course/04-anomaly-detection.md` 的 04-19～04-22。

## 產生 gate

六個必要欄位與六個 visual primitives 已完成模型專屬遷移；可開始產生 04-19～04-22 的版本化 C/D 教學頁，逐張通過 QA 後才能 approved。

## F01 模型中心思想與來源核對

只有正常影像，仍想找各種尺寸的陌生局部。STFPM讓學生只練習模仿固定教師對正常影像的多尺度反應，用兩者不一致的位置提示異常。

**教師固定、學生學習**：教師採預訓練網路；同架構學生只以正常資料學習，兩路都接收同一影像。

**多尺度模仿**：學生對齊教師的多層特徵，兼顧局部紋理與較大結構，不是只比整圖分類結果。

**測試看兩路落差**：正常處應接近，陌生處可能不同；各尺度差異對齊融合為位置線索，教師本身不需知道缺陷名稱。

**移除設計自測**：讓學生直接共享教師的全部權重與輸出，差異還有用嗎？

兩路相同就沒有可比較的落差。正常限定的學習才可能使學生在陌生局部與教師不同；但這個差異不是每種缺陷都保證出現。

**選型**：有正常訓練資料且可負擔兩路推論時可試；與 RD4AD 比較學生接原圖還是壓縮特徵，並量漏檢和端到端耗時。

[原論文／官方來源](https://arxiv.org/abs/2103.04257)。本輪原生 SVG 結合既有生成金屬件；特徵與差異為教學設定，沒有新增推論。先前章節如描述應用擴充，不應解讀為原模型必需步驟。

<!-- wi033-engineering:start -->
## WI-033 工程圖修正

### STFPM：把正常反應教給學生

使用正常影像訓練學生匹配固定教師的多尺度特徵，推論同待測影像送兩路並整合差異。交付可疑位置及影像分數；教師和學生也可能對缺陷反應相似，需留出真缺陷驗證。

學生學正常教師反應，差異只是回查線索。

來源：https://arxiv.org/html/2103.04257v3

### STFPM：兩路同尺度、同位置比較

教師與學生架構相同，正常訓練只更新學生；推論兩路都固定。以單位向量T=[1,0]、S=[.8,.6]為例，半平方L2距離=.2。原方法上採樣各層位置差異後逐點相乘，給定p三層.2/.4/.5得到.04；這是機制算例，不是異常機率或量測輪廓。

教師學生的逐層差異，經對齊後整合。

來源：https://arxiv.org/html/2103.04257v3

### STFPM：保存兩路權重與逐層配對

保存教師權重、學生checkpoint、前處理、特徵層/正規化/插值及彙整方式。推論固定兩路，按同位置與同層計差，不能混不同層或拿熱區直接量尺寸。用未見正常和真缺陷評門檻與覆核量。

同尺度同位置的配對，比單看熱區更重要。

來源：https://arxiv.org/html/2103.04257v3

### STFPM與RD4AD：學生吃的輸入不同

STFPM教師和同架構學生直接接收同影像；RD4AD由教師表示經瓶頸送反向學生重建。兩者皆在正常資料學習並比特徵，但學生輸入和重建路徑不同；同留出集比代價，不捏造優劣。

同樣比較特徵，兩種學生路徑要分清。

來源：https://arxiv.org/html/2103.04257v3

<!-- wi033-engineering:end -->

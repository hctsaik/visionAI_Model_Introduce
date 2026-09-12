# AnomalyDINO（`ad-anomalydino`）

- roadmap 分類：`anomaly-detection`
- 講義對照：`04-11`～`04-14`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/ad-anomalydino.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
正常樣本有限，想利用既有視覺表示找出金屬板上缺少正常先例的局部。

### 它交出什麼，也不交出什麼
可疑位置及影像分數，交人比對原圖；不是文字問答，也不是缺陷尺寸量測。

### 一句心智模型
AnomalyDINO利用已預訓練的DINOv2擷取區塊特徵，從正常圖建立參考。待測圖的區塊特徵與正常參考比相似度，局部差異映回原圖；Transformer讓區塊表示帶有全圖情境。免額外訓練指不為此異常偵測工作微調，並不是模型從未訓練或不需要正常資料。

**限制：** 同一片沒有刮傷的金屬板，換成斜照後出現亮帶，也可能被標成可疑。分數反映與既有正常的差異，不直接證明工件損壞。

### 換一個現場再推理
新產品只有少量確認正常影像，舊DINOv2特徵可用；一週內只能優先做補拍正常變化，或進行模型微調試驗。

**問題：** 你先補拍並建立參考，還是先微調？什麼結果會支持下一步換路線？

**核對：** 若問題是光照、批次或姿態覆蓋不足，先補正常參考通常更直接，也符合本方法免額外微調的起點。若獨立檢查顯示特徵無法分開任務關心的差異，再考慮微調或其他方法；那是新增方案，需另設訓練與驗證。少樣本與免微調都不代表免測誤報漏檢。
<!-- topic-learning-bridge:end -->
## 模型定位

AnomalyDINO 是 vision-only、training-free one/few-shot anomaly detector：以 frozen DINOv2 patch representations 建 nominal memory bank，讓每個 test patch 對整個 normal token memory（不限制與 support 的同一空間位置）做 cosine 1-nearest-neighbour distance。它從 raw patch-distance grid 分別形成 image candidate score 與定位 candidate map；不是 DINO object detector、Grounding DINO、defect classifier 或原生高解析 segmentation。normal support selection 與 DINOv2 patch resolution 決定可見的 normality。

## 必要欄位

### architecture_path

建 gallery：clean nominal reference image(s) → versioned resize/rotation policy → optional DINOv2 PCA object mask＋morphology → frozen DINOv2 checkpoint/layer → patch-token grid → retain valid nominal tokens → global support token memory bank。推論：test ROI/tile → 已宣告的 ROI／resize／mask／encoder policy → query patch tokens → cosine 1-NN distance to the full bank（不是同位置對應）→ raw patch-distance grid；reference 與 test 的 mask／rotation 不可默認相同。此 grid 分叉為 bilinear upsample/smooth/mask 後的定位 candidate map，以及版本化 top-tail/top-k aggregation 後的 image candidate score＋threshold/Gate。

### representation_or_score

Normality representation 是 one/few clean support 經 DINOv2 產生的 valid patch-token memory，不是 learned defect class、text prompt 或 generative normal model。Patch score 是 query token 到整個 memory 中最近 nominal token 的 cosine distance，不要求 support 與 query 位於同一空間位置。raw patch distances 有兩種不同用途：image score 聚合最高距離 patch 的尾端統計（原論文預設為最高 1% 距離的平均，但交付需鎖實作）；定位則保留 token grid，再做 upsample/smooth/mask。後者只是由 patch-token grid 插值而來的 localization candidate map，不是原生 pixel supervision、逐像素真值或 calibrated defect probability。

### cost_and_operating_point

鎖 DINOv2 exact checkpoint/size、layer/facet、input resolution（與 patch/grid contract）、normal shot count/IDs、support rotation policy、PCA mask test/threshold/morphology、ROI/tile/registration、token normalization、cosine/index/search K、map upsample/smoothing、tail/top-k aggregation、threshold/calibration、precision/export/engine。端到端 P95 包含 encoder、mask、support search、tile/map aggregation；同時報 support-selection variance、low-FPR escape、false reject/review load、RAM/storage與 drift。

### failure_boundary

One/few support bias、normal multimodality/coverage 不足與 contamination 會扭曲 memory；rotation augmentation 可能把應視為 anomaly 的 orientation 收進 normality，或反之。PCA mask 可能漏掉 object regions；registration/ROI/background shift、patch size/token grid 稀釋 tiny defects、DINOv2 domain mismatch、cosine/index/aggregation 選擇、recipe/lot/view drift 都會改變 score。它也不是判斷零件之間關係的可靠主模型：若異常是各零件外觀仍正常、但接線／裝配位置／數量關係錯誤的 semantic 或 layout anomaly（例如 cable swap），global patch novelty 可能接近正常，應改以 keypoint、relation/graph、metrology 或其他專門檢查路徑處理。公開 benchmark AUROC 不能代替本地低-FPR qualification。

### selection_gate

在只有少量 clean normal、需要快速 training-free exploration、DINOv2 foundation patch features 對目標局部 texture/structure novelty 有辨識力，且 one/few-shot support/mask/rotation 可治理時選用；不要把它當 semantic／layout relation inspection 的主檢查器。與 PatchCore/SubspaceAD 比較需固定 support/challenge/future split、ROI/registration/mask、effective pixels、input/token-grid resolution、score aggregation、hardware/index、decision unit、threshold/calibration，再比較 low-FPR escape、false reject/review load、P95/RAM、support variance與 drift。

### evidence_bundle

保存 exact DINOv2 checkpoint/layer/input resolution/patch-grid、support IDs/shot count/selection runs、contamination audit、rotation policy、PCA mask test/threshold/morphology、ROI/tile/registration、token normalization、cosine/index/K、map upsample/smoothing、tail/top-k aggregation、threshold/calibration revision、challenge/future/drift split、support variance、low-FPR escape/false reject/review load、P95/RAM/storage、failure images與 rebuild trigger。

## 視覺 primitive

- `input_roi`：one/few clean nominal references 與 test ROI，含 orientation/background/lot/view variation、tiny anomaly。
- `feature_or_patch_path`：DINOv2 resize/optional mask → frozen ViT patch-token grid → support/query tokens。
- `normality_representation`：valid nominal support token memory bank，明示 query 是搜尋整個 bank、不是同位置配對，並顯示 shot coverage、rotation/mask policy。
- `score_map`：cosine 1-NN raw distance grid → upsample/smooth/mask localization candidate map；不宣稱 native pixel mask。
- `aggregation`：同一 raw distance grid 的版本化 top-tail/top-k image statistic＋threshold/calibration/decision unit。
- `normal_state_gate`：support cleanliness/variance/coverage、mask test、rotation semantics、token resolution、low-FPR escape、drift/rebuild。

## 比較契約

- 比較 ID：`ad-anomalydino-vs-subspacead`
- 固定條件：相同 nominal support/challenge/future split、ROI/registration/mask、effective pixels、input/token-grid resolution、shot count、score map postprocess/aggregation、hardware/index、decision unit、threshold/calibration policy。
- 共同比較輸出：support-selection variance、low-FPR escape、false reject/review load、localization evidence、P95/RAM/storage、rotation/mask sensitivity、recipe/lot/view drift；不得以不同 shot/support 或公開 AUROC 宣稱排名。

## 來源

- Damm et al., “AnomalyDINO: Boosting Patch-based Few-shot Anomaly Detection with DINOv2,” arXiv:2405.14529（DINOv2 patch memory、cosine NN、mask/rotation preprocessing、tail aggregation）。
- `full-model-course/04-anomaly-detection.md` 的 04-11～04-14。

## 產生 gate

六個必要欄位與六個 visual primitives 已完成模型專屬遷移；可開始產生 04-11～04-14 的版本化 C/D 教學頁，逐張通過 QA 後才能 approved。

## F01 模型中心思想與來源核對

新產品可能只有幾張正常品。AnomalyDINO借用已學好的 DINOv2 表徵，把正常 patch tokens 留成小參考庫，再查待測局部是否有相近先例。

**固定 DINOv2**：整張影像進預訓練模型，取得帶有影像情境的局部 token；不是逐張裁片重新訓練。

**少量正常參考**：正常 tokens 組成記憶庫，待測局部不限同座標找近鄰；少樣本仍須涵蓋允收外觀。

**距離產生線索**：相近正常特徵找不到時，距離上升；patch 分數回映位置並聚合整圖，熱圖不等於精密邊界。

**移除設計自測**：固定 DINOv2 還在，卻把正常參考庫拿掉，原流程還能算什麼？

可以抽 tokens，但失去本產品的正常近鄰比較，不能沿用原來的距離分數。DINOv2 預訓練不等於已知道此產品的允收規格。

**選型**：正常樣本很少可先探索；換產品仍要建參考、驗證尺度和门檻。與 PatchCore 比較須固定影像解析度、參考數與硬體。

[原論文／官方來源](https://arxiv.org/abs/2405.14529)。本輪原生 SVG 結合既有生成金屬件；特徵與差異為教學設定，沒有新增推論。先前章節如描述應用擴充，不應解讀為原模型必需步驟。


<!-- wi030-model-core:start -->
## WI-030 核心做法與工作取捨

AnomalyDINO利用已預訓練的DINOv2擷取區塊特徵，從正常圖建立參考。待測圖的區塊特徵與正常參考比相似度，局部差異映回原圖；Transformer讓區塊表示帶有全圖情境。免額外訓練指不為此異常偵測工作微調，並不是模型從未訓練或不需要正常資料。

同一片沒有刮傷的金屬板，換成斜照後出現亮帶，也可能被標成可疑。分數反映與既有正常的差異，不直接證明工件損壞。

PatchCore保存CNN代表局部供查找；PaDiM估計每個位置的正常分布；AnomalyDINO用DINOv2特徵建立參考；EfficientAD用正常資料學教師／學生與全域特徵關係。先固定取像與缺陷需求，再比錯誤與完整成本。

固定DINOv2版本、縮放、背景處理與參考策略；更換產品或前處理後重建參考並驗證。少樣本仍要記錄取樣代表性、特徵儲存及推論成本。

先確認少量正常參考可涵蓋哪些允收外觀，保留未見批次，再測小缺陷和背景變動。

保存真實原圖、版本、正常資料切分、熱圖與覆核結果；同批獨立正常／缺陷樣本分開計誤報、漏檢，並量包含取像、前處理、模型與交接的耗時及記憶體。圖中熱區不是模型推論。

來源：https://arxiv.org/abs/2405.14529

版本及示意界線見工作項目 sources.md。使用者成品核准pending。
<!-- wi030-model-core:end -->

<!-- wi033-engineering:start -->
## WI-033 工程圖修正

### AnomalyDINO：固定模型，正常局部存庫

本課少樣本路徑用固定預訓練DINOv2抽整張影像的局部tokens，保留選定正常樣本的特徵與來源。不是逐張裁片重新訓練，也不是零設定；取像、resize及選用mask/rotation需寫清，未見正常與真缺陷另外留出。

免額外訓練，仍要選乾淨正常參考並建立相容庫。

來源：https://arxiv.org/html/2405.14529v2

### AnomalyDINO：每個局部找最近正常

待測整圖與參考共用DINOv2權重及相容前處理。每個test token以餘弦距離在normal memory找最近者；圖中0.40、0.62、0.55為教學給定距離，最小0.40不代表已足夠正常。局部距離上採樣/平滑形成位置圖；整件分數另聚合最高1%patch距離，不能把熱圖當精密輪廓。

最近距離保留位置，組成候選異常圖。

來源：https://arxiv.org/html/2405.14529v2

### AnomalyDINO：換參考就要重驗正常定義

固定模型與前處理只增加候選時，最近距離不會增加；若新增參考含缺陷，原本异常可能變得相近。用同一刮痕、原候選距離0.40/0.55、新污染候選0.03說明算術，不宣稱真實模型結果。更新後同时測正常與真缺陷，保存庫來源並量建庫、查詢及記憶體。

保存參考版本，誤報與漏檢要一起比較。

來源：https://arxiv.org/html/2405.14529v2

### AnomalyDINO：先判斷旋轉是否被允許

同一帶A-01刻字的板連同所有孔位/字一起剛性旋轉180度。若規格允許自由方向，可測旋轉參考是否減少誤報；若標誌必須朝上，就不能以納入倒置參考來消除方向錯誤，另做方向檢查。兩路是不同工作規格，不是演算法串接。

旋轉擴充改變正常涵蓋，朝向規格仍須另驗。

來源：https://arxiv.org/html/2405.14529v2

<!-- wi033-engineering:end -->

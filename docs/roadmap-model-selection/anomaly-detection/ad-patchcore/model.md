# PatchCore（`ad-patchcore`）

- roadmap 分類：`anomaly-detection`
- 講義對照：`04-03`～`04-06`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/ad-patchcore.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
金屬板缺陷很少，你已有一批確認正常的影像，想先把沒有正常先例的局部交給人回查。

### 它交出什麼，也不交出什麼
局部可疑熱圖與影像異常分數，送人工覆核原圖；不直接交付缺陷種類、實體尺寸或允收結論。

### 一句心智模型
PatchCore用固定的預訓練CNN擷取局部特徵，從正常特徵中挑代表子集存成庫。待測局部與庫中最相近的正常特徵仍相差很大時，該位置就更值得回查。庫中存的是特徵，並非直接比原圖像素；代表子集減少查找負擔，也會影響正常外觀覆蓋。

**限制：** 同一片沒有刮傷的金屬板，換成斜照後出現亮帶，也可能被標成可疑。分數反映與既有正常的差異，不直接證明工件損壞。

### 換一個現場再推理
新批次的允收紋理較多；小代表庫會誤報，較大的候選庫已改善誤報，但查詢時間超出你的節拍預算。

**問題：** 你會調整代表子集、保留大庫做離線覆核，或改測另一方法？先說出不能犧牲的條件。

**核對：** 三條路都可能合理。若線上節拍優先，先用涵蓋新正常變化的子集重測誤報與漏檢；若允許離線覆核，可保留大庫並計入等待成本。若仍不符合節拍，再比較其他方法的完整成本。已確認正常才可納入參考，所有候選都要用相同獨立正常／缺陷資料驗證。
<!-- topic-learning-bridge:end -->
## 模型定位

PatchCore 是以 clean nominal images 建立 representative patch-feature memory bank/coreset 的 nearest-neighbour anomaly detector。它以 test patch 到最近 normal exemplar 的距離產生 novelty map 與 image score，適合局部 texture/structure deviation 的 cold-start/few-normal-label 場景。它不學 defect class、根因或 calibrated release probability；normal support coverage 決定可接受變異的表徵。

## 必要欄位

### architecture_path

建 bank：nominal ROI/tile → frozen pretrained backbone → selected multi-layer feature maps → resize/alignment＋local patch embeddings → optional projection → coreset/subsampling → indexed normal memory bank。推論：test ROI → same feature path → each patch nearest-neighbour search against bank → distance score per patch → patch grid map → upsample/smooth/mask → versioned max/top-k/weighted image aggregation → threshold/Gate。

### representation_or_score

Normality representation 是 coreset 中具代表性的 nominal patch embeddings，不是 generative normal image 或單一 class centroid。Patch score 是到最近 normal memory exemplar 的 feature-space distance（distance/index/config 需鎖）；heatmap 是 encoder patch grid 經 upsample/aggregation 的 evidence，不是 native pixel defect mask。Image score 與 release probability 需另行 calibration。

### cost_and_operating_point

鎖 backbone/checkpoint、feature layers、input/ROI/tile/registration、patch pooling/alignment、embedding dimension/projection、coreset method/ratio/seed、distance metric、ANN/exact index、search K、map upsample/smoothing、aggregation、threshold/decision unit、precision/export/engine。端到端 P95 包含 feature extraction、index search、map postprocess與 aggregation；同時記 RAM/storage、bank build time、low-FPR escape、false reject/review load、localization/boundary evidence。

### failure_boundary

Normal bank coverage 不足會把合法 recipe/lot/view/texture variation 判為 anomaly；support contamination 會把缺陷收進 normality。Registration/ROI/mask/tile 變動、backbone domain mismatch、tiny defect 小於 patch/effective resolution、coreset 過度壓縮、ANN approximation、memory/P95 過高與 future drift 都會改變 distance map/threshold。公開 AUROC 不能代替低-FPR fab operating point。

### selection_gate

在 nominal support 可乾淨收集、可保存 representative exemplars、局部 texture/structure deviation 是主要風險、希望少量訓練且能接受 memory/index 成本時選用。與 PaDiM/AnomalyDINO 比較需固定 ROI/registration、support split/count、effective pixels、encoder/feature contract（若可比）、score aggregation、hardware/index、decision unit、threshold/calibration，再比較 low-FPR escape、false reject/review load、P95/RAM 與 drift behavior。

### evidence_bundle

保存 exact backbone/checkpoint/layers、input/ROI/tile/registration/mask、normal support IDs與 contamination audit、embedding/projection、coreset method/ratio/seed、memory size/checksum、distance/index/search K、map upsample/smoothing/aggregation、threshold/calibration revision、challenge/future/drift split、low-FPR escape/false reject/review load、P95/RAM/storage、failure images 與 rebuild trigger。

## 視覺 primitive

- `input_roi`：對齊 nominal/test ROI，包含 texture、structure、合法 recipe variation 與局部 anomaly。
- `feature_or_patch_path`：frozen backbone multi-layer feature maps → aligned patch embeddings → coreset/index。
- `normality_representation`：具代表性的 nominal patch-feature memory bank；顯示 coverage 與 compression。
- `score_map`：test patch nearest-neighbour distance → patch grid → upsample/smooth/mask anomaly heatmap。
- `aggregation`：versioned max/top-k/weighted patch-to-image score＋threshold/decision unit。
- `normal_state_gate`：support cleanliness/coverage、registration/ROI、memory/P95、low-FPR escape、drift/rebuild。

## 比較契約

- 比較 ID：`ad-patchcore-vs-padim`
- 固定條件：相同 nominal support/challenge/future split、ROI/registration/mask、effective pixels、encoder/features（可比時）、score map resolution/aggregation、hardware/index、decision unit、threshold/calibration policy。
- 共同比較輸出：low-FPR escape、false reject/review load、localization/boundary evidence、P95、RAM/storage、support contamination sensitivity、recipe/lot/view drift；不得以公開 AUROC 或不同 normal support 宣稱排名。

## 來源

- Roth et al., “Towards Total Recall in Industrial Anomaly Detection,” arXiv:2106.08265（nominal patch-feature memory bank、representative coreset、nearest-neighbour detection/localization）。
- `full-model-course/04-anomaly-detection.md` 的 04-03～04-06。

## 產生 gate

六個必要欄位與六個 visual primitives 已完成模型專屬遷移；可開始產生 04-03～04-06 的版本化 C/D 教學頁，逐張通過 QA 後才能 approved。


## P01 工作導讀（2026-09-06）

已加入 [八章工作導讀](../../patchcore-workplace-deep-dive.md)。局部提取位於CNN特徵圖，非先裁照片逐片推論；原論文L2與鄰域加權、作者程式平方L2與最大patch聚合分開記錄。教學二維例與作者實際結果不混稱。正式啟用資產及來源版本見topic deep_dive與p01-manifest.json。


## P03 學習後重製（2026-09-06）

八章工作導讀更新為17個閱讀視圖：实际CNN提取、來源局部與coreset、鄰域加權對照、同產品三模型資料流、兩個第三方raw/GT/output案例。原作者漏檢及正常／缺陷最近鄰對照保留。CNN示範非完整PatchCore推論；公開重現非原作者輸出，各自標示来源限制。正式啟用引用以topic為準，圖像與來源在p03-manifest.json。

## F01 模型中心思想與來源核對

缺陷種類列不完，卻有合格品可收集。PatchCore把正常局部的特徵留成參考，讓新局部找相似先例，不必先訓練每種缺陷分類器。

**局部描述**：固定預訓練 CNN，把中間層的局部訊息組成特徵；比較的是特徵，原圖小片用來追查來源。

**代表子集**：Coreset 保留覆蓋不同正常外觀的代表，減少儲存及搜尋；不是只留平均樣本。

**最近鄰距離**：待測局部查整個參考庫，最像的仍差很多才可疑；位置圖回到待測影像，整圖分數另按實作聚合。

**移除設計自測**：拿掉 coreset、保留全庫，還能判異常嗎？

仍可最近鄰比較，但儲存與搜尋成本增加。若改成隨意刪到只剩一種紋理，原本允收的少見正常局部可能找不到近鄰。

**選型**：已有涵蓋變化的正常品可先做建庫方法；換產品重建參考並留出正常／缺陷驗證。庫大小與搜尋耗時一起量。

[原論文／官方來源](https://arxiv.org/abs/2106.08265)。本輪原生 SVG 結合既有生成金屬件；特徵與差異為教學設定，沒有新增推論。先前章節如描述應用擴充，不應解讀為原模型必需步驟。


<!-- wi030-model-core:start -->
## WI-030 核心做法與工作取捨

PatchCore用固定的預訓練CNN擷取局部特徵，從正常特徵中挑代表子集存成庫。待測局部與庫中最相近的正常特徵仍相差很大時，該位置就更值得回查。庫中存的是特徵，並非直接比原圖像素；代表子集減少查找負擔，也會影響正常外觀覆蓋。

同一片沒有刮傷的金屬板，換成斜照後出現亮帶，也可能被標成可疑。分數反映與既有正常的差異，不直接證明工件損壞。

PatchCore保存CNN代表局部供查找；PaDiM估計每個位置的正常分布；AnomalyDINO用DINOv2特徵建立參考；EfficientAD用正常資料學教師／學生與全域特徵關係。先固定取像與缺陷需求，再比錯誤與完整成本。

不需為本工作微調特徵網路，但要建立與維護正常庫；產品、前處理或骨幹改變時需重建並驗證。比較代表子集大小造成的覆蓋、記憶體和查詢時間取捨。

先確認正常資料含允收紋理和光照，另留完整批次測試，固定ROI、縮放與CNN版本後建立正常庫。

保存真實原圖、版本、正常資料切分、熱圖與覆核結果；同批獨立正常／缺陷樣本分開計誤報、漏檢，並量包含取像、前處理、模型與交接的耗時及記憶體。圖中熱區不是模型推論。

來源：https://arxiv.org/abs/2106.08265

版本及示意界線見工作項目 sources.md。使用者成品核准pending。
<!-- wi030-model-core:end -->

<!-- wi033-engineering:start -->
## WI-033 工程圖修正

### PatchCore：用確認正常的局部當參考

建立正常參考只使用已確認正常影像；待測與留出資料不回灌。固定特徵擷取與庫版本，輸出局部距離圖及影像分數，交原圖覆核。這個任務不預先列完缺陷類別，也不直接交付尺寸。

正常庫定義見過什麼，輸出仍需人工覆核。

來源：https://arxiv.org/abs/2106.08265

### PatchCore：查最近正常特徵，再排回位置

固定CNN抽正常局部特徵，以coreset保留代表子集；待測局部在同特徵空間查最近鄰。二維例p=[3,2]，r1=[0,0]距離3.61，r2=[2,0]距離2.24；p位置排回2.24。圖中小網格僅局部距離示意，整圖分數還有原法的重加權，不能把局部距離說成缺陷機率。

局部距離來自特徵查庫，熱區要回原圖核對。

來源：https://arxiv.org/abs/2106.08265

### PatchCore：縮庫，要連正常覆蓋一起驗

保存骨幹、層、前處理、聚合、coreset及索引。給定10000×512 float32特徵約20.48MB，留1000代表約2.048MB，未含索引/其他模型成本；只是容量算例，不能宣稱查找快十倍。縮库後用獨立正常與真缺陷驗證。

庫小可以省資源，漏掉正常變化會有代價。

來源：https://arxiv.org/abs/2106.08265

### PatchCore：庫裡混入刮傷，就可能漏報

同特徵p=[3,2]原本最近正常[2,0]距離√5，誤把[3,2]存為正常後最近距離0。原圖缺陷没有改變；本例只展示局部查庫污染，非實際模型結果。保留資料審核及追溯，不以距離0當品質保證。

低距離可能只是正常庫被污染。

來源：https://arxiv.org/abs/2106.08265

<!-- wi033-engineering:end -->

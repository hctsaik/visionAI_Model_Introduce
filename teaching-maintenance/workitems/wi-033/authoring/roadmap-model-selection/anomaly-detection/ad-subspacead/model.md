# SubspaceAD（`ad-subspacead`）

- roadmap 分類：`anomaly-detection`
- 講義對照：`04-15`～`04-18`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/ad-subspacead.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
固定相機檢查兩孔金屬板，已有少量正常品。用正常局部的主要變化建立子空間，檢查新板刮傷 p 是否留下解釋不了的特徵。

### 它交出什麼，也不交出什麼
patch 網格的可疑熱圖與候選分數，用於回看原始影像；不直接提供缺陷名稱、精密像素輪廓、尺寸或放行結論。

### 一句心智模型
固定 DINOv2 提取局部特徵，PCA 從正常資料估計主要變動方向。待測特徵投影回子空間，未被解釋的殘差形成異常線索。

**限制：** 正常資料涵蓋不足可能誤報；保留太多方向可能吸收異常。線性子空間也未必適合所有正常分布。

### 換一個現場再推理
新產品有兩種差別很大的合法構型，合併後正常特徵分成兩群。

**問題：** 是否直接增加維度就足夠？

**核對：** 不保證。先確認兩種構型、取像與樣本量，檢查單一線性子空間能否同時解釋正常又分開缺陷；可考慮分產品／構型建模或其他特徵方法，用獨立驗證選擇，不能只看擬合殘差變小。
<!-- topic-learning-bridge:end -->
## 模型定位

SubspaceAD 是 training-free one/few-shot anomaly detector：以 frozen DINOv2 patch features 與乾淨 normal support 擬合一個 PCA linear subspace，將 test patch 投影回 normal plane，並以 feature reconstruction residual 產生 anomaly map 與 image score。它用 compact mean＋basis 表示 normal variation，不是 exemplar memory bank、defect classifier、pixel-supervised segmenter 或 calibrated release probability；support、feature recipe、PCA rank/variance policy 與 patch resolution 是核心契約。

## 必要欄位

### architecture_path

建 normal state：clean one/few-shot nominal ROI → versioned resize/augmentation/mask/registration → frozen DINOv2 checkpoint＋selected/aggregated patch-token layers → collect valid normal patch features X → normalization → fit global PCA mean μ and orthonormal basis C with locked explained-variance/rank policy → versioned compact subspace state。推論：test ROI → same preprocessing/encoder/features → centered patch z−μ → projection C C^T(z−μ) → orthogonal residual r=(I−CC^T)(z−μ) → ||r|| score grid → upsample/filter/mask → versioned top-tail/TVaR aggregation → image score＋threshold/Gate。

### representation_or_score

Normality representation 是所有合法 normal patch features 的 global low-dimensional linear plane，由 μ、basis C、rank/variance threshold 定義；不是逐位置 Gaussian 或保存所有 exemplar。Patch anomaly evidence 是 feature 到 normal subspace 的 orthogonal reconstruction residual norm；低 residual 表示被 normal plane 解釋，高 residual 表示落在 plane 外。Upsampled map 仍是 patch-grid evidence，不是 native pixel mask；image score 與 release probability需另行 calibration。

### cost_and_operating_point

鎖 exact DINOv2 checkpoint/size、feature layers與 aggregation、input resolution/token grid、ROI/registration/mask、normal support IDs/shot count、augmentation policy/seed、token normalization、PCA solver、mean/basis、explained-variance threshold或 rank、map upsample/filter、top-tail/TVaR aggregation、threshold/calibration、precision/export/engine。Basis state通常比 full patch bank compact，但端到端 P95仍包含大型 encoder；同時治理 fit time、state size、projection cost、support-selection variance、low-FPR escape、false reject/review load與 rebuild trigger。

### failure_boundary

Normal variation若是 multimodal、curved或非線性 manifold，單一 linear plane可能 underfit；rank過低會把合法 normal variation判異常，rank過高可能吸收 defect direction。Few-shot support bias、normal contamination與不合理 augmentation會污染 basis；ROI/background/registration shift、DINOv2 domain mismatch、patch欠採樣/tiny defect、feature layer或 normalization變動都會改 residual。Patch-based local evidence不直接理解 missing/misplaced component等 logical anomaly；recipe/lot/view drift需重新 qualification。公開 benchmark AUROC不能代替本地低-FPR operating point。

### selection_gate

在只有少量乾淨 normal、DINOv2 patch features 對目標外觀有效、normal variation可由 compact linear subspace近似，且希望避免 large exemplar bank/NN search時進入候選；仍以 emerging research candidate 管理，不直接視為 production default。與 AnomalyDINO/PatchCore比較需固定 support/challenge/future split、ROI/registration/mask、effective pixels、encoder/features/input token grid、augmentation、map aggregation、hardware、decision unit與 threshold/calibration，再比較 low-FPR escape、false reject/review load、P95/state size、support variance與 drift。

### evidence_bundle

保存 exact DINOv2 checkpoint/layers/aggregation/input resolution/token grid、support IDs/shot count/selection runs、contamination audit、augmentation/mask/registration recipe與 seed、token normalization、PCA solver/μ/basis/rank/explained-variance/state checksum、fit diagnostics與 residual distribution、map upsample/filter/top-tail/TVaR aggregation、threshold/calibration revision、challenge/future/drift split、support variance、low-FPR escape/false reject/review load、P95/state size/fit time、failure images與 rebuild trigger。

## 視覺 primitive

- `input_roi`：one/few clean nominal references與 test ROI，含合法 normal variation、support contamination、registration shift及 tiny/logical anomaly。
- `feature_or_patch_path`：DINOv2 resize/augmentation/mask → frozen ViT patch-token layers → selected/aggregated features。
- `normality_representation`：global PCA mean μ＋orthonormal basis C＋rank/variance policy，顯示 normal points貼近低維 plane。
- `score_map`：test feature projection → orthogonal residual vector → residual-norm patch grid → upsample/filter/mask heatmap。
- `aggregation`：versioned top-tail/TVaR image statistic＋threshold/calibration/decision unit。
- `normal_state_gate`：support cleanliness/coverage、augmentation semantics、rank/variance sensitivity、token resolution、low-FPR escape、drift/rebuild。

## 比較契約

- 比較 ID：`ad-anomalydino-vs-subspacead`
- 固定條件：相同 nominal support/challenge/future split、ROI/registration/mask、effective pixels、DINOv2 checkpoint/features/input token grid、shot count/augmentation、score-map postprocess/aggregation、hardware、decision unit、threshold/calibration policy。
- 共同比較輸出：low-FPR escape、false reject/review load、localization evidence、support-selection variance、P95/RAM/storage/state size、fit/rebuild cost、augmentation/registration sensitivity與 recipe/lot/view drift；不得以不同 support、encoder或公開 AUROC宣稱排名。

## 來源

- Lendering, Akdag, and Bondarev, “SubspaceAD: Training-Free Few-Shot Anomaly Detection via Subspace Modeling,” CVPR 2026 / arXiv:2602.23013v3（frozen DINOv2 patch features、global PCA normal subspace、orthogonal reconstruction residual、top-tail aggregation）。
- Official implementation：`https://github.com/CLendering/SubspaceAD`。
- `full-model-course/04-anomaly-detection.md` 的 04-15～04-18。

## 產生 gate

六個必要欄位與六個 visual primitives 已完成模型專屬遷移；可開始產生 04-15～04-18 的版本化 C/D 教學頁，逐張通過 QA 後才能 approved。

## F01 模型中心思想與來源核對

正常局部很多，卻可能只沿少數特徵方向變動。SubspaceAD用正常特徵估計低維子空間，檢查新局部是否留下正常變化解釋不了的部分。

**借用固定特徵**：使用預訓練 DINOv2 的局部特徵；免梯度訓練仍要以正常樣本擬合 PCA。

**正常方向成子空間**：PCA 保留主要正常變動方向；它在特徵空間，不是工件上的實體平面。

**投影後看殘差**：將待測特徵投影回正常子空間，剩餘距離形成異常線索；rank 太大可能也解釋掉异常。

**移除設計自測**：如果保留全部特徵維度，投影殘差會怎樣？

若子空間張成完整空間，重建投影等於輸入，殘差歸零，失去這條異常線索。rank 太小則可能把正常變化也當成殘差。

**選型**：和近鄰庫比較時，先問正常是否適合線性方向描述；換產品重估子空間，用未入庫正常品與缺陷檢查 rank 取捨。

[原論文／官方來源](https://arxiv.org/abs/2602.23013)。本輪原生 SVG 結合既有生成金屬件；特徵與差異為教學設定，沒有新增推論。先前章節如描述應用擴充，不應解讀為原模型必需步驟。

<!-- wi033-engineering:start -->
## WI-033 工程圖修正

### SubspaceAD：正常方向是資料擬合出來的

固定DINOv2不更新梯度，正常資料估計均值與低維PCA方向；待測投影殘差形成異常線索。免訓練指骨幹不做梯度更新，不表示免正常資料/擬合/部署驗證；保留原同板主線。

免骨幹訓練，仍要建立可比較的正常子空間。

來源：https://github.com/CLendering/SubspaceAD

### SubspaceAD：畫出投影與正交殘差

固定DINOv2提取patch特徵並用正常資料擬合PCA。給定已中心化特徵x=[3,2]與保留方向U=[1,0]，投影[3,0]，殘差[0,2]長度2。二維幾何例不代表工件平面或實際特徵維度；完整公式需保留均值，圖中明示mu=0。

未被正常方向解釋的殘差，才是異常線索。

來源：https://github.com/CLendering/SubspaceAD

### SubspaceAD：保留維度就是模型設定

保存骨幹/前處理、正常樣本、均值μ、正交基U和保留維度k；實際投影需先減μ再加回。圖中μ=0是算例簡化。更改k或特徵設定要重新評估正常誤報和真缺陷漏檢，不能只看擬合誤差下降。

均值、方向與保留維度都必須能重現。

來源：https://github.com/CLendering/SubspaceAD

### SubspaceAD：留全維，連異常也能投回去

延續中心化x=[3,2]；只留水平一維，投影[3,0]殘差2；二維全保留，投影等於x，殘差0。這是線性投影的確切算例，说明增加維度不保證異常檢測更好。

殘差變小，可能是保留的方向太多。

來源：https://github.com/CLendering/SubspaceAD

<!-- wi033-engineering:end -->

# ConvNeXt（`convnext`）

- roadmap 分類：`known-target-classification`
- 講義對照：`02-07`～`02-10`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/convnext.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
固定相機拍螺絲頭，要把十字、一字與內六角分流到不同料盒。

### 它交出什麼，也不交出什麼
已知類別與模型分數，交分流規則或人工覆核；未知產品、輪廓與3D姿態另行處理。

### 一句心智模型
ConvNeXt把卷積網路現代化：較大視窗的depthwise卷積先讓每個通道整理周圍空間線索，再用通道混合交換資訊，搭配殘差及其他設計。分類工作仍是從影像特徵得到已知類別；它不是因名稱新就一定較省或較準。

**限制：** 訓練照片中十字螺絲總在藍墊、內六角總在橘墊，模型可能學到背景捷徑。把同一十字螺絲換到橘墊後，可能誤判內六角；工件本身沒有改變。

### 換一個現場再推理
ResNet已符合現行需求；ConvNeXt候選在困難類別較好，但部署記憶體較高，且需要重新驗證。

**問題：** 你會維持ResNet、全面換成ConvNeXt，或只讓困難樣本走新模型？要補哪些成本證據？

**核對：** 若困難類別的漏分成本足以抵銷資源與驗證成本，可以換；若收益很小，保留穩定基準合理。分流方案也可測，但要驗證分流漏接、兩模型維護及最壞延遲。同資料、硬體、輸入和門檻比較，不能只按模型年代決定。
<!-- topic-learning-bridge:end -->
## 模型定位

ConvNeXt 是以 standard ConvNet modules 建立的現代化 CNN family。它保留卷積的局部與階層歸納偏置，吸收 patchify-like stem、large-kernel depthwise convolution、LayerNorm 與 inverted-bottleneck-style channel mixing 等設計；它是架構族而非單一 checkpoint，仍是 closed-set classifier 時只輸出已知類別 logits。

## 必要欄位

### architecture_path

固定 ROI image → versioned resize／normalize → patchify-like convolution stem → hierarchical stages：large-kernel depthwise convolution → LayerNorm → pointwise channel expansion → GELU → pointwise projection → residual merge → stage downsampling → global average pooling → normalization／linear head → class logits。必須鎖 Tiny／Small／Base 等 variant、pretraining、resolution 與 training recipe。

### representation_or_score

各 stage 輸出階層式 spatial feature maps；large-kernel depthwise convolution 擴大單層空間混合範圍，pointwise layers 做 channel mixing。分類 head 將 pooled image-level feature 轉成已知類別 logits／probability；大 receptive field 與 global score 都不等於 tiny defect 的局部證據或 mask。

### cost_and_operating_point

鎖 variant、pretraining／weights、resolution、augmentation、regularization、optimizer、stochastic depth、export engine、precision 與 batch。成本受 pixel budget、stage width/depth、large-kernel implementation 與 runtime 支援影響；P95 必須包含 resize、tiling／aggregation、backbone、head 與後處理，不能只量 backbone forward。

### failure_boundary

大 kernel 不會補回光學上未被 sampling 的 tiny defect；pooling 或 resize 仍可能稀釋小訊號。類別 ontology、recipe／equipment、背景與光源 shift 及 OOD 會破壞 label contract。tile inference 若沒有固定 overlap、border policy 與 score aggregation，同一 die/image 可因切法不同而改變決策。

### selection_gate

在固定 ROI、已知類別穩定，希望保有 CNN deploy toolchain並評估 modern large-kernel design 時選用。固定 data、pixels、pretraining policy、augmentation、train budget、hardware、tiling／aggregation、decision unit 與 reject policy，再與 ResNet／ViT 比較 critical-class recall、calibration、OOD reject、review load 與端到端 P95。低 confidence 或 OOD gate 未通過時轉 REVIEW。

### evidence_bundle

保存 ConvNeXt variant／weights、pretraining、input resolution、resize／normalize、augmentation、regularization、optimizer、stochastic-depth、tile size／overlap／border／aggregation、label revision、lot／recipe／equipment split、confusion matrix、critical recall、calibration、OOD／failure images、端到端 P95、export engine／precision 與模型版本。

## 視覺 primitive

- `input_image`：固定 ROI 或有明確 tile contract 的 die/image，標示 pixel budget 與 tiny defect sampling 風險。
- `feature_path`：patchify-like stem、hierarchical stages、large-kernel depthwise convolution、LayerNorm、pointwise expansion/projection、residual 與 downsampling。
- `classification_or_mask_output`：pooled image/tile feature → closed-set class logits；不是定位或 mask。
- `label_contract`：版本化 known classes、variant／recipe、lot/recipe split，以及 tile-to-die/image aggregation contract。
- `failure_gate`：tiny signal loss、tile border／aggregation、ontology／recipe shift、OOD、低 confidence → REVIEW。

## 比較契約

- 比較 ID：`classification-resnet-convnext-vit`
- 版型：`D-M` 多候選矩陣。
- 固定條件：同一 input／ROI、labels、pixel budget、pretraining policy、augmentation、train budget、hardware、decision unit、tile aggregation 與 threshold／reject policy。
- 共同比較輸出：critical-class recall、calibration、OOD reject、端到端 P95、memory／throughput 與 review load；沒有共同 contract 時不得宣稱架構排名。

## 來源

- Zhuang Liu et al., “A ConvNet for the 2020s,” arXiv:2201.03545.
- `full-model-course/02-known-target-classification-segmentation.md` 的 02-07～02-10。

## 產生 gate

六個必要欄位與五個 visual primitives 已完成模型專屬遷移；可開始產生 02-07～02-10 的版本化 C／D 教學頁。成品仍須逐張通過中文可讀性、工程因果、無虛構效能數值與 manifest／QA 驗證，才能標記 approved。


<!-- wi030-model-core:start -->
## WI-030 核心做法與工作取捨

ConvNeXt把卷積網路現代化：較大視窗的depthwise卷積先讓每個通道整理周圍空間線索，再用通道混合交換資訊，搭配殘差及其他設計。分類工作仍是從影像特徵得到已知類別；它不是因名稱新就一定較省或較準。

訓練照片中十字螺絲總在藍墊、內六角總在橘墊，模型可能學到背景捷徑。把同一十字螺絲換到橘墊後，可能誤判內六角；工件本身沒有改變。

ResNet用殘差相加傳遞特徵；ConvNeXt仍以卷積作空間與通道處理；ViT讓區塊特徵互相參照。三者都可接分類頭；用相同標註、資料切分、前處理與硬體比較錯誤、耗時和記憶體，不能只看模型新舊。

需各類工作標註和未見批次測試；選預訓練權重後調整任務頭。換類別、背景或拍攝條件重新核對，不能只沿用原測試準確率。

先定義各類與未知品接手規則，讓每類跨背景拍攝，按批次切開訓練和測試。

用未見批次逐類核對真實輸入、標籤、預測及信心，列混淆矩陣與背景／反光失敗例；記錄整段耗時、記憶體與人工覆核量。教學圖的分類結果不是實測。

來源：https://arxiv.org/abs/2201.03545

版本及示意界線見工作項目 sources.md。使用者成品核准pending。
<!-- wi030-model-core:end -->

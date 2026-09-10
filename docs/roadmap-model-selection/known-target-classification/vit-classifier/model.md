# ViT classifier（`vit-classifier`）

- roadmap 分類：`known-target-classification`
- 講義對照：`02-11`～`02-14`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/vit-classifier.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
固定相機拍螺絲頭，要把十字、一字與內六角分流到不同料盒。

### 它交出什麼，也不交出什麼
已知類別與模型分數，交分流規則或人工覆核；未知產品、輪廓與3D姿態另行處理。

### 一句心智模型
ViT把影像分成區塊，編碼成帶位置資訊的tokens。自注意力讓每個區塊依其他區塊的線索更新表示，再匯整成分類結果。圖上粗細連線示意資訊關係；注意力權重不是經驗證的缺陷位置或因果解釋。

**限制：** 訓練照片中十字螺絲總在藍墊、內六角總在橘墊，模型可能學到背景捷徑。把同一十字螺絲換到橘墊後，可能誤判內六角；工件本身沒有改變。

### 換一個現場再推理
ViT分類可以把可疑工件送人覆核。另一部門希望直接取得缺陷輪廓，但像素標註成本高。

**問題：** 先交付分類覆核流程，或增加分割任務？哪些需求會改變你的決定？

**核對：** 若工作目的是先分流且人工覆核量可接受，可先交付經驗證的分類流程；若後段確實需要輪廓或定位，則要定義相應輸出與標註並驗證。注意力圖不能替代輪廓真值。比較時一起計入標註、覆核、漏分和後段量測校正成本。
<!-- topic-learning-bridge:end -->
## 模型定位

ViT classifier 將影像切成固定 patch，映射成 token sequence，加入 positional encoding 後以 Transformer encoder 的 self-attention 建立跨區域關係，最後由 class token 或 pooling 輸出 closed-set logits。它不是 detector；patchization 前未被觀測或在 patch 內被稀釋的微小訊號，attention 無法復原。

## 必要欄位

### architecture_path

固定 ROI image `H×W` → `P×P` non-overlapping patches → flatten／linear patch embeddings → class token（依實作）＋positional encoding → repeated Transformer encoder blocks（LayerNorm、multi-head self-attention、MLP、residual）→ class token／global pooling → linear head → class logits。必須鎖 model size、patch size、resolution、pretraining、positional interpolation 與 head。

### representation_or_score

representation 是保留位置資訊的 patch tokens；每層 self-attention 混合 token 間的全域關係。Token 數約由 `H/P × W/P` 決定，另視 class token 而定。分類輸出是 image/tile-level logits，不是 box、mask 或 patch 內的量測證據；attention map 也不能直接當成已驗證的缺陷邊界。

### cost_and_operating_point

鎖 patch size、resolution、model size、pretraining weights、fine-tune layers、positional interpolation、augmentation、tile strategy、precision、export engine 與 batch。更小 patch／更高 resolution 會增加 token 數及 attention memory/compute；報告需包含 token count、VRAM、端到端 P95、tile aggregation 與 review load，不能只比較 backbone 或固定輸入尺寸名稱。

### failure_boundary

Patch sampling 可能在 tokenization 前稀釋 micro defect；attention 不能復原已消失細節。小資料從頭訓練、pretraining domain mismatch、positional interpolation、tile border／aggregation、ontology／recipe shift 與 OOD 都會破壞可用性。全域 attention 或高 confidence 不等於局部證據與未知檢出保證。

### selection_gate

在已知類別穩定、長距結構關係重要且可利用合適 pretraining/foundation initialization 時評估。先做 optical/pixel observability check，再固定 data、effective pixels、patch size、pretraining policy、train budget、hardware、decision unit、tile aggregation 與 reject policy，和 ResNet／ConvNeXt 比較 critical-class recall、calibration、OOD reject、VRAM、端到端 P95 與 review load。低 confidence 或 OOD gate 未通過時轉 REVIEW。

### evidence_bundle

保存 model／patch size、weights／pretraining、input resolution、positional interpolation、fine-tune layers、augmentation、tile／aggregation、token count、VRAM、label revision、lot／recipe／equipment split、confusion matrix、critical recall、calibration、OOD／failure images、端到端 P95、runtime／precision 與模型版本。

## 視覺 primitive

- `input_image`：固定 ROI、pixel budget 與 micro-defect 尺度，顯示 patch grid 對訊號的 sampling 關係。
- `feature_path`：patchify、embedding、positional encoding、class token、Transformer encoder、self-attention／MLP residual blocks。
- `classification_or_mask_output`：class token／pooling → closed-set logits；attention map 不是 box 或 mask。
- `label_contract`：model/patch size、pretraining、resolution、position interpolation、known classes 與 reject policy。
- `failure_gate`：patch 內訊號消失、小資料 from scratch、domain／recipe shift、tile/OOD、低 confidence → REVIEW。

## 比較契約

- 比較 ID：`classification-resnet-convnext-vit`
- 版型：`D-M` 多候選矩陣。
- 固定條件：同一 input／ROI、labels、effective pixel budget、pretraining policy、augmentation、train budget、hardware、decision unit、tile aggregation 與 threshold／reject policy；不能只因都叫 224×224 就宣稱 sampling 公平。
- 共同比較輸出：critical-class recall、calibration、OOD reject、端到端 P95、VRAM／throughput 與 review load；沒有共同 contract 時不得宣稱架構排名。

## 來源

- Alexey Dosovitskiy et al., “An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale,” arXiv:2010.11929.
- `full-model-course/02-known-target-classification-segmentation.md` 的 02-11～02-14。

## 產生 gate

六個必要欄位與五個 visual primitives 已完成模型專屬遷移；可開始產生 02-11～02-14 的版本化 C／D 教學頁。成品仍須逐張通過中文可讀性、工程因果、無虛構效能數值與 manifest／QA 驗證，才能標記 approved。


<!-- wi030-model-core:start -->
## WI-030 核心做法與工作取捨

ViT把影像分成區塊，編碼成帶位置資訊的tokens。自注意力讓每個區塊依其他區塊的線索更新表示，再匯整成分類結果。圖上粗細連線示意資訊關係；注意力權重不是經驗證的缺陷位置或因果解釋。

訓練照片中十字螺絲總在藍墊、內六角總在橘墊，模型可能學到背景捷徑。把同一十字螺絲換到橘墊後，可能誤判內六角；工件本身沒有改變。

ResNet用殘差相加傳遞特徵；ConvNeXt仍以卷積作空間與通道處理；ViT讓區塊特徵互相參照。三者都可接分類頭；用相同標註、資料切分、前處理與硬體比較錯誤、耗時和記憶體，不能只看模型新舊。

需各類工作標註和未見批次測試；選預訓練權重後調整任務頭。換類別、背景或拍攝條件重新核對，不能只沿用原測試準確率。

先定義各類與未知品接手規則，讓每類跨背景拍攝，按批次切開訓練和測試。

用未見批次逐類核對真實輸入、標籤、預測及信心，列混淆矩陣與背景／反光失敗例；記錄整段耗時、記憶體與人工覆核量。教學圖的分類結果不是實測。

來源：https://arxiv.org/abs/2010.11929

版本及示意界線見工作項目 sources.md。使用者成品核准pending。
<!-- wi030-model-core:end -->

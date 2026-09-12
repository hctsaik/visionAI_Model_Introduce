# ResNet（`resnet`）

- roadmap 分類：`known-target-classification`
- 講義對照：`02-03`～`02-06`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/resnet.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
固定相機拍螺絲頭，要把十字、一字與內六角分流到不同料盒。

### 它交出什麼，也不交出什麼
已知類別與模型分數，交分流規則或人工覆核；未知產品、輪廓與3D姿態另行處理。

### 一句心智模型
ResNet讓特徵走兩條路：一路直接保留x，另一路學修正F(x)，兩路相加後繼續處理。這使較深網路較容易最佳化；最後由分類頭把特徵對應到已知螺絲類別。相加的是相容的特徵，不是兩張原始照片。

**限制：** 訓練照片中十字螺絲總在藍墊、內六角總在橘墊，模型可能學到背景捷徑。把同一十字螺絲換到橘墊後，可能誤判內六角；工件本身沒有改變。

### 換一個現場再推理
新背景讓原ResNet分類變差。你可以先擴充跨背景標註，也可以比較更深的ResNet；同時做兩者會超出本輪時間。

**問題：** 你如何用一個小檢查決定先投入哪一邊？

**核對：** 先用同工件、不同背景的保留資料找錯誤集中在哪裡。若背景切換主導錯誤，先改善資料與取像較直接；若跨背景仍有一致的細部類別混淆，可比較容量或解析度。更深網路可能有用，但殘差不自動消除背景捷徑，仍須同資料驗證。
<!-- topic-learning-bridge:end -->
## 模型定位

ResNet 是 residual CNN 分類基線，對固定 ROI 輸出已知類別的 logits。Residual block 以 `F(x) + x` 的 shortcut 保留資訊與梯度路徑，使更深的 CNN 較易最佳化；它本身不回答未知缺陷、缺陷位置或 mask 邊界。

## 必要欄位

### architecture_path

固定 ROI image → versioned resize／normalize → convolution stem → residual stages（BasicBlock 或 Bottleneck；`F(x)+x`）→ global average pooling → linear classification head → class logits。必須鎖 ResNet-18／50／101、pretraining、input pixels 與 preprocess；不同 depth 不可當成同一模型設定。

### representation_or_score

Residual stages 產生逐步降採樣的 spatial feature maps；global pooling 後得到 image-level feature vector，linear head 輸出已知類別 logits／probability。Global class score 不是局部缺陷證據，也不能直接提供 box、mask 或量測座標；top-k 與 confidence 必須連同 label contract 解讀。

### cost_and_operating_point

鎖 depth、pretraining weights、input size、augmentation、loss／class weighting、batch 與 inference preprocess。成本受 depth、pixel budget 與部署 runtime 影響；量產報告需包含端到端 P95 latency、critical-class recall、calibration、reject rate，不能只比平均 top-1。

### failure_boundary

Global pooling 可能抹去 tiny defect 訊號；背景、治具或 lot correlation 會造成 shortcut learning。新 defect、class／recipe shift、光學 sampling 改變與 OOD 影像可能仍得到高 logit，因此不能把 closed-set confidence 當成未知檢出保證，也不能由分類分數推論位置或尺寸。

### selection_gate

在 ROI 固定、類別定義穩定且需要成熟 CNN toolchain／可部署 baseline 時選用。使用 class-balanced lot／recipe split 與獨立 calibration set，固定 data、pixels、train budget、threshold policy 與 SLA，再與 ConvNeXt／ViT 比較 critical recall、calibration、OOD reject、P95 latency。低 confidence 或 OOD gate 未通過時轉 REVIEW，不可硬判 PASS／FAIL。

### evidence_bundle

保存 ResNet depth、pretraining／weights、label revision、ROI／resize／normalize、augmentation、loss／class weight、data split（lot／recipe／equipment）、confusion matrix、per-class／critical recall、calibration curve、reject threshold、OOD／failure images、P95 latency、runtime 與模型版本。

## 視覺 primitive

- `input_image`：固定 ROI 與可見 pixel budget；同時標示非固定／過小 ROI 風險。
- `feature_path`：stem → residual stages，清楚畫出 `F(x)+x` shortcut、降採樣與 global pooling。
- `classification_or_mask_output`：class logits／top-k 是 image-level 分類，不是 box 或 mask。
- `label_contract`：版本化的已知類別、lot／recipe split、class balance 與 reject policy。
- `failure_gate`：tiny defect、背景捷徑、class／recipe shift、OOD、低 confidence → REVIEW。

## 比較契約

- 比較 ID：`classification-resnet-convnext-vit`
- 版型：`D-M` 多候選矩陣。
- 固定條件：同一 input／ROI、labels、pixel budget、pretraining policy、augmentation、train budget、hardware、decision unit 與 threshold／reject policy。
- 共同比較輸出：critical-class recall、calibration、OOD reject、端到端 P95 latency 與 review load；沒有共同 contract 時不得宣稱架構排名。

## 來源

- Kaiming He et al., “Deep Residual Learning for Image Recognition,” arXiv:1512.03385.
- `full-model-course/02-known-target-classification-segmentation.md` 的 02-03～02-06。

## 產生 gate

六個必要欄位與五個 visual primitives 已完成模型專屬遷移；可開始產生 02-03～02-06 的版本化 C／D 教學頁。成品仍須逐張通過中文可讀性、工程因果、無虛構效能數值與 manifest／QA 驗證，才能標記 approved。


<!-- wi030-model-core:start -->
## WI-030 核心做法與工作取捨

ResNet讓特徵走兩條路：一路直接保留x，另一路學修正F(x)，兩路相加後繼續處理。這使較深網路較容易最佳化；最後由分類頭把特徵對應到已知螺絲類別。相加的是相容的特徵，不是兩張原始照片。

訓練照片中十字螺絲總在藍墊、內六角總在橘墊，模型可能學到背景捷徑。把同一十字螺絲換到橘墊後，可能誤判內六角；工件本身沒有改變。

ResNet用殘差相加傳遞特徵；ConvNeXt仍以卷積作空間與通道處理；ViT讓區塊特徵互相參照。三者都可接分類頭；用相同標註、資料切分、前處理與硬體比較錯誤、耗時和記憶體，不能只看模型新舊。

需各類工作標註和未見批次測試；選預訓練權重後調整任務頭。換類別、背景或拍攝條件重新核對，不能只沿用原測試準確率。

先定義各類與未知品接手規則，讓每類跨背景拍攝，按批次切開訓練和測試。

用未見批次逐類核對真實輸入、標籤、預測及信心，列混淆矩陣與背景／反光失敗例；記錄整段耗時、記憶體與人工覆核量。教學圖的分類結果不是實測。

來源：https://arxiv.org/abs/1512.03385

版本及示意界線見工作項目 sources.md。使用者成品核准pending。
<!-- wi030-model-core:end -->

<!-- wi033-engineering:start -->
## WI-033 工程圖修正

### ResNet：先把整張照片分到已知類別

沿用支架完整／刮傷兩類工作例。用有標註的整圖訓練分類器，殘差分支學相對輸入的修正；分類頭彙整特徵後交付類別分數，無法直接交付刮傷座標。圖中分數是給定示意。

整圖分類要類別標註，細傷位置不會自動交付。

來源：https://arxiv.org/abs/1512.03385

### ResNet：保留輸入，再加上學到的修正

用同位置2×2特徵教學例：x=[2,1;0,3]，F(x)=[1,0;2,-1]，相加得到[3,1;2,2]。直通路是輸入特徵而非原圖；形狀不同時需投影或其他對齊。展示殘差核心，啟用函數與其他層於正文說明，不把加法當缺陷消除。

同形狀才能逐位置相加；換形狀需先對齊。

來源：https://arxiv.org/abs/1512.03385

### ResNet：分類結果要連回原圖與標籤

推論固定裁切、resize、標準化、權重與類別順序。分類頭使用彙整特徵，不把可視化特徵圖當缺陷位置。保存分數與原圖，分批次驗漏判與誤判；全域平均會弱化某些細小線索，是否漏判仍需資料驗證。

保存類別映射與前處理，換批次後重驗誤判。

來源：https://arxiv.org/abs/1512.03385

### ResNet：背景變了，分類依據仍要成立

相同支架與缺口只改背景，檢查模型是否依背景而非工件分類。若要缺陷位置，另評分割及其像素標註成本；ResNet可當骨幹，但本分類頭不因有熱圖可視化就變成分割器。

同件換背景測捷徑，定位需求另選位置輸出。

來源：https://arxiv.org/abs/1512.03385

<!-- wi033-engineering:end -->

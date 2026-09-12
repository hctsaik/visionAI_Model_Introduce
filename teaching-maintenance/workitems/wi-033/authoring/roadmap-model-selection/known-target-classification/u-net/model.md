# U-Net（`u-net`）

- roadmap 分類：`known-target-classification`
- 講義對照：`02-19`～`02-22`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/u-net.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
要把金屬板上的彎曲焊縫從背景分出來，交給區域覆核或後續量測。

### 它交出什麼，也不交出什麼
逐像素類別與預測區域遮罩，交邊界核對或後續量測；實體尺寸需另外校正與驗證。

### 一句心智模型
U-Net先縮小特徵以整合較大範圍，再逐步上採樣恢復輸出解析度。同尺度跳接把編碼側的細節送到解碼側，與較深層線索合併，協助預測每個像素的類別。跳接傳遞特徵，並非直接把原圖當答案貼回。

**限制：** 同一條細焊縫在縮小輸入後只剩極少像素，預測遮罩可能斷裂；原始工件並沒有真的斷裂。背景細紋也可能造成誤分。

### 換一個現場再推理
完整高解析度影像能保留細焊縫，但耗時較長；切圖可聚焦局部，卻會失去部分上下文並增加拼接邊界。

**問題：** 你先測高解析度整圖，還是重疊切圖？驗收不能只看哪個指標？

**核對：** 兩者都值得用相同保留影像比較。整體形狀很重要時先保留上下文；局部細線主導且可處理拼接時可試重疊切圖。除區域重疊外，另看細線召回、斷裂、邊界偏移與完整耗時。要交毫米尺寸仍需尺度與透視校正。
<!-- topic-learning-bridge:end -->
## 模型定位

U-Net 是 encoder-decoder semantic segmentation family：contracting path 擷取 context，symmetric expanding path 搭配 same-scale skip connections 恢復 localization。它輸出每個 pixel 的 semantic logits/mask，不會原生分開 touching instances，也不是固定 checkpoint 或 calibrated metrology；必須鎖 encoder、channel width、decoder、loss、input/tiling 與 mask postprocess。

## 必要欄位

### architecture_path

固定 image/ROI → resize/normalize 或 versioned tile extraction → downsampling encoder stages → bottleneck → upsampling decoder stages＋same-scale skip concatenate → segmentation head → per-pixel class logits/probabilities → threshold/argmax → semantic mask → optional connected components／instance split／measurement rules。

### representation_or_score

Encoder 的低解析深層 features 表示較大 context，skip features 保存同尺度的高解析局部資訊；decoder fuse 後輸出 H×W×K pixel logits。Probability/threshold、output stride、upsampling、tile blending 與後處理會改變 mask 邊界；semantic connected region 不等於 object instance，也不等於物理尺寸與不確定性。

### cost_and_operating_point

鎖 encoder family/pretraining、depth、channel width、decoder blocks、input/crop/tile size、overlap、loss（Dice/BCE/CE 等）、class weights、augmentation、precision/export/engine、threshold/argmax、edge handling、blend/stitch 與 runtime。端到端 P95 包含 tile extraction、model passes、blend/stitch、inverse mapping 與 postprocess；同時報 per-class IoU/Dice、critical-region recall、boundary error、tile-seam error 與 review load。

### failure_boundary

Touching same-class instances 會合為同一 semantic region；tiny/thin/low-contrast structures 可能被 downsampling 或 interpolation 稀釋。Boundary annotation noise、class imbalance、patch leakage、tile border、insufficient context、recipe/product shift 與 inconsistent threshold 都會造成漏失、孔洞、邊界漂移或跨 tile 不連續。Raw mask 不可直接宣稱 CD、面積或尺寸量測準確。

### selection_gate

在 known semantic classes、需要 dense region mask、有一致 pixel labels，且能控制 decoder/tiling/postprocess 時選用。若任務要求天然 instance identity，改走 instance segmentation 或明確驗證模型外 split 規則。與 SegFormer 比較時固定 data split、effective pixels、crop/tile、output/mask resolution、loss/augmentation budget、engine、threshold 與 decision unit，再比較 boundary/tiny recall、P95、memory、seam error 與 review load。

### evidence_bundle

保存 exact implementation/checkpoint、encoder/pretraining、depth/width/decoder、input/crop/tile/overlap、normalization、loss/class weights、augmentation、label/ignore revision、lot/product split、threshold/argmax、blend/stitch/edge handling、postprocess、output stride/resolution、per-class IoU/Dice、critical recall、boundary/seam error、P95/memory/precision、failure images 與 calibration/repeatability/uncertainty（若進量測）。

## 視覺 primitive

- `input_image`：高解析影像／ROI，包含 thin、tiny、touching 與 tile-border semantic regions。
- `feature_path`：contracting encoder → bottleneck → symmetric expanding decoder，畫出 same-scale skip concatenate。
- `classification_or_mask_output`：pixel logits/probabilities → threshold/argmax → semantic mask；instance split 與 measurement 明確在模型外。
- `label_contract`：pixel masks、class/ignore/void、boundary policy、class balance、lot-level split 與 tile extraction revision。
- `failure_gate`：touching instances、thin/tiny、boundary noise、imbalance、patch leak、tile seam、recipe shift；metrology 另接 calibration/uncertainty Gate。

## 比較契約

- 比較 ID：`known-target-classification-family-comparison`
- 固定條件：相同 image/ROI、pixel labels/ignore、lot-level split、effective pixels、crop/tile/overlap、train budget、output resolution、hardware/engine、threshold/postprocess 與 decision unit。
- 共同比較輸出：per-class IoU/Dice、critical-region recall、boundary/tile-seam error、calibration、memory、端到端 P95、review load；不得以 semantic IoU 直接推出 instance separation 或 metrology 能力。

## 來源

- Ronneberger, Fischer, Brox, “U-Net: Convolutional Networks for Biomedical Image Segmentation,” arXiv:1505.04597（contracting path、symmetric expanding path、localization 與 augmentation）。
- `full-model-course/02-known-target-classification-segmentation.md` 的 02-19～02-22。

## 產生 gate

六個必要欄位與五個 visual primitives 已完成模型專屬遷移；可開始產生 02-19～02-22 的版本化 C/D 教學頁，逐張通過 QA 後才能 approved。


<!-- wi030-model-core:start -->
## WI-030 核心做法與工作取捨

U-Net先縮小特徵以整合較大範圍，再逐步上採樣恢復輸出解析度。同尺度跳接把編碼側的細節送到解碼側，與較深層線索合併，協助預測每個像素的類別。跳接傳遞特徵，並非直接把原圖當答案貼回。

同一條細焊縫在縮小輸入後只剩極少像素，預測遮罩可能斷裂；原始工件並沒有真的斷裂。背景細紋也可能造成誤分。

U-Net和SegFormer提供語意分割：同類像素用同類標籤，未必區分每一件。YOLO-Seg提供實例分割：每件有自己的遮罩。先決定要量區域還是逐件計數，再比較模型與標註成本。

需像素標註；固定輸入解析度、增強和切分。更改縮放或裁切要重測細線及拼接邊界；同資料比較U-Net基準與SegFormer完整成本。

先定義焊縫標註邊界和最小可見寬度，保存原圖，分開完整批次作驗證。

用獨立影像和人工核對遮罩，分開量區域重疊、細焊縫漏失及邊界偏差；需尺寸時另做相機與尺度校正。記錄解析度、裁切、拼接與整段耗時。示意遮罩不是推論。

來源：https://arxiv.org/abs/1505.04597

版本及示意界線見工作項目 sources.md。使用者成品核准pending。
<!-- wi030-model-core:end -->

<!-- wi033-engineering:start -->
## WI-033 工程圖修正

### U-Net：標出每個像素屬於哪一類

沿用板上細焊線工作例，以對齊的影像和像素類別標註訓練。收縮路徑取得上下文，擴張路徑結合對應高解析度特徵恢復定位；輸出是語意區域，不自帶校正後尺寸。

像素標註教會區域，輸出仍需回原圖核對。

來源：https://arxiv.org/abs/1505.04597

### U-Net：粗尺度找上下文，細尺度補位置

原始U-Net以crop and concatenate把編碼特徵送到匹配尺度的解碼器，並非每條skip都逐元素相加。示意省略卷積邊界尺寸，但保留同尺度配對與融合；遮罩由學習分類得到，不直接複製原圖邊緣。

跳接提供對應特徵，解碼器仍要學會融合。

來源：https://arxiv.org/abs/1505.04597

### U-Net：像素位置先映回，再談尺寸

保存ROI、resize比例、padding及類別映射，將預測映回原图再核對細線斷裂、孔洞與邊界誤差。量測另需相機校正及誤差驗證；IoU高不保證細線連通或毫米誤差達標。

記錄resize與裁切，像素遮罩不能直接當毫米。

來源：https://arxiv.org/abs/1505.04597

### U-Net：看起來像一條線，仍可能斷一格

同一細線的真值和示意候選只在中央窄處不同；大區域重疊可能掩蓋斷線。固定標註規則與解析度，比較U-Net和多尺度Transformer候選的邊界、连通、錯分及延遲，不把單一IoU排名當唯一決策。

同件檢查細線連通，不能只看大區域重疊。

來源：https://arxiv.org/abs/1505.04597

<!-- wi033-engineering:end -->

# SegFormer（`segformer`）

- roadmap 分類：`known-target-classification`
- 講義對照：`02-23`～`02-26`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/segformer.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
要把金屬板上的彎曲焊縫從背景分出來，交給區域覆核或後續量測。

### 它交出什麼，也不交出什麼
逐像素類別與預測區域遮罩，交邊界核對或後續量測；實體尺寸需另外校正與驗證。

### 一句心智模型
SegFormer的階層Transformer產生多個尺度的特徵，再以輕量MLP解碼頭對齊尺度並融合，預測每個像素的類別。較大範圍提供上下文，較細尺度保留局部線索；仍需工作標註和細小邊界驗證。

**限制：** 同一條細焊縫在縮小輸入後只剩極少像素，預測遮罩可能斷裂；原始工件並沒有真的斷裂。背景細紋也可能造成誤分。

### 換一個現場再推理
現場多數墊圈彼此分開，少數會相接。現有語意遮罩已可用，改實例分割需要新增逐件標註。

**問題：** 先用語意遮罩加連通區與人工例外，或直接建實例分割？說明可接受條件。

**核對：** 若能保證分離條件並可靠識別例外，語意遮罩加連通區可作受限方案，需驗證相接件漏計與覆核量。若必須普遍處理相接、遮擋或逐件ID，應比較實例輸出及標註成本。換SegFormer骨幹本身不會把語意類別變成實例ID。
<!-- topic-learning-bridge:end -->
## 模型定位

SegFormer 是 hierarchical Transformer encoder＋lightweight MLP decoder 的 semantic segmentation family。Encoder 產生多尺度 features，decoder 將不同 stage 的 local/global information 投影、上採樣與融合成 pixel logits。它不是 instance segmentation，也不是固定 checkpoint；必須鎖 MiT variant、pretraining、crop/resize、decode head、output/mask resolution、sliding-window setting 與 engine。

## 必要欄位

### architecture_path

固定 image/ROI → resize/crop 或 versioned tile extraction → overlapping patch embedding → hierarchical MiT stages（逐 stage 降解析度、增 channels，使用 efficient self-attention）→ four-scale feature maps → per-scale MLP projection → upsample 到共同尺度 → concatenate/fuse → segmentation head → pixel logits → argmax/threshold → semantic mask → inverse mapping/stitch。

### representation_or_score

Representation 是由多個 hierarchical stage 輸出的 multi-scale token/feature maps；MLP decoder 將 coarse global context 與較細 local detail 對齊後融合為 H×W×K pixel logits。Decoder 上採樣與較高輸出解析度不代表原生高解析邊界證據；semantic probability、IoU 與 mask confidence 也不等於 instance identity 或物理尺寸不確定性。

### cost_and_operating_point

鎖 MiT B0～B5 variant、pretraining/checkpoint、input/crop/tile size、overlapping patch embedding與 stage widths/depths、decode head、loss/class weights、augmentation、sliding-window overlap、upsample/output resolution、argmax/threshold、stitch/postprocess、precision/export/engine。端到端 P95 必須包含多 crop/tile、model passes、upsample/fuse、stitch、inverse mapping 與 postprocess；同時報 per-class IoU、critical-region recall、boundary/tile-seam error、memory 與 review load。

### failure_boundary

Output stride 與 stage downsampling 會稀釋 tiny/thin/low-contrast boundary；資料不足、boundary noise、class imbalance、crop/context 不足、tile seam、recipe/pretraining 差異與 product shift 都會造成漏失或邊界漂移。Paper recipe 或公開 mIoU 不可直接換算成 fab operating point；semantic IoU 不可推出 instance separation、CD precision 或面積量測可信度。

### selection_gate

在 known semantic classes、多尺度 context 重要、有一致 pixel labels，且 token/memory/runtime 成本可接受時選用。與 U-Net 比較時固定 data/lot split、effective pixels、crop/tile/overlap、output/mask resolution、train/augmentation budget、hardware/engine、threshold/postprocess 與 decision unit，再比較 per-class/critical recall、boundary/seam error、calibration、memory、端到端 P95 與 review load。

### evidence_bundle

保存 exact MiT variant、checkpoint/pretraining、stage/decode-head config、input/crop/tile/overlap、normalization、loss/class weights、augmentation、label/ignore revision、lot/product split、sliding-window/stitch、output resolution、argmax/threshold/postprocess、precision/export/engine、per-class IoU、critical recall、boundary/seam error、memory/P95/review load、failure images 與 calibration/repeatability/uncertainty（若進量測）。

## 視覺 primitive

- `input_image`：含 multi-scale、thin/tiny、low-contrast 與 tile-border semantic regions 的高解析影像。
- `feature_path`：overlapping patch embedding → hierarchical MiT stages／efficient self-attention → four-scale feature maps → MLP project/upsample/fuse。
- `classification_or_mask_output`：segmentation head → pixel logits → argmax/threshold → semantic mask → stitch/inverse mapping。
- `label_contract`：pixel masks、class/ignore/void、boundary policy、lot-level split、crop/tile/overlap 與 data/pretraining revision。
- `failure_gate`：stride/tiny/thin、boundary noise、class imbalance、crop context、tile seam、recipe/pretraining/product shift；metrology 另接 calibration/uncertainty Gate。

## 比較契約

- 比較 ID：`known-target-classification-family-comparison`
- 固定條件：相同 image/ROI、pixel labels/ignore、lot-level split、effective pixels、crop/tile/overlap、output/mask resolution、train/augmentation budget、hardware/engine、threshold/postprocess 與 decision unit。
- 共同比較輸出：per-class IoU、critical-region recall、boundary/tile-seam error、calibration、memory、端到端 P95、review load；不得以 paper mIoU 或 semantic mask 直接推出量產排名與 metrology 能力。

## 來源

- Xie et al., “SegFormer: Simple and Efficient Design for Semantic Segmentation with Transformers,” arXiv:2105.15203（hierarchical Transformer encoder、multi-scale features、lightweight MLP decoder）。
- `full-model-course/02-known-target-classification-segmentation.md` 的 02-23～02-26。

## 產生 gate

六個必要欄位與五個 visual primitives 已完成模型專屬遷移；可開始產生 02-23～02-26 的版本化 C/D 教學頁，逐張通過 QA 後才能 approved。


<!-- wi030-model-core:start -->
## WI-030 核心做法與工作取捨

SegFormer的階層Transformer產生多個尺度的特徵，再以輕量MLP解碼頭對齊尺度並融合，預測每個像素的類別。較大範圍提供上下文，較細尺度保留局部線索；仍需工作標註和細小邊界驗證。

同一條細焊縫在縮小輸入後只剩極少像素，預測遮罩可能斷裂；原始工件並沒有真的斷裂。背景細紋也可能造成誤分。

U-Net和SegFormer提供語意分割：同類像素用同類標籤，未必區分每一件。YOLO-Seg提供實例分割：每件有自己的遮罩。先決定要量區域還是逐件計數，再比較模型與標註成本。

需像素標註；固定輸入解析度、增強和切分。更改縮放或裁切要重測細線及拼接邊界；同資料比較U-Net基準與SegFormer完整成本。

先定義焊縫標註邊界和最小可見寬度，保存原圖，分開完整批次作驗證。

用獨立影像和人工核對遮罩，分開量區域重疊、細焊縫漏失及邊界偏差；需尺寸時另做相機與尺度校正。記錄解析度、裁切、拼接與整段耗時。示意遮罩不是推論。

來源：https://arxiv.org/abs/2105.15203

版本及示意界線見工作項目 sources.md。使用者成品核准pending。
<!-- wi030-model-core:end -->

<!-- wi033-engineering:start -->
## WI-033 工程圖修正

### SegFormer：四個尺度一起判讀每個位置

MiT分層Transformer產生四種尺度特徵；輕量MLP解碼器投影、對齊、串接和融合後輸出語意類別。它不自動給每個相同類別物件獨立身份，與實例分割區分。

多尺度補上下文，輸出仍是語意類別圖。

來源：https://arxiv.org/abs/2105.15203

### SegFormer：先對齊尺度，再融合線索

四尺度表示先用MLP統一通道維度，再對齊到同一空間尺度，串接後用MLP融合及分類。顯示同一焊線位置在各尺度的對應，不能把四幅彩格當四次獨立模型分割，也不以框取代輸出遮罩。

四路特徵共同進解碼器，不是四張遮罩投票。

來源：https://arxiv.org/abs/2105.15203

### SegFormer：解析度與細邊界一起驗

雖不依赖固定位置編碼，仍需依模型和實作處理輸入尺寸與padding，不能說任意尺寸均等好。測同一細線在不同解析度的可見性、邊界誤差與整條流程成本；不把插值出更多像素當新增觀測。

多尺度不能補回取像已消失的細線。

來源：https://arxiv.org/abs/2105.15203

### SegFormer與U-Net：共同標註才可比較

同一產品、同一像素標註規則及留出影像，兩候選各用相容前處理。比較細線連通、邊界、換產品適配及完整延遲；圖只展示機制差異，不編造候選熱圖勝負。

語意相同、標註一致，再比細節與運算代價。

來源：https://arxiv.org/abs/2105.15203

<!-- wi033-engineering:end -->

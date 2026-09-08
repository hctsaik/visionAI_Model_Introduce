# SegFormer model concept

## 一句話定位

SegFormer 是一個用於 **semantic segmentation** 的 encoder–decoder family：階層式 Mix Transformer（MiT）encoder 產生四個尺度的 feature maps，輕量 all-MLP decoder 對齊並融合它們，最後輸出每一位置的 K 類 logits。

它回答的是「每個像素屬於哪個已知語意類別」，不是天然的 instance ID、物件數量、物理尺寸或 PASS／FAIL。

## 1. 任務與 I/O contract

### 輸入

- 影像或版本化 ROI，通常表示為 `B × 3 × H × W`。
- resize、crop／tile、padding、normalization 與 color convention。
- 訓練時另有 `B × H × W` 的 pixel class labels、background、ignore index 與 boundary policy。
- MiT variant、checkpoint／pretraining、decoder 與 class mapping。

### 輸出

- segmentation logits：`B × K × h × w`，其中 `K` 是已知 semantic classes。
- logits 經 resize 與 `argmax`（互斥類別）或依契約 threshold 後，形成 semantic mask。
- 大圖 sliding-window 推論還需 overlap、stitch、inverse mapping 與 postprocess。

輸出 mask 是模型與資料契約下的候選結果。若需求是 touching objects 的分離、instance count、CD／面積量測或產線放行，必須另接合適的 pipeline 與 qualification。

## 2. 整體資料流與 shapes

以下用 `512 × 512` 輸入示意；實際 channel 數由 B0–B5 決定。

| 部位 | 典型空間尺度 | 角色 |
| --- | --- | --- |
| Input | `512 × 512` | 原始可觀測影像 |
| Stage 1 / C1 | `128 × 128`，約 `1/4` | 較細的位置線索 |
| Stage 2 / C2 | `64 × 64`，約 `1/8` | 局部結構與中程 context |
| Stage 3 / C3 | `32 × 32`，約 `1/16` | 較強語意與大範圍 context |
| Stage 4 / C4 | `16 × 16`，約 `1/32` | 最粗、最大脈絡的 representation |
| Decode logits | 約 `128 × 128`，即 `1/4` | 四尺度融合後的 K 類 logits |
| Final mask | 依框架 resize 至目標大小 | 可回映與審查的 semantic candidate |

四個 stages 是四種尺度的中間表示，不是四張彼此獨立的 mask。decoder 使用較細 feature 保留位置線索，也使用較粗 feature 取得較大 context。

## 3. Overlapping patch embedding

MiT 的第一個 stage 不是把影像切成完全不重疊的方格。官方實作使用帶 overlap 的 convolutional projection；Stage 1 常見 kernel `7`、stride `4`，後續 stages 常見 kernel `3`、stride `2`。

重疊的目的，是讓相鄰 tokens 在嵌入時看見共同像素，保留局部連續性。它不代表 thin／tiny signal 一定能穿過所有下採樣與 decoder；能否觀測仍需用有效像素、boundary error 與 failure cases 驗證。

## 4. Efficient self-attention：縮減 K／V，而不是縮減問題定義

標準 self-attention 對 token 數 `N` 的成本會隨 `N²` 增長。MiT 在 attention 內對 K／V 做 sequence reduction，再和 Q 計算 attention。可把概念寫成：

```text
Q = XWq
K = SR(X)Wk
V = SR(X)Wv
Attention(X) = softmax(QKᵀ / √d) V
```

官方四個 stages 的 `sr_ratio` 為 `8, 4, 2, 1`：高解析度 stage 縮減較多，最粗 stage 不再縮減。這個 reduction 是 attention 計算策略，不等於 final mask 的 resize，也不應被解讀成輸出責任的改變。

## 5. Mix-FFN 與 position-encoding-free 設計

MiT 的 feed-forward block 不是只有兩個 linear layers。官方實作在中間加入 `3 × 3 depthwise convolution`：

```text
Linear → 3×3 DWConv → GELU → Linear
```

DWConv 讓局部鄰域在 FFN 內交互，為 token representation 提供空間線索。SegFormer encoder 不依賴固定 positional encoding，因此改變輸入解析度時不需要對位置向量插值。

「不使用 positional encoding」不是「任意解析度都已驗證」。輸入大小改變仍會影響 context、padding、記憶體、feature statistics 與推論延遲，部署前需重做 validation。

## 6. All-MLP decoder 的精確順序

官方 decode head 可用五個動作理解：

1. **Project**：C1–C4 各自經 linear projection，轉成共同 embedding dimension。
2. **Resize**：C2–C4 上採樣至 C1 的 `H/4 × W/4` grid。
3. **Concatenate**：沿 channel 維度串接四個 features。
4. **Fuse**：用 convolutional fusion 層整合多尺度表示，並套用 normalization／activation 與 dropout。
5. **Predict**：classifier 輸出 K 類 logits。

上採樣的功能是對齊 feature grids，不會重新量到原圖中已被取像、resize 或 encoder stride 消除的物理細節。

## 7. 訓練與推論要分開畫

### 訓練

```text
image + pixel labels
→ shared preprocessing / augmentation
→ SegFormer logits
→ resize to label grid
→ segmentation loss with ignore / class policy
→ update parameters
```

資料應按 lot、wafer、產品或時間分組切分，避免相鄰 tiles 或同一工作物件洩漏到 validation。class weights、ignore index、reduce labels 與 augmentation 都是 target contract 的一部分。

### 推論

```text
image or tiles
→ same preprocessing contract
→ SegFormer logits
→ resize / argmax or threshold
→ tile stitch / inverse mapping / postprocess
→ semantic candidate + evidence
```

部署指標要涵蓋整條路徑，不能只量 backbone 或單一 crop 的 latency。

## 8. B0–B5 variant 如何選

B0–B5 共享四-stage MiT 與 decoder 思路，但 stage channels、block depths、embed dimension 與參數量不同。容量增加通常伴隨更高記憶體與 latency，且在小資料、class imbalance 或 thin boundary 上不保證單調改善。

公平比較至少固定：

- 相同 train／validation／test split 與 pixel labels。
- 相同 input／crop／tile、augmentation 與 optimization budget。
- 相同 pretraining 起點或清楚標示差異。
- 相同 decode head、output resolution、stitch、postprocess 與 engine／precision。
- 相同 decision unit 與 failure slice。

論文 benchmark 可說明架構的公開趨勢；選擇 production variant 必須再用本地資料與硬體驗證。

## 9. 比較模型時看輸出責任

| Family | 主要表示 | 典型優勢 | 需要特別驗證 |
| --- | --- | --- | --- |
| U-Net | CNN encoder–decoder + same-scale skips | 結構直接、低資料 baseline 常有價值 | boundary、touching instances、tile policy |
| DeepLabV3+ | dilated CNN + ASPP + decoder | CNN 的多尺度 context | dilation、output stride、thin detail |
| Plain ViT / SETR 類 | 較平坦 token representation + segmentation decoder | 全局 attention | 高解析度成本、多尺度細節 |
| SegFormer | hierarchical MiT + all-MLP decoder | 四尺度 context 與簡潔 decoder | effective pixels、memory、seam、shift |
| YOLO instance segmentation | box／class + per-instance mask | 已知 instances 的偵測與分離 | NMS、mask overlap、instance labels |

這張表不是排名。若需求是已知 semantic classes 且 local／global context 都重要，可比較 SegFormer；若主要責任是 instance identity 或 measurement truth，應轉向對應流程。

## 10. AOI qualification 與 HOLD gate

### 建議證據

- per-class IoU 與 critical-region recall，而非只看平均 mIoU。
- boundary error、tile-seam error、hole／fragment failure slices。
- lot／產品／設備／時間／pretraining shift 的分層結果。
- calibration、記憶體、吞吐量、端到端 P95 與人工 review load。
- 保存 raw ROI、labels、logits、mask、版本、tile recipe 與 postprocess，讓錯誤可重播。

### 應 HOLD 的情況

- thin／tiny 訊號在有效像素或輸出 stride 上不可觀測。
- class、ignore、boundary labels 或 crop／tile／stitch 未版本化。
- semantic mask 被要求直接當成 instance identity、尺寸真值或自動放行證據。
- 新 lot、產品、取像或 pretraining domain shift 尚未通過 gate。
- latency、memory、boundary／seam 或 review load 不達接受條件。

## 11. 來源與使用邊界

- [SegFormer paper](https://arxiv.org/abs/2105.15203)：架構、B0–B5 與公開實驗的第一來源。
- [NVlabs official repository](https://github.com/NVlabs/SegFormer)：官方訓練／評估程式、models 與 repository license。該 repository 的 license 限定於非商業研究與評估；商業使用需另行確認授權。
- [Official MiT backbone](https://github.com/NVlabs/SegFormer/blob/master/mmseg/models/backbones/mix_transformer.py)：overlap patch、SR ratios、Mix-FFN 與 variants 的實作依據。
- [Official SegFormer decode head](https://github.com/NVlabs/SegFormer/blob/master/mmseg/models/decode_heads/segformer_head.py)：projection、resize、concatenate、fuse 與 predict 的實作依據。
- [Hugging Face SegFormer documentation](https://huggingface.co/docs/transformers/model_doc/segformer)：前處理、label handling、logits shape 與推論介面參考。

公開論文與程式碼支援「模型如何設計與在公開設定如何表現」；它們不直接支援特定產線的 accuracy、measurement uncertainty、runtime 或 release decision。這些主張必須由本地 qualification 建立。

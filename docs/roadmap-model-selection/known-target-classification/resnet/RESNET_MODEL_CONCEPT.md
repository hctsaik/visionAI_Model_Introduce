# ResNet 完整模型概念

## 一句話定位

ResNet 是使用殘差連接（residual connection）的卷積神經網路。對本課程的工業 AOI 範例而言，它接收一張規格固定的 ROI，輸出預先定義類別的 image-level logits；它不會自然產生缺陷位置、框、輪廓，也不保證能識別訓練類別之外的新異常。

## 1. 先定義任務與輸出責任

分類器的資料契約至少包含：ROI 座標、resize、normalization、類別表、ignore／reject 規則、資料切分方式與模型權重版本。輸入契約一旦改變，即使網路仍叫 ResNet，實際系統也已不是同一個模型版本。

標準分類頭的原生輸出是每個已知類別的 logits。softmax 可以把 logits 正規化為相對分數，但高 softmax 不等於「影像一定屬於某個已知類別」，更不等於「沒有未知缺陷」。框、mask、尺寸與根因都不是 ResNet 分類頭的原生責任。

## 2. 殘差塊為什麼是 `F(x) + x`

一般堆疊層直接學習目標映射；殘差塊改為讓卷積分支學習殘差 `F(x)`，再與 shortcut 傳來的 `x` 相加：

`y = F(x, W) + x`

當輸入與輸出 shape 相同，可使用 identity shortcut。若 stage 切換造成空間尺寸或通道數改變，則要使用 projection shortcut（通常是 `1×1` convolution，並可能帶 stride）對齊 shape 後才能相加。shortcut 的核心價值是建立較直接的訊號與梯度路徑，讓深層網路更容易最佳化；它不是缺陷殘差圖，也不是自動保留微小缺陷的保證。

## 3. BasicBlock、Bottleneck 與 stage shape

ResNet-18／34 使用 BasicBlock，主要卷積路徑為兩個 `3×3` convolution。ResNet-50／101／152 使用 Bottleneck：`1×1` 降通道、`3×3` 做空間處理、`1×1` 擴通道，輸出 expansion 為 4。

以常見的 `224×224` 輸入為例，stem 後進入四個 stages，空間尺寸大致依序為 `56×56`、`28×28`、`14×14`、`7×7`。ResNet-18 的 stage 輸出通道通常是 `64/128/256/512`；ResNet-50 因 Bottleneck expansion，通常是 `256/512/1024/2048`。最後經 global average pooling 形成一個 image-level feature vector，再由 linear head 輸出 class logits。

## 4. 訓練與推論不是同一條狀態路徑

訓練時會使用標籤、augmentation、loss 與 optimizer 更新權重。BatchNorm 在 training mode 以目前 mini-batch 的統計量正規化，並更新 running mean／variance。推論時應切到 evaluation mode，使用保存的 running statistics，不再更新它們。

若推論服務誤留在 training mode，或量產影像分布與訓練資料差異太大，輸出會受到 batch 組成與統計偏移影響。因此權重版本之外，也必須記錄 preprocess、model mode、BatchNorm 狀態及框架版本。

## 5. Global pooling 帶來的能力與盲點

Global average pooling 能把每個 channel 的空間 feature map 壓成單一數值，降低參數量並形成穩定的 image-level representation。代價是空間位置被彙整：若缺陷只佔極少像素，或 optics／resize 先把訊號抹平，微小局部變化可能被大面積正常背景稀釋。

CAM／Grad-CAM 可以做事後解釋，但它不是分類模型原生的精確定位輸出，也不應直接當作量測 mask。若任務要求找位置、輪廓或尺寸，應重新檢查 ROI crop、有效像素數，並比較 detector、segmentation 或 anomaly detection。

## 6. Softmax、校正與 OOD review

softmax 只描述模型在既有輸出類別間的相對偏好。量產決策需要獨立 calibration set，檢查 reliability／ECE、critical-class recall、混淆矩陣與 threshold。對低信心、類別衝突、分布偏移或 OOD 樣本，系統應有 reject／REVIEW 路徑，而不是強迫輸出 PASS 或 FAIL。

校正方法（例如 temperature scaling）只能改善「分數與正確率是否相符」，不能創造未知類別知識；OOD score 也必須在真實 lot、recipe、equipment 與 failure image 上驗證。

## 7. 深度、成本與公平比較

ResNet-18／34 較輕，適合快速 baseline；ResNet-50 是常見的 Bottleneck 基準；101／152 更深，但不保證在特定 AOI 任務更好。比較必須固定 pixels、labels、split、augmentation、pretraining policy、threshold 與硬體，再共同量測 critical recall、calibration、OOD／reject、P95 latency、記憶體與人工 review load。

較深模型若只提升平均 top-1，卻讓關鍵缺陷 recall、校正或 latency 變差，不應直接升級。

## 8. ResNet、ConvNeXt、ViT 怎麼選

- ResNet：成熟、容易訓練、工具鏈完整，適合作為已知類別分類 baseline。
- ConvNeXt：仍是 ConvNet，但使用較現代化的 large-kernel、depthwise 與 channel-mixing 設計；應在相同資料與成本下比較。
- ViT：以 patch tokens 與 self-attention 建模；資料量、pretraining、解析度與 latency 條件不同時，不能只比較模型名稱。

若輸出責任仍是固定 ROI 的已知類別 logits，ResNet 是合理起點。若要求位置、輪廓、未知異常或 tiny-defect observability，應先改任務與證據契約，而不是只把 backbone 換深。

## 量產證據清單

1. ROI、resize、normalization、類別表與權重 checksum。
2. lot／recipe／equipment 分組切分，避免近重複影像洩漏。
3. per-class confusion matrix 與 critical-class recall。
4. calibration curve、threshold、reject rate 與 OOD／shift 測試。
5. failure images、tiny-defect 有效像素與必要的定位模型比較。
6. P50／P95 latency、記憶體、batch size、runtime 與硬體版本。
7. 人工 review load、回復策略與監控漂移條件。

## 主要來源

- Kaiming He et al., [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385).
- PyTorch Vision, [official ResNet implementation](https://github.com/pytorch/vision/blob/main/torchvision/models/resnet.py).
- Hugging Face, [ResNet model documentation](https://huggingface.co/docs/transformers/model_doc/resnet).
- Chuan Guo et al., [On Calibration of Modern Neural Networks](https://arxiv.org/abs/1706.04599).
- Dan Hendrycks and Kevin Gimpel, [A Baseline for Detecting Misclassified and Out-of-Distribution Examples](https://arxiv.org/abs/1610.02136).
- Ramprasaath Selvaraju et al., [Grad-CAM](https://arxiv.org/abs/1610.02391).


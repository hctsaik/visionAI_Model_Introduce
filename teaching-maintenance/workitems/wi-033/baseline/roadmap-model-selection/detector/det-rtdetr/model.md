# RT-DETR（`det-rtdetr`）

- roadmap 分類：`detector`
- 講義對照：`03-06`～`03-09`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/det-rtdetr.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
同一綠色電路板上，左側 A 與右側 B 是兩個電阻；想知道在哪裡、有幾件，並保留原圖供覆核。

### 它交出什麼，也不交出什麼
框可支援計數與裁出局部；還需驗證漏件、重複與誤框，不直接提供缺陷真值、精密輪廓或實體尺寸。

### 一句心智模型
Dense框通常要整理重複；DETR以集合預測減少對NMS的依賴，但全尺度Transformer計算昂貴。RT-DETR把尺度內互動和跨尺度融合分開，並選較好的初始queries，讓集合式偵測更適合即時工作。

**限制：** 準備一致框標註與真實密集／小物驗證集。換產品或decoder深度後，同時量漏件、重複、前後處理P95及記憶體；無NMS不等於無門檻或零重複。

### 換一個現場再推理
同一模型減少解碼層後符合節拍；較小電阻和遮擋位置的漏件卻增加。部署團隊也已有 YOLO 工具鏈。

**問題：** 恢復解碼層、提高取像解析度，或比較 YOLO，如何做有條件的選擇？

**核對：** 固定資料、硬體與漏件容許量，比不同解碼深度、取像條件和 YOLO 基準的漏件、重複、端到端延遲及人工覆核。恢復層數可能省去返工，但提高解析度會增加運算；不能只以無 NMS 判定較快。兩者皆需要類別框標註，換產品需核對重訓與門檻；要輪廓則另選分割能力。
<!-- topic-learning-bridge:end -->
## 模型定位

RT-DETR 是 real-time-oriented DETR-family set detector。它以 efficient hybrid encoder 處理 multi-scale features，選出高品質 initial object queries，再由可調 decoder layers 輸出 box/class set。調整 decoder depth 可形成 speed–quality operating points，但論文 FPS 不等於產線 SLA。

## 必要欄位

### architecture_path

固定 image/ROI → versioned resize/padding → backbone multi-scale features → efficient hybrid encoder（intra-scale interaction＋cross-scale fusion）→ uncertainty-minimal query selection → object queries＋reference points → configurable decoder layers → class/box set → inverse mapping／runtime-specified postprocess → boxes/ROI crops。

### representation_or_score

Representation 包含 multi-scale encoded features 與固定容量 object queries；每個 query 經 decoder 與 image features 互動並預測 box/class。訓練以 bipartite assignment/set loss 建立一對一 target responsibility；不是 dense feature-location candidates。輸出 set 仍須校準、座標回映與 runtime 驗證。

### cost_and_operating_point

鎖 implementation/variant、backbone、encoder、query count/selection、decoder layers、input、training schedule、matching/loss、precision、export engine、batch 與 postprocess。Decoder depth 是 operating knob；每個 depth/export/runtime 都要分別量 camera-to-PLC P95、VRAM、critical-size recall、false HOLD 與 review load。

### failure_boundary

小物欠採樣、query capacity 不足、密集重疊、export operator/fusion 差異、decoder-depth 改動、domain/taxonomy shift 與 OOD 都可能造成 miss 或錯類。NMS-light/end-to-end 不代表沒有 postprocess contract，也不能把 paper benchmark FPS 外推到 camera-to-PLC SLA。

### selection_gate

在 closed-set box task、想評估 NMS-light query detector 且需要 decoder-depth speed–quality 調節時選用。固定 labels/ignore zones、effective pixels、train budget、hardware、decision unit、threshold/postprocess，再與 YOLO/DINO detector比較 critical-size recall、dense-overlap behavior、calibration、false HOLD、camera-to-PLC P95、VRAM 與 review load。Gate 未通過時 HOLD/REVIEW。

### evidence_bundle

保存 implementation/variant、weights、backbone/encoder、query count/selection、decoder layers、input/padding、matching/loss、training schedule、label/ignore revision、lot/recipe split、export graph/operators、runtime/precision、critical-size recall、overlap misses、calibration、camera-to-PLC P95、VRAM、failure images 與每個 operating point。

## 視覺 primitive

- `input_roi`：不同尺寸、密度與邊界位置的 known defects。
- `feature_path`：backbone multi-scale features → hybrid encoder → query selection → decoder layers。
- `candidate_or_query`：selected object queries/reference points；不可畫成 dense grid candidates。
- `assignment_or_matching`：bipartite assignment/set loss 的一對一 target responsibility。
- `box_output`：query set → classes/boxes → inverse mapping/ROI crops。
- `runtime_gate`：decoder-depth operating points、export/runtime、camera-to-PLC P95、small/overlap/OOD → HOLD/REVIEW。

## 比較契約

- 比較 ID：`det-dino-deformable-rtdetr-dense-matrix`
- 固定條件：相同 image/ROI、boxes/ignore zones、effective pixels、train budget、hardware、decision unit、threshold/postprocess 與 output capacity。
- 共同比較輸出：critical-size recall、false alarms/false HOLD、overlap misses、calibration、camera-to-PLC P95、VRAM/throughput 與 review load；不得以 paper FPS 或不同 export stack 排名。

## 來源

- Yian Zhao et al., “DETRs Beat YOLOs on Real-time Object Detection,” arXiv:2304.08069。
- `full-model-course/03-detectors-and-open-vocabulary.md` 的 03-06～03-09。

## 產生 gate

六個必要欄位與六個 visual primitives 已完成模型專屬遷移；可開始產生 03-06～03-09 的版本化 C/D 教學頁，逐張通過 QA 後才能 approved。

## D01 核心主線與來源補正

此節是2026-09-06本輪主線的補正；舊例若只展示部分路徑，不可據此當作模型全部能力。

Dense框通常要整理重複；DETR以集合預測減少對NMS的依賴，但全尺度Transformer計算昂貴。RT-DETR把尺度內互動和跨尺度融合分開，並選較好的初始queries，讓集合式偵測更適合即時工作。

**高效編碼，分開兩種資訊交換**：Hybrid encoder在高層特徵做尺度內注意力，再用卷積式跨尺度融合傳遞細節與脈絡，避免在所有細格上做昂貴互動。省哪一段必須說清楚，不能只因叫real-time就保證本站節拍。

**Query是一個逐步修正的物件假設**：從encoder候選選出有助分類和定位的起點；decoder透過影像證據更新queries及框。圖只畫三個query，實際數量依設定；query不是一種固定類別，也不等於已找到物件。

**一對一監督，訓練時分配責任**：訓練用匹配使不同預測對應不同真值，未匹配者學不輸出物件。推論不拿GT匹配，也不靠傳統NMS去重；仍需分數篩選、回映和覆核。decoder層數可調，但速度與漏件仍須一起量。

自測：拿掉訓練的一對一責任分配，卻仍要求推論不用NMS，為什麼不能只靠query數量少就保證不重複？

解釋：多個query仍可能指向同一件；有限數量不等於彼此分工。集合監督讓不同預測學習不同物件及無物件責任。這是作用解釋，實際移除訓練約束的效果需重新訓練驗證，不是改一個推論開關就得到公平比較。

工作接法：準備一致框標註與真實密集／小物驗證集。換產品或decoder深度後，同時量漏件、重複、前後處理P95及記憶體；無NMS不等於無門檻或零重複。

[原論文／官方文件](https://arxiv.org/abs/2304.08069)。D01核心與反例圖為既有素材加受控設定，沒有新模型推論。

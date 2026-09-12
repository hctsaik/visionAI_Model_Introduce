# YOLO dense detector（`det-yolo-dense`）

- roadmap 分類：`detector`
- 講義對照：`03-02`～`03-05`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/det-yolo-dense.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
同一綠色電路板上，左側 A 與右側 B 是兩個電阻；想知道在哪裡、有幾件，並保留原圖供覆核。

### 它交出什麼，也不交出什麼
框可支援計數與裁出局部；還需驗證漏件、重複與誤框，不直接提供缺陷真值、精密輪廓或實體尺寸。

### 一句心智模型
整圖分類只回答有什麼，產線還要知道在哪裡。這裡用YOLOv8式dense detector說明：共享全圖特徵，讓多尺度的許多位置同時提出框與類別，再整理成可覆核的候選，避免逐一裁出區域後重跑整個分類流程。

**限制：** 準備目標類別框標註、遮擋與小物樣本；回映候選裁圖供覆核。換產品要查類別與像素，必要時重訓；門檻改動重測漏件、重複及端到端P95。

### 換一個現場再推理
原流程在稀疏板上穩定，新板元件更靠近；保留的框有些跨到鄰件，產線又要求縮短延遲。

**問題：** 先放寬 NMS、改善像素與標註，或比較 RT-DETR，你會怎麼安排驗證？

**核對：** 先對回原圖區分框太寬與真正重複；NMS 不會修框。可比較抑制設定、取像／訓練改善及 RT-DETR，但用同一密集小物驗證集記漏件、重複、誤框與端到端時間。既有部署成熟可保留 YOLO 作基準；RT-DETR 省去 NMS 仍不保證零漏件。只有正常板也能標元件框，卻不能因此宣稱可找未知缺陷。
<!-- topic-learning-bridge:end -->
## 模型定位

YOLO 是 dense one-stage detector family：在多尺度 feature locations 上直接產生已知類別的 box/class/objectness candidates，再經版本專屬 decode 與 NMS 形成 boxes。`YOLO` 不是單一模型；產線必須鎖 exact version、backbone/neck/head、assignment、decode、NMS 與 export runtime。

## 必要欄位

### architecture_path

固定 image／ROI → versioned resize／letterbox → CNN backbone → FPN/PAN-like multi-scale neck（依版本）→ multi-scale dense detection heads → box/class/objectness candidates（依版本定義）→ decode → confidence/class filtering → NMS（或版本指定後處理）→ inverse mapping 到原座標 → boxes／ROI crops。

### representation_or_score

representation 是各 stride／feature location 的 dense candidates；每個 candidate 帶版本定義的 box regression 與 class/objectness signal。最終 confidence 的組合方式、anchor-based/anchor-free parameterization、assignment 與 NMS 都依實作而異，不能跨版本直接比較 raw score。輸出是 box 與已知 class，不是 mask、未知缺陷保證或物理尺寸。

### cost_and_operating_point

鎖 version／variant、backbone/neck/head、input/letterbox、stride、assignment、loss、decode、confidence/class thresholds、NMS IoU/class policy、max detections、tiling、precision、export engine 與 batch。端到端 P95 必須包含 preprocess、model、decode/NMS、inverse mapping、tile merge 與 box-to-ROI crop；同時報 critical-size bins、recall、false alarms、duplicate/missed overlap 與 review load。

### failure_boundary

Tiny object 在 optics、resize 或高 stride feature 上欠採樣時無法由 detector 補回；密集重疊、NMS suppression、tile border、label/ignore-zone 不一致、class/taxonomy drift、未知類與 domain shift 都會造成 miss、duplicate 或錯類。高 objectness/confidence 不等於未知缺陷檢出或尺寸量測可信。

### selection_gate

在已知 defect 類別、需要 box/ROI、資料可提供一致 box labels 且需成熟部署 baseline 時選用。先驗證 pixel/critical-size observability，再固定 data、pixels、labels/ignore zones、assignment、threshold/NMS、hardware、tiling 與 decision unit，和 RT-DETR／DINO detector 比較 critical-size recall、dense-overlap behavior、calibration、端到端 P95 與 review load。Gate 未通過時 HOLD/REVIEW，不可因速度或單一 mAP 放行。

### evidence_bundle

保存 exact YOLO version/variant、weights、backbone/neck/head、input/letterbox、stride、assignment/loss、decode、threshold/NMS、tile/merge、label revision/ignore zones、lot/recipe/equipment split、size-bin recall、per-class confusion、duplicate/miss cases、calibration、端到端 P95、runtime/precision 與失敗影像。

## 視覺 primitive

- `input_roi`：含不同尺寸、密度、邊界位置的已知 defect；標示 pixel observability 與 letterbox/tile contract。
- `feature_path`：CNN backbone → FPN/PAN-like multi-scale neck → dense heads，清楚顯示多 stride feature maps。
- `candidate_or_query`：每個 feature location 產生 dense box/class/objectness candidates；不是 object queries。
- `assignment_or_matching`：訓練 assignment、positive/negative/ignore 與版本專屬 losses；不得畫成 Hungarian set matching。
- `box_output`：decode/filter/NMS/inverse mapping → known-class boxes/ROI crops。
- `runtime_gate`：critical-size recall、overlap/NMS、false alarm、端到端 P95、未知/OOD → HOLD/REVIEW。

## 比較契約

- 比較 ID：`det-dense-vs-original-detr`
- 固定條件：同一 image/ROI、box labels/ignore zones、effective pixels、train budget、hardware、decision unit、threshold policy、tile merge 與 output cap。
- 共同比較輸出：critical-size recall、precision/false alarms、dense-overlap duplicates/misses、calibration、端到端 P95、memory/throughput 與 review load；不以不同版本、不同 NMS 或不同像素的公開 mAP 排名。

## 來源

- Joseph Redmon and Ali Farhadi, “YOLOv3: An Incremental Improvement,” arXiv:1804.02767，作為 multi-scale dense YOLO family 的來源錨點；實際交付仍必須鎖指定 YOLO implementation。
- `full-model-course/03-detectors-and-open-vocabulary.md` 的 03-02～03-05。

## 產生 gate

六個必要欄位與六個 visual primitives 已完成模型專屬遷移；可開始產生 03-02～03-05 的版本化 C／D 教學頁。成品仍須逐張通過中文可讀性、工程因果、無虛構效能數值與 manifest／QA 驗證，才能標記 approved。

## D01 核心主線與來源補正

此節是2026-09-06本輪主線的補正；舊例若只展示部分路徑，不可據此當作模型全部能力。

整圖分類只回答有什麼，產線還要知道在哪裡。這裡用YOLOv8式dense detector說明：共享全圖特徵，讓多尺度的許多位置同時提出框與類別，再整理成可覆核的候選，避免逐一裁出區域後重跑整個分類流程。

**共享特徵，多尺度共同提案**：骨幹與neck形成不同解析度的特徵，dense head在各位置預測框和已知類別。細尺度不只負責小物，粗尺度也不是固定類別；同一件可能被多處提出。

**框是學得的位置，不是格子本身**：格點是提出預測的參考位置，回歸與解碼產生不同大小的框。YOLOv8採anchor-free方式；其他YOLO版本的anchor、頭與後處理可能不同。

**整理重複，才能接到計數與覆核**：此路徑用分數篩選與NMS處理重複框，再回映原圖。NMS可能壓掉真實相鄰件；一階段也不代表沒有後處理，更不代表所有YOLO都使用NMS。

自測：同一元件有三個高分重疊框，拿掉NMS後直接把框數當件數，會發生什麼？

解釋：可能把一件算成三件。Dense位置可對同一物件重複提案；NMS用分數和重疊度保留代表框。但真實重疊物也可能被錯刪，要分別檢查重複與漏件，不能只追求框少。

工作接法：準備目標類別框標註、遮擋與小物樣本；回映候選裁圖供覆核。換產品要查類別與像素，必要時重訓；門檻改動重測漏件、重複及端到端P95。

[原論文／官方文件](https://docs.ultralytics.com/models/yolov8/)。D01核心與反例圖為既有素材加受控設定，沒有新模型推論。

<!-- wi033-engineering:start -->
## WI-033 工程圖修正

### YOLOv8式：從有標註的物件學出框

同PCB電阻A103/B272皆標resistor框；YOLOv8式骨幹與neck融合多尺度特徵，head預測類別與框，候選經門檻及NMS整理。輸出是影像框與類別，不是輪廓或物理尺寸；格位只示意候選位置。

框與類別來自訓練，不能用熱點代替框。

來源：https://docs.ultralytics.com/models/yolov8/

### YOLOv8式：候選重複，按分數去重

同一PCB有103與272兩顆電阻；A有三個重複候選，分數0.93/0.87/0.76，B為0.91。教學例採同類別NMS，A的候選IoU超過0.5，因此依分數保留A0.93與B0.91。門檻和分數為給定算例，不是模型推論。這裡限定YOLOv8式密集偵測，不推廣到所有YOLO版本。

NMS整理重複框，最後仍要回原圖查漏件。

來源：https://docs.ultralytics.com/models/yolov8/

### YOLO：去重設定也屬於交付條件

保留resize/letterbox映射、類別順序、權重、分數與IoU門檻。還原原圖座標後逐件驗漏框、重複與定位誤差，時間包括前後處理。圖中框分數為教學例，不是當前推論。

模型、前處理與門檻一起固定，再驗漏件。

來源：https://docs.ultralytics.com/models/yolov8/

### YOLO與RT-DETR：同一PCB比較交付

共同任務與硬體下，各用相容前處理與已驗證門檻，比較漏框、重複框、定位、記憶體及端到端時間。RT-DETR省NMS不保證本機更快；YOLOv8式作合理可部署基準。

比較逐件錯誤與完整延遲，不只看有無NMS。

來源：https://docs.ultralytics.com/models/yolov8/

<!-- wi033-engineering:end -->

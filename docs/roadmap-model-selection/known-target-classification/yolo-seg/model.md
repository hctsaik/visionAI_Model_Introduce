# YOLO-Seg（`yolo-seg`）

- roadmap 分類：`known-target-classification`
- 講義對照：`02-15`～`02-18`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/yolo-seg.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
輸送帶有兩個同類墊圈，需要分開每一件再計數，不能只知道哪些像素是墊圈。

### 它交出什麼，也不交出什麼
每件框、類別與獨立遮罩，供逐件核對和計數；A/B是實例ID，不代表不同產品類別或跨影格身分。

### 一句心智模型
以YOLOv8-seg機制為例，共享特徵產生一組原型遮罩，偵測分支為每件預測框、類別及遮罩係數。每件係數組合共享原型，再依框處理成該件遮罩。共享原型不是一張完整墊圈答案；兩件同類也要有分開的實例輸出。

**限制：** 兩個墊圈稍微重疊，模型可能只交出一件遮罩。原圖仍有兩件；人工圈出的漏件區不是模型的第二個偵測。

### 換一個現場再推理
兩個相接墊圈常只被算成一件。可增加重疊標註訓練，也可用分料或調整視角讓兩件更容易看清。

**問題：** 你會先做哪一項小試驗？何時保留兩者一起做？

**核對：** 先檢查人是否能從原圖穩定分辨兩件。可見線索足夠而資料不足時先補重疊樣本；遮擋讓身份難辨時改善分料／視角更直接。兩者都有問題可合用，但各自量成本與效益。驗證逐件召回、錯誤合併／切分、計數誤差和節拍，面積估數只能作另行驗證的受限方案。
<!-- topic-learning-bridge:end -->
## 模型定位

YOLO-Seg 是 YOLO family 的 closed-set instance segmentation pipeline：每個已知 instance 輸出 box、class/confidence 與自己的 mask/contour。它不是 semantic segmentation，也不是 calibrated metrology；必須鎖 exact version、backbone/neck、box/class head、prototype/mask head、NMS、mask compose/threshold/rescale 與 runtime。

## 必要欄位

### architecture_path

固定 image/ROI → versioned resize/letterbox → CNN backbone/neck → dense box/class head＋per-instance mask coefficients → prototype mask basis → decode/filter/NMS → coefficient×prototypes compose → box crop／mask threshold → inverse rescale 到原座標 → per-instance boxes/classes/masks。

### representation_or_score

Representation 同時包含 dense box/class candidates、共享 prototype masks 與每個 instance 的 mask coefficients；組合後才形成 object-level binary mask/contour。Mask resolution、crop、threshold、rescale 與 overlap policy 直接改變邊界；box/mask confidence 不等於物理尺寸不確定性。

### cost_and_operating_point

鎖 version/variant、weights、input/letterbox、stride、box/mask head、prototype resolution/count（依實作）、assignment/loss、NMS、mask compose/crop/threshold/rescale、tile/merge、precision/export/runtime。端到端 P95 包含 preprocess、model、decode/NMS、prototype compose、inverse mapping 與 instance aggregation；同時報 box recall、tiny-instance recall、boundary error、overlap errors 與 review load。

### failure_boundary

細邊界、tiny/low-contrast instance、低解析 prototype/stride、密集重疊與 NMS、tile border、mask annotation/ignore-zone 不一致、class/taxonomy shift 與 OOD 都會造成 mask 漏失、合併、破碎或錯類。Mask 可做 ROI/後處理候選，但不能直接宣稱 CD、面積或尺寸量測準確。

### selection_gate

在 known classes、需要 instance-level Box＋輪廓且有一致 instance masks/overlap rules 時選用。固定 data、effective pixels、labels/ignore/overlap、mask resolution/threshold、NMS、hardware、decision unit 與 runtime，再與 U-Net/SegFormer 等共同輸出比較 boundary/tiny recall、calibration、P95 與 review load。若要 metrology，必須接 calibration、repeatability 與 uncertainty Gate。

### evidence_bundle

保存 exact version/variant、weights、backbone/neck/heads、input/letterbox、prototype/mask config、assignment/loss、NMS、mask threshold/crop/rescale、tile/merge、label/ignore/overlap revision、product/ROI split、box/tiny recall、boundary/overlap errors、calibration、P95、runtime/precision 與 failure images。

## 視覺 primitive

- `input_image`：含不同 size、細邊界、重疊與 tile-border instances 的影像。
- `feature_path`：backbone/neck → dense box/class head＋mask coefficients；prototype mask branch。
- `classification_or_mask_output`：decode/NMS＋coefficient×prototypes＋crop/threshold/rescale → per-instance box/class/mask。
- `label_contract`：instance polygons/masks、class、ignore zones、overlap order 與版本。
- `failure_gate`：tiny/boundary/overlap/stride/tile/annotation/OOD；metrology 需另接 uncertainty Gate。

## 比較契約

- 比較 ID：`known-target-classification-family-comparison`
- 固定條件：相同 image/ROI、instance labels/ignore/overlap、effective pixels、train budget、hardware、decision unit、mask threshold/postprocess。
- 共同比較輸出：instance recall、boundary error、tiny/overlap errors、calibration、端到端 P95、review load；量測另報 calibration/repeatability/uncertainty，不以 mask mAP 直接推出尺寸能力。

## 來源

- Ultralytics official Instance Segmentation documentation（輸出為每個 instance 的 masks/contours、class/confidence 與 boxes；實際交付仍鎖指定 release）。
- `full-model-course/02-known-target-classification-segmentation.md` 的 02-15～02-18。

## 產生 gate

六個必要欄位與五個 visual primitives 已完成模型專屬遷移；可開始產生 02-15～02-18 的版本化 C/D 教學頁，逐張通過 QA 後才能 approved。


<!-- wi030-model-core:start -->
## WI-030 核心做法與工作取捨

以YOLOv8-seg機制為例，共享特徵產生一組原型遮罩，偵測分支為每件預測框、類別及遮罩係數。每件係數組合共享原型，再依框處理成該件遮罩。共享原型不是一張完整墊圈答案；兩件同類也要有分開的實例輸出。

兩個墊圈稍微重疊，模型可能只交出一件遮罩。原圖仍有兩件；人工圈出的漏件區不是模型的第二個偵測。

U-Net和SegFormer提供語意分割：同類像素用同類標籤，未必區分每一件。YOLO-Seg提供實例分割：每件有自己的遮罩。先決定要量區域還是逐件計數，再比較模型與標註成本。

需每件實例標註和相應版本權重；本課以YOLOv8-seg為例，不泛化聲稱所有YOLO版本都相同。固定解析度、門檻及後處理，測每件漏檢、重疊和推論成本。

先決定遮擋物件如何標註與計數，收單件、相鄰、重疊和空畫面，分開批次驗證。

保存真實原圖與逐件標註，量物件召回、錯誤合併／切分、遮罩品質和計數誤差；孔洞保留需求另驗，示意圖不是模型結果。

來源：https://github.com/ultralytics/ultralytics/blob/v8.3.0/ultralytics/nn/modules/head.py

版本及示意界線見工作項目 sources.md。使用者成品核准pending。
<!-- wi030-model-core:end -->

<!-- wi033-engineering:start -->
## WI-033 工程圖修正

### YOLO-Seg：同類零件也要各有一張遮罩

以YOLOv8式prototype和mask coefficients路徑說明。訓練需各實例的類別與輪廓，推論保留各物件框、分數和實例遮罩；圖中甲乙只是這張影像的實例，不是跨影格追蹤ID。

每件有框、類別與遮罩，身份只屬當前影像。

來源：https://docs.ultralytics.com/reference/nn/modules/head/#ultralytics.nn.modules.head.Segment

### YOLO-Seg：共用原型，每件用不同係數

檢測頭預測框/類別和每個候選的mask coefficients；Proto支路產生共享basis maps。保留候選的係數線性組合原型，经相應後處理與裁框映回。兩原型是簡化代數例，實際通道數與後處理依所用版本；不能把每張原型直接叫某件物體。

原型乘各件係數，再依物件框取回遮罩。

來源：https://docs.ultralytics.com/reference/nn/modules/head/#ultralytics.nn.modules.head.Segment

### YOLO-Seg：遮罩要和同一個框一起交付

遵循實作的候選過濾與去重，索引必須同步框、類別、係數，不能將甲框配乙mask。映回需還原letterbox，輪廓不能填掉空孔；定位與量測仍須另外驗證，遮罩不是亞像素尺寸真值。

把框、類別與遮罩綁定，映回原圖再核對。

來源：https://docs.ultralytics.com/reference/nn/modules/head/#ultralytics.nn.modules.head.Segment

### 語意與實例分割：同類是否需要分成兩件

共同输入与物件外观不变。语意遮罩同色表示同類，不一定提供逐件身份；實例分割分出甲乙，可支援後續逐件統計。重疊與遮擋仍可能分錯，需要標註與域內驗證；不聲稱必然比語意分割更適合所有工作。

需要逐件交付時，比較實例標註與分離品質。

來源：https://docs.ultralytics.com/reference/nn/modules/head/#ultralytics.nn.modules.head.Segment

<!-- wi033-engineering:end -->

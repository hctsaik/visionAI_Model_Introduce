# Keypoint R-CNN（`keypoint-r-cnn`）

- roadmap 分類：`known-target-classification`
- 講義對照：`02-27`～`02-30`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/keypoint-r-cnn.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
同張圖有兩塊L形件，要找出每件A、B、C孔中心，供對位或後續幾何求解。

### 它交出什麼，也不交出什麼
每件的2D關鍵點、框及相應分數，交對位或幾何步驟；不直接交出3D旋轉和平移。

### 一句心智模型
Keypoint R-CNN先偵測物件，以對齊的ROI特徵為每種關鍵點預測位置熱圖，再把框內位置映回原圖。A/B/C是定義好的點身分，每件都要一致；工業孔位需要相應訓練與標註，不能直接把COCO人體權重當孔位模型。

**限制：** 四孔板接近對稱，辨識方向的缺口又被遮住時，兩套點位對應可能都看似合理。錯誤身分可能得到看似小的重投影誤差；低誤差不能單獨證明姿態正確。

### 換一個現場再推理
目前工站只需檢查孔中心是否落在影像允收區；未來另一工站想用相機姿態做對位。

**問題：** 這輪先交2D點核對，或同時建立3D流程？各自還缺哪些資料？

**核對：** 目前需求可先交逐件2D點與允收核對，驗證點名、遮擋與映回原圖誤差。若本輪已需3D接手，才同時準備足夠正確2D–3D對應、已知幾何、相機校正、多解檢查及必要外參。不能把2D分數當姿態精度，也不必為尚未需要的輸出先付全部成本。
<!-- topic-learning-bridge:end -->
## 模型定位

Keypoint R-CNN 是 Faster/Mask R-CNN family 的 two-stage instance detector＋keypoint heatmap head：先以 RPN/box path 找到並分類每個 instance，再於其 ROI 內估計 K 個 keypoint heatmaps。它解決 instance-aware landmarks，不是全圖無關聯 pose solver，也不是 calibrated coordinate measurement；proposal recall 是後續 keypoint recall 的上限。

## 必要欄位

### architecture_path

固定 image/ROI → resize/normalize → CNN backbone＋FPN → RPN objectness/box proposals → proposal filter/NMS → ROIAlign per proposal → box/class head＋keypoint conv/deconv heatmap head → per-keypoint heatmaps → spatial argmax/soft-argmax（依實作）＋confidence/visibility gate → inverse map 到原圖 coordinates → per-instance boxes/classes/keypoints。

### representation_or_score

Representation 包含 FPN multi-scale features、RPN proposals、ROI-aligned instance features 與每個 landmark 的 ROI-local heatmap。Box/class score、heatmap peak/confidence 與 visibility 是不同訊號；ROIAlign、proposal box、heatmap resolution、argmax 與 inverse mapping 共同決定最終 keypoint coordinate。Peak score 不等於 calibrated coordinate uncertainty。

### cost_and_operating_point

鎖 backbone/FPN、RPN anchors/assignment、proposal/NMS count、ROIAlign sampling/output size、box/keypoint head、K/ordering、heatmap resolution、visibility encoding、loss、input/tile、argmax/refinement、confidence gate、inverse mapping、precision/export/engine。端到端 P95 包含 proposal、NMS、per-ROI keypoint head、coordinate mapping 與 association；同時報 proposal recall、keypoint pixel error/OKS、missing-keypoint rate、instance-association error、calibration 與 review load。

### failure_boundary

Proposal 漏失會使整個 instance 的 keypoints 不可恢復；小物/低有效像素、遮擋/截斷、對稱或重複紋理、密集重疊/NMS、ROI box 誤差、heatmap quantization、visibility/occlusion label 不一致、tile border 與 product shift 會造成 missing、swap、錯配或 coordinate drift。若進量測，必須傳遞 calibration、repeatability 與 per-keypoint uncertainty。

### selection_gate

在 known object classes、多 instance、每個 instance 需要固定 landmark set，且可提供一致 box/keypoint/visibility/symmetry labels 時選用。若物件先驗位置固定且不需要 instance proposal，可比較 direct heatmap/pose pipeline；若只需全域 semantic region，改走 segmentation。固定 input/effective pixels、labels、proposal budget、heatmap resolution、hardware/engine、decision unit 與 confidence/visibility policy，再比較 proposal/keypoint recall、pixel error、association、P95 與 review load。

### evidence_bundle

保存 exact implementation/checkpoint、backbone/FPN、RPN/anchor/assignment、proposal/NMS、ROIAlign、box/keypoint head、K/order/symmetry、heatmap resolution、loss/visibility encoding、input/tile、argmax/refinement/inverse mapping、label/ignore/occlusion revision、lot/product split、proposal recall、pixel error/OKS、missing/association errors、calibration/repeatability/uncertainty、P95/memory/precision 與 failure images。

## 視覺 primitive

- `input_image`：多 instance、small、occluded、symmetric 與 overlapping known objects。
- `feature_path`：backbone/FPN → RPN proposals → ROIAlign → box/class head＋keypoint heatmap head。
- `classification_or_mask_output`：per-instance box/class＋K heatmaps → argmax/confidence/visibility → original-image keypoint coordinates。
- `label_contract`：boxes、keypoint order、visibility/occlusion、symmetry/ambiguity、ignore/crowd 與版本。
- `failure_gate`：proposal miss、tiny/occlusion/symmetry/overlap、ROI/heatmap resolution、visibility labels、mapping/shift；metrology 另接 uncertainty Gate。

## 比較契約

- 比較 ID：`known-target-classification-family-comparison`
- 固定條件：相同 image/ROI、box/keypoint/visibility labels、lot split、effective pixels、proposal budget、heatmap resolution、train budget、hardware/engine、decision unit 與 confidence/visibility policy。
- 共同比較輸出：proposal recall、per-keypoint recall、pixel error/OKS、missing-keypoint/association errors、calibration、端到端 P95、review load；不得用 box AP 或 heatmap peak 直接推出量測能力。

## 來源

- He et al., “Mask R-CNN,” arXiv:1703.06870（Faster R-CNN extension、ROIAlign 與 keypoint/person-pose branch）。
- `full-model-course/02-known-target-classification-segmentation.md` 的 02-27～02-30。

## 產生 gate

六個必要欄位與五個 visual primitives 已完成模型專屬遷移；可開始產生 02-27～02-30 的版本化 C/D 教學頁，逐張通過 QA 後才能 approved。


<!-- wi030-model-core:start -->
## WI-030 核心做法與工作取捨

Keypoint R-CNN先偵測物件，以對齊的ROI特徵為每種關鍵點預測位置熱圖，再把框內位置映回原圖。A/B/C是定義好的點身分，每件都要一致；工業孔位需要相應訓練與標註，不能直接把COCO人體權重當孔位模型。

四孔板接近對稱，辨識方向的缺口又被遮住時，兩套點位對應可能都看似合理。錯誤身分可能得到看似小的重投影誤差；低誤差不能單獨證明姿態正確。

Keypoint R-CNN負責影像中的2D點及所屬物件；Pose Pipeline把這些同名點和已知3D幾何、相機校正接起來求姿態。它們可以串接，不是互相取代的模型排名。只需2D位置時不一定要增加3D求解。

定義每種工件固定點名、可見性與遮擋標註；以適當任務頭訓練，固定ROI和座標還原流程。換點位定義或工件需重訓／重驗。

先在不同旋轉和遮擋影像檢查人能否一致標A/B/C，再按批次分開訓練與測試。

逐件量2D位置誤差、點名混淆、漏點與遮擋表現，核對ROI映回原圖。若再求姿態，另外量姿態誤差，不能只以點位分數代替。

來源：https://docs.pytorch.org/vision/main/_modules/torchvision/models/detection/keypoint_rcnn.html

版本及示意界線見工作項目 sources.md。使用者成品核准pending。
<!-- wi030-model-core:end -->

<!-- wi033-engineering:start -->
## WI-033 工程圖修正

### Keypoint R-CNN：先找物件，再找具名點

把Mask R-CNN的關鍵點支路用於自訂工件，需重新定義並標註關鍵點身份；人體預訓練權重不直接懂支架孔心。每個ROI的每個關鍵點有位置分布，經解碼映回原圖，不是任意紅色熱區。

點的身份要先定義，座標不能混成無名熱區。

來源：https://arxiv.org/abs/1703.06870

### Keypoint R-CNN：ROI座標要映回原圖

ROIAlign取得對齊特徵，關鍵點頭分別產生K個位置heatmaps。圖用連續ROI座標示意x=x0+u*w、y=y0+v*h；實作還要遵循格心、resize與padding約定。A點[0.275,0.3125]在框原點[100,50]、寬高[200,160]時映到[155,100]。

同一個點沿ROI與原圖映射，A/B/C不能互換。

來源：https://arxiv.org/abs/1703.06870

### Keypoint R-CNN：遮住的點也可能被猜出

不可把每個輸出座標當已見到真實點。可見性標註與模型回傳的score/visibility欄位需按實作解讀；保留原圖、具名座標與分數，遮擋點單獨評估。接PnP另需K、畸變、3D對應與足够非退化點。

估計位置與可見證據分開，可信度不足要覆核。

來源：https://arxiv.org/abs/1703.06870

### 關鍵點與分割：要具名位置還是整片區域

固定同一支架影像，若要孔中心身份對應可評關鍵點；若要整片邊界可評分割。兩者都不單獨保證物理姿態或毫米尺寸；按可見性、標註成本、幾何誤差與後續用途比較。

按交付選標註：具名點、輪廓與姿態各有責任。

來源：https://arxiv.org/abs/1703.06870

<!-- wi033-engineering:end -->

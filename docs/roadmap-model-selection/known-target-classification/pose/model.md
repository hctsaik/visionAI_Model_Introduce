# Pose pipeline（`pose`）

- roadmap 分類：`known-target-classification`
- 講義對照：`02-31`～`02-34`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/pose.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
已找出四孔U形件的影像點，現在要知道工件相對相機的位置和方向，並可追查姿態可信度。

### 它交出什麼，也不交出什麼
物體到相機的旋轉／平移與驗證紀錄；如需工站座標需另接外參，不直接等於可執行的機器動作。

### 一句心智模型
Pose Pipeline先把同名2D影像點和已知3D工件點配對，連同相機內參及畸變設定交給PnP求解。結果表示物體座標到相機座標的旋轉與平移；再將3D點重投影回影像核對。點數、平面性和求解方法會影響可解性與多解，四點示意不保證唯一正確解。

**限制：** 四孔板接近對稱，辨識方向的缺口又被遮住時，兩套點位對應可能都看似合理。錯誤身分可能得到看似小的重投影誤差；低誤差不能單獨證明姿態正確。

### 換一個現場再推理
接近對稱的四孔板缺口被遮住，兩個候選姿態都可能有小重投影誤差。工件表面可能不允許永久標記。

**問題：** 選可移除標記、調整視角，或保留人工覆核？你要先核對哪個限制？

**核對：** 先核對表面處理規範、可見性、節拍和校正條件。可移除且穩定可見的標記可提供點身分；若不能標記，可測額外視角，但須維護校正與遮擋條件。短期人工覆核也可能合理，需明確攔下不確定解。任何路線都要驗證物理姿態，不能只選重投影分數略低者。
<!-- topic-learning-bridge:end -->
## 模型定位

`Pose` 是由 keypoint detection、instance association、coordinate transform 與 geometric solver 組成的任務 pipeline，不是單一模型名稱。進 shortlist 前必須選定 top-down 或 bottom-up、backbone/decoder、keypoint schema、2D/3D camera assumption、solver、confidence/visibility/fallback policy 與 runtime。教材以可審計 pipeline 呈現，不假設不存在的固定 Pose checkpoint。

## 必要欄位

### architecture_path

Top-down 固定 image → instance detector → box/NMS → crop/ROI transform → per-instance keypoint network → heatmaps/coordinates＋confidence/visibility → inverse mapping → geometric fit/PnP/fixture rule → pose＋uncertainty。Bottom-up 固定 image → shared backbone → joint/keypoint heatmaps＋association fields/tags → peak extraction → grouping/instance association → per-instance keypoints → geometric fit → pose＋uncertainty。

### representation_or_score

Representation 依 pipeline 分為 proposal-linked ROI heatmaps（top-down）或全圖 keypoint heatmaps＋association representation（bottom-up）。最終輸出包含 per-instance ordered keypoints、visibility/confidence、association、2D/3D pose/transform 與 uncertainty/fallback state。Heatmap peak、detector score 或 solver residual 都不能單獨代表 calibrated pose uncertainty。

### cost_and_operating_point

鎖 top-down/bottom-up、detector（若有）、backbone/decoder、keypoint ontology/order、input/crop/scale/flip、heatmap/coordinate loss、association method、visibility/occlusion/symmetry、inverse transforms、camera intrinsics/extrinsics、solver/RANSAC/fixture rule、confidence/uncertainty Gate、precision/export/engine。端到端 P95 包含 detector/crops 或 grouping、keypoint network、inverse mapping、solver、fallback；同時報 event success、tail keypoint/pose error、missing/swap/association、repeatability 與 review load。

### failure_boundary

Top-down 受 detector/proposal recall 限制；bottom-up 受 peak grouping/association 限制。遮擋/截斷、對稱/重複紋理、tiny/低有效像素、密集重疊、visibility/ontology 不一致、flip/scale/crop inverse mapping、camera drift、fixture deformation、OOD/product shift 會造成 missing、swap、錯配、pose flip 或 solver divergence。

### selection_gate

當 downstream 需要 orientation、assembly completeness、robot grasp/fixture localization 或 2D/3D pose，且有可審計 keypoint/camera/geometry contract 時選用。多 instance 且 detector 穩定可先驗證 top-down；instance 數多、希望 shared full-image inference 且 association 可學時驗證 bottom-up。固定 keypoint/camera/decision contract，比 event success、tail error、association/fallback、P95、memory 與 review load，而非只比 keypoint AP。

### evidence_bundle

保存 pipeline topology、exact detector/backbone/decoder/checkpoint、keypoint ontology/order、visibility/occlusion/symmetry policy、input/crop/scale/flip、heatmap/coordinate/association config、inverse transforms、camera calibration、solver/RANSAC/fixture rules、confidence/uncertainty/fallback thresholds、lot/product split、event success、P95/tail errors、missing/swap/association、repeatability、review load 與 failure images。

## 視覺 primitive

- `input_image`：多 instance industrial parts，含 orientation、occlusion、symmetry、overlap 與 camera-view variation。
- `feature_path`：top-down detector→crop→keypoint network；bottom-up full-image heatmaps＋association→grouping；兩路都接 transform/solver。
- `classification_or_mask_output`：ordered keypoints＋visibility/confidence＋association → 2D/3D pose/transform＋uncertainty/fallback。
- `label_contract`：keypoint ontology/order、visibility/occlusion、symmetry、instance ID/association、2D/3D coordinates 與 camera/fixture revision。
- `failure_gate`：detector miss、grouping error、occlusion/symmetry/tiny/overlap、mapping/camera drift、solver divergence、shift。

## 比較契約

- 比較 ID：`known-target-classification-family-comparison`
- 固定條件：相同 image/ROI、keypoint/visibility/symmetry/association labels、camera calibration、effective pixels、train budget、hardware/engine、decision event、confidence/uncertainty/fallback policy。
- 共同比較輸出：event success、keypoint/pose tail error、missing/swap/association、repeatability、端到端 P95/memory、fallback/review load；不得以 detector AP、keypoint AP 或 solver residual 單獨宣稱 pose 放行能力。

## 來源

- Xiao et al., “Simple Baselines for Human Pose Estimation and Tracking,” arXiv:1804.06208（top-down pose baseline；工業場景只採其 pipeline pattern）。
- Cao et al., “OpenPose: Realtime Multi-Person 2D Pose Estimation using Part Affinity Fields,” arXiv:1812.08008（bottom-up keypoint heatmaps＋association fields pattern）。
- `full-model-course/02-known-target-classification-segmentation.md` 的 02-31～02-34。

## 產生 gate

六個必要欄位與五個 visual primitives 已完成 pipeline-specific 遷移；可開始產生 02-31～02-34 的版本化 C/D 教學頁，逐張通過 QA 後才能 approved。


<!-- wi030-model-core:start -->
## WI-030 核心做法與工作取捨

Pose Pipeline先把同名2D影像點和已知3D工件點配對，連同相機內參及畸變設定交給PnP求解。結果表示物體座標到相機座標的旋轉與平移；再將3D點重投影回影像核對。點數、平面性和求解方法會影響可解性與多解，四點示意不保證唯一正確解。

四孔板接近對稱，辨識方向的缺口又被遮住時，兩套點位對應可能都看似合理。錯誤身分可能得到看似小的重投影誤差；低誤差不能單獨證明姿態正確。

Keypoint R-CNN負責影像中的2D點及所屬物件；Pose Pipeline把這些同名點和已知3D幾何、相機校正接起來求姿態。它們可以串接，不是互相取代的模型排名。只需2D位置時不一定要增加3D求解。

不一定需要訓練PnP，但需要可靠2D點、已知3D幾何、內外參和單位。換鏡頭、焦距、相機位置或工件幾何要重核對相應校正與座標鏈。

先用可追溯幾何與校正資料建立2D–3D對應，保存原始影像和點名，再選適用的PnP方法及多解檢查。

以獨立姿態參考量旋轉和平移誤差，另記重投影誤差、外點、多解、單位和座標轉換；只有重投影小不代表物理姿態必定正確。

來源：https://docs.opencv.org/4.13.0/d5/d1f/calib3d_solvePnP.html

版本及示意界線見工作項目 sources.md。使用者成品核准pending。
<!-- wi030-model-core:end -->

<!-- wi033-engineering:start -->
## WI-033 工程圖修正

### Pose：影像點必須對上實體點

同一支架的點名應跨影像與CAD一致。三點圖解只教對應；實際點數、幾何形狀與PnP方法影響可解性。需固定K、畸變、座標系及CAD單位，輸出的R/t才有意義；不以關鍵點熱區直接當姿態。

先鎖定點名與相機設定，才能解讀姿態。

來源：https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html

### Pose：先框再找點，或先找點再分組

兩種2D關鍵點方法是替代方案。Top-down先偵測每個物件，再於各ROI估點並映回原圖；Bottom-up先估全圖點，再歸到不同實例。兩者都須保留物件ID、點名與原圖座標。求3D姿態仍需已知3D對應、K與畸變，這裡的三點僅解釋分組，不聲稱足以唯一求PnP。

兩條替代路徑都交出有身份的 2D 點。

來源：https://mmpose.readthedocs.io/en/latest/guide_to_framework.html ; https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html

### Pose：姿態還要投回原图檢查

R/t表示物體到相機的變換，t單位跟3D工件座標一致。重投影把已知3D點經R/t與相機模型映回原圖，逐點比較觀測與投影；若用去畸變影像須搭配相應相機設定。交付點ID、可見性、誤差、版本與失敗狀態，外部機器人座標另需外參。

交付 R／t、座標單位與逐點誤差，再核對實體。

來源：https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html

### Pose：對稱件的小誤差也可能騙人

近對稱工件上缺口被擋，錯誤ID也可能有低重投影誤差。比較有標記與第二視角的選擇時，需核對表面限制、可見性、校正與節拍，不只挑分數略低的姿態。不能確認就輸出失敗狀態並覆核。

遇到身份歧義，補可見證據並攔下不確定姿態。

來源：https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html

<!-- wi033-engineering:end -->

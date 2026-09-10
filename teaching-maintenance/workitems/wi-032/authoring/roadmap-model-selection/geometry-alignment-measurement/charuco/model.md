# ChArUco（`charuco`）

- roadmap 分類：`geometry-alignment-measurement`
- roadmap 節點：`Charuco`
- 講義對照：`01-03`～`01-06`
- 內容覆蓋狀態：`complete`
- 產生狀態：`self-reviewed-tested; user-approval-pending`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/charuco.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
同一工件換到畫面邊角後，看起來的比例與位置不一樣。先用尺寸已知的ChArUco板建立相機幾何，才能分清鏡頭投影與工件本身的變化。

### 它交出什麼，也不交出什麼
交付內參、畸變模型與係數、相機／鏡頭／解析度條件和核對紀錄；需要姿態時另交付清楚方向與單位的R/t。日常工件對位、尺寸量測及工站座標轉換仍各需對應流程。

### 一句心智模型
ChArUco結合可辨識的ArUco標記與棋盤交點。標記協助辨認板上位置，精細棋盤角點提供影像座標；同一角點在多個位置與傾角被看見後，配合已知板上座標估計相機內參及畸變。單張姿態是另一個問題：已知內參／畸變，再由板上3D點與影像2D點求板相對相機的R/t。

**限制：** 若校正資料只覆蓋畫面中心，中心重投影看起來不錯也不能保證邊角可靠。用未參與估計的邊角與傾斜視角核對，再決定補拍；不是只增加照片張數。

### 換一個現場再推理
相機與鏡頭沒有更換，但工件治具平移；另一條線則換了鏡頭並把輸出解析度減半。

**問題：** 兩條線都直接重跑ECC就足夠嗎？各先核對什麼？

**核對：** 治具平移那條線先確認取像條件與既有內參仍適用，再重建工件／工站座標關係或做逐件定位；不必只因平移就盲目重校正。換鏡頭與解析度那條線先核對並重新估計或正確換算相機參數，再用獨立資料驗證。ECC可以協助接近位置的影像對齊，但不提供新鏡頭的完整校正或毫米準確保證。
<!-- topic-learning-bridge:end -->
<!-- wi032-model-core:start -->
## WI-032 核心做法與工作取捨

ChArUco結合可辨識的ArUco標記與棋盤交點。標記協助辨認板上位置，精細棋盤角點提供影像座標；同一角點在多個位置與傾角被看見後，配合已知板上座標估計相機內參及畸變。單張姿態是另一個問題：已知內參／畸變，再由板上3D點與影像2D點求板相對相機的R/t。

若校正資料只覆蓋畫面中心，中心重投影看起來不錯也不能保證邊角可靠。用未參與估計的邊角與傾斜視角核對，再決定補拍；不是只增加照片張數。

ChArUco解決已知標靶的相機幾何；SIFT與LightGlue處理影像間的對應點；ECC在合理起點附近微調外觀對齊。要逐件找位置不能只靠一次ChArUco校正，要校正相機也不能拿一般工件匹配取代已知幾何。

換鏡頭、焦距、對焦、影像裁切或解析度時重查內參適用性；換治具時核對座標關係。保留多位置／傾角影像、角點ID、板的尺寸與字典設定，重新拍攝的成本往往比算法執行更關鍵。

先確定相機模型、實體標靶尺寸／方格與標記設定；固定影像解析度與光學條件，採集涵蓋中心、邊角及傾角的清楚影像，另留獨立核對組。

保存輸入影像、角點ID／座標、設定、參數與每視角重投影分布；以獨立視角、重裝重拍及工作位置查穩定性。若要毫米量測，還需獨立尺寸基準與誤差預算。本頁新圖為受控示意，不是新相機校正實測。

來源：https://docs.opencv.org/4.13.0/da/d13/tutorial_aruco_calibration.html

版本及示意界線見工作項目 sources.md。使用者成品核准pending。
<!-- wi032-model-core:end -->
## 模型定位

ChArUco 是由 ArUco marker 與棋盤角點組成的實體標定板，不是 learned model。它在可放置標靶的條件下，建立相機內外參、姿態與可追溯幾何基準；它不取代產品影像的日常 registration。

## 必要欄位

### architecture_path

標靶影像 → marker detection 與 ID → 插值棋盤角點 → 已知 3D／平面點與 2D image corners 的 correspondence → calibration 或 PnP → intrinsics、extrinsics、pose 與 reprojection residual。

### representation_or_score

核心 representation 是有唯一 ID 的 2D corners 與已知尺寸／平面座標的 object points。工程 score 是 reprojection residual（P50/P95）、有效 corner count、FOV coverage 與 pose diversity；不是分類 accuracy。

### cost_and_operating_point

建置期需在全 FOV、不同距離與姿態收集清晰標靶影像並求解參數。部署期成本主要是 marker／corner detection 與 PnP；輸出必須通過 corner count、coverage 與 residual gate 才能採用。

### failure_boundary

遮擋、反光、模糊、角點覆蓋不足、板面彎曲、標靶尺寸誤差、焦點變更與 mount 鬆動，都會令單次平均 residual 掩蓋尾端風險。

### selection_gate

只有在可控制地放置已知標靶、需要可追溯幾何基準時選用。以不同位置、不同姿態與重裝後的 P95 reprojection／downstream registration residual 及拒用率通過 qualification；不得只以單次平均誤差放行。

### evidence_bundle

保存標靶版型與尺寸、平面度量測、mount 版本、camera/lens/focus 設定、影像覆蓋樣本、corner coverage、residual 分布、重裝 repeatability、拒用影像與 qualification 結果。

## 視覺 primitive

- `input_roi`：含 ChArUco 標靶的相機畫面。
- `coordinate_system`：已知標靶座標與相機／工站座標。
- `calibration_or_registration`：marker ID、corner correspondence、calibration/PnP 資料流。
- `measurement_output`：camera pose、reprojection residual、coverage。
- `uncertainty_gate`：遮擋／反光／模糊／板面彎曲與 reject gate。

## 視覺生產 gate

產圖前必須讀取 `../../VISUAL_PRODUCTION_STANDARD.md`。四張必備頁必須覆蓋定位、實用機制、建置與推論、選型與失效；直接比較頁使用 D，其餘使用 C。

<!-- wi032-engineering:start -->
## 工程層：輸入、機制、部署與限制

### ChArUco：把板上點連到影像點

以標靶已知3D平面座標與各視角2D點估計相機模型；板上Z=0不等於影像是正視投影。校正需要合適視角、模型及品質核對，不能把固定工件對位當成校正。

建立的是相機幾何，不是每天工件的定位結果。

來源：https://docs.opencv.org/4.13.0/da/d13/tutorial_aruco_calibration.html

### 辨認標記與精細棋盤角點，各有任務

偵測到ArUco標記之後，ChArUco流程估計及細化棋盤交點位置；實際可用角點取決於清晰度、視角、遮擋與設定。不能把marker中心替換成棋盤角點。

ID解決身份，棋盤角點提供精細影像位置。

來源：https://docs.opencv.org/4.13.0/da/d13/tutorial_aruco_calibration.html

### 已知內參後，才另外解單張姿態

solvePnP把板上物體座標轉到相機座標。平面與特定求解器可能涉及多解；需結合可見性、重投影和工作約束核對，單一低誤差不自動保證工站量測。

姿態、相機校正與工站轉換，是不同的交付。

來源：https://docs.opencv.org/4.13.0/da/d13/tutorial_aruco_calibration.html

### 相機設定變了，舊參數還能用嗎？

更換鏡頭、對焦或解析度後應重新確認參數適用性；已知縮放／裁切可換算像素內參但仍需驗證。毫米準確還涉及外參、工作平面、標靶真實尺寸和誤差預算。

把參數與取像條件綁定，改條件就重新核對。

來源：https://docs.opencv.org/4.13.0/da/d13/tutorial_aruco_calibration.html

<!-- wi032-engineering:end -->

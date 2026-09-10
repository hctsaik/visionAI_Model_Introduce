# ChArUco（`charuco`）

- roadmap 分類：`geometry-alignment-measurement`
- roadmap 節點：`Charuco`
- 講義對照：`01-03`～`01-06`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/charuco.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
你能在建置或維修時控制地放入一塊尺寸已知的 ChArUco 標定板。你需要知道相機看到的像素和工站座標如何對應，並留下可追溯的相機姿態；這不是每天拿產品影像硬做對位。

### 它交出什麼，也不交出什麼
ChArUco 交付經過角點數、視野覆蓋與 reprojection residual 驗證的 calibration 或 pose；不是產品缺陷分類、日常 registration、量產品質判定或自動放行。

### 一句心智模型
相機先偵測 ArUco marker ID，再插值出棋盤角點的 2D image corners。

每個 2D corner 與標靶尺寸、平面度所定義的 3D 或平面 object point 配成 correspondence。

calibration 或 PnP 用多組 correspondence 求出 intrinsics、extrinsics 或 pose，並把預測角點回投影到影像。

**限制：** 這把尺是可控制放入的實體標靶；它建立相機基準，不會自動替每一張產品影像完成日常對位，也不證明產品本身合格。

### 換一個現場再推理
維修後換了同型鏡頭與 mount；中心位置的一張 board image 平均 residual 很小，但產品會使用整個 FOV。

**問題：** 可以沿用舊 calibration／pose 交給量產嗎？指出至少兩個還沒被證明的條件與下一步。

**核對：** 不可以。mount、lens/focus revision 與 full-FOV／pose coverage 都已改變或尚未驗證；重拍多位置、多姿態 board，檢查 corner count、P95 residual、reject rate、重裝 repeatability 與 downstream registration residual。完成前 HOLD。
<!-- topic-learning-bridge:end -->
<!-- f02-model-core:start -->
## F02 模型中心思想與來源核對

**為什麼需要：** 你能在建置或維修時控制地放入一塊尺寸已知的 ChArUco 標定板。你需要知道相機看到的像素和工站座標如何對應，並留下可追溯的相機姿態；這不是每天拿產品影像硬做對位。

**在板上找出有身份的 marker 與角點**：相機先偵測 ArUco marker ID，再插值出棋盤角點的 2D image corners。

**把畫面角點接回已知標靶座標**：每個 2D corner 與標靶尺寸、平面度所定義的 3D 或平面 object point 配成 correspondence。

**求出相機參數或當下姿態**：calibration 或 PnP 用多組 correspondence 求出 intrinsics、extrinsics 或 pose，並把預測角點回投影到影像。

**移除核心設計自測：** 先猜：哪一組比較能暴露邊角區域的幾何誤差？為什麼只看一個平均 residual 不夠？

**自測核對：** 全 FOV、多姿態資料能讓解算看到不同區域與姿態的誤差；中心單張即使平均 residual 小，也可能掩蓋邊角、重裝或尾端失敗。

**選型線索：** 能受控放入已知標靶、需要可追溯相機幾何基準時，先選 ChArUco。固定標靶尺寸、平面度、mount、camera/lens/focus 與 capture coverage，並以不同位置、姿態和重裝後的 P95 reprojection 及下游 residual qualification；不要以單次平均誤差放行。

**來源：** [roadmap-model-selection/geometry-alignment-measurement/charuco/model.md](roadmap-model-selection/geometry-alignment-measurement/charuco/model.md)

F02 核心圖 `_course_content/generated-concepts/charuco/charuco-f02-core.svg` 是機制與案例素材的教學示意，不是模型推論輸出。
<!-- f02-model-core:end -->
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

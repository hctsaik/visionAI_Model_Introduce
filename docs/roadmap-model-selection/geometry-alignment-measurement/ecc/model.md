# ECC（`ecc`）

- roadmap 分類：`geometry-alignment-measurement`
- roadmap 節點：`ECC`
- 講義對照：`01-07`～`01-10`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/ecc.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
你有固定 template ROI，也有一張外觀相近、初始位置已接近的 moving ROI。你想在下游 AOI 前把小平移、旋轉或近似平面變形校正回來；你不是要解決任意大位移、視差或產品結構改變。

### 它交出什麼，也不交出什麼
ECC 交付迭代求得的 warp θ、aligned ROI、inverse transform、objective/residual 與收斂旗標；不是產品品質分數、缺陷遮罩，也不是所有場景都能收斂的萬用對位器。

### 一句心智模型
先鎖 template、mask、pyramid、initial transform 與可使用的 ROI，再選 translation、euclidean、affine 或 homography warp family。

目前的參數 θ 將 moving ROI warp 到 template 參考座標，並做對應的 photometric normalization。

coarse-to-fine pyramid 中，ECC objective 指引每輪更新 warp parameter，直到滿足停止條件或到達最大迭代。

**限制：** 透明片比喻假設兩張畫面外觀穩定、初始位置接近且幾何近似平面。反光、視差、大缺陷或錯初值會讓「看起來相關」不等於真的對齊。

### 換一個現場再推理
新治具使 current ROI 比 template 有大位移與非平面視差，局部還有強反光。

**問題：** 若 ECC 跑出高 objective，你會直接把 warp 送往下游嗎？

**核對：** 不會。它已超出可靠初值、穩定外觀與近似平面的假設；高 objective 可能是錯收斂。先 HOLD，重新建立可驗證 initialization／幾何條件，或改選適合視差與大位移的方法，再以 residual tail、inverse map 與下游結果驗證。
<!-- topic-learning-bridge:end -->
<!-- f02-model-core:start -->
## F02 模型中心思想與來源核對

**為什麼需要：** 你有固定 template ROI，也有一張外觀相近、初始位置已接近的 moving ROI。你想在下游 AOI 前把小平移、旋轉或近似平面變形校正回來；你不是要解決任意大位移、視差或產品結構改變。

**固定 template、moving ROI 與起始位置**：先鎖 template、mask、pyramid、initial transform 與可使用的 ROI，再選 translation、euclidean、affine 或 homography warp family。

**先用 warp 把 moving ROI 映到 template 座標**：目前的參數 θ 將 moving ROI warp 到 template 參考座標，並做對應的 photometric normalization。

**由 ECC objective 反覆更新 θ**：coarse-to-fine pyramid 中，ECC objective 指引每輪更新 warp parameter，直到滿足停止條件或到達最大迭代。

**移除核心設計自測：** 先猜：哪一張比較適合從目前位置開始迭代 warp？另一張若硬跑，可能會出現什麼危險？

**自測核對：** 小位移且外觀穩定的 ROI 有機會收斂到可信 micro-alignment；錯初值或強反光可能錯收斂到表面上相關的錯誤位置，所以必須看 residual、convergence 與下游 gate。

**選型線索：** 固定 template、外觀穩定、初始位置可靠且場景近似平面時，才把 ECC 放入候選。鎖 template/mask、pyramid、initial transform、warp family、最大迭代和停止條件；以 residual tail、錯收斂率、reject rate、下游 registration evidence 與 P95 判定，不以高相關或單一收斂旗標放行。

**來源：** [roadmap-model-selection/geometry-alignment-measurement/ecc/model.md](roadmap-model-selection/geometry-alignment-measurement/ecc/model.md)

F02 核心圖 `_course_content/generated-concepts/ecc/ecc-f02-core.svg` 是機制與案例素材的教學示意，不是模型推論輸出。
<!-- f02-model-core:end -->
## 模型定位

ECC（Enhanced Correlation Coefficient）是直接影像配準最佳化，不是 learned model。它在 template 與 moving ROI 外觀穩定、初始位姿接近時，以 iteratively updated warp 做連續校正；它不是大位移、視差或結構變化的萬用對位器。

## 必要欄位

### architecture_path

template ROI + moving ROI → 選擇 translation／euclidean／affine／homography warp → warp moving ROI → photometric normalization → ECC objective → coarse-to-fine iterative parameter update → warped ROI、inverse transform、residual 與收斂旗標。

### representation_or_score

運行 state 是 warp parameter `θ`。工程輸出是 aligned ROI、ECC objective、iteration、residual、收斂旗標與 inverse transform；下游異常 heatmap 必須能回映原始座標。

### cost_and_operating_point

部署前鎖定 template、mask、pyramid、initial transform、warp family、最大迭代與停止條件。推論成本隨 pyramid level、warp 自由度與迭代次數增加；P95 latency、錯收斂率和拒用率都要量測。

### failure_boundary

illumination drift、反光、dirty/defect 大範圍改變、錯初值、非平面視差，以及過度自由的 homography，會造成錯收斂或表面上高相關的錯誤 alignment。

### selection_gate

只在小位移、固定外觀、可靠初始位置與近似平面的場景選用。固定 ROI、template、initialization、硬體與 decision policy，比較 ChArUco／feature initialization 的 residual tail、錯收斂率與 P95 latency；不通過則拒用或改以其他初始化／方法。

### evidence_bundle

保存 template/mask、recipe/optics 版本、warp family、pyramid、initialization、iteration、objective/residual 分布、收斂旗標、failure images、inverse-transform 回映例與 qualification 結果。

## 視覺 primitive

- `input_roi`：template 與 moving ROI。
- `coordinate_system`：warp 前後及 inverse mapping 的 ROI 座標。
- `calibration_or_registration`：pyramid、warp、objective 與 iterative update。
- `measurement_output`：aligned ROI、residual、iteration、convergence。
- `uncertainty_gate`：錯初值、反光、視差、結構變化與 reject gate。

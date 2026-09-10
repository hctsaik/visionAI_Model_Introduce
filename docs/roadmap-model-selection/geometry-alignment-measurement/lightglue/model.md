# LightGlue（`lightglue`）

- roadmap 分類：`geometry-alignment-measurement`
- 講義對照：`01-15`～`01-18`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/lightglue.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
你有同一工件的兩張 ROI，希望由局部特徵建立幾何初始化；某些表面讓傳統 descriptor 不夠穩，因此考慮 learned matcher。你仍必須明確選上游 extractor、固定輸入契約，並把結果交給 RANSAC/pose/warp solver 驗證。

### 它交出什麼，也不交出什麼
LightGlue 交付從外部 extractor 的 keypoints/descriptors 中選出的 correspondences、confidence、adaptive pruning 與 early stopping 狀態；不是 detector、不是 transform solver，也不是已驗證的量測結果。

### 一句心智模型
image A/B 先經 SuperPoint、DISK 或 ALIKED 等指定 extractor，產生 keypoints 和 descriptors。

self/cross-attention matching 將兩張圖的 descriptor tokens 互動，形成對應候選與 confidence。

低可信或不必要的候選被 adaptive pruning，滿足條件時 early stopping，保留 matches 與 confidence。

**限制：** 配對員沒有量尺或幾何求解器。confidence 是 matcher 的訊號，不等於 transform 正確、inlier coverage 足夠或座標量測已校準。

### 換一個現場再推理
新 PCB 有週期性格紋，resize 與 keypoint budget 也被調過；LightGlue 的高 confidence matches 都集中在一小塊。

**問題：** 可以只因 confidence 高就送進 production warp 嗎？

**核對：** 不可以。extractor、resize、budget 改變即改變輸入契約；重複格紋也可使高 confidence 線一起錯配。先鎖完整 upstream contract，再用 RANSAC／solver 的 inlier spatial coverage、residual tail 與 reject rate 決定，不足即 HOLD。
<!-- topic-learning-bridge:end -->
<!-- f02-model-core:start -->
## F02 模型中心思想與來源核對

**為什麼需要：** 你有同一工件的兩張 ROI，希望由局部特徵建立幾何初始化；某些表面讓傳統 descriptor 不夠穩，因此考慮 learned matcher。你仍必須明確選上游 extractor、固定輸入契約，並把結果交給 RANSAC/pose/warp solver 驗證。

**先由外部 extractor 產生特徵 token**：image A/B 先經 SuperPoint、DISK 或 ALIKED 等指定 extractor，產生 keypoints 和 descriptors。

**讓 token 在圖內與跨圖互相參考**：self/cross-attention matching 將兩張圖的 descriptor tokens 互動，形成對應候選與 confidence。

**用 pruning 和 early stopping 控制計算**：低可信或不必要的候選被 adaptive pruning，滿足條件時 early stopping，保留 matches 與 confidence。

**移除核心設計自測：** 先猜：高 confidence 是否能單獨證明這些線支持同一個 warp？還缺少哪一層檢查？

**自測核對：** 不能。confidence 反映 learned matching 的可信訊號；重複結構仍可能讓看似強的 matches 沒有共同幾何意義。RANSAC/pose solver、inlier coverage 和 residual 才決定能否形成 transform。

**選型線索：** 傳統 descriptor 不穩、但可接受 extractor/weights 依賴並仍需要 correspondence 時，才評估 LightGlue。固定 extractor、image scale、keypoint budget、confidence threshold、early stop、RANSAC 和 input contract，與 SIFT 比較 inlier coverage、registration tail、reject rate 和 P95；低 confidence 或幾何 gate 不足時拒用。

**來源：** [roadmap-model-selection/geometry-alignment-measurement/lightglue/model.md](roadmap-model-selection/geometry-alignment-measurement/lightglue/model.md)

F02 核心圖 `_course_content/generated-concepts/lightglue/lightglue-f02-core.svg` 是機制與案例素材的教學示意，不是模型推論輸出。
<!-- f02-model-core:end -->
## 模型定位

LightGlue 是 learned local-feature matcher，使用上游 extractor 產生的 keypoints/descriptors，經 self/cross attention 建立高可信 matches 並 adaptive pruning/early stopping。它不是 detector，也不是 transform solver。

## 必要欄位

### architecture_path

image A/B → SuperPoint、DISK 或 ALIKED extractor → keypoints + descriptor tokens → self/cross-attention matching → confidence、adaptive pruning、early stopping → matches → RANSAC/pose/warp。

### representation_or_score

representation 是兩張圖的 learned descriptor tokens。模型輸出是 correspondence 與 confidence，不是直接量測值；幾何有效性仍由 RANSAC/pose solver、inlier coverage 與 residual 驗證。

### cost_and_operating_point

鎖 extractor、weights、resize、keypoint budget、confidence threshold、early-stop 與 RANSAC。P95 必須含 extractor、matcher 與 geometry solver；keypoint budget 和 pruning 影響 latency／recall tradeoff。

### failure_boundary

不可觀測表面、重複結構、非剛性變化、domain shift 及未校準 confidence 會令 learned matches 失去幾何意義。公開 demo pair 的結果不能取代量產 surface texture validation。

### selection_gate

在傳統 descriptor 不穩且可接受模型依賴時選用。固定 extractor、image scale、keypoint budget、RANSAC 與 input contract，與 SIFT 比較 inlier coverage、registration tail、reject rate、P95 cost；confidence 不足時 reject，不可硬湊 transform。

### evidence_bundle

保存 extractor/weights、resize、budget、threshold、early-stop、surface/domain split、confidence distribution、inlier coverage、residual tail、P95 與失敗 pairs。

## 視覺 primitive

- `input_pair`：同一工件的兩張 ROI。
- `extractor_boundary`：外部 extractor 與 LightGlue matcher 的責任分界。
- `token_matching`：descriptor tokens、self/cross attention、confidence/pruning。
- `geometry_solver`：RANSAC 後的 inliers/warp。
- `uncertainty_gate`：重複結構、不可觀測、domain shift、低 confidence reject。

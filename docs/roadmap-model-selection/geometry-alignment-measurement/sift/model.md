# SIFT（`sift`）

- roadmap 分類：`geometry-alignment-measurement`
- 講義對照：`01-11`～`01-14`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/sift.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
你有 reference ROI 和 current ROI，無法每次放 ChArUco 標靶；表面卻有穩定紋理、孔洞或局部細節可供辨識。你要找的是可追查的 correspondence，幫助估計幾何初始化或 warp，而不是分類產品品質。

### 它交出什麼，也不交出什麼
SIFT 交付帶位置、尺度與方向的 local keypoints/descriptors，以及經 ratio test、RANSAC、inlier coverage 和 residual 驗證後的 correspondence 或 transform；不是類別分數、缺陷候選或最終 registration 保證。

### 一句心智模型
image pyramid 產生多尺度影像，DoG extrema 找 candidate keypoints，再做 localization 與 contrast/edge rejection。

保留 keypoint 的位置、尺度、orientation，並從周圍梯度形成 descriptor。

reference 與 current descriptors 以 nearest-neighbor 比對，再用 ratio test 排除不夠明確的鄰居。

**限制：** 名片相近不等於幾何一定正確。低紋理、鏡面、週期重複圖樣或太小 ROI 會讓候選連線不足或集中錯配，仍要用 RANSAC、空間 coverage 和 residual 篩選。

### 換一個現場再推理
新產品表面平滑且鏡面，reference/current pair 幾乎沒有穩定局部紋理。

**問題：** 可以放寬 ratio test、用少數 match 硬求 transform 嗎？為什麼？

**核對：** 不可以。SIFT 缺少足夠可觀測的 keypoints 時，放寬門檻只會增加不受幾何支持的錯配。應拒用或調整 ROI／取像；若可放標靶可考慮 ChArUco，若已有可靠小位移初值才另驗 ECC。
<!-- topic-learning-bridge:end -->
<!-- f02-model-core:start -->
## F02 模型中心思想與來源核對

**為什麼需要：** 你有 reference ROI 和 current ROI，無法每次放 ChArUco 標靶；表面卻有穩定紋理、孔洞或局部細節可供辨識。你要找的是可追查的 correspondence，幫助估計幾何初始化或 warp，而不是分類產品品質。

**在不同尺度找候選局部地標**：image pyramid 產生多尺度影像，DoG extrema 找 candidate keypoints，再做 localization 與 contrast/edge rejection。

**為每個地標建立方向化 descriptor**：保留 keypoint 的位置、尺度、orientation，並從周圍梯度形成 descriptor。

**先把相似 descriptor 變成候選 match**：reference 與 current descriptors 以 nearest-neighbor 比對，再用 ratio test 排除不夠明確的鄰居。

**移除核心設計自測：** 先猜：哪一組比較能約束整個 transform？為什麼 match 數量不是唯一證據？

**自測核對：** 分散的 inliers 才會約束不同位置的幾何；大量集中在重複圖樣的 match 可能是同一種錯配重複出現。SIFT 的工程價值是可檢查 correspondence，不是累計連線數。

**選型線索：** 無法放置標靶、表面又有穩定可觀測紋理且需要可解釋 correspondence 時，SIFT 是合理基線。固定 detector threshold、matcher、ratio test、RANSAC model 和 inlier gate，量 inlier coverage、residual tail、reject rate 和 P95；不要只用 match 數或把它當最後 registration。

**來源：** [roadmap-model-selection/geometry-alignment-measurement/sift/model.md](roadmap-model-selection/geometry-alignment-measurement/sift/model.md)

F02 核心圖 `_course_content/generated-concepts/sift/sift-f02-core.svg` 是機制與案例素材的教學示意，不是模型推論輸出。
<!-- f02-model-core:end -->
## 模型定位

SIFT 是尺度不變局部特徵與 descriptor 管線，不是深度網路。它適用於無法放置標靶、但表面具有穩定可觀測紋理時，從 correspondence 估計幾何初始化或 warp。

## 必要欄位

### architecture_path

image pyramid → DoG extrema → localization 與 contrast/edge rejection → orientation → gradient descriptor → nearest-neighbor matches → ratio test/RANSAC → transform。

### representation_or_score

representation 是有位置、尺度、方向的 local keypoint 與 gradient descriptor。量測 match distance、inlier count、inlier spatial coverage、reprojection residual；輸出是 correspondence 或 warp，不是分類分數。

### cost_and_operating_point

鎖 detector threshold、descriptor matcher、ratio-test、RANSAC model 與 inlier gate。成本受影像解析度、keypoint 數、matching 與 RANSAC 假設影響；應量測 P95 latency 及 reject rate。

### failure_boundary

低紋理、鏡面、模糊、週期重複圖樣、大視角變化與 tiny ROI 都可能造成錯配或不足 coverage。position-sensitive AD 中，SIFT warp 常只是 initialization，仍需 finer registration gate。

### selection_gate

選它於需要可解釋 correspondence、且表面紋理可觀測的情境。通過 inlier spatial coverage、residual tail、reject rate 與下游 registration evidence 後才採用；match 集中於重複圖樣時拒用。

### evidence_bundle

保存 reference image、曝光/focus/產品版本、detector/matcher/RANSAC 設定、keypoint distribution、match/inlier coverage、residual tail、失敗影像與下游 gate。

## 視覺 primitive

- `input_roi`：兩張有紋理的 reference/current ROI。
- `feature_correspondence`：keypoints、descriptor matches、ratio test。
- `geometry_solver`：RANSAC inliers、transform 與 residual。
- `coverage_gate`：inlier 空間分布，而非只看 match 數量。
- `uncertainty_gate`：低紋理、反光、週期圖樣與 tiny ROI reject。

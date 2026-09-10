# SIFT（`sift`）

- roadmap 分類：`geometry-alignment-measurement`
- 講義對照：`01-11`～`01-14`
- 內容覆蓋狀態：`complete`
- 產生狀態：`self-reviewed-tested; user-approval-pending`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/sift.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
同一金屬件在兩張圖裡旋轉、縮放或位置改變，整張外觀不容易直接重疊。SIFT先尋找有辨識力的局部，再把局部變成可比較的描述，提供幾何定位所需的點對。

### 它交出什麼，也不交出什麼
SIFT交付關鍵點、尺度／方向與描述子；搭配matcher得到點對。需要平面單應、相機運動或工件定位時，另外選合適的幾何模型與求解器；描述子本身不交付warp。

### 一句心智模型
SIFT跨尺度尋找穩定局部，為關鍵點選擇尺度與主方向；在相對主方向的局部座標裡彙整梯度方向分布，形成描述子。兩張圖的描述子再經匹配與含糊候選篩選，得到對應點；幾何求解與驗證是後一步。

**限制：** 同一缺口被模糊後，局部方向與細節變弱，原本可區分的候選可能混在一起。更多點或更多線不必然更可靠；要看正確對應、幾何分布及獨立核對。

### 換一個現場再推理
新工件有規則排列的相同圓孔，另一件只有少量但獨特的缺口。兩者都要找平面位置。

**問題：** 應直接選匹配線比較多的一件作為可靠案例嗎？傳統匹配與學習配對怎麼比較？

**核對：** 重複圓孔可能給很多相似描述，線多卻錯；少量獨特缺口若正確且分布非退化，反而可能提供較有用幾何約束。先固定兩組影像，檢查對應身份、空間分布與幾何誤差，再比較SIFT匹配和相容LightGlue流程的完整成本。若影像本身無可區分線索，補取像或標靶可能比換matcher更有效。
<!-- topic-learning-bridge:end -->
<!-- wi032-model-core:start -->
## WI-032 核心做法與工作取捨

SIFT跨尺度尋找穩定局部，為關鍵點選擇尺度與主方向；在相對主方向的局部座標裡彙整梯度方向分布，形成描述子。兩張圖的描述子再經匹配與含糊候選篩選，得到對應點；幾何求解與驗證是後一步。

同一缺口被模糊後，局部方向與細節變弱，原本可區分的候選可能混在一起。更多點或更多線不必然更可靠；要看正確對應、幾何分布及獨立核對。

無需訓練且局部紋理可區分時，SIFT配傳統匹配可作起點；含糊候選需更多上下文時可試LightGlue及相容extractor。ECC適合有起點後依密集外觀微調；ChArUco提供已知標靶的相機幾何。這些工具可分工，不能直接用不同任務分數排名。

換工件時通常不用訓練SIFT，但仍需新參考影像、尺度／取像與匹配門檻驗證；若改用LightGlue，須核對extractor與matcher權重相容性。比較完整找點、描述、配對、幾何估計與覆核成本。

準備同工件不同視角與合理重疊的清楚影像，固定前處理；先看關鍵點能否覆蓋要定位的區域，再選匹配與幾何驗證方式。

保存關鍵點、描述子設定、候選／篩選後點對、幾何內點與誤差；另測模糊及重複紋理。平面單應可由4組合適的非退化正確點對求解，但點少、錯配或分布退化仍需警惕，不能單憑數量下結論。本輪插圖是示意，既有120點／104匹配記錄不冒稱本輪新實測。

來源：https://docs.opencv.org/4.13.0/da/df5/tutorial_py_sift_intro.html

版本及示意界線見工作項目 sources.md。使用者成品核准pending。
<!-- wi032-model-core:end -->
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

<!-- wi032-engineering:start -->
## 工程層：輸入、機制、部署與限制

### SIFT先找特徵，再交給配對器

SIFT透過尺度空間極值與局部定位找點，分配主方向後計算局部梯度描述子。匹配器以描述子尋找點對；單應、姿態或對齊並不是SIFT本身的輸出。

SIFT特徵、matcher點對與幾何變換分開。

來源：https://docs.opencv.org/4.13.0/da/df5/tutorial_py_sift_intro.html

### 描述子比較的是局部方向分布

標準SIFT描述子為4×4空間格、每格8方向，共128維；實作含加權、正規化及截斷等步驟。最近與次近描述子距離比可用來篩掉含糊候選，但閾值須用目標資料驗證。

ratio test篩含糊候選，不是幾何真值證明。

來源：https://docs.opencv.org/4.13.0/da/df5/tutorial_py_sift_intro.html

### 點對夠多，仍要看幾何分布

四組合適的非退化平面對應可求單應；大量共線或錯配點仍可能不可用。需要按工作選模型，RANSAC篩選內點后仍看空間覆蓋與獨立地標誤差。

數量、正確性與分布要一起看。

來源：https://docs.opencv.org/4.13.0/da/df5/tutorial_py_sift_intro.html

### 有視差時，一張平面warp未必夠

SIFT可提供局部對應，但場景有非平面視差時，單一單應未必能同時對齊全部深度。不能把此時的殘差全部解釋成特徵錯配，需檢查模型適用范圍。

匹配失敗與幾何模型不適用，要分開診斷。

來源：https://docs.opencv.org/4.13.0/da/df5/tutorial_py_sift_intro.html

<!-- wi032-engineering:end -->


## WI-032 歷史案例的證據範圍

R06原圖標示「教學示意，非實測」。原圖數字可用於查閱既有教學案例；本輪沒有重跑產生程序，也不以此宣稱現場性能。圖內舊簡寫不取代本輪機制與條件说明。

- [歷史R06教學示意原圖：配對數與模糊案例（非本輪實測）](images/final/WI032-retained-sift-r06-c2-how.png)
- [歷史R06教學示意原圖：配對數與模糊案例（非本輪實測）](images/final/WI032-retained-sift-r06-d4-stop.png)

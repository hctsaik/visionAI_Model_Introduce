# ECC（`ecc`）

- roadmap 分類：`geometry-alignment-measurement`
- roadmap 節點：`ECC`
- 講義對照：`01-07`～`01-10`
- 內容覆蓋狀態：`complete`
- 產生狀態：`self-reviewed-tested; user-approval-pending`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/ecc.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
治具已把同一金屬件放到大致位置，但每次仍有小偏移。若直接做固定ROI檢查，孔邊緣的位置差會混進結果；ECC用模板與待對圖的外觀，微調它們的幾何對齊。

### 它交出什麼，也不交出什麼
交付帶方向定義的warp、相關值及對齊取樣設定；另保存獨立殘差與原圖。後續ROI檢查接對齊影像，但不能把warp或相關分數當成缺陷標記。

### 一句心智模型
每輪依目前幾何變換把待對圖重採樣到可比較的座標，再比較與模板的外觀相關，計算變換更新並繼續迭代。圖中同孔的雙邊與強度曲線由錯位變接近，解釋它靠什麼調整；不是逐點描述子匹配，也不是缺陷分類。

**限制：** 同一兩孔件若從太遠的位置開始，局部孔緣相似可能產生錯誤解；必須同時看整件外框與同身份孔位。局部重合不代表整件對齊，相關值也不能取代獨立幾何核對。

### 換一個現場再推理
同一產線95%的工件已由治具放得很接近，另外5%會偏移很遠；每件容許的完整處理時間有限。

**問題：** 全部增加ECC迭代，與先判起點／必要時做粗定位，兩條路各有什麼條件？

**核對：** 若失敗主要來自近起點但迭代尚未收斂，可在時間預算內比較較多迭代；不能預設它會救回遠起點。若遠移動是主要失敗來源，可用粗定位或特徵匹配先建立合理起點，再接ECC；增加的前處理要與漏對、錯收斂及覆核成本一起量。用相同測試影像核對完整時間和獨立殘差後再選，不憑相關值最高就放行。
<!-- topic-learning-bridge:end -->
<!-- wi032-model-core:start -->
## WI-032 核心做法與工作取捨

每輪依目前幾何變換把待對圖重採樣到可比較的座標，再比較與模板的外觀相關，計算變換更新並繼續迭代。圖中同孔的雙邊與強度曲線由錯位變接近，解釋它靠什麼調整；不是逐點描述子匹配，也不是缺陷分類。

同一兩孔件若從太遠的位置開始，局部孔緣相似可能產生錯誤解；必須同時看整件外框與同身份孔位。局部重合不代表整件對齊，相關值也不能取代獨立幾何核對。

已經接近且外觀穩定時，可先用ECC微調；有可區分局部且需要較大範圍定位時，可先試SIFT匹配再做幾何估計，含糊匹配可評估LightGlue及相容extractor。ChArUco負責相機幾何，並非這些逐件定位的直接替代品。

換產品時要換模板、ROI／mask並重新驗證變換模型與起點範圍；固定相機也可能因光照或遮擋增加錯收斂。比較成本要包含粗定位、ECC迭代、重採樣與失敗覆核，不只計單次函式耗時。

準備同工作座標下的模板與待對圖，選平移／剛性／仿射或單應模型及合理起點，確認灰階、mask、解析度與重採樣方向一致。

保存原圖、初始／最終warp、相關值、迭代設定及獨立地標殘差，測不同起點、光照、遮擋與重拍。既有32/12位移與遠起點失敗資料保留來源；本輪新圖是概念示意，不是新跑的ECC結果。

來源：https://docs.opencv.org/4.13.0/dc/d6b/group__video__track.html

版本及示意界線見工作項目 sources.md。使用者成品核准pending。
<!-- wi032-model-core:end -->
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

<!-- wi032-engineering:start -->
## 工程層：輸入、機制、部署與限制

### ECC交付的是warp與相關值

OpenCV findTransformECC回傳相關值並更新warpMatrix。對齊影像需另行warp，獨立地標殘差與下游檢查也需另外計算；不把概念曲線當真實迭代紀錄。

相關值不是缺陷標記，也不是獨立定位誤差。

來源：https://docs.opencv.org/4.13.0/dc/d6b/group__video__track.html

### 一輪ECC：取樣、比較、更新

同一物件的強度曲線僅用來顯示錯位如何影響比較。ECC局部最優化依照當前幾何和強度計算參數更新；過遠初始位置、遮擋或模型不適用仍可能失敗。

靠密集外觀更新幾何，不靠逐點描述子。

來源：https://docs.opencv.org/4.13.0/dc/d6b/group__video__track.html

### warp方向錯了，影像就會往反方向移

OpenCV findTransformECC的warp常配warpAffine/warpPerspective及WARP_INVERSE_MAP，把input重採樣至template座標。若交換角色或自行取逆矩陣，旗標也必須一致；用已知平移點做驗證，不憑圖看起來像就認為方向正確。

先寫清楚映射方向，再決定反矩陣與取樣設定。

來源：https://docs.opencv.org/4.13.0/dc/d6b/group__video__track.html

### 局部相關高，整件仍可能對錯

既有32/12平移及遠起點失敗案例保留在舊正式圖及來源紀錄，並非本輪重新執行。這張圖補說如何核對孔位身份、外框與失敗處理，不用單一相關值放行。

用獨立幾何與完整失敗成本決定是否採用。

來源：https://docs.opencv.org/4.13.0/dc/d6b/group__video__track.html

<!-- wi032-engineering:end -->


## WI-032 歷史案例的證據範圍

R06原圖標示「教學示意，非實測」。原圖數字可用於查閱既有教學案例；本輪沒有重跑產生程序，也不以此宣稱現場性能。圖內舊簡寫不取代本輪機制與條件说明。

- [保留的反光／遮擋／視差案例原圖（依原圖標示判讀，本輪未重跑）](images/final/ECC-04-selection-boundary_v03-r04.png)
- [歷史R06教學示意原圖：位移與起點案例（非本輪實測）](images/final/WI032-retained-ecc-r06-c3-get.png)
- [歷史R06教學示意原圖：位移與起點案例（非本輪實測）](images/final/WI032-retained-ecc-r06-d4-stop.png)

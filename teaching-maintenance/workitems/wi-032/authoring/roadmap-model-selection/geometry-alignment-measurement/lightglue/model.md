# LightGlue（`lightglue`）

- roadmap 分類：`geometry-alignment-measurement`
- 講義對照：`01-15`～`01-18`
- 內容覆蓋狀態：`complete`
- 產生狀態：`self-reviewed-tested; user-approval-pending`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/lightglue.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
兩個孔看起來很像，只比較各自局部描述可能把孔位配錯。LightGlue接收上游找到的點和描述，讓同圖與跨圖訊息共同更新配對，幫助分辨含糊候選。

### 它交出什麼，也不交出什麼
交付點對、匹配信心等配對結果；上游找點、後端RANSAC／幾何變換與對齊取樣另有負責者。孔位身份、單應適用性與工站誤差仍由後續流程驗證。

### 一句心智模型
先由相容extractor提供關鍵點與描述；LightGlue以圖內與跨圖注意力更新表示，再估計點對與可匹配性。圖中缺口A的對應提供上下文，使孔B的兩條候選線收斂為較明確的配對。可可靠判斷的低可匹配點可被修剪，容易的配對也可提早停止；配對後仍需幾何求解與驗證。

**限制：** 當獨特缺口被遮住，兩個可見孔又很相似，上下文可能仍不足。模型不能憑空知道被遮住的外觀；保留不確定並補視角或定位特徵，比把某條高信心線直接當幾何真值更可靠。

### 換一個現場再推理
相同孔位工件只露出兩個很像的孔；另一組影像保留了獨特缺口，但傳統描述子仍有含糊候選。

**問題：** 兩組都換LightGlue就能解決嗎？如何安排小規模比較？

**核對：** 只有兩個相似孔且缺乏其他線索時，先補視角、解除遮擋或增加已知定位點，不能要求配對器猜出身份。保留獨特缺口但傳統匹配含糊的那組，可以比較相容LightGlue流程與傳統matcher；固定影像與幾何核對，量錯配、定位誤差和完整成本。若原流程已穩定且成本低，保留傳統方法也是合理選擇。
<!-- topic-learning-bridge:end -->
<!-- wi032-model-core:start -->
## WI-032 核心做法與工作取捨

先由相容extractor提供關鍵點與描述；LightGlue以圖內與跨圖注意力更新表示，再估計點對與可匹配性。圖中缺口A的對應提供上下文，使孔B的兩條候選線收斂為較明確的配對。可可靠判斷的低可匹配點可被修剪，容易的配對也可提早停止；配對後仍需幾何求解與驗證。

當獨特缺口被遮住，兩個可見孔又很相似，上下文可能仍不足。模型不能憑空知道被遮住的外觀；保留不確定並補視角或定位特徵，比把某條高信心線直接當幾何真值更可靠。

局部特徵已能分清時，可先用SIFT搭傳統matching減少部署複雜度；候選含糊時再以同資料評估LightGlue及其相容extractor。ECC使用的是密集外觀的局部對齊，ChArUco提供已知幾何校正，不能互換角色。

換工件需重查重疊、紋理與幾何結果，未必需要重訓，但也不能假設預訓練配對器可直接保證工業件準確。記錄extractor與matcher權重、影像縮放及停止／修剪設定，測CPU/GPU和完整鏈成本。

選相容extractor與LightGlue預訓練權重，準備有重疊且可獨立核對的影像對；先保存點與描述，再觀察匹配如何改變，最後接合適的幾何模型。

保存輸入、權重版本、extractor設定、點對／信心、修剪與停止設定，以及幾何內點、誤差和完整耗時；用同影像比較傳統matcher。本輪新圖只解釋候選更新，沒有執行LightGlue權重推論。

來源：https://github.com/cvg/LightGlue

版本及示意界線見工作項目 sources.md。使用者成品核准pending。
<!-- wi032-model-core:end -->
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

<!-- wi032-engineering:start -->
## 工程層：輸入、機制、部署與限制

### 配對器前後各有負責的步驟

官方提供多種extractor相容設定，部署應記錄權重、前處理與影像尺寸。點對與匹配信心不等於幾何準確率，後端求解與工作驗證仍需另行負責。

LightGlue不取代找點，也不直接給工站姿態。

來源：https://github.com/cvg/LightGlue

### 圖內關係與跨圖關係，一起更新表示

LightGlue交替使用self-/cross-attention更新局部表示，再結合匹配分配與matchability；一些點沒有可靠對應時允許不匹配。圖為機制示意，無真實注意力或信心數值。

不是每個點都必須硬配到另一張圖。

來源：https://github.com/cvg/LightGlue

### 自適應計算：少算什麼，要分清楚

自適應深度依信心提前停止，寬度修剪部分低可匹配點以減少後續計算；實際門檻與后端實現有關。完整時間包含extractor、資料搬移、matcher及幾何估計，不能只用名稱宣稱更快。

自適應不是每張圖都更快的保證。

來源：https://github.com/cvg/LightGlue

### 少重疊或對稱物，先確認是否有線索

用相同影像與獨立幾何證據比較傳統matcher及LightGlue；無法觀測的獨特細節不是換配對器一定能補回。優先核對重疊、紋理與遮擋，再決定是否換算法。

看不見或分不出的部分，不能要求模型猜對。

來源：https://github.com/cvg/LightGlue

<!-- wi032-engineering:end -->

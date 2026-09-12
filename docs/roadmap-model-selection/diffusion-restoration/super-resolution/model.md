# Super-resolution（`super-resolution`）

- roadmap 分類：`diffusion-restoration`
- roadmap 節點：`Super-resolution`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-prototype`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/super-resolution.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
舊相機拍到的金屬邊緣只有少量像素，放大後呈階梯，想提升檢視細節。

### 它交出什麼，也不交出什麼
高解析度估計圖，供檢視或另行驗證的下游處理；保留低解析原圖。

### 一句心智模型
插值只依既有像素計算放大後的值；學習式超解析使用訓練所得的邊緣與紋理規律，估計較高解析度的內容。CNN、Transformer或擴散模型都可做這個任務。圖中插值和學習式路徑是可比較的方案，不是每個模型都必須先插值再生成。

**限制：** 第二圖改用兩孔圓板的右下邊緣。同一粗像素區可能由有小缺口或無缺口的高解析邊緣降採樣而來。超解析選出其中一種，不表示缺口已被量到；需要真正有解析力的取像或獨立證據判斷。

### 換一個現場再推理
放大圖讓拉絲更漂亮，但缺口位置在不同方法間不一致；更高解析相機要增加取像成本。

**問題：** 哪些工作可以先用超解析，哪些應投資取像？

**核對：** 外觀檢視可測超解析並標明估計；關鍵缺口量測要以具有足夠解析力的真實取像及校正驗證。用相同已知缺口比較插值、前饋與擴散的假細節、定位誤差和時間；更漂亮不等於更適合量測。
<!-- topic-learning-bridge:end -->
<!-- wi026-model-core:start -->
## WI-026 核心做法與工作取捨

插值只依既有像素計算放大後的值；學習式超解析使用訓練所得的邊緣與紋理規律，估計較高解析度的內容。CNN、Transformer或擴散模型都可做這個任務。圖中插值和學習式路徑是可比較的方案，不是每個模型都必須先插值再生成。

第二圖改用兩孔圓板的右下邊緣。同一粗像素區可能由有小缺口或無缺口的高解析邊緣降採樣而來。超解析選出其中一種，不表示缺口已被量到；需要真正有解析力的取像或獨立證據判斷。

先與插值基準比較，再按延遲與細節需求測前饋或擴散式超解析。去模糊解拖影，超解析解低採樣，混合退化要選能處理相應條件的流程；擴散是做法而非第三個互斥任務。

只有正常高解析圖可以做降採樣對照，但不能證明未知微缺陷保留。換相機與材質需重驗噪聲、採樣與紋理。輸出不是像素真值或直接尺寸；同資料比較假紋理、邊界偏差、下游錯誤和總時間，別只看圖片變大。

來源：https://arxiv.org/abs/2104.07636

圖為AI生成教學示意；原工程段落為補充，首讀新版以本段及topic為準。使用者成品核准pending。
<!-- wi026-model-core:end -->
## 角色與安全邊界

Super-resolution（SR）從低解析影像估計高解析版本，是 inverse problem／生成 family。它不能創造感測器未量到的可靠 micro-defect evidence；model、scale 與 degradation 必須鎖定。

輸出一律是 `high-resolution estimate x-hat`。任何 texture、line width、micro-defect 或 CD 的主張都必須回到原始 capture 或 calibration target，不得以 SR output 當唯一 PASS／FAIL。

## 視覺因果 brief（產圖前必填）

### 07-30｜身份與問題（C）

1. **十秒句**：SR 把低解析影像估成高解析候選，不能把未量到的微小 defect 變成可靠證據。
2. **輸入物件**：low-resolution wafer ROI、pixel grid、scale factor 與原始 capture。
3. **方法／轉換**：upsampling CNN／transformer／diffusion prior 依 lock 的 scale／degradation 估計高解析 `x-hat`。
4. **可觀察輸出**：high-resolution estimate、放大 texture、alias／hallucination map 與 raw reference。
5. **工程決策**：可做檢視輔助或訓練研究；微缺陷與尺寸不可直接宣稱存在。
6. **箭頭對照表**：`low-resolution y → scale / degradation → SR prior → high-resolution x-hat → raw / artifact review`。

### 07-31｜架構（C）

1. **十秒句**：SR 的重建 loss、feature prior 與 generative prior 決定它偏向平滑或補出感知細節。
2. **輸入物件**：low-resolution `y`、scale、resize kernel／degradation 及 ROI。
3. **方法／轉換**：upsampling CNN／transformer／diffusion prior 將 `y` 估為 `x-hat`。
4. **可觀察輸出**：放大 estimate、texture／aliasing uncertainty 與 calibration reference。
5. **工程決策**：若 SR 與 ground truth 在關鍵 micro-pattern 不一致，改回高解析取像或只保留人工輔助用途。
6. **箭頭對照表**：`LR y → scale / degradation → SR prior → HR x-hat → texture / alias check`。

### 07-32｜建置與推論（C）

1. **十秒句**：不鎖 scale、resize kernel、degradation、tile overlap 與 sampling，就無法重播或比較 SR 的 hallucination。
2. **輸入物件**：paired LR／HR、calibration target、tile boundary 與 scale-stratified samples。
3. **方法／轉換**：鎖 scale、resize kernel、degradation、checkpoint、tile overlap、seed／steps。
4. **可觀察輸出**：paired fidelity、uncertainty／hallucination map、tile seam failure、VRAM／P95。
5. **工程決策**：以 paired ground truth 與 calibration target 驗證，而不是只比 PSNR 或畫面銳利度。
6. **箭頭對照表**：`LR/HR pair → fixed scale/degradation → fixed SR/tile contract → fidelity/alias/P95 → human review`。

### 07-33｜工程選型（D）

1. **十秒句**：高解析候選看似有 micro-detail，也不能用它宣稱實際 CD 或 defect 存在。
2. **輸入物件**：同一張 LR ROI、scale 與 calibration／HR reference。
3. **方法／轉換**：左側拿 SR texture 做 PASS／FAIL；右側保存 LR、SR、scale／degradation、uncertainty 並以 paired target／review 限定用途。
4. **可觀察輸出**：左側有 hallucinated texture／alias risk；右側有 LR-to-SR relation、calibration evidence、artifact map 與 human review。
5. **工程決策**：可用於非關鍵檢視、訓練研究；不得以 SR output 宣稱實際 CD、defect 或唯一 PASS／FAIL。
6. **箭頭對照表**：`SR texture 當量測（失敗） → 保留 LR/scale/artifact 並驗證（限定輔助用途）`。

## 模型專屬欄位

- `architecture_path`：`low-resolution y → scale / resize-kernel / degradation → upsampling CNN / transformer / diffusion prior → high-resolution estimate x-hat + uncertainty`。
- `representation_or_score`：SR 重建 loss／feature prior／generative prior 決定平滑或感知細節；輸出是 estimate，不是新增量測。
- `cost_and_operating_point`：鎖 scale、resize kernel、degradation、checkpoint、tile overlap、seed／steps；量測 VRAM、tile seam 與 P95。
- `failure_boundary`：texture hallucination、aliasing、tile seam、跨 domain、scale mismatch；不得將 SR output 做 CD、defect existence 或唯一 PASS／FAIL。
- `selection_gate`：paired LR／HR 或 calibration target 的 fidelity 與 hallucination 檢查；human／specialist review 限定用途。
- `evidence_bundle`：LR raw、scale、resize/degradation trace、checkpoint/sampling、SR estimate、uncertainty／artifact map、paired metrics、tile/P95、review decision。

## 必須畫出的視覺 primitive

- `low_resolution_raw`
- `scale_and_degradation`
- `upsampling_or_sr_prior`
- `high_resolution_estimate`
- `texture_or_aliasing_risk`
- `raw_measurement_gate`

## 交付頁面

| Course page | 頁型 | 核心回答 |
|---|---|---|
| 07-30 | C | 為何 SR 高解析圖不是 micro-defect 證據？ |
| 07-31 | C | scale 與 degradation 如何進入 SR prior？ |
| 07-32 | C | 哪些設定必須鎖定才能比較？ |
| 07-33 | D | 為何 SR 不能直接做 CD／PASS-FAIL？ |

## 產生 gate

已完成六欄位與頁面級視覺因果 brief。產圖後依根目錄 `IMAGE_STYLE_GUIDE.md` 11.10 做三秒、十秒與逐物件語意驗收；使用者確認意義與風格前一律標記 `in-review`。

<!-- wi033-engineering:start -->
## WI-033 工程圖修正

### 超解析：輸入採樣與輸出像素分清

同矩形板大左小右孔，固定q；保存原解析度、縮放倍率、退化假設與模型版本，輸出不是新增相機資料。

輸出更密，仍要保留原始低解析影像。

來源：https://arxiv.org/abs/2104.07636

### 超解析：由低採樣估計高解析候選

維持大左孔/小右孔矩形板，固定左孔邊q。低解析格可經插值或學習先驗變高解析；輸出細節是估計。給定局部兩子像素[20,80]與[40,60]平均同50，只說明非唯一，不聲稱這兩例直接對應有缺口/無缺口。指定主反例也改矩形同板同q。

更多輸出像素，不等於更多相機觀測。

來源：https://arxiv.org/abs/2104.07636

### 超解析：倍率改變像素量與成本

作者100×100到200×200由1萬到4萬像素，只是存儲/輸出量，不保證速度固定四倍。需實测延遲與細節保真，沒有本輪實測。

放大倍率和真實細節改善要分開驗。

來源：https://arxiv.org/abs/2104.07636

### 超解析：插值與生成如何取捨

插值成本通常較簡但不能恢復缺失細節；學習式使用先驗且可能幻覺。固定真實取像、退化、硬體與下游任務比較，不用跨論文排名。

同原圖比較細節保真與成本，不只看銳利。

來源：https://arxiv.org/abs/2104.07636

<!-- wi033-engineering:end -->

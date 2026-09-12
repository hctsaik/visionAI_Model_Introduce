# Diffusion Restoration（`diffusion-restoration`）

- roadmap 分類：`diffusion-restoration`
- roadmap 節點：`Diffusion Restoration`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-prototype`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/diffusion-restoration.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
舊AOI影像有雜訊或模糊，想讓工程師更容易看清結構，同時知道哪些細節只是估計。

### 它交出什麼，也不交出什麼
較清楚的復原估計，配合原觀測核對；可支援閱讀或另行驗證過的下游流程。

### 一句心智模型
擴散模型先從訓練資料學會清晰影像的規律。復原時把退化觀測或退化模型當條件，在反覆去噪中估計可能的清晰影像。圖中的『套回退化再比觀測』說明一致性檢查：候選不能只符合外觀先驗，也要能解釋原觀測；具體約束位置與方式依方法而異。

**限制：** 原觀測太模糊時，有裂紋及無裂紋兩個清晰候選，套回退化後都可能近似同一觀測。觀測一致是必要線索，仍不能唯一確定原來的細節；殘差也不直接等於缺陷機率或可信度。

### 換一個現場再推理
擴散候選細節漂亮卻在不同取樣間改變裂紋；快速模型結果平滑，產線又有時間限制。

**問題：** 會以清晰度選擴散，還是如何設計比較？

**核對：** 先用同一真實清晰對照與缺陷留出資料，量關鍵細節保留、假影、下游錯誤及總時間。快速模型可作基準；若兩者都不能確認裂紋，就改善取像或保留覆核，不能用漂亮細節代替證據。
<!-- topic-learning-bridge:end -->
<!-- wi026-model-core:start -->
## WI-026 核心做法與工作取捨

擴散模型先從訓練資料學會清晰影像的規律。復原時把退化觀測或退化模型當條件，在反覆去噪中估計可能的清晰影像。圖中的『套回退化再比觀測』說明一致性檢查：候選不能只符合外觀先驗，也要能解釋原觀測；具體約束位置與方式依方法而異。

原觀測太模糊時，有裂紋及無裂紋兩個清晰候選，套回退化後都可能近似同一觀測。觀測一致是必要線索，仍不能唯一確定原來的細節；殘差也不直接等於缺陷機率或可信度。

先分任務：模糊要去模糊，低解析要超解析，雜訊要去噪；擴散是可支援這些任務的一種做法。延遲嚴格時可先測傳統或前饋基準；多步生成的細節能力是否值得成本，須由相同資料上的錯誤與時間判斷。

只有正常清晰圖可製作受控退化對照，但不保證模擬了現場退化或保留真缺陷。換相機／材質需重驗退化假設與模型。輸出是影像估計，非直接缺陷分數或輪廓；比較原圖與復原後下游漏檢、誤報、假影及端到端時間。

來源：https://arxiv.org/abs/2201.11793

圖為AI生成教學示意；原工程段落為補充，首讀新版以本段及topic為準。使用者成品核准pending。
<!-- wi026-model-core:end -->
## 角色與安全邊界

Diffusion Restoration 是以 diffusion prior 復原退化影像的任務／方法家族；每個實作都必須指定 degradation model、condition、checkpoint 與 sampling。它能改善**可讀性**，但不能保證復原相機沒有量到的物理細節。

它的輸出一律標示為 `restored estimate`。原始退化影像、restored output、residual／uncertainty 與參數 trace 必須一起保存；關鍵 defect、尺寸與放行決策不得只依 restored pixels。

## 視覺因果 brief（產圖前必填）

### 07-22｜身份與問題（C）

1. **十秒句**：Diffusion Restoration 可以把退化影像變成可讀的 estimate，但不能把 estimate 當成原始量測。
2. **輸入物件**：有 blur、noise 或 compression artifact 的晶圓 AOI 影像與 ROI。
3. **方法／轉換**：工程師聲明 degradation／condition，diffusion denoiser 走反向復原路徑。
4. **可觀察輸出**：restored estimate、與 raw 對照、residual／uncertainty 以及耗時。
5. **工程決策**：可供 human-assist 或候選研究；關鍵決策回查 raw image。
6. **箭頭對照表**：`degraded image → degradation condition → reverse diffusion → restored estimate → raw/residual review`。

### 07-23｜架構（C）

1. **十秒句**：復原品質取決於退化假設與反向 denoising，而不是把影像單純「變清楚」。
2. **輸入物件**：degraded image `y`、blur／noise／compression condition 與 ROI。
3. **方法／轉換**：以 checkpoint 的 reverse diffusion／denoiser steps 估計 `x-hat`。
4. **可觀察輸出**：restored `x-hat`，同時可看見 raw 及 residual／uncertainty。
5. **工程決策**：若 residual 集中在關鍵區或 uncertainty 過高，改回取像／重新驗證。
6. **箭頭對照表**：`y → degradation/condition → reverse diffusion steps → x-hat → residual + uncertainty`。

### 07-24｜建置與推論（C）

1. **十秒句**：不鎖 degradation、checkpoint、sampling 與 tile 設定，就不能重播也不能比較復原結果。
2. **輸入物件**：paired 或 controlled-degradation 的影像、raw capture 與 calibration target。
3. **方法／轉換**：固定 blur/noise/compression model、checkpoint、steps、guidance、seed、resolution 與 tile stitch。
4. **可觀察輸出**：fidelity、hallucination failure gallery、steps／VRAM／P95 與 trace bundle。
5. **工程決策**：以 controlled pair 與真實 degraded holdout 驗證；不以單張「更清楚」決定採用。
6. **箭頭對照表**：`paired data → fixed degradation → fixed inference contract → fidelity/failure/P95 → human review`。

### 07-25｜工程選型（D）

1. **十秒句**：視覺上更清楚的 restored image 不等於可用量測；保留 raw、residual 與 uncertainty 後，才能限定安全用途。
2. **輸入物件**：同一張 degraded AOI image、ROI 與 calibration／raw reference。
3. **方法／轉換**：左側將 restored pixels 當唯一證據；右側保留 evidence bundle 並以 human review 判定輔助用途。
4. **可觀察輸出**：左側只有漂亮 estimate；右側有 raw、restored、residual／uncertainty、P95 與 review。
5. **工程決策**：可用於 human-assist、非關鍵可讀性或下游候選研究；不能直接送量測或當唯一 AD evidence。
6. **箭頭對照表**：`將 estimate 當證據（失敗） → 保留 raw/residual/uncertainty 並 review（可限定用途）`。

## 模型專屬欄位

- `architecture_path`：`degraded image y + degradation/condition → reverse diffusion / denoiser steps → restored estimate x-hat + residual/uncertainty`。
- `representation_or_score`：退化影像與 condition 是輸入；輸出為 estimate 而非觀測真值。residual／uncertainty 用於揭露復原不可靠區。
- `cost_and_operating_point`：記錄 diffusion steps、VRAM、P95、resolution、tile overlap／stitch 與 guidance；高步數不等於可用證據。
- `failure_boundary`：detail invention、domain mismatch、tile seam、高延遲、關鍵區 residual 或 uncertainty 偏高；不能將 restored pixels 當唯一量測或 AD evidence。
- `selection_gate`：先用 paired／controlled degradation 證明 fidelity，再用真實 degraded holdout 查 hallucination；以 specialist／human review 決定可用範圍。
- `evidence_bundle`：degraded raw、condition／degradation model、checkpoint、sampling trace、restored estimate、residual／uncertainty、fidelity／failure、P95 與 reviewer decision。

## 必須畫出的視覺 primitive

- `degraded_raw_image`
- `degradation_condition`
- `reverse_diffusion_path`
- `restored_estimate`
- `residual_or_uncertainty`
- `raw_evidence_gate`

## 交付頁面

| Course page | 頁型 | 核心回答 |
|---|---|---|
| 07-22 | C | 復原後的圖為何仍只是 estimate？ |
| 07-23 | C | degradation condition 如何進入 reverse diffusion？ |
| 07-24 | C | 哪些參數必須鎖定才能重播與驗證？ |
| 07-25 | D | restored image 何時可用、何時不可當證據？ |

## 產生 gate

已完成六欄位與頁面級視覺因果 brief。產出前仍須依根目錄 `IMAGE_STYLE_GUIDE.md` 11.10 完成三秒、十秒與逐物件的語意驗收；使用者明確確認 prototype 的意義與風格前，所有輸出均為 `in-review`。

<!-- wi033-engineering:start -->
## WI-033 工程圖修正

### 擴散復原：先說清楚觀測退化

線性逆問題示意，保存A/噪聲假設與原觀測；候選再退化對回y並檢未觀測細節，不把低殘差當真值。 r01實看修正：比較A估計與原觀測，依噪聲模型檢殘差；不宣稱知道真實n。

復原候選與原始觀測需一起交付。

來源：https://arxiv.org/abs/2201.11793

### 擴散復原：估計後，套回觀測條件

同中部雙孔板。以線性退化y=Ax+n為例，預訓練擴散先驗與已知觀測/退化條件形成候選；不同方法條件接法不同，不概括為單一演算法。作者兩像素平均算子：[0,100]及[40,60]都得50，證明非唯一；不把某次採樣當真值。

退化後相符是必要核對，不能證明細節唯一。

來源：https://arxiv.org/abs/2201.11793

### 擴散復原：退化假設與採樣要配套

保存模型、退化算子、噪聲與步數種子；不同候選一致不保證唯一真實。時間要含每步去噪及資料一致性。 r01實看修正：依噪聲模型驗殘差，並將結論寫成明確可做的條件核對。

退化條件改變，模型與驗證也要重新核對。

來源：https://arxiv.org/abs/2201.11793

### 擴散復原：錯退化也會給漂亮結果

作者反例把加性雜訊當卷積模糊，假設錯誤可引入不必要輪廓。需檢退化與獨立成像，不以漂亮結果證明模型合適。 r01實看修正：錯退化反例保留完整同板，在右外框畫多重邊；噪聲容許條件明寫。

先驗看起來合理，仍可能不符合取像原因。

來源：https://arxiv.org/abs/2201.11793

<!-- wi033-engineering:end -->

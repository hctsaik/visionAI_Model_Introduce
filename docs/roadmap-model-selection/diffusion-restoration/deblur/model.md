# Deblur（`deblur`）

- roadmap 分類：`diffusion-restoration`
- roadmap 節點：`Deblur`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-prototype`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/deblur.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
輸送中的金屬板在曝光期間移動，孔邊與外框拖開，影響人工判讀或後續定位。

### 它交出什麼，也不交出什麼
去模糊後的清晰估計；核對邊緣、重影和下游定位是否改善。

### 一句心智模型
模糊把原本局部的訊號散到周圍：運動可能形成方向性拖影，失焦則有不同的擴散形狀。去模糊利用已知或估計的退化線索與影像先驗，反推清晰候選；可用傳統反卷積，也可用直接學模糊到清晰的網路，不一定顯式輸出模糊核。

**限制：** 假設復原後在直邊旁多出平行明暗線，這可能是振鈴假影。獨立清晰重拍只有一條邊；因此不能把復原後所有銳利線都當成裂紋或實體結構。

### 換一個現場再推理
模型在原速度有效，加速後外框多出雙線；重拍較慢，但可以增加照明縮短曝光。

**問題：** 先換更大的模型，還是比較取像與去模糊方案？

**核對：** 先確認拖影與曝光、運動的關係，用相同物件比較縮短曝光的取像改善及現有／新去模糊方法。看真實邊緣、假影、漏檢與完整節拍；更大模型可能增加延遲，也未必涵蓋新模糊。
<!-- topic-learning-bridge:end -->
<!-- wi026-model-core:start -->
## WI-026 核心做法與工作取捨

模糊把原本局部的訊號散到周圍：運動可能形成方向性拖影，失焦則有不同的擴散形狀。去模糊利用已知或估計的退化線索與影像先驗，反推清晰候選；可用傳統反卷積，也可用直接學模糊到清晰的網路，不一定顯式輸出模糊核。

假設復原後在直邊旁多出平行明暗線，這可能是振鈴假影。獨立清晰重拍只有一條邊；因此不能把復原後所有銳利線都當成裂紋或實體結構。

需求是去模糊，候選可含反卷積、前饋網路與擴散方法；超解析主要處理採樣不足，不能把兩者當同一件事。可改善取像時也把取像方案納入成本比較。

只有正常清晰圖可建立模擬拖影基準，仍需真實模糊與缺陷資料檢查漏檢。換速度／相機／鏡頭時重新核對退化。結果是影像估計，若需精密輪廓或尺寸，要另驗實際邊界誤差；比較推論、重拍、人工覆核的總時間。

來源：https://arxiv.org/abs/1711.07064

圖為AI生成教學示意；原工程段落為補充，首讀新版以本段及topic為準。使用者成品核准pending。
<!-- wi026-model-core:end -->
## 角色與安全邊界

Deblur 是模糊逆問題家族，目標從 motion blur 或 defocus blur 估計較清晰的影像。它不是固定模型；在導入 neural restoration 前，必須先確認曝光、振動、focus 或 PSF 是否能直接改善。

輸出一律是 `restored estimate x-hat`。未知 blur、ringing 與假邊緣會讓看似清晰的紋理失去量測意義；關鍵 defect detection 優先改善取像，deblurred output 不可作量測真值。

## 視覺因果 brief（產圖前必填）

### 07-26｜身份與問題（C）

1. **十秒句**：Deblur 可以提供較清楚的候選，但第一個工程問題應是能否修正曝光、振動或 focus，而非相信模型補出的邊緣。
2. **輸入物件**：有 motion／defocus blur 的晶圓 ROI、曝光與設備狀態。
3. **方法／轉換**：先辨識 blur source，再以 estimated kernel 或 neural inverse 估計清晰影像。
4. **可觀察輸出**：blurred raw、估計的 PSF／kernel、deblurred estimate 與可能的 ringing／假邊緣。
5. **工程決策**：關鍵 defect 優先修正取像；deblur 僅做非關鍵 visual assist。
6. **箭頭對照表**：`blurred y → blur source / PSF → inverse deblur → x-hat + artifact check → capture / review decision`。

### 07-27｜架構（C）

1. **十秒句**：Deblur 的核心是對 `k` 的假設，而不是把影像單純變清楚。
2. **輸入物件**：`blurred y ≈ k*x+n`、ROI、motion 或 defocus 對照。
3. **方法／轉換**：estimated kernel／PSF 或 implicit neural inverse 將 `y` 估成 `x-hat`。
4. **可觀察輸出**：清晰候選、edge residual、ringing／false-edge map。
5. **工程決策**：若 PSF 與現場不符或 false edge 過高，回到 exposure／stabilization／focus。
6. **箭頭對照表**：`y → k / PSF assumption → inverse operator → x-hat → false-edge / raw review`。

### 07-28｜建置與推論（C）

1. **十秒句**：沒有 paired blur data、PSF、曝光與實作版本的 deblur 結果，不能驗證細節是復原還是創造。
2. **輸入物件**：controlled target、raw capture、blur severity 分層樣本與 paired data。
3. **方法／轉換**：鎖 blur data／PSF、loss、exposure、restoration implementation 與 input capture settings。
4. **可觀察輸出**：severity-stratified fidelity、false-detail rate、ringing failure gallery 與 P95。
5. **工程決策**：控制 target 與 raw capture 共同驗證；不能以一張看似更清楚的圖採用。
6. **箭頭對照表**：`paired / target → fixed PSF / capture → fixed inverse → false-detail / P95 → specialist review`。

### 07-29｜工程選型（D）

1. **十秒句**：當關鍵缺陷被模糊時，先改善 exposure 或 stabilization；deblur 不得把 estimate 變成 defect evidence。
2. **輸入物件**：同一張 blurred ROI、曝光／振動資料與 raw reference。
3. **方法／轉換**：左側用 sharpened output 直接判 defect；右側先調整取像並保留 raw／PSF／artifact map，僅用 deblur 做 human-assist。
4. **可觀察輸出**：左側出現假邊緣風險；右側有 capture fix、raw、deblur、false-edge map 與 review。
5. **工程決策**：關鍵 defect 採取 exposure／stabilization／focus 改善；非關鍵檢視才可使用 deblur。
6. **箭頭對照表**：`sharpened estimate 當 defect evidence（失敗） → 改善 capture + 保留 artifact evidence（安全輔助）`。

## 模型專屬欄位

- `architecture_path`：`blurred y ≈ k*x+n → estimated kernel / PSF or neural inverse → deblurred estimate x-hat + artifact / edge residual`。
- `representation_or_score`：`k` 或 PSF 是退化假設；`x-hat` 是估計。false-edge／ringing map 揭露可能被創造的邊緣。
- `cost_and_operating_point`：鎖 exposure、blur severity、PSF、paired data、inverse implementation、P95；需要在不同 severity 分層報品質。
- `failure_boundary`：unknown blur、PSF mismatch、ringing、假邊緣、跨 domain 與延遲；不可拿 deblurred pixels 當量測真值。
- `selection_gate`：先查取像是否可改善；以 controlled target／paired raw capture 證明 fidelity，並由 specialist review false-detail rate。
- `evidence_bundle`：blurred raw、capture metadata、PSF／kernel assumption、implementation/version、deblurred estimate、artifact map、severity metrics、P95 與 reviewer decision。

## 必須畫出的視覺 primitive

- `blurred_raw_image`
- `blur_source_or_psf`
- `inverse_deblur_path`
- `deblurred_estimate`
- `false_edge_or_ringing_map`
- `capture_first_gate`

## 交付頁面

| Course page | 頁型 | 核心回答 |
|---|---|---|
| 07-26 | C | 為何取像修正優先於相信 deblur？ |
| 07-27 | C | `k`／PSF 假設如何進入 inverse？ |
| 07-28 | C | 哪些資料與設定必須鎖定？ |
| 07-29 | D | 關鍵缺陷為何不應由 deblur 決定？ |

## 產生 gate

已完成六欄位與頁面級視覺因果 brief。產圖後須依根目錄 `IMAGE_STYLE_GUIDE.md` 11.10 做三秒、十秒與逐物件語意驗收；使用者確認意義與風格前一律標記 `in-review`。

<!-- wi033-engineering:start -->
## WI-033 工程圖修正

### Deblur：模糊觀測與清晰參考分开

同板直邊，不只比較視覺清晰度；以同位置獨立短曝光/清晰圖驗邊緣偏移、假邊與下游量測。

去模糊是估計，量測需驗邊緣偏差。

來源：https://arxiv.org/abs/1612.02177

### Deblur：模糊邊緣反推清晰候選

同金屬板直邊橫切，真邊階躍與曝光平均展寬。傳統反卷積/學習式復原均輸出估計，圖示非某一特定模型架構；空間變化運動模糊不能用單一核概括。回套退化及獨立短曝光影像檢查重影/振鈴。不用可能缺字的近似符號，直接寫約等於。

清晰候選仍要用獨立觀測檢查假邊。

來源：https://arxiv.org/abs/1612.02177

### Deblur：速度、細節和假邊一起驗

物理移動/失焦與空間變化不同，模型訓練退化需對應。作者像素邊界100/102差2只示例，不是毫米或模型實測。 r01實看修正：真邊/估計/差值移出影像並以同色標明，避免跨邊界。

按實際曝光與運動條件驗完整流程。

來源：https://arxiv.org/abs/1612.02177

### Deblur：銳利的多重邊可能是振鈴

同邊橫切振鈴比原平滑觀測更銳利但有額外輪廓，量測若選錯峰會偏移。獨立成像驗證。

銳利度增加，不能取代真邊位置證據。

來源：https://arxiv.org/abs/1612.02177

<!-- wi033-engineering:end -->

# Inpainting（`inpainting`）

- roadmap 分類：`diffusion-restoration`
- roadmap 節點：`Inpainting`
- Markdown pages：`07-18` 至 `07-21`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-prototype`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/inpainting.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
製作外觀模擬圖時，想清除金屬板中央污漬，讓周圍拉絲紋理自然延續。

### 它交出什麼，也不交出什麼
獨立保存的編修影像及遮罩；檢查接縫、紋理和區域外變化。

### 一句心智模型
Inpainting是一類填補任務，並非單一模型。遮罩指出可重畫的區域，未遮住的周邊提供上下文；擴散式實作以這些條件引導逐步去噪，讓局部從雜訊形成合理紋理。傳統修補或其他神經網路也能做Inpainting，本課用擴散式路徑說明。

**限制：** 第二圖改用下半部真的破洞：同樣能把它填成平整表面，但改變的是畫面，沒有修復金屬。兩個上方製造孔仍保留；這樣才能清楚追蹤是哪個區域被重畫。

### 換一個現場再推理
一張圖只有小污漬，另一張的孔邊整片被遮住；交付時間很短。

**問題：** 會兩張都用同一擴散設定，還是分開處理？

**核對：** 小污漬可先比較傳統或快速填補，核對紋理接縫；大面積結構缺失可用帶條件的生成方法探索，但可能有多個合理答案。按用途核對結構、外區變化及總時間；若需知道實體原狀，應重拍或取得其他觀測。
<!-- topic-learning-bridge:end -->
<!-- wi026-model-core:start -->
## WI-026 核心做法與工作取捨

Inpainting是一類填補任務，並非單一模型。遮罩指出可重畫的區域，未遮住的周邊提供上下文；擴散式實作以這些條件引導逐步去噪，讓局部從雜訊形成合理紋理。傳統修補或其他神經網路也能做Inpainting，本課用擴散式路徑說明。

第二圖改用下半部真的破洞：同樣能把它填成平整表面，但改變的是畫面，沒有修復金屬。兩個上方製造孔仍保留；這樣才能清楚追蹤是哪個區域被重畫。

要局部修補，先測Inpainting；要生成整體布局相近的外觀，可用ControlNet。兩者能在支援的實作中搭配。若目標是生成某類真實刮傷，需要缺陷概念及資料準備，不能只因遮罩存在就當作已學會缺陷。

只有正常影像也能測局部填補；新產品需重新核對材質、遮罩大小和周邊資訊。比較傳統修補、前饋或擴散實作時，固定用途與遮罩，記接縫、外區改動、生成時間及人工覆核量。結果是編修圖，不是精密分割或實體量測。

來源：https://arxiv.org/abs/2201.09865

圖為AI生成教學示意；原工程段落為補充，首讀新版以本段及topic為準。使用者成品核准pending。
<!-- wi026-model-core:end -->
## Identity and engineering boundary

Inpainting 是依據 binary／soft mask 與周邊 context 填補區域內容的任務 family，不是單一模型，也不是 defect detector、量測工具或放行決策。它可用於非證據性的資料修補、模擬與視覺化；被填補的 pixels 是 plausible synthetic content，不能被說成相機觀測到的真實 defect、結構或尺寸。

## Reproducible engineering contract

### `architecture_path`

`原始影像／ROI + binary 或 soft mask + mask 外圍 context + optional prompt/condition → 指名的 latent/pixel inpainting implementation 與 base checkpoint → guided denoising / blend → filled image + original/mask/output relationship → fidelity review → synthetic/edit candidate 或人工交接`。

### `representation_or_score`

- mask 表示允許模型填補的區域與邊界，不是 defect label、量測 ROI 或真實證據。
- filled region 是根據 context、guidance 與 sampling 產生的 plausible content；它不是被觀測到的物理表面。
- 原圖、mask、filled image 與任何 downstream score 是不同物件；不可以用填補區直接判斷 defect existence、尺寸或 PASS/HOLD。

### `cost_and_operating_point`

鎖定 implementation／code revision、base checkpoint/license/hash、mask generator/version、原圖 ROI/resolution、prompt/condition、steps、sampler、guidance、seed、blend/tile policy、GPU/VRAM、完整 P95 與輸出保存。驗收需依 mask size、位置與邊界複雜度分層檢查填補品質、failure gallery、context mismatch 與 review 負荷。

### `failure_boundary`

- mask leakage、錯誤邊界、context mismatch、prompt bias、seed/sampler 漂移與 domain shift 都可能幻覺、抹除或改寫重要結構。
- 漂亮的填補結果不證明 defect 存在、缺陷形態、關鍵尺寸或材料結構為真。
- raw 與 filled pixels 混用、沒有 synthetic/edit label、缺少 original/mask/output 關聯或把填補結果送入自動放行，都使流程失效。

### `selection_gate`

只在用途明確限定為非證據性的資料增強、展示或受控模擬時考慮 Inpainting。先固定 mask policy、base implementation、sampling、原圖／mask／輸出保存與 human review；以 mask-stratified quality、failure gallery、完整 P95 與 downstream real-holdout 效益決定是否小規模使用。任何關鍵 defect、尺寸、traceability 或產線決策皆為 no-go。

### `evidence_bundle`

保留 original image/ROI hash、mask 及其 generator/version、mask boundary policy、implementation/base checkpoint/license/hash、prompt/condition、sampler/steps/guidance/seed、resolution/tile/blend、filled output/edit manifest、synthetic label、mask-stratified review、failure gallery、P95/VRAM/cost、human review、safe fallback 與最終 action。

## 視覺因果 brief（產圖前）

- **十秒復述句**：工程師圈定允許修補的區域，Inpainting 依周邊 context 產生填補候選；候選可供模擬或資料增強，但不能取代原始影像作 defect 或量測證據。
- **輸入物件**：原始 AOI 影像、明確的 repair mask、mask 外圍 context。
- **方法／轉換**：inpainting denoising 只在 mask 內填補，並與周圍影像 blend。
- **可觀察輸出**：原圖、mask、filled candidate 與 synthetic/edit 關聯。
- **工程決策**：資料增強／展示候選交人工 review；關鍵 defect、尺寸、traceability 決策回到 raw image。
- **主箭頭**：`原圖 + mask + context → masked denoising → filled candidate + edit trace → review / no-measurement gate`。

## Required C / D visual pages

| page | lesson | archetype | visible causal story |
| --- | --- | --- | --- |
| `07-18` | identity and problem | C | 工程師在 AOI 影像上標示 repair mask；模型只填補遮罩內內容，候選回到人工 review，raw image 仍保留為證據。 |
| `07-19` | architecture | C | image、mask、context 與 optional condition 進入 inpainting denoising；filled region 與原圖／mask 一起保存。 |
| `07-20` | build and inference | C | 工程師鎖 mask generator、checkpoint、prompt、steps、seed、blend，依 mask size/location 檢查 quality、failure 與 P95。 |
| `07-21` | engineering selection | D | 對比「把填補像素當真實證據」與「只作 synthetic/edit candidate 並保留 raw、mask、review」的工作流。 |

## Sources

- `full-model-course/07-diffusion-generation-and-restoration.md` 的 `07-18` 至 `07-21` 課程內容。

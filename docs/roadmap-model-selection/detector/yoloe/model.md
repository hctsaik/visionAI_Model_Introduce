# YOLOE（`yoloe`）

- roadmap 分類：`detector`
- roadmap 節點：`YOLOE`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-prototype`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/yoloe.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
同一綠色電路板上，左 A 印 103、右 B 印 272；相似外觀不保證相同料號。

### 它交出什麼，也不交出什麼
Grounding DINO 交出框與詞語；YOLOE 支援框與遮罩。需要確認對象、邊界與漏件後，才能接計數、裁圖或量測流程。

### 一句心智模型
有時物件能用文字描述，有時更容易給一張範例，也可能想先不指定提示。YOLOE把文字、視覺和免提示路徑接到高效偵測／分割中；重點是改變「找什麼」的輸入方式，不只是切換框或mask的顯示。

**限制：** 文字保存詞表；視覺保存範例原圖與區域；免提示保存模型與詞庫版本。按checkpoint檢查框與mask，換產品重測召回、邊界、提示成本及P95。精細mask不能直接當作尺寸或缺陷真值。

### 換一個現場再推理
視覺範例在舊板上可用；新產品反光更強，mask 蓋到背景。現場希望免標註又直接用遮罩判尺寸。

**問題：** 先改善提示、取像與分割，還是換成只找框的流程？如何驗證代價？

**核對：** 先核對同一原圖邊緣與範例是否含背景，測不同取像及提示，必要時補現場分割標註。若只要計數可先驗框；要輪廓則比較 YOLOE 與 Grounding DINO 加分割流程的邊界誤差、漏件及完整延遲。固定類別可另設受監督基準，但不能拿框替代輪廓。尺寸仍需獨立校正與量測驗證，不能把免外部提示當作免資料或免覆核。
<!-- topic-learning-bridge:end -->
## 角色與安全邊界

YOLOE 是 open-vocabulary／promptable YOLO family 的一項設計，可涵蓋 detection 與部分 segmentation 介面。文字 prompt 與 visual exemplar 都是可變輸入；必須鎖版本、mode 與 prompt source。

輸出 boxes、masks、open-vocabulary scores 粒度不同，不能混成單一性能，也不能把 text／visual prompt 的 candidate 直接當製程證據或 release 判定。

## 視覺因果 brief（產圖前必填）

### 03-22｜身份與問題（C）

1. **十秒句**：YOLOE 讓 text 或 visual exemplar 產生 candidate boxes／masks，但 candidate 仍需 specialist 確認。
2. **輸入物件**：AOI image、text prompt 或 visual exemplar、選定 detection／segmentation mode。
3. **方法／轉換**：prompt representation 進入 prompt-aware YOLO head，輸出 mode-specific boxes／masks／scores。
4. **可觀察輸出**：text／visual prompt 對同一 AOI image 的 candidate boxes、masks 與 ROI review。
5. **工程決策**：只作 promptable candidate workflow；不得以 candidate 直接決定 defect／release。
6. **箭頭對照表**：`image + text/visual prompt → prompt representation → prompt-aware head → boxes/masks/scores → specialist confirmation`。

### 03-23｜架構（C）

1. **十秒句**：YOLOE 的可變 prompt representation 決定 prompt-aware head 要找什麼、以 box 或 mask 輸出什麼。
2. **輸入物件**：image features、text tokens、visual exemplar embedding、mode selection。
3. **方法／轉換**：prompt-aware detection／segmentation head 對 feature locations 產生 boxes／masks／scores。
4. **可觀察輸出**：分開顯示 text prompt box、visual prompt box／mask 與 inverse ROI。
5. **工程決策**：box、mask 與 score 分開驗證，不將其當單一性能或 defect proof。
6. **箭頭對照表**：`features + text/visual prompt → prompt-aware head → mode-specific boxes/masks/scores → inverse ROI`。

### 03-24｜訓練與推論（C）

1. **十秒句**：prompt source、visual exemplar、mode、threshold、NMS／mask postprocess 未版本化，就不能比較 YOLOE 的端到端成本或可靠度。
2. **輸入物件**：text templates、class／visual exemplars、preprocess、head mode、threshold。
3. **方法／轉換**：固定 prompt embeddings、detection／segmentation head、NMS／mask postprocess 與 coordinate transform。
4. **可觀察輸出**：text／visual、seen／unseen 的 candidate recall，mask consistency，embedding／forward／postprocess P95。
5. **工程決策**：先檢驗每個 prompt mode；確認 candidate workflow owner，再談採用。
6. **箭頭對照表**：`prompt source → fixed prompt/mode/preprocess → head + postprocess → recall/mask/P95 → specialist review`。

### 03-25｜工程選型（D）

1. **十秒句**：若將 visual prompt 的 box／mask 直接視為 defect truth，會忽略 exemplar bias、prompt drift 與不一致 mask；正確流程是固定 prompt contract 後交 specialist。
2. **輸入物件**：同一 vocabulary、visual exemplar、ROI、pixels 與 owner action。
3. **方法／轉換**：左側 prompt box／mask 直接決策；右側保存 prompt source、mode、candidate ROI 和 specialist evidence。
4. **可觀察輸出**：左側 candidate 與不一致 mask；右側有 text／visual prompt 對照、ROI confirmation 與 review。
5. **工程決策**：可探索 text／visual prompt 介面；與 YOLO-World／Grounding DINO 比固定 vocabulary、ROI、pixels、owner action，不以 candidate 直接放行。
6. **箭頭對照表**：`prompt candidate 直接決策（失敗） → fixed prompt / mode + specialist confirmation（可採行）`。

## 模型專屬欄位

- `architecture_path`：`image features + text/visual prompt representations → prompt-aware detection/segmentation head → mode-specific boxes/masks/scores → inverse ROI`。
- `representation_or_score`：prompt representation 可為文字或 visual exemplar；boxes、masks、scores 是不同輸出粒度，不能混合成單一性能。
- `cost_and_operating_point`：鎖 prompt source、class/visual exemplars、mode、preprocess、threshold、NMS/mask postprocess；量測 prompt embedding、forward、postprocess P95。
- `failure_boundary`：prompt drift、visual exemplar bias、small object、mask inconsistency、mode mismatch；candidate 不可取代製程證據。
- `selection_gate`：分開驗證 text／visual、seen／unseen candidate recall 與 mask consistency；固定 vocabulary、ROI、pixels、owner action 後交 specialist review。
- `evidence_bundle`：raw image、prompt source/version、visual exemplars、mode/head version、boxes/masks/scores、postprocess/inverse ROI、recall/mask/P95、review result。

## 必須畫出的視覺 primitive

- `aoi_image`
- `text_and_visual_prompts`
- `prompt_representation`
- `prompt_aware_head`
- `box_mask_score_outputs`
- `candidate_to_specialist_gate`

## 交付頁面

| Course page | 頁型 | 核心回答 |
|---|---|---|
| 03-22 | C | text／visual prompt 為何只產生 candidate？ |
| 03-23 | C | 可變 prompt 如何進入 prompt-aware head？ |
| 03-24 | C | 哪些 prompt／mode／postprocess 必須鎖定？ |
| 03-25 | D | 為何 prompt box／mask 不可直接 release？ |

## 產生 gate

已完成六欄位與頁面級視覺因果 brief。產圖後依根目錄 `IMAGE_STYLE_GUIDE.md` 11.10 做語意驗收；使用者確認前一律標記 `in-review`。

## D01 核心主線與來源補正

此節是2026-09-06本輪主線的補正；舊例若只展示部分路徑，不可據此當作模型全部能力。

有時物件能用文字描述，有時更容易給一張範例，也可能想先不指定提示。YOLOE把文字、視覺和免提示路徑接到高效偵測／分割中；重點是改變「找什麼」的輸入方式，不只是切換框或mask的顯示。

**文字：RepRTA改善區域文字對齊**：以可重參數化的輕量輔助網路調整預訓練文字表示。部署可整理固定詞彙的表示以減少額外工作；效果仍受預訓練和詞義影響。

**視覺：SAVPE從指定區域取範例線索**：以語意與activation分支形成視覺提示表示；指定物件區域能比一句名稱更直接。但框到背景或混入別件會改變提示，範例不是品質真值。

**免提示：LRPC仍使用內建大詞彙**：免提示不用使用者每次輸入文字，仍受模型內建詞庫與學得能力限制，不等於任意未知缺陷都能找。支援的模型可交框及實例mask；實際能力依checkpoint／介面核對，不把兩者說成一定互斥。

自測：移除使用者文字、改用免提示模式，是否等於也移除了詞彙限制，能保證找出新發明的缺陷？

解釋：不是。LRPC仍利用內建大詞彙與學得表示，沒有無限語意知識。要找特定外觀可測文字或視覺提示，但仍需樣本驗證與必要的訓練；框和mask只能支持各自的定位／輪廓判讀。

工作接法：文字保存詞表；視覺保存範例原圖與區域；免提示保存模型與詞庫版本。按checkpoint檢查框與mask，換產品重測召回、邊界、提示成本及P95。精細mask不直接提供尺寸或缺陷真值。

[原論文／官方文件](https://arxiv.org/abs/2503.07465)。D01核心與反例圖為既有素材加受控設定，沒有新模型推論。

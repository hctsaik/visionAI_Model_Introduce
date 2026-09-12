# Grounding DINO（`det-grounding-dino-interface`）

- roadmap 分類：`detector`
- roadmap 節點：`Grounding DINO`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-prototype`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/det-grounding-dino-interface.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
同一綠色電路板上，左 A 印 103、右 B 印 272；相似外觀不保證相同料號。

### 它交出什麼，也不交出什麼
Grounding DINO 交出框與詞語；YOLOE 支援框與遮罩。需要確認對象、邊界與漏件後，才能接計數、裁圖或量測流程。

### 一句心智模型
固定類別偵測器不方便臨時指定要找的物件。Grounding DINO將影像與語言一起處理，讓文字不只替既有框命名，而是參與挑選候選與定位；它利用大規模grounded預訓練支持開放集合搜尋。

**限制：** 先以明確物件詞驗證，再用專家確認框；記錄prompt及同詞不同外觀。換詞／產品需重驗漏檢與誤框，必要時微調；只有正常品也能探索物件，但不能直接變成未知缺陷檢測。

### 換一個現場再推理
新板上的電阻仍清楚可見，但用 R-17 提示沒有框；改成 resistor 後又出現多個候選，下一站還想量輪廓。

**問題：** 你會修改提示、改用視覺範例，還是訓練固定類別模型？輪廓要怎麼交付？

**核對：** 先回原圖確認像素與物件存在，將通用詞候選對照位置／料表；空結果不能當缺件。可用 Grounding DINO 加外接分割，或比較 YOLOE 視覺提示與 mask；類別固定且有框標註時，再比較 YOLO／RT-DETR。保留同批小物影像評估漏件、誤框、邊界與完整延遲，換板後重驗，不能以更多候選或單一成功圖決定。
<!-- topic-learning-bridge:end -->
## 角色與安全邊界

Grounding DINO 是 text-conditioned open-set candidate detector：文字 phrase 導引 box proposal。它擴大早期探索與長尾名稱的候選召回，但 box 只代表後續 ROI；不能當 metrology、defect truth 或 PASS／release。

文字、tokenization、prompt template、phrase threshold 與座標 inverse mapping 都是 inference contract。每次推論需保存 prompt、version、candidate box／score、ROI transform 與 specialist confirmation。

## 視覺因果 brief（產圖前必填）

### 03-14｜身份與問題（C）

1. **十秒句**：Grounding DINO 用文字找 candidate ROI，不會用一個 phrase box 證明缺陷存在。
2. **輸入物件**：AOI image、工程師輸入的 phrase／prompt 與指定探索 ROI。
3. **方法／轉換**：image feature 與 text tokens 在 grounding path 對齊，產生 phrase-conditioned candidate boxes。
4. **可觀察輸出**：畫有 candidate box 的原圖、phrase score、inverse-mapped ROI 與 specialist confirmation lane。
5. **工程決策**：candidate 送高解析 detector／AD／人工確認；不能直接 release。
6. **箭頭對照表**：`image + phrase → text/image alignment → phrase-conditioned boxes → inverse ROI → specialist confirmation`。

### 03-15｜架構（C）

1. **十秒句**：文字 tokens 會改變 Grounding DINO 的 query selection 與 box score space。
2. **輸入物件**：image features、phrase tokens、prompt template。
3. **方法／轉換**：feature enhancer → language-guided query selection → cross-modal decoder。
4. **可觀察輸出**：phrase-conditioned boxes／scores，並映回 raw coordinates。
5. **工程決策**：box 被當作高解析 specialist 的 ROI，而非 defect proof。
6. **箭頭對照表**：`image features + text tokens → enhancer → guided queries → decoder → boxes / inverse ROI`。

### 03-16｜訓練與推論（C）

1. **十秒句**：不鎖 prompt、tokenization、threshold 與 ROI inverse transform，就無法比較 grounding 表現。
2. **輸入物件**：prompt vocabulary／synonyms、test image、raw coordinates、box thresholds。
3. **方法／轉換**：固定 text/image preprocessing、phrase postprocess、NMS 與 coordinate transform。
4. **可觀察輸出**：grounding recall／IoU、prompt sensitivity、specialist confirmation rate 與 P95。
5. **工程決策**：判定 prompt 是否可作候選探索；不把 zero-shot score 當 defect probability。
6. **箭頭對照表**：`prompt bundle → fixed preprocessing → threshold / inverse map → recall / sensitivity / P95 → confirmation review`。

### 03-17｜工程選型（D）

1. **十秒句**：若把 phrase box 直接當 release，會忽略 prompt ambiguity 與 tiny-object 失敗；正確流程是 candidate ROI 後再確認。
2. **輸入物件**：同一 image、同一 phrase、同一 ROI／pixel budget。
3. **方法／轉換**：左側 phrase box 直接放行；右側固定 prompt contract，將 box inverse map 後交 detector／AD／人工。
4. **可觀察輸出**：左側只有文字導引框；右側可看見 candidate ROI、specialist evidence 與 final human decision。
5. **工程決策**：只允許 exploration candidate workflow；專業模型／人工才可決定 defect 或 release。
6. **箭頭對照表**：`phrase box 直接 release（失敗） → prompt contract + candidate-to-specialist confirmation（可採行）`。

## 模型專屬欄位

- `architecture_path`：`image features + text tokens → feature enhancer → language-guided query selection → cross-modal decoder → phrase-conditioned boxes/scores → inverse ROI`。
- `representation_or_score`：phrase tokens 定義 query／score space；box／score 是 candidate evidence，不是 defect probability。
- `cost_and_operating_point`：鎖 prompt、tokenization、text/image preprocessing、box／phrase threshold、NMS、ROI transform，量測 grounding recall、prompt sensitivity、P95。
- `failure_boundary`：phrase ambiguity、domain vocabulary、tiny object、false localization、prompt drift；禁止將 phrase box 直接 release。
- `selection_gate`：同 vocabulary、ROI、pixels 下看 seen／unseen grounding recall，並量測 specialist confirmation rate；低敏感度與可回查 prompt 才可進探索流程。
- `evidence_bundle`：image/raw coordinates、prompt template/vocabulary/version、tokenization、candidate boxes/scores、inverse ROI、specialist evidence、review result、P95。

## 必須畫出的視覺 primitive

- `aoi_image_and_phrase`
- `text_token_representation`
- `language_guided_query_path`
- `candidate_box_and_inverse_roi`
- `specialist_confirmation_gate`
- `no_release_from_phrase_box`

## 交付頁面

| Course page | 頁型 | 核心回答 |
|---|---|---|
| 03-14 | C | 文字導引框為何只是 candidate？ |
| 03-15 | C | text token 如何改變 query 與 box？ |
| 03-16 | C | 哪些 prompt 與 postprocess 必須鎖定？ |
| 03-17 | D | 為何 phrase box 不可直接 release？ |

## 產生 gate

已完成六欄位與頁面級視覺因果 brief。產圖後依根目錄 `IMAGE_STYLE_GUIDE.md` 11.10 做三段語意驗收；使用者確認前一律標記 `in-review`。

## D01 核心主線與來源補正

此節是2026-09-06本輪主線的補正；舊例若只展示部分路徑，不可據此當作模型全部能力。

固定類別偵測器不方便臨時指定要找的物件。Grounding DINO將影像與語言一起處理，讓文字不只替既有框命名，而是參與挑選候選與定位；它利用大規模grounded預訓練支持開放集合搜尋。

**先融合圖像與文字證據**：影像骨幹與文字編碼器各自產生表示，feature enhancer做跨模態互動；詞語需與可見區域建立關係，不是把字串附在最後結果。

**文字引導query選擇**：從圖像特徵中選與輸入文字較相關的候選作為解碼起點。改問什麼，可能改變哪些區域被選入；詞句、分詞、門檻都要可追查。

**跨模態解碼，交出詞語對應的框**：decoder同時取用影像與文字來修正物件queries與框，輸出詞語相關分數和位置。空結果不能證明不存在，框也不是mask；需要精細輪廓可另接分割流程。

自測：若只先跑固定類別偵測，再把文字貼在框旁邊，為何不能當成Grounding DINO的文字引導定位？

解釋：事後改標籤沒有讓文字參與特徵融合、query選擇與框修正，原本沒提出的區域不會因此被搜尋。Grounding需要影像與語言互動；即使有此機制，也不保證模型理解任意缺陷詞或空間關係。

工作接法：先以明確物件詞驗證，再用專家確認框；記錄prompt及同詞不同外觀。換詞／產品需重驗漏檢與誤框，必要時微調；只有正常品也能探索物件，但不能直接變成未知缺陷檢測。

[原論文／官方文件](https://arxiv.org/abs/2303.05499)。D01核心與反例圖為既有素材加受控設定，沒有新模型推論。

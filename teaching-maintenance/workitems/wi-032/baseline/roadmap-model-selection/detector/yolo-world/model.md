# YOLO-World（`yolo-world`）

- roadmap 分類：`detector`
- roadmap 節點：`YOLO-World`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-prototype`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/yolo-world.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
傳統YOLO的類別隨訓練固定，臨時換要找的物件不方便。YOLO-World以區域與文字對齊的預訓練，讓dense偵測可以使用可更換詞彙；prompt-then-detect把固定詞彙先準備好，減少重複編碼文字的工作。

### 它交出什麼，也不交出什麼
模型交出物件候選框與相關分數；需回映原圖供後續確認。 保存詞表、embedding／部署權重版本與框覆核結果。詞表大、詞義相近或工件很小都需測召回／誤框；量文字準備與每影像推論成本，不把跨硬體FPS當本站節拍。

### 一句心智模型
傳統YOLO的類別隨訓練固定，臨時換要找的物件不方便。YOLO-World以區域與文字對齊的預訓練，讓dense偵測可以使用可更換詞彙；prompt-then-detect把固定詞彙先準備好，減少重複編碼文字的工作。

**限制：** 保存詞表、embedding／部署權重版本與框覆核結果。詞表大、詞義相近或工件很小都需測召回／誤框；量文字準備與每影像推論成本，不把跨硬體FPS當本站節拍。

### 換一個現場再推理
新產品只有正常影像；要先找元件位置，未來還想取得輪廓。本站另有固定節拍與漏件容許量。

**問題：** 能直接用模型名稱宣稱找出未知缺陷嗎？你會如何起步，還需要哪些資料與驗證？

**核對：** 先固定要找的物件與輸出：前三者需已知類別框監督；後三者借助預訓練與提示探索。開放詞彙不等於免驗證，只有正常品時先做物件探索與覆核，不能宣稱已建立未知缺陷偵測。 同一資料切分、輸入像素、硬體與漏件容許量下，量漏件／重複／誤框、P95、記憶體及人工覆核。換產品要重查標註、詞彙／範例與門檻；需要輪廓時選支援mask的checkpoint或另接分割，不把box當輪廓。 可先用提示模型探索並人工确认，或標註框後訓練已知類別模型；方案取決於目標、資料及驗證，不只一個正確模型名稱。
<!-- topic-learning-bridge:end -->
## 角色與安全邊界

YOLO-World 將文字語意與 real-time-style dense detection 接合，是 open-vocabulary candidate detector。class representation 來自 text embedding，而不是既有 closed-set class head；prompt ensemble 與 vocabulary 會改變 score space。

輸出 box／open-vocabulary score 只可導引 candidate ROI。版本、prompt、embedding/cache、normalization、threshold、NMS、export 與 P95 都需鎖定；zero-shot score 不是 defect probability，也不能直接 release。

## 視覺因果 brief（產圖前必填）

### 03-18｜身份與問題（C）

1. **十秒句**：YOLO-World 用文字 embedding 做 dense candidate detection，快不代表 zero-shot box 是 defect 證據。
2. **輸入物件**：AOI image、工程 prompt vocabulary、text embedding cache。
3. **方法／轉換**：YOLO-like multi-scale features 與 text embeddings 做 vision-language alignment／fusion，形成 dense open-vocabulary scores。
4. **可觀察輸出**：多尺度 candidate boxes、prompt-conditioned score、NMS 後 ROI 與 specialist evidence。
5. **工程決策**：可用於探索大量候選名詞；box 仍交 specialist gate。
6. **箭頭對照表**：`image + vocabulary → text embeddings/cache → dense fusion → scores/boxes → NMS/inverse ROI → specialist`。

### 03-19｜架構（C）

1. **十秒句**：YOLO-World 的 class score 來自 prompt embedding 對 dense image features 的對齊。
2. **輸入物件**：multi-scale image features、text embeddings、prompt ensemble。
3. **方法／轉換**：vision-language alignment／fusion 產生每個 dense location 的 open-vocabulary score。
4. **可觀察輸出**：decode／NMS 後 boxes 與 prompt-conditioned score space。
5. **工程決策**：固定 vocabulary 後只比較 candidate recall／stability，不把 score 當 calibrated defect probability。
6. **箭頭對照表**：`features + embeddings → alignment/fusion → dense scores → decode/NMS → boxes / ROI`。

### 03-20｜訓練與推論（C）

1. **十秒句**：不鎖 vocabulary、synonym、negative phrase、embedding cache 與 calibration，就無法比較 YOLO-World 的候選品質與 P95。
2. **輸入物件**：prompt vocabulary、synonyms、negative phrases、image/text normalization、test AOI image。
3. **方法／轉換**：固定 embedding 建置／cache、dense head、score calibration、decode/NMS、ROI transform。
4. **可觀察輸出**：seen／unseen grounding recall、prompt stability、embedding／forward／postprocess P95 與 specialist confirmation。
5. **工程決策**：只採用可回查的 prompt-to-ROI candidate workflow。
6. **箭頭對照表**：`vocabulary → embedding cache → fixed dense inference → calibration/NMS/inverse ROI → recall/stability/P95 → review`。

### 03-21｜工程選型（D）

1. **十秒句**：將 zero-shot dense score 當 defect probability 會把 vocabulary bias 與 tiny ROI 失敗藏起來；正確選擇是固定 prompt、比 candidate recall，再送 specialist。
2. **輸入物件**：同一 vocabulary、ROI、pixel budget、hardware 與 threshold policy。
3. **方法／轉換**：左側 dense score 直接 PASS／FAIL；右側固定 vocabulary／embedding，box inverse map 後交 specialist。
4. **可觀察輸出**：左側有語意相近／tiny ROI 偏差；右側有 candidate boxes、prompt stability／P95 與 confirmation。
5. **工程決策**：可作長尾候選探索；比較 Grounding DINO 時看 candidate recall、prompt stability、P95，final decision 仍由 specialist。
6. **箭頭對照表**：`zero-shot score 直接決策（失敗） → fixed vocabulary + candidate-to-specialist（安全探索）`。

## 模型專屬欄位

- `architecture_path`：`image → YOLO-like multi-scale features + text embeddings → vision-language alignment/fusion → dense open-vocabulary scores → decode/NMS → boxes/ROI`。
- `representation_or_score`：class score 由 prompt embedding 定義；prompt ensemble、synonym 與 vocabulary 會改變 score space。
- `cost_and_operating_point`：鎖 embedding cache、prompt vocabulary、normalization、dense inference、NMS、export；分開量測 embedding、forward、postprocess 與 P95。
- `failure_boundary`：prompt／詞彙偏差、語意相近類、tiny ROI、calibration、domain shift、export 差異；zero-shot score 不可作 defect probability。
- `selection_gate`：固定 vocabulary、ROI、pixels、hardware、threshold，評估 candidate recall、prompt stability、P95、specialist confirmation rate。
- `evidence_bundle`：raw image、vocabulary/synonym/negative phrases、embedding/cache version、normalization、boxes/scores、NMS/inverse ROI、recall/stability/P95、review result。

## 必須畫出的視覺 primitive

- `aoi_image_and_vocabulary`
- `text_embedding_cache`
- `dense_multiscale_feature_path`
- `alignment_or_fusion`
- `dense_scores_decode_nms`
- `candidate_to_specialist_gate`

## 交付頁面

| Course page | 頁型 | 核心回答 |
|---|---|---|
| 03-18 | C | 為何 open-vocabulary dense box 是 candidate？ |
| 03-19 | C | prompt embedding 如何進入 dense score？ |
| 03-20 | C | 哪些 vocabulary／cache／calibration 必須鎖定？ |
| 03-21 | D | 為何 zero-shot score 不可直接 PASS／FAIL？ |

## 產生 gate

已完成六欄位與頁面級視覺因果 brief。產圖後依根目錄 `IMAGE_STYLE_GUIDE.md` 11.10 做語意驗收；使用者確認前一律標記 `in-review`。

## D01 核心主線與來源補正

此節是2026-09-06本輪主線的補正；舊例若只展示部分路徑，不可據此當作模型全部能力。

傳統YOLO的類別隨訓練固定，臨時換要找的物件不方便。YOLO-World以區域與文字對齊的預訓練，讓dense偵測可以使用可更換詞彙；prompt-then-detect把固定詞彙先準備好，減少重複編碼文字的工作。

**區域與文字共同學習**：區域文字對比目標讓區域表示對應詞語，而不只對應固定類別編號。能力來自預訓練資料與對齊，輸入新名稱不等於模型已學會新的製程缺陷。

**RepVL-PAN交換視覺與語言資訊**：可重參數化的視覺語言neck在多尺度中融合圖與詞，再由dense頭產生框與詞彙相關分數。它不是單純對全圖做一次CLIP分類。

**先編碼詞彙，重用於多張影像**：可先將離線詞彙編碼／重參數化供部署使用；影像仍逐張處理。換詞要更新相應表示與驗證，快取不等於無成本；自然語言not也不是通用布林排除運算。

自測：介面把「元件」改成「連接器」，卻沿用舊詞彙embedding；模型真的已換成新的查詢了嗎？

解釋：沒有。模型實際比對的仍是舊表示；只改顯示文字不會更新cache或重參數化權重。需重新準備詞彙表示並核對版本，再以新詞與代表樣本重驗。這也說明預先算的是文字條件，不是未來影像的偵測結果。

工作接法：保存詞表、embedding／部署權重版本與框覆核結果。詞表大、詞義相近或工件很小都需測召回／誤框；量文字準備與每影像推論成本，不把跨硬體FPS當本站節拍。

[原論文／官方文件](https://arxiv.org/abs/2401.17270)。D01核心與反例圖為既有素材加受控設定，沒有新模型推論。

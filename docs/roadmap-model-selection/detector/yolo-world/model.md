# YOLO-World（`yolo-world`）

- roadmap 分類：`detector`
- roadmap 節點：`YOLO-World`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-prototype`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/yolo-world.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
料盤需要找的零件名稱會變，重做固定類別訓練未必是每次試做的起點。YOLO-World讓文字詞彙參與偵測，但找到一個叫作螺栓的區域，仍不等於證明它無裂紋。

### 它交出什麼，也不交出什麼
相對選定詞彙的物件候選框、類別與分數；若要品質分類、根因、尺寸或輪廓，還需要對應方法與驗證。提示詞不是完整業務規則。

### 一句心智模型
文字先經編碼器成為詞彙表示，影像經視覺骨幹成為多尺度特徵；視覺語言路徑讓兩者互動，再以區域與詞彙表示的相似關係產生類別分數和框。固定詞彙可預先編碼／快取，部分實作可進一步重參數化，減少每張圖重做文字處理。

**限制：** 同一螺栓頭的細裂紋在低解析影像中被混成邊緣，即使詞彙寫「裂紋螺栓」，框到螺栓也不證明模型看見裂紋。先確認原始取像有足夠細節，再用有標註樣本核對；新圖是觀測限制示意，不是實測預測。

### 換一個現場再推理
系統能找到螺栓，卻分不清頭部細裂紋；另一組需求只是每週換一批外觀明顯不同的零件名稱。

**問題：** 兩組需求都靠增加提示詞解決合理嗎？

**核對：** 細裂紋先確認原始像素與光照能看見，再用缺陷標註比較專用檢測、分類或分割；框到螺栓不等於辨出裂紋。外觀明顯、詞彙常變的零件可先試更新YOLO-World詞彙和表示，再做獨立場景驗證；若詞彙更新仍常錯類，可比較補標註微調或固定類別模型。以資料、輸出目的和完整成本選擇，不以提示長度選擇。
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


<!-- wi032-model-core:start -->
## WI-032 核心做法與工作取捨

文字先經編碼器成為詞彙表示，影像經視覺骨幹成為多尺度特徵；視覺語言路徑讓兩者互動，再以區域與詞彙表示的相似關係產生類別分數和框。固定詞彙可預先編碼／快取，部分實作可進一步重參數化，減少每張圖重做文字處理。

同一螺栓頭的細裂紋在低解析影像中被混成邊緣，即使詞彙寫「裂紋螺栓」，框到螺栓也不證明模型看見裂紋。先確認原始取像有足夠細節，再用有標註樣本核對；新圖是觀測限制示意，不是實測預測。

文字詞彙常變且要快速試候選時，YOLO-World提供與固定類別偵測不同的準備路線；類別穩定且已有標註時，DINO或既有固定類別偵測器也值得比較。開放詞彙不等於無限制辨識，固定類別也不等於不能重新訓練擴充。

換詞彙需更新文字表示／重參數化產物並重新核對；換產品或取像可能仍需標註與微調。測試要固定模型版本、詞彙、相容前處理與硬體，納入文字準備攤提、線上推論、後處理及覆核成本。

選明確YOLO-World版本與預訓練checkpoint，準備具體類別詞彙和代表性影像，先做獨立人工標註核對集，再評估快取或重參數化部署。

保存原圖、詞彙與編碼／模型版本、輸出框和人工真值；比較換詞彙前後的漏檢、錯類與完整成本，含無目標物件影像。本輪沒有執行權重推論；區域相似度與缺陷可見性圖是教學示意。

來源：https://arxiv.org/abs/2401.17270

版本及示意界線見工作項目 sources.md。使用者成品核准pending。
<!-- wi032-model-core:end -->

<!-- wi032-engineering:start -->
## 工程層：輸入、機制、部署與限制

### 開放詞彙偵測：詞彙是輸入的一部分

YOLO-World利用預訓練視覺語言表示進行開放詞匯檢測，文字不是直接搜索像素的規則。提示類別的粒度、視覺可見性和訓練分布都會影響現場結果。

詞彙可變，但現場辨識能力仍需驗證。

來源：https://arxiv.org/abs/2401.17270

### 文字參與特徵整理，也參與區域比對

以論文v3的RepVL-PAN為例，Text-guided CSPLayer把影像／詞彙相似經max與sigmoid形成權重，乘回影像特徵；Image-Pooling Attention另用池化的影像資訊更新文字表示。區域與詞彙相似度用於類別評分，框回歸另負責位置。圖只展開文字引導權重與區域比對，矩陣深淺為示意，不是實際權重輸出。部署版本可能省略或改寫模組，需按官方設定核對。

保留影像與文字兩條來源，才看得懂比對。

來源：https://arxiv.org/html/2401.17270v3

### 快取與重參數化，是兩種不同準備

官方reparameterize文檔區分快取文本特征和進一步轉換部署結構。采用時應記錄版本、詞匯、編碼器及部署產物；換詞匯需要對應更新，不只改前端顯示文字。

快取向量不等於已完成模型重參數化。

來源：https://arxiv.org/abs/2401.17270

### 文字提示不是完整的檢驗規則

物件框不證明細裂紋或缺陷存在，也不直接給尺寸或根因。若任務要求細缺陷，應先檢查取像像素和光照，再準備適合缺陷任務的標注與驗證流程。

先定義要框物件還是判缺陷，再選後續流程。

來源：https://arxiv.org/abs/2401.17270

<!-- wi032-engineering:end -->

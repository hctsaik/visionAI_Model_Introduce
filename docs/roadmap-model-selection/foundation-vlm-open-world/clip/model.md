# CLIP（`clip`）

- roadmap 分類：`foundation-vlm-open-world`
- roadmap 節點：`CLIP`
- 課程頁面：`06-02` 至 `06-05`
- 內容覆蓋狀態：`complete`
- 產生狀態：`ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/clip.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
你想用「金屬支架」「齒輪」等文字整理工件照片，希望增加候選類別時，不必每次都重新訓練一個固定分類器。

### 它交出什麼，也不交出什麼
回傳影像與文字的相似度及候選排序，交給檢索或分類流程；整圖排序本身不提供可靠的缺陷位置。

### 一句心智模型
CLIP 用影像與其文字描述配對做預訓練，讓正確配對在共同表示空間裡更接近。部署時，影像和每條候選文字分別經編碼器，再比較兩邊表示的相似度。因此可用文字定義候選，做零樣本分類或檢索；它的這條路徑是在排序文字，不是逐字生成回答。

**限制：** 圖中明明是齒輪，但候選只有「金屬支架」與「軸承」時，仍可能選出一個第一名。第一名只是集合內的相對結果；加上「其他」也不會自動解決未知類別辨識。

### 換一個現場再推理
你的照片庫新增聯軸器，現有候選只有軸承與齒輪。團隊想把最高分當作類別。

**問題：** 先增加文字候選、訓練分類器，還是加覆核？怎樣決定？

**核對：** 可先補聯軸器與易混淆描述並做小規模檢索測試，配合未知樣本和覆核；若細微差異仍不穩定且有足夠標註，專用分類器也合理。不能只因已有最高分就把照片硬分進舊類別。
<!-- topic-learning-bridge:end -->
<!-- wi027-model-core:start -->
## WI-027 核心做法與工作取捨

CLIP 用影像與其文字描述配對做預訓練，讓正確配對在共同表示空間裡更接近。部署時，影像和每條候選文字分別經編碼器，再比較兩邊表示的相似度。因此可用文字定義候選，做零樣本分類或檢索；它的這條路徑是在排序文字，不是逐字生成回答。

圖中明明是齒輪，但候選只有「金屬支架」與「軸承」時，仍可能選出一個第一名。第一名只是集合內的相對結果；加上「其他」也不會自動解決未知類別辨識。

CLIP 與原始 SigLIP 都可做圖文相似度，但 CLIP 用批次對比與 softmax 正規化，SigLIP 用逐對 sigmoid 目標。訓練目標的差異不保證某一個在你的工件上更準、更快。

只有正常照片也能探索語意检索，但仍需候選文字、實際類別／相關性標註與未知樣本來驗證。換產品先重查詞彙、拍攝條件及混淆類別；同圖同詞比較排序錯誤、拒答、文字特徵快取和完整耗時。

列出希望搜尋的工件名稱及描述，準備各類代表影像和容易混淆／不在候選內的測試圖；固定原始 CLIP 權重及前處理。

核對前幾名是否包含正確／相關候選、改寫文字是否翻轉結果，以及未知圖是否被錯選；與既有搜尋或分類流程比較錯誤與覆核時間。

來源：https://arxiv.org/abs/2103.00020

版本及示意界線見工作項目 sources.md。使用者成品核准pending。
<!-- wi027-model-core:end -->
## 模型身份與責任邊界

CLIP 是由 image encoder 與 text encoder 組成的 dual encoder。它把影像和文字映射到共享 embedding space，使用 normalized similarity 對受控的文字候選進行排序；適合 semantic retrieval、zero-shot candidate 與少標註探索。

它輸出的是 **相似度／排序**，不是校準後的 defect probability、pixel mask、metrology、可追溯 defect claim 或 generative answer。當主張需要定位、量測、可校準機率或產品放行時，必須接 specialist / human evidence gate。

## 六個模型專屬欄位

### `architecture_path`

`timestamped image → fixed ROI/tile → declared resize/normalize → vision encoder → normalized image embedding v`，同時 `prompt ontology/template → tokenizer → text encoder → normalized text embedding t`；最後以 `s = v·t / τ` 排序受控候選，並進入 calibration、OOD / prompt-sensitivity 與人工／專家模型 action。

CLIP 沒有將文字 token 送入 image decoder 的 multimodal bridge；它的 cross-modal 接點是共同 embedding space 的 similarity。視覺輸入仍可有 patch / visual-token 表示，且影像解析度、ROI、tile 與 preprocessing 會決定 tiny evidence 是否在 encoder 前保留。

### `representation_or_score`

- `v`：版本化 checkpoint 與 image preprocessing 後的 normalized image embedding。
- `t`：版本化 prompt template、詞彙、tokenizer 與文字 encoder 後的 normalized text embedding。
- `s`：temperature-scaled dot-product similarity，用於 ranking；它只在固定候選集合與 prompt ontology 下可被解讀。
- candidate 是待驗證線索；similarity 不能直接升格為 defect probability、局部定位或量測結論。

### `cost_and_operating_point`

必須鎖定 checkpoint / vision backbone、input resolution、ROI / tile policy、image preprocess、prompt templates / synonyms、tokenizer、temperature、candidate aggregation、calibration、cache policy 與 downstream specialist。

完整 P95 包含 capture、image encode、text encode 或 prompt cache、similarity ranking、aggregation、calibration、review queue 與後續專家模型／人工交接；不得只報 image forward latency。

### `failure_boundary`

- tiny defect 已在 resize、tile 或 visual-token 中稀釋時，embedding 無法恢復局部證據；
- prompt wording、template、同義詞與領域詞彙會改變 `t`，所以排名不穩不代表影像本身改變；
- 產線 domain、材料外觀、照明、recipe shift 或 OOD 時，共享空間的語意對齊可能失效；
- global similarity 不保證 pixel localization、defect size、因果或 calibrated release probability；
- candidate ontology 不完整時，最高分只是「在列出的候選中相對高」，不是已知正常或已知缺陷的證明。

### `selection_gate`

只在下列條件下採用 CLIP 作為 semantic candidate / retrieval 層：

1. 固定 input、ROI / tile、checkpoint、prompt ontology、tokenizer 與 decision unit；
2. local production vocabulary、prompt variance、OOD / abstain、retrieval / grounding 與端到端 P95 都被量測；
3. similarity 後仍有 specialist 或人工的定位／證據 gate；
4. 與 SigLIP 比較時使用同一影像、prompt pool、candidate labels、cache policy、hardware 與 P95 定義。

否則僅能作探索性候選，不得直接放行。

### `evidence_bundle`

保留 image / ROI / tile provenance、preprocess checksum、checkpoint hash、prompt template 與 synonym pool、tokenizer / temperature、top-k similarities、prompt-variance distribution、OOD / abstain outcome、retrieval or grounding truth、specialist / human decision、queue load 與 end-to-end P95 / P99。

## 必須畫出的 CLIP 視覺 primitive

- `image_roi_and_patch_coverage`：影像中的 tiny evidence 先通過 ROI / tile / patch；
- `vision_encoder_to_v`：image embedding `v`；
- `prompt_ontology_and_tokenizer`：受控文字候選、template 與 text embedding `t`；
- `normalized_similarity_temperature`：`v·t / τ` 只做 ranking；
- `shared_embedding_not_bridge`：清楚標示共同 embedding，不假裝有 generative bridge；
- `candidate_to_evidence_gate`：candidate → specialist / human，不可直接 claim；
- `prompt_variance_and_ood_abstain`：prompt / domain 不穩時進 REVIEW / HOLD；
- `end_to_end_cost`：image encode、text cache、ranking、downstream action 的完整 P95。

## 頁面與 C / D 版型

| page | 教學問題 | archetype | 核心故事 |
| --- | --- | --- | --- |
| `06-02` | CLIP 可負責什麼、不能保證什麼？ | C | 工程師以受控 prompt 將 image / text 映射到共享 embedding，得到 candidate 而非 defect claim。 |
| `06-03` | CLIP 為何是 dual encoder ranking？ | C | image `v` 與 prompt `t` 經 normalization / temperature 相似度產生排序。 |
| `06-04` | 要鎖住哪些 build / inference contract？ | C | checkpoint、preprocess、prompt pool、cache、calibration、P95 和 evidence bundle。 |
| `06-05` | CLIP 與 SigLIP 怎麼公平選？ | D | 相同影像與 prompt contract 下，比 retrieval / grounding、prompt variance、P95 與 abstain。 |

## Sources

- Radford et al., *Learning Transferable Visual Models From Natural Language Supervision* (2021), [arXiv:2103.00020](https://arxiv.org/abs/2103.00020).
- `full-model-course/06-foundation-vision-and-vlm.md`，本課程的工程邊界與頁面需求。

<!-- wi033-engineering:start -->
## WI-033 工程圖修正

### CLIP：用描述整理零件照片

工件照片與候選描述各自編碼。新增描述可定義新的比較集合，無須為每次檢索重新訓練固定類別頭；預訓練及域內驗證仍不可省略。相似度排名不是缺陷位置或合格證明。

文字定義候選，影像與描述的相似度幫你找圖。

來源：https://arxiv.org/abs/2103.00020

### CLIP：圖文各自編碼，再比較候選

影像和候選文字各自通過編碼器，正規化後比較相似度。圖以二維向量示意 0、15、60、80 度的方向；cosine 約 0.97、0.50、0.17 是教學計算，不是 CLIP 的實測特徵或正確率。

圖文各走一條路，匯合後才比較候選。

來源：https://arxiv.org/abs/2103.00020

### CLIP：文字可快取，改字就要更新

同一模型／前處理下可預先計算候選文字表示。新影像只需走影像編碼器，再與相容文字表示比較。改文字、權重或設定時更新相關快取，使用已知和未知零件重新驗證；文字快取並不是把影像直接送進文字編碼器。

換文字或權重後，更新表示並重測候選排名。

來源：https://arxiv.org/abs/2103.00020

### CLIP：第一名也可能沒有正確答案

同一齒輪影像遇到缺少齒輪的候選集合，仍會有第一名。補齊描述後先檢查易混淆與未知資料；若工作要求細微尺寸或缺陷差別，可準備標註資料測專用分類器。以下排名為反例示意，不代表模型實測。

先確認候選涵蓋需求，再決定排序能否交付。

來源：https://arxiv.org/abs/2103.00020

<!-- wi033-engineering:end -->

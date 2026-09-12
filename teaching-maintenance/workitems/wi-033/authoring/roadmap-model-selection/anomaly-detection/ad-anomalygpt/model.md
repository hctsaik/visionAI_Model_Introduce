# AnomalyGPT (`ad-anomalygpt`)

- roadmap category: `anomaly-detection`
- course pages: `04-67` through `04-70`
- research status: `complete`
- visual status: `ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/ad-anomalygpt.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
金屬板的細痕 p 需要檢出，正常孔邊 q 又不能一直誤報；先確認資料與需要的位置或問答輸出。

### 它交出什麼，也不交出什麼
交付可疑位置線索；文字或熱圖都不能直接代表精密輪廓、尺寸、根因或自動放行。

### 一句心智模型
合成異常影像、遮罩與文字配對訓練影像解碼器和提示學習器，影像編碼器與 LLM 固定。測試影像的局部特徵經解碼後與正常／異常文字匹配，產生內建位置圖；提示學習器把位置資訊轉成提示，連同影像表示與問題送入 LLM，產生回答。

**限制：** 語意與位置仍可能錯；必須用未見正常與真缺陷檢查適用範圍。

### 換一個現場再推理
新產品外觀、允收反光與缺陷型態都不同。

**問題：** 哪些準備與驗證不能直接沿用？

**核對：** 重新核對提示來源、正常參考或既有模型的適用範圍；有適配時另留驗證資料。分開檢查正常誤報、真缺陷漏檢與成本；需要對話時再驗文字是否有據。
<!-- topic-learning-bridge:end -->
## Model identity

AnomalyGPT is the industrial anomaly localization and dialogue model in the 2023 paper / AAAI 2024 publication. The image encoder and LLM are frozen; synthetic anomaly images, masks and paired text train the image decoder and prompt learner. Anomaly localization is an internal model capability, not a required external specialist input.

## Architecture path

### Build

Align synthetic anomaly pixels, masks and location descriptions. Train the lightweight image decoder and prompt learner with localization and text supervision while keeping the image encoder and LLM fixed. Keep independent normal and real-defect validation examples. Version image preprocessing, frozen checkpoints, decoder and prompt weights, training data and generation settings.

### Inference

The test image encoder provides global and local representations. The image decoder maps local features for matching with normal/anomalous text representations, producing the internal location map. The prompt learner converts location information into prompts; the LLM receives those prompts together with the image representation and user question to generate a response. The few-shot extension may additionally use normal reference feature matching.

Save the original image, location map, question and response together. Review location and language against the original. Measure preprocessing, encoding, localization, prompt processing and text generation when reporting latency. External retrieval, SOP lookup or a separate specialist model are optional application extensions and must not be presented as the paper's mandatory inference path.

## Representation and score

- Local representation: decoded image features matched with normal/anomalous text features.
- Output: an anomaly location map and natural-language answer. A structured evidence/uncertainty record may be added by the application; it is not a guaranteed native output schema.
- Validation: measure localization and normal/defect errors separately from unsupported language, region-text disagreement, latency and human review time.

## Failure boundary

- Synthetic training patterns may not cover real defects. Validate on unseen real anomalies and acceptable normal variation.
- Tiny defects may disappear during acquisition or preprocessing. Inspect the original and effective input resolution.
- Location and text can disagree. A confident root-cause statement does not establish depth, mechanism or acceptability.
- Updated weights, prompts, token generation settings or normal references require renewed checks of affected outputs.

## Selection gate

Compare WinCLIP, AnomalyCLIP and AnomalyGPT on the same images, image resolution, required defect sensitivity and hardware. First compare localization errors; then determine whether dialogue reduces review time enough to justify language errors and generation cost. WinCLIP and AnomalyCLIP do not natively provide the same dialogue output. Do not describe all three as external-evidence assistants.

## Visual primitives

- `training_pairs`: synthetic image, same-location mask and text; frozen backbone/LLM versus trained decoder/prompt learner.
- `internal_localization`: image -> local features -> image decoder -> normal/anomaly text matching -> location map.
- `location_guided_dialogue`: map -> prompt learner -> LLM, with image representation and question entering separately.
- `evidence_review`: same original image, proposed location and answer; observed versus inferred versus unknown.
- `selection`: common localization task first, additional dialogue benefit and cost second.

## Sources

- Gu et al., "AnomalyGPT: Detecting Industrial Anomalies Using Large Vision-Language Models," arXiv:2308.15366 / AAAI 2024, [official project](https://anomalygpt.github.io/), [official implementation](https://github.com/CASIA-LMC-Lab/AnomalyGPT).
- Course source: `full-model-course/04-anomaly-detection.md`, pages 04-67 through 04-70.

## Production gate

Research contract and visual primitives are complete. Pages 04-67 through 04-70 may proceed to white high-density C / D visual production and model-local QA.

## F01 模型中心思想與來源核對

一般看圖聊天模型能說出物件，卻常說不清局部異常。AnomalyGPT把細粒度定位接到語言提示中，用合成異常及文字配對訓練，讓回答有區域依據。

**合成圖文練習**：合成異常影像與對應說明提供訓練資料；不是只對通用聊天模型加一句請找瑕疵。

**先取得定位訊號**：固定影像編碼器的局部特徵經 image decoder 與正常／異常文字比較形成位置圖；few-shot 路徑可用正常記憶庫。

**位置引導回答**：Prompt learner 將定位資訊轉為 LLM 可用的提示，連同影像和問題產生回答；外部 specialist 覆核是應用擴充，不是必要模型輸入。

**移除設計自測**：保留 LLM 卻拿掉定位資訊到 prompt learner 的連接，會少什麼？

會少了讓回答受局部異常訊號引導的路徑；語句仍可能流暢，但位置與描述不一定一致。人仍需回看原圖核實。

**選型**：需要互動解讀時可列候選；和只輸出分數／位置的方法分開驗證。文字正確、定位正確及覆核耗時各自量，不能把回答當成精密量測。

[原論文／官方來源](https://arxiv.org/abs/2308.15366)。本輪原生 SVG 結合既有生成金屬件；特徵與差異為教學設定，沒有新增推論。先前章節如描述應用擴充，不應解讀為原模型必需步驟。

<!-- wi033-engineering:start -->
## WI-033 工程圖修正

### AnomalyGPT：用成對資料學定位與回答

用合成異常影像、位置遮罩及文字配對訓練；預訓練影像編碼器和LLM保持固定，更新影像解碼器及提示學習器。遮罩和描述須對上同一異常，否則不同監督互相矛盾；真實未見缺陷仍需獨立驗證。

合成影像、遮罩與文字要描述同一處异常。

來源：https://github.com/CASIA-LMC-Lab/AnomalyGPT

### AnomalyGPT：定位由內建支路產生

影像編碼器提供全局與局部表示。局部表示經影像解碼器，與正常／異常文字特徵匹配得位置圖，再由prompt learner轉為提示；LLM另接全局影像表示與使用者問題。此圖是原模型內建支路，不把任意外部檢測器當必要輸入。

內建位置圖先轉提示，再連同影像與問題產生回答。

來源：https://github.com/CASIA-LMC-Lab/AnomalyGPT

### AnomalyGPT：文字與位置一起交付

交付原圖、內建定位與對話記錄，逐項核對文字描述的部位和異常類型。對話可協助判讀但不能替代定位驗證；若回答與圖不一致，保留失敗狀態並回原圖。額外外部檢測器是應用整合選擇，不是原模型必需支路。

回答、位置和原圖一起覆核，對不上就保留疑問。

來源：https://github.com/CASIA-LMC-Lab/AnomalyGPT

### AnomalyGPT：會回答不代表會判對

同一支架若位置圖指中部，回答卻描述孔邊，不能因語句流暢就放行。以同一批真缺陷與正常圖比較只看位置或加問答的錯誤、延遲和人工覆核时间；沒有收益時保留簡單流程也合理。

同圖比較定位與文字證據，再量覆核成本。

來源：https://github.com/CASIA-LMC-Lab/AnomalyGPT

<!-- wi033-engineering:end -->

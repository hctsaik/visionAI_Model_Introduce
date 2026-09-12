# WinCLIP (`ad-winclip`)

- roadmap category: `anomaly-detection`
- course pages: `04-59` through `04-62`
- research status: `complete`
- visual status: `ready-for-visual-production`

<!-- topic-learning-bridge:start -->
## 先讀這 90 秒

> 本段由 `_course_content/topics/ad-winclip.json` 產生，供首次讀者建立正確邊界；下方工程契約仍是實作與驗證依據。

### 現場問題
金屬板的細痕 p 需要檢出，正常孔邊 q 又不能一直誤報；先確認資料與需要的位置或問答輸出。

### 它交出什麼，也不交出什麼
交付可疑位置線索；文字或熱圖都不能直接代表精密輪廓、尺寸、根因或自動放行。

### 一句心智模型
人工組合正常／異常狀態詞與句型，固定 CLIP 把文字和視窗影像轉成可比較的表示。各視窗的異常分數排回覆蓋位置，以調和平均聚合重疊與多尺度線索。WinCLIP+ 再用少量正常品建立 patch／視窗特徵庫，找最相似正常特徵的距離，融合文字線索。

**限制：** 語意與位置仍可能錯；必須用未見正常與真缺陷檢查適用範圍。

### 換一個現場再推理
新產品外觀、允收反光與缺陷型態都不同。

**問題：** 哪些準備與驗證不能直接沿用？

**核對：** 重新核對提示來源、正常參考或既有模型的適用範圍；有適配時另留驗證資料。分開檢查正常誤報、真缺陷漏檢與成本；需要對話時再驗文字是否有據。
<!-- topic-learning-bridge:end -->
## Model identity

This course's WinCLIP is **WinCLIP: Zero-/Few-Shot Anomaly Classification and Segmentation** (CVPR 2023). It extends frozen CLIP for zero-shot and few-normal-shot anomaly classification / segmentation with a compositional ensemble of state words and prompt templates, plus efficient image-, window-, and patch-level visual features aligned to normal / anomalous text.

WinCLIP+ is the few-normal-shot extension: it supplements language-guided scores with declared normal reference images. Prompt text, state words, templates, category names, CLIP checkpoint, window construction, feature level, and aggregation are model inputs and operating state. “Zero-shot” does not turn a prompt score into a calibrated production defect probability, and it does not remove the need for local calibration, failure evidence, or abstention policy.

## Architecture path

### Build

Lock the CLIP image and text encoder checkpoint / preprocessing -> declare product / class names, normal and anomaly state-word vocabulary, prompt templates, ensemble weights, tokenization, and text embedding normalization -> construct fixed ROI and one or more window scales / strides -> encode full image, windows, and declared patch features -> compare each visual embedding with normal and anomalous text embeddings -> normalize and aggregate similarity differences into image score and localization map.

For WinCLIP+, also version the normal reference IDs, reference preprocessing, bank size / selection / aggregation, split and contamination audit. Version checkpoint, model revision, image resolution, crop / resize / colour / normalization, ROI / registration, windows / strides / padding / scale policy, patch / window / image feature layers, prompt ensemble, state vocabulary, class names, similarity metric / temperature / normalization, few-normal reference policy, map resize / smoothing / aggregation, calibration / threshold, decision unit, seed, hardware, and abstain / review rule.

### Inference

Test ROI -> same preprocessing -> image, window, and patch extraction under declared scales -> frozen CLIP image embeddings -> normal / anomaly prompt text embeddings (and declared normal references for WinCLIP+) -> similarity-difference terms -> versioned window / patch / image aggregation -> localization map and image score -> local calibration / threshold / abstain -> PASS / REVIEW / HOLD.

Store the input, ROI, prompt-set revision, text embeddings or hashes, window layout, visual embedding state, optional normal references, normal / anomaly similarities, map / image score, calibration state, and decision together. Latency includes crop / window construction, all visual encodes, text-embedding reuse or construction as declared, reference lookup, similarity, aggregation, transfer, and hand-off; measure P50/P95/P99 under the actual window / batch / hardware policy.

## Representation and score

- Normality representation: CLIP's image-text alignment against the locked normal / anomalous prompt ensembles, optionally complemented by a fixed normal-reference bank in WinCLIP+.
- Local evidence: window- and patch-level normal-versus-anomaly text similarity differences under the declared layout, not natural-language fluency or a global image score alone.
- Image score: a versioned aggregation of image / window / patch score terms, or those terms plus the stated normal-reference contribution, with local calibration / threshold under a declared decision unit.
- The score is an operating signal, not a defect probability, root-cause label, proof of localization at sub-window scale, or a guarantee that unseen product / surface language is semantically covered.

## Cost and operating contract

Version together:

- CLIP family / checkpoint / tokenizer / image resolution / precision / device; image and text preprocessing; class naming policy; normal and anomaly state vocabulary; prompt templates / ensemble weights; text-embedding cache revision; similarity / temperature / normalization;
- normal-reference IDs, split, contamination audit, number, sampling / selection, memory layout, and aggregation when using WinCLIP+;
- ROI, registration, input resolution, crop / padding, colour conversion, transforms, normalization, full-image / window / patch extraction, window scales / sizes / strides / overlap, and feature aggregation;
- map resize / smoothing / masking, image aggregation, calibration data / method / threshold revisions, decision unit, abstention policy, review owner, and output schema;
- prompt sensitivity, vocabulary / naming ablation, normal-versus-anomaly margin distributions, low-FPR, false reject / review load, local / global localization, few-normal reference benefit, unseen-product / future / drift evidence, and error taxonomy;
- complete image-to-decision P50/P95/P99, window count / batch policy, GPU / CPU memory, cache condition, transfer / hand-off, repeatability, and hardware.

## Failure boundary

- Prompt wording, state-word composition, class names, language, tokenization, or text embedding normalization can reverse a similarity margin; prompt revisions require calibration and regression evidence.
- CLIP's global semantic alignment and finite window / patch resolution can miss tiny defects, repetitive texture issues, effective-pixel failures, or localized defects below the declared window scale.
- Image / text domain mismatch, product naming gaps, novel material / illumination / view / camera / background shift, and language ambiguity can produce false alarm or false normal margins.
- A few normal references may help but create selection, contamination, bank-coverage, and memory / latency dependencies; they do not make the release independent of data governance.
- Similarity normalization, window / patch weighting, aggregation, calibration, and threshold can alter low-FPR behavior independently of a visually plausible heatmap.
- Natural-language explanation is not localization evidence; global logical defects, missing relationships, and causal diagnosis remain outside this score path.

## Selection gate

Consider WinCLIP for an exploratory zero- or few-normal-shot semantic candidate when labels are scarce, CLIP / prompt state can be governed, and a team needs a rapid image / window-level hypothesis before specialist evidence is available. Verify prompt sensitivity, product naming, effective pixels, normal-reference policy, local calibration, low-FPR / review load, abstention, unseen product, and complete P95.

Hold or prefer a specialist AD path when prompts drift, defects are small relative to windows, naming / image domain coverage is unclear, low-FPR or localization traceability is critical, normal references are ungoverned, or global logic dominates. Compare AnomalyCLIP, AnomalyGPT, and WinCLIP with the same prompt revision, ROI, window policy, class names, normal support / references, calibration, owner action, hardware, and error taxonomy; do not choose by fluent descriptions.

## Visual primitives

- `prompt_ensemble`: declared normal / anomaly state words, templates, class names, tokenizer / text encoder, ensemble embeddings, and prompt revision.
- `window_alignment_path`: ROI -> full image / windows / patches -> frozen CLIP image embeddings -> text similarities -> normal-anomaly margins -> map / score.
- `few_normal_extension`: WinCLIP+ reference IDs / bank policy and complementary normal-image contribution; absent from pure zero-shot claims.
- `prompt_evidence_review`: prompt sensitivity, margin distributions, window map, false rejects, low-FPR, review load, abstention, unseen product, and complete P95/P99.
- `selection_gate`: prompt / language drift, tiny-defect effective pixels, domain / naming coverage, reference-bank governance, global logic, and fair VLM comparison.

## Evidence bundle

Keep CLIP and tokenizer revisions; prompt vocabulary / templates / class names / ensemble embeddings; normal reference IDs and contamination audit for WinCLIP+; ROI / image recipe / window / patch layouts; image, window, patch, text, normal-reference, similarity, map, score, calibration, and decision traces; prompt / naming sensitivity results; small-defect and drift failures; local calibration, low-FPR, false reject, review load, abstention, localization, and unseen-product evidence; runtime / memory / hardware / cache records; and a prompt or drift rebuild trigger.

## Sources

- Jeong et al., "WinCLIP: Zero-/Few-Shot Anomaly Classification and Segmentation," CVPR 2023, pp. 19606–19616, [CVF open-access paper](https://openaccess.thecvf.com/content/CVPR2023/html/Jeong_WinCLIP_Zero-Few-Shot_Anomaly_Classification_and_Segmentation_CVPR_2023_paper.html).
- Course source: `full-model-course/04-anomaly-detection.md`, pages 04-59 through 04-62.

## Production gate

Research contract and visual primitives are complete. Pages 04-59 through 04-62 may proceed to white high-density C / D visual production and model-local QA.

## F01 模型中心思想與來源核對

只有少量甚至沒有目標正常樣本，想先借用文字描述正常與異常；但整圖 CLIP 容易忽略小瑕疵。WinCLIP用不同大小視窗保留局部語意線索。

**固定文字狀態組合**：用正常／異常狀態詞與模板形成 prompt ensemble，借用固定 CLIP 的圖文對齊，不是即席聊天。

**不同範圍看局部**：全圖、重疊視窗與局部特徵提供不同尺度資訊，局部證據再回到相應位置。

**比較並聚合**：比較影像表示與正常／異常文字；WinCLIP+ 才另加入少量正常視覺參考，兩種設定分開驗證。

**移除設計自測**：只留下整圖 embedding，小缺口為什麼可能被忽略？

大部分正常背景可能主導整體表示；視窗讓局部異常有機會單獨參與比較。但缺口若小於有效解析度，視窗也救不了。

**選型**：無目標訓練資料可先做語意探索；有少量正常參考可比較 WinCLIP+。文字相似不等於缺陷機率，換產品重新驗證提示與尺度。

[原論文／官方來源](https://arxiv.org/abs/2303.14814)。本輪原生 SVG 結合既有生成金屬件；特徵與差異為教學設定，沒有新增推論。先前章節如描述應用擴充，不應解讀為原模型必需步驟。

<!-- wi033-engineering:start -->
## WI-033 工程圖修正

### WinCLIP：文字與局部視窗檢查新件

目標零樣本WinCLIP以人工文字狀態和視窗表示評局部異常，無目標訓練仍須目標留出驗證。WinCLIP+可另加少量正常視覺參考，需明列實際使用模式。

固定模型仍要固定提示、取像與驗證。

來源：https://arxiv.org/html/2303.14814v1

### WinCLIP：視窗分數，依覆蓋位置聚合

固定CLIP，人工正常/異常狀態詞與句型組合產生文字表示；每視窗整體表示與文字比相似。分數分給視窗所覆蓋位置，同位置重疊視窗使用調和平均，再融合多尺度。給定同尺度兩窗0.2/0.8，在共同覆蓋p的平均為2/(1/0.2+1/0.8)=0.32，不是算術平均0.5，也不是缺陷機率。

文字定狀態，視窗分數依覆蓋回到位置。

來源：https://arxiv.org/html/2303.14814v1

### WinCLIP：零樣本與正常參考要分清

保存CLIP版本、人工提示、視窗尺度/聚合、前處理；WinCLIP+另外保存正常參考和視覺比對。不能用+的結果宣稱未用正常參考，也不把相似分數當概率。

增加正常參考，資料與庫版本也成為設定。

來源：https://arxiv.org/html/2303.14814v1

### WinCLIP：與學習提示比較

兩方法均以CLIP語意與局部特徵提供異常線索；前者人工設計文字，後者使用輔助標註學物件無關提示。同資料與錯誤成本比較，不預設固定排名。

同件比較人工提示與學習提示的成本。

來源：https://arxiv.org/html/2303.14814v1

<!-- wi033-engineering:end -->

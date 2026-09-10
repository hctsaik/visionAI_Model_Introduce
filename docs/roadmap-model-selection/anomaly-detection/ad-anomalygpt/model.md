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

This course's AnomalyGPT is the industrial anomaly dialogue model in *AnomalyGPT: Detecting Industrial Anomalies Using Large Vision-Language Models* (2023; AAAI 2024). It trains an LVLM with simulated anomalous images and paired textual descriptions, a prompt learner, a visual-language bridge, and a lightweight visual-textual image decoder for location output. It can answer anomaly questions and propose evidence regions, but both are candidate evidence—not calibrated PASS / FAIL decisions.

Production use is an assist layer: ground the response in declared image / region / specialist evidence, expose uncertainty and an explicit next human / specialist confirmation, and keep final class / heatmap / release responsibility outside the LLM. Do not reinterpret the paper's task score or natural-language fluency as a safety, metrology, root-cause, or automatic release guarantee.

## Architecture path

### Build

Lock normal support, image recipe, and simulated-anomaly generation / mask / text-description policy -> version visual encoder tokens, prompt learner, visual-language bridge / LVLM base and adaptation checkpoint, instruction / dialogue templates, text schema, image-decoder / localization branch, losses, seed, optimizer, and training split -> validate image / text grounding, localization evidence, hallucination, abstention, review routing, and security boundary.

Version all source and simulated data IDs / licenses / target split, prompt weights, vision encoder, bridge projection, LLM model / revision, tokenizer, temperature / top-p / max-token policy, system and retrieval / SOP snapshot, response and evidence-region schema, image decoder, calibration / specialist model links, threshold / owner action, data-retention / redaction / access policy, hardware, and complete latency.

### Inference

Test ROI and any specialist evidence -> fixed preprocessing -> visual encoder tokens plus learned prompt -> bridge / LVLM with locked dialogue / retrieval / schema policy -> candidate anomaly text response; image decoder / localization branch -> candidate evidence region / map -> grounded-evidence and uncertainty check -> specialist or human confirmation -> PASS / REVIEW / HOLD under the owner’s decision contract.

Store ROI, evidence-region references, model / prompt / retrieval / SOP revisions, user request, generation controls, response, uncertainty / abstention, localization output, specialist confirmation, and final decision. P95 includes preprocessing, visual encoding, bridge, retrieval, generation tokens, image decoder, grounding checks, hand-off, and the declared batch / cache / hardware policy.

## Representation and score

- Representation: visual tokens aligned with learned prompt and language-model state; local signal is an image-decoder / visual-textual matching location candidate.
- Output: a structured response plus evidence region and uncertainty / abstain fields. Neither text confidence nor decoder activation is a defect probability or final release score.
- Decision: only a versioned specialist / human policy can convert grounded evidence into PASS / REVIEW / HOLD.

## Failure boundary

- Simulated anomaly-text pairs can miss production morphology, language, and error taxonomy; record synthetic-to-real transfer evidence.
- Hallucination, ungrounded answers, unsupported causal diagnosis, and region-text disagreement require abstention and human confirmation.
- Prompt, LLM / tokenizer, bridge, retrieval / SOP, temperature, schema, and output-length revisions change output behavior and must be versioned.
- Sensitive images, prompts, SOP / retrieval data, retention, access, and external model endpoints require explicit security and privacy boundaries.
- Token generation / retrieval and image decoder make latency variable; never report encoder-only timing as complete P95.
- The assist layer does not solve tiny-defect effective pixels, global logic, or low-FPR release requirements without a specialist evidence path.

## Selection gate

Consider AnomalyGPT for grounded engineering assistance: explaining a specialist finding, retrieving a declared SOP, drafting a review summary, requesting more evidence, and routing uncertain cases. Require evidence-region links, uncertainty / abstention, a human / specialist owner, hallucination testing, security approval, real holdout review, and complete latency.

Hold it out of autonomous release when grounding is absent, evidence regions cannot be verified, prompt / retrieval / model state is uncontrolled, sensitive data policy is missing, token P95 exceeds the workflow, or low-FPR / precise localization is critical. Compare WinCLIP / AnomalyCLIP / AnomalyGPT as assist layers under the same ROI, evidence schema, prompt / retrieval revision, owner action, latency, privacy boundary, and error taxonomy.

## Visual primitives

- `simulated_instruction_path`: normal support -> simulated anomaly / text pairs -> prompt learner -> bridge / LVLM / decoder state.
- `grounded_assist_path`: ROI + specialist evidence -> visual tokens / prompt -> bridge / LLM -> candidate response and evidence region -> uncertainty / human confirmation.
- `output_schema`: evidence-region ID, observed-versus-inferred statement, uncertainty / abstain, SOP / retrieval revision, next confirmation action, and final owner.
- `assist_evidence_review`: grounded-answer rate, hallucination, region-text agreement, synthetic-to-real transfer, review load, token / full P95, drift, and security audit.
- `selection_gate`: grounding, security / sensitive data, latency, specialist confirmation, tiny defects / global logic, and fair VLM-assist comparison.

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

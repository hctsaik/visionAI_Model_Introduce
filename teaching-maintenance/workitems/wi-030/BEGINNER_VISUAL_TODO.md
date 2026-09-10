# WI-029 兩入口重製
- [x] 六案例／12PNG、Markdown主線、互動、自評、驗證、學習及commit＋push／公開核對完成。詳見 workitems/wi-029/RELEASE.md。

# Beginner visual redesign TODO

## WI-027 視覺基礎與多模態七課重製
- [x] 保存七課基準、讀五份權威與 skills、實看參考／現版、核對第一手來源及版本；14張基準截圖與sources.md。
- [x] 逐圖版本化 preflight 與DINOv2原型 PNG 審查；原型94，其他成圖仍各自審查。
- [x] DINOv2／DINOv3 核心、反例、比較及獨立手機圖。
- [x] CLIP／SigLIP 核心、反例、比較及獨立手機圖。
- [x] LLaVA／Qwen-VL／Gemini Vision 核心、反例、比較及獨立手機圖。
- [x] 整合正文、資料準備／成本／驗收、自測、model.md；構建 course/docs。
- [x] 逐圖與整頁審讀評分、桌面手機互動／引用／HTTP、必要回歸。
- [x] 學習寫回、保存副本與接續紀錄；commit／push 及公開核對。


## WI-028 下一輪：時序八課與兩個工作入口
- [ ] 保存八個時序主題及 production／foundations 基準，讀最新學習及來源。
- [ ] 逐圖 Markdown preflight、代表原型與實際PNG審查。
- [ ] 重製 Frame Difference／Background Subtraction／Lucas–Kanade／RAFT。
- [ ] 重製 ByteTrack／ConvLSTM／VideoMAE／V-JEPA。
- [x] production／foundations 已由WI-029完成與發布；本項其餘八課保持待辦。
- [ ] 桌面手機、圖文／互動／HTTP、逐圖及整頁評分、必要回歸。
- [ ] 學習回寫、保存副本、commit＋push及公開核對。

## WI-026 生成與影像復原八課重製
- [x] 2026-09-10 commit `bd4b87b` 已 push；遠端一致、Pages success、公開 HTML／38 PNG hash 通過。下方未發布描述為前次 checkpoint。
- 收尾：17份保存副本hash一致，git diff --check PASS；正式本機引用與生成候選已分開記錄。
- [x] 保存八課基準、核對第一手技術來源、實看首選參考與現版；16張桌面手機baseline畫面已保存。
- [x] 完成版本化逐圖brief／preflight，單張原型實際PNG審查；18 preflights PASS，Inpainting r02桌面原型已實看。
- [x] 重製DefectFill、AnomalyDiffusion、TF-IDG核心、限制與比較。
- [x] 重製ControlNet、Inpainting核心、限制與比較。
- [x] 重製Diffusion Restoration、Deblur、Super-resolution核心、限制與比較。
- [x] 整合八課正文、自測及正式首讀引用，重建course/docs。
- [x] 逐圖與整頁評分、桌面手機互動／插槽／HTTP、必要回歸。
- [x] 共用學習與保存副本、TODO／STATUS實際結果更新。
- 38圖自評91–95，8頁93–94（v1.0逐項證據）；48狀態144圖放大／Escape、自測與導覽通過，最後操作卡修正後16狀態可見文案／圖片／無溢出通過；76次HTTP hash與course/docs一致，5項回歸PASS、8課preflight PASS。
- 完整slot audit保留24筆舊工程SVG中繼資料及slide-manifest的歷史樣式標記，沒有新首讀圖或disk/HTTP錯配；文字因果鏈實際img/object=0。未以首讀分數代表原工程圖，未跑真人學習／模型實測，使用者核准pending。未commit/push，公開網站尚未更新。

## WI-025 視覺參考偏好落盤
- [x] 核對使用者貼圖與既有風格優先順序。
- [x] 寫入首選／次選參考及下輪使用方法。
- [x] 兩張首選參考路徑存在，3份更新副本SHA256一致，git diff --check通過；僅文件更新，未 commit/push。

## WI-024 偵測課程重製
- [ ] 核對使用者六題／四連結差異；先做四個明確主題。
- [x] 保存基準、讀規範與方法來源、實看現版與參考。
- [x] YOLO dense：桌面／手機單圖原型、反例與比較、圖文整合。
- [x] RT-DETR：查詢／多尺度／一對一訓練與無NMS邊界。
- [x] Grounding DINO interface：文字與影像交互、短語定位與輸出責任。
- [x] YOLOE：文字／視覺／免提示三模式、框與mask及準備成本。
- [x] 各圖自評、整頁審讀、course/docs互動、必要回歸：20PNG、24狀態72圖互動；最終8狀態與40本機HTTP hash，8 tests／6 subtests通過。
- [x] 更新skill／共用Markdown與保存副本；commit/push、公開網站核對：184f1ee，Pages成功，公開HTML與20PNG hash一致。
- 四個已提供連結的課程完成，20張不同PNG已生成並實看原生／328px；24狀態互動及最終本機／公開核對通過。另兩題待提供；使用者成品核准pending，未做真人學習測試。

## WI-014 ECC R01 visual 1（2026-09-07）

- [x] 2026-09-08 R06：整題第一遍依 C1–D5 重產五張獨立 PNG；工程參考維持文字；正式四張未重畫。
- [x] 2026-09-08 R05：首圖改為 C 型「它在做什麼／怎麼做」；live 標題已換成微調重合。HOLD 頁留在後面。
- [x] 2026-09-08：agent 自截 course／docs；發現 docs 機制圖 388×194 SVG。已重建 docs、寫入 slot-audit Markdown＋skill。course/docs 現為 r04 894–936px。
- [x] 禁止完成條件含「請使用者刷新回報」。
- [x] G0：記錄正式 topic／F02 基線，暫停 ChArUco 為平行未完成項。
- [x] G1：寫共用 log 學習與 `tmp/ecc-r01/brief.md`。
- [x] 跑 `validate_teaching_preflight.py`（不帶正式 topic）PASS。
- [x] 產生桌面 1600×900 與手機 720×1280 PNG／SVG，保留 F02。
- [x] OpenCV ECC 證據入 `ecc-evidence.json`／manifest。
- [x] 像素／takeaway／殘差色差核對完成；view_image 仍不可用，已記 view-limit。
- [x] 擁文評分：桌面 82、手機 79，未過 >90。
- [x] 修同一張：加大殘差＋色尺、畫出反變換、減少數字後重評。
- [x] 重評桌面 93／手機 91，完成度各 ≥8，無否決項。
- [x] 正式 topic 第一張已改接 `ecc-r01-core.png`／mobile PNG，並重建 HTML；HTTP 已回傳 R01。
- [x] 其餘四張 beginner、比較圖與主線文案已換成同一 A-17 故事並重建 HTML。
- [ ] 使用者接受保持未做。

### R08 integration geometry update (2026-09-06)

- [x] Add candidate-only `full-mobile` wrapper with optional intrinsic width/height.
- [x] Use the same versioned mobile PNG for candidate reference and verification; remove fixed 1672×941 nested mobile geometry.
- [x] Produce candidate page, static geometry contract, hashes, and rollback packet.
- [ ] Sol integration recheck and formal topic update remain pending.

### R07 formal integration candidate (2026-09-06)

- [x] Stage a versioned topic candidate and integration packet without editing formal `charuco.json`.
- [x] Copy R07 desktop/mobile PNGs to versioned generated assets and record exact hashes.
- [x] Record formal-topic hash and rollback path; await Sol page recheck.
- [ ] Formal integration, user approval, and batch rollout remain pending.

### R07 layout-gate update (Luna, 2026-09-06)

- [x] Move desktop provenance outside panel 1 and move detector/c17 evidence upward with bottom padding.
- [x] Increase mobile third-zone spacing/height without clipping the fourth zone or takeaway.
- [x] Re-render and inspect R07 desktop/mobile PNGs; update manifest hashes and evidence.
- [ ] Sol re-review and user approval; formal topic and batch rollout remain unchanged.

### R06 delivery-gate update (Luna, 2026-09-06)

- [x] Rebuild versioned R06 SVGs from actual R05 source without overwriting R05.
- [x] Remove all `qq/PP`, `q/P P`, and `q17q/PP17`; use readable `image q / board P` notation.
- [x] Add physical m17/m23/c17 board callouts, split detector evidence, and wrap mobile takeaway with 30px side padding.
- [x] Generate and inspect R06 desktop/mobile PNGs; save complete manifest with hashes, font, and detector evidence.
- [ ] Sol re-review and user approval; formal topic and batch rollout remain unchanged.

### R03 delivery-gate update (Luna, 2026-09-06)

- [x] Versioned native SVG desktop/mobile candidate produced while preserving R02.
- [x] Added distinct m17/m23 marker patterns, separate c17, four non-collinear PnP pairs, predicted c17/residual, REVIEW/HOLD gate, and counterfactual self-test.
- [x] Rasterized and inspected actual desktop/mobile PNGs with local Qt fallback.
- [ ] Resolve local font/rasterizer failure: PNG geometry is visible but text is unreadable; do not call this a visual pass.
- [ ] Obtain user review/approval; keep formal topic and batch rollout unchanged.

## WI-013 Sol→Luna→Sol：ChArUco R02 整章審查與原型修訂（2026-09-06）

### R03 單張核心原型 checkpoint（Luna，2026-09-06）

- [x] 找到 R02 原生 SVG／Edge Playwright 匯出入口，確認 R02 舊資產保留。
- [x] 建立 versioned preflight：`tmp/charuco-r03/brief.md`。
- [ ] 繪製 R03 真實 ChArUco 板、marker/corner 身份、ArUco＋棋盤分工、calibration/PnP 分界與固定 `c17`。
- [ ] 輸出並實看 R03 桌面／手機 PNG；記錄尺寸、hash 與可見缺口。
- [ ] 建立 R03 manifest、只更新首圖候選引用；不批量改五張主圖。
- [ ] 執行 preflight／局部資產檢查；`visual_status` 維持 `prototype_pending_user_review`。
- [ ] 回報未解決問題；Sol 複審與使用者接受另行記錄。

- [x] 使用者指定 Playwright 後，獨立 Playwright + Edge 開頁、讀 DOM、首屏截圖並實看成功；其餘章節與手機驗證仍待完成。

- [x] 使用 teaching-review-cycle，核對現行 HTTP R02 首圖與本地 bytes 並實看 PNG。
- [x] Sol 依固定量表完成可取得範圍的整章重評：頁面 72/100；五張 beginner 主圖 60/65/64/71/72；三張輔助圖未評估。
- [x] Sol 撤回舊 R02 自評 92 作為有效品質分數，保留為歷史；完整問題與學習寫入共用 log。
- [x] 建立 `CHARUCO_R02_SOL_TO_LUNA_HANDOFF_2026-09-06.md`，含 `CHAR-P0-01` 至 `CHAR-EVID-11` 的修訂與驗收條件。
- [ ] Luna 先修一張核心原型：正確 ChArUco 板、marker/corner 身份、存在理由、calibration/PnP 分界、c17 追蹤。
- [x] Luna 完成 R03 brief/preflight 與候選 SVG／手機 SVG／manifest；R02 未覆寫、未接入正式 topic。
- [ ] 產出並實看 R03 桌面／手機 PNG；目前 Edge／Playwright `WinError 5` 阻塞，不能以 SVG 原始碼代替成品檢查。
- [ ] 修正 Sol delivery-gate 發現：唯一 marker 圖樣、`m17/m23` 與 `c17` 身份、至少四組非共線 PnP correspondence、predicted c17 可回算、P95／coverage 門檻、正式自測接入。
- [ ] Sol 複審原型；未通過則逐 ID 回交，不得批量推展。
- [ ] 持續循環：每輪保留舊版、寫回 Sol 學習、由 Luna 只修一張原型，再由 Sol 逐 ID 複審；Sol 通過不等於使用者接受。
- [ ] 逐張補查三張輔助圖、桌面／手機互動與 lazy-load；使用者接受另行記錄。

## WI-013 ChArUco R02：依五份指定 Markdown 重做，等待使用者審閱（2026-09-06）

- [x] 讀取並對齊 `CLAUDE.md`、`IMAGE_STYLE_GUIDE.md`、`TEACHING_REVIEW_LOG.md`、`TEACHING_SCORING_RUBRIC.md`、`TEACHING_WEBPAGE_GUIDE.md`。
- [x] 完成單頁 preflight：C 型 Engineer + AI Story、四個主節點、單一路徑與 `#FFF4CC` takeaway；證據：`tmp/charuco-r02/brief.md`。
- [x] 先做一張 prototype，再以 Edge 實際輸出桌面／手機 PNG；證據：`tmp/charuco-r02/final/desktop.png`、`tmp/charuco-r02/final/mobile.png`。
- [x] 將 R02 prototype 接入 `charuco.json`、`interactive-learning.html` 與 `docs/index.html`；舊 F02 保留作為稽核基線。
- [x] 執行 machine-checkable preflight gate：`tools/validate_teaching_preflight.py` 通過。
- [!] `visual_status` 保持 `prototype_pending_user_review`；未把實作或測試通過當成使用者核准。
- [ ] 使用者確認圖的中心思想、視覺風格與網頁閱讀順序後，才可把 R02 標成可用並推展同家族。

## WI-012 F02 — 27 題核心重建撤回，全部待修訂（2026-09-06）

### G0：範圍與基線

本輪接續全站盤點：58 個正式 topic 中，分類／分割／姿態 8 題、偵測 6 題與異常偵測 17 題已有近期核心修訂；本輪處理幾何 4 題、時間／影片 8 題、Foundation／VLM 7 題、Diffusion／復原 8 題，共 27 題。每題以現行 `_course_content/topics/<slug>.json`、對應 `roadmap-model-selection/**/model.md`、原有第一張案例圖與 `TEACHING_SCORING_RUBRIC.md v1.0` 為基線。

### G1：學習與取捨（先於生成）

採納既有 F01 原則：第一眼先回答「原本遇到什麼困難」，核心圖要讓輸入、模型專屬轉換、可交付輸出與人的下一步可追蹤，最後用移除核心設計的後果做自測。部分採納舊批次的成功做法：保留同一案例與既有詳細章節；不採納把全站所有模型畫成同一個三欄模板，也不把影像生成結果、embedding、flow、mask、復原圖或文字回答誤稱為量測真值。

家族 brief：

- 幾何（ChArUco、ECC、SIFT、LightGlue）：影像點、模板／局部特徵、幾何變換與 residual／correspondence 要分開；未通過 coverage、初始化、匹配品質或重裝驗證時 HOLD。
- 時間／影片（Frame Difference、Background Subtraction、Lucas–Kanade、RAFT、ByteTrack、ConvLSTM、VideoMAE、V-JEPA）：明畫時間戳與 frame window，分清變化、稠密／稀疏 flow、track identity、預測／表徵；不要把彩色 flow 或 latent 直接當事件真值。
- Foundation／VLM（DINOv2、DINOv3、CLIP、SigLIP、LLaVA、Qwen-VL、Gemini Vision）：分清 feature、image-text similarity、token 對齊與 provider／LLM 回答；任何 score、box、mask、量測或放行都要有命名的下游 owner。
- Diffusion／復原（DefectFill、AnomalyDiffusion、TF-IDG、ControlNet、Inpainting、Diffusion Restoration、Deblur、Super-resolution）：raw、condition、generated／restored estimate 與 review 必須分開；生成／復原改善可讀性不等於還原物理真值，也不覆蓋 raw evidence。

### G2–G3：製作方式與原型

沿用既有各題第一張案例圖作案例身分參考，新增 native SVG 機制總覽；每個家族先用一張代表圖檢查，再批次生成其餘 26 題。左側保留既有案例素材，右側只畫該模型的代表性輸入→轉換→輸出→接手；圖面明示「F02 機制示意，非模型推論」。手機版改為上方案例、下方縱向機制，避免縮小桌面圖造成讀不懂。

### G4–G6：驗證與再學習

成圖檢查先遮住長正文，確認每張圖仍看得到模型特有的關係；再在網站中檢查桌面／手機、放大、章節、自測與頁寬。分數只記新增核心圖的逐圖證據，保留舊圖不沿用歷史高分。若圖只有名詞框而沒有可見轉換，視為需重製；若核心輸出是設定或下游計算，直接標示證據身分。

生成模式：native SVG + 各 topic 現有案例 PNG；未新增模型推論、性能比較或外部部署。實際資產：`_course_content/generated-concepts/<slug>/<slug>-f02-core.svg`、同名 `.png`、`-core-mobile.svg` 及 `f02-manifest.json`。原型與逐圖證據寫入 `tmp/f02-series/`，完成後回填本輪結果。


## WI-012 F02 撤回與待修訂核對（2026-09-06）

本輪 27 題已產生資產與整合頁面，但使用者判定成品質量太差、不可使用；因此 27 題全部撤回為待修訂。 31 題既有近期修訂維持已修訂狀態。

- [x] 幾何 4 題：ChArUco、ECC、SIFT、LightGlue。
- [x] 時間／影片 8 題：Frame Difference、Background Subtraction、Lucas–Kanade、RAFT、ByteTrack、ConvLSTM、VideoMAE、V-JEPA。
- [x] Foundation／VLM 7 題：DINOv2、DINOv3、CLIP、SigLIP、LLaVA、Qwen-VL、Gemini Vision。
- [x] Diffusion／復原 8 題：DefectFill、AnomalyDiffusion、TF-IDG、ControlNet、Inpainting、Diffusion Restoration、Deblur、Super-resolution。

每題已更新 topic JSON 的「為什麼需要、三個核心設計、移除核心自測、換情境 transfer、選型」；對應 model.md 已加入 F02 核心與來源橋接。HTML／docs 已重建，27 題共 270 個桌面／手機頁面狀態通過實際 runtime QA。這是 implementation-complete 與 test-complete；尚未宣稱使用者核准、真人理解或真實模型效能。

持久證據：`teaching-images/vision-ai-model-selection/f02-review.json`、`tmp/f02-series/`、本檔 WI-012 F02 final，以及課程 `BEGINNER_VISUAL_TODO.md`／`BEGINNER_VISUAL_STATUS.md`。

### F02 final evidence

- [x] 27 題 topic JSON、27 個 model.md、54 個桌面／手機核心 SVG、27 個 PNG 與 27 個 manifest 已保存。
- [x] 58 題 HTML 重建；source verifier、contract、navigation、bundle、deep-dive regression 與 270 狀態 runtime QA 通過。
- [x] 每題第一張圖直接顯示「為什麼需要」與三個核心要點；手機版保留縱向案例到人工接手流程。
- [x] 27 題 final desktop first-read 核對完成；未見裁切、核心流程缺失或水平溢位。
- [!] 使用者已判定本輪品質不可用；27 題全部待修訂，不能作為可用教材。

證據：`f02-review.json`、`tmp/f02-series/<slug>/report.json`、`_course_content/generated-concepts/<slug>/<slug>-f02-core.svg/.png`、`<slug>-f02-core-mobile.svg`、`f02-manifest.json`。

## WI-011 F01 — 本輪 17 題核心修訂與工具驗證完成，待使用者審閱

- [x] 保存基準、核對 17 題第一手來源、參考圖與逐題製作 brief。
- [x] 製作並檢視 17 組核心圖（34 個桌面／手機視圖），完成圖後修正。
- [x] 17 題頁首存在理由、可見三要點、反事實與換情境自測、model.md 同步。
- [x] 三個深入主題後續七章逐字保存，首章舊圖仍可切換。
- [x] 188 個章節狀態與 17 個最終頁首驗證；必要回歸、來源／docs verifier 通過。
- [x] 本機 HTML／docs／新資產 hash 與 HTTP 核對，學習回寫共用 log 與指南。
- [?] 真人理解與使用者審閱尚未取得；保留舊圖沒有在本輪全部重新評分，不宣稱整套全面達標。

入口：http://127.0.0.1:8000/interactive-learning.html?rev=ad-f01#view=lesson&lesson=ad-patchcore&slide=1

記憶與證據：`ad-f01-brief.md`、`ad-f01-review.json`、根目錄 `TEACHING_REVIEW_LOG.md` WI-011。生成模式：原生 SVG 搭配既有生成金屬件，PNG 為瀏覽器匯出；特徵與差異皆為教學設定。資產：`_course_content/generated-concepts/<topic>/<topic>-f01-core.svg/.png` 與 `-core-mobile.svg`，各題 `f01-manifest.json` 記錄來源與保存路徑。

本輪新增 37 個啟用資產；發布資料夾引用 1298 個資產。HTML SHA256：`d915635d43a9f69bca7bdce8910130b038d545b9ed62862ec81634a50b45b1ef`。未執行外部部署。後續從使用者指出的具體圖與理解缺口接續，不用自行重跑舊版 renderer。

## WI-010 E03 八模型系列獨立重評（2026-09-06）

- [x] 核對 ResNet E02 與七題 E03 現行正式版本、代表性桌面／手機成品及既有驗證證據。
- [x] 依固定量表重新評比，不沿用製作者自評；建立 `MODEL_INTRO_SERIES_REVIEW_E03_2026-09-06.md`。
- [x] 記錄上輪至本輪分數、實質改善、仍未通過項目及下一輪優先順序。
- [?] 本輪為 review-only，未改圖、未重建頁面；四題為 90 分且所有啟用圖未逐張重新驗收，不能宣稱全系列通過。

## WI-009 D01 六題偵測系列（實作與驗證完成，待使用者審閱）

- [x] 保存基準、實看現頁／參考、核對第一手來源並寫學習brief。
- [x] YOLO dense detector：存在理由、dense／多尺度／NMS、反事實與工作案例。
- [x] RT-DETR：高效編碼、query與集合預測、訓練匹配／推論邊界。
- [x] DINO detector：對比去噪訓練、mixed query selection與框修正；分清訓練和測試。
- [x] Grounding DINO：語言影像融合、文字引導query與跨模態解碼。
- [x] YOLO-World：區域文字對齊、RepVL-PAN與prompt-then-detect。
- [x] YOLOE：文字／視覺／免提示三路及框／mask責任。
- [x] 共同決策比較、逐圖實看與修正、六題桌面手機／自測／放大、必要回歸及bundle。
- [x] 最終分項證據、來源／資產hash、TODO／STATUS／共用log同步。
- [?] 真人理解與使用者審閱，尚未取得。

驗證與逐圖分項：`d01-detector-review.json`及共用log WI-009；自評／工具檢查與真人審閱分開。

## WI-008-R1 外部總評取捨與學習（2026-09-06）

- [x] 讀取總評，核對E01／E02審查範圍與E03正式topic版本；七題SHA256均與E03完成紀錄一致。
- [x] 逐項區分採納原則、部分採納、已改善及待證據提案，不直接繼承總分與優先序；詳見根目錄TEACHING_REVIEW_LOG.md的WI-008-R1。
- [x] 合併共用教學／圖像規則，記錄下一輪如何驗證；保留原AI報告及E03歷史。
- [x] 核對Markdown連結、進度與未製作範圍，完成持久記憶同步。

下輪候選（待證據與具體brief，並非本輪已製作或新增硬性門檻）：

- [ ] 先核對Keypoint漏物件／錯點ID與YOLO候選篩選／mask錯誤的可見後果，挑一個有來源的代表反例作原型。
- [ ] 按任務取得可核對的原圖、真值、模型版本／權重與輸出，再決定真實案例；不用生成圖補造GT或預測。
- [ ] 在現版頁面檢查共同決策表與手機段落是否降低比較負擔，同時保持核心原理在正文。

## WI-008 八模型介紹系列總評（2026-09-06）

- [x] 盤點 ResNet、ConvNeXt、ViT、U-Net、SegFormer、YOLO-Seg、Keypoint R-CNN、Pose Pipeline 的正式 topic 與現行視覺資產。
- [x] 依 `TEACHING_SCORING_RUBRIC.md` v1.0 重評內容、圖片教學力、工作情境與失敗證據。
- [x] 建立 `MODEL_INTRO_SERIES_REVIEW_2026-09-06.md`，逐模型列出保留項、改善缺口、建議修改與優先順序。
- [ ] 本輪未改圖、未改網頁；E03 製作進度與使用者驗收仍依原有工作流追蹤。

目前接續：E03七題中心思想修正與ResNet回查已完成，待使用者審閱。驗證與逐項證據見core-e03-review.json；不以自評宣稱真人理解或穩定收斂。

## E03 七題中心思想補正

- [x] convnext：核心圖、必要原理、三要點與反事實自測；實看和驗證。
- [x] vit-classifier：核心圖、必要原理、三要點與反事實自測；實看和驗證。
- [x] u-net：核心圖、必要原理、三要點與反事實自測；實看和驗證。
- [x] segformer：核心圖、必要原理、三要點與反事實自測；實看和驗證。
- [x] yolo-seg：核心圖、必要原理、三要點與反事實自測；實看和驗證。
- [x] keypoint-r-cnn：核心圖、必要原理、三要點與反事實自測；實看和驗證。
- [x] pose：核心圖、必要原理、三要點與反事實自測；實看和驗證。
- [x] ResNet回查、八題操作、必要回歸／bundle／記憶同步。

- [?] 使用者審閱與真人學習證據，尚未取得。

## WI-007 八主題持續學習（2026-09-06）

- [x] resnet：基準審查、學習、重製、正式整合、成圖／互動驗證、分項評分。
- [x] convnext：基準審查、學習、重製、正式整合、成圖／互動驗證、分項評分。
- [x] vit-classifier：基準審查、學習、重製、正式整合、成圖／互動驗證、分項評分。
- [x] u-net：基準審查、學習、重製、正式整合、成圖／互動驗證、分項評分。
- [x] segformer：基準審查、學習、重製、正式整合、成圖／互動驗證、分項評分。
- [x] yolo-seg：基準審查、學習、重製、正式整合、成圖／互動驗證、分項評分。
- [x] keypoint-r-cnn：基準審查、學習、重製、正式整合、成圖／互動驗證、分項評分。
- [x] pose：基準審查、學習、重製、正式整合、成圖／互動驗證、分項評分。
- [x] 分類組回查ResNet／ConvNeXt；分割組回查前三題及U-Net；關鍵點組回查分割與全套一致性。
- [x] 最終必要回歸、HTML／本機bundle、跨題學習與限制交付。
- [?] 使用者審閱及真人學習證據，未核准。



## PatchCore P04 — P03獨立重評（2026-09-06）

- [x] 確認正式topic已更新為SHA256 `5625A43E...C92561C`，共8章17閱讀視圖、34個桌面／手機資產。
- [x] 逐張檢視P03桌面成圖，另檢視第2/3/5/7/8章代表手機圖與實際頁面截圖。
- [x] 依量表v1.0獨立重評：整頁91；章節最低91、89、91、91、89、91、89、90。
- [x] 不接受P03內部自評93及「每張>90」作驗收；第2章兩層合併、第5章Eq.7、第7章PatchCore與第8章公開重現仍未超過90。
- [?] 使用者審閱尚未核准；本輪只重評與記錄，沒有重製資產。

## PatchCore P03 — 已採納修正完成，待使用者審閱

- [x] 同步撤回P01達標宣稱；核對15視圖中11個未超過90，保留原評分來源與歷史。
- [x] 第7章：同產品、同測試條件，具體畫出三方法的資料→更新對象→待測比較→輸出／覆核；不能只換旋鈕、橢圓、晶片和成本清單。
- [x] 第2章：同一來源局部標出可觀察的邊緣／紋理與鄰域，連至特徵描述的用途；實測激活與概念示意須分列，不補造CNN輸出。
- [x] 第3章：每個代表／被刪點都可回查來源局部，顯示重複變化被合併、獨特正常變化留下；不可把三種部位當真實coreset類別。
- [x] 第5章：從原圖可疑區、其正常近鄰及附近參考，畫到整件判讀，解釋聚合／權重影響；不僅展示2×0.8。
- [x] 第1/6章：補庫內容與資料来源，保持同一待測及候選，直接顯示刪除代表後改配誰及覆核後果。
- [x] 第8章：取得同樣本raw／GT／公開重現output（明列第三方，未冒充原作者）的成功證據與局部判讀；不能從疊圖逆造raw或生成GT。保留有效漏檢對照。
- [x] 重製後逐張實看、分項據證評分；必要桌面手機操作與bundle驗證，全部記憶同步，未達標不得再用平均分結案。

- [?] 使用者審閱：尚未核准；分項證據見共用log P03，完整測試與來源見STATUS最新P03。

## PatchCore P02 — 已有重評紀錄（2026-09-06）

- [x] 鎖定正式 topic hash，逐張重看15個桌面閱讀視圖與代表手機視圖。
- [x] 依量表v1.0先做圖片單獨評分，不借正文、技術正確性或互動QA補圖分。
- [x] 撤回P01「整頁92、逐圖91–94皆達標」作為現版驗收依據；重評整頁89，章節最低89、83、82、91、84、87、71、88。
- [x] 記錄最弱項：第7章PaDiM／EfficientAD差異主要靠文字，第3章特徵點未回連工件局部，第5章分數聚合偏數字化。
- [?] 使用者審閱尚未核准；本輪只評分與記錄，沒有重製資產。

## PatchCore P01 — 整套製作（2026-09-06）

- [x] 回答本輪評分：核對30資產hash及代表截圖；維持原內部自評，說明最弱章與證據限制，不把測試通過當教學滿分。

- [x] 核對現有topic/model契約、保存基準，查原論文與作者程式。
- [x] 先寫學習brief並驗證coreset單圖原型。
- [x] 產生八章：工作資料、CNN局部特徵、coreset、查庫、分數/位置、參考風險、選型成本、作者證據。
- [x] 更正舊首讀描述，正式deep_dive／concept／來源整合。
- [x] 各圖實看、固定量表評分、桌面手機／導航／自測／放大與回歸。
- [x] 更新本機HTML與docs、所有記憶與交付入口。
- [?] 真人學習與使用者核准另列。

## A14 — 全套完成（承接A13，非局部結案）

- [x] 保存實際topic基準，實看認可PPT第4頁及缺口。
- [x] 第1章：分成準備／判讀，每個視圖保留工件、輸出與人的責任。
- [x] 第5章：乾淨／污染兩視圖保留相同待測與原有候選，變因可見。
- [x] 第2章：桌面查庫結果與對應關係可讀。
- [x] 第8章：至少兩個有query／GT／作者輸出的原始成功案例，保留漏檢與誤報。
- [x] 全套來源／數字／逐圖視覺與固定量表審查，未達標即修。
- [x] 本機整合、桌面手機、自測、放大、必要回歸及docs bundle。
- [x] 同步所有未完成清單与學習、交付入口；使用者核准另列。

- [?] 使用者審閱尚未核准；無真人學習／現場推論驗證。

## A13 — 外部建議轉為修正（2026-09-05）

- [x] 實看第7章來源與認可 PPT 參考；採納裁字／局部來源／正常比較三項。
- [x] 第7章 EfficientAD 分件保留原圖示，完整SVG標籤；先驗原型。
- [x] 第7章 PatchCore：產品上標來源區、放大同源局部，再說明代表特徵選樣；不得宣稱三種紋理等於實際coreset。
- [x] 第3章正常候選距離完整呈現，標明設定值。
- [x] 整合、桌面／手機成圖與互動、回歸、bundle、分項審查。
- [x] 後續第1／5章降低對照記憶負擔；第8章找額外原始成功證據，保留解析度限制。（由 A13/A14 實作與驗證完成；此區保留舊版歷史。）
- [?] 真人學習證據與使用者核准尚無。

## A12 current A10 opinion review (2026-09-05)

- [x] Confirm active snapshot `8b56b191...529f30` includes A10 chapter-2 mobile and chapter-4 location/arithmetic assets; inspect the changed views and current weakest comparison view.
- [x] Record judgment: progressive views solve most overload, but the lesson is not finished because retained chapter 1/3/5/7/8 gaps remain and EfficientAD comparison has visibly clipped source text.
- [?] User approval remains pending; no asset was regenerated in this review-only step.

## A11 formal score of active A09 snapshot (2026-09-05)

- [x] Lock active topic snapshot `E3C664B9...BC3D92C` at 21:19:42 and inspect all 16 A09 desktop views, representative mobile views, retained figures 1/5 and A09 page QA.
- [x] Re-score with rubric v1.0: page 90; chapter groups 86, 90, 88, 88, 90, 93, 88, 89. Only chapter 6 clears the strict per-image >90 group gate.
- [x] Continue corrections from the weakest active views; the unintegrated A10 prototype receives no advance credit.（由 A13/A14 實作與驗證完成；此區保留舊版歷史。）
- [?] User approval remains pending; this is reviewer judgment, not a learning study.

## 歷史：WI-003 / A10 (2026-09-05)

- [x] 接續實際 A09 引用、保存 topic 與 renderer 基準，閱讀量表與實看參考。
- [x] 實看完整八章及啟用分段，記錄圖片與頁面缺口。
- [x] 學習先寫回：補強局部距離到位置熱圖的可見轉換；完成單圖原型與逐圖驗證。
- [x] 整合通過檢查的 A10 資產與教材，保留同時更新的 A09 內容。
- [x] 重建、測試桌面／手機導覽、分段、自測、放大與必要回歸。
- [x] 固定量表重評，記錄真實分數／限制及下一步，更新入口和 STATUS。
- [?] 使用者審閱，尚未核准。

A10本輪重製與驗證已完成；整套仍需改善，不是全數達標。後續待辦：

- [x] 先修第7章EfficientAD：A09並行更新擴大來源裁切後露出半截文字，最終實看87分；保留完整循環箭頭但排除來源標籤碎片。（由 A13/A14 實作與驗證完成；此區保留舊版歷史。）
- [x] 補齊第3章正常對照的其他候選距離，讓最小值可由圖內核對。（由 A13/A14 實作與驗證完成；此區保留舊版歷史。）
- [x] 第7章PatchCore代表特徵可回查同產品局部。（由 A13/A14 實作與驗證完成；此區保留舊版歷史。）
- [x] 改善第1/5章密度與手機跨段記憶負擔，限定第8章成功單例的結論範圍，再重新評分。（由 A13/A14 實作與驗證完成；此區保留舊版歷史。）

## 歷史：WI-001 / A09 (2026-09-05)

接續入口：[WORKITEMS.md](../../WORKITEMS.md)。本區是歷史 AnomalyDINO 工作清單，目前以A14為準；下方 A07、v02 與其他輪次是歷史紀錄，不代表正式版本。A09已整合並完成本輪工具驗證；A10並行接續中，以正式topic與最新紀錄核對啟用資產。

- [x] 根據 A08 建立 A09 第 7 圖修正原型，並展開第 2/3/4/6/7/8 章共 16 組桌面／手機視圖；製作證據見 STATUS 與共用 log A09。
- [x] 核對正式topic與A09 manifest，完成裁切碎片與图2超界複查。
- [x] 逐張檢查 16 組桌面／手機視圖，修正問題並記錄實際評圖證據；原型通過不等於全數通過。（由 A13/A14 實作與驗證完成；此區保留舊版歷史。）
- [x] A09已接入正式topic並更新教材文字；視覺品質以A11校準繼續修正。
- [x] A09已重建本機教材及docs bundle，測試與32個桌面／手機視圖驗證記錄於共用log。
- [x] 依固定量表重新評分，保存限制及證據，更新 WORKITEMS、TODO、STATUS 與共用 log。（由 A13/A14 實作與驗證完成；此區保留舊版歷史。）
- [?] 使用者審閱；目前尚未核准，未外部部署。

持久工作記憶 WI-002：已建立根目錄入口與 AGENTS.md 接續規則；本次只整理工作紀錄，未執行上述待辦。

## A07 renewed learning and production cycle (2026-09-05)

- [x] Reinspect the PPTX comparison reference and A06 image 7 prototype; record concrete learning before regeneration in shared log A07.
- [x] Correct image 7 training relations and feature-bank metaphor; inspect actual output before extending production.（由 A13/A14 實作與驗證完成；此區保留舊版歷史。）
- [x] Generate and inspect image 7 candidates v04–v09; verify isolated desktop/mobile prototype. v09 scores 86, needs revision; production is not complete.
- [x] Resolve concurrent topic/asset edits before changing active references; preserve the other workflow's chapter updates.（由 A13/A14 實作與驗證完成；此區保留舊版歷史。）
- [x] Finish remaining authorized visuals, integrate page references, validate desktop/mobile and rescore with rubric v1.0.（由 A13/A14 實作與驗證完成；此區保留舊版歷史。）
- [?] User review remains pending; current active v02 is needs revision.

## AnomalyDINO user visual recalibration (2026-09-05)

- [x] Accept the user's eight image rescoring values (78, 68, 66, 79, 80, 72, 60, 84) and supersede the inflated 91–94 image scores.
- [x] Record the scoring failure and add RULE-012 image-only visual sufficiency gates to the shared rubric and both teaching guides.
- [x] Redesign and regenerate the eight AnomalyDINO visuals only when production is requested; current v02 status is needs revision.（由 A13/A14 實作與驗證完成；此區保留舊版歷史。）

## AnomalyDINO independent rereview (2026-09-05)

- [x] Review the complete active v02 across eight rendered figures, desktop/mobile evidence, 25 mobile steps, arithmetic and the authors' paper; fixed-rubric result 94/100, no veto.
- [?] Historical A04 review is superseded by the user's visual calibration; no approval is recorded.

## Actual regeneration cycle v11 (2026-09-05)

- [x] Independently re-review the complete active v11 with current rendered evidence and the primary paper; fixed-rubric result 94/100, no veto, real-inference/common-benchmark evidence remains absent, user approval not inferred.
- [x] Strengthen skill's mandatory regeneration and combined-request semantics; record EAD-005 before production.
- [x] Regenerate efficiency explanation and tradeoff scenarios as v11; provide opt-in five-step mobile case while preserving full diagram. Correct cropped arrow remnants after visual inspection.
- [x] Inspect, test, score and rebuild active v11. Page 93, images 92–94, mobile views 94; evidence in EAD-005. HTML, 3 new mobile tests, 5 ResNet, 3 navigation and 1 bundle pass; real-inference gap remains explicit.

## Reusable teaching-review-cycle skill (2026-09-05)

- [x] Capture latest critique as shared RULE-010: efficiency explanation, meaningful tradeoffs, representative real evidence and mobile cognitive burden.
- [x] Create personal teaching-review-cycle skill with fixed-rubric loop, shared memory routing, intent boundaries and truthful completion conditions.
- [x] Pass skill-creator quick_validate plus reference/YAML/default-prompt/UI-length and rubric-total checks; record delivery. Manual intent-path review completed; no independent runtime teaching cycle claimed.
- [x] Execute authorized next iteration in EAD-005: efficiency explanation, scenario tradeoffs and mobile chapter-6 segmentation delivered as v11; trustworthy real-output evidence remains a limitation.

## Core mechanism and continuous case v09 (2026-09-05)

- [x] Independently re-review the user's revised v10 across all eight rendered figures, focused desktop/mobile evidence, chapter copy, numeric trace and primary-paper positioning; record remaining efficiency-story and real-output evidence gaps without claiming user approval.
- [x] Record RULE-009 in shared Markdown before regeneration; retain eight chapters and fixed rubric weights.
- [x] Regenerate cooperation, traceable numeric case and conditional comparison as v09→v10; add decisions at useful points. Preserve eight chapters.
- [x] Inspect all eight actual images and desktop/mobile page; verify numerical case, chapter 3/6/7 figures and answer reveals; rebuild bundle. Fixed rubric page 93, individual images 92–94; detailed limits in EAD-004.
- [?] User review remains pending.

## EfficientAD workplace iteration (2026-09-05)

- [x] Re-review the complete eight-chapter EfficientAD lesson after the user clarified that `slide=5` was only the current URL position; record the remaining model-mechanism, real-evidence and active-learning gaps. No lesson edit or user approval is implied.
- [x] Create independent shared scoring rubric v1.0, regenerate all eight chapters and images as v07, inspect and score actual outputs in EAD-003.
- [x] Regenerate the concrete visual corrections as v08; inspect all eight final images and desktop/mobile page under unchanged v1.0. Page 92; each image 92–94; no identified veto. EAD-003 records all subscores and limitations.
- [x] Rebuild local bundle (1,177 assets); HTML verifier, 3 navigation tests, 1 bundle test and 1 zoom-edge test pass; capture evidence in root tmp/efficientad-redesign-20260905/workplace-v08.
- [?] User review of the complete workplace revision remains pending.

## Reusable teaching webpage guidance (2026-09-05)

- [x] Record the user's audience: practical model understanding, workplace application and model tradeoffs; update both guides and shared AUDIENCE-001 review entry.
- [x] Reassess and rewrite the full EfficientAD lesson against workplace transfer and cross-model choice through EAD-003 v07→v08; older scores remain historical.

- [x] Establish one root TEACHING_REVIEW_LOG.md for all topics and link both guides to the autonomous generate/review/learn/regenerate workflow.
- [x] Record strict >90/100 gates for the webpage and every active teaching image, fixed scoring criteria, evidence requirements, and separate self-review/user-approval states.
- [x] Complete EfficientAD EAD-001: eight v05 SVGs and authored chapters, two image/content rounds plus mobile zoom correction; page 93/100 and individual images 92–94/100 after actual inspection.
- [x] Verify desktop/mobile navigation, self-check, zoom edges and close; pass HTML verification and 10 focused/regression tests; rebuild the local docs bundle.
- [x] Record the user's rejection of formula-led chapter 6; replace its main visual with workpiece/heatmap comparison v06, move formulas to advanced concept text, and update RULE-007 in both shared guides.
- [x] Verify chapter 6 SVG and desktop/mobile rendering, self-check, HTML and bundle.
- [?] Await user review of v06 chapter 6; v05 scores are historical and are not user approval.

- [x] Read IMAGE_STYLE_GUIDE.md and prior teaching review evidence; create ../../TEACHING_WEBPAGE_GUIDE.md with cross-topic improvement principles, authoring brief, review prompt, and proposed rubric.
- [?] Await user review of the proposed guidance; no lesson redesign or image generation performed in this task.

This is the active checklist for the beginner-first visual redesign. `[x]`
means implemented and validated; `[?]` means waiting for user review.

## Active state: v01 baseline restored (2026-08-18)

- [x] Restore all 291 active beginner-path references to the preserved v01
  inventory in `_course_content/audit/beginner-visual-redesign-review.json`.
- [x] Rebuild the offline HTML and verify the active v01 baseline.
- [x] Pass the v01 baseline mapping/readability regression gates and the full
  suite: 393 passed / 3,997 subtests passed.
- [x] Keep Ref process v03 assets on disk as inactive recovery material; do not
  delete or present them as the active lesson.
- [x] Publish the current interactive course as a GitHub Pages-ready `docs/`
  bundle and push the initial `main` commit to `hctsaik/visionAI_Model_Introduce`.
- [ ] Enable GitHub Pages in the repository settings: deploy from `main` and
  `/docs`; this requires the repository owner's GitHub web/API session.
- [?] Any future visual redesign needs a separate user-approved scope.

## SegFormer introduction review (2026-08-20)

- [x] Inspect the published SegFormer lesson, authored topic content, five
  beginner-path visuals, four retained engineering-reference slides, model.md,
  manifest, and QA record.
- [x] Verify the technical review against the SegFormer paper, official NVIDIA
  implementation, and current Hugging Face model documentation.
- [x] Record the main finding: the lesson is strong on engineering contracts
  and misuse boundaries, but it does not yet provide a complete model-first
  explanation of MiT internals, positional-encoding-free Mix-FFN, sequence-
  reduction attention, B0-B5 tradeoffs, training/inference separation, or
  paper evidence.
- [x] Record the presentation finding: retained engineering-reference slides
  contain clipped headline/footer text and substantially duplicate the active
  beginner path; their historical `approved` labels are not user approval.
- [x] Receive user agreement to implement the SegFormer-specific redesign.
- [x] Author an eight-chapter `deep_dive` contract covering task/output,
  input contract, four-stage shapes, MiT internals, MLP decoder, training vs.
  inference, B0-B5 evidence, and comparison/HOLD decisions.
- [x] Generate seven deterministic 1672x941 SVGs and reuse the existing
  contract visual for chapter 02; add primary-source links and the durable
  `SEGFORMER_MODEL_CONCEPT.md` reference.
- [x] Add real `slide=1..8` navigation, sticky chapter controls, keyboard
  traversal, mobile horizontal image reading, and remove the four clipped
  legacy PNGs from the rendered SegFormer lesson.
- [x] Rebuild `interactive-learning.html` and the GitHub Pages `docs/` bundle;
  verify 58 topics, 559 instructional images, and the deployed concept file.
- [x] Pass focused SVG/runtime tests, desktop/mobile visual QA, and the full
  regression suite: 398 tests passed.
- [?] Await the user's final semantic and visual review of the implemented
  eight-chapter page; implementation/test completion is not user approval.

## ResNet full-page regeneration (2026-08-31)

- [x] Receive user approval to rewrite the ResNet lesson and regenerate its
  explanatory imagery using `IMAGE_STYLE_GUIDE.md` as the governing example.
- [x] Inspect the active ResNet topic, model bridge, five beginner visuals,
  four concept visuals, renderer, shared deep-dive contract, and validation
  patterns.
- [x] Define an eight-chapter scope: task/output, residual addition,
  stage/shape variants, training vs inference and BatchNorm, global pooling
  observability, calibration/OOD review, depth/cost evidence, and fair model
  selection.
- [x] Generate a new text-free AOI workpiece anchor with built-in ImageGen and
  record the exact prompt intent and saved project path.
- [x] Author the ResNet model concept, eight source-backed chapter records,
  and eight full-canvas Style-Guide-conformant mechanism visuals.
- [x] Rebuild the offline lesson and GitHub Pages bundle without changing the
  other 57 topic contracts.
- [x] Pass focused ResNet contract, SVG readability, browser layout, HTML,
  bundle, and relevant regression gates.
- [?] Await explicit user semantic and visual approval after implementation;
  implementation and automated tests alone are not user approval.

The older Ref process v03 checklist below is retained only as a historical
implementation record and must not be interpreted as the current site state.

## Historical Ref process v03 record

- [x] Apply the Ref process v03 first-read shell to all 58 teaching topics.
- [x] Migrate all 291 beginner-path visuals and rebuild the offline HTML.
- [x] Complete the site-wide implementation and automated validation. Human
  review remains a separate approval record and has not been fabricated.
- [x] Batch-audit all topic families for the same clarity failure: missing
  input → mechanism → output → engineering-action causality.
- [x] Batch-fix the shared renderer and family-specific story copy so all 291
  visuals use the same Ref reading standard without pretending every model has
  the same output responsibility.

## Site-wide migration

- [x] Deterministic migration script: `tools/migrate_all_beginner_visuals.py`.
- [x] Every topic has a 1672x941 first-read PNG plus v02 SVG companion/source.
- [x] Every SVG has five numbered reading stages, causal arrows, mechanism copy,
  review boundary, and a takeaway; topic-specific evidence footers are kept
  for anomaly, diffusion, geometry, classification, segmentation, detection,
  and temporal/video families.
- [x] Preserve the existing raster work example as the evidence anchor where
  available; do not invent model results in the teaching shell.
- [x] Update all topic JSON references and the 291-job master manifest.
- [x] Rebuild `interactive-learning.html` with 58 topics / 232 topic images,
  291 image-led first-read visuals, and 551 total instructional images.

## Validation

- [x] HTML verification and offline/no-fetch checks.
- [x] SVG readability audit: 58 reviewed, 0 topics with text below 18px.
- [x] Image-led migration audit: 58/58 candidates migrated, 0 replacements
  required; shared visible assets also pass.
- [x] Desktop/mobile runtime QA for all 58 topics.
- [x] Site-wide migration contract tests: 13 focused tests passed.
- [x] Representative visual review across anomaly, foundation/VLM,
  diffusion, geometry, and temporal/video categories.
- [x] Beginner-copy pass removed dense English jargon from the rendered
  first-read surface while preserving source-topic engineering vocabulary.
- [x] Final automated redesign audit: 291 KEEP, 0 PARTIAL, 0 REDO.
- [x] Ref process clarity audit: 58 topics / 291 visuals PASS, including
  family-specific semantic terms and no inherited YOLO badge.
- [x] Browser runtime audit after the redesign: 58 topics PASS at desktop and
  mobile widths, with no SVG text outside the 16:9 canvas.
- [x] Full regression suite after the Ref migration: 394 tests passed and
  3,997 subtests passed.
- [?] Human semantic/visual approval is still unrecorded; no topic is claimed
  as user-approved until the user reviews it.

## Parallel generation records

- [x] Foundation wave 1: `dinov2`, `dinov3`, `clip`, and `siglip`; 4/4
  built-in image-generation lanes succeeded and were integrated.
- [x] Foundation wave 2: `qwen-vl`, `llava`, `gemini-vision`, and
  `ad-anomalyclip`; 4/4 lanes succeeded and were integrated.
- [x] Anomaly wave 4: `ad-winclip`, `ad-anomalygpt`, `ad-diffad`, and
  `ad-subspacead`; 4/4 lanes succeeded and were integrated.
- [x] Record each source output, target path, attempt count, and prompt in
  the dated manifests under `_course_content/audit/`.
- [x] Make reruns resumable: prefer `_v02` anchors and preserve the
  user-confirmed YOLO Dense specialized storyboard during generic migration.
- [?] Keep all generated batches pending user visual/semantic approval until
  the user explicitly accepts them.

## Review rule

Do not mark a topic user-approved merely because its renderer, audit, or
runtime test passes. The current batch is implementation-complete and
validation-complete; user approval remains a separate, explicit state.

## Latest user review: DINOv2 / DINOv3 and attached references (2026-08-18)

- [ ] Copy the four user-attached reference images into `C:\code\claude\visionAI\ref`.
  The workspace `ref` directory is currently empty, and the chat attachments
  are not exposed as local source files in this environment.
- [x] Inspect the current DINOv2 and DINOv3 topic copy and first-read renders.
- [x] Record the clarity finding: the current material explains feature
  contracts and validation boundaries, but does not lead with the concrete
  Good/Bad group → same patch position → group comparison → patch score map →
  heatmap → process action story shown in the user references.
- [x] Redesign the DINOv2/DINOv3 visual sequence in the Ref process style;
  keep the model-output boundary explicit because a patch heatmap is a
  downstream application, not an automatic DINO output.
- [x] Add a complete DINOv2 Markdown explanation covering self-supervised
  Teacher/Student learning, ViT inference outputs, Good/Bad patch analysis,
  downstream ownership, model-family boundaries, and engineering limits.
- [x] Re-review the DINOv2 interactive lesson against that explanation and
  update its first-read summary plus expandable source copy; rebuild and
  validate the offline HTML.
- [ ] Copy the exact four user-attached source files into `C:\code\claude\visionAI\ref`
  when the attachments are available as local files; the current directory is
  still empty, so no substitute files are claimed as the originals.

## Local website startup (2026-09-05)

- [x] Start the existing interactive course on localhost port 8000 and verify HTTP 200.
- [x] Restart the local server on user request; verify HTTP 200 again. Automatic browser launch was blocked by execution policy; provide the clickable URL.

## EfficientAD teaching review (2026-09-05)

- [x] Review lesson source, model notes, one retained reference PNG, and primary paper/code; record provisional teaching score (60/100).
- [ ] Verify rendered desktop/mobile lesson when browser connection is available. No redesign requested or approved.

## Authorized standalone browser verification (2026-09-05)

- [x] Use explicitly user-authorized standalone Playwright to open the EfficientAD lesson and inspect its desktop screenshot. Full desktop/mobile lesson audit remains pending.

## EfficientAD rendered lesson reassessment (2026-09-05)

- [x] Inspect actual desktop first-read text, five rendered figures, and expanded text using authorized Playwright; replace provisional source-only score with reviewer score 62/100.
- [ ] Correct same-workpiece visual discontinuity, generic heading mismatch, imprecise P95 definition, and missing mechanism walkthrough if implementation is requested. These findings are not user-approved changes.


## AnomalyDINO review cycle A01（2026-09-05）
- [x] 保存基線；核對原論文與作者程式；將共用學習 RULE-011 寫回根目錄指南與共用紀錄。
- [x] 重製 AnomalyDINO 八章、逐圖與手機閱讀（v01→v02）。
- [x] 完成 v02 技術與介面驗證；原網頁93／各圖91–94的達標結論已由 A04 撤回，不能作目前完成依據。
- [x] 使用者審閱：明確指出圖片分數過高；A04 已重評並寫回學習，未獲核准。
- [x] A06已完成：依 A04 重製視覺：優先第7張模型工作流程比較、第3張最近鄰、第2張固定模型；先選參考母版、完成單張原型再展開。
- [x] A06新成圖逐張評分與完整網頁重評，實際接入八章；自評達標，待使用者審閱。
- [x] A05：完整記錄高估事件的學習；新增共用RULE-012，更新teaching-review-cycle影像產生／檢討／學習／重製流程。

## A06 實際製作完成
- [x] 七張ImageGen新示意＋作者原像素第八圖，接入頁面與本機bundle。
- [x] 評分→記錄原因→定向重製／改構圖→手機與桌面验证；學習同步共用Markdown與skill。
- [ ] 使用者審閱v03；自評93／圖片91–94不代表核准。

## A08 目前版本缺點審查（2026-09-05）
- [x] 確認正式topic為A06/v03資產組；實看八張成圖及代表手機截圖，核對主線、論文與第一眼資訊負擔，缺點記錄於唯一共用log A08。
- [x] 重開視覺狀態為需簡化：圖7負擔非常高、圖4高，圖2/3/6中高；手機分段改善字體大小但未自動降低概念數。
- [ ] 修正圖2整圖／局部特徵流程、拆分圖4分數與定位、圖3/4案例連續性、圖7同條件比較與手機上下文；圖6改為一次一個反例，補查作者正常／失敗例。
- [ ] 修正後依v1.0正式逐項重評；A06歷史高分不再作全面達標依據，使用者未核准。

## A09 製作與驗證收尾（不代表視覺全面達標）
- [x] 保存基線、實看母版、先寫回學習並修復編碼。
- [x] 第7張ImageGen原型與定向修正，另生成清楚的正常參考工件。
- [x] 製作16組桌面／手機視圖，接入第2/3/4/6/7/8章與教材Markdown。
- [x] 修正裁切越界／殘字、存庫語意、算術來源對應、手機重疊及中文按鈕。
- [x] 完成13項回歸測試／14子測試，最後3項聚焦與bundle檢查／8子測試；32個頁面視圖無JS錯誤。
- [x] HTML驗證通過；本機docs bundle共1212資產；32張A09資產SHA與bundle一致。
- [ ] 整頁及所有視圖嚴格>90：仍未通過，沿用A11校準與A10後續修正，不能以本輪工具通過結案。
- [?] 使用者審閱，未核准；未外部部署。

### 2026-09-05 即時版本核對（取代先前「尚未整合」摘要）
詢問是否上線時重新核對：正式 ad-anomalydino.json 已引用 A09；teaching-images/vision-ai-model-selection/interactive-learning.html 已包含 anomalydino-02-store_a09.svg，修改時間為 21:10:24；http://127.0.0.1:8000/interactive-learning.html 實際 HTTP 回應也包含該 A09 引用。因此本機頁面已更新；外網部署、本輪完整驗證及使用者核准尚未確認。先前未整合紀錄已落後於磁碟，不能再當目前狀態。下一步核對完整 A09 驗證證據與 bundle／外網狀態，再決定剩餘工作；不要重複整合。此次只確認回應文字含新版引用，未宣稱瀏覽器視覺驗收通過。

- P03 checkpoint：第7章原型已檢查，第2章實際CNN特徵已保存；進入其餘資產產生與正式整合驗證，尚未評分／核准。


## PaDiM R01 review started (2026-09-06)

User switched to reviewing ad-padim. Scope: review current page and five beginner visuals plus four supporting visuals; no production requested for this topic. Next: capture actual desktop/mobile page and assets, inspect, score with rubric v1.0, save findings. Evidence directory: tmp/padim-review-20260906. Browser connection unavailable; use previously authorized standalone Edge. Scores pending.


ResNet E01 checkpoint: baseline eight images inspected; chapter2 overlap, chapter3 shape-only, chapter5 untraceable grid and chapter7/8 list-only comparison accepted for repair. Brief: tmp/eight-topics-20260906/resnet/brief.md. Real CPU ResNet50 residual data saved to e01-data/activations.json; exact tensor addition error 0. Prototype generated, visual review pending; not complete or user-approved.


## WI-007 checkpoint：ResNet E01整合；分類組繼續（2026-09-06）

ResNet八章已實際重製為16張桌面／手機SVG，正式topic及本機HTML已啟用。5項ResNet既有回歸通過；16個桌面／手機章節導航、專用手機圖、放大Escape、自測與頁面無溢出通過。證據tmp/eight-topics-20260906/resnet/final/report.json，逐圖hash及邊界在final-assets/assets.json。尚未外部部署或使用者核准。

原型先挑最大残差卻全歸零，未放行；改成同通道同位置的正負修正後才展開。SVG裁切補explicit clipPath，避免方形框露出原crop以外的設備。第3章手機上下標籤曾碰撞，已修。BatchNorm只示中心化，不以假標準差冒充完整正規化。圖上假設分數不是真實工件分類。

目前自評尚未定稿：第8章三模型機制仍較概括，列入分類組回查，不能宣稱全題已達標。下一步在ConvNeXt/ViT展開來源局部與操作差異，再回填ResNet比較。全八題WI-007仍執行中，沒有縮成只做ResNet。

ConvNeXt基準五圖及桌面手機已截圖並實看：切片圖只用方格代替被切的訊號；depthwise/channel mixing仍靠格子長條；主頁通用文案與主題重點不一致，手機仍橫向920px。需改成同一來源實際裁片與兩種混合方向。將擴充既有beginner path的可選reading_views，沿用已驗證deep-dive手機元件與安全驗證；不強迫每題加成八章。

維護程式：tools/teaching_e01_canvas.py、extract_resnet_e01.py、render_resnet_e01.py。資料generated-concepts/resnet/e01-data/activations.json，生成模式code-native SVG+原圖像素+本機CPU特徵。記憶與下一項在WORKITEMS、BEGINNER_VISUAL_TODO/STATUS與共用TEACHING_REVIEW_LOG，原始基準可恢复。


## WI-007 最新接續：ViT製作中；分类組比較仍待完成

- ResNet E01：8章16圖、正式HTML已整合；5項回歸及16桌面手機章節QA通過。第8章比較尚需分類組回填，未評為完成。
- ConvNeXt E01：5段6視圖、12桌面手機資產（首圖由原生SVG忠實轉PNG）；已整合。實圖全看、HTML verifier、新增2項回歸及10頁面狀態/6視圖放大通過。手機實寬由278增至>=340px，已實看新頁。仍需三模型共同對照，不冒稱整題達標。
- ViT：baseline五圖與桌面手機已保存並實看；brief在tmp/eight-topics-20260906/vit-classifier/brief.md。開始CPU ViT-B/16中間輸出擷取，來源V-01及供群組比較的R-01。原型尚未畫、尚未改正式topic。
- 重要學習：patch token是多維向量，不是平均成一個數，不能因token數少就斷言細節一定消失。改解析度的成本例固定P16；不假設現有checkpoint可隨便改patch大小。
- 共用UI已加入beginner可選reading_views；首圖PNG約束、安全路徑及crop驗證保留，僅opt-in使用作者文案及手機圖，legacy保持原流程。工具tools/build_interactive_learning_html.py、verify_interactive_learning_html.py；回歸tests/test_beginner_focused_views.py。
- 接續先完成ViT prototype→全題→分類組三模型比較與回查→固定量表逐圖及頁面評分，再做U-Net、SegFormer、YOLO-Seg、Keypoint R-CNN、Pose。全八題未完成，不要在此checkpoint停工。
- 沒有外部部署、真人學習證據或使用者核准。最新QA證據tmp/eight-topics-20260906/{resnet,convnext}/final/report.json；精確資產hash在各final-assets/assets.json。
ViT原型尚缺實際加權結果，已記錄學習並補擷取；下一步修原型後全題。
WI-007分類組回查：同R-01共用四個實際操作視圖已接入ResNet8、ConvNeXt5、ViT5。發現R-01和V-01縱橫比不同時，外部框需跟隨圖片meet的留白；已修正attention來源標框。測試完成不代替逐圖教學評分，評分仍待最終校準。下一步U-Net用局部斷口與多尺度合併取代符號U形圖，全部八題仍執行。
U-Net：開始原型第3圖；五段皆待重製驗證，未完成。
U-Net已重製整合，QA與分組評分待收尾；SegFormer八章開始原型。
SegFormer已重製整合，分組回查/評分待收尾；YOLO-Seg原型第3圖開始。


## WI-007 checkpoint：六題已整合，開始關鍵點組

ResNet、ConvNeXt、ViT、U-Net、SegFormer、YOLO-Seg的E01已啟用本機HTML。分類比較已加入同R-01實際運算。U-Net10、SegFormer16、YOLO-Seg10桌面手機頁面QA通過；工具結果不是視覺評分。YOLO-Seg原背景B框改回原始PCB兩個真元件，桌面第2圖底部裁字已縮短修正；模式原像素＋原生SVG人工mask／可追算基底，首PNG忠實轉圖，保存於各generated-concepts/{topic}/*e01*。

Keypoint R-CNN基準五图已實看，框與角點漂到背景的缺陷採納；brief在tmp/eight-topics-20260906/keypoint-r-cnn/brief.md。下一步同金色元件四熱圖原型→回映／遮擋→Pose→分組回查與固定量表校準→共用回歸與bundle。全八題仍執行，未最終評分、未外部部署、未使用者核准。


## WI-007：八題E01已重製整合，進入最終審查

Keypoint R-CNN五段六視圖完成原像素近角、每點熱圖、2×2取樣、回映偏移與遮擋修正；10頁面狀態QA通過。Pose六段完成同PCB分組、G-01已知幾何、縮图内參、實際PnP、外圍檢查與交付。來源、意圖在tmp/eight-topics-20260906/{keypoint-r-cnn,pose}/brief.md；原生SVG及手機專圖保存在generated-concepts/{topic}/*e01*，首圖為忠實PNG輸出，非生成模型推論。

學習：Pose第一版底部文字在桌面碰撞、分組前後不夠可見，已修排版並加每件連線；外圍檢查點原先與擬合角點重合，已改為未參與擬合的(55,35,0)mm再重算，不冒稱獨立檢查。最終受控例分散/集中RMSE0.31/0.34px，外圍0.49/8.35px，只支持此設定。原型局部殘差150倍顯示，外圍差異6倍顯示，均明示倍率。

三組已回填前題：分類用同R-01實測操作；分割用已標示各自案例的融合/共享基底；關鍵點組用2D→幾何角色對照。下一步完整逐圖分項評分、最後頁面與手機實看、共享回歸、HTML/docs bundle及hash核對。仍未宣稱全題達標、外部發布或使用者核准。


## WI-007 E01 最終交付（2026-09-06）

八主題 ResNet、ConvNeXt、ViT、U-Net、SegFormer、YOLO-Seg、Keypoint R-CNN、Pose Pipeline 已完成審查→Markdown學習→實際重製→正式整合→驗證；三組已回查前題。本段取代先前「製作中／最終檢查待完成」checkpoint，使用者尚未核准。

- 產物：49組桌面／手機圖，共98個唯一啟用資產；正式topic與本機HTML、docs網站包同步。生成模式為原始像素搭配原生SVG、實際CPU模型張量或明示的概念／合成幾何；沒有把示意當實際模型預測。生成意圖、來源與保存路徑見本檔各題紀錄、course tools內E01 renderer/extractor、各題generated-concepts manifest。
- 固定量表v1.0整頁自評：ResNet 93、ConvNeXt 93、ViT 92、U-Net 94、SegFormer 92、YOLO-Seg 93、Keypoint R-CNN 92、Pose 93；最低單圖91。逐圖分項、扣分與證據在共用TEACHING_REVIEW_LOG.md及course e01-eight-topic-review.json。這是自評，沒有真人學習驗收證據。
- 驗證：20項pytest測試＋18個子測試通過；94個桌面／手機章節狀態、切換／放大／答案展開检查通過。數值獨立核對通過。最終docs verifier通過，1305個包內資產存在，98個啟用資產hash一致；本機HTTP 200且HTML與docs一致。證據：tmp/eight-topics-20260906下各題final/report.json、final-assets/assets.json、numeric-audit.json、delivery-audit.json。
- 本機入口：http://127.0.0.1:8000/interactive-learning.html?rev=eight-e01-final#view=lesson&lesson=resnet&slide=1 。未執行外部部署。
- 已回用的學習：特徵與實際來源局部對應；保留剩餘貢獻而不只挑好看的通道；concat畫成分開的特徵平面；ROI裁圖須核對縮放與留白偏移；2D／3D座標分清；獨立驗證點不得參與擬合；手機需逐張實看。規則已更新IMAGE_STYLE_GUIDE.md與TEACHING_WEBPAGE_GUIDE.md，並用於後續題和前題回查。
- 下一步：待使用者審閱這八題；有新回饋時按具體缺口重開，沿用既有授權，不能只寫學習紀錄而不修改成品。不要重做本輪已驗證產物。PaDiM評論暫停、PatchCore P04待改進屬既有其他項目，不因本輪八題完成而宣稱已結案。


E02：動機／跳接原型、4個新SVG、前兩章主線與自測、16頁面狀態及必要回歸完成。證據resnet-e02-review.json；使用者審閱仍未核准。

E02最後驗證：HTML verifier PASS（58主題、HTML解析與離線內嵌資料通過）；本機bundle 1309資產。4新圖與HTML經hash核對和HTTP確認，未外部部署。
# WI-013 continuous cycle: R03 failed Sol re-review (2026-09-06)

- [x] Sol inspected actual R03 desktop/mobile PNG plus SVG/manifest.
- [x] Sol scored desktop 25/100 and mobile 18/100 with fixed rubric.
- [ ] Replace Qt raster path with browser/Playwright and a verified CJK font; wait for `document.fonts.ready` and check `document.fonts.check`.
- [ ] Generate and detector-verify a real `cv2.aruco.CharucoBoard` with named dictionary; retain IDs as evidence.
- [ ] Make counterfactual visible; map P95/coverage to named pose/grid/sample evidence or remove unsupported numbers.
- [ ] Re-render and inspect desktop plus true 390px mobile; pass readable text/no overflow before Sol re-review.
- [ ] Do not integrate into formal topic or batch-expand until prototype passes; user acceptance remains separate.
# WI-013 R05 next cycle after R04 HOLD (2026-09-06)

- [x] Sol re-reviewed R04 actual desktop/mobile PNGs: 78/100 and 73/100 HOLD.
- [ ] Use renderer-safe `q ↔ P` (or `image point q / board point P`) everywhere; remove `qq/PP` corruption.
- [ ] Add callouts from m17, m23, and c17 labels to the actual board locations.
- [ ] Remove desktop detector truncation and wrap mobile takeaway with 30px side padding.
- [ ] Add R05 manifest with PNG/SVG hashes and board/font evidence.
- [ ] Sol re-review actual R05 PNGs before formal topic integration; user acceptance stays separate.
# WI-013 R06 after failed R05 mixed render (2026-09-06)

- [x] Sol inspected R05 PNGs: desktop 79/100 fail; mobile 72/100 fail.
- [ ] Rebuild from actual R05 source; set visible version to R06 in both outputs.
- [ ] Globally remove `qq/PP`, `q/P P`, and `q17q/PP17`.
- [ ] Add physical m17/m23/c17 board callouts.
- [ ] Fix desktop evidence wrapping and mobile takeaway crop.
- [ ] Add R06 manifest, inspect both PNGs, then Sol re-review.
# WI-013 R07 final layout pass after R06 HOLD (2026-09-06)

- [x] Sol re-reviewed R06: desktop 85/100 HOLD; mobile 86/100 HOLD.
- [ ] Move/shorten desktop board provenance caption.
- [ ] Raise c17 detector evidence and preserve one line-height bottom padding.
- [ ] Optionally increase mobile third-zone line spacing without crop.
- [ ] Re-render, inspect actual PNGs, update manifest hashes, and obtain Sol >90 re-review.
# WI-013 post-R07 controlled integration (2026-09-06)

- [x] Sol reviewed actual R07 PNGs: desktop 92/100, mobile 92/100; prototype pass.
- [ ] Stage R07 as a versioned formal-topic integration candidate without deleting prior revisions.
- [ ] Sol re-open actual integrated page/assets and verify version, hashes, image visibility, and mobile layout.
- [ ] Record formal-topic technical validation, Sol review pass, and user acceptance as separate states.
# WI-013 R08 integration geometry fix (2026-09-06)

- [x] Sol checked candidate hashes/references; integration failed on mobile geometry contract.
- [ ] Make candidate mobile conform to 1672x941 page contract or provide an explicitly compatible candidate wrapper.
- [ ] Add machine-checkable geometry contract and static mapping check.
- [ ] Sol recheck candidate; live browser remains unverified if unavailable.

# WI-013 R09 packet/asset consistency fix (2026-09-06)

- [x] Create exact authoritative packet at `tmp/charuco-r09/integration-packet.json` plus identical compatibility copy at `tmp/charuco-r08/integration-packet.json`, without changing formal topic or R02-R08.
- [x] Point candidate `quality_status.current_mobile_asset` and reading view to the actual R07 mobile PNG.
- [x] Add desktop PNG path, 1600x1080 intrinsic dimensions, SHA256, and recomputed candidate/contract/packet hashes.
- [x] Run static consistency validation; browser page remains unavailable and is not claimed as validated.
- [ ] Sol performs candidate integration recheck; formal topic and user acceptance remain separate.

# WI-013 R10 cleanup (2026-09-06)

- [x] Remove stale R08 labels from R09 generated page, wrapper, and candidate review metadata.
- [x] Change geometry rollback to authoritative R09 candidate with explicit R08 compatibility packet paths.
- [x] Recompute packet, candidate, contract, and static-evidence hashes; run the final static integration gate.
- [ ] Sol performs final static integration recheck; browser runtime and user acceptance remain separate.
# WI-013 R10 static integration complete (2026-09-06)

- [x] Sol static integration pass: R09 packet/refs/hashes/rollback consistent after R10 cleanup.
- [x] Preserve formal topic and prior revisions; no user acceptance claim.
- [ ] If a browser becomes available, perform live candidate page desktop/mobile runtime check.
# WI-013 full ChArUco redesign after style re-review (2026-09-06)

- [x] Sol inspected all five formal beginner visuals and rescored chapter 67/100.
- [x] Luna prototype visual 1: D comparison, why combine chessboard + ArUco; R11 candidate is pending Sol review.
- [x] R12 correct visual 1 comparison with three distinct physical boards and same camera/occlusion condition; pending Sol review.
- [ ] Luna prototype visual 2: C path, q17/P17 → PnP → predicted c17/residual.
- [ ] Luna prototype visual 3: center-only vs full-FOV multi-pose HOLD.
- [ ] Luna prototype visual 4: calibration setup vs daily ROI route boundary.
- [ ] Convert formal beginner path from five visuals to exactly four only after prototype Sol pass.
- [ ] Produce readable desktop/mobile assets and re-score each >90 before promotion.
# WI-013 R12 first-image technical correction (2026-09-06)

- [x] Sol reviewed R11 actual desktop/mobile PNGs: 81/77, style improved but technical comparison failed.
- [x] Replace reused-board comparison with true board variants or explicit ablation label.
- [x] Correct ArUco explanation: marker corners exist; identity/corner-density/precision trade-off must be shown.
- [x] Recheck R12 actual PNGs before starting visuals 2–4.
- [x] Luna R13: fix R12 header contradiction, unsafe ArUco corner wording, missing combine arrow, and 360px readability; obtain Sol >90 desktop/mobile before advancing.

# WI-013 R13 visual 1 candidate (2026-09-06)

- [x] Replace contradictory header with same camera/perspective/occlusion condition plus three target types.
- [x] Replace unsafe ArUco corner-count wording with marker ID/local recognition and marker-corner localization-precision wording.
- [x] Add thick arrows from chessboard corner precision and local marker ID into the ChArUco merge panel.
- [x] Reduce mobile copy to one advantage and one limitation per lane; inspect 720px and 360px-equivalent outputs.
- [x] Preserve three distinct board assets, m17/m23/c17 callouts, yellow takeaway, R02-R12, formal topic, and visuals 2-4.
- [x] Sol re-open candidate and score desktop/mobile: 96/94, visual 1 prototype technical pass; no user acceptance or formal promotion.

# WI-013 after R13 visual 1 Sol pass (2026-09-06)

- [ ] Clean `board-evidence.json` stale `fewer corner samples` wording and recompute evidence/manifest hashes; PNG rerender is not required if pixels stay unchanged.
- [ ] Build visual 2 as a C-type single path using the same camera/board and continuing m17/m23/c17 through q17/P17, PnP, predicted c17, and residual.
- [ ] Inspect visual 2 actual desktop/mobile PNGs and score each >90 before starting formal integration.
- [ ] Keep visual 1 prototype pass, full-chapter pass, formal integration, and user acceptance as separate states.

## WI-019 — 13 課公開頁重審
- [x] 讀技能、規範與 F01 歷史範圍。
- [x] 保存公開版本、逐課圖片槽與主線；公開 HTML 與 docs hash 一致。
- [x] 實看 65 張桌面首讀圖與 26 張手機前兩圖；130 次放大／Escape、26 組解答與導航。手機 13 張首圖放大另等完整載入通過。
- [x] 核對必要核心技術主張來源，逐課提出重建程度與驗收方式；WinCLIP+ 精確匹配說法保留待公式核對。
- [x] 寫回共用 log／指南學習、STATUS 與 WORKITEMS；審查完成，可交付判斷。
- 未評估：隱藏正式 slide 圖、手機後續全部橫向區域、整課總分與真人學習效果；不當作本輪已驗收。
- 後續建議（尚未製作）：先 AE 完整案例原型，優先修 RD4AD／AnomalyGPT 的呈現與角色矛盾，再按比較組擴展。
- 本輪未授權批量重製／發布，使用者核准另列。
## WI-021 — 實際重製 13 課（2026-09-09）
- [x] 接續 WI-019、讀有效規範與指定參考，建立 AE 原型 brief。
- [x] AE 單張桌面／手機原型生成、實看、修正與逐項評分。
- [x] AE 五張桌面＋五張手機圖接入本機教材，兩個入口／三種視窗互動檢查通過；全頁與其餘圖量表整理仍待完成。
- [x] AE、DRAEM 首讀圖文重製與案例連續性，本機整合及互動通過；逐圖量表／全頁自評整理仍待完成。
- [x] STFPM、RD4AD：同圖雙支路與反向特徵重建，本機接入及互動QA完成；全頁分數另列。
- [x] SubspaceAD：正常子空間、局部殘差與方法取捨，本機接入及QA完成。
- [x] UniAD、Dinomaly、InvAD：多產品案例與各自重建限制，本機接入及QA完成。
- [x] DiffusionAD、DDAD：恢復條件與分數來源差異，本機圖文接入及六狀態QA完成。
- [x] WinCLIP、AnomalyCLIP、AnomalyGPT：提示來源、定位與對話責任；圖文與六狀態QA完成。
- [x] 本機正式圖文整合、逐張桌面／手機檢查、必要回歸與完成紀錄。
- [x] 全13頁審讀、自評與發布包核對。
- [x] commit/push及公開網站核對：749401f，公開HTML及62PNG雜湊一致。
- 使用者成品核准 pending；不以製作授權或舊分數代替。

- WI-021 checkpoint：CLIP三課12張新PNG已生成及328px自評，整合/QA/13課全頁分數待執行，使用者核准pending。

## WI-021 本機實作與驗證完成／即將commit＋push
- 13課、43組邏輯圖槽、62張不同桌面/手機PNG正式引用；imagegen生成模式，非實測。原工程參考保留。
- 原78狀態/258圖互動PASS；最終26狀態/86圖解碼PASS、124本機HTTP hash PASS；1299引用資產逐檔一致、未引用0，bundle 1,029,718,818 bytes。
- 全13頁已實讀與逐项自評，詳workitems/wi-021/page-assessment.json；逐圖四份image-assessment檔。自評不是真人驗收，使用者核准pending。
- 回歸：ad_f01 4、navigation 3、tall_mobile 1、bundle 1、三張首讀邊界1 PASS。全站verifier既有charuco阻塞及anomalydino整檔4個舊斷言失敗保留，不宣稱全站通過。
- 發布包清除403個tracked未引用舊資產及24個未提交重複PNG，來源原檔保留。git diff --cached --check PASS。
- 下一步：commit、push、比較遠端HEAD與公開HTML/PNG；目前尚未發布。Git僅追蹤docs/README，本機記憶不宣稱已push。


## WI-021 已完成重製與發布（2026-09-09）
- 授權：使用者要求以skill重製13課；沿用commit＋push授權。實作、工具驗證與發布完成；使用者成品核准pending、真人學習測試未做。
- 產物：13課首讀圖文、43組邏輯圖槽、62張不同PNG（桌面31／手機31），imagegen實際生成並逐圖審看；原工程參考保留。示意圖不當作真實模型推論。
- 驗證：course/docs 78狀態與258次圖互動PASS；最終26狀態與86圖解碼PASS；124本機HTTP雜湊PASS。公開HTML與發布版一致，公開62PNG全部200且SHA256一致。
- 必要回歸PASS：ad_f01 4、navigation 3、tall_mobile 1、bundle 1、三圖首讀邊界1。全站charuco verifier阻塞與anomalydino整檔4個歷史斷言失敗未處理，不宣稱全站通過。
- 發布：commit `749401f96609279cd19c068b897a4edb17504476`；origin/main一致，worktree乾淨。GitHub Pages action 34283005280 completed/success；https://hctsaik.github.io/visionAI_Model_Introduce/
- 證據：workitems/wi-021/public-release-verification.json、release-audit.json、page-assessment.json、image-assessment-*.json、qa-*/；共用TEACHING_REVIEW_LOG.md。Git僅發布docs與README，根記憶和製作素材保留本機，未宣稱已push。
- 下一步：本輪已授權工作完成；若使用者給成品回饋，從此版本與上述證據接續。舊checkpoint保留為歷史，由本段取代。

## WI-028 本輪執行入口（2026-09-10）
- 八個時序題已明確授權製作，詳細 checklist 以 `workitems/wi-028/PLAN.md` 為準；下方 WI-028 歷史清單保留，兩入口已由 WI-029 完成。
- [ ] 完成八課圖文、驗證、學習及交付；目前基準與來源核對中，尚未生成／測試。

## WI-028 八課製作驗證完成、準備發布
- 36張PNG、八課圖文／反例／比較／自測與操作卡已整合，逐圖和整頁自評通過。來源、prompt、資產hash及分項證據：workitems/wi-028。
- 已驗證48頁面狀態、144次放大／Escape、自測／導覽，16最終閱讀狀態，72HTTP圖片hash，1292資產與HTML一致；聚焦測試7+4subtests及bundle1通過。
- 全站舊verifier仍報既有ChArUco inline schema錯誤，歷史有相同紀錄；不宣稱全站檢查全過。
- 下一步：保存維護快照、commit/push、公開HTML及36PNG核對。使用者核准pending。


## WI-028 完成紀錄 — 八個時序 Topic
- [x] Frame Difference、Background Subtraction、Lucas–Kanade、RAFT、ByteTrack、ConvLSTM、VideoMAE、V-JEPA 圖文已製作並公開。
- [x] 18個故事、36張桌機／手機PNG；每課核心、反例、比較、自測與操作卡；來源與生成提示、修正紀錄、逐圖及整頁分項自評均落盤。
- [x] 48頁面狀態／144次圖片放大Escape、自測導覽、16閱讀狀態、72本機HTTP圖片hash、1292引用資產及HTML一致；聚焦pytest 7 tests+4 subtests及bundle 1 test通過。
- [x] ca7254653d5f025617fff1885132063328adf67a 已推送；Pages run34494424414成功；公開HTML與36PNG hash符合成品。首次部署前舊HTML檢查失敗保留為歷史，完成後重查通過。
- 範圍確認：僅八課改動，其他50課相同。全站legacy verifier既有ChArUco inline schema失敗仍存在，未算通過；原工程圖未納入這輪首讀評分。
- 啟用：selected-assets.json；實證：image-review.md、page-review.md、validation-summary.json、scope-verification.json、public-release-verification.json。公開入口 https://hctsaik.github.io/visionAI_Model_Introduce/#view=lesson&lesson=frame-difference&slide=1 。
- 使用者成品核准：pending。圖像為教學示意，無模型推論／現場效能或真人學習測試。下一步僅依使用者成品回饋開新修訂，保留本輪版本與證據。

## WI-030 進行中：十二課重作
專用清單：workitems/wi-030/PLAN.md。先保存現版與查來源，PatchCore原型後展開其餘課程；工具測試、自評、使用者核准分開。

WI-030 checkpoint：正文12課草稿與共享入口修正已落盤；ResNet原型完成，其他圖逐版生成修正，未整合。詳見workitems/wi-030/PLAN.md和prototype-review.md。學習已合併根IMAGE_STYLE_GUIDE、TEACHING_WEBPAGE_GUIDE及共用REVIEW_LOG。下一步全部PNG審查與真實頁面測試；未將使用者核准打勾。

WI-030接續：九課已整合本機且建置成功，18/21故事候選審查完成，剩姿態核心/比較手機及YOLO核心。詳細失敗與修正見prototype-review.md，分項非使用者核准；頁面整套QA未跑。下一步完成42PNG與12課整合、互動與HTTP驗證、持久快照及發布。當前建置與測試程序需先核對再續作。


## WI-030 最終審查 checkpoint（2026-09-11）
21故事42張PNG逐圖原生與936/328px審查完成，分數91–96，啟用版本及hash見selected-assets.json、image-review.json；十二課預設主線完成逐頁閱讀，自評92–93，證據與扣分見page-review.md。五課既有deep_dive資料保留，只增加預設收合旗標；原工程內容未算本輪評分。使用者成品核准pending。
72頁面狀態／216次解碼放大Escape／自測及導覽通過；最後自測改為帶條件的合理替代選擇，另測24桌機手機狀態，確認新解答實際展開可讀。84HTTP圖片hash、1231引用資產及HTML一致、12課變更／46課不變／5課舊章資料保留均通過。聚焦pytest 9 tests＋10 subtests、bundle 1 test通過。舊全站verifier仍在未改動ChArUco inline schema失敗，不計為通過。
即將執行：僅更新自評狀態後最後重建HTML與docs，刷新hash及範圍證據，保存teaching-maintenance快照，再依本輪既有授權commit/push並核對公開HTML與42PNG。現在公開站尚未更新；發布未完成。必要來源與prompt意圖在workitems/wi-030，截圖及原生PNG亦保存在該持久目錄。沒有模型推論或真人學習實測。


### WI-030 發布文件缺漏修正
最後查操作卡時發現本機docs缺少model.md／slide-manifest.md，原因是bundle只選圖與concept_path，未收modelPath／manifestPath。HTML雖有連結，但發布目標不存在；不是瀏覽器快取。已補builder依現有課程連結打包文件，會使其餘課程既有文件也可到達，不改其教材JSON。即將重建docs、測全部文件的來源／打包位元一致及十二課24個HTTP連結；原1231資產數屬修正前歷史，新總數待實際建置確認。公開部署尚未執行。


## WI-030 發布前核對完成
最新打包1347引用資產與HTML皆與來源hash一致（新增58課既有model.md及manifest共116文件；其餘46課教材JSON仍不变）。新增文件打包回歸2 tests＋116 subtests通過，十二課24文件HTTP/hash通過。前述1231是補文件前的歷史數量；不覆寫歷史紀錄。72互動狀態、216次放大Escape及24最終主線／新解答狀態均完成；最終HTML hash與完整範圍見validation-summary.json。
已完成逐圖、逐頁分項評分與兩份指南／共用REVIEW_LOG學習回寫。接下來保存teaching-maintenance可恢復來源、prompt、審查與測試快照，commit/push；公開HTML、42PNG及116文件HTTP核對尚未完成。啟用為本機候選，自評與工具驗證通過；使用者核准pending。舊全站ChArUco schema錯誤仍列失敗，無其他阻礙。


## WI-030 完成與公開版本（2026-09-11）
- [x] 四個異常偵測與八個分類／分割／姿態Topic共12課已重作並發布；21個故事、42張桌機手機PNG，必要原理、反例、比較、自測及操作卡完整。
- [x] 逐圖原生及936/328px自評、十二課整頁閱讀完成；實際驗證72頁面狀態、216次圖片解碼放大Escape、24最終閱讀／新解答狀態、84本機PNG HTTP/hash。
- [x] 最終1347引用資產及HTML來源／docs一致；僅12課教材JSON變動，其他46課一致，五課既有深讀資料保留。文件打包修正涵蓋58課共116既有文件，2 tests／116 subtests及12課24文件HTTP/hash通過。聚焦UI／型別／尺寸回歸9 tests／10 subtests通過。
- [x] 內容commit `c7d1533214fb832abbdaccc93b5ac88c06539ffd` 已push；Pages run 34508577230 成功。公開HTML、42PNG與116 Markdown文件逐一HTTP及內容hash核對成功，證據public-release-verification.json。
- [x] 共用學習已写回IMAGE_STYLE_GUIDE.md、TEACHING_WEBPAGE_GUIDE.md與TEACHING_REVIEW_LOG.md；版本／prompt／來源／自評／實際驗證及可恢復修改保存在workitems/wi-030與teaching-maintenance快照。
- 限制：舊全站verifier仍在未改動ChArUco inline schema失敗，未算通過。原工程圖未重審，不用本輪首讀分數代表舊工程內容。所有新圖為教學示意，無本輪模型推論、現場效能或真人學習測試。
- 狀態：實作、驗證與公開發布完成；使用者成品核准pending。下一步僅依使用者實際成品回饋開修訂，不把自評通過當作核准。即將把公開驗證紀錄同步並另做紀錄commit；不再改教材。

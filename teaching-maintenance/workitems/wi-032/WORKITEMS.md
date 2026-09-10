## WI-032-P 發布 checkpoint（2026-09-11）

第一部分六課成果已 commit 並 push：2e218926e2ff5d1a8d21ca5cb7bbe381fde27819；GitHub Pages 部署成功，公開 93 個檔案逐一 hash 與已提交內容一致（本機部分 Markdown 為 CRLF，Git 為 LF，文字內容一致）。發布證據為 workitems/wi-032/public-release-verification.json。最新學習及接續資料同步保存在 Git 的 teaching-maintenance。使用者成品核准仍 pending；第二部分 52 課未開始，下次依根 Overall_Review.md 第二部分接續。此段取代下方歷史未發布狀態。

## WI-032-P 發布 checkpoint（2026-09-11）

使用者已明確授權 commit + push。正在整理第一部分六課與最新學習／接續紀錄，尚未提交；完成後核對遠端與公開網站。第二部分 52 課保持未開始，下次由 Overall_Review.md 第二部分接續。細項見 workitems/wi-032/PLAN.md 的 WI-032-P。

## WI-032-H 下次從第二部分接續（2026-09-11）

使用者表示之後再請接著做；目前停在第一部分六課本機重建完成、第二部分 52 課局部修正尚未開始。下次說「接著做／第二部分」時，先讀根 Overall_Review.md 第二部分及課程 workitems/wi-031/REPORT.md，核對現行引用，再建立分批修正工作項，優先修正語意錯誤。詳細交接見課程 workitems/wi-032/PLAN.md 的 WI-032-H。

Git 實查：本機 HEAD 與遠端 main 同為 79364cf0fb82ed7c016092f30ba68771578bcb01，但第一部分成果及最新紀錄仍有未提交變更／未追蹤檔案，因此尚未全部 check in／push。這次只保存接續紀錄，未提交或發布。第一部分使用者成品核准 pending；第二部分不能標成已完成。

## WI-032-L 學習補記完成（2026-09-11）
已依使用者要求補入 TEACHING_REVIEW_LOG.md 的 WI-032-L：六項觀察、規則位置、下次驗證，以及 HTML 最終版本固定的學習；共用原則同步 TEACHING_WEBPAGE_GUIDE.md。細項與證據見課程目錄 workitems/wi-032/PLAN.md。六課本機完成、使用者核准 pending、未發布；第二部分 52 課未啟動。

## WI-032 最終完成狀態（取代下方舊checkpoint）
WI-032第一部分六課本機重建、自評與必要驗證完成。Overall_Review.md已分列6課／52課；本輪學習已回寫三份權威Markdown。76張新PNG（28主線＋48工程）及正文／自測／交付已啟用；24主頁狀態／168放大、18補測狀態、14 tests／130 subtests通過，1351資產hash一致，52課payload不變。報告：teaching-images/vision-ai-model-selection/workitems/wi-032/REPORT.md。無未完成必要實作或驗證；使用者成品核准pending，未commit/push/發布。下一步：依使用者審閱處理回饋；第二部分52課等待後續指示。

## WI-032 進行中：Overall Review第一部分六課重建
- 總計畫：根Overall_Review.md已建立，兩部分共58課與學習已記錄。
- 授權：製作第一部分6課主線及受影響工程圖；第二部分52課維持待辦。
- 接續：teaching-images/vision-ai-model-selection/workitems/wi-032/PLAN.md為唯一細項。下一步保存基準、實看參考、製作preflight與單圖原型。
- WI-032最新checkpoint：Overall_Review.md已列第一部分6課、第二部分52課與學習；6課完整正文／自測草稿已保存lesson-content.json，15檔基準與14組主線brief已保存。ECC核心桌機手機、DINO核心、YOLO-World核心等候選已生成實看；ChArUco兩次生成角點失敗後改精確SVG，r05已產出待頁內核對。SIFT/LightGlue點位與ECC反例仍在修正，不把候選當完成。其餘反例／比較正在製作，工程4圖尚待重建；尚未整合教材，測試未跑，未發布，user approval pending。下一步完成主線候選與精確幾何修正，再重建工程層、整合和實頁驗收。產物在workitems/wi-032，詳細原生審查見prototype-review.md。

## WI-031 最終完成：58課Markdown標準審查（2026-09-11）

- 狀態：審查與學習落盤完成，取代本檔下方WI-031執行中checkpoint。全課符合0、局部修正52、主線重建6：ChArUco、ECC、SIFT、LightGlue、DINO detector、YOLO-World。
- 完成範圍：58課桌機／手機主線、每課4工程圖、五課40深讀章節。52課主線可保留，工程／指定深讀／手機需局部修正；不等於58課全部重建，也不沿用舊首讀分數判整課通過。
- 產物：teaching-images/vision-ai-model-selection/workitems/wi-031/REPORT.md（58課總表、保留／修正範圍、優先序與證據）、results.json、observations.md、final-verification.json；細項入口PLAN.md。
- 實際驗證：116頁狀態、376放大、116自測、116導覽完成；80深讀章節尺寸狀態／148視圖；644資產course/docs與基準hash一致、HTML未變；66共享主圖hash核對。188手機圖說0字形重疊，13過早白圖重查正常。305報告連結與424逐課證據路徑通過。
- 學習：根IMAGE_STYLE_GUIDE.md、TEACHING_WEBPAGE_GUIDE.md、TEACHING_REVIEW_LOG.md已回寫，v1.0配分不變。人工缺口分類，沒有替644圖逐張編造完整分數；本輪未重跑模型、未做真人學習測試。
- 授權／下一步：本輪審查工作無未完成項與阻礙。教材未修改，未commit/push/發布；使用者成品核准不由審查推定。後續收到重製指示時從REPORT的6課P1與局部語意錯圖另開工作項，不自動啟動生成。

## WI-029 foundations／production 兩入口重製（2026-09-10）
- 最終完成（取代下方歷史checkpoint）：WI-029兩入口重製及發布完成：內容commit `c6c32a4bad797a0c1bebb5287db6f95c5ffd0b95` 已push，Pages run 34415751416 success；公開HTML、12張PNG及2份Markdown全部一致。六案例由Markdown驅動，12狀態36次放大／自測、8最終狀態、9項回歸、1303資產course/docs一致；圖自評92–94、兩頁94，使用者成品核准pending，未做真人學習測試。
- 最新checkpoint（取代下方舊狀態）：兩入口本機重製與驗證完成：6故事／12PNG，Markdown實際驅動頁面；12狀態36圖放大與解析、24PNG HTTP hash及4Markdown HTTP通過，8最終狀態正文一致與圖首可達，9回歸PASS，1303引用檔course/docs一致。圖自評92–94、頁93–94，使用者核准pending。學習回寫三份共用Markdown，正在保存副本／commit＋push；公開核對尚未執行。
- 使用者明確指定兩頁重作並commit＋push；進行中，先保存基準與製作原型。
- 接續：teaching-images/vision-ai-model-selection/workitems/wi-029/PLAN.md。
- 八個時序主題保留WI-028待辦；两入口由WI-029接手。未生成／驗證／發布，使用者核准pending。

## WI-027 視覺基礎與多模態七課重製（2026-09-10）
- 最終發布完成（取代下方舊checkpoint）：七課重製commit `784e572633b7b35d9d380ef327523d6b270af8d8` 已push，遠端main一致；Pages run 34399986161 success，公開HTML及30PNG SHA256全部通過。84份已提交學習／審查副本hash一致；Git工作目錄乾淨。七課實作與技術驗證完成，使用者成品核准pending。WI-028時序八課及production／foundations仍排隊，未宣稱完成。
- 已commit＋push：`784e572633b7b35d9d380ef327523d6b270af8d8`，遠端main一致；84份已提交副本hash通過，Git乾淨。Pages run34399986161排隊，公開版本尚待核對；下一步等部署成功後執行publish_check.py。
- 發布前最終核對：1289個引用資產的course/docs SHA256及HTML全數一致，清理90個未引用發布檔（作者來源保留）；7課preflight通過。頁面狀態更新後CopyFile2遇Windows1224，已用逐檔hash及14狀態／60HTTP重驗確認完整。保存副本初次因bundle報告未完成中止，現報告存在後重跑。接著commit／push；使用者核准pending。
- 最新完成 checkpoint（取代下方執行中狀態）：七課重製30張PNG／15組故事，圖文與model.md已接入course/docs。42狀態126次放大／Escape、自測導覽、14最終頁面狀態、60 HTTP hash、1289資產存在及5項回歸通過；30圖自評91–96、7頁93–94，使用者核准pending。QA曾與docs複製重疊而失敗，建置完成後重跑通過。即將同步學習副本、commit＋push及公開核對，尚未發布。證據workitems/wi-027/。
- 最新 checkpoint：30張已逐張原生／頁內審查；SigLIP手機r05完整結論及負配對修正通過，原生861×1827已明確登錄。前五課30狀態90次放大通過；即將整合SigLIP／Qwen、清理重建發布包及最終驗證。尚未commit/push，使用者核准pending。
- 生成校正 checkpoint：LLaVA r02 已修正投影旁路；DINOv3 r02 矩陣已對稱。SigLIP r01 負配對損失方向錯誤、Qwen r01 把照片切片當特徵、Gemini r01 把能力名稱當 model ID，均未採用。比較圖另有錯配標籤及查詢繞過編碼器，反例圖不應把生成圖稱實拍；六項 r02 brief 已驗證，正在生成桌面／手機修訂，尚未整合／發布。產物及 prompt：workitems/wi-027/corrections-batch5.json；完整驗證未跑，使用者核准 pending。
- 最新核對：七課正式 topic 仍引用 f02 舊圖，docs 中 WI027 PNG 為0；遠端仍為上一輪 bd4b87b，尚未提交本輪。已保存六張候選PNG（含DINOv2失敗稿），七課正文草稿、14個其他故事preflight及整合脚本；仍需修圖／生成其餘圖、整合、驗證及發布。
- 最新使用者授權：先完成本七課、學習寫回及 commit＋push，再執行 WI-028 八個時序主題與 production／foundations；前輪仍在生成及驗證，不縮減原範圍。
- 目標／授權：依使用者截圖，以 Markdown 與 skill 重製 DINOv2、DINOv3、CLIP、SigLIP、LLaVA、Qwen-VL、Gemini Vision 七課。
- 狀態：進行中；已讀教學 cycle／imagegen／planned-code-modifier，正在核對五份權威與现版。尚未生成、整合或測試；使用者成品核准 pending。
- 範圍：七課首讀圖文、桌面／手機插圖、反例、比較與自測；既有工程參考另列。沿用前輪完整交付流程，完成後同步學習保存副本及 commit／push。
- 接續入口：teaching-images/vision-ai-model-selection/BEGINNER_VISUAL_TODO.md、BEGINNER_VISUAL_STATUS.md，workitems/wi-027/。
- 下一步：保存七課基準、查第一手來源與具體版本、實看認可參考，先製作一張代表原型，再逐課生成。
- 驗收：逐圖及整頁 v1.0 證據、桌面／手機實看、course/docs 引用／HTTP／互動與必要回歸；學習及實際結果落盤，生成示意與模型實測分開。

## WI-026 生成與影像復原八課重製（2026-09-09）
- 2026-09-10 最終發布完成（取代本項下方未發布 checkpoint）：commit `bd4b87bc5601d884a1ffe9cf0fb9e4f0d03330d6` 已推送，遠端 main 一致，Git 工作目錄乾淨；Pages run 34386196881 success，公開 HTML 與 38 張 PNG SHA256 核對通過。17 個已提交維護副本 hash 一致；證據 `workitems/wi-026/public-release-verification.json`、`deployment.json`。提交範圍為 docs 與 teaching-maintenance，原始作者工作區仍留本機；使用者成品核准另列 pending。
- 發布 checkpoint：commit `bd4b87b` 已 push 到 origin/main；49 檔包含網頁、38 PNG 與維護紀錄，17 個已提交副本 hash 一致，Git 工作目錄乾淨。公開 Pages 部署與 HTTP 版本仍待核對。
- 2026-09-10 發布授權：使用者要求進行 commit＋push。即將核對並提交 docs 與 teaching-maintenance，推送後驗證遠端及公開 HTML／38 PNG；發布尚未完成，以下未發布狀態為前次 checkpoint。
- 收尾核對：17份teaching-maintenance保存副本SHA256一致，git diff --check PASS；本機版本完成。
- 目標／授權：依截圖使用教學skills與Markdown重做八課首讀圖文。
- 狀態：本機完成，使用者核准pending；未commit/push。
- 成果：八課首讀圖文完成：每課核心／反例／比較三張，19組不同故事、38張桌面／手機PNG。已接入topic、learner、model.md與course/docs；影像為AI生成示意。
- 驗收：38圖自評91–95，8頁93–94（v1.0逐項證據）；48狀態144圖放大／Escape、自測與導覽通過，最後操作卡修正後16狀態可見文案／圖片／無溢出通過；76次HTTP hash與course/docs一致，5項回歸PASS、8課preflight PASS。
- 接續入口：teaching-images/vision-ai-model-selection/BEGINNER_VISUAL_TODO.md、BEGINNER_VISUAL_STATUS.md；證據workitems/wi-026/image-assessment.json、page-assessment.json、validation-summary.json。
- 下一步：有新回饋再按版本證據修訂；公開網站尚未更新，保留工程參考圖不在本輪評分範圍。

## WI-025 視覺參考偏好落盤（2026-09-09）
- 目標／授權：使用者要求把首選兩張幾何圖、次選四張模型圖的風格順序寫入對應 Markdown；僅文件維護。
- 狀態：文件已完成；圖片指南記錄首選／次選、明示與歸納界線，網頁指南連回權威，共用 log 保存原話與下輪驗證方式。
- 接續：BEGINNER_VISUAL_TODO.md / BEGINNER_VISUAL_STATUS.md 的 WI-025；IMAGE_STYLE_GUIDE.md 11.3；共用 TEACHING_REVIEW_LOG.md。
- 下一步：後續製作先讀 IMAGE_STYLE_GUIDE.md 11.3 的 WI-025 並實看首選參考；本輪無待製作項。
- 驗收：參考可定位、順序明確、舊規則衝突已說明；不把風格認可當技術驗收。未生成圖片、未跑程式測試，無阻礙。
- 實際驗證：兩張首選 PNG 存在，3份更新保存副本 SHA256 一致、git diff --check PASS；文件維護完成，未 commit/push。

## WI-024 偵測課程重製（2026-09-09）
- 目標／授權：使用skill重製指定課程，完成後直接commit＋push；桌面／手機實際PNG、首讀圖文、驗證與學習同步。
- 範圍：已提供det-yolo-dense、det-rtdetr、det-grounding-dino-interface、yoloe四連結；使用者稱六個，另兩題已詢問待回覆，不自行推定。
- 狀態：四個已提供連結的課程重製與發布完成，commit `184f1ee4da026e90160e97bfdb073428fd08f842` 已push且遠端main一致；工作目錄乾淨，12個已提交副本hash核對通過。
- 接續：teaching-images/vision-ai-model-selection/BEGINNER_VISUAL_TODO.md WI-024、BEGINNER_VISUAL_STATUS.md、workitems/wi-024/；共用TEACHING_REVIEW_LOG.md。
- 最終驗證：Pages run34288353853 completed/success；公開HTML與發布版一致，20張新PNG全部HTTP200且SHA256一致。證據為workitems/wi-024/public-release-verification.json、deployment.json、release-audit.json及逐圖／整頁評分。
- 下一步：四課已完成；另外兩題仍待使用者補連結，不自行推定。使用者成品核准pending、未做真人學習測試。已提交docs、skill與四份學習Markdown及三份審查副本；完整作者工作區／本接續檔仍保留本機。
- 驗收：各題正式引用、逐圖與整頁審讀、兩入口與公開版本核對；同步學習保存副本，commit/push。成品使用者核准另列pending。

## WI-023 學習文件 commit＋push（2026-09-09）
- 目標／授權：使用者要求提交及推送 WI-022 更新的 skill 與四份 Markdown。
- 狀態：完成commit＋push；現有repository的teaching-maintenance保存明示來源的版本副本，原位置仍為編輯權威。
- [x] 保存四份Markdown、完整teaching-review-cycle skill及本輪接續紀錄，更新精確追蹤範圍與來源說明。
- [x] 核對副本一致與skill格式、commit/push、驗證遠端HEAD。
- 已驗證：9個來源／副本SHA256一致、skill quick_validate PASS、git diff --check PASS。README列出還原方法與歷史證據未全數備份的限制；.gitattributes保留副本位元組。
- 發布結果：commit `4a65188` 已push到origin/main；9個已提交Git blob雜湊符合manifest，遠端HEAD與本機一致、tracked工作目錄乾淨。docs網站內容未修改。
- 格式紀錄：首次staged diff檢查把原始CRLF與歷史空白視為格式錯誤；保存副本以.gitattributes保留原始位元組及空白，未改寫來源內容，重查通過。
- 下一步：後續更新學習權威檔時，同步teaching-maintenance副本與manifest再提交。本輪完成。

## WI-022 學習回寫 skill 與四份權威 Markdown（2026-09-09）
- 目標／授權：依使用者要求，把 WI-021 可重用學習寫進 teaching-review-cycle 與圖片指南、網頁指南、評分量表、共用 review log。
- 狀態：完成；skill與四份Markdown已回寫，保留 v1.0 配分與門檻。
- [x] 核對既有規範與實際失敗／修正。
- [x] 更新 skill 主入口、產圖參照及四份 Markdown；單次模型細節留在 log。
- [x] 驗證 skill、連結與適用範圍，更新完成紀錄。
- 實際驗證：quick_validate PASS；6份檔案UTF-8讀取、3個skill相對連結PASS；人工核對文件分工與適用範圍。完成紀錄腳本因PowerShell管線中文字元失真未寫入，已改用apply_patch完成。
- 下一步：下輪教學製作依更新規則建立brief與成圖驗證。詳細對照見TEACHING_REVIEW_LOG.md WI-022；本機保存，未發布這些檔案。
- 驗收：新規則可從 SKILL.md 找到，各文件職責清楚，無改分湊門檻；本輪不重新製圖或發布網站。
## WI-021 已完成重製與發布（2026-09-09）
- 授權：使用者要求以skill重製13課；沿用commit＋push授權。實作、工具驗證與發布完成；使用者成品核准pending、真人學習測試未做。
- 產物：13課首讀圖文、43組邏輯圖槽、62張不同PNG（桌面31／手機31），imagegen實際生成並逐圖審看；原工程參考保留。示意圖不當作真實模型推論。
- 驗證：course/docs 78狀態與258次圖互動PASS；最終26狀態與86圖解碼PASS；124本機HTTP雜湊PASS。公開HTML與發布版一致，公開62PNG全部200且SHA256一致。
- 必要回歸PASS：ad_f01 4、navigation 3、tall_mobile 1、bundle 1、三圖首讀邊界1。全站charuco verifier阻塞與anomalydino整檔4個歷史斷言失敗未處理，不宣稱全站通過。
- 發布：commit `749401f96609279cd19c068b897a4edb17504476`；origin/main一致，worktree乾淨。GitHub Pages action 34283005280 completed/success；https://hctsaik.github.io/visionAI_Model_Introduce/
- 證據：workitems/wi-021/public-release-verification.json、release-audit.json、page-assessment.json、image-assessment-*.json、qa-*/；共用TEACHING_REVIEW_LOG.md。Git僅發布docs與README，根記憶和製作素材保留本機，未宣稱已push。
- 下一步：本輪已授權工作完成；若使用者給成品回饋，從此版本與上述證據接續。舊checkpoint保留為歷史，由本段取代。

- 接續入口：teaching-images/vision-ai-model-selection/BEGINNER_VISUAL_TODO.md WI-021。

## WI-020 Git commit／push 同步（2026-09-09）

- 目標／授權：使用者要求 commit + push 現有工作。
- [x] 核對唯一 Git 儲存庫 `teaching-images/vision-ai-model-selection`：tracked worktree 乾淨，HEAD `c05f69b`；根目錄不是儲存庫，現行 .gitignore 僅發布 docs 與 README。
- [x] `git push origin main` exit 0，回覆 Everything up-to-date；`git ls-remote` 確認遠端 main 與 HEAD 同為 `c05f69b103190a5aa11c9a26c0d38317575777a2`，工作目錄乾淨。本輪沒有新增 commit。
- 範圍／限制：本輪審查 Markdown 位於儲存庫外，課程內審查證據被排除；未改公開追蹤範圍，沒有建立空 commit。同步確認完成；審查紀錄仍僅保存在本機，不宣稱已提交。

## WI-019 目前接續：13 課重審已完成，重建為建議範圍（2026-09-08）

- 使用者目標：用 skill 重新檢視指定公開 13 課，判斷是否重建。已完成審查，正式教材未改、未發布。
- 結論：6 課可保留核心思路並重編後續，7 課宜大幅重建首讀內容；保留網站框架及有效互動。優先 RD4AD／AnomalyGPT 的案例與角色矛盾，AE 適合先做完整示範課。
- 證據與量表：共用 `TEACHING_REVIEW_LOG.md` 的 WI-019；65 張桌面逐圖 v1.0 五分項已記錄，`teaching-images/vision-ai-model-selection/review-evidence/wi-019/assessment.json`；26 張手機前兩圖實看。
- 驗證：公開 HTML 與 docs hash 相同；130 次放大開啟／Escape、26 次解答與導覽；13 次手機首圖放大等完整載入通過。來源、截圖、互動及補查紀錄均在 `review-evidence/wi-019/`。Git tracked worktree 仍乾淨。
- 限制：隱藏正式 slide 圖、手機後續所有橫向區域及真人理解未全面評估；全章總分、最終五項完成度及使用者核准未取得。較早 WI-019 進行中 checkpoint 由本段取代。
- 下一個具體動作：依使用者後續決定確立製作範圍；若開始重建，從 AE 單張版本化 preflight／桌面手機原型開始，讀既有五份權威與本輪逐課缺口，單圖審查後再擴展。不可把審查完成當成重建完成。

## WI-017 歷史接續：SIFT＋LightGlue 依 ECC 學到的契約重產（2026-09-08）

- 狀態：使用者確認若經驗已寫回 Markdown，接著重做 SIFT 與 LightGlue。
- 寫回：RULE-013（算法／學習模型／配對器）；網頁指南新增「不要把算法當 AD 模型」；`TEACHING_SITE_READING_LAYERS.md` 補「方法還是模型」並授權本兩題。
- 已完成：兩課各五張 r06 PNG 已接到正式 topic；HTML／docs 已同步。SIFT live 標題從「不是學習模型」起；LightGlue 從「是學習配對器，不是偵測器」起。工程參考皆 0 圖。
- 入口：http://127.0.0.1:8000/interactive-learning.html?rev=sift-lg-r06#view=lesson&lesson=sift&slide=1 與 lesson=lightglue
- 未宣稱 >90 或使用者接受。

## WI-016 完成第一遍：ECC 整題依 C1–D5 重產（2026-09-08）

- 狀態：使用者要求重新思考並重新產生 ECC 教學主題。WI-015 層契約已採納。
- 授權：只重產 ECC 第一遍五張＋topic 文案；保留 R04/R05 舊檔；不改 58 題；不標使用者接受。
- 已完成：五張 `ecc-r06-c1`…`d5` 已接到正式 topic；HTML／docs 已同步。live 標題為工作→做法→輸出→HOLD→選型。工程參考 0 圖。估得 32.1、12.1 px（設定 32、12）；錯起點對回 217 px。
- 未做：正式四張 slide 未重畫；未宣稱 >90 或使用者接受。
- 入口：http://127.0.0.1:8000/interactive-learning.html?rev=ecc-r06#view=lesson&lesson=ecc&slide=1

## WI-015 暫停完成診斷：多代理重想整站閱讀層（2026-09-08）

- 狀態：使用者指出「工程參考」又把本文圖片重複一遍；要求 multi-agent 重想整個教學網站邏輯與流程。WI-014 ECC 內容修訂並行未完成。
- 授權：只做閱讀層診斷與建議落盤；未授權一次改 58 題。先釐清各層該新增什麼，再決定是否改 builder。
- 已知結構：image-led 課的 `legacyCausalReferenceHTML()` 仍呼叫 `causalChainHTML()`，而 `inline_image` 指向同一組 beginner PNG，所以展開「工程參考」會再播一次主圖。
- 已完成：三代理報告在 `tmp/teaching-site-flow/`。契約 `TEACHING_SITE_READING_LAYERS.md`。image-led「工程參考」改為文字因果鏈（Playwright：該區 img=0、causal-step-text=4）。
- 未做：58 題內容重排成 C1–D5；deep_dive 與正式四張的關係。
- 驗收：工程參考不再嵌入 beginner PNG。全站改造與使用者核准分開。

## WI-014 暫停未完成：ECC R05 先講「它在做什麼／怎麼做」（2026-09-08）

- 狀態：使用者判定現行頁沒有介紹 ECC 是什麼、怎麼做到；插槽已修好但教學主線仍從 HOLD 起跳。使用者核准 pending。
- 授權：沿用「修到滿足為止」；本輪先做 visual 1 C 型原型（什麼＋怎麼做），保留 R04 其餘圖。
- 已完成：`ecc-r05-v1-what.png` 已接到正式 visual 1；HTML 已重建；docs 已同步該檔。live 標題為「ECC 在做什麼？把已接近的畫面微調重合」。
- 下一步：等使用者對這張「是什麼／怎麼做」圖的評語；其餘 R04 頁未改。不宣稱 >90 或使用者接受。
- 入口：http://127.0.0.1:8000/interactive-learning.html?rev=ecc-r05-what#view=lesson&lesson=ecc&slide=1
- 授權範圍：teaching-review-cycle G0–G6 + teaching-visual-slot-audit；不標使用者接受。
- 剛完成：重建 `docs/`。重建前 `/docs/index.html` 機制步驟是 `<object>` SVG **388×194**、beginner 仍 R01/R02、正式圖仍 ppt-master。重建後 course 與 docs 皆為 `ecc-r04-*.png` full-width **894×503**／beginner **936×527**／正式 **1010×568**；`audit_lesson_visual_slots.py ecc` failures=0。
- 已落盤：`TEACHING_VISUAL_SLOT_AUDIT.md`、`tools/audit_lesson_visual_slots.py`（含截圖與 CSS 寬）、Grok/Codex skill `teaching-visual-slot-audit`。
- 下一步：R04 相對 AnomalyDINO 漫畫密度仍未宣稱 >90；等使用者對 live 大圖的內容評語，不把插槽修復當視覺達標。
- 證據：`tmp/ecc-slot-audit.json`；重建前 `tmp/ecc-agent-inspect/docs-first-causal-before.png`。
- 入口：http://127.0.0.1:8000/interactive-learning.html?rev=ecc-r04-docs#view=lesson&lesson=ecc&slide=1 以及 `/docs/index.html` 同一 hash。

## WI-013 暫停：ChArUco R02 Sol→Luna→Sol 循環（2026-09-06）

### R03 delivery-gate update (Luna, 2026-09-06)

- Status: source implementation-complete; PNG evidence generated but visual validation is blocked by local Qt font fallback.
- Next action: replace or repair the rasterizer with a text-capable local path, then re-inspect both PNGs; do not connect the formal topic or batch update.
- Artifacts: `teaching-images/vision-ai-model-selection/_course_content/generated-concepts/charuco/charuco-r03-core.svg`, `charuco-r03-core-mobile.svg`, `charuco-r03-manifest.json`, `tmp/charuco-r03/final/desktop.png`, `tmp/charuco-r03/final/mobile.png`.

### R03 原型 checkpoint（Luna，2026-09-06）

- 授權範圍：只製作一張 ChArUco 核心 prototype；保留 R02，不批量重製、不改量表、不標為使用者接受。
- 已完成：找到 R02 原生 SVG／Edge Playwright 匯出入口；建立 `tmp/charuco-r03/brief.md`，明列 C 故事、單一路徑、4 節點、參考頁與單一 `#FFF4CC` takeaway。
- 進行中：繪製 R03 桌面／手機 SVG，解決 `CHAR-P0-01`、`CHAR-P0-02`、`CHAR-P0-03` 與 `CHAR-P1-05`。
- 下一步：新增版本化 SVG／PNG 與候選 manifest，更新單一首圖候選引用，跑 preflight／局部檢查並實看最終桌面／手機 PNG。
- 預期產物：`_course_content/generated-concepts/charuco/charuco-r03-core.svg/.png`、`charuco-r03-core-mobile.svg`、R03 manifest、`tmp/charuco-r03/final/desktop.png` 與 `mobile.png`。
- 尚未完成／阻礙：尚未生成或實看 R03 PNG；Sol 複審與使用者接受均未取得。

- 後續連線確認：使用者指定 Playwright 後，獨立 Python Playwright + headless Edge 已成功開啟指定 ChArUco URL，取得 DOM 並實看 1440×1000 首屏截圖 `tmp/charuco-playwright-check/desktop.png`。內建 browser runtime 仍不可用；後續可用此 Playwright 路徑補查，尚未完成整章／手機／互動驗收。

- Sol 已完成整章可取得範圍的固定量表審查：頁面 72/100；五張 beginner 主圖 60/65/64/71/72；三張輔助圖未評估。舊 R02 自評 92 保留歷史但撤回有效性。
- Sol 已寫入 `TEACHING_REVIEW_LOG.md`，並建立 `teaching-images/vision-ai-model-selection/CHARUCO_R02_SOL_TO_LUNA_HANDOFF_2026-09-06.md`；問題 ID、原因、修訂、保留項與驗收條件均已落盤。
- 狀態：等待 Luna 只修一張核心原型；使用者尚未核准。Browser runtime 無可用實例，standalone Playwright sandbox `WinError 5`，未評估三張輔助圖最終渲染與即時互動。
- Luna checkpoint：已產生候選 `tmp/charuco-r03/brief.md`、`charuco-r03-core.svg`、`charuco-r03-core-mobile.svg`、`charuco-r03-manifest.json`；R02 仍為正式引用。R03 PNG 因 Edge／Playwright `WinError 5` 尚未產生，未能實看，Sol 複審暫停。
- Sol delivery-gate 複核：R03 不可評分；另有唯一 marker 圖樣、PnP 多點 correspondence、predicted c17 可回算、P95／coverage 門檻、正式自測未接入等缺口。
- 下一步：Luna 先修 source-level 缺口並以允許的本機路徑產出／實看 R03 desktop/mobile PNG；再由 Sol 逐問題 ID 複審，不得批量推展。
- 循環狀態：使用者已確認持續執行 Sol→Markdown→Luna→Sol；本輪 Luna 正在修正 delivery-gate 缺口，直到原型達固定門檻或明確記錄阻礙。

## WI-012 F02 — 27 題核心重建撤回，全部待修訂（2026-09-06）

- [!] 使用者判定 27 題 F02 成品質量太差、不可使用；27 題全部回到待修訂。
- [x] 幾何 4、時間／影片 8、Foundation／VLM 7、Diffusion／復原 8，共 27 題完成 F02 核心重建。
- [x] topic JSON、model.md、SVG／PNG／mobile SVG、manifest、interactive-learning.html 與 docs/index.html 已同步。
- [x] 270 個桌面／手機頁面狀態、放大／Escape、自測與無水平溢位通過；契約、導航、bundle、deep-dive regression 與 HTML verifier 通過。
- [x] 27 題 final desktop first-read 已逐題人工核對；未見裁切、核心流程缺失或水平溢位。
- [!] 使用者已逐題審閱並判定本輪品質不可用；27 題全部待修訂。獨立評審、真實模型推論與同條件效能比較也未完成。
- 證據：`teaching-images/vision-ai-model-selection/f02-review.json`、`tmp/f02-series/`、課程 BEGINNER_VISUAL_TODO.md／BEGINNER_VISUAL_STATUS.md。

# 工作項目與接續入口

## WI-013 R08 integration candidate — current checkpoint

- Formal topic remains unchanged at SHA256 `5298aecf02a3deaf1ef8d96755ad64bc6f58fea69c094aec93781c245cfe2895`.
- Candidate packet: `tmp/charuco-r08/charuco-r08-integration-packet.json`; candidate topic/page/wrapper/geometry contract are all under `tmp/charuco-r08/`.
- Mobile contract: `full-mobile`, intrinsic `720x1660`, candidate reference and verification both use `charuco-r07-core-mobile.png`.
- Next action: Sol integration recheck; do not edit formal topic or claim acceptance.

## WI-013 R07 formal integration candidate — current checkpoint

- Formal `teaching-images/vision-ai-model-selection/_course_content/topics/charuco.json` is unchanged (SHA256 `5298aecf02a3deaf1ef8d96755ad64bc6f58fea69c094aec93781c245cfe2895`).
- Candidate packet: `tmp/charuco-r07/charuco-r07-integration-packet.json`; candidate topic: `tmp/charuco-r07/charuco-r07-topic-candidate.json`.
- Scope: first beginner visual only, R07 versioned assets, no batch changes, no user acceptance claim.
- Next action: Sol page recheck; integrate only after explicit review outcome.

## WI-013 R07 ChArUco candidate — current checkpoint

- Status: R07 layout revision complete as a candidate; R06 and earlier remain intact, formal topic untouched.
- Evidence: `charuco-r07-core.svg`, `charuco-r07-core-mobile.svg`, `charuco-r07-manifest.json`, `tmp/charuco-r07/final/desktop.png`, `tmp/charuco-r07/final/mobile.png`.
- Validation: R07 brief preflight passes; both PNGs inspected; desktop provenance/detector and mobile third-zone spacing repaired.
- Next action: Sol re-review only; no batch update or user-approval claim.

## WI-013 R06 ChArUco candidate — current checkpoint

- Status: R06 source, PNGs, preflight, and manifest are complete as a candidate; not accepted and not connected to formal topic.
- Evidence: `charuco-r06-core.svg`, `charuco-r06-core-mobile.svg`, `charuco-r06-manifest.json`, `tmp/charuco-r06/final/desktop.png`, `tmp/charuco-r06/final/mobile.png`.
- Validation: Microsoft JhengHei loaded explicitly; OpenCV `DICT_4X4_50` board detector found 24/24 IDs including 17 and 23; both PNGs inspected with `view_image`.
- Next action: Sol re-review only; do not batch update or replace R04/R05.

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

## WI-009 D01 — 六題偵測系列本輪完成，待使用者審閱

WI-009 D01已完成本輪圖文重製及驗證（2026-09-06），待使用者審閱。六題各四幅主線、三個可見核心要點、移除設計及新情境自測；28個啟用資產。49項測試、48章節狀態、兩份HTML verifier及來源／bundle／HTTP一致性檢查通過。逐圖路徑、模式、設計意圖、分項、hash及限制見d01-detector-review.json和共用log WI-009。沒有新模型推論或外部部署，不宣稱已永久收斂。

- 紀錄：course BEGINNER_VISUAL_TODO.md／BEGINNER_VISUAL_STATUS.md／d01-detector-review.json；共用TEACHING_REVIEW_LOG.md WI-009。
- 本機入口：http://127.0.0.1:8000/interactive-learning.html?rev=detector-d01#view=lesson&lesson=det-yolo-dense&slide=1 。
- 後續收到讀者疑問，按相應圖及機制重新開啟，保留本輪證據；不把自評當作使用者核准。

## WI-008-R1 — 外部總評取捨與Markdown學習已完成（2026-09-06）

- 已核實E03學習記憶與七題正式topic hash；外部報告自述E01/E02，不直接沿用其分數作E03驗收。
- 逐項取捨與下輪驗證：TEACHING_REVIEW_LOG.md的WI-008-R1；通用原則合併TEACHING_WEBPAGE_GUIDE.md及IMAGE_STYLE_GUIDE.md。
- 候選製作與狀態：course BEGINNER_VISUAL_TODO.md／BEGINNER_VISUAL_STATUS.md。原報告保留並標示歷史範圍。
- 本輪未改頁面、未產圖或新增模型推論；E03完成狀態如下，使用者審閱與真人學習證據仍未取得。

## 目前接續：WI-007 E03 — 七題中心思想修正與驗證完成，待審閱

- ConvNeXt、ViT、U-Net、SegFormer、YOLO-Seg、Keypoint R-CNN、Pose Pipeline已補存在理由、核心因果圖、三要點、自測；回查ResNet E02。
- 新增14啟用桌面／手機圖，核心說明直接出現在主線；已實際整合本機頁面與docs。
- 19 tests＋18 subtests、94個桌面／手機章節狀態、兩份HTML verifier通過；14新資產hash及HTTP／bundle一致，bundle1323資產。
- 細項：course BEGINNER_VISUAL_TODO.md；進度與生成紀錄BEGINNER_VISUAL_STATUS.md；分項證據core-e03-review.json、共用TEACHING_REVIEW_LOG.md。
- E01整頁高分已由E02/E03取代；自評與工具PASS不等於使用者核准或真人理解，也不宣稱整套已收斂。WI-008独立總評及其他工作項目保留。
- 本機入口：http://127.0.0.1:8000/interactive-learning.html?rev=core-e03#view=lesson&lesson=convnext&slide=1 。未外部部署。

## 歷史：WI-007 ResNet E02修正完成

- 使用者指出E01未教清楚模型存在理由及skip connection；已實際重製前兩章，新增4個SVG及對應自測。
- E01 ResNet93撤回，以course resnet-e02-review.json記錄當輪自評和證據。這不代表八题品質已穩定收斂。
- 5項ResNet重跑、另5項聚焦測試＋14子測試通過；16個頁面狀態、4新資產hash、本機HTML/docs一致。
- 下一步：使用者審閱；有新缺口時沿既有授權繼續修改，不能只更新記憶。PaDiM暫停、PatchCore P04待改進仍是其他未結項目。
- 記憶：course BEGINNER_VISUAL_TODO.md、BEGINNER_VISUAL_STATUS.md；共用TEACHING_REVIEW_LOG.md及TEACHING_WEBPAGE_GUIDE.md。
- 本機入口：http://127.0.0.1:8000/interactive-learning.html?rev=resnet-e02#view=lesson&lesson=resnet&slide=1 。未外部部署。

## 目前接續：WI-006 — PatchCore P03 重製與驗證完成，待審閱

- 狀態：完成已採納的8章修正、正式整合與本機驗證；使用者尚未核准。
- 產物：17閱讀視圖、34桌面／手機圖，其中26新P03、8保留P01；實際CNN特徵、來源到coreset、權重對照、三模型流程、兩組公開raw/GT/output均已接入。
- 驗證：9項回歸＋14 subtests、HTML/docs、16章／30切換放大檢查、最終4個追加頁面檢查；34資產hash與bundle一致。
- 自評：整頁93，章內最低92、91、92、91、91、92、91、92；固定量表、逐視圖證據在TEACHING_REVIEW_LOG.md P03及p03-review-manifest.json。自評不代表核准或實際效能。
- 記憶：course BEGINNER_VISUAL_TODO.md、BEGINNER_VISUAL_STATUS.md；證據tmp/patchcore-review-20260906/p03/final/report.json。
- 入口：http://127.0.0.1:8000/interactive-learning.html?rev=patchcore-p03#view=lesson&lesson=ad-patchcore&slide=1
- Skill已補授權接續優先順序：評分被撤回後沿用原製作授權，不能只更新TODO停止。此次已完成實際重製。
- 限制：本機docs已更新1255資產；未外部部署，無真人學習／完整PatchCore現場推論／同條件模型效能實測。新回饋再依檔案重開。

## 目前接續：WI-005 — A14 整套教材完成，待審閱

- 狀態：八章既定修改、本機整合、驗證與學習紀錄完成；待使用者審閱，非使用者已核准。
- 已完成：第1/5章同屏對照、第2章查庫結果、第8章两種原始作者成功例；A13第3/7章修正保留。共21視圖、42桌面/手機資產，本輪新增13。
- 驗證：9項回歸（另8 subtests）、HTML與docs verifier；16章與42視圖切換/放大/自測/無溢出，42資產hash確認。
- 固定量表v1.0自評：整頁92，章節最低93、91、91、93、93、93、91、92；逐圖>90、五項>=8、無未解否決項。證據與限制見TEACHING_REVIEW_LOG.md A14及course a14-review-manifest.json。
- 下一步：使用者審閱；接到新回饋再重開具體項目。原已採納TODO已完成，不留待下一輪。
- 工作記憶：course BEGINNER_VISUAL_TODO.md、BEGINNER_VISUAL_STATUS.md；驗證tmp/anomalydino-review-20260905/a14/final/report.json。
- 入口：http://127.0.0.1:8000/interactive-learning.html?rev=anomalydino-a14#view=lesson&lesson=ad-anomalydino&slide=1
- 本機docs已更新（1220資產）；未外部部署，沒有真人學習或現場推論驗證。下方早期狀態均為歷史。

## WI-004 — A13 外部建議修正

- 狀態：本輪第3／7章修正與驗證完成；整套仍需改善，使用者未核准。
- 已完成：EfficientAD裁字、PatchCore同源局部與特徵對應、正常對照三個設定距離，共6個SVG；正式topic、本機HTML與docs已整合。
- 驗證：HTML、4項回歸；16章與32閱讀視圖／放大／自測，34資產截圖與hash；本機bundle1212資產。
- 自評：本輪三組91／91／92，並非全套達標；第1／2／5／8章仍有≤90保留圖。
- 下一步：讀專用TODO／STATUS，先降低第1／5章手機跨段對照負擔；第8章找額外原始成功案例，不能以AI重繪或放大冒充證據。
- 產物：course tools/render_anomalydino_a13.py與資產a13-manifest.json；測試證據tmp/anomalydino-review-20260905/a13/final/report.json；持久逐項理由在TEACHING_REVIEW_LOG.md A13。
- 入口：http://127.0.0.1:8000/interactive-learning.html?rev=anomalydino-a13#view=lesson&lesson=ad-anomalydino&slide=7
- 未外部部署，尚無真人學習證據。下方WI-003為歷史版本。

## WI-003 — AnomalyDINO A10 學習循環

- 狀態：本輪重製與驗證完成；整套教材仍需改善，使用者未核准。
- 已完成：第2章手機模型／參考庫流程、第4章位置圖／算術共6個SVG；正式topic、本機HTML與docs已更新（1212資產）。
- 驗證：HTML、7項回歸、桌面1440／手機390共16章節與32閱讀視圖／放大檢查通過；34資產截圖與hash。
- 評分：整頁91，新改圖92–94；保留图仍有86–90，不能宣稱全部達標。
- 下一個具體動作：先修最終核對發現的第7章EfficientAD來源半截字，再補圖3正常候選比較與圖7代表特徵來源；讀專用TODO與共用log，延續既有授權，不重做已驗證的6張圖。
- 證據：`tmp/anomalydino-review-20260905/a10/final/report.json`；持久結論與逐圖分項在`TEACHING_REVIEW_LOG.md` A10最終交付；source/dependency hash在course `a10-*-manifest.json`。
- 入口：http://127.0.0.1:8000/interactive-learning.html?rev=anomalydino-a10#view=lesson&lesson=ad-anomalydino&slide=4
- 未外部部署；無真人學習或本機模型推論證據。下方WI-001、A11舊快照及早期checkpoint為歷史，不代表目前引用。

## WI-001 — AnomalyDINO A09 製作與工具驗證

- 狀態：工具驗證完成；視覺品質未全部達標，交接WI-003/A10。
- 已完成：ImageGen原型及正常參考素材，16組桌面／手機視圖，正式topic／教材整合、HTML及1212資產本機bundle。32個頁面視圖無JS錯誤，13項回歸＋最終3項聚焦／bundle檢查通過。
- 產物與來源：course `_course_content/generated-concepts/ad-anomalydino/`；持久prompt／來源在其 `a09-sources/`。詳見共用TEACHING_REVIEW_LOG.md最新A09收尾。
- 下一步：A10接續修正與重新評分；先核對正式topic，禁止用A09 renderer整批覆蓋A10。
- 品質：A11校準頁面90、部分視圖未達>90，保留需修正狀態，不因工具通過推定核准。
- 專用清單：[TODO](teaching-images/vision-ai-model-selection/BEGINNER_VISUAL_TODO.md)；[STATUS](teaching-images/vision-ai-model-selection/BEGINNER_VISUAL_STATUS.md)。證據在tmp/anomalydino-review-20260905/a09/，必要結論已寫回Markdown。未外部部署。

## WI-002 — 建立持久工作記憶

- 狀態：完成。
- 使用者要求：Codex 經常當機，將 TODO、進度與接續設計保存在 Markdown，並寫入 AGENTS.md。
- 已完成：建立本入口、加入 AGENTS.md 的逐步 checkpoint 規則、補上 A09 專用清單及 STATUS 接續紀錄。
- 驗證：檢查 Markdown 落盤、相對連結及關鍵檔案存在；僅文件變更，未執行教材測試。

## 新工作記錄格式

新增 `WI-003` 等穩定 ID，填寫：目標、授權範圍、狀態、專用清單連結（沒有則在此建立 checklist）、最後完成、進行中、下一步、產物與證據、驗收條件、阻礙、最後更新日期。保留已完成項目的簡短紀錄。

### 2026-09-05 即時版本核對（取代先前「尚未整合」摘要）
詢問是否上線時重新核對：正式 ad-anomalydino.json 已引用 A09；teaching-images/vision-ai-model-selection/interactive-learning.html 已包含 anomalydino-02-store_a09.svg，修改時間為 21:10:24；http://127.0.0.1:8000/interactive-learning.html 實際 HTTP 回應也包含該 A09 引用。因此本機頁面已更新；外網部署、本輪完整驗證及使用者核准尚未確認。先前未整合紀錄已落後於磁碟，不能再當目前狀態。下一步核對完整 A09 驗證證據與 bundle／外網狀態，再決定剩餘工作；不要重複整合。此次只確認回應文字含新版引用，未宣稱瀏覽器視覺驗收通過。

A10 最新checkpoint：6個新SVG已整合（僅第2章手機與第4章定位／算術）。下一步完成本機重建與本輪桌面／手機32個閱讀視圖、自測、放大和必要回歸；證據tmp/anomalydino-review-20260905/a10/integration.json。尚未外部部署。

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
WI-007：ViT注意力原型已實看，補實際value加權結果後繼續全題；其餘範圍不變。
WI-007分類組回查：同R-01共用四個實際操作視圖已接入ResNet8、ConvNeXt5、ViT5。發現R-01和V-01縱橫比不同時，外部框需跟隨圖片meet的留白；已修正attention來源標框。測試完成不代替逐圖教學評分，評分仍待最終校準。下一步U-Net用局部斷口與多尺度合併取代符號U形圖，全部八題仍執行。
WI-007下一步：U-Net第3圖原型，後展開與分割組學習；分類組已整合共同對照，最終逐項評分待完成。
WI-007接續：SegFormer第4章SR attention原型，後展開8章；U-Net E01已整合，既定八題範圍不變，尚未全套完成。
WI-007：接續YOLO-Seg原型/全題，後Keypoint R-CNN與Pose；前五题已改正式來源，但全套評分與共同回歸未完，不得結案。


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
# WI-013 R03 Sol re-review result and continuous loop (2026-09-06)

- Sol inspected actual R03 desktop/mobile PNG, SVG, and manifest.
- Scores: desktop **25/100**, mobile **18/100**; both fail. The PNG text is fallback blocks and overflows, so source-level fixes do not count as delivery evidence.
- New blockers: `CHAR-P0-10` unreadable raster text; `CHAR-P0-11` unverified hand-drawn marker; `CHAR-P1-12` unsupported P95/coverage mapping; `CHAR-P1-13` counterfactual manifest-only; `CHAR-P1-14` mobile overflow; `CHAR-P1-15` comparison wording not visibly explicit.
- Next Luna prototype: browser/Playwright with loaded CJK font and `document.fonts.ready`; OpenCV `CharucoBoard` plus named dictionary/detector verification; visible counterfactual; named coverage samples/cells or remove numbers; re-render and inspect both PNGs before Sol re-review.
- Status distinctions: implementation candidate exists; technical/visual validation failed; Sol review failed; user acceptance is not recorded. Formal topic remains R02 and must not be overwritten.
# WI-013 R04 Sol re-review and R05 handoff (2026-09-06)

- R04 actual PNG review: desktop **78/100 HOLD**, mobile **73/100 HOLD**.
- Passed: readable CJK font, generated `DICT_4X4_50` board with 24/24 detector IDs, visible counterfactual, REVIEW/HOLD gate, and explicit comparison.
- Fails: `CHAR-P1-16` broken `q↔P` notation; `CHAR-P1-17` no board callouts; `CHAR-P1-18` desktop truncation; `CHAR-P1-19` mobile crop; `CHAR-EVID-20` missing R04 manifest.
- R05 is assigned to Luna; preserve R04 and do not integrate formal topic until Sol passes actual PNGs. User acceptance remains unrecorded.
# WI-013 R05 Sol result: failed mixed render; R06 required (2026-09-06)

- Actual R05 scores: desktop **79/100**, mobile **72/100**, both fail.
- Partial desktop correspondence update does not offset stale R04 titles, remaining `qq/PP`, missing board callouts, desktop truncation, and mobile crop.
- `CHAR-EVID-21` added for version identity failure. Luna must rebuild from actual R05 source for R06; no formal integration, no user acceptance.
# WI-013 R06 Sol result: 85/86 HOLD; R07 final layout pass (2026-09-06)

- Sol scored desktop **85/100** and mobile **86/100**. All prior R05 issues pass except desktop bottom collision.
- `CHAR-P1-18`/`CHAR-P1-20`: provenance caption and c17 detector evidence collide at desktop panel edge. R07 moves or shortens provenance and raises evidence group.
- Formal topic and user acceptance remain pending; do not batch-integrate before every enabled image exceeds 90.
# WI-013 R07 Sol prototype pass (2026-09-06)

- R07 actual PNGs scored desktop **92/100** and mobile **92/100**; all tracked blockers pass.
- This is a Sol prototype pass only. Formal topic is not connected, and user acceptance is pending.
- Next: stage a versioned formal-topic integration candidate while preserving all prior revisions; Sol must recheck the actual page before any formal status change.
# WI-013 R07 integration candidate staged (2026-09-06)

- Candidate packet and topic JSON staged under `tmp/charuco-r07/`; formal `charuco.json` was not modified.
- Candidate references R07 PNG/SVG hashes and has rollback instructions. Sol must recheck candidate assets/page before any formal status change.
# WI-013 R07 integration failed; R08 mobile geometry fix (2026-09-06)

- Sol found candidate mobile geometry incompatible with the hardcoded page nested image (`720x1660` candidate vs `1672x941` page contract). Formal topic remains unchanged.
- R08 must fix candidate-only mobile mapping/geometry and add a machine-checkable contract; preserve R07 prototype and rollback.
# WI-013 R08 integration failed on packet/asset consistency; R09 required (2026-09-06)

- Geometry repair passed statically, but packet path, mobile metadata, and desktop evidence are inconsistent with actual rendered assets.
- R09 must normalize exact packet path, point quality metadata to PNG, and include desktop path/hash/dimensions before Sol recheck.

# WI-013 R09 integration packet normalization (2026-09-06)

- R09 candidate-only packet is authoritative at `tmp/charuco-r09/integration-packet.json`; an identical compatibility copy is at `tmp/charuco-r08/integration-packet.json`; R09 source is under `tmp/charuco-r09/`.
- Mobile quality metadata and reading view both reference the R07 mobile PNG; desktop packet evidence records the R07 desktop PNG, 1600x1080 intrinsic size, and SHA256.
- Static validation passed. Formal `charuco.json` and R02-R08 artifacts remain unchanged; browser runtime remains unavailable and Sol page recheck is pending.
- Next action: Sol performs static/integration recheck; do not mark formal acceptance or user acceptance.

# WI-013 R10 cleanup and final static gate (2026-09-06)

- R09 generated outputs no longer contain stale R08 labels; `.candidate-r09` is used in the R09 page/wrapper.
- Geometry rollback now names `tmp/charuco-r09/` as authoritative and lists R08 packet files only as compatibility copies.
- `R10_STATIC_INTEGRATION_GATE=PASS`; formal topic, R02-R09 history, and user acceptance remain unchanged. Browser runtime remains unavailable.
# WI-013 R09 integration blocked by stale version contamination; R10 cleanup (2026-09-06)

- Asset and hash consistency passed; integration remains blocked by R08 rollback text and `.candidate-r08` CSS selector in R09 candidate files.
- R10 must clean stale labels, recompute hashes, and obtain Sol recheck.
# WI-013 R10 final static integration pass (2026-09-06)

- Sol static integration gate passes after R10 cleanup: packet naming, stale-version cleanup, asset refs, hashes, dimensions, metadata, and rollback are consistent.
- Formal topic remains unchanged. Runtime browser validation is unassessed due unavailable browser; user acceptance is pending.
# WI-013 R09 promoted to formal topic and bundle rebuilt (2026-09-06)

- Formal `charuco.json` now uses R07 desktop/mobile assets for the first ChArUco visual; R02 backup preserved under `tmp/charuco-r09/`.
- Builder now supports the explicit 1600x1080 / 720x1660 R07 contract and full-mobile rendering. `interactive-learning.html` rebuilt successfully with 58 topics and 232 images.
- Live browser runtime remains unverified; user acceptance remains separate.
# WI-013 formal chapter re-review: 5→4 visual redesign required (2026-09-06)

- Sol rescored the actual formal chapter: images 60/78/79/85/81; chapter **67/100 fail**. Earlier R07 92 is withdrawn for formal style/continuity.
- Root cause: only first image changed, English-heavy 2x2 cards, 1600x1080 non-16:9 asset, no cross-image identity trace, and no consistent mobile assets.
- Luna must rebuild exactly four all-Traditional-Chinese, image-led C/D visuals under the new contract in `TEACHING_REVIEW_LOG.md`.

# WI-013 R11 visual 1 prototype (2026-09-06)

- R11 creates only the first D-type comparison prototype: same oblique/occluded scene versus pure chessboard, pure ArUco, and ChArUco.
- Real `cv2.aruco.CharucoBoard` with `DICT_4X4_50` generated and detector-verified 24/24 IDs; m17/m23/c17 are visibly tracked.
- Desktop/mobile PNGs were inspected with `view_image`; preflight and static board evidence pass. Formal topic and the other three visuals are unchanged.
- Next: Sol reviews this prototype; do not promote, batch-rebuild, or claim user acceptance.

# WI-013 R12 visual 1 physical-board correction (2026-09-06)

- R11 style direction retained, but R12 replaces the reused-board comparison with three distinct physical board diagrams under the same perspective/occlusion condition.
- Pure chessboard shows dense corners without local IDs; pure ArUco shows marker IDs plus marker corners with fewer samples; ChArUco shows marker identity plus interpolated chessboard corners.
- R12 desktop/mobile PNGs were inspected; OpenCV board evidence and preflight pass. Formal topic, R11, and visuals 2-4 remain unchanged.
- Next: Sol reviews R12 visual 1 only; no formal promotion or user acceptance claim.

### Sol R12 review result (2026-09-06)
- R12 is not passed: desktop 84, mobile 77. Three physical boards are now correct, but the header contradicts that fact, the ArUco corner-count wording is unsafe, the combine path is not visible, and 360px labels/body text are borderline unreadable.
- Next Luna action: R13 visual 1 only. Correct the four issues as `CHAR-R12-P0-01` through `CHAR-R12-P1-04`; do not modify formal topic or batch visuals 2-4.
# WI-013 R11 style prototype failed technical review; R12 correction (2026-09-06)

- R11 style direction improved, but Sol scored 81/77 because the comparison is technically misleading: reused ChArUco board and incorrect "ArUco has no corners" claim.
- R12 must use true board variants or explicit evidence-ablation labeling and correct OpenCV terminology.

# WI-013 R13 visual 1 wording/merge/mobile correction (2026-09-06)

- R13 is candidate-only and changes only visual 1; formal topic, R02-R12, and visuals 2-4 remain preserved.
- Corrected the header to `同一相機視角／同一斜視／同一遮擋比例，三種標靶`; replaced unsafe ArUco wording with marker-ID/local-recognition and marker-corner localization-precision wording; added thick evidence arrows into ChArUco.
- R13 desktop/mobile PNGs and native SVGs were regenerated and inspected, including a 360px-equivalent mobile preview. Preflight, OpenCV detector evidence, and static geometry/hash gate pass.
- Next: Sol reviews this candidate only; no formal promotion or user acceptance is claimed.

### Sol R13 actual-PNG result (2026-09-06)
- Sol 直接檢視 desktop、mobile 與 360px preview；固定量表 v1.0 分數為 **96/100**、**94/100**，R13 visual 1 prototype technical pass。`CHAR-R12-P0-01`、`CHAR-R12-P1-02`、`CHAR-R12-P1-03`、`CHAR-R12-P1-04` 均通過，無新 P0/P1。
- 非阻斷 `CHAR-R13-NB-01`：證據 JSON 尚留 `fewer corner samples` 舊字串；封存／整合前改成 marker-corner 定位精度敘述並重算 evidence/manifest hash，不需重畫已通過 PNG。
- 下一個具體動作：Luna 先清理證據字串，再製作 visual 2 的 C 型單一路徑原型，延續同一 camera/board 與 m17/m23/c17 到 q17/P17、PnP、predicted c17、residual。R13 未正式整合，整章未通過，使用者接受未記錄。

## WI-018 — 目前網站 Git check-in（2026-09-08）
- 目標／授權：依使用者「請先幫我 check in」，提交現有 Git 儲存庫的網站快照；不變更既有教材核准狀態。
- 範圍：teaching-images/vision-ai-model-selection，沿用只追蹤 docs/ 與 README 的設定；外層工作記憶與被忽略的原始檔不納入 commit。
- [x] 找到儲存庫並核對狀態：5 個已追蹤變更、526 個未追蹤網站資產。
- [ ] 即將執行：網站包驗證、暫存 docs/、檢查 staged diff、建立本機 commit。
- [ ] 驗收：commit 成功，Git 工作目錄乾淨；記錄 hash 與實際驗證結果。
- 下一步：執行 bundle 測試與 HTML verifier；尚未執行測試，尚未提交或 push。原教材工作 WI-017 保留。

WI-018 checkpoint：HTML verifier FAIL：charuco: invalid inline mechanism visual 1。保留現況提交，不在本次 check-in 擴大修圖。docs 暫存及 bundle 測試進行中；下一步完成暫存檢查後 commit。

WI-018 checkpoint：bundle unittest 1/1 PASS（70.241 秒）；HTML verifier 因 ChArUco inline mechanism visual 1 FAIL；staged diff 發現 ResNet 文件 EOF 多空白行。即將建立現況快照 commit；不改原圖與既有內容，未 push。

WI-018 完成 checkpoint（2026-09-08）：
- [x] 暫存及檢查現有 docs 快照，建立本機 commit c05f69b — Update teaching site snapshot and visual assets。
- [x] 提交 531 檔，1300 insertions、24 deletions；提交後 git status --short 無輸出，工作目錄乾淨。
- 驗證：bundle unittest 1/1 PASS；HTML verifier FAIL（charuco: invalid inline mechanism visual 1）；diff check 有 ResNet 文件 EOF 空白行。未跑完整回歸與新視覺審查。
- 範圍限制：未 push；外層 Markdown、被 .gitignore 忽略的教材 source 不在本次 commit。教材使用者核准維持 pending。
- 下一步：check-in 已完成，原教材 WI-017 接續與既有 ChArUco 驗證缺口保留，沒有因快照提交宣稱修復。

WI-018 push checkpoint：使用者明確授權 please push。已確認 main c05f69b 領先 origin/main 1 commit，工作目錄乾淨。即將執行 git push origin main 至 hctsaik/visionAI_Model_Introduce；驗收為遠端 main hash 與本機 HEAD 一致，尚未推送完成。

WI-018 push 完成：git push origin main 成功（3fef795..c05f69b）。[x] git ls-remote 確認遠端 main 與本機 HEAD 同為 c05f69b103190a5aa11c9a26c0d38317575777a2；git status --short --branch 為 main...origin/main，無未提交變更。下一步無待推送項目；GitHub Pages 部署狀態未驗證，教材既有驗證缺口與使用者審閱狀態不變。

## WI-019 — 13 課異常偵測公開網站重審與重建判斷（2026-09-08）
- 目標／授權：使用 teaching-review-cycle 重審使用者指定 13 課，提出逐課保留、局修或重建判斷與依據；本輪是審查及決策，不直接批量重製或發布。
- 範圍：ad-subspacead、ad-stfpm、ad-rd4ad、ad-ae、ad-draem、ad-uniad、ad-dinomaly、ad-invad、ad-diffad、ad-ddad、ad-winclip、ad-anomalyclip、ad-anomalygpt。
- 狀態：進行中；已讀 skill、量表 v1.0、五份規範相關段落、F01 歷史與閱讀層契約。
- 接續 checklist：teaching-images/vision-ai-model-selection/BEGINNER_VISUAL_TODO.md 的 WI-019；狀態同目錄 BEGINNER_VISUAL_STATUS.md；唯一評審紀錄根目錄 TEACHING_REVIEW_LOG.md。
- 即將執行：保存公開 HTML、13 課圖片槽及桌面／手機截圖、完整主線文字與來源核對。預期產物 teaching-images/vision-ai-model-selection/review-evidence/wi-019/。
- 驗收：逐課可定位問題與優點、重建程度／順序／驗證條件；未看的資產明列未評，不沿用 F01 高分、不宣稱使用者核准。
- 最後完成：Browser runtime 選取失敗，discovery 為 []，已讀 troubleshooting；改用 standalone Playwright 讀公開頁。尚未截圖／評分／重製；下一步擷取基線。

WI-019 checkpoint：13 課 desktop/mobile 公開頁擷取完成（capture.py exit 0）。公開 HTML SHA256 與本機 docs 相同；首讀共 65 圖槽。已實看前 8 課桌面主圖（SubspaceAD 至 InvAD），發現通用 h3 與圖義錯配、F01 與舊圖換工件、RD4AD 黑色工件區。尚未完成其餘 5 課與手機人工審查；下一步檢視 Diffusion／VLM 組及互動驗證。證據在 review-evidence/wi-019/，未改正式頁。
# WI-019 最新接續：審查收尾（2026-09-08）

- 已完成：13 課公開基準與資產 hash、65 張桌面首讀圖實看、26 張手機首兩圖實際 viewport 檢查；130 次放大開啟／Escape、26 次答案與下一課導覽檢查。公開 HTML 與 docs hash 相同。
- 即將執行：將逐圖量表評分、逐課重建建議及原始來源寫入共用 `TEACHING_REVIEW_LOG.md`，更新既有指南；正式教材未改。
- 證據：`teaching-images/vision-ai-model-selection/review-evidence/wi-019/`。手機放大首次 DOM 取樣早於圖片載入，正在補等載入確認，不能把早期 naturalWidth=0 判為破圖。
- 未完成／限制：隱藏正式 slide 圖未逐張實看；手機後續所有橫向區域未全面逐段評分；真人理解與使用者核准未取得。這是重建決策審查，不是全章驗收或新一輪產圖。

## WI-028 下一輪：時序八課與工程前提／量產頁（2026-09-10）
- 目標／授權：WI-027 學習寫回、commit＋push 後，用 Markdown 與 skills 建立附圖八題及兩個連結入口。
- 範圍：Frame Difference、Background Subtraction、Lucas–Kanade、RAFT、ByteTrack、ConvLSTM、VideoMAE、V-JEPA，以及 #view=production、#view=foundations。
- 狀態：已授權排入下一輪，尚未製作或測試；user approval pending。先完成 WI-027，不取消前輪七課。
- 接續入口：BEGINNER_VISUAL_TODO.md／BEGINNER_VISUAL_STATUS.md WI-028。下一步保存十個入口基準、讀權威與前輪學習、核對來源，再做逐圖 preflight／原型。
- 驗收：實際圖文生成／引用、逐圖及整頁證據、桌面手機互動／HTTP與必要回歸、學習落盤及發布核對。

- 最終Git核對：紀錄commit `9a5c147735ba56903be2bdc33fda7c78de9faaf4` 已push且遠端一致，137份已提交副本hash通過、工作目錄乾淨。網站內容commit c6c32a4已部署且公開檔案核對完成；後續紀錄提交沒有變更docs。
## WI-028 時序八課正式製作啟動（2026-09-10）
- 最新授權：依使用者截圖，製作 Frame Difference、Background Subtraction、Lucas–Kanade、RAFT、ByteTrack、ConvLSTM、VideoMAE、V-JEPA 八題；production／foundations 已由 WI-029 完成。
- 狀態：進行中；已核對工作入口、技能及五份權威的適用／最新段落，Git 工作目錄乾淨。尚未生成本輪圖、整合或測試；使用者核准 pending。
- 下一步：保存現版、實看首選參考、查第一手來源，建立逐圖 preflight，先製作代表原型。
- 接續與驗收：`teaching-images/vision-ai-model-selection/workitems/wi-028/PLAN.md`、BEGINNER_VISUAL_TODO.md／BEGINNER_VISUAL_STATUS.md；八課圖文、桌面手機審查、互動／HTTP及必要回歸、學習回寫與既有發布流程。

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

## WI-030 — 四個異常偵測與八個分類／分割／姿態Topic重作
- 使用者最新要求12課：PatchCore、PaDiM、AnomalyDINO、EfficientAD、ResNet、ConvNeXt、ViT、U-Net、SegFormer、YOLO-Seg、Keypoint R-CNN、Pose Pipeline。
- 狀態：WI-030實作、驗證及公開發布完成；內容commit c7d1533214fb832abbdaccc93b5ac88c06539ffd。使用者成品核准pending，歷史checkpoint保留如下。
- 接續唯一細項：teaching-images/vision-ai-model-selection/workitems/wi-030/PLAN.md。下一步依使用者成品回饋開修訂；不用舊自評代替回饋。
- 驗收：實際新版圖文、每張與每頁分項證據、桌面手機互動、HTTP／引用一致、學習回寫與既有發布流程。

## WI-030 接續 checkpoint（2026-09-11）
仍在十二課重作。已保存24現版截圖、來源與21故事preflight；十二課正文草稿完成，尚未整合。ResNet桌機手機原型自評92/91，其他圖逐版修正中，不能視為十二課完成。共享builder新增可選舊章收合，聚焦型別／章節保留測試1＋4subtests通過，整頁測試未跑。原生PNG、prompts、失敗原因與下一版在workitems/wi-030；下一步完成逐圖審查、整合引用、頁面驗證及發布。使用者核准pending。具體清單仍PLAN.md。

WI-030最新：九課本機來源已重作並建置，18故事候選審查完成。未發布，剩三課與整體QA。詳workitems/wi-030/PLAN.md；原始PNG/逐版prompt/原生與顯示尺寸審查持續落盤。


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

WI-030最終Git核對：紀錄commit 79364cf0fb82ed7c016092f30ba68771578bcb01 已推送並與origin/main一致，Git工作目錄乾淨。此commit只補公開驗證與接續紀錄，docs與已驗證內容commit c7d1533214fb832abbdaccc93b5ac88c06539ffd 完全一致。公開版本與必要文件核對完成；使用者成品核准仍pending。無待執行實作／測試／發布，下一步依成品回饋另開修訂。此本機最後核對見workitems/wi-030/git-sync-verification.json；Git歷史為紀錄commit的版本依據。


## WI-031 當前工作：全部58課 Markdown 標準審查
使用者要求重新看58課，列哪些符合、哪些需重建。本輪審查、判斷與文件落盤，不改教材；WI-030製作已完成。唯一細項與接續入口：teaching-images/vision-ai-model-selection/workitems/wi-031/PLAN.md。預期產物為58課總表、逐課缺口與證據、重建優先順序；以五份Markdown及量表v1.0為準，首讀與進階範圍分開。正在盤點現行版本並準備實際桌機／手機檢查；尚未完成全站審查，不能沿用舊分數判通過。下一步保存基準及擷取頁面。使用者核准不由自評推定。

WI-031 checkpoint：58課基準及644圖清單已保存；全站桌機手機擷取進行中。幾何4課已有首讀實看缺口，詳observations.md；其餘尚未完成審查。SVG object擷取與放大等待條件已修正，首次逾時不算網站錯誤。下一步續逐課實看、進階層與技術來源核對。

WI-031 checkpoint：58課、116桌機手機頁面擷取完成，另補兩課inline SVG手機8圖；公開HTML與本機一致、644圖片HTTP可達。以上是擷取及可達性，不等於644圖人工合格。已實看幾何4、分類8、偵測6、異常前7課主線與4張工程圖；AE正在完成。初步多數新版主線可保留，舊工程圖有模板化與機制不明缺口；ChArUco/ECC/SIFT/LightGlue及DINO detector/YOLO-World主線需重建。五課深讀章節尚未完成。下一步完成其餘33課及深讀，形成58課總表；教材未修改，未發布。詳observations.md。

WI-031 checkpoint：已完成人工審讀50課主線與各4張工程圖，最後8課生成／復原進行中；DefectFill主線與工程圖已看，AnomalyDiffusion剛開始。五課深讀章節待審。116頁擷取已完成，沒有長批次程序仍在執行。各課具體發現見observations.md；下一步完成8課、檢查深讀及共用版面，輸出58課分類與重建範圍。教材與發布版本未修改；未將擷取完成或HTTP200視為人工合格。

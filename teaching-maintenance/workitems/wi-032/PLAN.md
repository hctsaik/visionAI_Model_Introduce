# WI-032 第一部分：六課重建

- 目標：執行Overall_Review.md第一部分，重建ChArUco／ECC／SIFT／LightGlue／DINO detector／YOLO-World主線及其受影響工程圖。
- 授權：使用者明確要求先記錄兩部分與本輪學習，再執行第一部分。第二部分52課待辦不啟動。完成本機生成、整合與驗證；使用者成品核准pending。
- 規格：五份權威Markdown、量表v1.0與teaching-review-cycle G0–G6；保留有效實測，不把新示意當真實推論。
- 基準：WI-031 baseline與本工作item/baseline；開始製作前核對當前來源。
- 下一步：本輪必要製作／驗證完成；依使用者審閱處理回饋。第二部分與發布待後續指示。

## Checklist
- [x] 建立根Overall_Review.md，列6課及52課全部範圍。
- [x] 保存本輪審查學習與下次驗證方式。
- [x] 保存6課來源基準、核對權威與第一手技術來源。
- [x] 逐圖brief／preflight通過，完成代表原型實圖審查。
- [x] ChArUco圖文、自測、工程層重建及實圖檢查。
- [x] ECC圖文、自測、工程層重建及實圖檢查。
- [x] SIFT圖文、自測、工程層重建及實圖檢查。
- [x] LightGlue圖文、自測、工程層重建及實圖檢查。
- [x] DINO detector圖文、自測、工程層重建及實圖檢查。
- [x] YOLO-World圖文、自測、工程層重建及實圖檢查。
- [x] course/docs整合、6課桌機手機、放大／自測／導覽／文件連結與相關回歸。
- [x] 各圖及整頁分項證據、hash核對、學習回寫與總計畫狀態更新。

## Checkpoint
最新：ECC桌機／手機原生已看，DINO桌機原型已看；未頁內驗證。ChArUco r01/r02都未通過同角點身份與棋盤格位核對，停止同式生成；下一版改精確原生幾何圖，防止生成器重畫棋盤造成錯誤。其他主線按已驗證敘事續作SIFT/LightGlue/YOLO-World核心與ECC反例。未整合、完整測試未跑；所有user approval pending。
ECC core原型已生成並原生自評93，頁內／手機尚未驗，未啟用，user pending。14組主線brief已通過preflight-validation.json。即將生成charuco-core與dino-core桌機原型，預期同名r01-desktop.png；先檢查校正／姿態與訓練／推論分流，通過才展開對應圖。
2026-09-11：計畫與學習已落盤，正在讀製作規則及準備原型；未生成，未整合，測試未跑。成品自評未評、使用者核准pending。無已知阻礙。

即將執行：ECC core r01桌機單圖原型，built-in imagegen，依ecc-core-r01.md已通過preflight，GEO-02/GEO-21已實看。基準15檔已保存。預計產物ecc-core-r01-desktop.png，完成後先逐圖審查，再決定手機與其餘圖；目前未生成／未啟用／未評分，user approval pending。

WI-032最新checkpoint：Overall_Review.md已列第一部分6課、第二部分52課與學習；6課完整正文／自測草稿已保存lesson-content.json，15檔基準與14組主線brief已保存。ECC核心桌機手機、DINO核心、YOLO-World核心等候選已生成實看；ChArUco兩次生成角點失敗後改精確SVG，r05已產出待頁內核對。SIFT/LightGlue點位與ECC反例仍在修正，不把候選當完成。其餘反例／比較正在製作，工程4圖尚待重建；尚未整合教材，測試未跑，未發布，user approval pending。下一步完成主線候選與精確幾何修正，再重建工程層、整合和實頁驗收。產物在workitems/wi-032，詳細原生審查見prototype-review.md。


WI-032 checkpoint：兩部分58課與本輪學習已在Overall_Review.md。6課正文／自測草稿已保存；主線桌機／手機候選持續審查。ChArUco固定棋盤、SIFT/LightGlue固定點、ECC整件一致平移改用原生SVG→PNG；native-r03發現標題間距、張數對照及含糊線標示問題，r04已修正待完整核對。偵測手機r01仍過密，r02減字放大；反例r03簡化。所有舊稿保留，沒有把候選當通過。工程4圖尚未製作、教材尚未整合、整頁及回歸未跑、未發布、使用者核准pending。下一步完成主線原生審查，製作工程層並整合驗證。

## 整合checkpoint（最新）
六課主線28個PNG、工程48個PNG及6課新正文／自測已接入topic／learner／model.md／manifest；builder新增僅指定課程的手機工程圖與可捲動放大。ECC舊工程4原圖仍保存並新增閱讀連結。第一次建置被既有「learner brief too long: charuco」驗證攔下，HTML仍舊版，尚未跑頁面與回歸；下一步縮短首讀操作摘要，完整說明留本課正文，再建置與實頁核對。禁止把已整合或PNG存在當完成；user approval pending，未發布。

## 實頁檢查checkpoint
course與docs已建置；ChArUco/ECC/SIFT各4個桌機／手機URL狀態及28個放大檢查通過，其餘3課檢查中。12個focused tests與14 subtests通過。實看手機圖片後發現截圖被sticky導覽列覆蓋，這是長圖元素截圖的固定介面混入，將另存不含導覽列的圖框證據；正常頁面與互動截圖保留。展開舊技術契約有SIFT warp等舊用語，正在改為新版教學來源供給交付與家族摘要；修正後重建及核對。主線三要點移除第四個交付列（交付仍在操作卡）。未完成項目：全部圖文人工評分、更新後頁面與資產驗證、回歸及學習收尾。

## 驗證與來源checkpoint
修正版已通過14 tests及130 subtests；六課第二輪24頁狀態檢查接近完成。新增歷史R06來源連結：4個PNG原樣複製到formal目錄，保留SHA；原圖標示非實測，sources.md已釐清。這次僅補來源連結及model.md，不改新圖。即將重建bundle，檢查新增連結、scope、HTTP/hash與最終評分；user approval pending。

## 最終圖像修正
24個第二輪頁面／168放大／24自測及導覽通過；18個390px deep-link、前後張與舊課fallback通過。1351資產course/docs hash相同、186 HTTP hash通過，6課改動、52課資料不變。實圖重評發現World工程3仍偏部署文字方框，r07新增詞彙轉1×1分類頭參數及特徵→分數可見路徑；官方來源已核對。即將實看此2張、重建並重驗該課；共用工程展開標題也改為符合實際內容。其他新圖不變。

## 最後驗證補充
64個啟用原生SVG檢查初報ChArUco核心2圖panel外溢；實圖正常。檢查器把第三節點內的小殘差框當成整節點背景，造成誤報。已保留svg-layout-false-positive.json，修正只辨認大型節點背景；畫布檢查仍對全部文字執行。不修改圖片，也不把該次failed寫成passed。390px來源鏈結初測另因測試工具以相對URL呼叫APIRequestContext失敗，已改用a.href絕對URL並重新通過18狀態。

## 收尾checkpoint
六課主線、工程4圖、手機版與交付已重建，76張新PNG已逐圖及整頁自評；14 tests／130 subtests、24主頁狀態／168放大與18補充390px及舊課回歸已通過。正在保存最終報告、資產重新核對與維護來源快照。第二部分52課未啟動，未發布，使用者成品核准pending。下一步：完成final-verification.json與維護快照一致性，將Overall／PLAN及本入口結案。
64個啟用原生SVG畫布／大型節點文字邊界檢查通過；38份選定故事brief通過preflight。每圖完成度五項有理由，圖片分數不可借用頁面正文或測試成功。


## 最終完成狀態
WI-032第一部分六課本機重建、自評與必要驗證完成。Overall_Review.md已分列6課／52課；本輪學習已回寫三份權威Markdown。76張新PNG（28主線＋48工程）及正文／自測／交付已啟用；24主頁狀態／168放大、18補測狀態、14 tests／130 subtests通過，1351資產hash一致，52課payload不變。報告：teaching-images/vision-ai-model-selection/workitems/wi-032/REPORT.md。無未完成必要實作或驗證；使用者成品核准pending，未commit/push/發布。下一步：依使用者審閱處理回饋；第二部分52課等待後續指示。
基準22份來源備份保留；原型及失敗稿未刪。完成的是本機實作、自評、驗證与文件，沒有使用者成品核准。

## 最終HTML序列化核對
收尾重建因Python set欄位迭代次序而產生不同JSON鍵順序；全部解析資料（含58課）及移除JSON後的HTML模板完全相同。沒有教材或UI差異。已保留實頁驗證過的序列化版本並同步course/docs，兩URL HTML HTTP SHA256再次一致；詳見final-verification.json final_html_freeze。這不是內容回退，也未改動其餘52課。必要驗證均已完成。

最後文件核對：Overall／REPORT共21個本機連結、76個逐圖證據路徑及最終HTML hash通過；Overall第一部分6列完成、第二部分52列待執行。git diff --check通過（僅Windows換行提示）。

## WI-032-P 提交與發布（2026-09-11）

使用者明確授權「繼續 commit + push」。範圍為已完成第一部分六課、審查與學習、第二部分接續紀錄；不開始第二部分。即將同步 Git 內維護副本並檢查提交清單，避免根目錄 Markdown 只留本機。

- [x] 同步最新來源與學習副本，核對已驗證 HTML、資產與提交差異。
- [ ] Commit 並 push main，核對遠端 SHA。
- [ ] 核對 Pages 結果與公開內容，保存發布證據及接續狀態。

目前提交／發布未執行；既有 14 tests／130 subtests 通過，這次未改教材，不重新建置已固定的 HTML。下一步同步與提交前檢查。使用者成品審閱與發布授權分開。

提交前 checkpoint：已確認 course／docs HTML 與實頁驗證 hash 相同，985 份維護 manifest hash 通過；4 張未引用候選保留到 unused-publish-candidates，未刪除。git diff --check 通過。GitHub CLI 未登入，因此發布狀態將以公開 API 核對；Git push 使用既有 Git 認證，不輸出憑證。即將提交 docs 與 teaching-maintenance。

## WI-032-L 學習補記（2026-09-11）

### WI-032-H 下次接續交接（2026-09-11）

使用者要求記住目前進度，之後再請接著做。目標與授權：保存接續位置並查核 Git 狀態；本次不啟動第二部分。

- [x] 核對本機 Git：第一部分成果仍有已修改及未追蹤檔案，尚未全部 commit／push。
- [x] 將「第一部分本機完成，下一次開始第二部分 52 課局部修正」寫入工作入口與 TODO／STATUS，核對落盤。

完成證據：三個入口均以 UTF-8 實讀核對，WI-032-H 接續段落存在。git ls-remote origin refs/heads/main 與本機 HEAD 均為 79364cf0fb82ed7c016092f30ba68771578bcb01；git status 仍有第一部分修改及新增檔案。接續紀錄已本機保存，未 commit／push。此輪未變更教材，未重跑網頁測試，無阻礙。

下一個製作動作：收到使用者接續指示後，先讀根 Overall_Review.md 第二部分及 WI-031/REPORT.md，核對當前正式引用和未提交成果；建立第二部分專用工作項及分批 checklist，優先修正會教錯的語意關係。第二部分目前零課完成，不能把「做到第二部分」記成第二部分已完成。先前 40–80 小時僅粗估，首批完成後依實際耗時校準。

驗收：三個持久入口均明確指向第二部分；Git 狀態與遠端核對如實記錄。第一部分使用者成品核准 pending；不將本次進度詢問視為發布指示。

使用者再次要求將學習保存為 Markdown。本次授權為整理本輪既有證據、補足可重用原則與接續入口；六課製作完成狀態不變。

- [x] 核對既有共用學習紀錄、最終完成狀態與 HTML 序列化核對紀錄。
- [x] 在共用 log 補齊「觀察 → 規則位置 → 下次驗證」，補記最後版本固定的學習。
- [x] 更新網頁指南及 WORKITEMS／TODO／STATUS，核對 UTF-8 與證據連結。

Checkpoint：既有八項重建學習已存在 TEACHING_REVIEW_LOG.md；正在補記最後收尾發現及下次驗證方式。預期產物為共用 log、網頁指南及接續 Markdown，不另建第二套規則。驗收為新增紀錄有可定位證據、連結存在、狀態不混淆。文件檢查尚未執行，無阻礙。

完成 checkpoint：共用 log 已補六項「觀察／規則位置／下次驗證」及 HTML 版本固定的學習，共用網頁指南已同步。6 份 Markdown UTF-8 檢查、4 個新增證據連結及既有 final_html_freeze 證據核對通過；git diff --check 通過（僅既有 HTML 換行提示）。首次用 PowerShell 管線寫入三個入口時中文轉成問號，實讀發現後已用 apply_patch 修復並再次核對；後續中文文件應直接以 UTF-8 檔案或 apply_patch 寫入，不能只看命令成功。此次未重跑網頁測試、產圖或模型推論。無阻礙；下一步依使用者後續指示接續。六課製作完成與使用者待核准狀態不變。

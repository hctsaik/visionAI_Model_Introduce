# WI-042 定版修正與發布

目標／授權：依WI-041審查完成六課文字與維護驗證器修正，使用者明確授權commit＋push；發布後核對公開成品並給定版判斷。

基準：2c4cb73，HTML43c3557a。既有產品工作目錄乾淨。本輪不新增功能或重畫，沿用需求流程契約，不需新增OpenSpec能力。

- [x] 修正六課mechanism title/body/why及DiffusionAD相關操作文件，主線與工程參考一致。
- [x] 對齊全站verifier與目前原生圖片／schema／需求助手契約，增加有意破壞資料的回歸驗證。
- [x] 建置course/docs，核對有限變更、必要測試、六課桌面手機實頁與圖片。
- [x] 保存學習與可恢復maintenance快照，commit＋push。
- [x] 核對公開HTML與六課修正、公開需求流程，記錄最終定版判斷。

即將執行：保存基準、修文字及verifier；預期產物authoring-diff、驗證log、12課頁截圖、公開release-verification與REPORT。尚未修改、測試未跑、未發布，使用者成品核准pending。下一步先完成文字和schema修正。

????checkpoint?30tests?146subtests?15???????verifier/????10tests?11subtests?????source/docs???????PASS????????12?????title/body/why??????????JS??????????????HTML139d466d??????mechanism_steps????????commit/push??????????pending?

最終發布checkpoint：六課修正與新版verifier完成並公開。內容commit 592d5c5已push，公開HTML 139d466d與docs相同；六課12個公開桌面手機實頁及需求流程通過。本機30tests+146subtests、15規則、verifier補驗10tests+11subtests及source/docs總驗證通過。WI041必修已關閉，建議本版定版；使用者成品核准仍pending。

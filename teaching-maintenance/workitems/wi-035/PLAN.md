# WI-035 教材語義修正與 PoC 互動改善

目標：修正 WI-034 成立的文字錯位，讓 PoC 從攤開表單變成可往返、能核對成果的三步引導，將學習寫回 Markdown。
授權：使用者明確要求修改教材與指定 PoC 頁、記錄學習；沿用現有架構，本輪實作與本機驗證。成品使用者審阅 pending。
基準：358fefe；WI-034 REPORT.md。保留既有圖片與有效問答，修改真正來源並重建 course/docs。

- [x] 保存公開頁／本機基準、互動規格與學習；完成預檢。
- [x] 修正機制標題與內文、標籤、收束、卡片引導與可見繁簡文案。
- [x] 實作 PoC 三步引導、模型提示、完整度、預覽、Markdown 匯出與草稿保護。
- [x] 驗證桌面／手機、往返／重載、匯入／匯出、列印與既有課程回歸；修正實測缺口。
- [x] 同步 Markdown 學習、維護副本與交付證據。

互動規格：三步均可直接返回；不強迫填滿才能下一步。欄位內容留存於既有瀏覽器草稿；完成度僅表示填寫程度，不表示模型通過驗收。選模型显示該模型交付與限制，可明確帶入空欄。範例／操作卡不靜默覆蓋已填內容。預覽全部欄位，列印完整文字；下載獨立 PoC Markdown，同時保留舊 JSON 匯出匯入。儲存失敗須誠實提示。保留舊草稿相容性。

驗收：上述操作皆有瀏覽器行為測試；小螢幕無水平溢出、欄位標籤與按鈕可讀；修正欄位在編譯後與實頁相符。未變動圖片沿用可確認的 WI-033 證據；本輪不新增模型推論。

Checkpoint：即將保存基準並開始修正。未跑測試。預期產物：本目錄 before/after 截圖、驗證 JSON、REPORT.md；來源 tools/build_interactive_learning_html.py、_course_content/topics/*.json；輸出 interactive-learning.html、docs/index.html。內建 Browser 無可用連線，改本機 Playwright 測試。

實作與必要驗證完成，詳 REPORT.md／final-verification.json。25 項相關測試通過；舊全站 verifier 的既有 schema 問題於基準重現並記錄，不算本次產品退化。下一步依先前 Git push 授權提交並確認公開頁；成品使用者審閱 pending。

最終 checkpoint：ce52c34 已 push 並部署成功。公開 HTML 與本機 SHA-256 一致；公開桌面／手機操作通過，見 release-verification.json。授權修改工作完成，沒有尚待實作項目；使用者審閱 pending 與完成狀態分開。

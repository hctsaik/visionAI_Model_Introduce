# WI-035 教材文字與 PoC 互動改善

2026-09-12。基準 `358fefe`，本輪使用者要求「修改並將學習放進 Markdown」，以及改善公開 PoC 頁互動。實作與本機驗證完成；Git／公開部署狀態以本目錄 RELEASE.md 為準。成品使用者審閱仍 pending。

## PoC 現在怎麼用

1. 現場問題：寫下要解決的工作及期待輸出，可先帶入晶圓 AOI 範例。
2. 比較方法：填資料與目前做法，搜尋候選模型；選定後顯示模型交付與限制，可只補入空白欄位。
3. 驗收與交接：寫下驗收指標、停止條件與負責角色，再預覽完整草稿。

各步可往返或留白，顯示已填數與可點選的待補項目。草稿自動保留；範例／課程操作卡帶入前保護既有內容，並可撤銷。完整預覽支援 Markdown 下載、列印／PDF；舊版 JSON 與七欄草稿仍可使用。新增 baseline／owner 兩欄，舊草稿不會憑空補成已完成。儲存失敗會提示先匯出。只清 PoC 與清全部學習資料分開。

完成度只表示已填寫，不宣稱答案正確、模型通過驗收或現場已實測。

## 教材修正

- DINO：分開訓練真值、正負去噪訊號與一般影像查詢初始化；第三頁標籤改為訓練主題，PoC 比較步驟改為可執行行動。
- 15 課 foundation／diffusion：第一個機制步驟改為各課輸入、處理與機制；LLaVA、SigLIP、ControlNet、inpainting、超解析等另核對後續步驟。
- ResNet：輸入、殘差兩路、分類接手的標題與內文重新配對。YOLO-World：詞彙表示、影像文字互動與出框分開。YOLOE：移除錯欄的突兀 LRPC 解答，保留有效問答及各提示模式說明。
- 六課偵測：統一卡片引導的功能，明確寫有條件的選型收束，保留新版各自不同的第 3／4 頁問答。
- 修正已確認繁簡混用，移除學生文案中的製作版本註記。詳見 content-changes.json；不是對全部歷史文件做盲目字形替換。

共 19 課機制文字修正；全 58 課編譯後 summary 等於 mechanism step0 的項目從 15 降至 0。未重畫已正確的 PNG，啟用圖像維持既有版本。

## 驗證與限制

- PoC 真實瀏覽器行為：8 項 × course/docs 兩入口，共 16 項通過，涵蓋往返、重載、模型搜尋與提示、草稿保護／撤銷、JSON 往返、Markdown 長文、列印可見完整文字、手機鍵盤與儲存失敗。
- 3 項導航、2 項 bundle、4 項工程資料測試通過，共 25 項相關測試。
- 19 課 × 2 入口共 38 路由展開核對；20 張 PoC 桌面／手機截圖，390px 無水平溢出。五課因果鏈截圖已人工檢視；PoC 桌面編輯／預覽與手機編輯／預覽已實看。
- 1370 個發布資產來源／docs SHA-256 相同，兩份 HTML 位元一致。最終 HTML：`f4f6600448e80275e046fa57b61bc26a28b4649f5ab34f8d6e80b1887d3d20fb`。
- 舊 `verify_interactive_learning_html.py` 不接受 WI-033 已存在的 engineering_slides，於 charuco 失敗；已對 `358fefe` 重現同一失敗，保留 test-html-baseline.txt，未改教材迎合過時契約。以現行 builder schema、資產雜湊、相關回歸與瀏覽器實頁檢查補足本輪驗證，沒有宣稱所有歷史測試通過。
- PoC 範例 PDF 已生成；長文列印以實際 print media 預覽測試驗證。未新增模型推論、現場驗收或真人學習成效試驗，不以自評分數代替使用者審閱。

證據：final-verification.json、content-validation.json、test-results.json、test-*.txt、page-checks.json、after-*.png、poc-example.pdf。截圖與 PDF 保存在本機；可追溯結論、來源與測試紀錄納入 teaching-maintenance。

## 學習寫回

根 TEACHING_WEBPAGE_GUIDE.md 的 WI-035：欄位語義、真正步驟互動、草稿保護、完整匯出、儲存失敗及 blur 重畫吞點擊的實測回歸。

根 TEACHING_REVIEW_LOG.md 的 WI-035：觀察、原因、適用條件、修正與實際驗證。FAILURES-AND-LEARNING.md 保留首次 schema、點擊與收束覆寫失敗。安裝的 skill 未更改；本輪要求的 Markdown 學習已實際寫回並有維護副本。

## 接續與維護

權威來源是完整工作區 `_course_content/topics`、learner-briefs.json、poc-workbench.js/css 與 tools/build_interactive_learning_html.py。先建 HTML 再建 docs。

Git 儲存庫為發布包與維護快照；本輪目前來源快照在 `teaching-maintenance/workitems/wi-035/authoring/`，覆蓋相對路徑到完整工作區後再建置。歷史 WI-033 快照保留，不當成最新來源重跑。共用指南仍以根 Markdown 為編輯權威。

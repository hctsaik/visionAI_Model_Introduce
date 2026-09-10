## WI-032 發布完成（2026-09-11）

第一部分六課成果已 commit 並 push：2e218926e2ff5d1a8d21ca5cb7bbe381fde27819；GitHub Pages 部署成功，公開 93 個檔案逐一 hash 與已提交內容一致（本機部分 Markdown 為 CRLF，Git 為 LF，文字內容一致）。發布證據為 workitems/wi-032/public-release-verification.json。最新學習及接續資料同步保存在 Git 的 teaching-maintenance。使用者成品核准仍 pending；第二部分 52 課未開始，下次依根 Overall_Review.md 第二部分接續。此段取代下方歷史未發布狀態。

# WI-032：第一部分六課重建完成

狀態：本機實作、自評與必要驗證完成。使用者成品核准仍為pending；未commit、push或發布。第二部分52課未啟動。

本輪依根Overall_Review.md執行；五份權威Markdown及v1.0量表未放寬。新內容涵蓋每課核心原理、具體反例、方法比較、自測、操作交付，以及四張工程圖的桌機／手機版本。

## 逐課結果

| 課程 | 新版重點 | 整課自評 | 本機頁面 |
| --- | --- | --- | --- |
| ChArUco | 同棋盤角點、多視角校正／已知內參姿態分開、邊角反例 | 92/100 | [開啟](../../docs/index.html#view=lesson&lesson=charuco&slide=1) |
| ECC | 取樣與相關更新、warp方向、局部錯解及獨立殘差 | 92/100 | [開啟](../../docs/index.html#view=lesson&lesson=ecc&slide=1) |
| SIFT | 尺度方向與梯度描述、ratio、四組非退化點對與視差 | 92/100 | [開啟](../../docs/index.html#view=lesson&lesson=sift&slide=1) |
| LightGlue | 相容extractor、圖內／跨圖關係、未匹配及自適應計算 | 91/100 | [開啟](../../docs/index.html#view=lesson&lesson=lightglue&slide=1) |
| DINO detector | 訓練專用正負去噪、mixed query、推論輸出與遮擋 | 92/100 | [開啟](../../docs/index.html#view=lesson&lesson=det-dino-detector&slide=1) |
| YOLO-World | 詞彙與影像互動、區域比對、快取／分類頭重參數化及取像限制 | 92/100 | [開啟](../../docs/index.html#view=lesson&lesson=yolo-world&slide=1) |

自評不是使用者核准或真人學習成效。逐圖91–94分、整課91–92分；手機長捲動、次要圖例較小、部分結構簡化，以及沒有同硬體現場比較，都明列扣分或限制。

## 圖片與來源

- 38個故事、76張新PNG：主線14組桌機／手機共28張，工程24組桌機／手機共48張。工程圖沒有與主線PNG重複hash。
- 相同幾何／偵測比較圖按hash共用，各課位置與圖說另驗。
- ChArUco與其他幾何圖採新建精確SVG；偵測主線與ECC核心使用內建imagegen。生成意圖、各版brief、失敗稿及修正保存在本工作項目，見[原型審查](prototype-review.md)。
- R06四張歷史示意原樣複製，另保留ECC舊工程4連結；不把舊數字或照片當成新模型實測。見[來源界線](sources.md)及[保留檔hash](retained-evidence.json)。

## 實際驗證

| 檢查 | 結果 | 證據 |
| --- | --- | --- |
| 桌機1440／手機360，course與docs | 24頁狀態、168次放大解碼／Escape、24自測、24導覽 | 每課pages目錄/report.json |
| 390px深連結與放大前後張 | 18狀態，含ResNet／RAFT／PatchCore 6個舊課fallback狀態 | [final-smoke.json](final-smoke.json) |
| 資產與來源 | 1351資產course/docs hash一致；186 HTTP hash，最後12份交付文件另做24次HTTP重核 | [final-verification.json](final-verification.json) |
| 範圍 | 6課payload更新，52課payload與基準相同 | [final-verification.json](final-verification.json) |
| 必要回歸 | 14 tests、130 subtests通過 | [test-results.json](test-results.json) |
| 製作前檢查／原生邊界 | 38份選定brief通過；64 SVG文字畫布／大型節點邊界無最終錯誤 | [preflight](selected-preflight-validation.json)、[SVG](svg-layout-check.json) |
| 人工審查 | 76張圖逐項評價、6課整體評價 | [image-assessment.json](image-assessment.json)、[page-assessment.json](page-assessment.json) |

圖框截圖排除固定導覽列，僅用於讀图；top、handoff與放大截圖保留實際介面。兩類測試工具誤報及初次建置失敗保留於[PLAN歷程](PLAN.md)，沒有算成通過。

## 本輪學習與接續

共用學習已回寫根TEACHING_REVIEW_LOG.md、IMAGE_STYLE_GUIDE.md、TEACHING_WEBPAGE_GUIDE.md及Overall_Review.md。第一部分具體修正：同物件幾何、手機斷詞／密度、訓練與推論角色、交付文字與新圖一致、可見重參數化，以及舊證據等級重核。

第二部分52課仍依Overall_Review.md逐課記錄，沒有開工。當下沒有必要實作／驗證阻礙；下一步依使用者審閱結果處理第一部分回饋，或依後續指示開始第二部分。發布及使用者核准均沒有被預設完成。

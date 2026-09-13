# WI-041 PoC 獨立重新審查

2026-09-13。產品唯讀，沒有 Git 或發布。主 Agent 負責共享狀態。

## Checkpoint

- 已重新閱讀現行 poc-decision.js、poc-workbench.js、docs/index.html 的保存／還原實作及全部 PoC 測試。規則 15 項已重新通過，包含完整可達路徑枚舉。
- 第一次使用舊 8000 server：hardening 前五項通過，最後舊備份測試遇到 ERR_CONNECTION_REFUSED；這是服務中途停止，不是合法備份被拒絕的產品證據。保留 recheck-reliability-* 原始失敗紀錄。
- 即將／正在以獨立 8014 server 完整重跑，HTTP bytes 與現行 docs/index.html 一致，SHA-256 43c3557afba4300ad67425bdaba432e0a3582a14e227af0144711db1c0e75e28。
- 最終測試尚未完成；不可用舊 reliability-review.md 當本輪通過。下一步確認 recheck-reliability-attempt2-* 全部結果及額外 dirty-save/stale-branch 檢查後更新本檔。

- 8014 重跑進展：15 規則 + 6 hardening 全數通過（含合法 v1/v2、9 類錯檔、取消、storage failure rollback）；13 PoC 與追加交互檢查進行中。

## 獨立審查裁決

現行需求助手、方法推導、草稿保存與備份還原，未發現需要阻止定版的新問題。判定限於教學選型與小規模試做規劃；不等於現場模型準確度、硬體速度或量測精度已實測通過。

## 新證據

- recheck-reliability-attempt2-rules.txt：15 項 Node 測試通過，包括完整可達答案路徑、不確定條件、缺資料、不良取像優先、真實課程 ID 與無效／殘留答案不污染分支。
- recheck-reliability-attempt2-hardening.txt：6 項瀏覽器測試通過；包含 9 類錯檔、合法 v1/v2、現版備份往返、取消不更動、儲存失敗回滾、桌面手機首頁入口。
- recheck-reliability-attempt2-poc.txt：13 項瀏覽器測試通過；包含六情境子案例、generation／unknown、上一題改答案、reload、舊稿、Markdown／print media、JSON 往返、reset／undo、範例取消、storage failure、手機鍵盤與課程筆記。
- recheck-reliability-evidence.json：本輪追加 dirty-selection/reload、未 blur 交接文字立即下載／重整、dark theme 往返、stale branch import 均通過、page_errors 為空。該檔 hardening exit 1 是第一次 server 中斷，已由 attempt2 完整通過反證。

## 關鍵前提再核對

1. 固定格位先比較簡單規則；任意擺放先定位每件；方法優先於模型選擇。
2. 新異常篩查要求真實獨立異常測試；熱圖不當作精密輪廓。
3. 逐件與整片區域分割區分；重疊看不到的邊界不得假定有真值。
4. 毫米量測需要尺度與校正；不同高度不能直接共用平面換算。
5. 影片偵測、追蹤、事件規則為不同步驟；即時要求完整流程延遲實測。
6. 逐字抄錄先 OCR，即使本站無 OCR 專課也不誤導至 VLM；生成圖不當現場證據。
7. 匯入先驗證格式再確認取代；保存失敗回滾；舊課程筆記不參與新方法推導。

## 可以接受的限制

- 全路徑執行並非每條答案組合逐一人工評分，也不是全瀏覽器／硬體／列印機實測。
- 暫存限目前瀏覽器；跨裝置依賴 JSON，單次 undo 不等於版本歷史或雲端協作。
- 未對同時多分頁改稿提供合併保證，本輪不新增此產品範圍。

## 下一版選配

最值得觀察的是使用者是否能把待驗證方向落成可交接的小實驗。現行 pocPlanSections 產生方法、原因、待確認條件、小規模驗證，現場目標／負責人放在一個選填文字欄。若實際試用者常漏填，可提供一個具體完成範例，提示填入資料批次、現行基準、允收門檻與人工接手方式。這是降低交接遺漏的改進，現有畫面已明示並非上線結論，因此不列為定版必修。

未修改產品，未發布，使用者核准仍 pending。主 Agent 統一整合最終 REVIEW.md。

## 最終 checkpoint

8014 attempt2 全部完成：15 規則、6 hardening、13 PoC、追加未按繼續保存／交接立即下載／深色主題／殘留分支均通過，無 pageerror。完整證據 recheck-reliability-attempt2-evidence.json。先前進行中描述為歷史 checkpoint，已被本項完成證據取代。PoC 審查無未完成測試或定版阻礙；後續由主 Agent 整合全站裁決。

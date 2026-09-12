# 本輪實測缺口與修正

1. 第一次 HTML 建置拒絕 DINO 第三頁的個別 label，因 engineering_slides schema 未允許此欄。修正為明確的可選欄位，保留文字驗證，並讓 page_payload 使用個別 label，未放寬其他未知欄位。
2. 初輪 8 個 PoC 行為測試有 1 個失敗：輸入長文字後點預覽，再下載時找不到可見下載按鈕。原因是 textarea blur 觸發 change，重畫 summary 按鈕，第一次點擊失效。文字僅在 input 更新；select 在 change 更新。保留此實際操作回歸，不能只檢查函式存在。
3. 第一次頁面語義驗證發現 DINO takeaway 還是交付長句。真正原因是 make_course_data 最後用 promise.body 覆蓋先前來源。增加經驗證的可選 takeaway，由已重寫課程明確擁有卡片收束；六課偵測改成有條件的選型句。
4. 發現時序課 relation 夾入「r01 實看修正」等製作過程文字，連同簡體殘留移除。工程維護註記留在本紀錄，不放在學生圖說。
5. 第一次 screenshot 與測試工具輸出不等於成果驗證。預覽截圖需等待 toast 消失；長文字用完整預覽列印，不依 textarea 可見範圍。source/docs 兩路與手機均需新驗。

共用原則已合併至根目錄 TEACHING_WEBPAGE_GUIDE.md WI-035；根 TEACHING_REVIEW_LOG.md 保存觀察、原因與驗證連結。未修改安裝的 skill，本次使用者要求的學習交付為 Markdown。

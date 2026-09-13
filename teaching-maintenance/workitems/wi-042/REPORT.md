# WI-042 定版修正與發布

狀態：實作與建置完成，最後實頁驗證進行中；Git及公開部署尚未完成。使用者已授權修改、commit＋push，成品核准pending。

## 修改與原因

- DiffusionAD：工程參考改為高／低兩個噪聲尺度各做單步估計，交代引導、後续定位與兩種訓練監督。同步修正步驟標題、正文、理由、錨點與diagram字段。既有主線及model.md已正確，不重複改寫。
- U-Net：補像素標註如何提供訓練目標；推論不附人工答案。
- YOLO-Seg：分清逐件標註監督，以及共享原型與每件係數形成各件遮罩。
- EfficientAD：分清固定教師、正常資料訓練學生與固定權重的待測比較。
- ConvLSTM：說明新輸入、舊狀態經卷積門控更新記憶。
- VideoMAE：說明可見塊編碼與遮蔽像素重建預訓練，再區分部署任務頭。

相對基準2c4cb73，course-data只改六課mechanism_steps；另外52課、主線圖片及所有共用JS/CSS/HTML模板相同。沒有新圖像、模型推論或功能擴充。範圍斷言與12個實頁結果见verification.json。

## 維護驗證器

`tools/verify_interactive_learning_html.py` 現在檢查現行需求助手／備份hook；接受既有inline/full-width顯示、原生桌面手機資產、full-mobile reading views與預設收合深讀欄位。圖片實際尺寸須符合既有native契約或精確宣告的手機尺寸，仍檢查PNG完整性、SVG解析、裁切邊界、58課、232張工程圖、40深讀圖、87共用圖及全部部署引用。

原有legacy concept共享／誤重複引用守門保留。新反例測試拒絕缺檔、越界路徑、錯誤尺寸、壞SVG、非法display、缺diagram、越界裁切與遺失備份hook。這是對齊目前契約，不是忽略失敗。

## 驗證證據

- pytest.txt：30 tests＋146 subtests通過，涵蓋新verifier、導覽、bundle文件、備份防護及PoC。
- verifier-regression.txt：10 tests＋11 subtests通過，含既有共享比較圖守門；其中6項新verifier測試與上述30項重疊，不重複計數。
- rules.txt：決策規則測試結果由verification.json記錄。
- verifier-source.txt／verifier-docs.txt：最終source/docs完整總驗證，完成狀態以verification.json為準。
- local-*.png：六課×1440/390展開因果鏈實頁；文字逐字段比對來源，無水平溢出或JS錯誤。實際看圖完成狀態待補。
- release-verification.json：公開HTML hash、本機及遠端提交、六課公開實頁與桌面手機需求流程；尚待push後產生。

初次verifier遷移的錯誤保留於verifier-attempt*.txt；包含不存在的hook拼字、未使用手機精確宣告尺寸、及遷移腳本將閱讀view邊界誤套到舊mobile_steps。最終修改與負例驗證取代這些失敗，不能重跑歷史update-verifier.py覆蓋最新版；最終來源以authoring快照為準。

## 定版界線

本輪關閉WI041已確認的有限文字及維護問題；自測取捨深度、PoC完整交接範例、縮放適配可放下一版，非目前缺陷。未新增真人學習、Safari/iOS實機或模型效能證據，不宣稱319圖逐字全評。公開核對成功後可作為本輪穩定教學版定版，使用者成品核准仍獨立記錄。

## ??????

verification.json complete=true?source/docs?????PASS??1370??????15?????????????12???????????????????????????????????????????????commit/push???hash/?????HTML SHA-256?139d466de1e9c5a3c2728d9c42fdde3bb44a6f5aefb4ac8bb5547ba1fd78a35a?

## 公開完成與定版判斷

六課修正與新版verifier完成並公開。內容commit 592d5c5已push，公開HTML 139d466d與docs相同；六課12個公開桌面手機實頁及需求流程通過。本機30tests+146subtests、15規則、verifier補驗10tests+11subtests及source/docs總驗證通過。WI041必修已關閉，建議本版定版；使用者成品核准仍pending。

公開核對證據release-verification.json；首次部署前舊hash拒絕及等待保留於deployment-wait.json。前述尚待發布段落是歷史checkpoint，不代表目前狀態。公開成品已包含六課修正，維護版verifier也已通過；沒有剩餘必修阻礙，建議定版。後續選配僅依真實使用回饋另排，不以這次完成代表所有模型現場實測。

?????????12??????????????????bytes??????public-screenshot-comparison.json???run34735161758????????????????????592d5c5?????????

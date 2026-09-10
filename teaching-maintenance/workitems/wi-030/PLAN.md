# WI-030 十二課重作

目標：依使用者四個連結與八題截圖，重作PatchCore、PaDiM、AnomalyDINO、EfficientAD、ResNet、ConvNeXt、ViT、U-Net、SegFormer、YOLO-Seg、Keypoint R-CNN、Pose Pipeline。以工作案例、必要原理、可見輸出、反例與取捨為主線。
授權：本輪明確要求重作；延續本專案製作、驗證、學習回寫及發布流程。使用者成品核准與自評分開。
基準：12fc9ff，Git乾淨。不得用既有高分替代新版審查，不覆蓋歷史原圖與實測證據。

- [x] 保存12課來源、資產清單與24張桌機手機現版，查第一手來源。
- [x] 實看參考，設計逐圖preflight，PatchCore桌機手機原型審查。
- [x] 其餘11課逐圖生成／修正／原生和實際尺寸審查。
- [x] 改寫12課正文、比較、自測與操作卡，整合新版引用。
- [x] 重建course/docs，逐課桌機手機、放大、自測、導覽、HTTP及必要回歸。
- [ ] 分項評分、共用學習回寫、持久快照、Git與公開版本核對。

## Checkpoint
最後完成：baseline、baseline-views、sources與21份preflight，validator通過。PatchCore r01否決項與r02修正已保存；r02桌面已實看，手機生成中。ResNet／U-Net／Keypoint代表原型生成中，尚未展開各家族批次。
下一步：原型原生和顯示尺寸審查，通過後產生其他圖；同時改寫12課正文。預計42張PNG，全部教學示意、非模型推論。實際啟用未改，頁面測試未跑，使用者核准pending。

## 預設閱讀路徑修正計畫
五課有deep_dive：PatchCore、AnomalyDINO、EfficientAD、ResNet、SegFormer；PaDiM沒有。為這五課增加經驗證的可選收合設定，預設新版首讀＋既有資料收合；其他課維持原行為。保留八章原資料與工程圖，檢查收合展開、章節導覽及直接hash入口；共享builder加聚焦回歸測試。這是本輪重作入口修正，不增加其他功能。

## 本機整合 checkpoint（2026-09-11）
- 已完成：18故事36張候選已審原生/936/328px、逐圖分項在prototype-review.md。九課已整合來源並建置course/docs成功（1292引用資產）。
- 正在進行：Pose核心/比較手機與YOLO核心修訂。YOLO改單件A加權路徑以避免複製基底造成錯誤因果；剩餘三課尚未整合。
- 下一步：收尾剩餘圖及全十二課，再跑72狀態互動與24閱讀狀態、84HTTP核對、必要回歸和公開發布。
- 測試：optional boolean早前1 test＋4subtests通過；此次完整collapsed UI與tall mobile測試進行中，不能算通過。公開站未更新，使用者核准pending。

### 建置證據更正
剛才build_github_pages_site成功只代表複製既有HTML，不會呼叫教材builder；因此1292是舊bundle，不是新版頁驗證。collapsed UI測試找不到legacy-deep-reference揭露問題（1 failed, 2 passed, 4 subtests）。已核對build_github_pages_site.py來源，下一步先build_interactive_learning_html.py再bundle；先前『已建置』不得當作新版完成。原JSON九課整合有效，尚未發布。

WI-030收尾：20故事40PNG已選，11課来源已整合，YOLO核心r06生成中；最後兩個新增精確尺寸已加validator和test，待最终重建。9 tests/10 subtests已通過（新增尺寸後需再跑tall）；全頁QA/HTTP/發布未完成。

## 全十二課整合完成，開始最終驗證
21故事42PNG逐圖自評完成，詳細分項與hash在image-review.md/json；逐版否決與修正仍在prototype-review.md。42份選用版本preflight通過；12課topic/model/learner來源整合。即將依序重建HTML與docs，執行72頁面狀態/216放大、自測導覽，24最終閱讀狀態及84HTTP/hash核對。所有檢查尚未完成，不提前打勾。啟用是本機候選，公開網站未更新，使用者核准pending。


## WI-030 最終審查 checkpoint（2026-09-11）
21故事42張PNG逐圖原生與936/328px審查完成，分數91–96，啟用版本及hash見selected-assets.json、image-review.json；十二課預設主線完成逐頁閱讀，自評92–93，證據與扣分見page-review.md。五課既有deep_dive資料保留，只增加預設收合旗標；原工程內容未算本輪評分。使用者成品核准pending。
72頁面狀態／216次解碼放大Escape／自測及導覽通過；最後自測改為帶條件的合理替代選擇，另測24桌機手機狀態，確認新解答實際展開可讀。84HTTP圖片hash、1231引用資產及HTML一致、12課變更／46課不變／5課舊章資料保留均通過。聚焦pytest 9 tests＋10 subtests、bundle 1 test通過。舊全站verifier仍在未改動ChArUco inline schema失敗，不計為通過。
即將執行：僅更新自評狀態後最後重建HTML與docs，刷新hash及範圍證據，保存teaching-maintenance快照，再依本輪既有授權commit/push並核對公開HTML與42PNG。現在公開站尚未更新；發布未完成。必要來源與prompt意圖在workitems/wi-030，截圖及原生PNG亦保存在該持久目錄。沒有模型推論或真人學習實測。


### WI-030 發布文件缺漏修正
最後查操作卡時發現本機docs缺少model.md／slide-manifest.md，原因是bundle只選圖與concept_path，未收modelPath／manifestPath。HTML雖有連結，但發布目標不存在；不是瀏覽器快取。已補builder依現有課程連結打包文件，會使其餘課程既有文件也可到達，不改其教材JSON。即將重建docs、測全部文件的來源／打包位元一致及十二課24個HTTP連結；原1231資產數屬修正前歷史，新總數待實際建置確認。公開部署尚未執行。


## WI-030 發布前核對完成
最新打包1347引用資產與HTML皆與來源hash一致（新增58課既有model.md及manifest共116文件；其餘46課教材JSON仍不变）。新增文件打包回歸2 tests＋116 subtests通過，十二課24文件HTTP/hash通過。前述1231是補文件前的歷史數量；不覆寫歷史紀錄。72互動狀態、216次放大Escape及24最終主線／新解答狀態均完成；最終HTML hash與完整範圍見validation-summary.json。
已完成逐圖、逐頁分項評分與兩份指南／共用REVIEW_LOG學習回寫。接下來保存teaching-maintenance可恢復來源、prompt、審查與測試快照，commit/push；公開HTML、42PNG及116文件HTTP核對尚未完成。啟用為本機候選，自評與工具驗證通過；使用者核准pending。舊全站ChArUco schema錯誤仍列失敗，無其他阻礙。

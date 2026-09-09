# WI-029 共同前提與量產入口重製

- 授權：使用者指定 foundations、production 兩網址，使用 Markdown 與 skill 重作，完成後 commit＋push。
- 範圍：兩頁的預設教學主線、圖像、案例、取捨、自測及工作交接；原工程教材可作明示的延伸參考。WI-028 的八個時序主題保持待辦；兩入口工作由本項接手，避免重複生成。
- 狀態：規範與現況閱讀中；尚未生成、整合、驗證或發布，使用者核准 pending。
- 計畫：先保存兩個公開入口及本機來源，找出首讀問題；依五份權威選實體案例與3–4節點故事，版本化preflight；單張原型原生與頁內審查後擴展其餘；整合、測試及逐圖／逐頁評分，學習回寫，提交推送並核對公開版本。
- 驗收：兩入口實際新圖文、手機獨立閱讀版本、可追蹤的案例與工作選擇、自測／圖像放大／導覽可用；每圖每頁按v1.0 >90且無否決；course/docs及公開HTML／新PNG一致；必要回歸通過。
- 生成模式：適合實體工件的圖用built-in imagegen；數值教學與精確互動用HTML，明示示意不作真實模型成績。
- 最後完成：讀WORKITEMS／TODO／STATUS、教學cycle與planned-code-modifier，查到現版兩頁由build_interactive_learning_html.py提供：單張橫圖、預設展開第一模組，18／24張工程教材。
- 即將執行：保存公開／本機baseline與來源副本，實看參考；web文字工具無法開啟公開頁，改以實際瀏覽器與HTTP讀取。可用工具目錄沒有browser/node_repl，沿用本機Playwright Edge驗證。
- 產物：workitems/wi-029/；阻礙：無；完整驗證未跑。

## Checklist
- [x] 現版來源及桌面／手機基準、學習與參考。
- [x] 原型brief／preflight、產生及實際PNG審查。
- [x] foundations 圖文、取捨與自測。
- [x] production 圖文、取捨與自測。
- [x] course/docs建置、互動、引用／HTTP、逐圖逐頁與必要回歸。
- [ ] 共用學習、接續紀錄、保存副本、commit＋push與公開核對。

- Checkpoint：8個基準狀態／16截圖與來源已保存，兩張首選參考已實看，六brief preflight PASS。即將執行fdn-visible-r01桌面原型；prompt存prototype-prompt.json，預期PNG在本工作目錄。node_repl工具已找到，但瀏覽器discovery=[]，讀troubleshooting後使用Playwright Edge。未整合／發布。


- 原型r01已生成與實看：fdn-visible-r01-desktop.png，原始exec-ef1dc1e4-01c4-430a-be5b-cef5747a3548.png；第三區焦距文字需修，尚未通過。r02 preflight PASS，即將精確修正；其餘尚未生成。


- 原型r03原生及936px審查通過，自評94，詳細prototype-review.md；已保存11個其他輸出prompt在generation-plan.json。即將生成fdn-visible手機、fdn-data桌面／手機；其餘生成候選逐張審查。頁面正文Markdown草稿已保存，未整合。


- fdn-visible手機r01已生成原生審看，待326px；fdn-data兩版r01未通過（正常mask、特徵及替代箭頭），r02 brief已驗證。即將生成修訂及其餘故事；檔案及prompt在本工作目錄，未整合／發布。


- fdn-data桌面r02已修正常mask／向量／獨立路線，待936px；手機r02仍把正常參考畫成缺口，未採用。fdn-output兩版r01混入前圖對焦文案，手機量測端點未落兩個缺口唇，需修正。即將生成prd-test桌面手機及prd-shadow桌面，prompt均已存generation-plan.json；未整合。


- 量測桌面／手機r02已修正文案與端點，待頁內審讀；資料手機r03仍未恢復正常形狀，改由正確桌面重新設計r04。即將執行generation-batch3.json六圖：資料手機r04、切分桌面手機r02、旁觀手機及回退兩版。未採用錯誤稿，尚未建置／發布。

- 最後修訂即將執行：prd-test兩版r03移除虛構測值與重複資料，prd-shadow手機r02修同工件形狀。prompt保存corrections-final.json。新Markdown／UI／parser已接入來源，2個parser測試PASS；尚未建置或發布。
- 12張PNG原生與936/326px審查完成，自評92–94；selected-assets／image-assessment及正式assets.json已保存。course已建置，docs建置待程序結果。即將執行12狀態36圖互動、HTTP及回歸；使用者核准pending，未發布。
- 實際瀏覽器發現CLI建置仍輸出__WORKPLACE_UI__佔位符，頁面空白；原7測試通過不能當成頁面完成。已統一main呼叫build並補CLI回歸，重建後重新驗證；尚未发布。

## 發布前checkpoint
- 兩入口本機重製與驗證完成：6故事／12PNG，Markdown實際驅動頁面；12狀態36圖放大與解析、24PNG HTTP hash及4Markdown HTTP通過，8最終狀態正文一致與圖首可達，9回歸PASS，1303引用檔course/docs一致。圖自評92–94、頁93–94，使用者核准pending。學習回寫三份共用Markdown，正在保存副本／commit＋push；公開核對尚未執行。
- 生成模式：built-in imagegen。完整意圖與版本在prototype-prompt、generation-plan／batch3、corrections-final及各brief；選用路徑／hash在assets.json和image-assessment。
- 最後完成：實作與必要驗證；下一步：保存維護副本、commit/push並查公開HTML／PNG／Markdown。無阻礙。
- 截圖校正：locator整元素截圖會把fixed工具列混入圖中；final-pages改用原viewport捲動、等待穩定後拍攝，24個圖首均在工具列下方，12手機圖尾可達。

## WI-029 foundations／production 兩入口重製（2026-09-10）
- 最終完成（取代下方歷史checkpoint）：WI-029兩入口重製及發布完成：內容commit `c6c32a4bad797a0c1bebb5287db6f95c5ffd0b95` 已push，Pages run 34415751416 success；公開HTML、12張PNG及2份Markdown全部一致。六案例由Markdown驅動，12狀態36次放大／自測、8最終狀態、9項回歸、1303資產course/docs一致；圖自評92–94、兩頁94，使用者成品核准pending，未做真人學習測試。
- 最新checkpoint（取代下方舊狀態）：兩入口本機重製與驗證完成：6故事／12PNG，Markdown實際驅動頁面；12狀態36圖放大與解析、24PNG HTTP hash及4Markdown HTTP通過，8最終狀態正文一致與圖首可達，9回歸PASS，1303引用檔course/docs一致。圖自評92–94、頁93–94，使用者核准pending。學習回寫三份共用Markdown，正在保存副本／commit＋push；公開核對尚未執行。
- 使用者明確指定兩頁重作並commit＋push；進行中，先保存基準與製作原型。
- 接續：teaching-images/vision-ai-model-selection/workitems/wi-029/PLAN.md。
- 八個時序主題保留WI-028待辦；两入口由WI-029接手。未生成／驗證／發布，使用者核准pending。

## WI-027 七課重製（2026-09-10）
- 最終發布完成（取代下方舊checkpoint）：七課重製commit `784e572633b7b35d9d380ef327523d6b270af8d8` 已push，遠端main一致；Pages run 34399986161 success，公開HTML及30PNG SHA256全部通過。84份已提交學習／審查副本hash一致；Git工作目錄乾淨。七課實作與技術驗證完成，使用者成品核准pending。WI-028時序八課及production／foundations仍排隊，未宣稱完成。
- 已commit＋push：`784e572633b7b35d9d380ef327523d6b270af8d8`，遠端main一致；84份已提交副本hash通過，Git乾淨。Pages run34399986161排隊，公開版本尚待核對；下一步等部署成功後執行publish_check.py。
- 發布前最終核對：1289個引用資產的course/docs SHA256及HTML全數一致，清理90個未引用發布檔（作者來源保留）；7課preflight通過。頁面狀態更新後CopyFile2遇Windows1224，已用逐檔hash及14狀態／60HTTP重驗確認完整。保存副本初次因bundle報告未完成中止，現報告存在後重跑。接著commit／push；使用者核准pending。
- 最新完成 checkpoint（取代下方執行中狀態）：七課重製30張PNG／15組故事，圖文與model.md已接入course/docs。42狀態126次放大／Escape、自測導覽、14最終頁面狀態、60 HTTP hash、1289資產存在及5項回歸通過；30圖自評91–96、7頁93–94，使用者核准pending。QA曾與docs複製重疊而失敗，建置完成後重跑通過。即將同步學習副本、commit＋push及公開核對，尚未發布。證據workitems/wi-027/。
- 最新 checkpoint：30張已逐張原生／頁內審查；SigLIP手機r05完整結論及負配對修正通過，原生861×1827已明確登錄。前五課30狀態90次放大通過；即將整合SigLIP／Qwen、清理重建發布包及最終驗證。尚未commit/push，使用者核准pending。
- 五課本機已整合並構建course/docs，QA正在執行。構建首次指出比較需三列，已補既有檢索／專用分類基準；第二次指出新原生725×2167，另核對1672×940，已加精確畫布白名單與相鄰尺寸拒絕測試。沒有縮放PNG。29圖審查已記reviewed-assets-progress8.json，SigLIP手機r05仍生成中；七課整頁與公開核對未完成，未commit/push。
- 即將本機整合：reviewed-assets-progress7.json已有27張原生與頁內審查；五課素材齊備，先寫選圖／逐圖證據並整合DINOv2、DINOv3、CLIP、LLaVA、Gemini Vision。Qwen反例r03與SigLIP手機r05尚待成圖審查；七課全過後才commit/push。預期topic／learner／model.md／course/docs更新；本機與公開分開，QA尚未跑，user approval pending。
- 可接續 checkpoint：已通過原生與936／326px審查的11張記於reviewed-assets-progress2.json；其餘仍是候選。DINO對比r02已補兩側查詢編碼，待頁內審查；DINO反例r03修裁切及模糊輸入、圖文比較r03修雙模態共同輸入，generation-batch10/11.json。正文、integration與QA／publish脚本已備妥但未執行正式整合。最後完成：學習規則寫入共用三份Markdown。下一步：收齊修訂→逐圖頁內審查→selected-assets→整合／驗證／發布。遠端仍上一輪bd4b87b，使用者核准pending。
- 反例三組r01都誤沿用參考圖黄色contract結論；prompt漏傳逐圖takeaway，已找到原因並補精確文字，六張r02即將生成。Qwen手機來源裁切右螺絲位置及token措辭一併修正；LLaVA核心手機r03分開視覺／文字token標示。產物generation-batch9.json；舊稿未採用，整頁測試未跑。
- r02 審查更新：SigLIP已修正負配對損失，但仍有編碼器互相傳訊箭頭；Qwen已分開特徵與問題，仍殘留「真實拍攝」。兩者r03採精確局部文字／箭頭編輯，generation-batch8.json，仍未採用。Gemini r02已分清能力與模型ID，待頁內尺寸審查。
- 即將生成：LLaVA／Qwen／Gemini 三個反例的桌面與手機、LLaVA 核心手機、圖文候選反例手機；預期八張候選，依已驗證 brief，prompt 在 generation-batch6.json。原生與頁內審查未完成，尚未採用或發布。
- 生成校正 checkpoint：LLaVA r02 已修正投影旁路；DINOv3 r02 矩陣已對稱。SigLIP r01 負配對損失方向錯誤、Qwen r01 把照片切片當特徵、Gemini r01 把能力名稱當 model ID，均未採用。比較圖另有錯配標籤及查詢繞過編碼器，反例圖不應把生成圖稱實拍；六項 r02 brief 已驗證，正在生成桌面／手機修訂，尚未整合／發布。產物及 prompt：workitems/wi-027/corrections-batch5.json；完整驗證未跑，使用者核准 pending。
- 即將生成比較圖：features-d3、alignment-d3、vlm-d3 桌面／手機，共六PNG，brief已preflight PASS。比较分别是更換骨幹重建下游、訓練目標與同題驗證、自建／託管部署。prompt保存generation-batch4.json；當前已審原型外其餘仍pending，未整合或發布。
- 中斷後核對：batch1 已結束，磁碟有DINOv3／CLIP／LLaVA桌面r01及DINOv2手機r01；加上DINOv2桌面r01/r02共六PNG。正式七課仍是f02，docs新圖0，遠端bd4b87b為前輪。本輪尚未commit/push，頁面回歸未跑。下一步修LLaVA核心（照片不能標成特徵，移除投影旁路），完成其餘核心與手機，再反例／比較。
- 最新使用者授權：先完成本七課、學習寫回及 commit＋push，再執行 WI-028 八個時序主題與 production／foundations；前輪仍在生成及驗證，不縮減原範圍。
- 原型通過：DINOv2 r02 原生與936px已實看，自評94（分項／缺口見workitems/wi-027/prototype-review.md），手機／整頁未評。14張其他故事preflight通過；即將生成DINOv3、CLIP、LLaVA桌面代表圖及DINOv2獨立手機，逐圖另審。
- 原型 checkpoint：DINOv2 r01 已生成與實看，第四區參考特徵畫成相同且查詢輸入缺失，判需修正，未給達標分。r02 brief 已記具體修改，接著修圖再查全圖；原檔保留 workitems/wi-027/dinov2-c1-r01-desktop.png。baseline 手機為 object/SVG，初版 img-only 檢查 timeout，已調整後重跑。
- 授權：以 Markdown 與 skill 生成截圖七題；工作範圍為首讀教學，依既有交付流程整合及發布，使用者成品核准另列 pending。
- 最後完成：確認七個 topic JSON 存在，Git 工作目錄乾淨，WI-026 已發布；技能／權威閱讀進行中。
- 即將執行：保存 baseline、核對版本与官方來源、實看幾何參考與七課現版，設計首張原型。尚未產图、評分或測試，沒有生成程序。
- 生成模式／產物：built-in imagegen，AI 生成教學示意非模型實測；prompt、候選、審查及驗證保存於 workitems/wi-027/，正式引用確認後另記。
- 前輪學習：位置／來源一致、訓練與推論責任分開、操作卡回答實際準備及驗收、替代方案不串接。七題另需分清特徵、圖文相似度與生成回答，不能畫成同一輸出。

## WI-026 八課重製啟動（2026-09-09）
- 2026-09-10 最終發布完成（取代本項下方未發布 checkpoint）：commit `bd4b87bc5601d884a1ffe9cf0fb9e4f0d03330d6` 已推送，遠端 main 一致，Git 工作目錄乾淨；Pages run 34386196881 success，公開 HTML 與 38 張 PNG SHA256 核對通過。17 個已提交維護副本 hash 一致；證據 `workitems/wi-026/public-release-verification.json`、`deployment.json`。提交範圍為 docs 與 teaching-maintenance，原始作者工作區仍留本機；使用者成品核准另列 pending。
- 發布 checkpoint：`bd4b87b` commit／push 成功，17 個已提交副本 hash 核對通過，Git 工作目錄乾淨；下一步 Pages 部署及公開 HTML／38 PNG hash 核對，尚不能宣稱公開更新完成。
- 2026-09-10 發布開始：使用者明確授權 commit＋push；既有圖文與測試完成，即將檢查 docs／teaching-maintenance 提交範圍、推送及驗證公開版本。未更動圖文，尚未完成 Git／部署驗證；證據將存 workitems/wi-026/。
- 收尾保存：17份teaching-maintenance副本SHA256一致，git diff --check PASS。完整prompt／失敗稿／原始工具PNG路徑保存在workitems/wi-026/，final-provenance.json核對38張；本機HTTP服務保留供閱讀。
- 最新完成（取代本項下方執行中checkpoint）：八課首讀圖文完成：每課核心／反例／比較三張，19組不同故事、38張桌面／手機PNG。已接入topic、learner、model.md與course/docs；影像為AI生成示意。
- 驗證：38圖自評91–95，8頁93–94（v1.0逐項證據）；48狀態144圖放大／Escape、自測與導覽通過，最後操作卡修正後16狀態可見文案／圖片／無溢出通過；76次HTTP hash與course/docs一致，5項回歸PASS、8課preflight PASS。
- 範圍與限制：完整slot audit保留24筆舊工程SVG中繼資料及slide-manifest的歷史樣式標記，沒有新首讀圖或disk/HTTP錯配；文字因果鏈實際img/object=0。未以首讀分數代表原工程圖，未跑真人學習／模型實測，使用者核准pending。未commit/push，公開網站尚未更新。
- 接續：本輪本機製作完成；如有新回饋，依selected-assets.json及逐圖／整頁證據重開相應項目。產物workitems/wi-026/；沒有待執行生成程序。
- 38張選定PNG已原生及936px／326px逐張實看，selected-assets.json記啟用候選；修正紀錄保留r01至r03。現在即將整合八課、建置course/docs及48狀態QA；頁面驗證尚未跑。新原生手機726×2167與728×2161只增明確白名單，未改圖像像素。使用者核准pending。
- 最新checkpoint：19組桌面故事已有候選，核心與反例已逐張檢查；比較圖發現替代方案被串接及虛構LoRA分類，正在依corrections-batch4.json修正。手機剩餘反例與比較正在生成，未完成326px全數審讀。正文新增不同工件／遮罩案例說明及含雜訊一致性的限制。下一步選定38張圖、整合與48狀態QA；尚未建置或發布，使用者核准pending。
- 基準完成：本機8000原先未啟動，已以隱藏服務啟動（course根）；`baseline-views/`16狀態截圖及全文完成。首讀新版仍未正式接入。核心與反例候選逐步生成，原始工具路徑見`generated-results.json`，完整prompt基礎在`generation-plan.json`，修正在`corrections-batch1.json`。下一步完成剩餘手機、逐圖326px審讀和整合；不把檔案存在視為已評。
- 正文checkpoint：`lesson-content.json`八課核心、反例、比較、成本與自測已完成草稿；`integrate.py`語法檢查PASS，尚未整合。18張其他圖preflight全PASS。DefectFill／TF-IDG r02已落盤，ControlNet／Deblur／SR核心r01已生成；具體需修事項在共用log。手機Inpainting已生成，待326px核對。
- r02原型已保存並原生實看，修正局部來源矛盾，自評94（非用戶核准）；下一步獨立手機與其餘故事逐圖生成。`visual-plan.json`保存18個其他故事、來源、四節點與不可改變事項。正式引用仍未變，網頁测试未跑。
- 原型checkpoint：inpainting-c1-r01-desktop.png已生成並實看；局部放大錯帶上方孔，需r02修正，未接正式。preflight PASS；尚未手機生成及網頁測試。built-in browser discovery=[]，改用本機Playwright驗證。TF-IDG原文PDF已保存在sources/，確認需補特徵對齊、適應遮罩及紋理保存。
- 已完成：範圍依截圖確認八題；已讀教學cycle、slot-audit、imagegen技能與五檔規範相關內容。
- 即將執行：來源／基準盤點、首選幾何參考實看、逐圖brief及單張原型。
- 產物預定workitems/wi-026/；生成模式built-in imagegen，示意不作模型實測。正式版本未改，尚未產圖／測試；使用者核准pending，無已知阻礙。

## WI-025 視覺偏好已寫回（2026-09-09）
- 已完成：IMAGE_STYLE_GUIDE.md 11.3 記首選幾何兩圖／次選模型四圖，TEACHING_WEBPAGE_GUIDE.md 連回，TEACHING_REVIEW_LOG.md 保存明示回饋與歸納界線。
- 最後核對：兩張首選 PNG 路徑存在；組內無排名，風格認可不當技術或全課核准。
- 完成驗證：3份 teaching-maintenance 更新副本與權威來源 SHA256 一致，manifest 已更新，git diff --check PASS。無新圖片、未跑程式測試、未 commit/push；無阻礙。
- 下輪：按圖片指南選首選參考，先實看及單張原型，再擴展。WI-024 四課完成狀態保留。

## WI-024 開始偵測課重製
- **完成／取代下方本輪舊checkpoint**：四個已提供課程各三張首讀，20張不同desktop/mobile PNG已實際生成、引用、驗證與發布。Commit `184f1ee4da026e90160e97bfdb073428fd08f842`，origin/main一致，tracked worktree乾淨；Pages run34288353853 completed/success，公開HTML及20PNG hash一致。
- 驗證證據：workitems/wi-024/image-assessment.json（20圖v1.0分項）、page-assessment.json（4課預設全文與自測）、qa-*/（24狀態72圖互動）、release-audit.json（1311資產、40本機HTTP hash、最終8狀態）、public-release-verification.json、deployment.json。桌面936px／360視窗326px，另328px逐圖審看；8 tests／6 subtests PASS、skill有效、12已提交snapshot blobs hash符合manifest。
- 狀態分界：以上為實作、工具與自評完成；非真人學習成效，使用者成品核准pending。尚未提供的兩題不自行假定。根記憶、作者素材／提示／截圖與工具修改保留本機；提交範圍為docs及teaching-maintenance學習與三份審查副本，並非整個作者工作區備份。
- 發布checkpoint：遠端main與184f1ee完整hash一致；GitHub Pages run34288353853建置中。第一次公開HTML尚未更新，不能當發布完成。等待部署後重跑workitems/wi-024/verify_public.py，核對HTML及20張PNG。
- 已commit/push：`184f1ee4da026e90160e97bfdb073428fd08f842`，40檔變更；12已提交學習／審查副本hash一致、tracked工作目錄乾淨。四課20PNG已發布至Git，公開Pages尚待核對。下一步verify_public.py與遠端main；另外兩題未提供、使用者成品核准pending。
- 最後完成：四課預設全文與自測實讀，修正比較成本摺疊及learner輸出欄位；YOLOE頁首已顯示框與mask。8 tests／6 subtests PASS，skill quick_validate PASS。共20PNG、24狀態72圖互動；發布包去除12未引用檔案（8舊手機SVG、4重複PNG），原作者素材保留。release_audit進行中，接著逐頁分數、同步副本、commit/push及公開核對；未發布、user_review pending。
- 四課20張不同PNG已原生與328px審看；YOLOE C1桌面r02修正「區域切分」為特徵位置示意，手機r01保留提示向量旁路；D2邊界溢出與共用提示比較圖均r01。即將接入最後兩課、同步course/docs、跑六狀態QA。原生727×2164新增明確尺寸白名單，使用既有tall_mobile回歸與本機真圖驗證；不重採樣。尚未發布，使用者成品核准pending。
- Grounding DINO C1桌面r03／手機r01、D2桌面與手機r01已生成實看，待328px與整合；C1前兩稿修正原圖／特徵角色、查詢入解碼器及側標籤遮擋。YOLOE即將用SAVPE視覺提示單一案例製作，三模式不畫成同時必需輸入。前兩課course/docs各六狀態QA通過，實際頁面截圖待審讀。
- YOLO／RT-DETR各三張已接入topic、learner與model橋接；course已建置，docs同步執行中。10張不同PNG原生及328px已審看；尚待各圖分項整理與全頁QA，未發布。
- 已知比較圖r01分支箭頭都誤指YOLO，r02移除跨欄箭頭並改共同準備標題；手機r01為上下並列，無串接箭頭。RT-DETR D2手機r02已移除測試輸入的預測框。
- 下一步Grounding DINO新圖，另兩題仍待使用者回覆；不擅自補主題。
- YOLO D2桌面r02／手機r01已生成實看；桌面r01的NMS縮框錯誤已修，手機移除已刪候選的虛線避免與保留框混淆。RT-DETR C1桌面r02／手機r01已實看，修正細／中誤入高層注意力的箭頭。
- RT-DETR D2桌面r01已生成；手機r01第四區輸入誤含框，未通過，r02即將修正。所有產物及prompt在workitems/wi-024/，尚未整合、未發布；其餘圖／頁面未評。
- YOLO C1桌面1672×941／手機724×2172已生成並原生／328px審看，來源與prompt在workitems/wi-024/yolo-c1-generation.json。A三框+B一框→A/B各一框可追蹤，尚未正式接入。
- 原型自評：桌面[24,23,18,19,9]=93、手機[24,22,18,19,9]=92；特徵僅示意且回歸細節由正文展開，手機省略跨区虛線但順序成立。完成度桌面[9,9,9,9,9]／手機[8,9,9,9,9]：大主體、四步完整、來源誠實、短文、箭頭清楚；手機長圖需捲動，未做真人學習。使用者核准pending。
- 即將製作YOLO D2去重誤刪鄰件及RT-DETR核心；原型條件可沿用，不把其自評當其他圖通過。
- 已讀入口、技能及現版YOLO來源；明確四題det-yolo-dense、det-rtdetr、det-grounding-dino-interface、yoloe，另兩題待使用者回覆。
- 即將保存topic/model/learner基準，實看首讀圖與PPT參考；後續imagegen產圖前各寫brief並驗證。未生成、未測試、未發布，使用者成品核准pending。
- 工作產物預定workitems/wi-024/，原工程圖保留；本次明確授權完成後commit/push。

## WI-021 已完成重製與發布（2026-09-09）
- 授權：使用者要求以skill重製13課；沿用commit＋push授權。實作、工具驗證與發布完成；使用者成品核准pending、真人學習測試未做。
- 產物：13課首讀圖文、43組邏輯圖槽、62張不同PNG（桌面31／手機31），imagegen實際生成並逐圖審看；原工程參考保留。示意圖不當作真實模型推論。
- 驗證：course/docs 78狀態與258次圖互動PASS；最終26狀態與86圖解碼PASS；124本機HTTP雜湊PASS。公開HTML與發布版一致，公開62PNG全部200且SHA256一致。
- 必要回歸PASS：ad_f01 4、navigation 3、tall_mobile 1、bundle 1、三圖首讀邊界1。全站charuco verifier阻塞與anomalydino整檔4個歷史斷言失敗未處理，不宣稱全站通過。
- 發布：commit `749401f96609279cd19c068b897a4edb17504476`；origin/main一致，worktree乾淨。GitHub Pages action 34283005280 completed/success；https://hctsaik.github.io/visionAI_Model_Introduce/
- 證據：workitems/wi-021/public-release-verification.json、release-audit.json、page-assessment.json、image-assessment-*.json、qa-*/；共用TEACHING_REVIEW_LOG.md。Git僅發布docs與README，根記憶和製作素材保留本機，未宣稱已push。
- 下一步：本輪已授權工作完成；若使用者給成品回饋，從此版本與上述證據接續。舊checkpoint保留為歷史，由本段取代。

## WI-021 已push／公開部署待核對
- commit 749401f96609279cd19c068b897a4edb17504476；git push origin main成功。tracked worktree乾淨。
- 公開HTML第一次核對仍舊版，正在等待部署；不能宣稱已上線。下一步verify_public.py核對HTML及62PNG。

## WI-021 本機實作與驗證完成／即將commit＋push
- 13課、43組邏輯圖槽、62張不同桌面/手機PNG正式引用；imagegen生成模式，非實測。原工程參考保留。
- 原78狀態/258圖互動PASS；最終26狀態/86圖解碼PASS、124本機HTTP hash PASS；1299引用資產逐檔一致、未引用0，bundle 1,029,718,818 bytes。
- 全13頁已實讀與逐项自評，詳workitems/wi-021/page-assessment.json；逐圖四份image-assessment檔。自評不是真人驗收，使用者核准pending。
- 回歸：ad_f01 4、navigation 3、tall_mobile 1、bundle 1、三張首讀邊界1 PASS。全站verifier既有charuco阻塞及anomalydino整檔4個舊斷言失敗保留，不宣稱全站通過。
- 發布包清除403個tracked未引用舊資產及24個未提交重複PNG，來源原檔保留。git diff --cached --check PASS。
- 下一步：commit、push、比較遠端HEAD與公開HTML/PNG；目前尚未發布。Git僅追蹤docs/README，本機記憶不宣稱已push。

## WI-021 發布整理中
- 13課首讀圖文已接入；62張不同PNG均已原生實看與328px審讀。生成模式imagegen，示意非模型實測；逐圖量表四份在workitems/wi-021/image-assessment-*.json。
- course/docs共78種狀態、258次圖片與放大互動通過；13課預設全文與自測已讀。即將保存整頁評分、清除發布包未引用資產、最終驗證及commit/push。
- 使用者成品核准pending。全站verifier既有charuco阻塞，未宣稱全站通過。

# Beginner visual redesign status

## WI-021 全13課圖已產生，最後三課即將整合
- WinCLIP C1 r02/r01、AnomalyCLIP C1 r02/r02、AnomalyGPT C1 r02/r04、共用CLIP D2 r02/r01、GPT D2 r01/r01、共用D3 r04/r07已實看及328px審讀；十二PNG的逐項分數與限制在image-assessment-clip.json。
- 生成模式imagegen；正文packet三份完成。共62張不同新PNG，最後12張尚未正式引用。新手機原生725×2169納入明確尺寸集合，未裁切。
- 即將執行整合三課、建置course/docs、三課六狀態QA、13課全頁審讀及必要回歸。使用者核准pending，未commit/push。

## WI-021 十課接入／CLIP核心製作中
- DiffusionAD/DDAD已接course/docs，兩課六狀態QA各18圖通過；首讀摘要過長曾被builder拒絕，縮短後重建成功assets1323/1003.9MB。逐圖證據image-assessment-diffusion.json。
- 累計十課50張不同新PNG，尚未commit/push；整頁分數未完成。
- WinCLIP C1桌面r02/手機r01已生成實看；AnomalyCLIP桌面r02修正圖文各自輸入，手機即將生成。AnomalyGPT與共用錯誤/比較未做。
- 生成模式imagegen，非實測。使用者核准pending。下一步完成三課圖文、整頁審讀和發布驗證。

## WI-021 擴散兩課即將整合
- DiffusionAD C1 r04/r03、DDAD C1 r01/r02、共用 D2 r02/r03、D3 r02/r04 已實看；D2 手機第四區原圖刮傷補回，D3 A/R 改兩個獨立輸入箭頭。八張 PNG 為 imagegen 示意，噪聲非實際高斯樣本。
- 328px 審讀前三張及 D3 完成；D2 最新版待重跑。新增原生725×2170，不裁切。即將整合 packet、course/docs 與六狀態 QA。
- 已完成八課本機接入42張不同圖；兩課整合後為十課50張。CLIP三課與全頁評分未完成，未發布，使用者核准 pending。

## WI-021 擴散原型 checkpoint
- DiffusionAD C1 桌面 r04／手機 r03 已生成並實看；N→引導估計連線修正完成。加噪縮圖仍是生成式紋理示意，未當作實際高斯噪聲樣本；手機標籤已改噪聲示意。尚未 328px 審讀／正式引用／自評。
- DDAD C1 即將生成，brief ddad-c1-r01.md 通過；正常去噪、特徵適配、原圖條件、多步與雙差異四區。產物 ddad-c1-r01-desktop.png，內建 imagegen，非實測。
- 八課各六狀態 QA 已通過，UniAD/Dinomaly/InvAD 實際頁面截圖已看；擴散兩課及 CLIP 三課未完成、未發布、使用者核准 pending。

## WI-021 八課接入／DiffusionAD 即將生成
- UniAD、Dinomaly、InvAD 已整合 course/docs；建置成功 assets 1323、990.5 MB。Dinomaly／InvAD 六狀態 18 圖互動檢查各通過，UniAD QA 仍在執行。累計 42 張不同新 PNG，八課本機引用。
- 新三課逐圖自評與五項完成度證據在 image-assessment-multi-three.json；全頁分數待實際主線審讀，未宣稱整頁完成。
- 下一步：DiffusionAD C1 四區原型，brief diffusionad-c1-r01.md 已驗證；內建 imagegen，預定 diffusionad-c1-r01-desktop.png。兩尺度單步估計及學習分割，非整套一次網路。DDAD與CLIP家族尚未製作；使用者核准 pending，未發布。

## WI-021 多類三課即將整合
- 10 張不同新 PNG 已實看及 328px 審讀：UniAD C1 桌面 r02／手機 r02；Dinomaly C1 桌面 r04／手機 r01；InvAD C1 桌面 r01／手機 r03；共用 D2 桌面 r02／手機 r03；D3 桌面 r02／手機 r02。原生手機 724×2171/2172。
- Prompt／修正均保存 generation.json；正常 q 手機輸出改乾淨示意圖，避免兩輪殘留刮傷；InvAD 共享起始與空間條件已分清。全為 imagegen 示意，非實测。
- 即將執行三個 packet 整合、前五課比較成本移到預設可見圖說、build course/docs，再跑三課六狀態 QA。全頁自評尚未完成，使用者核准 pending，未發布。

## WI-021 多類特徵組原型 checkpoint
- UniAD C1 桌面 r02／手機 r02，Dinomaly C1 桌面 r04／手機 r01 已實看；手機皆原生 724×2172，328px 預覽尚未做，未正式引用。
- InvAD C1 即將內建 imagegen 生成，brief invad-c1-r01.md 已驗證；輸入條件調制共享起始特徵，非每張最佳化。預定 invad-c1-r01-desktop.png。
- 未完成：三課共用逐類驗證／比較圖、圖文整合與全頁 QA；擴散與 CLIP 三課未製作。使用者核准 pending、未發布。

## WI-021 前五課完成本機接入／UniAD 原型即將生成
- AE、RD4AD、DRAEM、STFPM、SubspaceAD 合計 32 張不同新 PNG，course/docs 六種狀態逐課 QA 通過（共 114 次圖片／放大）。SubspaceAD 手機頁實看完成。
- 逐圖自評及五項完成度理由在 workitems/wi-021/image-assessment-first-five.json，共用 log 有逐項表；非使用者核准。整頁文字已讀取，尚待記錄全頁評分。
- 下一步：UniAD C1 原型，brief uniad-c1-r01.md；內建 imagegen，四區多類正常共訓／限制特徵照抄，預定 uniad-c1-r01-desktop.png。八課未完成、未發布、使用者核准 pending。

## WI-021 SubspaceAD C1 即將生成
- STFPM course/docs 建置完成，三張規則聚焦測試通過，browser QA 執行中。
- SubspaceAD 原型 brief `workitems/wi-021/subspacead-c1-r01.md`；正常 PCA 擬合、待測局部特徵、投影殘差與網格熱圖四區。
- 內建 imagegen 示意；明說特徵空間非工件平面、不更新骨幹仍需擬合。預定 `subspacead-c1-r01-desktop.png`，未啟用／評分／使用者核准。

## WI-021 建置器回歸結果
- 更新的三張首讀／兩張拒絕／首圖 raster 邊界測試已執行；完整 `test_anomalydino_beginner_path.py` 11 項有 4 項舊斷言失敗，涉及先前已更名的 causalChain 函式簽名與 F01 前固定圖片路徑，非本輪三張規則造成。不宣稱整檔通過。
- 本輪只修已過時的最少圖數測試；其餘歷史斷言保留待專項處理。STFPM 頁面需要實際 browser QA 補證據。

## WI-021 STFPM 建置門檻修正 checkpoint
- 第一次整合後 builder 拒絕三張首讀圖（舊硬性至少四張）；該次 docs 仍是前版，不能當 STFPM 已顯示。
- 已核對 `TEACHING_SITE_READING_LAYERS.md:13` 明示第一遍 3–5 張；builder 最少改為三張，仍保留首圖 raster、安全路径及完整欄位驗證，不縮短其他課。
- 更新既有測試：三張保持 authored order、兩張拒絕、SVG 首圖仍拒絕。即將重新 build course→成功才 build docs；測試正在跑。STFPM 頁面驗證尚未完成。

## WI-021 STFPM 三圖整合中
- 選用 C1 桌面 r02／手機 r01、D2 桌面 r02／手機 r01、三方法比較桌面 r02／手機 r03；已實看 PNG 與 328px 預覽。
- 修正來源：C1 保持同架構編碼器圖示；D2 移除重複欄位編號；比較圖把正常 PCA 擬合與待測殘差分清，手機刪除重複點與誤導連線。修訂 prompt 在 workitems/wi-021 的 generation.json。
- 即將執行：`stfpm-packet.json` 整合 topic/bridge/learner、建置 course/docs、三視窗 QA。生成模式 imagegen 示意，非實測；手機原生 724×2171 已納入明確尺寸集合，鄰近不支援尺寸仍拒絕，測試通過。
- DRAEM QA 六頁／24 圖放大等通過，ad_f01 四測試通過。四課本機內容有改動但逐圖量表尚未整理完；剩餘九課未製作，未發布、使用者核准 pending。

## WI-021 STFPM 原型即將生成
- 接續 AE/RD4AD/DRAEM 本機三課，DRAEM 頁面 QA 進行中。下一原型 STFPM 同圖雙支路；四區 preflight 在 `workitems/wi-021/stfpm-c1-r01.md`。
- 內建 imagegen 示意，正常訓練學生／固定教師、同架構、三尺度對照；預定 `stfpm-c1-r01-desktop.png`。尚未啟用／評分／使用者核准。

## WI-021 DRAEM 三組新圖＋比較圖整合中
- 已產生並實看：C1 桌面／手機 r01、C2 桌面 r01／手機 r03、D3 桌面 r02／手機 r01；手機 328px 預覽已生成。
- 修正：D3 桌面及 C2 手機原圖／重建共享括線；C2 手機 r02 底部裁切由 r03 修正。舊版保留未啟用。比較圖復用本輪 AE D5 r02。
- 即將執行：以 `draem-packet.json` 整合四圖、更新權威 bridge／learner brief、建置 course/docs 與三尺寸互動檢查；啟用清單在 `ad-draem-active-assets.json`。所有新圖為內建 imagegen 示意，非推論。
- RD4AD 6 頁面狀態／24 次圖片放大等檢查通過，已看手機首圖及桌面失敗圖。仍需完成逐圖量表彙整，其他 10 課未製作、未發布、使用者核准 pending。

## WI-021 DRAEM 原型即將生成
- RD4AD 四圖本機接入，互動檢查進行中；接著 DRAEM C1。
- 四區：正常／合成訓練、待測重建、兩圖判別、位置覆核；brief `workitems/wi-021/draem-c1-r01.md`。
- 內建 imagegen，概念示意非實測；mask 僅訓練監督。預定 `draem-c1-r01-desktop.png`，未啟用、未評分，使用者核准 pending。

## WI-021 RD4AD 四圖本機接入（驗證中）
- 最後完成：C1 桌面 r04／手機 r01、C2 桌面 r02／手機 r01、D3 桌面／手機 r01；比較圖復用同案例 AE D5 r02。全部實際 PNG 與 328px 手機預覽已看；C1 簡化比較並改為純反向 decoder，C2 修正漏檢熱圖和更新線，D3 q 小孔位置一致。
- 即將執行：course/docs 三種視窗、24 次圖像／放大／自測／導覽檢查。`rd4ad-packet.json` 和 `integrate_lesson.py` 是正式圖文來源，原 topic／authority 保存在 baseline；產物 hash 在 `ad-rd4ad-active-assets.json`。
- 未完成：RD4AD 頁面實看及逐圖量表；其餘 11 課尚未製作，AE 其餘量表尚待整理。未發布，使用者核准 pending。

## WI-021 AE 本機整合 checkpoint／RD4AD 即將製作
- AE 最終十圖清單、尺寸與 SHA256：`workitems/wi-021/ae-active-assets.json`；C2 標籤、D4 q 熱區、D5 比較來源與手機瓶頸誤鎖已修正並實看。
- 生成模式：內建 imagegen 概念示意；所有原版及修改版、prompt 意圖保存在 workitems/wi-021，非模型實測。
- AE course/docs × 1440/390/360 共 6 狀態、30 張載入與放大、自測／導航／無溢出／無 JS error 通過，證據 `workitems/wi-021/qa-ae/report.json`。已實看 360px 首圖與桌面比較圖。
- tall-mobile 1、ad_f01 4、navigation 3、github-pages-bundle 1 測試通過；全站 verifier 既有 charuco inline mechanism visual 1 錯誤，沒有全站通過證據。
- 即將執行 RD4AD C1 桌面原型，`workitems/wi-021/rd4ad-c1-r01.md`，先驗 preflight；同板 A、教師特徵與反向學生特徵比較，正常瓶頸可訓練。其他 12 課尚未完成；AE 其餘逐圖及整頁量表待整理。使用者成品核准 pending，未發布。

## WI-017 SIFT + LightGlue R06 first-read（2026-09-08）

- 寫回：RULE-013、網頁指南、閱讀層「方法還是模型」。
- SIFT：OpenCV 120 keypoints、104 ratio matches、模糊後 4。C1 不是學習模型。
- LightGlue：教學示意，點用 SIFT 代替 extractor；C1 是 matcher 不是 detector/transform。
- live 兩課工程參考 0 圖。使用者審閱 pending。

## WI-016 ECC R06 C1–D5 first-read regenerated（2026-09-08）

- 生成：PIL + `findTransformECC`；同一金屬件照片；五張各答一問。舊 R04/R05 檔保留。
- 產物：`ecc-r06-c1-what.png`、`c2-how`、`c3-get`、`d4-stop`、`d5-pick`（各 1600×900 與 720×1280）。
- live h3：現場差幾個像素 → 怎麼做 → 交出位移與殘差 → 起點太遠 HOLD → 三個方法各管一段。
- 工程參考仍 0 圖。正式 slide 未改。使用者審閱 pending。不宣稱 >90。

## WI-015 site reading layers — engineering ref is text-only（2026-09-08）

- 三代理：`tmp/teaching-site-flow/01-inventory.md`、`02-reader-journey.md`、`03-critique.md`。
- 契約：`TEACHING_SITE_READING_LAYERS.md`。
- Builder：image-led「工程參考」不再放 figure。ECC 自截：該區 0 張圖、4 段 `.causal-step-text`。
- 未改 58 題正文。使用者核准 pending。

## WI-014 ECC R05 — what/how opener, not user-approved（2026-09-08）

- 使用者判定先前沒有介紹 ECC 是什麼、怎麼做。採納。
- 生成模式：PIL + `findTransformECC` MOTION_TRANSLATION；同一金屬件照片；紅藍疊圖顯示對齊前後。
- 產物：`ecc-r05-v1-what.png` 1600×900 SHA256 `7295e97fa972aa514104f2fe9c5007b47789fe5c3eac161c25d9b57e4bf4c437`；mobile SHA256 `0a9a9006cfc626230d6490e6f041a0b1add172d5f3bfc71b6e520289df3f477a`。
- 證據：設定位移 32、12 px，估得 32.14、12.07，對回 0.16 px，相關 0.999；takeaway 黃帶約 83%。
- live：h3「ECC 在做什麼？把已接近的畫面微調重合」；圖 936×527。R04 其餘四張未改。
- 未評 >90；使用者審閱 pending。

## WI-014 ECC slot self-inspect — docs was the tiny diagram（2026-09-08）

- Agent 自己用 Playwright 1440×1000 截圖，沒有請使用者看。
- `/interactive-learning.html`：r04 beginner 936×527、機制 full-width 894×503、正式 v03-r04 1010×568；無 hexagon。
- `/docs/index.html` 重建前：beginner 仍 r01/r02；機制 `<object>` SVG 388×194；正式仍 `v02-ppt-master-style`。這對得上使用者「還是小圖」截圖。
- 已重建 `docs/`（1307 assets）。重跑 `tools/audit_lesson_visual_slots.py ecc`：course 與 docs 槽位一致，failures=0。
- 流程已寫入 `TEACHING_VISUAL_SLOT_AUDIT.md` 與 Grok/Codex `teaching-visual-slot-audit` skill；稽核現在會比兩份 HTML 並量 CSS 寬。
- 生成模式：未重畫 PNG；本輪是插槽／docs 同步與自查工具。使用者審閱 pending。不宣稱 R04 >90。

## WI-014 ECC R01 — visual-1 candidate self-score pass, not user-approved（2026-09-07）

- 只做 visual 1 D 型候選。正式 `ecc.json` 未改（SHA256 `a5184c25ec0918a86af754e49065c3c263ec0ac86efd8a4a8cb88de29c344da7`）。F02 首圖 hash 不變。
- 生成模式：PIL 排版 + `tools/ecc_r01_evidence.py` `findTransformECC`；殘差為對齊圖紅疊＋共用顯示 vmax；反變換畫成模板↔原圖。
- 產物：desktop SHA256 `3eac1a6e2eb14bb63f3acf46c8a955bd74fc2dccbc19be6385d60c959c7d2546`；mobile SHA256 `31db80ea8f4c8f3846aacf54c777c5298783340730031b3e3fcb79875bd51903`。
- 測試：`tests/test_ecc_r01_recompute.py` 5 OK。Preflight PASS。自評桌面 93／手機 91。view_image 不可用。
- 使用者指出網頁仍是舊圖後，已把 visual 1 接到正式 `ecc.json` 並重建 `interactive-learning.html`／`docs/index.html`。HTTP 200 含 `ecc-r01-core.png`，F02 不再出現在 HTML。F02 檔保留。使用者審閱 pending。

## Local website startup (2026-09-07)

Existing localhost Python `http.server` already listening on `127.0.0.1:8000` (PID 152, started 2026-09-05 16:10:24). Verified HTTP 200 for `interactive-learning.html` (2,538,330 bytes, Vision AI course content). Issued default-browser launch to library view. No course rebuild, visual edits, or approval-state changes.

## WI-013 R08 integration candidate — 2026-09-06

- R08 candidate fixes integration geometry only; formal `charuco.json` remains unchanged at SHA256 `5298aecf02a3deaf1ef8d96755ad64bc6f58fea69c094aec93781c245cfe2895`.
- `full-mobile` candidate wrapper uses intrinsic `720x1660`; it removes the fixed 1672×941 nested mobile image path.
- Candidate topic, page, wrapper, and geometry contract are in `tmp/charuco-r08/`; the candidate references and verifies the same versioned mobile PNG (`charuco-r07-core-mobile.png`, SHA256 `fbb2e5962e40707bde6e9c12080f9128a75635db6917793f14a50674560d5a09`).
- Browser page recheck remains pending/unavailable; static geometry contract passed. Sol integration recheck is required; no formal acceptance or user approval.

## WI-013 R07 formal integration candidate — 2026-09-06

- Staged `tmp/charuco-r07/charuco-r07-topic-candidate.json` and `tmp/charuco-r07/charuco-r07-integration-packet.json`; formal `charuco.json` remains unchanged.
- Candidate points only the first beginner visual to versioned R07 PNG/SVG assets. R02–R06 assets remain preserved; no batch update or user-approval claim.
- Formal topic SHA256 before/after staging: `5298aecf02a3deaf1ef8d96755ad64bc6f58fea69c094aec93781c245cfe2895`.
- Awaiting Sol page recheck. Rollback is packet-only cleanup plus removal of versioned R07 copies; never delete R02–R06.

## WI-013 R07 candidate checkpoint — Luna — 2026-09-06

- R07 preserves R06 and earlier candidates; it only repairs layout collisions and remains disconnected from the formal topic.
- Desktop board provenance is now an independent caption outside panel 1; detector/c17 evidence is moved up with bottom padding. Mobile third-zone height/line spacing increased without crop; takeaway remains two lines with 30px side padding.
- R07 desktop/mobile PNGs were regenerated and both inspected with `view_image`; Microsoft JhengHei remains explicitly loaded. Hashes and board evidence are in `charuco-r07-manifest.json`.
- R07 brief preflight passes. Sol re-review and user approval remain pending; do not call this a pass or roll out batch changes.

## WI-013 R06 candidate checkpoint — Luna — 2026-09-06

- R06 is rebuilt from the actual R05 SVG source and preserves R02/R03/R04/R05; it is not connected to the formal topic.
- Fixed visible defects: both titles say R06; all correspondence uses `image q / board P`; board callouts point to m17, m23, and c17; desktop detector evidence is split; mobile takeaway is two lines with 30px side padding.
- R06 PNGs were generated with `PyQt5.QtSvg.QSvgRenderer` after loading `C:\Windows\Fonts\msjh.ttc` (`Microsoft JhengHei`, `Microsoft JhengHei UI`) and both were inspected with `view_image`.
- Preflight passes: `tmp/charuco-r06/brief.md`. Complete candidate evidence is in `charuco-r06-manifest.json`; user review remains pending and this is not a pass.

## WI-013 R03 delivery-gate checkpoint — Luna — 2026-09-06

- R03 candidate source is complete without replacing R02: `charuco-r03-core.svg`, `charuco-r03-core-mobile.svg`, and `charuco-r03-manifest.json`.
- P0/P1 source repairs: distinct m17/m23 patterns and separate c17; four non-collinear PnP correspondences; predicted c17 plus recomputable 1.00 px residual; P95/coverage/repeatability shown as REVIEW/HOLD; marker/chessboard counterfactual self-test recorded in the manifest.
- Actual PNGs exist at `tmp/charuco-r03/final/desktop.png` and `tmp/charuco-r03/final/mobile.png`, rasterized with PyQt5 QtSvg. Geometry was inspected, but the local Qt environment exposes no usable font families, so text appears as unreadable fallback blocks. This is not a visual pass.
- Preflight passes for the candidate brief only. Formal topic remains on R02; no user approval and no batch rollout.

## WI-013 R03 單張核心原型 checkpoint（Luna，2026-09-06）

狀態：已完成規範與交接閱讀，尚未生成圖像。R02 所有資產保留；本輪授權只做一張 R03 核心 prototype，不批量改寫其餘四張主圖、不改量表、不宣稱使用者接受。

- 目標：用一條 C 型路徑補足 `CHAR-P0-01` 真實板／身份、`CHAR-P0-02` 結合理由、`CHAR-P0-03` calibration/PnP 邊界，以及 `CHAR-P1-05` 固定 `c17` 追蹤。
- 已落盤：`tmp/charuco-r03/brief.md`；生成模式為 native SVG 精確繪圖，數值只作教學設定，沒有新增模型推論。
- 正在進行：繪製桌面／手機 SVG，預期輸出 `_course_content/generated-concepts/charuco/charuco-r03-core.svg/.png`、`charuco-r03-core-mobile.svg` 與 R03 manifest。
- 下一步：用 Edge Playwright 匯出 `tmp/charuco-r03/final/desktop.png`／`mobile.png`，實看兩張 PNG，再更新候選引用與本狀態。
- 驗證：preflight 尚未重跑；PNG 尚未實看；Sol 複審、使用者審閱、真人理解證據均未取得。

## WI-013 Sol→Luna→Sol：整章重評完成，等待 Luna 原型（2026-09-06）

Sol 已檢查 R02 首圖桌面／手機、五張 beginner 主圖桌面／手機截圖、topic 主線與可取得資產；頁面固定量表為 72/100，五張主圖為 60/65/64/71/72，三張輔助圖未評估。舊 92 分自評因量表與證據判定過寬撤回有效性。

現行問題：真實 ChArUco 標靶與 marker/corner 身份不足；未先教結合 ArUco 與棋盤的理由；calibration/PnP 邊界混淆；P50/P95/coverage/PASS 缺可回算證據；同角點無法追蹤；手機核心結果不可同屏。

Sol 已建立 `CHARUCO_R02_SOL_TO_LUNA_HANDOFF_2026-09-06.md`，問題 ID `CHAR-P0-01` 至 `CHAR-EVID-11` 均含修訂與驗收條件。Luna 尚未修改；不得批量推展。

Luna checkpoint：已完成 `tmp/charuco-r03/brief.md`、preflight、`charuco-r03-core.svg`、`charuco-r03-core-mobile.svg` 與 `charuco-r03-manifest.json`；R02 仍為正式引用。R03 PNG 尚未產生／實看，Edge／Playwright 子程序遇 `WinError 5`，所以 Sol 複審與新分數尚未開始。這些候選 SVG 不等於成品驗收，也不等於使用者接受。

Sol delivery-gate 複核：R03 不可評分；四個 marker 重用同一圖樣、PnP 文字需改為至少四組適當非共線 correspondence、0.8 px 缺 predicted c17 座標、P95／coverage／repeatability 無具名門檻或樣本，正式自測／comparison 尚未接入。所有視覺與頁面分項維持 blocked／未評估；下一步先修 source-level 缺口並產出實看 PNG，使用者接受仍未取得。

使用者已確認持續執行 `Sol 審查 → Markdown 交接 → Luna 修訂 → Sol 複審`。目前進入下一輪 R03 原型修訂；尚未產生新 PNG、尚未取得 Sol 通過或使用者接受。若同一問題連續兩輪未改善，Sol 將改寫修訂方案與構圖，不以文字補充或調整分數結案。

Browser runtime 清單為空；standalone Playwright 在 sandbox 遇 `WinError 5`，未假稱即時全頁驗收。三張輔助圖最終渲染、lazy-load、導航、放大、答案互動仍未評估。使用者接受仍未取得；目前狀態待修訂。

## WI-013 最新審查：首圖 60/100、待修訂（2026-09-06）

- 後續能力確認：使用者指定 Playwright，已以 Python sync_playwright、Chromium 的 msedge channel、headless、1440×1000 開啟指定 URL 並取得 DOM。首屏截圖 `tmp/charuco-playwright-check/desktop.png` 已實看。這是獨立瀏覽器，不是連入使用者現有分頁；內建 runtime 不可用不代表本機 Playwright 不可用。未點擊完成／收藏，未修改教材，未完成整章或手機評分。

- 現行 HTML 與 HTTP 圖片確認仍引用 R02；圖片與本地 bytes 相同。首張 PNG 已實看，固定量表 14/25 + 13/25 + 12/20 + 15/20 + 6/10 = 60/100。
- 舊 92 分因分項不符量表、證據判定過寬而撤回；不以歷史 test-complete 或 pending user review 推定已達品質門檻。
- 問題：數字方格不是可教正確交點的 ChArUco 板；板上身份到 q/P 不可追蹤；混合標靶的核心利益不足；P95/coverage/PASS 搶走入門重點。
- 本輪只审查與寫回 Markdown，沒有生成／修改圖像、沒有重建或部署；generation mode/prompt/saved asset：不適用。
- 驗證限制：browser runtime 無可用實例，未測實際桌面／手機 DOM、導航或放大；其餘圖片未逐張實看，不給整章分數。
- 完整分項、來源、學習與下一步：根目錄 TEACHING_REVIEW_LOG.md 最新 WI-013。使用者接受仍未取得；教材狀態待修訂。

## WI-013 ChArUco R02 checkpoint（2026-09-06）

| 項目 | 狀態 | 證據 |
|---|---|---|
| 五份指定 Markdown 已讀取並寫入 preflight | implementation-complete | `tmp/charuco-r02/brief.md` |
| C 型四節點 prototype | implementation-complete | `charuco-r02-core.svg` / `.png` |
| 桌面／手機實際 PNG 檢視 | test-complete | `tmp/charuco-r02/final/desktop.png`、`mobile.png` |
| 網頁與 docs 重建 | test-complete | `interactive-learning.html`、`docs/index.html` 含 `charuco-r02-core` |
| 本機 URL 桌面 runtime QA | test-complete | `tmp/charuco-r02/final/page-desktop.png`；R02 asset、無水平溢出、無 page error |
| 本機 URL 手機 runtime QA | test-complete | `tmp/charuco-r02/final/page-mobile.png`；R02 asset、無水平溢出、無 page error |
| 使用者意義與風格核准 | pending | `quality_status.current_revision = R02 prototype awaiting user review` |

R02 主線是「標定板與 marker ID → 2D↔已知板座標 → pose 回投影與 P50/P95 → 全 FOV PASS/HOLD」。自評只記錄為 prototype evidence，不代替使用者評分。

### 目前模型狀態（2026-09-06）

| 系列 | 主題數 | 已修訂 | 待修訂 |
|---|---:|---:|---:|
| 幾何、校正與對位 | 4 | 0 | 4 |
| 分類、分割與姿態 | 8 | 8 | 0 |
| 物件偵測與開放詞彙 | 6 | 6 | 0 |
| 異常偵測 | 17 | 17 | 0 |
| 時間序列、運動與影片 | 8 | 0 | 8 |
| Foundation Vision、語意檢索與 VLM | 7 | 0 | 7 |
| Diffusion、合成與影像復原 | 8 | 0 | 8 |
| **合計** | **58** | **31** | **27** |

> 使用者已撤回 WI-012 F02 的可用性判定。幾何、影片、Foundation／VLM、Diffusion 共 27 題目前全部標為「待修訂」；現有資產只保留作為重製前的失敗基準。

## WI-012 F02 — 27 題核心重建撤回，全部待修訂（2026-09-06）

### G0：範圍與基線

本輪接續全站盤點：58 個正式 topic 中，分類／分割／姿態 8 題、偵測 6 題與異常偵測 17 題已有近期核心修訂；本輪處理幾何 4 題、時間／影片 8 題、Foundation／VLM 7 題、Diffusion／復原 8 題，共 27 題。每題以現行 `_course_content/topics/<slug>.json`、對應 `roadmap-model-selection/**/model.md`、原有第一張案例圖與 `TEACHING_SCORING_RUBRIC.md v1.0` 為基線。

### G1：學習與取捨（先於生成）

採納既有 F01 原則：第一眼先回答「原本遇到什麼困難」，核心圖要讓輸入、模型專屬轉換、可交付輸出與人的下一步可追蹤，最後用移除核心設計的後果做自測。部分採納舊批次的成功做法：保留同一案例與既有詳細章節；不採納把全站所有模型畫成同一個三欄模板，也不把影像生成結果、embedding、flow、mask、復原圖或文字回答誤稱為量測真值。

家族 brief：

- 幾何（ChArUco、ECC、SIFT、LightGlue）：影像點、模板／局部特徵、幾何變換與 residual／correspondence 要分開；未通過 coverage、初始化、匹配品質或重裝驗證時 HOLD。
- 時間／影片（Frame Difference、Background Subtraction、Lucas–Kanade、RAFT、ByteTrack、ConvLSTM、VideoMAE、V-JEPA）：明畫時間戳與 frame window，分清變化、稠密／稀疏 flow、track identity、預測／表徵；不要把彩色 flow 或 latent 直接當事件真值。
- Foundation／VLM（DINOv2、DINOv3、CLIP、SigLIP、LLaVA、Qwen-VL、Gemini Vision）：分清 feature、image-text similarity、token 對齊與 provider／LLM 回答；任何 score、box、mask、量測或放行都要有命名的下游 owner。
- Diffusion／復原（DefectFill、AnomalyDiffusion、TF-IDG、ControlNet、Inpainting、Diffusion Restoration、Deblur、Super-resolution）：raw、condition、generated／restored estimate 與 review 必須分開；生成／復原改善可讀性不等於還原物理真值，也不覆蓋 raw evidence。

### G2–G3：製作方式與原型

沿用既有各題第一張案例圖作案例身分參考，新增 native SVG 機制總覽；每個家族先用一張代表圖檢查，再批次生成其餘 26 題。左側保留既有案例素材，右側只畫該模型的代表性輸入→轉換→輸出→接手；圖面明示「F02 機制示意，非模型推論」。手機版改為上方案例、下方縱向機制，避免縮小桌面圖造成讀不懂。

### G4–G6：驗證與再學習

成圖檢查先遮住長正文，確認每張圖仍看得到模型特有的關係；再在網站中檢查桌面／手機、放大、章節、自測與頁寬。分數只記新增核心圖的逐圖證據，保留舊圖不沿用歷史高分。若圖只有名詞框而沒有可見轉換，視為需重製；若核心輸出是設定或下游計算，直接標示證據身分。

生成模式：native SVG + 各 topic 現有案例 PNG；未新增模型推論、性能比較或外部部署。實際資產：`_course_content/generated-concepts/<slug>/<slug>-f02-core.svg`、同名 `.png`、`-core-mobile.svg` 及 `f02-manifest.json`。原型與逐圖證據寫入 `tmp/f02-series/`，完成後回填本輪結果。


## WI-012 F02 撤回與待修訂核對（2026-09-06）

本輪 27 題已產生資產與整合頁面，但使用者判定成品質量太差、不可使用；因此 27 題全部撤回為待修訂。 31 題既有近期修訂維持已修訂狀態。

- [x] 幾何 4 題：ChArUco、ECC、SIFT、LightGlue。
- [x] 時間／影片 8 題：Frame Difference、Background Subtraction、Lucas–Kanade、RAFT、ByteTrack、ConvLSTM、VideoMAE、V-JEPA。
- [x] Foundation／VLM 7 題：DINOv2、DINOv3、CLIP、SigLIP、LLaVA、Qwen-VL、Gemini Vision。
- [x] Diffusion／復原 8 題：DefectFill、AnomalyDiffusion、TF-IDG、ControlNet、Inpainting、Diffusion Restoration、Deblur、Super-resolution。

每題已更新 topic JSON 的「為什麼需要、三個核心設計、移除核心自測、換情境 transfer、選型」；對應 model.md 已加入 F02 核心與來源橋接。HTML／docs 已重建，27 題共 270 個桌面／手機頁面狀態通過實際 runtime QA。這是 implementation-complete 與 test-complete；尚未宣稱使用者核准、真人理解或真實模型效能。

持久證據：`teaching-images/vision-ai-model-selection/f02-review.json`、`tmp/f02-series/`、本檔 WI-012 F02 final，以及課程 `BEGINNER_VISUAL_TODO.md`／`BEGINNER_VISUAL_STATUS.md`。

### F02 final evidence

- [x] 27 題 topic JSON、27 個 model.md、54 個桌面／手機核心 SVG、27 個 PNG 與 27 個 manifest 已保存。
- [x] 58 題 HTML 重建；source verifier、contract、navigation、bundle、deep-dive regression 與 270 狀態 runtime QA 通過。
- [x] 每題第一張圖直接顯示「為什麼需要」與三個核心要點；手機版保留縱向案例到人工接手流程。
- [x] 27 題 final desktop first-read 核對完成；未見裁切、核心流程缺失或水平溢位。
- [!] 使用者已判定本輪品質不可用；27 題全部待修訂，不能作為可用教材。

證據：`f02-review.json`、`tmp/f02-series/<slug>/report.json`、`_course_content/generated-concepts/<slug>/<slug>-f02-core.svg/.png`、`<slug>-f02-core-mobile.svg`、`f02-manifest.json`。

## WI-011 F01 — 本輪 17 題核心修訂與工具驗證完成，待使用者審閱

- [x] 保存基準、核對 17 題第一手來源、參考圖與逐題製作 brief。
- [x] 製作並檢視 17 組核心圖（34 個桌面／手機視圖），完成圖後修正。
- [x] 17 題頁首存在理由、可見三要點、反事實與換情境自測、model.md 同步。
- [x] 三個深入主題後續七章逐字保存，首章舊圖仍可切換。
- [x] 188 個章節狀態與 17 個最終頁首驗證；必要回歸、來源／docs verifier 通過。
- [x] 本機 HTML／docs／新資產 hash 與 HTTP 核對，學習回寫共用 log 與指南。
- [?] 真人理解與使用者審閱尚未取得；保留舊圖沒有在本輪全部重新評分，不宣稱整套全面達標。

入口：http://127.0.0.1:8000/interactive-learning.html?rev=ad-f01#view=lesson&lesson=ad-patchcore&slide=1

記憶與證據：`ad-f01-brief.md`、`ad-f01-review.json`、根目錄 `TEACHING_REVIEW_LOG.md` WI-011。生成模式：原生 SVG 搭配既有生成金屬件，PNG 為瀏覽器匯出；特徵與差異皆為教學設定。資產：`_course_content/generated-concepts/<topic>/<topic>-f01-core.svg/.png` 與 `-core-mobile.svg`，各題 `f01-manifest.json` 記錄來源與保存路徑。

本輪新增 37 個啟用資產；發布資料夾引用 1298 個資產。HTML SHA256：`d915635d43a9f69bca7bdce8910130b038d545b9ed62862ec81634a50b45b1ef`。未執行外部部署。後續從使用者指出的具體圖與理解缺口接續，不用自行重跑舊版 renderer。

WI-009 D01已完成本輪圖文重製及驗證（2026-09-06），待使用者審閱。六題各四幅主線、三個可見核心要點、移除設計及新情境自測；28個啟用資產。49項測試、48章節狀態、兩份HTML verifier及來源／bundle／HTTP一致性檢查通過。逐圖路徑、模式、設計意圖、分項、hash及限制見d01-detector-review.json和共用log WI-009。沒有新模型推論或外部部署，不宣稱已永久收斂。

WI-008-R1已完成：核實上一輪Markdown學習記憶、外部總評逐項取捨及共用規則整合；詳見根目錄TEACHING_REVIEW_LOG.md的WI-008-R1。七題正式topic SHA256與E03紀錄一致。原報告自述核對E01/E02，不能當E03完整重評；本輪未重新出圖、未改頁面、未跑新瀏覽器／回歸，也未新增教學分數。下輪候選與驗證方法已寫入TODO，未標成已實作。

目前最新：E03七題中心思想修正、ResNet回查及驗證完成，待使用者審閱；詳見檔尾E03完成紀錄及core-e03-review.json。

## A12 current A10 opinion review (2026-09-05)

Confirmed the active topic snapshot SHA-256 `8b56b191611e53767857fdd08b22e8331ddebd71f964b0cb1bc2c75d25529f30` contains A10 chapter-2 mobile views and chapter-4 location/arithmetic views. Actual A10 final renders were inspected. The redesign is materially better: chapter 4 now exposes the location grid, spatial enlargement and top-1% arithmetic as separate three-stage stories; chapter 2 mobile keeps the whole-image input, fixed DINOv2, query features, visible reference candidates and nearest result together. These changes reduce conceptual overload rather than merely enlarging the old diagram.

The current lesson is good but not finished. The visible EfficientAD comparison view contains clipped red source text across the central workflow; PatchCore remains symbolic rather than traceable to product patches; retained chapters 1 and 5 are still dense; chapter 3 normal evidence and chapter 8 success evidence remain limited. Therefore the A10 review result remains page 91 with chapter weakest-view scores `86, 90, 88, 93, 90, 93, 87, 89`, and the complete set still needs improvement. No new asset or page change was made in this review-only step; user approval is not inferred.

## A11 active A09 formal re-score (2026-09-05)

Scored the active topic snapshot modified 21:19:42, SHA-256 `E3C664B9837D497498CE9901D7F137D0C80F7553955CF99E1CE6FDFECBC3D92C`. It uses retained figures 1/5 plus 16 A09 progressive views for chapters 2/3/4/6/7/8. The A10 location prototype is not yet integrated and receives no credit. Browser runtime remained unavailable; all saved A09 desktop views, representative mobile views and its zero-error width report were inspected.

Rubric v1.0 result: page 90/100 `[19,18,19,17,8,9]`; chapter-group scores use the weakest active view: `86, 90, 88, 88, 90, 93, 88, 89`. Only chapter 6 clears the strict >90 group gate. Progressive views substantially reduce overload, but chapter 1 remains dense; chapter 2 query and chapter 3 normal counterexample remain partly abstract; chapter 4 arithmetic is still numeric-led; chapter 7 PatchCore uses symbolic rather than traceable product patches; chapter 8 success view is a single low-resolution positive example. No veto identified. Status remains needs revision and is not user-approved.

## AnomalyDINO v02 visual scores corrected by user (2026-09-05)

The user rejected the earlier high visual scores and supplied image-by-image replacements: 78, 68, 66, 79, 80, 72, 60 and 84. These values supersede the earlier 91–94 image scores. All eight active images fail the strict >90 gate, so v02 is now marked needs revision rather than release-ready. The earlier review incorrectly credited page copy, technical correctness, provenance, arithmetic and layout cleanliness as evidence that the images themselves communicated clearly. It also rewarded a consistent three-column renderer and repeated workpiece even when processing, reference influence, candidate differences and method comparisons remained text-dependent.

RULE-012 is now active in the root scoring rubric and both shared guides: score the image alone first, hiding page copy and reviewer knowledge; require visible input/object, processing or comparison, changed result and next action; do not let text boxes, unexplained numeric differences or repeated identical outputs earn high visual-meaning scores. No images were regenerated in this review-only turn. User approval is not recorded.

## AnomalyDINO v02 independent rereview (2026-09-05)

Reviewed the complete active AnomalyDINO v02 as a review-only teaching cycle using eight rendered figures, current chapter copy, desktop/mobile captures, all 25 mobile semantic crops, QA JSON and the authors' paper. The in-app browser had no available connection. Fixed-rubric result: 94/100 [19,20,19,18,9,9], no veto. The lesson correctly connects fixed DINOv2 features, full-memory nearest-neighbor cosine distances, top-1% image aggregation, a separate localization path, reference contamination, masking/rotation tradeoffs and conditional model choice. The cited author Figure 1 is clearly separated from the A-01 illustrative case and local inference claims. Remaining evidence gaps are local real inference and a same-condition comparison against PatchCore/EfficientAD; these are explicitly disclosed. Review completion is not user approval.

## Independent v11 rereview complete (2026-09-05)

Reviewed the user's newest complete EfficientAD revision as a review-only teaching cycle. Used the active v11 topic, all eight v11 screenshots, desktop case/tradeoff evidence, five mobile vertical-step captures and runtime report; the in-app browser had no available connection. Cross-checked the new efficiency explanation against the primary paper's PDN, early downsampling, single fully-convolutional forward and shared Student hidden-layer rationale. Independent fixed-rubric result: 94/100 [19,20,19,18,9,9], no veto. v11 resolves the prior efficiency-story and mobile cognitive-load findings and strengthens tradeoff reasoning. Real inference and same-condition model benchmarking remain absent but are explicitly labeled rather than fabricated. Review completion is not user approval.

## v11 regenerated and validated (2026-09-05)

Completed both requested actions: updated teaching-review-cycle skill to require actual regeneration and handle combined skill+next-round requests; regenerated active teaching as v11. Chapter 1 now explains PDN/early downsampling/shared Student computation and S/M tradeoffs. Chapters 1/2/6 ask conditional choices involving capacity, data quality/coverage, and missed defects/review volume. Chapter 6 mobile rendering has five vertical stages using validated crops from the same full diagram; desktop and full-image enlargement remain available. First crop inspection found arrow remnants; refined crops and regenerated before final QA.

Generation: deterministic code-native SVG, no real inference or bitmap ImageGen. Intent: clarify efficiency and make the same A-01 decision flow readable vertically without changing values or identity. Generator: tools/render_efficientad_mechanism.py. Saved assets under `_course_content/generated-concepts/ad-efficientad/`: efficientad-work-01-work_v11.svg, efficientad-work-02-data_v11.svg, efficientad-work-03-meaning_v11.svg, efficientad-work-04-output_v11.svg, efficientad-work-05-limits_v11.svg, efficientad-work-06-workflow_v11.svg, efficientad-work-07-comparison_v11.svg, efficientad-work-08-transfer_v11.svg. Images 2–8 byte-identical to v10; first image and authored text changed. Mobile crops are opt-in chapter metadata, not extra untracked images. Contract design recorded in openspec/changes/mobile-teaching-steps/proposal.md.

Final self-review under unchanged rubric: page 93; images 93,93,92,94,92,94,93,93; five mobile views 94 each, all completion dimensions >=8, no identified veto. Shared EAD-005 contains evidence and deductions. Final captures in root tmp/efficientad-redesign-20260905/cycle-v11 (including mobile-step-1..5 and tradeoffs). HTML verifier, 3 mobile contract/browser tests, 5 ResNet regressions, 3 navigation and 1 bundle test pass. Scenario arithmetic independently verified; eight-figure/page QA has no overflow or page errors, navigation/self-check/enlarge/Escape pass. Full suite not rerun. Local bundle rebuilt (1,177 assets); no external publication. Skill quick_validate passes.

User approval pending. Real model outputs and same-condition benchmarks remain absent; this iteration does not claim to resolve those evidence gaps. Local entry: http://127.0.0.1:8000/interactive-learning.html?rev=efficientad-v11#view=lesson&lesson=ad-efficientad&slide=6 .

## Actual regeneration v11 underway (2026-09-05)

User explicitly requested both stronger skill wording and the next teaching round. Skill now requires source/asset/page regeneration and active-version verification, including combined skill+production requests. EAD-005 records adopted improvements before implementation: efficiency explanation, meaningful scenario tradeoffs and mobile vertical reading for the full case. Preserve eight chapters, fixed rubric and explicit non-empirical evidence boundary. Validation pending.

## Reusable review-cycle skill created (2026-09-05)

Validation complete: skill-creator quick_validate reports valid. Local checks pass for all linked references, YAML, literal skill invocation in default_prompt, UI description length, implicit invocation policy and both 100-point totals. Manually reviewed intent paths (critique-only, regenerate, skill-only, missing evidence); no independent agent simulation or new teaching cycle was executed. Installed in the personal skills discovery directory; availability in the current already-loaded catalog is not assumed. Skill can be addressed by its name or absolute SKILL.md path.

User asked for a reusable skill, not a new page version in this turn. Recorded latest critical learning in root guides/rubric as RULE-010 and shared log WORKFLOW-001. Created personal `C:/Users/hctsa/.codex/skills/teaching-review-cycle/` with SKILL.md, agents/openai.yaml, a default rubric for projects lacking one and visionAI routing reference. Skill separates critique-only from production, requires evidence-based adoption decisions and Markdown learning before regeneration, fixes score inflation and false evidence risks, and resumes from shared records. No page/image generation, no new lesson score; v10 remains active and user approval remains separate.

## Independent rereview of user-revised EfficientAD v10 (2026-09-05)

Re-reviewed the complete revised lesson using all eight mechanism-v10 figure captures, focused desktop/mobile chapter 3/6/7 captures, current topic copy, numerical QA and the EfficientAD paper abstract. The earlier central criticism is resolved: chapter 3 now correctly gives one Student two output groups and separates Teacher-versus-S1 local evidence from AE-versus-S2 global evidence; chapter 6 follows the same A-01 workpiece through raw discrepancies, percentile normalization, 0.20/0.02 fusion to 0.11, threshold comparison and human review; chapter 7 states fair-run conditions instead of asserting an unsupported winner; scenario checks now appear throughout the decision path. Reviewer judgment: the chapter is now coherent and release-worthy for the intended practical audience. Remaining improvement space is narrower: explain visually why EfficientAD is efficient (lightweight PDN and S/M/runtime tradeoff, without transferring paper latency claims to local hardware), show one real inference example when trustworthy evidence is available, and make the mobile horizontal-reading affordance slightly more discoverable. No lesson files were changed and user approval remains pending.

## Core mechanism and continuous case v10 delivered (2026-09-05)

Wrote shared RULE-009 before regenerating: explain necessary roles/comparisons, trace one case into a work decision, distinguish toy arithmetic from empirical evidence, and place scenario questions at decision points. Rebuilt twice (v09→v10). v09 figure 6 scored 88 because numeric grids dominated and the final action was relegated to a footnote; v10 uses workpiece overlays and a visible score/threshold/review chain. Full nine-cell arithmetic is preserved in EFFICIENTAD_WORKPLACE_GUIDE.md. No changes to shared runtime or other lesson contracts.

Generation mode: deterministic code-native SVG using tools/render_efficientad_mechanism.py, importing prior reusable drawing helpers. Prompt/design intent: make Teacher, Student output groups and AE cooperation explicit; follow A-01 into local/global discrepancies, normalized fusion, maximum score and human decision; state fair comparison conditions. Saved assets: `_course_content/generated-concepts/ad-efficientad/efficientad-work-01-work_v10.svg`, `efficientad-work-02-data_v10.svg`, `efficientad-work-03-meaning_v10.svg`, `efficientad-work-04-output_v10.svg`, `efficientad-work-05-limits_v10.svg`, `efficientad-work-06-workflow_v10.svg`, `efficientad-work-07-comparison_v10.svg`, `efficientad-work-08-transfer_v10.svg`. No ImageGen bitmap or real inference; no fabricated benchmark numbers.

Final fixed-rubric self-review: page 93; images 93,93,92,94,92,94,93,93; all five completion dimensions >=8, no identified technical veto. Detailed evidence/deductions in root TEACHING_REVIEW_LOG.md EAD-004. Evidence folder root tmp/efficientad-redesign-20260905/mechanism-v10: eight screenshots, desktop/mobile, focused chapters 3/6/7, text and QA JSON. Numeric trace independently checks all nine positions, score 0.11 and illustrative >0.08 rule; chapter 2/3/4/6 answer reveals pass in both viewports. No SVG overflow or page errors; navigation, zoom edges, Escape pass. HTML verifier, 3 navigation and 1 bundle tests pass. Full suite not rerun. Local docs rebuilt (1,177 assets), not externally deployed.

User review remains pending. Real output evidence and common-hardware benchmarking remain absent and are explicitly distinguished from the illustrative case; scores describe teaching quality, not proven learning or model performance. Local URL: http://127.0.0.1:8000/interactive-learning.html?rev=efficientad-v10#view=lesson&lesson=ad-efficientad&slide=3 .

## Core mechanism revision started (2026-09-05)

User requested writing the critical review lessons into shared Markdown and regenerating. Recorded RULE-009 before implementation. Preserve eight chapters; strengthen Teacher/Student/AE cooperation and a continuous numerical case, qualify comparison conditions, place scenario decisions where useful. No claim of real model inference or user acceptance. Validation and regeneration pending.

## User clarification: complete EfficientAD lesson review (2026-09-05)

The user clarified that `slide=5` was only the current URL position and requested an assessment of the complete EfficientAD chapter. Reviewed all eight preserved workplace-v08 figures plus the desktop/mobile validation evidence because the in-app browser had no available connection. The complete lesson is strong in workplace framing, normal-only data preparation, local-versus-global anomaly meaning, output ownership, capture failure modes, POC workflow, method comparison and transfer to a changed requirement. Its main remaining gap is model-specific understanding: the visible path does not yet give a sufficiently concrete frozen-teacher/student/autoencoder walkthrough, explain the student's output groups, or trace one real or numeric example from branch discrepancies through fusion, image score, threshold and review decision. Repeated stylized workpiece diagrams provide continuity but little authentic evidence, and the final self-check is less active than the scenario-driven lesson deserves. Recommendation: preserve the practical eight-chapter spine, strengthen one central mechanism chapter, add one evidence-backed end-to-end inference case, qualify the PatchCore comparison with measured conditions, and add scenario decisions with immediate feedback. No files were regenerated and no user approval is recorded.

## EfficientAD workplace v08 complete for review (2026-09-05)

Rewrote the complete eight-part teaching lesson and generated all eight workplace figures. Two actual rounds v07→v08, using root TEACHING_SCORING_RUBRIC.md v1.0 without changing weights. v07 page 87 and images 81–94 failed, including a product-identity veto. v08 fixes visible normal variation, loss of scratch signal while preserving the workpiece, and consistent product B inputs/outputs. Shared root TEACHING_REVIEW_LOG.md EAD-003 records detailed per-category scores, deductions, fixes and RULE-008 learned into both guides. Final self-review page 92/100; individual images 93,93,92,94,92,92,93,93; all completion dimensions >=8. No identified veto; user approval pending.

Generation mode: deterministic code-native SVG, no ImageGen raster and no model inference. Design/prompt intent: explain normal-only preparation, two complementary cues, anomaly heatmaps versus contour needs, capture limitations, workflow cost, EfficientAD/PatchCore/supervised-segmentation tradeoffs, and transfer to a new product/requirement. Saved final assets: `_course_content/generated-concepts/ad-efficientad/efficientad-work-01-work_v08.svg`, `efficientad-work-02-data_v08.svg`, `efficientad-work-03-meaning_v08.svg`, `efficientad-work-04-output_v08.svg`, `efficientad-work-05-limits_v08.svg`, `efficientad-work-06-workflow_v08.svg`, `efficientad-work-07-comparison_v08.svg`, `efficientad-work-08-transfer_v08.svg`. Source generator: tools/render_efficientad_workplace.py. Teaching Markdown: roadmap-model-selection/anomaly-detection/ad-efficientad/EFFICIENTAD_WORKPLACE_GUIDE.md. v07 images and baseline source remain preserved.

Actual final evidence: root tmp/efficientad-redesign-20260905/workplace-v08, including all eight SVG screenshots, desktop/mobile/zoom screenshots, page text and report.json. No SVG text overflow or page errors; 1440/390 viewport navigation, self-check, enlargement, reachable image edges and Escape pass. HTML verification and 5 focused regression tests pass (3 navigation, 1 bundle, 1 zoom). Full-site suite not rerun. Local docs bundle rebuilt, 1,177 referenced assets. No external deployment. Local entry: http://127.0.0.1:8000/interactive-learning.html?rev=efficientad-v08#view=lesson&lesson=ad-efficientad&slide=1 . Mobile uses horizontal image reading. Scores reflect reviewer judgment, not a user study or user acceptance.

## EfficientAD workplace rewrite in progress (2026-09-05)

Created root TEACHING_SCORING_RUBRIC.md v1.0 as the single current rubric. Rewrote all eight chapters and generated eight `efficientad-work-*_v07.svg` files using tools/render_efficientad_workplace.py. Mode: deterministic code-native SVG; intent: concrete workpieces, visible anomaly/output differences and workplace choices, no measured output claim. Actual screenshots and interactions in root tmp/efficientad-redesign-20260905/workplace-v07. EAD-003 records page 87, image 81–94 and the image-8 identity veto. Revision is in progress; not yet complete or user-approved.

## Audience clarified: practical understanding and model choice (2026-09-05)

The user explicitly wants learners to understand model meaning, connect it to actual work, and recognize tradeoffs across models, without overly academic content. Updated root TEACHING_WEBPAGE_GUIDE.md to v0.3 and the opening of IMAGE_STYLE_GUIDE.md with this priority. Shared TEACHING_REVIEW_LOG.md AUDIENCE-001 records the distinction between confirmed audience objectives and proposed teaching approaches. Prior scores remain historical; the earlier chapter-six-only repair is not a full audience-alignment redesign. This turn updates direction and documentation only, with no page/image regeneration or new quality score. Full lesson reassessment is now an unchecked task.

## User correction: images before arithmetic (2026-09-05)

The user rejected chapter 6's formula-led teaching despite the previous high self-score. EAD-002 in the single root review log records that correction; v05 is not user-approved. Replaced chapter 6 with `efficientad-deep-06-fusion_v06.svg`: deterministic SVG, one consistent workpiece, two raw maps, two aligned maps and a fused overlay, plus normal-reference samples. Intent: show the purpose and observable effect of scale alignment; all maps explicitly qualitative illustrations, not measured model output. Main-page points and self-check now focus on interpreting background versus anomaly; exact formulas moved to the concept document's advanced section. No ImageGen bitmap generation. Other seven chapter assets remain v05.

Updated IMAGE_STYLE_GUIDE.md and TEACHING_WEBPAGE_GUIDE.md with RULE-007, an explicit user preference for visual meaning before arithmetic in beginner teaching. Inspected actual full-size SVG screenshot and desktop/mobile chapter views in root tmp/efficientad-redesign-20260905/v06; no SVG text overflow or page-wide horizontal overflow, self-check and v06 loading pass. HTML verifier and bundle test pass; local docs rebuilt. Figure-only self-score 92/100 is provisional reviewer judgment, not user approval or a new whole-site score. Entry: http://127.0.0.1:8000/interactive-learning.html?rev=efficientad-v06#view=lesson&lesson=ad-efficientad&slide=6 .

## EfficientAD v05 delivered locally (2026-09-05)

Implemented the requested new webpage as an eight-chapter EfficientAD deep dive using the existing opt-in course renderer. Added `tools/render_efficientad_deep_dive.py`, eight `efficientad-deep-*_v05.svg` assets, authored topic deep_dive and `roadmap-model-selection/anomaly-detection/ad-efficientad/EFFICIENTAD_MODEL_CONCEPT.md`. Generation mode: deterministic SVG with a consistent four-recess workpiece, labelled hypothetical maps and arithmetic; no bitmap ImageGen or actual inference outputs. Prompt/design intent and every output are recorded in root TEACHING_REVIEW_LOG.md EAD-001. Prior v04 and baseline source/HTML are preserved under the existing asset directory and root tmp/efficientad-redesign-20260905/baseline.

Two image/content rounds corrected arrow direction, training-target relationships, numerical continuity and source labels. Actual mobile inspection additionally found an oversized concept SVG centered beyond the reachable left edge; changed concept lightbox alignment to start and added test_concept_zoom_edges.py. Learned reusable rules were written into both root guides and the single shared review log.

Final self-review: webpage 93/100; each image 92–94/100 with all five completion dimensions >=8/10, no identified technical veto. User approval remains pending. Evidence in root tmp/efficientad-redesign-20260905/final includes eight full-size images, desktop/mobile, enlarged views, stable chapter-eight views, page text and report.json. Both viewport checks pass, no page errors or SVG text overflow, image edges reachable. HTML verifier passes; 5 ResNet, 3 navigation, 1 bundle and 1 zoom regression tests pass. Full-site 403-test suite was not rerun. Local docs bundle rebuilt with 1,177 referenced assets; no external publication. Entry: http://127.0.0.1:8000/interactive-learning.html?rev=efficientad-v05#view=lesson&lesson=ad-efficientad&slide=1 .

## Shared autonomous review workflow established (2026-09-05)

The user confirmed a single shared review log rather than per-topic logs. Created root TEACHING_REVIEW_LOG.md with a common index, historical EfficientAD entry (62/100 under its original rubric), rule register, and per-round evidence/scoring template. Updated TEACHING_WEBPAGE_GUIDE.md to v0.2 with section 14 and IMAGE_STYLE_GUIDE.md with section 12. Both specify strict >90/100 for the webpage and each active instructional image, no averaging, technical vetoes, stable rubrics, preserved versions, actual desktop/mobile and per-image inspection, and separate user approval. Existing image completion dimensions remain >=8/10. New subjective lessons remain hypotheses until supported; user preference requires explicit feedback. This turn establishes the documentation workflow; no new teaching page/images have been generated or scored. First production-round scope was asked asynchronously, with EfficientAD suggested. Documentation link/fence/threshold checks are the applicable validation; no runtime or image-generation completion is claimed.

## Reusable teaching webpage guidance (2026-09-05)

Created `../../TEACHING_WEBPAGE_GUIDE.md` at the user's request. It generalizes the EfficientAD review into teaching goals, progression, mechanism specificity, traceable examples, figure/text alignment, web interactions, learning checks, priorities, a proposed scoring rubric, an authoring brief, and a reusable AI review prompt. Consulted IMAGE_STYLE_GUIDE.md, especially sections 11.10 and 11.11, existing review records, saved desktop-top.png, and page-text.txt. Evidence scope is explicit: no fresh full-site/mobile audit; the prior 62/100 remains a historical topic-specific review score under its original rubric. Guidance is a proposed draft pending user review, not confirmed preference. No lesson or image edits and no generated assets. Documentation validation checks cover local Markdown link targets, paired code fences, and rubric weights summing to 100.

Last updated: 2026-08-31 (Asia/Taipei)

## ResNet eight-chapter implementation (2026-08-31)

The user explicitly requested a full ResNet lesson rewrite and regenerated
explanatory imagery, using the root `IMAGE_STYLE_GUIDE.md` as the example. The
implemented page is an eight-chapter, source-backed deep dive covering the
classifier contract, residual addition, BasicBlock/Bottleneck stage shapes,
training versus inference and BatchNorm state, global-pooling observability,
softmax calibration and OOD review, depth/cost evidence, and a fair
ResNet/ConvNeXt/ViT selection decision. Each chapter has a full-width
mechanism visual, three authored learning points, a self-check, and direct
paper, official-code, or official-documentation source links. `slide=1..8`
now navigates the actual ResNet chapters, while the generic beginner and
legacy reference blocks are hidden on this deep-dive page.

The persistent model explanation is
`roadmap-model-selection/known-target-classification/resnet/RESNET_MODEL_CONCEPT.md`.
The offline `interactive-learning.html` and deployable `docs/` bundle were
rebuilt. The shared renderer and the other 57 authored topic contracts were
not changed; the HTML validator was generalized from one to any number of
eight-chapter model deep dives.

### Generated asset record

Generation mode for the concrete workpiece anchor: built-in ImageGen, default
generation. Prompt intent: create a photorealistic, text-free 16:9 industrial
AOI scene with exactly one precision-machined rectangular aluminum workpiece,
a stable repeatable fixture, and a top-mounted inspection camera; use neutral
silver, charcoal, and restrained blue-gray materials; leave clean margins for
later overlays; exclude people, text, labels, arrows, UI, logos, watermarks,
heatmaps, boxes, synthetic defects, clutter, dramatic glow, duplicated parts,
and impossible optics. The saved project asset is:

- `_course_content/generated-concepts/resnet/resnet-industrial-known-class-anchor_v03.png`

Generation mode for the eight teaching mechanisms: deterministic code-native
SVG from `tools/render_resnet_deep_dive_visuals.py`. Prompt/design intent: use
the Style Guide's white 1672x941 canvas, C/D causal-story archetypes, large
labels, restrained blue/cyan/green/orange/purple semantic color, and one pale
yellow engineering takeaway; keep exact shapes, arrows, gates, responsibilities,
and technical text reproducible instead of asking an image model to draw them.

- `_course_content/generated-concepts/resnet/resnet-deep-01-task-output_v03.svg`
- `_course_content/generated-concepts/resnet/resnet-deep-02-residual-addition_v03.svg`
- `_course_content/generated-concepts/resnet/resnet-deep-03-stage-shapes_v03.svg`
- `_course_content/generated-concepts/resnet/resnet-deep-04-train-infer-bn_v03.svg`
- `_course_content/generated-concepts/resnet/resnet-deep-05-pooling-observability_v03.svg`
- `_course_content/generated-concepts/resnet/resnet-deep-06-calibration-ood_v03.svg`
- `_course_content/generated-concepts/resnet/resnet-deep-07-variants-evidence_v03.svg`
- `_course_content/generated-concepts/resnet/resnet-deep-08-selection-decision_v03.svg`

### Validation record

- All eight SVGs are 1672x941; visible text is at least 18px and browser text
  bounding boxes remain inside each canvas.
- Desktop 1440x1000 and mobile 390x844 Playwright QA passed. The runtime shows
  eight chapters and eight figures, supports `slide=8`, centers the active
  mobile navigation item, and produces no document-wide horizontal overflow.
- ResNet runtime DOM QA confirmed zero `.teaching-primer` and zero
  `.formal-slide-reference` blocks on the deep-dive page.
- `python tools/build_interactive_learning_html.py` and
  `python tools/verify_interactive_learning_html.py interactive-learning.html`
  passed: 58 topics, 232 topic images, 291 baseline first-read visuals, 16
  deep-dive visuals across SegFormer and ResNet, 87 shared images, and 567
  instructional images total.
- GitHub Pages bundle contains 1,168 referenced assets, including raster
  dependencies referenced from SVG teaching visuals;
  `tests/test_github_pages_bundle.py` and `tests/test_interactive_navigation.py`
  passed.
- Focused ResNet suite passed 5 tests. Full regression command
  `python -m unittest discover -s tests -p "test_*.py"` passed 403 tests in
  351.040 seconds.

Implementation and automated validation are complete. Final semantic and
visual approval remains pending user review and is not claimed here.

## SegFormer eight-chapter implementation (2026-08-20)

The user agreed to the proposed SegFormer-specific redesign scope. The lesson
is now implemented as an eight-chapter deep dive: semantic task/output,
ROI/label/tile/checkpoint contract, four-stage MiT shapes, Overlap Patch +
sequence-reduction attention + Mix-FFN internals, exact MLP decoder shape
flow, separate training/inference pipelines, B0-B5 evidence and cost framing,
and comparison/HOLD decisions. Each chapter has a full-width mechanism visual,
three authored takeaways, a self-check, and direct paper or official-code
source links. `slide=1..8`, chapter buttons, and left/right keys now locate the
actual chapter instead of toggling the historical four-slide details block.

The page no longer renders the four clipped historical engineering PNGs.
Those files remain recoverable through `slide-manifest.md`, where their state
is now `reference-only`; the QA log records why they are no longer first-read
assets. Other 57 topic render paths were not changed. The persistent concept
source is
`roadmap-model-selection/known-target-classification/segformer/SEGFORMER_MODEL_CONCEPT.md`.

### Generated asset record

Generation mode: deterministic, code-native SVG from
`tools/render_segformer_deep_dive_visuals.py`; built-in bitmap image generation
was not used. Prompt intent: explain one SegFormer-specific relationship per
full 1672x941 canvas, keep the same wafer AOI evidence anchor, make shapes and
responsibility boundaries explicit, and avoid inventing model predictions.
Chapter 02 intentionally reuses the existing contract SVG.

- `_course_content/generated-concepts/segformer/segformer-deep-01-task-output_v01.svg`
- `_course_content/generated-concepts/segformer/segformer-beginner-02-contract-overlap-patches_v01.svg` (reused)
- `_course_content/generated-concepts/segformer/segformer-deep-03-stage-shapes_v01.svg`
- `_course_content/generated-concepts/segformer/segformer-deep-04-mit-block_v01.svg`
- `_course_content/generated-concepts/segformer/segformer-deep-05-decoder-shapes_v01.svg`
- `_course_content/generated-concepts/segformer/segformer-deep-06-train-infer_v01.svg`
- `_course_content/generated-concepts/segformer/segformer-deep-07-variants-evidence_v01.svg`
- `_course_content/generated-concepts/segformer/segformer-deep-08-comparison-decision_v01.svg`

### Validation record

- All eight assets are 1672x941; all visible SVG text is at least 18px and all
  browser text bounding boxes stay inside the canvas.
- Desktop 1440x1000 and mobile 390x844 runtime QA passed. Mobile diagrams use
  a contained 920px horizontal reading surface without causing document-wide
  overflow, and the active chapter is centered in the sticky navigation.
- Runtime DOM QA confirmed eight new chapter figures, zero `.teaching-primer`
  blocks, and zero `.formal-slide-reference` blocks for SegFormer.
- `interactive-learning.html` and `docs/index.html` both pass the offline HTML
  validator: 58 topics, 232 topic images, 291 baseline first-read visuals,
  eight SegFormer deep-dive visuals, 87 shared images, and 559 instructional
  images total.
- GitHub Pages bundle contains 1,122 referenced assets including the concept
  Markdown; `tests/test_github_pages_bundle.py` passed.
- Full regression: `python -m unittest discover -s tests -p "test_*.py"`
  passed 398 tests in 138.755 seconds.

Implementation and automated validation are complete. Final semantic and
visual approval remains pending user review and is not claimed here.

## Current result

The active beginner lesson has been restored to the preserved v01 baseline
across all 58 topics and 291 beginner-path visuals. The source of truth is
`_course_content/audit/beginner-visual-redesign-review.json`: 282 `_v01`
assets plus nine historical specialized assets intentionally retained from
their original versions.

The Ref process v03 renderer, assets, manifests, and audit outputs are kept as
historical recovery material only. They are not the active visual shell and
must not be used to describe the current site or its approval state.

No topic is marked user-approved. The user selected the available v01 baseline
after the immediately pre-v03 in-place source files were found to be
unrecoverable.

## GitHub Pages publication (2026-08-18)

The public static site bundle was built into `docs/`: `docs/index.html` and
1,114 referenced assets (266.3 MB). The initial Pages commit
`71aef06 Deploy interactive Vision AI course to GitHub Pages` was pushed to
`https://github.com/hctsaik/visionAI_Model_Introduce` on `main`. The GitHub
CLI in this environment has no authenticated API session, so Pages itself has
not been enabled programmatically. Enable it in GitHub repository settings by
choosing `main` and `/docs` as the branch publishing source.

## Active outputs and archived v03 records

- `_course_content/topics/*.json`: 58 topic references restored to the
  historical review inventory.
- `_course_content/generated-concepts/`: active assets are the 291 files from
  the historical inventory; retained v03 files remain inactive.
- `interactive-learning.html`: rebuilt offline site.
- Archived: `_course_content/audit/beginner-visual-generation-master-manifest.json`:
  291/291 implemented, pending user review.
- Archived: `_course_content/audit/beginner-visual-redesign-metrics.json` and related
  CSV/Markdown: latest automated redesign audit is 291 KEEP / 0 PARTIAL /
  0 REDO after the beginner-copy pass.
- Archived: `_course_content/audit/ref-process-clarity-audit.json`: 58 topics / 291
  visuals PASS for the Ref five-stage and family-semantic contract.

## Recent parallel generation batches

All batches below used four parallel built-in image-generation lanes. The
bitmap prompt prohibited text, labels, arrows, diagrams, UI, watermarks,
heatmaps, and synthetic defects; exact teaching copy remains deterministic
SVG. All four jobs in each listed batch succeeded on the first attempt.

- Foundation wave 1 manifest:
  `_course_content/audit/image-generation-batch-2026-08-17-foundation-wave-1.json`
  - DINOv2: `_course_content/generated-concepts/dinov2/dinov2-industrial-ceramic-carrier-anchor_v02.png`
  - DINOv3: `_course_content/generated-concepts/dinov3/dinov3-industrial-ceramic-carrier-anchor_v02.png`
  - CLIP: `_course_content/generated-concepts/clip/clip-industrial-ceramic-workpiece-anchor_v02.png`
  - SigLIP: `_course_content/generated-concepts/siglip/siglip-industrial-ceramic-workpiece-anchor_v02.png`
- Foundation wave 2 manifest:
  `_course_content/audit/image-generation-batch-2026-08-17-foundation-wave-2.json`
  - Qwen-VL: `_course_content/generated-concepts/qwen-vl/qwen-vl-industrial-variable-input-anchor_v02.png`
  - LLaVA: `_course_content/generated-concepts/llava/llava-industrial-question-contract-anchor_v02.png`
  - Gemini Vision: `_course_content/generated-concepts/gemini-vision/gemini-vision-industrial-client-workpiece-anchor_v02.png`
  - AnomalyCLIP: `_course_content/generated-concepts/ad-anomalyclip/anomalyclip-industrial-ceramic-contacts-anchor_v02.png`
- Anomaly wave 4 manifest:
  `_course_content/audit/image-generation-batch-2026-08-17-anomaly-wave-4.json`
  - WinCLIP: `_course_content/generated-concepts/ad-winclip/winclip-industrial-ceramic-contact-anchor_v02.png`
  - AnomalyGPT: `_course_content/generated-concepts/ad-anomalygpt/anomalygpt-industrial-metal-plate-anchor_v02.png`
  - DiffusionAD: `_course_content/generated-concepts/ad-diffad/diffad-industrial-ceramic-cap-anchor_v02.png`
  - SubspaceAD: `_course_content/generated-concepts/ad-subspacead/subspacead-industrial-normal-panel-anchor_v02.png`

The archived deterministic migration uses `_v02` anchors before older v01
anchors and explicitly preserves the five-slide YOLO Dense v02 references.
This prevents a resumable rerun from silently replacing the accepted baseline
with a generic first-read card.

## Generation record

The archived site-wide shell pass used deterministic local SVG generation and Edge
rasterization. The recent foundation and anomaly waves additionally used
parallel built-in image generation for new physical workpiece anchors; their
prompts, source outputs, attempts, and target paths are recorded in the dated
manifests above. The saved site outputs remain the 291 `_v02.svg` sources and
58 `_v02.png` first-read renders under `_course_content/generated-concepts/`.

## Historical v03 validation record

- `python tools/verify_interactive_learning_html.py interactive-learning.html`
  passed: 58 topics, 232 topic images, 291 first-read visuals, 551 total
  instructional images, offline embedded data, no `fetch()`.
- `python tools/audit_beginner_svg_readability.py` passed: 58 reviewed,
  0 flagged below 18px.
- `python tools/audit_image_led_migration.py` passed: 58 candidates,
  0 replacements required; shared visible assets also pass.
- `python tools/audit_beginner_visual_redesign.py --write` passed: 291 KEEP,
  0 PARTIAL, 0 REDO.
- `python tools/audit_ref_process_clarity.py` passed: 58 topics, 291 visuals,
  291 PASS.
- `python tools/qa_image_led_runtime.py` passed for all 58 topics at desktop
  and 390px mobile widths after the Ref redesign; no SVG text leaves the
  1672x941 canvas.
- Direct all-asset contract check passed: 58 topics, 291 visuals, 58 PNGs;
  every current v02 SVG has the Ref process marker, five numbered stages, at
  least 4 arrows, an evidence anchor, and the 1672x941 canvas.
- `python -m pytest tests/test_all_beginner_visual_migration.py
  tests/test_anomalydino_beginner_path.py -q` passed: 13 tests.
- `python -u -m pytest -q` passed: 394 tests and 3,997 subtests in 244.95s.
- Rerun after the parallel waves passed: migration produced 58 topics / 291
  visuals / 57 non-specialized first-read rasterizations, and the focused
  migration/audit/image-led gate passed 21 tests.
- Full image-led runtime rerun passed for all 58 topics at desktop and 390px
  mobile widths after the latest resumable migration.
- A browser-heavy full-suite run previously reached 392 passed before the
  remaining shared-renderer checks; the final authoritative gates are the
  focused migration tests plus the full 58-topic runtime and HTML audits.

## Review state and remaining risk

Implementation and automated validation are complete. User review remains a
separate approval record for semantic accuracy and whether each existing
raster anchor is the preferred teaching example; no approval has been claimed.

## Active visual baseline rollback (2026-08-18)

At the user's request, the active 58-topic / 291-visual beginner path has
been restored to the preserved v01 baseline in
`_course_content/audit/beginner-visual-redesign-review.json`. The inventory
contains 282 `_v01` assets plus 9 deliberately retained historical specialized
assets (8 `_v02` and one `_v03`); filename suffixes are not used as a proxy for
their intended version. `interactive-learning.html` was rebuilt from this
mapping and passed its offline HTML verification.

The Ref process v03 SVG/PNG files and generation scripts remain on disk but
are no longer referenced by topic JSON or the generated lesson. Its v03-only
audits and validation figures below are historical records, not claims about
the active site. The immediately pre-v03 in-place `_v02` state could not be
recovered because those source files were overwritten and no repository history
or backup existed; the user selected the available v01 historical baseline.

Validation after the v01 restore:

- `python tools/build_interactive_learning_html.py` rebuilt the lesson with 58
  topics, 291 first-read visuals, and 551 instructional images.
- `python tools/verify_interactive_learning_html.py interactive-learning.html`
  passed: all visible assets are 1672x941, embedded offline data has no
  `fetch()`, and the HTML parser passed.
- `python -m pytest tests/test_all_beginner_visual_migration.py
  tests/test_anomalydino_beginner_path.py
  tests/test_segdet_beginner_svg_readability.py -q` passed: 16 tests.
- `python -u -m pytest -q` passed: 393 tests and 3,997 subtests in 243.95s.

The active mapping test now compares every `(topic, visual_id)` to the 291-item
historical review inventory, rather than asserting the retired v03 marker or a
uniform filename suffix. Ref-specific style instructions were removed from
`PREFERRED_SLIDE_STYLE.md`.

## DINOv2 complete-concept review (2026-08-18)

The user requested a full DINOv2 concept introduction and a review of the
interactive DINOv2 lesson against that level of completeness. The durable
Markdown source is now
`roadmap-model-selection/foundation-vlm-open-world/dinov2/DINOv2_MODEL_CONCEPT.md`.
It records model positioning, label-free Teacher/Student self-supervised
training, ViT patchification/inference, global and patch outputs, the
Good/Bad group-to-heatmap application flow, comparisons with classifier,
detector and VLM families, implementation controls, limits, and primary
sources.

The interactive DINOv2 page was previously technically careful about
Good/Bad patch comparison and downstream Heatmap ownership, but did not make
the model's self-supervised training and deployment distinction sufficiently
visible. Its learner brief, expandable first-read source copy, and synced
`model.md` bridge now state that Teacher/Student is a training mechanism,
deployment uses the encoder, and the native outputs are global embedding plus
patch tokens—not defect, box, mask, or Heatmap. The full concept Markdown is
linked from `model.md`, which the page exposes through its "查看 model.md" action.

Validation after this content change:

- `python tools/sync_model_learning_bridges.py --write`: updated 1 DINOv2
  `model.md` bridge.
- `python tools/build_interactive_learning_html.py`: passed, 58 topics / 232
  topic images.
- `python tools/verify_interactive_learning_html.py interactive-learning.html`:
  passed, including offline data and all 551 instructional images.
- `python -m pytest tests/test_dinov2_beginner_visuals.py
  tests/test_dinov2_architecture_c_story.py tests/test_dinov2_contract_c_story.py
  tests/test_dinov2_c_story.py tests/test_dinov2_selection_d_story.py -q`:
  12 passed.

## Why the earlier audits still missed unclear content

The earlier pass measured mostly structural proxies: asset existence, image
dimensions, arrows, numbered cards, font floor, and a takeaway keyword. Those
checks could pass a generic card deck even when a beginner could not answer
four essential questions: what goes in, what the model actually does, what it
really outputs, and what the engineer does next. The renderer also reused one
generic story across different model families and carried a fixed `YOLO
Defense` badge into DINO and non-YOLO topics. Browser canvas overflow was not a
completion gate either.

This pass fixes the process rather than only the visible symptoms: the shared
renderer now has a five-stage Ref contract, family-specific stage copy, DINO
Good/Bad same-position patch comparison, a dedicated semantic audit, and a
desktop/mobile SVG bounding-box runtime gate. A green structural audit alone
is no longer treated as evidence that the teaching story is clear.

## Maintenance

Read `BEGINNER_VISUAL_TODO.md` and this file before future material actions.
After any regeneration, update the generated paths, generation mode/prompt
intent when applicable, validation commands, and user-review state here.

## Latest user review: DINOv2 / DINOv3 and attached references

On 2026-08-18, the user supplied four visual references showing an explicit
engineering storyline: Good/Bad image groups, same patch positions, group
embedding comparison, patch difference scores, heatmap back-projection, and
the handoff from image evidence to process improvement. The four attachments
are visible in the conversation but are not available as local files to copy;
the existing workspace `C:\code\claude\visionAI\ref` directory is empty.
No substitute DINOv2 slides were copied as if they were those attachments.

The current DINOv2 and DINOv3 introductions were inspected in their topic JSON
and rendered first-read PNGs. They are technically careful about input
contracts, feature outputs, downstream ownership, and evidence gates, but the
first-read story is not sufficiently concrete for a beginner: it does not show
what is compared, why the same patch position is collected across a group, how
a patch score becomes a heatmap, or how that heatmap becomes a process clue.
The first-read PNGs also retain the generic `YOLO Defense · v02` shell badge,
which is a misleading presentation detail for DINO topics.

The attached style has now been applied as a DINO-specific application
storyline and as the shared site-wide visual contract. The redesign states
that DINOv2/DINOv3 provide global or patch features; group statistics,
difference scores, heatmaps, and process actions are downstream steps. DINOv3
is framed as a controlled baseline comparison, not automatically as “better”
or as a detector. The exact four original attachments are still not copied
because the chat attachments are not exposed as local source files; the
workspace `ref` directory remains empty rather than containing substitutes.

## Local website startup (2026-09-05)

Later startup request: restarted the localhost-only Python server (PID 23588) and verified HTTP 200 plus the EfficientAD topic in the served HTML. The command containing default-browser launch was rejected by execution policy, so the user receives a clickable local URL. No lesson edits or approval-state changes.

Started Python http.server bound to 127.0.0.1:8000, serving the existing course directory. Entry: http://127.0.0.1:8000/interactive-learning.html#view=library . Verified HTTP 200 and Vision AI page content. No course rebuild or visual changes; user-review status unchanged. Logs: tmp/vision-ai-site.stdout.log and tmp/vision-ai-site.stderr.log (repository root).

## EfficientAD teaching review (2026-09-05)

User requested evaluation of ad-efficientad slide=1. Reviewed topic JSON, model.md, rendering logic, retained EFFICIENTAD-01-positioning PNG and beginner SVG markup; cross-checked WACV 2024 paper and nelson1425/EfficientAD predict implementation. Browser discovery returned no available browser, so live layout/interactions and full visual quality are not scored. Provisional beginner-teaching score: 60/100 (accessibility 10/20, sequencing 11/20, mechanism explanation 14/25, worked evidence 9/15, boundaries 13/15, learning checks 3/5). Strengths: shared workpiece, local/global distinction, calibration and deployment boundaries. Gaps: jargon precedes explanation, student output groups and AE target unclear, PDN efficiency and losses underexplained, no concrete score walkthrough, checks emphasize HOLD over mechanism. Logical-anomaly capability should be explained positively before limiting guarantees. Retained reference diagram visually suggests serial local-to-global processing. These are reviewer findings, not user-approved changes. No lesson or image edits.

## Authorized standalone browser verification (2026-09-05)

User explicitly authorized independent Playwright after discussing the Browser skill restriction. Python Playwright with headless Edge successfully loaded the exact EfficientAD lesson URL: HTTP 200, h1 EfficientAD, no pageerror events. Inspected desktop-top.png at 1440x1000; actual first screen includes plain-language four-card primer and local/P95 definitions, so the previous source-based accessibility assessment needs reconsideration against the rendered page. Saved desktop-top.png, desktop-full.png and page-text.txt in repository-root tmp/efficientad-browser-review/. Browser plugin transport remains unavailable; independent Playwright is verified working. No lesson edits or user visual approval.

## EfficientAD rendered lesson reassessment (2026-09-05)

Inspected 1440x1000 desktop first screen, default-visible page text, all five rendered beginner figures (actual-figure-1 through actual-figure-5.png), and expanded lesson text. Reviewer score 62/100: entry readability 14/20, progression 10/20, mechanism 13/20, visual evidence 8/20, engineering boundaries 13/15, learning checks 4/5. This supersedes the prior source-only 60 as a broader desktop-content assessment, not learner-study evidence. Confirmed plain-language summaries and collapsed advanced material deserve credit. Concrete defects: first figure is a square plate with four recesses, later figures use a ring assembly while claiming same workpiece; visible fourth/fifth generic headings concern stopping/comparison while the figures concern local/global counterfactuals and HOLD respectively; P95 described as slowest of 20 is imprecise; repeated primer/callout statements add length without explanation. Missing student output-group distinction and numeric map walkthrough remain. Screenshot capture initially targeted hidden reference images and timed out; successful subsequent capture used visible images/objects. No content changes; no user approval implied.


## AnomalyDINO review cycle A01（2026-09-05，進行中）
已保存 baseline 與閱讀作者原文／程式，基線網頁69、五圖78–85。共用學習先寫入根目錄 RULE-011。下一步實際重製；預定使用可重現程式 SVG（圖解），作者 Figure 1 僅作有來源的公開輸出證據，未執行模型推論。使用者尚未審閱新版本。


### AnomalyDINO A03 / v02 完成狀態（2026-09-05）
使用者授權的本輪已完成：基線69→重製v01自評89→修正v02自評93；八張啟用圖各91–94，量表v1.0未改。使用者尚未審閱，沒有使用者核准或現場實測效能宣稱。

生成：`tools/render_anomalydino_deep_dive.py`，可重現程式SVG；資產目錄 `_course_content/generated-concepts/ad-anomalydino/`。圖01–08分別為 `anomalydino-work-01_v02.svg`、`02_v02.svg`、`03_v02.svg`、`04_v02.svg`、`05_v02.svg`、`06_v02.svg`、`07_v02.svg`、`08_v02.svg`（後七項同前綴）。設計意圖依序：同工件初探、共享固定模型、最近鄰、200格完整數值流程、參考更新反例、前處理／排列限制、條件式比較、作者實際输出。圖1–7非AI生成照片或真推論；圖8內嵌作者Figure1之局部視窗。原PNG為 `anomalydino-author-figure1.png`，來源、SHA與引用界線已寫入根目錄共用紀錄。

八章來源 `_course_content/topics/ad-anomalydino.json`，全文 `roadmap-model-selection/anomalydino-workplace-deep-dive.md`。已重建 `interactive-learning.html` 與 `docs/index.html`（1186資產），沒有外部部署。驗證：HTML結構、7項既有聚焦測試、HTTP桌機／手機導覽與放大、逐圖視覺、全部25個手機分段與算術核對通過；證據在 workspace `tmp/anomalydino-review-20260905/v02/`。

兩輪學習／分項分數及扣分全部在唯一根目錄 `TEACHING_REVIEW_LOG.md`；共用RULE-011同步到兩份指南。新入口：http://127.0.0.1:8000/interactive-learning.html?rev=anomalydino-v02#view=lesson&lesson=ad-anomalydino&slide=1 。下一步由使用者閱讀回饋決定重開項目；如取得可靠實測資料，再做效果與成本比較。

### AnomalyDINO A04：目前有效狀態為需重製（2026-09-05）
使用者明確指出圖片評分偏高。重新檢視v02全部八圖並核對指南第11節後，撤回A03的自評達標結論。量表v1.0不改，逐圖修正為78、68、66、79、80、72、60、84；各項與完成度、證據、扣分理由見根目錄共用TEACHING_REVIEW_LOG.md的A04。先前93及91–94只保留為歷史錯誤評分，不能作驗收依據或跨輪客觀提升曲線。

主要原因：正文知識被借給圖片加分、技術與排版通過被當成視覺教學通過、先固定三欄renderer再填內容、未先選母版檢查單張原型；第7圖相同輸入／熱圖沒有表達方法差異，第3圖候選缺可見與可追查的局部證據。圖片風格未獲使用者核准；原技術驗證結果仍只在其既有範圍有效。

本次為評分檢討與共用學習，未新生成資產，網頁仍為v02。已更新IMAGE_STYLE_GUIDE.md與TEACHING_SCORING_RUBRIC.md的執行解釋、TODO及共用紀錄。後續優先重製圖7、3、2，先驗單圖原型；完整網頁分數待連同新成圖校準，不以暫估新分數補齊。

### A05：共用影像循環已寫入skill（2026-09-05）
依使用者要求將A04全部根因映射到可執行G0–G6規則：有效規則／基線、實看參考與逐圖brief、工具選擇、單張原型、成圖審查、據證評分、學習再生成。專案規則在根目錄IMAGE_STYLE_GUIDE.md RULE-012，完整可攜流程在 `C:/Users/hctsa/.codex/skills/teaching-review-cycle/references/image-production-cycle.md`；SKILL.md已加入必讀路由。共用log A05記錄映射、責任與承諾界線。

本次新增的是規則與技能，沒有新生成影像，生成模式／資產仍同v02；頁面未重製。A04的需重製狀態與60–84圖片分數維持，使用者尚未核准成圖。後續循環不能因本次技能完成而跳過原型或改稱視覺達標。

技能驗證：quick_validate以Python UTF-8模式通過（初次cp950讀中文失敗已解決）；必讀路由、對接與UI政策已檢查，五種任務情境已人工走查。未執行新圖生成或真人理解測試，不宣稱驗證器能保證視覺品質。

### A06進行中：修正錯誤停止（2026-09-05）
使用者再次指出原要求包含持續重製。A04/A05把後續文件指示誤當範圍替代，並要求下次授權才製作，是Codex的執行錯誤；原授權一直有效。本輪已提取並實看PPTX第1/2/4頁，寫入 `tmp/anomalydino-review-20260905/a06/PRODUCTION_BRIEF.md`，使用內建image_gen開始第7章比較圖原型。後續持續產圖、更新網頁與驗證；skill已補上跨回覆保留未完成製作目標的規則。未宣稱新成圖達標。

### A07：重新學習循環（2026-09-05，進行中）
已實看PPTX第2頁與圖7 v03，學習已先寫入共用log A07。將以內建image_gen定向修正Teacher關係及特徵相簿比喻；啟用仍為v02，原型未核准，後續製作與頁面驗證待完成。


A07本輪結果：圖7已用內建ImageGen產生v04–v09共六張候選，保存於_course_content/generated-concepts/ad-anomalydino/，逐版prompt意圖及修正結果在共用log。最新v09為86/100，專業完成度7/10，未達標、未核准。已執行並實看隔離桌機／手機原型，證據tmp/anomalydino-review-20260905/a07/。本輪未修改正式topic或重建bundle：發現另一流程同時更新第1/2/3/8圖與topic，第7圖已由該流程啟用v04，因此先前全v02狀態已過時。已詢問使用者協調寫入責任；新v09暫留候選，不覆蓋並行工作。完整製作仍未完成。


### A06最終實際狀態（取代A06進行中描述）
已完成八章實際重製與啟用：網頁自評93，八圖94/92/91/93/94/93/91/92，固定量表v1.0。生成模式：圖1–7內建image_gen新生成／定向編輯，圖8保留作者PNG原像素的SVG視窗。意圖、失敗候選、來源路徑與SHA詳見 workspace tmp/anomalydino-review-20260905/a06/PRODUCTION_BRIEF.md、generation-manifest.json，唯一評分紀錄在根目錄TEACHING_REVIEW_LOG.md A06。A07候選檔案保留，未採用其v09。
啟用資產：
- _course_content/generated-concepts/ad-anomalydino/anomalydino-work-01_v04.svg
- _course_content/generated-concepts/ad-anomalydino/anomalydino-work-02_v04.svg
- _course_content/generated-concepts/ad-anomalydino/anomalydino-work-03_a06-final.svg
- _course_content/generated-concepts/ad-anomalydino/anomalydino-work-04_v03.png
- _course_content/generated-concepts/ad-anomalydino/anomalydino-work-05_a06-final.png
- _course_content/generated-concepts/ad-anomalydino/anomalydino-work-06_v03.png
- _course_content/generated-concepts/ad-anomalydino/anomalydino-work-07_a06-final.png
- _course_content/generated-concepts/ad-anomalydino/anomalydino-work-08_v03.svg
八章topic、concept Markdown、interactive-learning.html及docs/index.html已更新。HTML驗證、7項聚焦測試、桌面1440/手機390導覽、自測、放大與29分段檢查通過；證據tmp/anomalydino-review-20260905/a06-final/。本機bundle1186資產，未外部部署。
使用者尚未審閱／核准；沒有本機真實推論、共同效能實測或真人理解證據。生成局部是概念示意，只有第8圖保留來源像素。後續依讀者回饋重開，不以自評作驗收。
入口：http://127.0.0.1:8000/interactive-learning.html?rev=anomalydino-v03#view=lesson&lesson=ad-anomalydino&slide=1

### A08 現版缺點審查（2026-09-05，取代全面自評達標狀態）
使用者指出目前圖片可能太複雜；結論採納。本輪確認正式topic為A06/anomalydino-v03資產組，實看八張a06-final成圖、啟用第7張及既有手機完整圖與分段圖，核對topic和原論文。Browser runtime無可用連線，因此未宣稱重新操作即時頁面。整體複雜度為圖7非常高、圖4高、圖2/3/6中高；圖1/5/8主故事較清楚。手機裁切改善字體大小，但沒有自動減少概念數。
另發現圖2輸入流程易誤读、圖3/4跨圖工件與局部對應不足、圖7換線產品不一致及模型產物仍用相簿、手機裁切丟失比較上下文、圖8真實案例不足。後續應讓每個可見畫面只負責一個主要問題與近三個主要階段，將詳細算術、例外及跨模型工作移到漸進步驟或次層；細節與驗證方式在唯一共用TEACHING_REVIEW_LOG.md A08。
A06網頁93／圖片91–94僅保留歷史紀錄，撤回其作為現版全面達標依據；技術整合完成、視覺教學需簡化與修正、使用者未核准。本輪未正式逐項計分，未新跑介面測試。生成模式／prompt／資產沿用A06，沒有生成或改教材／部署。

### A09 ???

A09製作進度：第7張原型修正後已展開，共產生16組桌面／手機SVG視圖（第2/3/4/6/7/8章）。使用既有生成影像的原像素視窗與新生成第7圖原型素材；作者Figure6/7以原PNG嵌入，未經生成模型重畫。第2/3/4章共用work來源與query/scratch固定座標。圖4算術獨立視圖，圖6一次一個反例，第7章一次一種方法，圖8成功／漏檢／誤報可切換。正在實看檢查，尚未接入正式topic；路徑與SHA於a09/generation-manifest.json，prompt於a09/imagegen-prompts.json。

### WI-002：持久工作記憶已建立（2026-09-05）
使用者因 Codex 經常當機，要求將工作項目、TODO 與接續設計保存到 Markdown。已建立根目錄 WORKITEMS.md，將 A09 設為 WI-001 目前接續項目；AGENTS.md 加入開始先讀、長操作前落盤、每個可驗證步驟後更新 checkpoint、恢復時核對產物和程序、完成需驗證證據等規則。專用 TODO 頂端補上 A09 唯一細項清單，舊 A07/v02 紀錄保留為歷史。
最新接續點仍為 A09 候選視圖的實際檢查；尚未整合正式 topic，尚未完成本輪桌面／手機驗證與使用者審閱。本次無新生成，生成模式／prompt／素材沿用 A09，路徑见 WORKITEMS.md。僅修改工作記憶文件，未改教材或部署。文件落盤與連結檢查另於本次工具結果保存。

### 2026-09-05 即時版本核對（取代先前「尚未整合」摘要）
詢問是否上線時重新核對：正式 ad-anomalydino.json 已引用 A09；teaching-images/vision-ai-model-selection/interactive-learning.html 已包含 anomalydino-02-store_a09.svg，修改時間為 21:10:24；http://127.0.0.1:8000/interactive-learning.html 實際 HTTP 回應也包含該 A09 引用。因此本機頁面已更新；外網部署、本輪完整驗證及使用者核准尚未確認。先前未整合紀錄已落後於磁碟，不能再當目前狀態。下一步核對完整 A09 驗證證據與 bundle／外網狀態，再決定剩餘工作；不要重複整合。此次只確認回應文字含新版引用，未宣稱瀏覽器視覺驗收通過。

### WI-003 / A10 開始（2026-09-05）
已保存A09基準，閱讀固定量表與技能、實看PPTX第4頁及A09局部圖。正在全頁截圖審查；準備獨立SVG原型補強第4章「局部距離保留位置→熱區→回原圖」。生成方式為既有工件原像素＋精確SVG，尚未生成或整合，brief與來源已先寫共用log A10。下一步執行capture.py並逐圖檢查；證據tmp/anomalydino-review-20260905/a10/。使用者核准待審。

### A10 checkpoint：已整合，待驗證（2026-09-05）
已產生6個SVG：第2章正常／待測手機圖、第4章定位與算術桌面／手機圖，檔名含_a10，位於_course_content/generated-concepts/ad-anomalydino/。模式：既有原像素嵌入＋程式SVG；未呼叫新ImageGen、未重畫作者輸出。設計意圖與失敗修正已記共用log A10；正式topic僅改第2章手機引用、第4章兩視圖與說明，其他六章逐項比較確認保留。整合前topic備份、引用SHA在tmp/anomalydino-review-20260905/a10/topic-before-integration.json、integration.json。已實看新原型，正在重建、進行本輪介面驗證；尚未宣稱整頁達標或使用者核准。


### A09 製作、驗證與並行交接（2026-09-05）

已實際產出並整合：第7張內建ImageGen新原型與一次定向編輯；另生成高解析正常工件作為獨立示意參考。第2/3/4/6/7/8章共16個單一問題視圖，各有桌面SVG與手機伴隨SVG；圖1/5保留。圖2整張影像進固定模型、正常存庫／待測查庫分開；圖3同屏比待測局部與正常參考；圖4分流／定位／算術分開且兩格標在同一來源；圖6一次一個反例；圖7共同B產品、特徵庫與模型產物不同；圖8作者Figure6/7成功、漏檢與正常誤報。

可攜來源與prompt：`_course_content/generated-concepts/ad-anomalydino/a09-sources/`（workpiece-baseline.png、作者PNG、author-sources.json、imagegen-prompts.json）；新生成正常工件 `anomalydino-normal-source_a09.png`、比較來源 `anomalydino-work-07_a09-source.png`。這些是生成示意或作者引用，不是本站模型推論。精確圖像呈現用SVG來源clipPath，不對作者圖進行生成編輯。

驗證：13項測試、14子測試通過（focused views、mobile steps、ResNet、navigation）；最終新增中文按鈕斷言與bundle視圖資產檢查後，3項測試、8子測試通過。16個視圖×桌面／手機共32個實際頁面檢查，無JS錯誤；SVG文字界限報告為空。HTML驗證器已支援並逐一檢查reading_views資產與crop，interactive-learning.html驗證通過。docs/index.html已建立，1212資產／405.9MB；32張A09資產與docs副本SHA逐一一致。

過程發現並修正：裁切範圍外舊標題／箭頭外露、圖2重複圖例越界、正常來源低解析與舊框、存庫再次抽特徵的歧義、手機PatchCore標籤重疊、shell寫入中文變問號。學習回寫IMAGE_STYLE_GUIDE的RULE-009/012裁切驗證補充。來源renderer為tools/render_anomalydino_a09.py；新契約與接受條件在openspec/changes/focused-teaching-views/。

證據：`tmp/anomalydino-review-20260905/a09/page/report.json`、`svg-bounds.json`、`generation-manifest.json`、`final-asset-sha.json`、`topic-validated.json`及逐視圖PNG。本輪驗證的是A09；不得據此宣稱後續A10也已驗證。

品質狀態：A11對A09快照的校準仍指出整頁90、部分視圖未過門檻。本輪沒有替它補成91以上；圖1/5未改，所有圖片全面>90仍未完成。A10已由另一流程進行位置→距離格→熱圖、算術與手機分工補強；交接前核對正式引用，不整批重跑A09 --integrate去覆蓋A10。本輪接續為A09工具驗證完成、視覺品質需繼續修正、使用者未核准、未外部部署。


### A10 本輪完成／整套仍需改善（2026-09-05）
第2章手機存庫／查庫、第4章位置／算術共6個SVG已整合並重建本機HTML及docs（1212資產）。生成方式為既有像素＋SVG，來源、設計意圖、失敗修正與hash見共用log A10及a10-*-manifest.json。3導覽、3手機分段、1bundle回歸及HTML通過；本輪Edge桌面1440／手機390的16章節檢查、32視圖切換／放大／Escape通過，無頁面錯誤和水平溢出。證據tmp/anomalydino-review-20260905/a10/final/report.json。
整頁自評91，新改圖92–94；保留圖仍有86–90與完成度未達標，故整套仍需改善，不是全部完成或使用者核准。下一步先修圖3正常候選比較、圖7代表特徵來源，再處理圖1/5手機上下文及圖8成功範圍。A11關於「A10未整合」限其舊快照，目前已整合。本輪未外部部署或做真實模型推論。

A10最終hash差異複核：A09並行更新了待測桌面及第7章PatchCore／EfficientAD共5個資產，已看本輪final實際成圖。PatchCore來源對應缺口仍在；EfficientAD擴大裁切後循環箭頭完整，但露出來源半截字，現評87（取代舊91），已列最優先待辦。QA只證明操作／引用可用，不替此視覺問題背書。本輪6個新A10資產未受影響，使用者核准仍待審。

A09最終補充：docs/index.html獨立HTML驗證也已通過。A09收尾證據已寫回WORKITEMS的WI-001，保留WI-003/A10為目前進行中工作；本輪不再覆寫正式topic或A10資產。品質尚未全部達標與使用者待審閱狀態維持。


## A13 開始／生成前 checkpoint

採納第7章紅字裁斷、PatchCore缺產品局部關係與第3章正常候選不足。第1／5章密度採納為後續；第8章部分採納：原像素解析度確有限，但不得用插值或AI重繪冒充額外證據。分數86、90、88、93、90、93、87、89是A12他評，非驗收。
模式：code-native SVG 組版，嵌入既有PNG來源；不重繪產品、熱圖或產生新實測。意圖：同源圖示、可追溯局部與完整文字。候選檔將存 _course_content/generated-concepts/ad-anomalydino/*_a13[-mobile].svg；維護工具 tools/render_anomalydino_a13.py。基準topic SHA256 8b56b191611e53767857fdd08b22e8331ddebd71f964b0cb1bc2c75d25529f30。尚未生成、尚未測試；下一步先看EfficientAD原型。

A13 原型 checkpoint：已實看 EfficientAD 桌面／手機原型，三個來源圖示與訓練迴圈完整、無來源殘字，SVG標籤完整；允許擴至 PatchCore／正常近鄰兩組。尚未整合。原型截圖 tmp/anomalydino-review-20260905/a13/anomalydino-07-efficient_a13[-mobile].png。

A13 整合 checkpoint：6個SVG候選已實看，僅改第3章正常對照與第7章PatchCore／EfficientAD的reading_views引用，其他章與A10六圖保留。新資產與來源hash見a13-manifest.json。即將重建HTML、執行桌面／手機與回歸、產出本機docs；目前尚未完成驗證。


## A13 最終 checkpoint — 本輪三項修正完成

- 啟用資產：`anomalydino-07-efficient_a13[-mobile].svg`、`anomalydino-07-patch_a13[-mobile].svg`、`anomalydino-03-normal_a13[-mobile].svg`，皆位於 `_course_content/generated-concepts/ad-anomalydino/`。生成模式為原始PNG像素嵌入SVG；沒有新增實測、重繪作者影像或ImageGen呼叫。prompt意圖／來源與腳本见本輪開始紀錄與a13-manifest.json。
- 第7章訓練迴圈完整，左右圖示不含原圖紅字碎片。PatchCore的來源框與裁片使用同一原圖座標，藍色條明示為特徵示意；兩個選入、一個未選只是子集示意，非實際coreset。第3章三個設定距離完整可比較。
- 正式topic、concept、interactive-learning.html與本機docs/index.html已更新。未外部部署。
- 驗證：HTML verifier通過；navigation 3 tests＋pages bundle 1 test通過；1440桌面／390手機各8章、共32個reading-view與放大邊界、自測答案、無水平溢出／JS錯誤通過。34張資產完成截圖與hash核對；另實看六張新資產及手機實際頁面。沒有宣稱整個測試套件通過。
- 證據：`tmp/anomalydino-review-20260905/a13/final/report.json`與同資料夾截圖。本機bundle1212資產／406MB。
- 量表v1.0人工自評：正常對照91、PatchCore91、EfficientAD92（桌面／手機分别檢視，同分）；第1／2／5／8章低分仍在，不能以此宣稱全章節>90。詳細分項／扣分見根目錄TEACHING_REVIEW_LOG.md A13。
- 下一步：先處理第1／5章手機跨段對照負擔，保留同一工件與分支變因；第8章需額外原始作者成功案例與可核對來源，不能以插值放大冒充更高解析度實驗。使用者尚未核准，也沒有真人理解測試。
- 入口：http://127.0.0.1:8000/interactive-learning.html?rev=anomalydino-a13#view=lesson&lesson=ad-anomalydino&slide=7


## A14 開始 checkpoint
目標為整套完成；基準tmp/anomalydino-review-20260905/a14/topic-before.json。已核對認可參考與原始論文Figure4圖說。即將下載作者原圖、製作第5章原型；尚未生成或測試。模式、逐圖意圖与檢查方式在根目錄TEACHING_REVIEW_LOG.md A14 brief。必要結論會保存此處，tmp不是唯一記憶。

A14 原型 checkpoint：第5章乾淨庫桌面／手機已實看，同一待測與兩個候選、最近距離、重測動作同畫面。原型分項24/23/19/18/9=93，五項8/9/9/8/9；來源局部仍有放大限制但識別刮傷足夠。擴展7視圖已生成，尚未整合。作者Figure4兩個原始PNG已取得（1100x2221與1100x1941），選瓶口及磁磚兩例，原始每格約254像素，非AI放大；待核對裁切。上次checkpoint因相對路徑重複寫入失敗，此次補正。

A14 整合 checkpoint：13新SVG已生成並檢視主要桌面/手機構圖；修正正常驗證插圖使其與建庫照片不同，兩個原始作者案例裁切已核對。正式topic與concept已整合，第8章改為瓶口／磁磚成功加原漏檢／誤報；來源README與hash已保存。即將構建並做全套21視圖雙尺寸QA，尚未驗收。


## A14 最終完成 checkpoint

- 八章既定修改、驗證、文件已完成，狀態為待使用者審閱；不再保留已採納項目待下一輪實作。
- 新資產13個：01-prepare/01-interpret/05-clean/05-contaminated/08-bottle/08-tile六組桌面手機，以及02-query桌面，皆為anomalydino-*_a14[-mobile].svg。生成方式、意圖與來源在本輪brief及a14-manifest.json；code-native SVG嵌入原PNG，不生成假預測。使用tools/render_anomalydino_a14.py可重現。
- 正式topic、concept、interactive-learning.html、docs/index.html已更新。21閱讀視圖、42資產；29沿用且hash確認、13新增已實看。原8章低解析度單一成功例已由兩組query/GT/1-shot作者例取代，保留漏檢/誤報；原始來源README/hash可查。
- 工具通過：HTML與docs verifier，navigation3、focused_views2＋8 subtests、mobile_steps3、bundle1共9測試。16章導覽/自測、42閱讀視圖雙尺寸放大/切換/邊界/無溢出、42資產hash通過。報告tmp/anomalydino-review-20260905/a14/final/report.json。
- 內部自評：整頁92；章節最低分93、91、91、93、93、93、91、92，每圖>90且五項>=8、無未解否決項。完整42圖分項與理由在根目錄TEACHING_REVIEW_LOG.md A14 final以及a14-review-manifest.json；不靠平均遮蔽低分圖。
- 原始作者每個來源區約254x254像素，沒有AI補細節；其限制明寫，兩例只支持個別定位觀察。無現場推論/真人學習證據，未使用者核准。
- 下一步：由使用者審閱新版；有新缺口再以同量表重開，不因自評否定回饋。外部部署不在本次執行範圍。
- 本機入口：http://127.0.0.1:8000/interactive-learning.html?rev=anomalydino-a14#view=lesson&lesson=ad-anomalydino&slide=1 。本機bundle1220資產/450.7MB。


## PatchCore P01 開始 checkpoint
現有topic無八章deep_dive，舊首讀名詞密且輸入裁片/聚合規則需澄清。基準tmp/patchcore-review-20260906/p01/topic-before.json。將用code-native SVG嵌入已維護的工件來源，數值另做二維教學設定，作者結果另引原始圖；不把AnomalyDINO模型/分數或作者圖當PatchCore。正在查原始來源，尚未生成。

P01 原型第一次實看：桌面coreset可辨六點與三個代表，手機E標籤與圖例重疊、C標籤太靠D，暫不通過；已縮小手機點圖尺度並分離C標籤。下一步重新截圖驗修正，尚未批量產圖。Browser可用清單為空，沿用使用者已授權headless Edge；首次啟動較慢，未因此跳過視覺檢查。




### PatchCore P01 製作與整合 checkpoint（2026-09-06）

代表子集原型已實看修正，E 與圖例、C 與 D 標籤已分離。六個二維教學點保留 A/D/E 的次序與覆蓋可核算；原型自評92，准入完整製作，並非使用者核准。

已產製8章、15組桌面／手機SVG，共30張。逐張實看後，第2章手機連線穿標題已移除重複標籤，桌面CNN名稱留足邊距；第6章以A/D/E/G原始局部取代相同符號，保留同一待測及庫變因，註明小圖追溯特徵來源而非存照片。第7章PatchCore沿用A13已驗證的產品B定位框→同源局部→特徵→選樣構圖。第8章實看作者瓶口／皮革成功定位，以及電纜漏檢、膠囊誤報，保留原像素。

正式topic、concept與model契約已整合。本機HTML正在建置，桌面／手機全套QA及評分尚未結案。來源程式commit fcaa92f124fb1ad74a7acf56726decd4b27cbcad 的兩個raw檔案hash與已查內容一致。

補正記錄：前兩次checkpoint經Windows舊版PowerShell管線傳入Python，中文字被轉成問號；無法解讀的行已移除並在此完整重記。後續中文修改直接使用UTF-8檔案，另檢查成品文字。圖檔的最近距離標籤同樣已補正，待最新實圖驗證。


## PatchCore P01 完成 checkpoint（2026-09-06）

評分詢問補記：30個現行圖檔與P01-review的hash完全一致；再次實看第2章手機、第4章刮傷桌面、第7章PaDiM手機、第8章成功手機截圖。本次為既有評分的版本與證據核對，並非新的全套獨立重評。維持整頁92、原逐圖91–94；第2/7章仍較抽象，第8章受原始解析度限制，手機正文仍長，因此不給95以上。沒有重製或新的真人學習證據。

- 8章、15閱讀視圖、30張桌面／手機圖已產生、整合、逐張實看與驗證，既定P01 TODO完成；使用者尚未核准。
- 正式topic／concept／model、本機interactive-learning.html及docs已更新；來源、模式、數值與生成意圖保存在P01 brief、p01-manifest.json、p01-sources/README.md。
- 回歸9項及HTML/docs verifier通過；16章雙尺寸導覽／自測、24可切換視圖放大及單視圖章放大、30資產hash與本機docs一致，無JS錯誤或水平溢出。測試報告tmp/patchcore-review-20260906/p01/final/report.json，持久摘要p01-review-manifest.json。
- 內部量表：整頁92；章節最低93、91、92、94、92、93、91、92。每張>90，完成度>=8、無未解否決項；完整分項與扣分在根目錄TEACHING_REVIEW_LOG.md P01。未經真人學習或現場推論驗證。
- 修正：CNN輸入語意、coreset覆蓋、同庫正常對照、論文／程式分數尺度、刪E／污染G來源局部、第7章來源裁片、第8章成功／漏檢／誤報，手機交線與桌面標籤間距均已核查。中文問號問題已補正為UTF-8直接寫入。
- 本機docs 1251資產／553.4MB；未外部部署。入口：http://127.0.0.1:8000/interactive-learning.html?rev=patchcore-p01#view=lesson&lesson=ad-patchcore&slide=1
- 下一步為使用者審閱；若有新缺口，從現行P01資產與同量表重開具體項目，不把內部完成當使用者核准。

## PatchCore P02 獨立重評（2026-09-06）

P03啟動補記：前次只停在P02紀錄，是執行錯誤；skill原本已要求未完成製作授權延續。現在將「先前做到達標」置於「單次評語只討論」之前，並補交付前的缺口→資產→啟用→驗證核對。skill修訂不能取代產圖。正在以第7章作原型，接續第2/3/5/1/6/8章；尚未完成新圖或整合。

- 範圍鎖定正式 `ad-patchcore.json`：SHA256 `050D9F3792F03ACC8F621FB4A569B7DE3A68EEF00D8340B967A05613A5E89C51`，修改時間 `2026-09-06 03:31:20`。使用者提供的 `rev=efficientad-v05` 是快取參數；本輪按實際啟用的 PatchCore topic 與 P01 最終成圖評分。
- Browser 外掛本輪無可用 runtime，未宣稱重新操作即時頁面；改用 `tmp/patchcore-review-20260906/p01/final/` 的實際桌面／手機頁面與30張資產成圖、`report.json` 互動結果及正式 topic 核對。QA只證明可到達、可切換、可放大、無溢位，不替圖片教學品質加分。
- 量表v1.0獨立重評：整頁 `89/100`；八章以各章最弱啟用視圖計為 `89、83、82、91、84、87、71、88`。P01的整頁92與逐圖91–94保留為歷史自評，但不再作現版驗收或改善證據。
- 主要優點：同一金屬工件貫穿前七章；正常／刮傷最近鄰、參考污染、作者漏檢與誤報都有可見對照；手機版字體與版面可讀。
- 主要缺口：CNN圖仍以格點／長條代替可辨特徵；coreset二維點未回連實際局部；整圖分數主要靠數字與文字說明；第7章PaDiM與EfficientAD用通用圖示加清單，沒有把位置統計、重訓、模型產物、推論負擔畫成可比較的差異；作者成功圖缺少同屏raw／GT／output判讀鏈。
- 結果是「需修正」，不是達標或使用者核准。本輪沒有產生或修改教材資產，也沒有真人學習／現場推論證據。


### P02 回饋核對與狀態同步（2026-09-06）

使用者提供八章最低分89/83/82/91/84/87/71/88與判斷。核對發現本機已有相同P02逐視圖重評；本次保留其作者／來源身分，採為修正工作基準，不冒稱本次重新完成獨立全套評分。正式topic hash與30個資產hash均吻合原受評版本。本次再看第1/3/5/6/7章的代表截圖，結合本對話已檢視的第2/4/7/8章，確認以下缺口成立。

- 採納第2/3/5/7章問題：可讀格點、正確座標與通用作業圖示沒有充分展示方法；上一輪把這些證據評成方法完整，是高估。
- 採納第1/6章改善方向：分流與庫變因本身清楚，但要把參考內容、來源局部、匹配變化與覆核結果接在一起，不能僅由分數變化要求讀者推理。
- 保留第4章、污染例與作者漏檢的有效對照，不因整套低分而全數推倒。
- 採納第8章成功案例判讀缺口；raw/GT/output必須來自可核對的同一樣本，不能從疊圖反推原圖或用AI補GT。
- 不把「每圖都要raw/GT/output」或「格點與圖示都不可用」訂成硬規則；要看它是否能完成該圖教學責任。第7章也不必堆完整逐層架構，而應具體表現同產品的準備資料、更新對象、待測比較與接手工作。

撤回P01整頁92及全部圖片達標的現版驗收結論。採既有P02整頁89作工作基準，15個視圖中11個<=90、4個>90；P02原先寫13個未達是計數錯誤，已按逐列分數更正。八章數字仍是各章最低視圖，不能平均成整頁分數。所有舊分數保留歷史並標記被取代。

工作入口、TODO、STATUS及機器可讀review manifest同步為「需修正」。本次完成回饋核對與文件同步，未重製圖片或改動網頁，也未重跑未受影響的互動測試。修正順序7→2/3→5→1/6→8；各項有可观察的驗收條件，不先填目標分數。

現行機器可讀分數：_course_content/generated-concepts/ad-patchcore/p02-review-manifest.json。P01-review保留原分數並標記superseded。


## PatchCore P03 — 學習後重製啟動與圖稿brief

原因：P02撤回達標後，先前「完成整套」授權仍有效，上一回覆停在紀錄是執行錯誤。已修改teaching-review-cycle/SKILL.md的模式判斷優先順序與交付檢查。quick_validate首次因Windows cp950讀取UTF-8失敗，使用python -X utf8重跑通過；沒有把skill修正當教材交付。

基準：tmp/patchcore-review-20260906/p03/topic-before.json；P02整頁89、最低89/83/82/91/84/87/71/88維持，尚無新圖分數。再次實看認可PPT第4頁（tmp/anomalydino-review-20260905/a06/master-slide-4.png），沿用工件→操作→結果→人的判讀路徑，不照搬其高密度七欄。

模式：code-native SVG嵌入原像素、精確連線／來源框。A-01材料與產品B是既有生成示意；方法回應、特徵與二維點只作教學設定，不稱實測。作者證據另列原論文和第三方公開重現。先第7章EfficientAD原型，實看因果及桌面手機後再擴展。

| 圖／工作問題 | 固定輸入、操作與可見證據 | 判讀／下一步、來源與驗證 |
|---|---|---|
|1 正常如何建庫與驗證|同A-01正常來源定位到紋理／螺絲／直邊，帶來源身分的特徵索引；另留正常與缺陷對照|先審參考、另留資料；不能把庫畫成無來源的相同長條|
|2 CNN邊緣與鄰域|同工件來源框與兩個不同局部，突出方向／周邊結構→描述；整圖進CNN，不把裁片當輸入|圖中可追看到哪些線索、為何上下文不同；概念示意不能標實際CNN激活|
|3 coreset覆蓋|六來源局部各綁A–F與同一二維點，保留A/D/E、B/C/F連向代表|看出被刪與保留的外觀；選樣按特徵距離而非每部位一票|
|5 分數／位置|固定刮傷、最近E及E周圍參考的距離關係→權重作用；格點→放大→原圖疊合|分數需與門檻版本配套；不是只背2×0.8；位置不當尺寸|
|6 coverage|固定合格直邊E，完整庫配E→刪E後配A，保留兩次匹配箭頭與新疑點|直接看見少哪個正常代表、改配誰；補庫前重測正常與缺陷|
|7 PatchCore|同產品B的正常多個局部→保留來源特徵庫；同待測從所有位置搜尋並標最近|換產品更新庫/索引；庫規模對查詢工作量可見，不造耗時|
|7 PaDiM|同產品B固定位置，數張正常該位置特徵聚成範圍；同位置待測落入/落出分布|換產品重估位置分布；展示錯位帶來比較對象改變，不畫通用橢圓了事|
|7 EfficientAD原型|同正常B走固定Teacher與可更新Student，回應比對回饋Student；待測用已訓練Student和Teacher比對局部回應|不再用旋鈕/晶片代替角色；示意差異與覆核相連，訓練回饋只能指向Student。AE另在文中交代，本圖限定局部分支|
|8 成功與不完美定位|第三方repository固定commit原圖gallery的同一行input/GT/output/overlay；保留至少两例|明寫第三方重現而非原論文/本站推論，不能用熱區重疊宣稱整件分類通過；檢查多亮區與邊界|
|8 誤報|原作者正常膠囊局部、同位置熱區與檢查步驟，保留分數/門檻|亮區是覆核對象，不能憑正常品的亮區推定缺陷原因|

第三方重現來源：mtaha-ai/industrial-anomaly-detection commit f19d2c6263d34c5755ab5ce7b0dbb9eb089eac88，results/figures/capsule_patchcore.png。已實看1775×1784原圖；gallery第1/3行有標註與熱區重疊，第2行顯示最大亮區可能偏離標註，不能按README概述全稱成功。原像素及URL/hash保存ad-patchcore/p03-sources；將按觀察限定案例結論。


### P03 原型通過、擴展製作 checkpoint
已實看第7章EfficientAD桌面／手機原型及修正版：固定Teacher、Student回饋與調整後接近、同一待測刮傷的回應差異直接呈現。生成方式為原像素嵌入code-native SVG；波形明標概念示意。原型png在tmp/patchcore-review-20260906/p03，保存路徑為ad-patchcore/patchcore-work-07-efficientad_p03[-mobile].svg。比較工件統一改A-01，取代brief的產品B，避免正常及刮傷來源跳轉。
第2章改用本機已快取ResNet50 IMAGENET1K_V2實際CPU前向，輸入是既有生成工件，明確不是PatchCore異常推論。來源crop、前處理、權重SHA、版本、通道選法、完整數值保存在p03-sources/cnn-features.json；可重跑工具extract_patchcore_p03_features.py。先前手畫波形不足以解釋特徵形成，故更換證據方式；第三方成功案例仍獨立標示。
下一步：產生其餘P03視圖、檢查全部成圖、整合正式topic/HTML、重新驗證。新分數尚未評，使用者尚未核准。

## PatchCore P03 — 實際重製與最終驗證（2026-09-06）

已完成本輪採納修正，並非只寫評分／學習文件。正式topic為8章17閱讀視圖、34個桌面／手機資產；新增26個P03 SVG，保留8個已核對hash的P01 SVG。入口： http://127.0.0.1:8000/interactive-learning.html?rev=patchcore-p03#view=lesson&lesson=ad-patchcore&slide=1

Skill原本已有評分→學習→重製要求，這次漏做是執行時把最新評語誤判為獨立review，忽略先前整套完成授權。已修teaching-review-cycle/SKILL.md模式判斷優先順序及交付檢查；python -X utf8 quick_validate通過。共用IMAGE_STYLE_GUIDE補實際特徵證據的範圍，TEACHING_WEBPAGE_GUIDE補接續授權原則。

生成與來源：code-native SVG嵌原像素；p03-sources/cnn-features.json為本機ResNet50实际CPU提取（不是PatchCore異常推論）。p03-sources/capsule_patchcore.png為固定commit第三方重現，README/source.json保留crop與hash。其他波形／二維點／熱區示意不混稱實測。第7章統一A-01，PaDiM正常框改到與刮傷相應的右下位置。

驗證：HTML及docs verifier通過；9項回歸、14 subtests通過。16章節／30可切換視圖的桌面手機導航、自測、放大邊緣與Escape通過；另有單視圖放大檢查。34資產成圖與hash確認，最後手機第2章間距和第8章來源句修正後追加4個頁面檢查與1張資產截圖。34資產與本機docs逐檔相同；bundle1255資產577.6MB。CNN的3×3平均與較深層對齊、coreset選樣、L2例和Eq.7權重均獨立核算。證據：tmp/patchcore-review-20260906/p03/final/report.json。

過程缺陷與修正：成功例手機第二排標題碰到上排影像→調間距；CNN每圖選通道→改為正常圖選定後固定；手機兩層連線可能誤指→改每層輸出值放在各自圖下；PaDiM來源位置→統一右下區；旧句將第三方包成原論文→限定後兩例為S1/S2。建置曾因來源網域不在既有清單失敗，改連同版本官方GitHub；一次生成與讀取重疊造成暫時尺寸檢查失敗，待生成結束後順序重建通過，未放寬檢查。

整頁自評：[19,19,19,18,9,9]=93。工作案例與輸出接法有A-01及四種公開行為證據；必要原理由實際特徵／來源coreset／查詢／模型更新關係支持。比較18：同工作條件與成本測法成立，但無共同硬體實測；閱讀9：穩定viewport已檢查，手機細節需放大；自測9：含資料少、縮庫、換產品節拍、誤報/漏檢取捨，尚無真人學習成效證據。分數不是客觀效能或使用者核准，不使用舊高分作改善曲線。

逐視圖評分／扣分理由唯一紀錄在根目錄TEACHING_REVIEW_LOG.md P03與p03-review-manifest.json。章內最低：92、91、92、91、91、92、91、92；待使用者審閱，未核准。

## PatchCore P04：P03獨立重評（2026-09-06）

- 正式topic SHA256為 `5625A43E1F71143EBA9EFA550A73244AD87FE15221A820FEB8F6F8B74C92561C`；確認已由P01/P02資產組更新為P03的17個閱讀視圖與34個桌面／手機資產。
- Browser runtime清單為空，未宣稱重新操作即時頁面；改用P03 final實際資產成圖、桌面／手機頁面截圖、正式topic與 `report.json` 核對。QA只支持可達、切換、放大與無溢位，不替圖片案例或方法意義加分。
- 獨立重評為整頁 `91/100`；八章最低視圖 `91、89、91、91、89、91、89、90`。這取代P03內部自評93及章節最低92/91/92/91/91/92/91/92作為目前審查判斷，但保留其歷史紀錄。
- P03是實質改善：第2章加入可反查CNN回應，第3章A–F點可回連來源局部，第7章清楚分出查全庫／同位置分布／Teacher-Student，第8章拆出raw／GT／heatmap／overlay；手機圖亦維持可讀。
- 尚未完全達標：第2章兩層描述的合併規則仍由文字承擔；第5章Eq.7視圖仍偏數字與線段；第7章PatchCore查全庫未把查詢成本或索引行為具體化；第8章第三方公開重現沒有整件分數／門檻，且局部命中不等於整件成功。手機章節正文較長，閱讀負擔仍在。
- 結果為「接近完成、仍需小修」，不是使用者核准或真人學習驗證。本輪沒有修改教材資產。


## PaDiM R01 review started (2026-09-06)

User switched to reviewing ad-padim. Scope: review current page and five beginner visuals plus four supporting visuals; no production requested for this topic. Next: capture actual desktop/mobile page and assets, inspect, score with rubric v1.0, save findings. Evidence directory: tmp/padim-review-20260906. Browser connection unavailable; use previously authorized standalone Edge. Scores pending.

## 目前接續：WI-007 — 八主題持續學習與重製

- 授權：使用者確認按建議持續學習；完成ResNet、ConvNeXt、ViT、U-Net、SegFormer、YOLO-Seg、Keypoint R-CNN、Pose Pipeline。依序完成每題的審查→學習→重製→整合→驗證；三組各回查前題。不需要再次要求開工確認。
- 狀態：已保存八題正式來源基準；先檢查ResNet。PaDiM獨立評論因使用者切換八題而暫停；其截圖已留存，不冒稱已評完。PatchCore較新的P04重評在共用log，原P03自評不是最新驗收。
- 計畫：維持原工程參考與介面契約，按實看結果調整教學圖、主線與手機視圖。使用已有來源，示意、實際數值與模型推論分清。先原型、後展開。
- 驗收：每題可見工作問題／方法／結果／人的處置；每張新圖實看、桌面手機/放大/自測檢查；適當回歸與HTML、bundle驗證；量表v1.0分項記錄，不把測試或高分當真人核准。
- 檔案：course BEGINNER_VISUAL_TODO.md及BEGINNER_VISUAL_STATUS.md；根TEACHING_REVIEW_LOG.md；基準及證據tmp/eight-topics-20260906。
- 下一步：ResNet實圖與主線審查、確認單張原型要解決的缺口。尚未生成；尚未評分。



ResNet E01 checkpoint: baseline eight images inspected; chapter2 overlap, chapter3 shape-only, chapter5 untraceable grid and chapter7/8 list-only comparison accepted for repair. Brief: tmp/eight-topics-20260906/resnet/brief.md. Real CPU ResNet50 residual data saved to e01-data/activations.json; exact tensor addition error 0. Prototype generated, visual review pending; not complete or user-approved.


## WI-007 checkpoint：ResNet E01整合；分類組繼續（2026-09-06）

ResNet八章已實際重製為16張桌面／手機SVG，正式topic及本機HTML已啟用。5項ResNet既有回歸通過；16個桌面／手機章節導航、專用手機圖、放大Escape、自測與頁面無溢出通過。證據tmp/eight-topics-20260906/resnet/final/report.json，逐圖hash及邊界在final-assets/assets.json。尚未外部部署或使用者核准。

原型先挑最大残差卻全歸零，未放行；改成同通道同位置的正負修正後才展開。SVG裁切補explicit clipPath，避免方形框露出原crop以外的設備。第3章手機上下標籤曾碰撞，已修。BatchNorm只示中心化，不以假標準差冒充完整正規化。圖上假設分數不是真實工件分類。

目前自評尚未定稿：第8章三模型機制仍較概括，列入分類組回查，不能宣稱全題已達標。下一步在ConvNeXt/ViT展開來源局部與操作差異，再回填ResNet比較。全八題WI-007仍執行中，沒有縮成只做ResNet。

ConvNeXt基準五圖及桌面手機已截圖並實看：切片圖只用方格代替被切的訊號；depthwise/channel mixing仍靠格子長條；主頁通用文案與主題重點不一致，手機仍橫向920px。需改成同一來源實際裁片與兩種混合方向。將擴充既有beginner path的可選reading_views，沿用已驗證deep-dive手機元件與安全驗證；不強迫每題加成八章。

維護程式：tools/teaching_e01_canvas.py、extract_resnet_e01.py、render_resnet_e01.py。資料generated-concepts/resnet/e01-data/activations.json，生成模式code-native SVG+原圖像素+本機CPU特徵。記憶與下一項在WORKITEMS、BEGINNER_VISUAL_TODO/STATUS與共用TEACHING_REVIEW_LOG，原始基準可恢复。


## WI-007 最新接續：ViT製作中；分类組比較仍待完成

- ResNet E01：8章16圖、正式HTML已整合；5項回歸及16桌面手機章節QA通過。第8章比較尚需分類組回填，未評為完成。
- ConvNeXt E01：5段6視圖、12桌面手機資產（首圖由原生SVG忠實轉PNG）；已整合。實圖全看、HTML verifier、新增2項回歸及10頁面狀態/6視圖放大通過。手機實寬由278增至>=340px，已實看新頁。仍需三模型共同對照，不冒稱整題達標。
- ViT：baseline五圖與桌面手機已保存並實看；brief在tmp/eight-topics-20260906/vit-classifier/brief.md。開始CPU ViT-B/16中間輸出擷取，來源V-01及供群組比較的R-01。原型尚未畫、尚未改正式topic。
- 重要學習：patch token是多維向量，不是平均成一個數，不能因token數少就斷言細節一定消失。改解析度的成本例固定P16；不假設現有checkpoint可隨便改patch大小。
- 共用UI已加入beginner可選reading_views；首圖PNG約束、安全路徑及crop驗證保留，僅opt-in使用作者文案及手機圖，legacy保持原流程。工具tools/build_interactive_learning_html.py、verify_interactive_learning_html.py；回歸tests/test_beginner_focused_views.py。
- 接續先完成ViT prototype→全題→分類組三模型比較與回查→固定量表逐圖及頁面評分，再做U-Net、SegFormer、YOLO-Seg、Keypoint R-CNN、Pose。全八題未完成，不要在此checkpoint停工。
- 沒有外部部署、真人學習證據或使用者核准。最新QA證據tmp/eight-topics-20260906/{resnet,convnext}/final/report.json；精確資產hash在各final-assets/assets.json。
# ViT E01 原型修正意圖

2026-09-06：已實看 prototype/3-0-image.png 與手機版。來源座標與權重可追，但四條短線只表權重，尚未讓人看到「權重乘各位置的 value，再相加」的結果；此原型不放行為完成圖。補擷取同一層、頭、query 的第0個 value 分量，列出四項乘積、其餘項貢獻與加權結果。原像素裁片只表示初始位置，最後一層的向量已含上下文，不能把它稱為原始 patch 的獨立因果貢獻。

下一次檢驗：四項以外沒有省略，算式獨立核對；結果更新查詢位置，未假裝已產出分類；手機數字不撞字。保留權重最大四項僅合計5.60%的真實結果，不另挑較戲劇化頭。這個原則同樣用於CNN通道選取：展示少數項時列明剩餘貢獻。

WI-007分類組回查：同R-01共用四個實際操作視圖已接入ResNet8、ConvNeXt5、ViT5。發現R-01和V-01縱橫比不同時，外部框需跟隨圖片meet的留白；已修正attention來源標框。測試完成不代替逐圖教學評分，評分仍待最終校準。下一步U-Net用局部斷口與多尺度合併取代符號U形圖，全部八題仍執行。
U-Net基準五圖已實看；brief已寫先於renderer。原型第3圖用斷口訊號、同尺度通道拼接，避免符號U字與文字堆疊。分類組逐圖分項最終校準仍待做。
U-Net原型實看：細斷口與粗圖的差異已可見，但拼接仍只有文字，且手機少了候選結果；未放行。修正為兩張同尺度特徵各自保留的可見疊層，補同一斷口候選，避免讓單張粗圖被誤讀為融合結果。
U-Net E01五段10桌面手機圖已整合，原型3次檢查後修疊層與手機候選；全圖實看後修第2/5文字碰撞、放大第5焊墊ID。生成模式原像素+原生SVG人工概念，首PNG忠實轉圖。SegFormer正式八章baseline已實看，brief已寫；從SR原型續作。
SegFormer SR原型已實看：候選位置縮減可見，但左圖標Q再箭頭到K/V易誤讀為把Q縮小。修成共同來源特徵網格與橘框query，明確K/V支路縮減；Q保留64位置。後續decoder沿用U-Net的實際可見多圖層拼接，不能只畫concat文字框。
SegFormer E01八章16圖正式整合；全圖已實看，修overlap框留白、訓練預測與GT可見差異、第1/6正文碰撞，QA執行中。YOLO-Seg原五圖已實看，B標框在背景是實質缺陷，改回原始PCB兩顆可見元件；brief先於製作。


## WI-007 checkpoint：六題已整合，開始關鍵點組

ResNet、ConvNeXt、ViT、U-Net、SegFormer、YOLO-Seg的E01已啟用本機HTML。分類比較已加入同R-01實際運算。U-Net10、SegFormer16、YOLO-Seg10桌面手機頁面QA通過；工具結果不是視覺評分。YOLO-Seg原背景B框改回原始PCB兩個真元件，桌面第2圖底部裁字已縮短修正；模式原像素＋原生SVG人工mask／可追算基底，首PNG忠實轉圖，保存於各generated-concepts/{topic}/*e01*。

Keypoint R-CNN基準五图已實看，框與角點漂到背景的缺陷採納；brief在tmp/eight-topics-20260906/keypoint-r-cnn/brief.md。下一步同金色元件四熱圖原型→回映／遮擋→Pose→分組回查與固定量表校準→共用回歸與bundle。全八題仍執行，未最終評分、未外部部署、未使用者核准。


## WI-007：八題E01已重製整合，進入最終審查

Keypoint R-CNN五段六視圖完成原像素近角、每點熱圖、2×2取樣、回映偏移與遮擋修正；10頁面狀態QA通過。Pose六段完成同PCB分組、G-01已知幾何、縮图内參、實際PnP、外圍檢查與交付。來源、意圖在tmp/eight-topics-20260906/{keypoint-r-cnn,pose}/brief.md；原生SVG及手機專圖保存在generated-concepts/{topic}/*e01*，首圖為忠實PNG輸出，非生成模型推論。

學習：Pose第一版底部文字在桌面碰撞、分組前後不夠可見，已修排版並加每件連線；外圍檢查點原先與擬合角點重合，已改為未參與擬合的(55,35,0)mm再重算，不冒稱獨立檢查。最終受控例分散/集中RMSE0.31/0.34px，外圍0.49/8.35px，只支持此設定。原型局部殘差150倍顯示，外圍差異6倍顯示，均明示倍率。

三組已回填前題：分類用同R-01實測操作；分割用已標示各自案例的融合/共享基底；關鍵點組用2D→幾何角色對照。下一步完整逐圖分項評分、最後頁面與手機實看、共享回歸、HTML/docs bundle及hash核對。仍未宣稱全題達標、外部發布或使用者核准。


## WI-007 E01 最終交付（2026-09-06）

八主題 ResNet、ConvNeXt、ViT、U-Net、SegFormer、YOLO-Seg、Keypoint R-CNN、Pose Pipeline 已完成審查→Markdown學習→實際重製→正式整合→驗證；三組已回查前題。本段取代先前「製作中／最終檢查待完成」checkpoint，使用者尚未核准。

- 產物：49組桌面／手機圖，共98個唯一啟用資產；正式topic與本機HTML、docs網站包同步。生成模式為原始像素搭配原生SVG、實際CPU模型張量或明示的概念／合成幾何；沒有把示意當實際模型預測。生成意圖、來源與保存路徑見本檔各題紀錄、course tools內E01 renderer/extractor、各題generated-concepts manifest。
- 固定量表v1.0整頁自評：ResNet 93、ConvNeXt 93、ViT 92、U-Net 94、SegFormer 92、YOLO-Seg 93、Keypoint R-CNN 92、Pose 93；最低單圖91。逐圖分項、扣分與證據在共用TEACHING_REVIEW_LOG.md及course e01-eight-topic-review.json。這是自評，沒有真人學習驗收證據。
- 驗證：20項pytest測試＋18個子測試通過；94個桌面／手機章節狀態、切換／放大／答案展開检查通過。數值獨立核對通過。最終docs verifier通過，1305個包內資產存在，98個啟用資產hash一致；本機HTTP 200且HTML與docs一致。證據：tmp/eight-topics-20260906下各題final/report.json、final-assets/assets.json、numeric-audit.json、delivery-audit.json。
- 本機入口：http://127.0.0.1:8000/interactive-learning.html?rev=eight-e01-final#view=lesson&lesson=resnet&slide=1 。未執行外部部署。
- 已回用的學習：特徵與實際來源局部對應；保留剩餘貢獻而不只挑好看的通道；concat畫成分開的特徵平面；ROI裁圖須核對縮放與留白偏移；2D／3D座標分清；獨立驗證點不得參與擬合；手機需逐張實看。規則已更新IMAGE_STYLE_GUIDE.md與TEACHING_WEBPAGE_GUIDE.md，並用於後續題和前題回查。
- 下一步：待使用者審閱這八題；有新回饋時按具體缺口重開，沿用既有授權，不能只寫學習紀錄而不修改成品。不要重做本輪已驗證產物。PaDiM評論暫停、PatchCore P04待改進屬既有其他項目，不因本輪八題完成而宣稱已結案。


## WI-007 reopened：ResNet E02 動機與跳接（2026-09-06）

採納使用者回饋：E01未在可見主線充分解釋skip connection及為何需要ResNet。已有數字相加與shortcut字樣不等於教懂。撤回ResNet E01整頁93作為達標依據，八題品質穩定收斂的結論不成立；其餘七題並未重新評分。

觀察→原因：把工作輸出限制當作模型存在理由；把實際張量的可追算性當作初學者機制解釋。可重用原則：模型主線先回答原方法遇到什麼困難、這個設計改變哪一條路徑、为何改善，再接數值與部署限制。適用於模型原理教學，不強制每題加章。

製作計畫與brief：保留八章及有效E01圖，新增E02兩組桌面／手機原生SVG。先作跳接原型：同一中間特徵x，普通卷積串聯vs分支繞過卷積後逐元素相加；設定非負[2,1,3]與修正[0,2,-1]可追得[2,3,2]，零修正直接保留x，並明示ReLU與尺寸對齊。其次動機圖：普通深網比淺網訓練更差的質性曲線，明示依原論文Fig.1示意非數據；觀察訓練而非只看測試，接到残差設計與本站驗證。來源arxiv:1512.03385 §1/3、1603.05027；不把退化簡化成過擬合或單一梯度消失原因。

參考：實看tmp/anomalydino-review-20260905/a06/master-slide-4.png，沿用單一問題、可追流程、證據與結論分區；不複製無關產線裝飾。生成意圖為精確雙路箭頭、同值對照及訓練困難，不使用生成照片冒充證據。預期資產generated-concepts/resnet/resnet-e02-*.svg；基準tmp/resnet-e02/resnet-e01-baseline.json。

- [ ] 跳接雙路原型桌面／手機實看並修正。
- [ ] 動機圖、前兩章正文／自測重製與正式引用。
- [ ] 八章桌面手機、必要回歸、HTML/docs及分項審查。

目前即將產圖，尚未新驗證或新評分；下一步原型。原E01技術驗證保留為歷史，不作E02或使用者核准證據。
E02原型checkpoint：已實看skip桌面與手機，雙路與逐格值可追；發現中間箭頭穿過F(x)標籤，已斷開留出標籤區後重製。構圖可展開動機圖；尚未正式整合或完成QA。原型自評[23,24,18,18,9]=92，視覺[8,9,9,8,9]；保留精確雙路對照，扣分為基本塊概念仍須正文定義特徵，非真人驗收。
E02整合checkpoint：新增來源誤用title而非schema規定label/scope，builder擋下；因此初次頁面QA讀到E01並在答案核對失敗，不能列為E02通過。已修來源欄位並重建，待成功後再跑QA。手機動機圖另補直接跳接示意，避免解法只存在桌面。


## WI-007 ResNet E02 修正完成（2026-09-06）

已採納並實際修正兩個核心缺口：第1章改為「為何加深反而學不好」，第2章先看普通／殘差雙路，再看本機實測數值。新增why/skip共4個桌面手機SVG，保存generated-concepts/resnet/resnet-e02-*.svg；生成模式原生SVG質性圖與可追算設定例，非模型推論。renderer為tools/render_resnet_e02.py，來源與生成意圖见e02-manifest.json及本輪前置brief。原工作接法和實測圖保留為第二視圖。

修正閉環：原型箭頭穿字→分開箭頭與標籤；手機缺解法→補分支與相加；來源schema欄位錯誤→更正label/scope並重建。初次QA及一個runtime測試讀到舊HTML而失敗，未計作通過；成功建置後重跑ResNet全部5項通過，另5項聚焦測試與14子測試通過。16個桌面手機章節狀態、所有閱讀視圖切換／放大／答案／無水平溢出通過。4新資產hash與docs一致，HTTP200且本機HTML與docs一致；數值[2,1,3]+[0,2,-1]=[2,3,2]独立核算。HTML verifier結果另附checkpoint。

固定量表v1.0：動機圖[23,23,18,18,9]=91，跳接圖[23,24,18,18,9]=92；兩組五項完成度[8,9,9,8,9]，美感為清晰原生圖但非細緻情境插畫；完整為責任具體可見；專業為證據與簡化清楚；密度仍需少量術語；層級能沿問題／路徑／結果追蹤。桌面手機均實看。保留對照及可追路徑；扣分為質性而非真實訓練曲線、基本塊省略BN與投影、手機仍須捲動。整頁自評[18,18,19,18,9,9]=91，逐項證據見resnet-e02-review.json；未修改圖沿用E01相同資產證據，不據此替其他七題重新認證。

E01整頁93已被取代，不能用不同校準下分數宣稱進步。新的91亦非真人理解或使用者核准；這輪只完成採納的ResNet修正，不能再宣稱八題品質已穩定收斂。學習規則已寫回TEACHING_WEBPAGE_GUIDE.md：先有存在理由與路徑因果，再接張量與工程限制。

入口：http://127.0.0.1:8000/interactive-learning.html?rev=resnet-e02#view=lesson&lesson=resnet&slide=1 。本機更新，未外部部署。證據tmp/resnet-e02/resnet/{assets,final}/，持久分項course resnet-e02-review.json。下一步待使用者審閱；新回饋依既有授權重開具體修改，不只寫TODO。

E02最後驗證：HTML verifier PASS（58主題、HTML解析與離線內嵌資料通過）；本機bundle 1309資產。4新圖與HTML經hash核對和HTTP確認，未外部部署。


## WI-007 E03：七題中心思想補正（2026-09-06）

使用者要求：其他模型同樣沒有教清中心思想，需一併修正。沿原八題範圍，ResNet E02保留並作回查，其餘七題實際修改；不是只評分、寫清單或只補術語。撤回其餘七題E01高分作為「中心思想已教清楚」的依據，歷史技術證據保留。

觀察：ConvNeXt先講切片；ViT先講類別；U-Net與SegFormer先講標註／輸出；YOLO-Seg與Keypoint先講候選；Pose先比較前端，讀者尚不知為何需此設計。原因是以局部可追算與工程限制代替整體模型解釋。一般化原則：先有問題→核心機制→有用結果，再沿原機制章展開；每題約三個必記要點需各有圖上證據與移除設計的反事實練習，不把清單當解釋。

G1逐圖brief（E03首圖各一對桌面／手機）：
| 題目 | 困難與核心理解 | 同源輸入／可見機制／結果 | 下一步與風險 |
| ConvNeXt | 純CNN如何吸收現代設計；分開處理空間和通道 | 同R-01；7×7單通道鄰域→同位置多通道→殘差合併；分清核權重與注意力 | 接實際DW/PW運算；不能說性能只來自大核 |
| ViT | 將影像當序列，依內容連結不同位置 | 同V-01；patch格→帶位置token→不同粗細權重邊→CLS分類 | 接實際投影／attention；不是把注意力當缺陷解釋 |
| U-Net | 語意脈絡與精細位置都需要 | 同PCB斷口；U形縮小／放大，細特徵跨接decoder，粗細兩平面→邊界 | 先作代表原型；不能把skip誤畫成ResNet相加 |
| SegFormer | Transformer做密集預測，要保留多尺度且控制成本 | 同W-01；四尺度特徵各自接到對齊融合；輕量decoder出像素類別 | 不是U形鏡像；接overlap/SR/融合細節 |
| YOLO-Seg | 每件要輪廓，也希望共用全圖計算 | 同A/B；共享特徵分岔為基底與每件係數，組成A/B兩mask | 限YOLOv8式；不冒稱所有YOLO版本相同 |
| Keypoint R-CNN | 多件的固定點不能混在一起 | 同金色A/B；候選→ROIAlign→每件四熱圖→點ID | 框與點關係可見；非預訓練人體點直接適用工業 |
| Pose Pipeline | 像素位置不等於物體的旋轉與位移 | 同G-01合成板；有ID的2D與3D、相機→PnP→R/t→回投影 | 明說這是流程，不是單一神經模型；不越界成機械手座標 |

構圖參考：沿已實看認可PPT第4頁的單一工作問題、因果箭頭與結果；各題用不同機制構圖，非七張同版文字卡。生成模式原生SVG＋已有原像素／明示概念特徵；不做新模型推論。預期路徑generated-concepts/{topic}/{topic}-e03-core.svg及-mobile.svg，首讀PNG由瀏覽器忠實輸出。先U-Net原型實看，後逐題出圖並檢查。來源原論文／官方程式（ConvNeXt 2201.03545、ViT 2010.11929、U-Net1505.04597、SegFormer2105.15203、Mask R-CNN1703.06870、Ultralytics Segment head、OpenCV PnP）已核對。

計畫：保存基準→原型→七題核心圖與主線／自測→逐圖桌面手機→正式建置後八題操作回查→必要回歸與bundle→記憶同步。基準tmp/core-e03/baseline；未開始新驗證，未核准。
## WI-008：八模型介紹系列總評（2026-09-06）

本輪為 review-only。已針對 ResNet、ConvNeXt、ViT、U-Net、SegFormer、YOLO-Seg、Keypoint R-CNN、Pose Pipeline 建立獨立總評：`MODEL_INTRO_SERIES_REVIEW_2026-09-06.md`。評分依 `TEACHING_SCORING_RUBRIC.md` v1.0，並以正式 topic、最新 manifest、代表性 PNG／SVG 與既有驗證證據為準；系列平均為 88.6/100。

主要結論是：系列的內容正確性與工程責任已強，但多數模型仍缺少同一樣本的 raw／GT／prediction／error／decision 真實證據；ViT、Pose Pipeline、Keypoint R-CNN、YOLO-Seg 最容易讓初學者建立錯誤心智模型，應優先處理。ResNet 與 SegFormer 的導覽深度也和其餘六題不一致，後續宜統一「模型介紹完成定義」與家族比較格式。

瀏覽器控制器本輪沒有可用 browser instance，因此沒有宣稱完成新版本的逐頁互動驗收；評點限制已在總評 Markdown 明列。本輪沒有產生或替換圖片，也沒有改動 E03 的製作狀態；E03 仍是獨立且優先的實作工作流，是否完成或獲使用者認可須依其原有紀錄判定。
E03原型：U-Net桌面／手機已實看，U形縮放、跨接细特徵、粗圖放大仍缺斷口可見。發現底部多餘箭頭及斜箭頭穿拼接標籤，已移除重複箭頭並移標籤後再出圖。原型自評[23,24,18,18,9]=92，視覺[8,9,9,8,9]；構圖可展開，並非其他圖已驗收。
E03逐圖修正：ViT和SegFormer有連線穿文字，已移開；ViT位置對照由色卡改原像素patch。YOLO基底原色階吞掉負值，改為有正負色階與圖例；Keypoint來源裁片與熱圖重疊，已縮小並標示來源；Pose把已知3D文字卡改成同ID、已知尺寸平板。這些均是實看後再重製，尚未評為通過。
E03主線已整合七題各三要點與移除設計的自測。另發現首讀只顯示部分callout，完整原理被摺疊；新增嚴格布林core_ideas欄位，六題beginner主線直接顯示三要點，SegFormer用既有可見points。追加UI回歸以檢查三要點不在details。正建置，完成後進八題QA與必要回歸；未宣稱通過。

E03驗證checkpoint：14個新核心桌面／手機資產已實看並逐圖記錄；六題三要點在主線完整可見，SegFormer沿既有points。HTML verifier已通過；首次因獨立驗證器缺少core_ideas欄位而失敗，已同步限定布林契約後重跑。bundle已建出1323資產；八題操作、回歸及交付hash尚在執行，未提前勾完TODO。

## WI-007 E03 完成紀錄（2026-09-06）

七題都已實際修正模型存在理由、核心圖、三要點與移除設計的自測；ResNet E02保留並回查。六題原先有內容却藏在工程details的問題已由core_ideas嚴格布林契約與可見正文修正；SegFormer三要點用既有points。首圖後保留有效細節視圖，後續圖說回扣核心機制。不是只改Markdown，也不是七題套同一張文字卡。

生成模式：原生SVG、沿用原像素／明示概念場／既有PnP幾何；六張桌面圖由Edge忠實輸出PNG，無新模型推論或AI補造GT。啟用14張E03（七桌面、七手機），另保留六張桌面SVG來源，共20新圖檔。意圖與路徑見前置brief、各題e03-manifest.json及core-e03-review.json.assets；renderer為tools/render_core_e03.py，主線來源core_e03_lessons.py及integrate_core_e03.py。

驗證：19 tests與18 subtests通過；八題94個桌面／手機章節狀態通過，包含閱讀視圖切換、放大關閉、答案、核心正文與無水平溢出。14新資產hash與本機docs一致，HTML與docs/index.html逐byte一致，HTTP200載入同內容。source及bundle HTML verifier均PASS；bundle1323資產。ViT無位置重排／YOLO正負基底獨立數值核算通過。深色核心段實看可讀。正常390×844操作截圖之外，另用同390寬的長視窗完整檢視核心文字，避免元素截圖被黏性導覽遮住；未將長視窗冒充一般手機視窗。

逐圖自評與整頁分項、證據及扣分見core-e03-review.json和共用log。圖片自評91–93、七題頁面自評91–92；未變動圖只引用hash一致的既有圖像證據，E01整頁達標宣稱被取代。工具PASS不證明教學有效。使用者未核准、無真人學習或新現場推論證據；不能宣稱整套已穩定收斂。獨立WI-008總評及其他workitem完整保留，不被本輪覆蓋。

學習已寫回TEACHING_WEBPAGE_GUIDE.md與IMAGE_STYLE_GUIDE.md：先解釋存在理由與因果，再看算例；檢查實際DOM完整可見；正負色階、來源與特徵身分要正確。首次verifier不認新欄位已修契約後重跑；中途截圖發現的遮擋、座標與負值問題均重新出圖再檢查。最後YOLO圖將「省去逐件重跑骨幹」改為「共享特徵後直接預測候選」，避免誤導讀者以為兩階段模型均逐件重跑骨幹；重新輸出、實看與核對bundle。最終圖hash以core-e03-review.json.assets為準，前述圖像評分仍適用，舊hash只代表先前檢查版本。

新版本機入口：http://127.0.0.1:8000/interactive-learning.html?rev=core-e03#view=lesson&lesson=convnext&slide=1 。未外部部署。下一步為使用者審閱；若指出具體新缺口，沿既有授權重開修改，不只記TODO。

## WI-008-R1 外部意見學習完成（2026-09-06）

使用者要求自行判斷而非全盤採納。已保留原報告並加入版本註記，在共用log寫入25項取捨及「觀察→原因→原則→適用／下輪驗證」。採納失敗後果可見、證據配對主張及共同決策方向；部分採納真實案例、手機精簡及路徑一致性；不採納硬性同版／同章數、切patch等於訊號消失、無幾何依據的PCB 6DoF或任意head比較。E03已補的存在理由、位置對照、粗細融合與Pose責任不重複排工。

學習合併至TEACHING_WEBPAGE_GUIDE.md和IMAGE_STYLE_GUIDE.md，TODO保留待證據候選；WORKITEMS增加接續指標。核對七題topic hash、Markdown目的地與章節存在；沒有重評圖片、重建頁面或執行新推論。原報告88.6與E03自評均不當真人理解證據，待使用者審閱狀態不變。下一步若進入製作，從TODO候選建立具體brief並取得證據，再走原型→實看→重製→驗證，而不是把採納規則算成新成圖。
## WI-010：E03 八模型系列獨立重評（2026-09-06）

本輪重新檢查 ResNet E02、七題 E03 核心圖、代表性後續章節、桌面與手機保存證據，並依 `TEACHING_SCORING_RUBRIC.md` v1.0 重新評比。新報告為 `MODEL_INTRO_SERIES_REVIEW_E03_2026-09-06.md`。分數為 ResNet 91、ConvNeXt 90、ViT 90、U-Net 91、SegFormer 91、YOLO-Seg 90、Keypoint R-CNN 90、Pose Pipeline 91，平均 90.5。舊報告 88.6 保留為 E01／E02 範圍的歷史意見，不與 E03 自評混用。

判斷：E03 確實修正「中心思想不清」；各題現在能較清楚回答存在理由、核心資訊路徑與移除設計的後果。扣分不是因為圖不漂亮，而是 ConvNeXt／ViT 仍缺核心機制接到實際分類結果，YOLO-Seg／Keypoint R-CNN 仍缺關鍵失敗鏈；多數分割／點位核心圖仍是概念示意而非實際模型 prediction。ConvNeXt、ViT、YOLO-Seg、Keypoint R-CNN 為 90 分，依門檻不通過。其他完整章節雖為 91，本輪沒有把所有未變動啟用圖逐張重新打分，不能據總分宣稱整題完成。

Browser runtime 本輪沒有可用 browser instance；已依規定確認 browser list 為空，沒有改用其他瀏覽器控制工具，也未聲稱新的即時互動驗收。頁面閱讀以 E03 保存的實際截圖、正式 topic／資產與既有 QA 證據為準。本輪 review-only，未產生、替換圖片或重建網頁；使用者核准與真人學習證據仍未取得。


## WI-009 D01 整合 checkpoint
六題已整合正式topic、四幅首讀主線及三個可見核心要點，model.md的90秒說明及D01來源補正已同步。產生28個啟用桌面／手機資產（6個PNG核心、22個SVG）及6個核心SVG來源；模式為原生SVG搭配同源PCB像素與明示設定，並非新模型推論。資產位於_course_content/generated-concepts/<topic>/<topic>-d01-*，共同比較在det-yolo-dense。原型、逐圖brief、失敗及修正見共用TEACHING_REVIEW_LOG.md的WI-009；原始基準在tmp/detection-d01/baseline。
目前D01專屬3項測試通過（資產可達／核心語意／同源NMS算例），修正concept bridge至少三段callouts的構建錯誤。正式頁面構建、實際UI、逐圖分項與bundle驗證仍進行中；不能因來源整合就標示全數通過，也未獲使用者核准。


WI-009 D01驗證checkpoint：六題48個實際章節狀態全部通過；共44 tests（D01 3、navigation 3、companions 2、舊偵測renderer 36）通過；28張圖已實看，分項存d01-detector-review.json。來源verifier及bundle生成／verifier／hash與HTTP核對仍在執行，尚未最終結案。復原時先查tmp/detection-d01/run_checks.py的各log及現有final/report.json，不從產圖重跑。


WI-009 D01發布checkpoint：来源verifier已PASS；新增4項共用引用測試PASS；本機docs已生成1294資產／846.4 MB。package_checks.py仍在跑bundle-test及docs/index.html的完整verifier。當這兩項通過後執行tmp/detection-d01/closeout.py即可同步最終49項測試、48狀態、分項評分及記憶；不需重新產圖或再跑六題UI。


## WI-009 D01最終資產及驗證
WI-009 D01已完成本輪圖文重製及驗證（2026-09-06），待使用者審閱。六題各四幅主線、三個可見核心要點、移除設計及新情境自測；28個啟用資產。49項測試、48章節狀態、兩份HTML verifier及來源／bundle／HTTP一致性檢查通過。逐圖路徑、模式、設計意圖、分項、hash及限制見d01-detector-review.json和共用log WI-009。沒有新模型推論或外部部署，不宣稱已永久收斂。

生成模式：原生SVG＋既有PCB同源像素；核心PNG由瀏覽器輸出。設計意圖：讓同一A/B物件贯穿核心、反例與選型；訓練／推論、詞表／範例、框／mask分清。

- `_course_content/generated-concepts/det-dino-detector/det-dino-detector-d01-core.png`
- `_course_content/generated-concepts/det-dino-detector/det-dino-detector-d01-core-mobile.svg`
- `_course_content/generated-concepts/det-dino-detector/det-dino-detector-d01-failure.svg`
- `_course_content/generated-concepts/det-dino-detector/det-dino-detector-d01-failure-mobile.svg`
- `_course_content/generated-concepts/yolo-world/yolo-world-d01-core.png`
- `_course_content/generated-concepts/yolo-world/yolo-world-d01-core-mobile.svg`
- `_course_content/generated-concepts/yoloe/yoloe-d01-core.png`
- `_course_content/generated-concepts/yoloe/yoloe-d01-core-mobile.svg`
- `_course_content/generated-concepts/yolo-world/yolo-world-d01-failure.svg`
- `_course_content/generated-concepts/yolo-world/yolo-world-d01-failure-mobile.svg`
- `_course_content/generated-concepts/yoloe/yoloe-d01-failure.svg`
- `_course_content/generated-concepts/yoloe/yoloe-d01-failure-mobile.svg`
- `_course_content/generated-concepts/det-rtdetr/det-rtdetr-d01-core.png`
- `_course_content/generated-concepts/det-rtdetr/det-rtdetr-d01-core-mobile.svg`
- `_course_content/generated-concepts/det-rtdetr/det-rtdetr-d01-failure.svg`
- `_course_content/generated-concepts/det-rtdetr/det-rtdetr-d01-failure-mobile.svg`
- `_course_content/generated-concepts/det-grounding-dino-interface/det-grounding-dino-interface-d01-core.png`
- `_course_content/generated-concepts/det-grounding-dino-interface/det-grounding-dino-interface-d01-core-mobile.svg`
- `_course_content/generated-concepts/det-grounding-dino-interface/det-grounding-dino-interface-d01-failure.svg`
- `_course_content/generated-concepts/det-grounding-dino-interface/det-grounding-dino-interface-d01-failure-mobile.svg`
- `_course_content/generated-concepts/det-yolo-dense/det-yolo-dense-d01-core.png`
- `_course_content/generated-concepts/det-yolo-dense/det-yolo-dense-d01-core-mobile.svg`
- `_course_content/generated-concepts/det-yolo-dense/det-yolo-dense-d01-failure.svg`
- `_course_content/generated-concepts/det-yolo-dense/det-yolo-dense-d01-failure-mobile.svg`
- `_course_content/generated-concepts/det-yolo-dense/det-yolo-dense-d01-compare-known.svg`
- `_course_content/generated-concepts/det-yolo-dense/det-yolo-dense-d01-compare-known-mobile.svg`
- `_course_content/generated-concepts/det-yolo-dense/det-yolo-dense-d01-compare-prompt.svg`
- `_course_content/generated-concepts/det-yolo-dense/det-yolo-dense-d01-compare-prompt-mobile.svg`
# WI-013 R03 Sol re-review failed (2026-09-06)

- Actual candidate files inspected: `tmp/charuco-r03/final/desktop.png`, `mobile.png`, R03 SVGs, and manifest.
- Fixed-rubric result: desktop **25/100**, mobile **18/100**. Geometry is visible, but text is colored fallback blocks and mobile labels overflow; this is a hard visual blocker (`CHAR-P0-10`, `CHAR-P1-14`).
- Source repairs are only partial: `CHAR-P0-01/02/03`, `CHAR-P1-05`, `CHAR-P1-09`; delivery remains blocked. Additional issues: `CHAR-P0-11`, `CHAR-P1-12`, `CHAR-P1-13`, `CHAR-P1-15`.
- Next cycle is assigned to Luna as recorded in `TEACHING_REVIEW_LOG.md`; Sol will re-open actual PNGs after the next prototype. Formal R02 is preserved; no user acceptance.
# WI-013 R04 Sol review: HOLD (2026-09-06)

- Actual R04 PNGs scored desktop **78/100** and mobile **73/100**.
- Font blocker is fixed; generated board and detector evidence are present. Remaining issues are `CHAR-P1-16` broken correspondence notation, `CHAR-P1-17` missing board callouts, `CHAR-P1-18` desktop truncation, `CHAR-P1-19` mobile crop, and missing R04 manifest (`CHAR-EVID-20`).
- Luna is assigned R05 with concrete acceptance conditions in `TEACHING_REVIEW_LOG.md`. R04 remains a candidate; formal R02 is preserved and user acceptance is not recorded.
# WI-013 R05 Sol review failed (2026-09-06)

- R05 actual PNGs scored desktop **79/100** and mobile **72/100**, both failed.
- This is a mixed partial render: some desktop correspondence text changed, but visible titles remain R04, mobile/counterfactual still contain `qq/PP`, board callouts are absent, and crop/truncation remains.
- R06 handoff is recorded in `TEACHING_REVIEW_LOG.md`; formal topic and user acceptance remain unchanged.
# WI-013 R06 Sol review HOLD (2026-09-06)

- R06 actual scores: desktop **85/100**, mobile **86/100**; all prior blockers pass except desktop first-panel caption/evidence collision.
- R07 is assigned to Luna with a narrow layout-only acceptance condition. Formal topic remains unchanged; no user acceptance.
# WI-013 R07 prototype Sol pass (2026-09-06)

- Actual R07 desktop/mobile PNGs pass Sol at **92/100** each. Tracked layout, notation, callout, crop, and manifest issues are resolved.
- This is not formal-topic integration and not user acceptance. Next controlled action is versioned staging followed by Sol page recheck.
# WI-013 R07 integration blocked; R08 geometry fix (2026-09-06)

- Prototype R07 remains Sol-pass at 92/92. Candidate integration fails because the 720x1660 mobile SVG is mapped into the page's fixed 1672x941 nested image contract (`CHAR-INT-P0-01`).
- Packet filename mismatch is also recorded as `CHAR-INT-P1-02`; formal topic is unchanged, browser runtime unavailable, and user acceptance is not recorded.
- R08 must fix candidate-only mobile mapping and packet naming before Sol integration recheck.

# WI-013 R09 candidate packet normalization (2026-09-06)

- Candidate-only R09 packet: `tmp/charuco-r09/integration-packet.json`; identical compatibility copy: `tmp/charuco-r08/integration-packet.json`; R09 source bundle: `tmp/charuco-r09/`.
- `quality_status.current_mobile_asset` now matches the actual reading-view asset `_course_content/generated-concepts/charuco/charuco-r07-core-mobile.png` (720x1660, SHA256 `fbb2e5962e40707bde6e9c12080f9128a75635db6917793f14a50674560d5a09`).
- Desktop evidence now points to `_course_content/generated-concepts/charuco/charuco-r07-core.png` (1600x1080, SHA256 `be742adfe5fef789d9737ce33db22657eab3ca05e34174d88f5e31287afa9842`).
- Geometry contract SHA256: `5e0fcb33fd23422acc69e4315b8cba0368378ec1f42107360fc0e2657438c81d`; authoritative packet SHA256: `edebca1b830c1be08de2c664b989e1c9373069e36bc66caeea1356494291f929`; packet hash evidence: `tmp/charuco-r09/integration-packet.sha256.json` (mirrored under R08).
- Static evidence SHA256: `dfa25efdd4bc33846dd5a1acd37ff2f93167857db129c5cfa2b46f5e60c079b4`; browser unavailable, so no screenshot or runtime claim is made.
- Validation: `R09_STATIC_VALIDATION=PASS`; formal topic SHA256 remains `5298aecf02a3deaf1ef8d96755ad64bc6f58fea69c094aec93781c245cfe2895`. Browser unavailable; no live page claim, Sol recheck pending, user acceptance unrecorded.

# WI-013 R10 cleanup and final static gate (2026-09-06)

- R09 generated candidate page/wrapper now use R09 identity (`.candidate-r09`); stale R08 labels are absent from generated outputs. R08 references remain only as explicit source/compatibility paths.
- Geometry rollback is authoritative for `tmp/charuco-r09/`; R08 packet/hash files are listed as compatibility copies, while formal topic and R02-R09 remain preserved.
- `R10_STATIC_INTEGRATION_GATE=PASS`.
- Updated hashes: packet `613ee079425d52427e699558e841ea76a96b1f1cd4d01700898c9a3ffc922ef3`; candidate `5e5bda37c1d54276337f6a1231016e9e36de9f164a996c50e05d2688961c7f52`; contract `a4805de00e2e27a9b95cd34e3de053ef23ac7bb6de97c52c128fb06e984d82c9`; static evidence `68cdd1238f22adaf6391552466c9009aca5412d6b6da5c48eda737cacfa99945`.
- Browser remains unavailable; no runtime screenshot or Sol acceptance is claimed. Formal topic SHA256 remains `5298aecf02a3deaf1ef8d96755ad64bc6f58fea69c094aec93781c245cfe2895`.
# WI-013 R10 static integration pass (2026-09-06)

- Sol static integration passed after R10 cleanup. Candidate R09 is internally consistent and formal topic remains unchanged.
- Browser runtime is unavailable, so live page status is unassessed. User acceptance is pending; prototype Sol pass and static integration pass are recorded separately.
# WI-013 formal promotion complete (2026-09-06)

- User requested update; formal ChArUco topic now points to R07 assets and the HTML bundle was rebuilt successfully.
- R02 backup is preserved. Builder supports R07's explicit desktop/mobile dimensions and full-mobile branch.
- No live-browser claim: runtime unavailable. User acceptance remains pending.
# WI-013 formal chapter style failure and redesign (2026-09-06)

- Sol full-chapter review: 5 active visuals scored 60/78/79/85/81; overall 67/100. Earlier R07 92 is withdrawn for chapter/style use.
- Formal topic is now a mixed R07/v01 state and is not a valid final chapter. Luna is assigned an exactly-four-visual, all-Traditional-Chinese, image-led redesign.
- No new formal promotion will occur until each actual desktop/mobile image clears >90 and continuity checks pass.

# WI-013 R11 visual 1 prototype (2026-09-06)

- Candidate-only R11 prototype: `tmp/charuco-r11/brief.md`, `generate_r11.py`, `desktop.svg`, `mobile.svg`, `desktop.png`, `mobile.png`, `manifest.json`.
- Design: D comparison, one reading path, four nodes, same oblique/occluded board condition across pure chessboard / pure ArUco / ChArUco; no 2x2 card grid or speech bubbles.
- OpenCV evidence: `tmp/charuco-r11/board-evidence.json`, `DICT_4X4_50`, `cv2.aruco.CharucoBoard`, detector `24/24`, visible m17/m23/c17 callouts.
- PNG hashes: desktop `0df9317041f2c75259288a320be756e37ceff0167a91545900fb6e429822305f`; mobile `20d19add6a99af44a77db0ea138f515729ed0853bf4046e04c9afe50f5a43577`.
- SVG hashes: desktop `7caf2422bce26b3df21afccd9813f0d5a694abce331856f5c24a522d112511db`; mobile `63791b7e3929a4187ee695312e3fa77198846a696a0fd782ec452202a6e25715`.
- Preflight validator passed; actual PNGs were inspected. Formal topic, other visuals, Sol review, and user acceptance remain unchanged/pending.

# WI-013 R12 visual 1 physical-board correction (2026-09-06)

- R12 candidate-only files: `tmp/charuco-r12/brief.md`, `generate_r12.py`, `desktop.svg`, `mobile.svg`, `desktop.png`, `mobile.png`, `manifest.json`.
- Three distinct board sources are rendered under the same camera perspective and occlusion overlay: `chessboard-r12-8x6-board.png`, `aruco-r12-dict4x4-50-board.png`, and `charuco-r12-dict4x4-50-board.png`; board hashes are distinct.
- OpenCV evidence: pure ArUco `GridBoard` detector 24/24; ChArUco `CharucoBoard` detector 24/24; visible m17/m23/c17 callouts remain in the ChArUco lane.
- PNG dimensions/hashes: desktop `1600x900`, SHA256 `c0d40e1d0d41fb0751ba243ac8c1efb9eed1f2602206fa6cdce41011ec7ec904`; mobile `720x1280`, SHA256 `29c22ad6836b7ad6b702fe69b6702cb4f77263900deda098bfd7ef3275b6c609`.
- SVG hashes: desktop `f680bfed5cb65199d4008fb8de2dbc9cf2b1acbfee91367ed21436b57c098c68`; mobile `976fde1dfa19aebc8baa5a2c9ca16b3a0a3246bc99b4a37d176f22b2cf1a7f1f`.
- Preflight and `R12_BOARD_AND_ASSET_GATE` passed; both final PNGs were inspected. Formal topic, visuals 2-4, Sol review, and user acceptance remain unchanged/pending.
- Sol R12 re-review failed: desktop 84/mobile 77. Issues `CHAR-R12-P0-01` to `CHAR-R12-P1-04` are recorded in `TEACHING_REVIEW_LOG.md`; R13 is required before any formal promotion.

# WI-013 R13 visual 1 candidate (2026-09-06)

- Candidate files: `tmp/charuco-r13/brief.md`, `generate_r13.py`, `desktop.svg`, `mobile.svg`, `desktop.png`, `mobile.png`, `mobile-360-preview.png`, `board-evidence.json`, and `manifest.json`.
- Desktop PNG: `1600x900`, SHA256 `b89c70747e9561f47cd531e33cd3b277945b3f68e6361398dcb5e5e4a5bcf29c`; mobile PNG: `720x1280`, SHA256 `e641573edefa790c0e489729e09e376052b03f8a1f68494a80dd72e77e9e280a`.
- Desktop SVG SHA256 `158e6dc3c4833cad0c90dbddc1943b344c440e360974892bc579544e4d103892`; mobile SVG SHA256 `b7ef66943acf4701b325f96a2e5c0289b302a0f4b7dcb2f62cd807360f9a4372`; board evidence SHA256 `58fc68531a2bfa8854f67fcafcaaed075ea462596717f4283f918574d182b215`.
- Board evidence uses distinct chessboard, `cv2.aruco.GridBoard`, and `cv2.aruco.CharucoBoard` assets under `DICT_4X4_50`; ArUco and ChArUco detector counts are `24/24`.
- `validate_teaching_preflight.py` passed; `R13_STATIC_AND_360_GATE=PASS`. `view_image` inspected desktop, mobile, and the 360px-equivalent preview. Browser evidence is not claimed; Sol review and user acceptance remain pending.
- Formal topic remains unchanged (`formal_topic_connected=false`); no batch rebuild or promotion occurred.

# WI-013 R13 Sol actual-PNG review (2026-09-06)

- Sol directly inspected `tmp/charuco-r13/desktop.png`, `mobile.png`, and `mobile-360-preview.png` with `view_image`; desktop/mobile hashes match the R13 manifest, and the 360 preview SHA256 is `6d7fc11f551a2efe212a110c01dda8f8a354da526eb859ffcbdb46f9e6023c1c`.
- Fixed rubric v1.0: desktop **96/100** `[24,24,19,19,10]`; mobile **94/100** `[24,23,19,18,10]`. Completion checks are desktop `[9,9,9,9,9]`, mobile `[9,9,9,8,9]`; no veto applies.
- `CHAR-R12-P0-01` through `CHAR-R12-P1-04` all pass in actual pixels: corrected same-condition wording, safe ArUco marker-corner precision wording, visible blue/green merge arrows, and readable uncropped 360px output.
- No new P0/P1 was found. Non-blocking `CHAR-R13-NB-01`: the non-rendered board evidence still contains stale `fewer corner samples`; clean it and update evidence/manifest hashes before archival or integration.
- Status: **visual 1 prototype technical pass only**. R13 is not connected to the formal topic, visuals 2-4 are not complete, the full chapter is not passed, and user acceptance is pending.
- Next action: clean the evidence wording/hash, then create visual 2 as the same-case C path from m17/m23/c17 to q17/P17, PnP, predicted c17, and residual.

## WI-019 啟動
- 審查 13 課；證據將存 review-evidence/wi-019/。未產圖或改正式引用。Browser runtime 無可用實例，將用 standalone Playwright；尚未驗證公開版本。
- F01 只代表核心導入修訂歷史，不能當本輪全課合格證據。

WI-019 checkpoint：13 課 26 個頁面擷取完成；公開 HTML 與 docs hash 一致。桌面前 8 課首讀圖已看，標題／圖義錯配與 RD4AD 黑框待查來源。手機自動無頁面橫向溢出不代表可讀，人工檢視尚未完成。
# WI-019 審查完成（2026-09-08；取代本項較早進行中紀錄）

- 本輪生成模式：無教學產圖，僅抓取既有公開頁面與截圖、抽取原參考 PPT 圖；未改 topic／HTML／正式資產，未發布。
- 已完成：13 課 65 張桌面首讀圖實看與 v1.0 五分項評分；26 張手機首兩圖 viewport 實看；130 次放大開啟／Escape、26 組解答與下一課導航。13 張手機首圖放大曾提早取樣，`check_zoom_load.py` 補等載入全部通過；另實看 SubspaceAD／AnomalyGPT 放大完成截圖，放大後仍需橫移，不能用載入通過替代可讀性。
- 產物：`review-evidence/wi-019/` 的公開基準、65 圖 inventory/hash、capture.json、interactions.json、zoom-load-check.json、assessment.json、各課桌面／手機截圖。唯一審查敘述在 root `TEACHING_REVIEW_LOG.md` WI-019。
- 結論：13 課首讀須重整，網站基礎可保留；6 課保留核心思路重編後續、7 課大幅重建。RD4AD／AnomalyGPT 優先矯正；AE 為建議先做的完整原型。
- 學習：已併入網頁指南既有標題語意規則／F01 補充、圖片指南 RULE-009，無新主題 review log、無評分權重更動。
- 尚未評估：隱藏正式 slide 圖逐張審查、手機後續所有橫向區域、整課總分、最終五項完成度、真人理解。WinCLIP+ 的否定近鄰匹配文字待原始公式核對；不宣稱確定錯誤。
- 下一步：本輪審查可交付；後续製作需明確範圍，先版本化 preflight 與單張實際桌面／手機原型。技術審查、自評、正式引用及使用者核准持續分開；使用者核准仍 pending。
## WI-021 產圖前 checkpoint（2026-09-09）
- 即將執行：AE C1 r01 內建 imagegen 原型；brief 在 `workitems/wi-021/ae-c1-r01.md`，四節點，正常學習／待測重建／差異比較與 p 覆核。
- 已完成：WI-019 缺口已寫回共用指南，本輪新增製作授權；指定參考已實看。
- 生成意圖：教學示意、同板身分與刮傷位置固定、重建不是正常真值；尚未產圖，原型審查／其餘課／整合皆未完成。
- 保存：預定 `_course_content/generated-concepts/ad-ae/ad-ae-wi021-c1-r01*.png`，內建工具原始輸出需複製進專案；正式引用未改，使用者核准 pending。
WI-021 AE r01 生成 checkpoint：內建 imagegen 已實際產圖並保存 `workitems/wi-021/ae-c1-r01.png`。實看發現訓練權重箭頭接到差異圖，非推論 AE；r01 不通過，下一步生成 r02 修正交接與限制註記。其他課未展開，正式引用未改。
WI-021 AE 五張候選 checkpoint：C1 桌面 r02／手機 r04 自評可展開；C2 桌面 r02、C3 桌面 r02 已修比較來源；D4／D5 桌面 r01 已生成但待修。C2 手機把「訓練前重建」誤寫成「原始影像」，需改標籤；D4 正常小孔 q 的熱區位置需對齊；D5 AE 比較的兩條來源線竟都接重建圖，需改回原圖旁路，DRAEM 訓練標籤需說合成異常重建正常。下步先修這三項，再補 C3/D4/D5 手機與整課預覽。產物均在 `workitems/wi-021/`，其餘12課未製作、正式topic與HTML未改。

# WI-033：第二部分 52 課局部修正

開始日期：2026-09-12。使用者授權「繼續第二部分」。依據根 Overall_Review.md 與 WI-031/REPORT.md；第一部分已發布，保持其有效成果。

## 範圍與驗收

保留成立的首讀主線，修正 52 課工程圖、指定反例／比較、五課指定深讀及手機可讀性；連動圖說與交付內容。每圖先 preflight、參考與原型，再逐張審查；沿用 v1.0，每張新啟用圖及完成課頁各 >90、無否決項，五項完成度各 >=8。工具、視覺自評、使用者審閱及發布分開。既有 commit／push 指示屬第一部分收尾；本輪先完成本機成品及驗證，發布狀態另記。

## 執行 checklist

- [x] 核對五份權威 Markdown、基準來源／已執行程序、52 課完整修正清單，保存基準。
- [x] 第一批：CLIP、SigLIP、Pose Pipeline、DINOv3、DiffusionAD、AnomalyGPT；修工程語意與各課已列手機／反例。
- [x] 第二批：Lucas–Kanade、RAFT、AnomalyDINO、EfficientAD；同條件比較及深讀缺口。
- [x] 第三批：ResNet、ConvNeXt、ViT、U-Net、SegFormer、YOLO-Seg、Keypoint R-CNN。
- [x] 第四批：YOLO dense、RT-DETR、Grounding DINO、YOLOE、DINOv2、LLaVA、Qwen-VL、Gemini Vision。
- [x] 第五批：PatchCore、PaDiM、SubspaceAD、STFPM、RD4AD、AE、DRAEM、UniAD。
- [x] 第六批：Dinomaly、InvAD、DDAD、WinCLIP、AnomalyCLIP、Frame Difference、Background Subtraction、ByteTrack。
- [x] 第七批：ConvLSTM、VideoMAE、V-JEPA、DefectFill、AnomalyDiffusion、TF-IDG、ControlNet、Inpainting、Diffusion Restoration、Deblur、Super-resolution。
- [x] 全站必要回歸、逐課資產／來源／docs／HTTP 核對，保存學習、報告與維護副本。

批次不縮減整體 52 課授權；每課細項將由 inventory.json 與各批審查紀錄追蹤，通過實作與驗證後才完成。下次中斷後先核對磁碟及程序，從第一個未完成步驟繼續。

## 初始 checkpoint

已讀 WORKITEMS、TODO、STATUS 與 Overall 第二部分，Git 無未提交修改；正在閱讀適用指南與既有工程層整合方式。下一步保存目前 58 課基準、52 課清單，實看 CLIP 參考與舊工程圖，建立首張原型 preflight。尚未製作／評分／測試，第二部分完成 0/52，無阻礙。

最新 checkpoint：165 份課程基準與五權威快照、52 課 inventory 已保存。沒有前輪生成程序仍在執行；沿用 8000 服務。CLIP 工程 2 r01／r02 缺口保留，r03 桌機手機原生圖自評93／92，preflight通過；詳見 prototype-review.md。尚未整合、頁內驗證／回歸未跑，完成仍0/52。下一步完成 CLIP／SigLIP 其餘工程頁及手機比較，再整合驗證，依計畫繼續其餘課程。

CLIP／SigLIP checkpoint：9 份選定 preflight 通過，17 張待啟用 PNG 原生審查有逐項理由（16 工程＋1 共用手機比較）；分數91–93，使用者核准pending。已更新兩課來源、工程 manifest／model.md，舊泛用工程橋接圖退出啟用，歷史來源保留。即將建置 course／docs 並跑8個桌機手機狀態；驗證尚未執行，完成仍0/52。預期證據 alignment-image-assessment.json、alignment-active-assets.json、pages/clip 與 pages/siglip。下一步頁內實看與必要測試，然後繼續第一批另四課。

## 手機實頁複核 checkpoint

CLIP／SigLIP 已接入16張工程PNG與1張手機比較，8頁狀態、8 tests／120 subtests通過。已實看全部新工程圖桌機手機頁及保留主線；SigLIP首讀手機圖仍細字密集，正在補修，故整課完成仍0/52。即將生成 SigLIP手機核心与Pose分支原型，11份preflight通過。其餘50課待製作；第一部分保持已發布，第二部分尚未發布，使用者核准pending。下一步實看新候選、整合及重驗，再接第一批另四課。

QA初次複製脚本時工作目錄錯誤，修正後執行成功；未影響教材來源。回歸命令：`python -m pytest tests/test_engineering_mobile_pages.py tests/test_github_pages_bundle.py tests/test_interactive_navigation.py -q`，實際8 passed、120 subtests passed、91.84s。

## CLIP／SigLIP 完成本機修正

- [x] CLIP：四工程與共用手機比較，原生／頁內／來源HTTP驗證。
- [x] SigLIP：四工程、共用手機比較与手機核心，原生／頁內／來源HTTP驗證。

CLIP／SigLIP本機修正、自評與驗證完成，第二部分2/52。18張啟用新PNG逐張原生／頁內實看；8頁狀態、56放大、8自測／導覽、56 HTTP與1351資產hash通過；8 tests／120 subtests通過，SigLIP手機核心補修後四頁狀態另通過。其餘50課未完成。Pose四工程及DINOv3訓練原型已實看，尚待評分整合；DINOv3其餘與DiffusionAD／AnomalyGPT原型即將製作。下一步從PLAN第一批未完成處接續。第一部分已發布；第二部分未commit/push，使用者核准pending。證據：alignment-page-assessment.json、verification-clip-siglip.json；首批其餘四課不可打勾。

## 第一批其餘四課 checkpoint

Pose四工程已原生實看與記分後整合；首次建置被每圖需兩個名詞的來源契約攔下，補入R/t及重投影定義後重建。舊HTML未被失敗的來源建置覆寫；新增build.py讓來源建置失敗時不再繼續bundle。DINOv3主反例与工程4曾重複，工程4改同題換骨幹取捨；DiffusionAD/AnomalyGPT r02核心原型原生實看通過，將延伸各自其他三工程。尚未宣稱這四課完成；第二部分仍2/52。

- [x] Pose：八工程PNG原生／頁內與完整課程審查；4狀態28放大、32HTTP、1351資產一致。證據pose-page-assessment.json與verification-pose.json。

## 接續 checkpoint

第二部分完成 3/52 課本機修正與驗證：Pose Pipeline、CLIP、SigLIP。DINOv3、DiffusionAD、AnomalyGPT工程來源已整合，DINOv3同件反例已更新；26張新候選原生審查完成，整頁仍待驗。即將對這三課跑12個頁面狀態，AnomalyGPT首讀手機密字也須實看後減量。其餘批次尚未製作。上一批必要8 tests／120 subtests通過；本批先驗實頁，不以原生圖分數當整课完成。 第二部分未commit/push，使用者成品核准pending。

AnomalyGPT首讀三張手機原圖已實看：核心四段密集、反例四段多餘人物與細節、比較四段；即將以三組2304高手機SVG減量，保留原p/q與兩孔板身份，工程4另有教學責任。三課頁面驗證先跑目前工程版，之後僅補驗改動範圍。

第一批六課完成本機修正。新增本三課29張啟用PNG原生與頁內審查；12狀態、84放大、自測/導覽、來源HTTP与全站資產hash通過，數量以verification-dinov3-ad-diffad-ad-anomalygpt.json為準。其餘46課仍待修，使用者核准pending。

## 接續 checkpoint

第二部分完成 6/52 課本機修正與驗證：Pose Pipeline、DiffusionAD、AnomalyGPT、DINOv3、CLIP、SigLIP。第一批六課修正完成，第二批正在核對LK／RAFT共同反例、AnomalyDINO旋轉案例与EfficientAD深讀缺口；即將建立各自機制原型。52課授權範圍不縮減；其餘批次尚未製作。第一批8 tests／120 subtests通過，後續主圖改動另跑實頁補驗。 第二部分未commit/push，使用者成品核准pending。

第二批即將製作16工程與3個主/深讀故事，共19組桌機手機SVG候選。先看四課工程2原型：LK梯度算例、RAFT查詢更新、AnomalyDINO局部查庫、EfficientAD雙分支。EfficientAD七章手機另外排版，未在本19組內宣稱完成。候選與正式引用分開；render前preflight逐份驗證。

第二批即將製作16工程與3個主/深讀故事，共19組桌機手機SVG候選。先看四課工程2原型：LK梯度算例、RAFT查詢更新、AnomalyDINO局部查庫、EfficientAD雙分支。EfficientAD七章手機另外排版，未在本19組內宣稱完成。候選與正式引用分開；render前preflight逐份驗證。

第二批即將製作16工程與3個主/深讀故事，共19組桌機手機SVG候選。先看四課工程2原型：LK梯度算例、RAFT查詢更新、AnomalyDINO局部查庫、EfficientAD雙分支。EfficientAD七章手機另外排版，未在本19組內宣稱完成。候選與正式引用分開；render前preflight逐份驗證。

第二批即將製作16工程與3個主/深讀故事，共19組桌機手機SVG候選。先看四課工程2原型：LK梯度算例、RAFT查詢更新、AnomalyDINO局部查庫、EfficientAD雙分支。EfficientAD七章手機另外排版，未在本19組內宣稱完成。候選與正式引用分開；render前preflight逐份驗證。

即將生成EfficientAD深讀8組候選：1章核心/工作、2/3/4/5/7/8；4/7桌機手機都替换，其餘只啟用手機。第6可追算流程保留，所有章節正文與自測保留必要涵義。預期10張啟用PNG，尚未審查/整合。

第二批即將製作16工程與3個主/深讀故事，共19組桌機手機SVG候選。先看四課工程2原型：LK梯度算例、RAFT查詢更新、AnomalyDINO局部查庫、EfficientAD雙分支。EfficientAD七章手機另外排版，未在本19組內宣稱完成。候選與正式引用分開；render前preflight逐份驗證。

第二批即將製作16工程與3個主/深讀故事，共19組桌機手機SVG候選。先看四課工程2原型：LK梯度算例、RAFT查詢更新、AnomalyDINO局部查庫、EfficientAD雙分支。EfficientAD七章手機另外排版，未在本19組內宣稱完成。候選與正式引用分開；render前preflight逐份驗證。

第二批48張新PNG逐張原生桌機/手機實看與逐圖理由已保存batch2-image-assessment.json（92–93）。四課工程、共用光流反例、ADINO旋轉及Eff同件反例/深讀已接入來源；即將build與實頁驗證，完成仍6/52。Eff第6章可追算舊圖保留，其餘保留桌機圖與新手機需共同實頁核對。

## 接續 checkpoint

第二部分完成 6/52 課本機修正與驗證：Pose Pipeline、DiffusionAD、AnomalyGPT、DINOv3、CLIP、SigLIP。第一批六課完成；第二批LK、RAFT、AnomalyDINO、EfficientAD的48張新PNG已逐張原生審查並接入來源，四工程/共同光流反例/旋轉深讀/同托盤反例與指定深讀已修正。正在建置，下一步跑16主頁狀態與64深讀章節狀態，實看頁面後才完成四課。其餘42課尚未製作。第一批8 tests／120 subtests通過；第二批新實頁與深讀回歸尚未跑。52課授權範圍不縮減。 第二部分未commit/push，使用者成品核准pending。

深讀QA脚本r01失敗：SVG放大使用object，脚本誤等img，且失敗後未關modal導致後章點擊被擋。保存failed-r01報告，停止該程序；已改支援img/object並finally關閉，重新驗證。這是QA腳本缺口，不把未驗章節當完成。

實頁複核發現新反例的較長圖說緊貼放大按鈕；手機版圖說改標題獨立一行，按鈕下排。改動位於共用builder的手機CSS，將核對58課圖說与本批深讀，不能只以頁面無水平overflow判通過。第二批10 tests/130 subtests（360.63秒）、16主頁/112放大/116HTTP與1364資產hash已通過，CSS補修後仍需重建補驗。


## WI-033 持續完成授權（2026-09-12）

使用者要求「一口氣完成」第二部分全部52課，批次之間持續執行。最後完成6課；第二批4課48張新PNG已接入，先前10 tests/130 subtests及16主頁驗證有紀錄。手機CSS補修後的補驗未完成。已核對沒有WI-033生成/QA程序仍執行，本機8000服務存在。
即將重建後核對58課手機圖說、第二批深讀與主頁，再完成後42課；產物與唯一checklist在workitems/wi-033/PLAN.md。使用者成品核准pending，未發布。本次新測試尚未跑。首次接續註記經PowerShell管線發生中文字編碼損失，已用UTF-8檔案修正；教材未受影響。



### WI-033 第三批原型與第二批補驗（2026-09-12）

第三批7課28故事preflight已通過；即將渲染ResNet、ConvNeXt、ViT、U-Net、SegFormer、YOLO-Seg、Keypoint R-CNN的工程2原型（精確SVG→桌機/手機PNG），尚未原生審查或整合。已實看共同幾何契約參考；用具體格位、殘差算例、尺度映射與具名點提供機制證據，保留原有效主線。來源及設計在plan-batch3.py與各圖r01.md。

第二批CSS後補驗：15/16主頁通過；LK桌機及EfficientAD部分深讀出現圖片decode錯誤，保留batch2-deep-report-decode-failed-r02.json。正在核對是來源損毀或lazy/picture選圖時序，不能當通過。全站手機圖說QA尚在執行；完成仍6/52，使用者核准pending，未發布。下一步原型審查與修正補驗。


### WI-033 第二批補驗通過、視覺證據收尾（2026-09-12）

第三批7課28故事preflight已通過；即將渲染ResNet、ConvNeXt、ViT、U-Net、SegFormer、YOLO-Seg、Keypoint R-CNN的工程2原型（精確SVG→桌機/手機PNG），尚未原生審查或整合。已實看共同幾何契約參考；用具體格位、殘差算例、尺度映射與具名點提供機制證據，保留原有效主線。來源及設計在plan-batch3.py與各圖r01.md。

第二批CSS後補驗：16/16主頁與64深讀章節狀態通過。原圖片decode錯誤在等待實際lazy/picture載入後重驗成功，失敗報告保留。全站58課178個手機圖說間距通過（caption-verification.json），QA原來以來源JSON不存在的id欄位取slug，已改檔名並嚴格驗58課。第二批桌機手機16工程與新主反例頁內已實看；EfficientAD深讀長元素截圖有合成空白及sticky遮擋，單步crop-diagnostic.png正常，正在逐段補證據，不當教材壞圖。深讀來源/docs相同。完成仍6/52，使用者核准pending，未發布。

第三批原型r01缺口已記prototype-review.md；ResNet/YOLO/Keypoint r02與ConvNeXt/U-Net/SegFormer r03正在複核，ViT r01候選。尚未擴展其餘21故事、整合或計為完成。下一步第二批深讀視覺收尾與第三批原型通過後擴展。


### WI-033 最新：10/52課本機完成（2026-09-12）

第一、二批共10課完成修正與必要驗證；第二批48張新PNG、16主頁/112放大/116HTTP/1364資產一致、64深讀章節狀態、58課178手機圖說間距，11 tests/126 subtests通過。長元素截圖錯誤已逐段補證據，第六章來源保留，未當破圖。證據：workitems/wi-033/batch2-validation-summary.json與batch2-page-assessment.json。
第三批7課28故事preflight已寫，七個工程2原型修正中；其餘35課尚未製作。即將完成第三批原型審查並擴展其他工程/指定深讀，所有未完成仍待辦。使用者要求一口氣完成52課；使用者成品核准pending，未commit/push/發布。唯一checklist：workitems/wi-033/PLAN.md。


### WI-033 第三批擴展（2026-09-12）
完成數仍10/52。七模型工程2原型已原生實看/記分，版本與證據見batch3-prototype-image-assessment.json。即將渲染其餘21個工程故事（42PNG），精確SVG模式，不是模型實測；尚未逐圖審查、整合、頁內驗證或完成指定深讀。第三批全部範圍及後35課持續執行；使用者成品核准pending，未發布。


### WI-033 第三批擴展原生複核

其餘21故事42PNG已產出；21張桌機圖已實看，手機尚未逐張看。發現U-Net工程1及SegFormer工程4輸出壓字、粗取樣示意不應以人工斷線代替、YOLO去重前後顯示尺度不同、Keypoint無目標箭頭、ViT刮傷誤稱缺口。七故事r02 preflight通過，即將重渲染14PNG後原生複核；舊r01保留但不採用。七課指定深讀仍未完成、頁內/新測試未跑，完成數10/52，使用者核准pending。下一步逐張手機審查，保留深讀原實測來源並重排，然後整合驗證。產物：workitems/wi-033/revise-batch3-expanded.py、engineering-plan.json及各版本PNG。


### WI-033 第三批工程來源整合、深讀原型

七課28工程故事56張選定PNG已逐張桌機/手機實看並接入來源；新增44張（21故事及ViT工程2修訂）證據在batch3-expanded-image-assessment.json，其餘12張在prototype assessment。壓字、取樣誤示、去重尺度、刮傷命名、ConvNeXt逐通道限定及乙標籤均已修正；歷史候選未啟用。尚未build或頁內驗證，不增加完成數。

ResNet/SegFormer深讀兩家族原型preflight通過，即將用deep-batch3-reflow.py重排既有SVG證據區塊，保留原內嵌場景、實際特徵值與示意身份。預期resnet-deep-residual與segformer-deep-core r01手機768×2800；未實看、未整合。其餘指定深讀仍待製作。下一步原型實看後擴展其餘9種深讀圖，再build/實頁驗證。完成10/52，使用者核准pending，未發布。


### WI-033 深讀兩家族原型通過、擴展九圖

第三批56工程PNG已原生實看接入來源，尚未build。ResNet residual r02及SegFormer core r04手機原型已實看記分，精確clipPath避免viewBox留白區滲入鄰字，進一步避開半行字；來源實測數字與原場景保留。證據batch3-deep-prototype-image-assessment.json。九份擴展preflight通過，即將deep-batch3-expanded.py產出九張手機2800高PNG；未逐圖審、未整合、未驗實頁。下一步審查九图後整合指定深讀並build/驗證。完成10/52，使用者核准pending，未發布。


### WI-033 第三批全部來源接入，開始建置

第三批七課56工程PNG及11張深讀手機PNG已逐張原生審查（12處深讀引用，ResNet殘差共用）；指定ResNet2/4/8、SegFormer1/3/4/5接入完成。BN算式放大、跨欄殘箭頭/碎字/切斷圖格已修正，實際特徵與桌機來源保留。原生assessment與batch3-deep-active-assets.json保存hash、來源及舊引用。即將build.py重建，預期28主頁狀態與64深讀章節狀態、自測/放大/導覽、來源docs/HTTP與必要回歸。新驗證尚未跑，完成仍10/52，使用者核准pending，未發布。之後繼續第四批八課與後27課。


### WI-033 第三批建置尺寸契約補修

第三批67張選定新PNG已逐張原生實看並接入。建置因768×2800不在尺寸允許清單而失敗，未覆寫HTML；已僅新增此明確尺寸，其他錯誤尺寸仍拒絕。計畫重建後驗證圖片契約、ResNet/SegFormer深讀與共用頁面回歸，再跑28主頁與64深讀章節/HTTP資產驗證。新測試未跑，完成仍10/52。來源與assessment保存在workitems/wi-033；使用者核准pending，未發布。後35課仍待完成。


### WI-033 第三批深讀重驗通過、主頁補驗中

第三批67張新PNG已原生審查接入並完成建置，1365資產。ResNet/SegFormer依序重驗64章節狀態全部通過（batch3-deep-report.json）；先前並行QA載入失敗紀錄保留。回歸15 tests/120 subtests通過，2項舊媒體數斷言重複計桌機與手機；已改分別驗視圖/桌機/手機數量並限定深讀容器，補驗未通過前不計完成。ConvNeXt主頁4狀態通過，其餘6課主頁待補驗及頁面實看/HTTP hash。第四批8課工程2原型preflight已落盤，尚未渲染；其餘24故事、兩主反例及後27課待做。完成數仍10/52，使用者核准pending，未發布。下一步完成第三批主頁與測試證據，同時製作第四批精確SVG原型；產物在workitems/wi-033。


### WI-033 第三批測試與深讀完成、第四批即將渲染

第三批17項測試已通過（原15 tests/120 subtests，補驗2 tests/21.23s）；深讀64狀態通過，11種新手機圖已逐張頁內實看，證據batch3-tests-supplement.json、batch3-deep-page-review.json。ResNet與ConvNeXt主頁各4狀態通過，其餘五課正在QA，尚待全部頁面實看與HTTP資產核對，完成數仍10/52。第四批8工程2原型已通過preflight並完成新SVG場景程式，即將render.py產出16PNG；未原生審、未整合。預期workitems/wi-033/*-engineering-2-r01-{desktop,mobile}.png。後續24工程故事、兩個主反例與後27課持續執行。使用者核准pending，未發布。


### WI-033 第四批候選繪製缺畫補修

第四批r01桌機8圖及前4手機已實看，發現RT/Grounding輸出PCB與部分手機文字缺畫，SVG節點仍完整；候選不啟用。已修改渲染為disable-gpu、等待字型及500ms，八份r02 preflight通過，即將重繪16PNG。另統一NMS前後顯示尺度、YOLOE全電阻半透明遮罩、DINO遮蔽名稱及Qwen解析度標題。尚未確認修復，剩四張r01手機不浪費重審，直接檢查全部r02。第三批ResNet/ConvNeXt/ViT/U-Net/SegFormer主頁通過，另兩课QA中；完成仍10/52，使用者核准pending。


### WI-033 最新：17/52課本機完成（2026-09-12）

第三批七課完成本機修正與驗證：56工程PNG、11深讀手機PNG（12引用）；28主頁/196放大/196HTTP/1365資產一致、64深讀狀態、17 tests及120 subtests通過。逐張原生與頁內證據在batch3-page-assessment.json、batch3-deep-page-review.json、batch3-validation-summary.json。保留首讀主線與原實测數據，使用者成品核准pending，未發布。
第四批8課工程2共16張r02候選已渲染，尚未原生複核或整合；r01缺畫未啟用，改disable-gpu及等待字型。下一步審查r02後擴展24工程故事、DINOv2/Gemini同件主反例，再驗八課。後27課仍待製作，持續完成全部52課授權。唯一checklist在workitems/wi-033/PLAN.md。


### WI-033 更正第四批缺畫判斷

獨立新browser重拍Grounding r02，與候選PNG逐像素完全相同（difference bbox=None）；RT r01被認為缺圖處的像素也是PCB色(217,236,230)。因此先前「PNG缺畫」判断撤回：是審查顯示誤判，沒有證據顯示原PNG損壞或disable-gpu修復了圖。ground-render-diagnostic-fresh.png已完整實看；證據render-diagnostic-result.json。保留r02實質尺度/透明遮罩/命名修正，繼續逐張審查；不再為顯示誤判重畫教材。第三批完成17/52，第四批其餘工程及後27課持續；使用者核准pending。


### WI-033 第四批八原型原生審查完成

八課工程2選定16PNG已逐張原生實看並記錄92分自評（非使用者核准）：DINOv2 r03，其餘r02。證據batch4-prototype-image-assessment.json；Grounding缺畫判斷已透過独立重拍/逐像素比對撤回，PNG內容完整。即將建立其餘24工程故事與DINOv2/Gemini同件主反例preflight並渲染；未整合、未驗頁。完成17/52，後35課持續；使用者核准pending，未發布。


### WI-033 第四批其餘24工程故事即將渲染

八原型16PNG已原生審查，DINOv2 r03其餘r02；其餘24故事preflight與具體SVG路由已完成。即將render-batch4-expanded.py產出48張1672×941/768×2304候選PNG，尚未原生實看/整合/頁內驗證。使用原PCB雙電阻、L支架與接頭/銘牌的機制、映射、查庫距離及交付例；不跑模型。DINOv2/Gemini兩主反例仍待獨立修正。完成17/52，下一步逐圖審查與兩主反例，再整合八課。產物在workitems/wi-033，使用者核准pending。


### WI-033 兩個同件主反例即將渲染

第四批24故事48工程PNG正在渲染，尚未逐圖看。兩個主反例preflight通過：DINOv2同L支架右緣小缺口＋給定近距離反例；Gemini主線同圓接頭的格式/內容雙檢查。即將產出4PNG，未審查/整合/驗頁；不新增模型實測。產物workitems/wi-033/{dinov2,gemini-vision}-main-failure-r01-*.png。完成17/52，所有後續課程持續，使用者核准pending。


### WI-033 第四批桌機審查：驗收例前後一致

24工程候選48PNG與兩反例4PNG產出，正在逐張原生看。前三種detector工程3末格原畫高重疊重複框，接在明確NMS後容易造成同算例矛盾；改為「另驗定位偏移與漏框」，保留前述去重算例。三份r02 preflight通過，即將重渲染6PNG；其他桌機與全部手機審查未完，未整合。完成17/52，使用者核准pending。


### WI-033 第四批工程分工補修

24張擴展桌機r01已實看，全部手機尚待看；三個detector工程3 r02產出未複核。Grounding/LLaVA/Gemini工程1與工程2整張過度重複，改工程1為任務、詞區域對應與欄位交付；工程2保留機制。另縮短LLaVA/Gemini覆核文字，Gemini設定改公開模型識別/schema。五份r02 preflight通過，即將渲染10PNG，未整合。原型仍16PNG通過，兩主反例4PNG待看。完成17/52，使用者核准pending。


### WI-033 第四批選定桌機已審、手機逐張複核中

選定24張擴展桌機（含8張修訂）已原生實看；YOLO、RT-DETR六張手機及Grounding工程1/3手機已實看，另16張手機待看。八原型16PNG已審；兩同件主反例4PNG已審並由promote-batch4-failures.py接入來源，未建置。下一步剩餘手機、48張擴展assessment、整合八課工程、建置與32狀態/頁內審查/HTTP及測試。產物workitems/wi-033；完成仍17/52，使用者核准pending。前述PNG缺畫判斷已撤回，以render-diagnostic-result.json為準。繼續全部52課授權。


### WI-033 第四批68張選定PNG原生審查完成

32工程故事64PNG（16原型+48擴展）及兩個主反例4PNG皆逐張實看，原生自評92、五完成度>=8，使用者核准pending。證據batch4-{prototype,expanded,failure}-image-assessment.json；兩反例已接來源。即將整合八課工程並build.py建置course/docs，再跑32主頁狀態/224放大、來源HTTP一致與必要8 tests/120 subtests，逐張實頁複核。新實頁驗證未跑，完成仍17/52；後27課繼續。產物workitems/wi-033。


### WI-033 第四批建置完成、第五批機制原型preflight

第四批已建置1371資產/963.7MB；32主頁狀態與8 tests/120 subtests執行中，尚未整批完成。第五批八課原首讀桌機已逐張實看，查核論文/官方repo；八份機制原型preflight通過。即將製作16PNG：查庫距離、位置協方差、正交投影、STFPM逐層差、RD瓶頸反向重建、AE差110、DRAEM雙監督、UniAD注意力連線。其餘24工程故事與PatchCore第二章手機尚未製作。產物workitems/wi-033，完成仍17/52，使用者核准pending；全部52課持續。


### WI-033 第四批自動驗頁通過，逐圖頁審過半

八課32主頁狀態/224放大/自測與導覽通過；8 tests/120 subtests通過127.30s，證據batch4-tests.json與pages各report.json。YOLO/RT/Grounding/YOLOE全部32張新工程桌機手機頁內圖已逐張實看，剩四課32工程頁圖與兩主反例4頁圖待看；來源/HTTP verify-batch.py執行中。第五批八機制原型16PNG已渲染未審，不能整合；PatchCore深讀與24擴展仍待做。完成仍17/52，使用者核准pending，全部52課持續。下一步完成第四批審查並驗hash，接第五批原型。產物workitems/wi-033。


### WI-033 最新：25/52課本機完成

第四批8課已完成64工程PNG/4同件主反例，逐張原生與頁內審查；32頁面狀態224放大、8 tests/120 subtests、來源docs及HTTP一致通過。證據batch4-page-assessment.json、batch4-failure-page-review.json、batch4-validation-summary.json；使用者核准pending，未發布。驗證脚本已依實際收合設計在展開後查模型背景，重驗通過；先前PNG缺畫誤判已撤回。
第五批8課機制原型16PNG已生成尚未原生審；24工程擴展與PatchCore深讀手機第二章待做。下一步逐張審原型/修正，再擴展整合驗頁；後19課繼續，全部52課授權不縮減。產物與唯一checklist：workitems/wi-033/PLAN.md。


### WI-033 第五批原型桌機審查補修

第四批已完整本機完成，累計25/52。第五批八張r01桌機原生實看，發現PatchCore/PaDiM文字超框、PaDiM橢圓壓算式、RD瓶頸壓圖說；同時補STFPM已對齊同位置、AE q與DRAEM mask、UniAD局部範圍。八份r02 preflight通過，即將渲染16PNG，r01未整合。第五批手機、擴展24故事/PatchCore第二章深讀待做；使用者核准pending，全部52課繼續。


### WI-033 第五批八機制原型原生審查完成

八課r02機制16PNG已逐張桌機/手機實看，自評92且完成度>=8，證據batch5-prototype-image-assessment.json；原型未整合或驗頁。即將擴展24工程故事及PatchCore第二章兩手機深讀，保留實際ResNet50數值/原作者和第三方案例。完成25/52，使用者核准pending，後27課持續；產物workitems/wi-033。


### WI-033 PatchCore第二章兩手機深讀即將重排

第五批機制16PNG已原生審查，未整合；其餘24工程故事待製作。PatchCore第二章兩份preflight通過，原SVG檢查圖已實看並核對cnn-features.json的原精度4.695003/4.065633/3.911689。即將產出patchcore-deep-{features,context}-r01-mobile.svg/png（768×2800），保留原像素/特徵證據、桌機和其他章節。候選未審/整合；下一步逐圖實看。完成25/52，使用者核准pending，全部52課持續。


### WI-033 第五批24擴展故事preflight通過

八機制16PNG已原生審；其餘24故事的任務/部署/比較preflight通過，即將完成具體SVG場景並渲染48PNG，未產出/審查/整合。PatchCore兩手機深讀候選已產出尚未實看。比較保持同件孔位，容量/污染/全維投影/AE複製均為作者給定算例。完成25/52，使用者核准pending，全部52課持續；產物workitems/wi-033。


### WI-033 第五批其餘48工程PNG即將渲染

24故事preflight與具體SVG路由已完成，原型16PNG已審；即將render.py产出24故事48張PNG，尚未實看/整合。新增容量、污染、正則化、全維投影、AE複製/孔模糊與跨類驗證例，保持同件；PatchCore第二章2張手機已生成待審。完成25/52，使用者核准pending，全部52課持續。下一步逐張審查並整合第五批。產物workitems/wi-033。


### WI-033 第五批桌機審查補修

24擴展桌機及兩深讀手機已實看。RD4AD工程1訓練圖需無刮傷正常輸入；PatchCore features手機排除裁切半行標籤。兩份r02 preflight通過，即將渲染3PNG，未整合；擴展手機待看。完成25/52，全部52課持續，使用者核准pending。產物workitems/wi-033。


### WI-033 第五批66張選定PNG原生審查完成

64工程與2深讀手機逐張實看，自評92、完成度>=8；RD4AD正常訓練輸入與深讀殘字r02修正。原數值/桌機證據保留；即將整合8課工程與建置，頁內審查/32主頁及32深讀狀態/HTTP與回歸未跑。完成25/52，使用者核准pending，全部52課持續。產物batch5-{prototype,expanded,deep}-image-assessment.json與deep-active-assets。


### WI-033 第六批八機制preflight完成

第五批已建置1370資產958.7MB，32主頁/回歸執行中，深讀與頁內審尚未完成。第六批原主圖8張與CLIP共用手機2張已實看，原論文核對；八機制preflight通過。即將生成16PNG，尚未審或整合；24擴展與2共用手機待做。完成25/52，全部52課持續，使用者核准pending。產物workitems/wi-033。


### WI-033 第五批驗頁腳本相容性修正

8 tests/120 subtests通過123.73s。RD4AD/AE/DRAEM原首讀有4/5/4張，QA硬設3張而失敗；保留失敗報告並依topic實際張數比對，未改教材。即將補驗三課，放大總量依實際圖數計，不能沿用224。完成25/52；第六批八機制preflight通過，尚待渲染；全部52課持續。


### WI-033 最新：33/52課本機完成

第五批8課64工程PNG及PatchCore第二章2手機PNG已逐張原生與頁內實看。32主頁狀態240放大、32深讀狀態、8 tests/120 subtests、1370來源/docs資產一致與HTTP通過，見batch5-validation-summary.json。使用者核准pending，未發布，未新跑模型。第六批16原型PNG已生成，待審查修正及24擴展、2共用首讀手機；最後11課未完成。下一步逐張審第六批，全部52課持續；唯一checklist：workitems/wi-033/PLAN.md。


### WI-033 第六批16原型實看與修正

第五批完成，累計33/52。第六批r01逐張原生實看，發現兩窗尺寸矛盾/第二工件缺失/圖文重疊/長字溢出；r02八份preflight通過，即將渲染16PNG。尚未再審、擴展24故事或整合。使用者核准pending，全部52課持續。


### WI-033 第六批24擴展preflight完成

第六批r02原型渲染中，24擴展故事已定義並驗preflight；即將完成具體SVG場景，原型再審後生成。新增均為作者算例，保持原工件與時間身份；兩共用CLIP手機待做。完成33/52，使用者核准pending，全部52課繼續。


### WI-033 第六批原型完成原生審查

八課r02的16PNG逐張原生實看通過，自評92、完成度>=8，見batch6-prototype-image-assessment.json。24擴展preflight与SVG已完成，即將渲染48PNG，尚未審查或整合。2共用手機首讀待做；完成33/52，使用者核准pending，全部52課繼續。


### WI-033 第六批共用手機首讀preflight

兩共用手機原圖此前已實看，現以3節點重排正常q/刮傷p反例與三方法比較。兩preflight通過，即將渲染2PNG；24擴展48PNG另在生成，尚未審或整合。完成33/52，使用者核准pending；全部52課持續。


### WI-033 第六批擴展手機初審修正

24擴展手機及2共用首讀均已實看。發現WinCLIP零樣本誤標訓練、孔口圈填色掩孔、影片方件多L標記/位置、英文標題斷字，已修10故事與1共用手機r02 preflight。即將渲染20工程PNG和1主圖；其他桌機尚未審，整合與驗頁未做。完成33/52，使用者核准pending，全部52課繼續。


### WI-033 第六批66張選定PNG原生審查完成

64工程與2共用手機全部逐張實看，修正版重新審查通過；自評92，完成度>=8。即將整合八課與建置，頁面實看/32狀態/回歸/HTTP尚未跑。完成33/52；使用者核准pending，全部52課持續。證據batch6-expanded/main/prototype-image-assessment.json。


### WI-033 ??????????

????????????????768?2400???????????????????HTML/docs????????33/52????????????????????????/??????????????pending???52????


### WI-033 第七批11課機制preflight

第六批來源/docs建置成功1370資產，32狀態與8回歸正在跑；頁內實看未完，完成仍33/52。第七批11課原主圖已實看、原論文/官方TF-IDG梯度程式核對；11機制preflight通過，即將建立SVG並渲染22PNG，尚未審/整合。SR反例需同矩形板，V-JEPA頁內圖說間距待驗；33擴展故事未做。全部52課持續，使用者核准pending。


### WI-033 最新：41/52課本機完成

第六批8課64工程PNG及2共用首讀手機已原生/頁內逐張實看。32頁狀態224放大、8 tests/120 subtests、1370來源/docs資產一致、236HTTP及額外首讀來源核對通過。建置已納入768×2400原生尺寸。使用者核准pending，未發布，未新跑模型。最後11課的22機制PNG已生成，尚未審/修正；33擴展與SR同件主反例待做。下一步審第七批原型並完成剩餘全部課程與全站驗證；唯一checklist：workitems/wi-033/PLAN.md。


### WI-033 第七批22原型實看與修正

11課桌機/手機22PNG已逐張實看。7課需修正狀態語意、孔位/污點身份或圖說間距，r02 preflight通過；即將渲染14修正版，尚未再審。其餘4課原型原生通過。33擴展、SR主反例與整合驗頁未完成；完成仍41/52。產物batch7-prototype-r01-review與r02-preflight-validation。全部52課持續，使用者核准pending。


### WI-033 第七批機制原生審查完成

11課選定22PNG逐張原生實看，7課r02修正重審；逐圖自評92、完成度>=8且無否決項，證據batch7-prototype-image-assessment.json。即將定義33擴展故事與SR同件主反例，尚未渲染／整合或驗頁。完成仍41/52；使用者核准pending，全部52課持續。


### WI-033 第七批33擴展故事preflight

22機制原型原生審查已通過。33擴展preflight完成，保持各課原工件/影片身份，數值為作者算例；即將實作SVG並渲染66PNG，尚未生成或審查。SR同件主反例另待做，整合與頁面驗證未跑。完成41/52，使用者核准pending；全部52課持續。


### WI-033 SR同件主反例preflight

原主反例圓板右下邊與核心矩形板不一致，現固定矩形大左小右孔與左孔q；兩可能邊界不假稱精確同降採樣。preflight通過，即將生成2PNG，尚未審/整合。33擴展66PNG生成中。完成41/52，使用者核准pending，全部52課持續。


### WI-033 第七批擴展初審與SR修正

33擴展66PNG已生成；前5課的15故事30PNG原生實看，時間軸標籤需分別定位，VideoMAE平均例將明寫平方差。其餘18故事36PNG未看。SR主反例2PNG實看見局部孔超裁切框，r02 preflight通過，即將渲染2PNG。正式引用未改；完成41/52。使用者核准pending，全部52課持續。


### WI-033 第七批66擴展與SR原生實看

33擴展桌機/手機66PNG全部逐張實看，8故事需修时间刻度、平方差名詞、噪聲驗證/同板反例或文字跨影像；r02 preflight通過，即將渲染16PNG，尚未再審。SR同件主反例r02兩PNG已實看通過，尚未接入。完成41/52；工程整合/44頁狀態/回歸/全站驗證未跑。全部52課持續，使用者核准pending。


### WI-033 第七批90張選定PNG原生審查完成

88工程PNG與2張SR同板主反例均已逐張原生實看，16張修正版亦重新審查；自評92、完成度>=8、無否決項。證據batch7-prototype/expanded/main-image-assessment.json。即將整合11課並建置，44頁狀態、頁內實看、回歸與全站驗證尚未跑。完成仍41/52，使用者核准pending，未發布；全部52課持續。


### WI-033 第七批頁內審查checkpoint

11課88工程PNG與2張SR主反例已整合並建置，1370資產。8 tests/120 subtests通過（114.91秒）；44頁狀態QA持續。已逐張頁內實看3課24工程截圖，名單及hash見batch7-page-view-ledger.json；V-JEPA三首讀手機圖說間距另實看通過。尚未完成其餘頁內/全站驗證與收尾，不增加41/52完成數。使用者核准pending，未發布，全部52課持續。


### WI-033 第七批頁內審查checkpoint

11課88工程PNG與2張SR主反例已整合並建置，1370資產。8 tests/120 subtests通過（114.91秒）；44頁狀態QA持續。已逐張頁內實看5課40工程截圖，名單及hash見batch7-page-view-ledger.json；V-JEPA三首讀手機圖說間距另實看通過。尚未完成其餘頁內/全站驗證與收尾，不增加41/52完成數。使用者核准pending，未發布，全部52課持續。


### WI-033 第七批頁內審查checkpoint

11課88工程PNG與2張SR主反例已整合並建置，1370資產。8 tests/120 subtests通過（114.91秒）；44頁狀態QA持續。已逐張頁內實看7課56工程截圖，名單及hash見batch7-page-view-ledger.json；V-JEPA三首讀手機圖說間距另實看通過。尚未完成其餘頁內/全站驗證與收尾，不增加41/52完成數。使用者核准pending，未發布，全部52課持續。


### WI-033 第七批頁內審查checkpoint

11課88工程PNG與2張SR主反例已整合並建置，1370資產。8 tests/120 subtests通過（114.91秒）；44頁狀態QA持續。已逐張頁內實看9課72工程截圖，名單及hash見batch7-page-view-ledger.json；V-JEPA三首讀手機圖說間距另實看通過。尚未完成其餘頁內/全站驗證與收尾，不增加41/52完成數。使用者核准pending，未發布，全部52課持續。


### WI-033 第七批頁內審查checkpoint

11課88工程PNG與2張SR主反例已整合並建置，1370資產。8 tests/120 subtests通過（114.91秒）；44頁狀態QA持續。已逐張頁內實看11課88工程截圖，名單及hash見batch7-page-view-ledger.json；V-JEPA三首讀手機圖說間距另實看通過。尚未完成其餘頁內/全站驗證與收尾，不增加41/52完成數。使用者核准pending，未發布，全部52課持續。


### WI-033 最新：52/52課本機修正完成，總驗證收尾中

第七批88工程PNG與2張SR主反例均逐張原生及頁內實看；V-JEPA圖說另驗。44頁狀態308放大320HTTP、1370資產hash一致；8+16 tests、120+10 subtests及58課178圖說通過。52課均完成本機實作與逐課驗證；全52最新HTTP/資產重核、總報告與維護副本尚未完成。使用者核准pending，未發布，未新跑模型。下一步完成PLAN最後一項後交付。


### WI-033 全52課驗證與報告已完成，維護副本收尾

52/52本機完成，最終1506HTTP/1370資產hash、24 tests/130 subtests、58課178圖說通過。累計208主頁1472放大與160深讀狀態，既有頁面證據按已審hash重核。REPORT.md及final-selected-assets.json完成，學習已回写兩指南及共用log；即將保存維護副本並核對manifest。使用者核准pending，未發布；無教材待修。


## WI-033 最終完成：第二部分52/52課（2026-09-12）

- 狀態：本機實作、逐圖／逐課審查、必要驗證、學習與維護副本完成；實作待辦0。使用者成品核准pending，未commit／push／發布，沒有新增模型推論。
- 成果：52課208组工程故事（416桌機／手機PNG）及指定主圖／深讀修正，共460張新啟用PNG；逐圖自評91–93，五項完成度>=8、無否決項。第一部分6課教材資料未改。
- 證據：workitems/wi-033/REPORT.md、final-selected-assets.json、verification-all52.json、final-verification.json、maintenance-verification.json；相對於teaching-images/vision-ai-model-selection。
- 實際驗證：1370來源/docs資產一致、最終1506HTTP與兩HTML入口hash一致；累計208主頁1472放大、160深讀，最後44主頁在最終HTML重拍。最終24 tests/130 subtests、58課178手機圖說及git diff --check通過；未宣稱所有歷史套件通過。
- 接續：唯一checklist在workitems/wi-033/PLAN.md，已全勾選。本輪授權範圍無未完成項及阻礙；後續依使用者成品回饋或發布指示另續。以下較早checkpoint保留作歷史，不代表仍待製作。


## WI-033 Git提交／推送授權（2026-09-12）

使用者明確要求「Git check in push」。52課本機成果及驗證已完成；已fetch，main與origin/main無領先或落後。即將提交docs網站包及teaching-maintenance維護副本，再push origin main；沒有force push。沿用最終24 tests/130 subtests與1506HTTP驗證，教材內容未再修改。成品核准仍pending，Git推送與網站部署狀態分開。

- [ ] 提交已驗證成果，核對暫存範圍與差異。
- [ ] Push後核對遠端HEAD與本機一致，保存實際提交SHA。

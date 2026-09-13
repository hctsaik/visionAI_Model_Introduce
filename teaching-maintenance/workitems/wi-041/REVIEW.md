# WI-041 全站定版前 Multi Agent 審查

日期：2026-09-13。三位獨立 Agent 分別負責內容、桌面手機介面、PoC與資料可靠性；主 Agent 負責公開資產、技術反證及最終裁決。現行公開版本 `2c4cb73`，HTML hash `43c3557afba4300ad67425bdaba432e0a3582a14e227af0144711db1c0e75e28`。

狀態：三路獨立審查及主Agent反證已完成。六課修正尚未實作；本輪只審查與記錄，使用者成品核准pending。

## 定版建議

建議完成六課有限文字收尾後再定版。現有證據不支持全站重畫、增加大量章節或改造需求助手。已確認問題主要在展開工程參考，正確的預設主線仍存在；目前使用不必停止，但不能在已知矛盾存在時宣稱內容完全定稿。

### 定版前修正

| 項目 | 可重現問題與影響 | 有限修正／驗收 |
|---|---|---|
| DiffusionAD | `#view=lesson&lesson=ad-diffad&slide=1` 展開工程參考第2步写「一次 forward」，與預設主線兩噪聲尺度相矛盾。作者程式在兩尺度各呼叫去噪模型，不能用單次呼叫概括完整恢復與定位成本。 | 改為兩尺度各做單步估計，交代後續定位；同步核對圖說、操作卡與相關來源。主 Agent 已在公開頁重現，詳 `recheck-finding-ad-diffad.png`、`recheck-findings.json`。 |
| 五課六處標題／正文錯位 | U-Net第1步；YOLO-Seg第1、2步；EfficientAD第1步；ConvLSTM第2步；VideoMAE第2步。標題提到標註、訓練或狀態更新，段落卻講推論、限制或部署。 | 將每步標題、機制、原因重新對齊；不需因此重畫。主 Agent已在六課公開頁實際展開並查看截圖；逐處原文與源欄位見 `recheck-content-review.md`。 |

技術反證來源：[作者 DiffusionAD DDPM.py](https://github.com/HuiZhang0812/DiffusionAD/blob/main/models/DDPM.py)，`norm_guided_one_step_denoising_eval` 對 `normal_t/noisier_t` 各呼叫 `calc_loss`，其內各呼叫 `model`。來源快照與雜湊保存在本 workitem，未執行模型推論。

### 維護收尾

舊 `tools/verify_interactive_learning_html.py` 本輪實跑仍失敗，原因是要求新版已不使用的「帶入晶圓 AOI 範例」UI文字。這是驗證入口未跟上現行介面，不能解讀為使用者流程壞掉，也不能宣稱全套測試已通過。若要一併凍結維護版，建議將它對齊現行需求流程，保留真正的行為檢查；不要只刪除失敗斷言。證據 `recheck-legacy-verifier.txt`。本次失敗發生在歷史 ChArUco schema 檢查之前，不能照抄舊錯誤當新驗證結果。

### 留下一版

1. 挑少量較容易從警語猜答案的時序自測，改成兩個都合理的方案，讓讀者依節拍、資料與風險做取捨；不必全課加題。
2. PoC增加一個完整交接範例，示範資料批次、現行基準、允收門檻及人工接手。現行已有選填交接欄與待確認條件，因此不列為缺功能。
3. 依真實讀者回饋，再精簡深讀區英文術語與重複設定說明；沒有證據支持定版前全量改写。

## 實際覆蓋

- **內容：**58課逐課讀頁首工作摘要、主圖標題／圖說／callouts、機制步驟、比較、選型、首讀自測與遷移題。58課實際預設／展開DOM字段核對零缺漏；`recheck-content-coverage.md/.json`、`recheck-rendered-content.json`。
- **PoC：**新跑15項規則、6項備份保護、13項流程測試全通過；追加未確認選擇保存、未blur交接立即匯出、主題往返、舊分支答案不污染新結果亦通過。第一次本機8000服務中斷已保留失敗，以獨立8014重跑反證；`recheck-reliability-attempt2-evidence.json`、`recheck-poc-review.md`。
- **公開成品：**本機HEAD與遠端一致、公開HTML與course/docs一致；1440/390公開首頁到需求→方法→計畫及錯檔拒絕、原稿保留通過；`recheck-public-verification.json`。
- **引用資產：**1370項來源/docs hash一致、全部公開HTTP可達，含SVG依賴及必要Markdown文件；`recheck-asset-audit.json`。
- **來源連結：**135個來源字串拆成134個獨立URL；122個GET通過，11個OpenCV403與1個ECVA TLS問題改用web工具全部可讀。58課實際DOM共35個唯一外部href，沒有拼接異常。`recheck-source-links.json`、`recheck-source-fallback.md`、`recheck-external-rendered-anchors.json`。
- **其他驗證：**navigation/bundle共5 tests＋116 subtests通過。不是全repository歷史測試全綠。
- **瀏覽器廣度：**1440/390各58課、各232張投影片路由、各12個共用路由（共116課頁狀態、464投影片路由、24共用路由）。獨立磁碟瀏覽器1228次img解碼全通過；初次8000伺服器污染的載圖失敗保留，不改標通過。穩定HTTP PatchCore與公開成品另核對；`recheck-coverage-1440.json`、`recheck-coverage-390.json`、`recheck-file-image-decode.json`。
- **證據整合：**主Agent `recheck-root-summary.py` 重新核對58個不同課程／每寬度、source/docs/public hash、1228解碼及35個實際外部href均涵蓋在來源清單，全部斷言通過；`recheck-root-summary.json`。代表圖實看及手機額外交互以瀏覽器最終報告為準。
- **實看與額外交互：**瀏覽器Agent實看七家族桌面／手機代表首圖或放大圖及共同頁面，詳 `recheck-browser-review.md`。主Agent最後獨立在公開390px頁驗證搜尋PatchCore、選單開關、主題重整保存、圖題位於header下、放大圖四邊可達及Escape關閉，無JS錯誤；`recheck-public-mobile-ui.json`與兩張公開截圖，均實看。首次root探測誤等整頁未捲到的lazy圖而逾時，改成目前圖槽的有界載入檢查後通過，屬測試選擇範圍錯誤，不是產品修正。

## 判定界線

本輪全站審查有全58課文字／路由的廣度，並分開記錄代表圖像實看；沒有對全部319張圖及所有深讀章節逐字逐像素重評，不宣稱全站每圖 >90。沒有真人學習、現場模型準確度、相機量測精度或多裝置效能實測。

審查與修正分開：本輪只新增審查證據與Markdown，教材及公開站未修改，未提交或發布新版本；六課修正尚未實作。使用者成品核准 pending。

# WI-041 全站文字獨立重查（2026-09-13）

狀態：全 58 課主線、頁首工作摘要、機制步驟、比較選型、首讀自測與遷移題重新閱讀完成；產品未修改。這是內容一致性審查，不是逐圖評分，也不是使用者核准。來源以本輪 `docs/index.html` 中實際編譯 `course-data` 為準，再回查維護 JSON 與 renderer。舊 `content-coverage.json` 的 pending 保留，不拿旧檔當完成證據。

## 結論

不建議再做全站重畫或加章。現行主線普遍能說明工作問題、機制、輸出責任、反例與有條件選型；資料需求、未知品、真實量測與示意證據界線也已有交代。值得在定版前收尾的是 **DiffusionAD 一處技術語意矛盾**，以及 **五課六個展開步驟的標題／內文错位**。後者不推翻正確主線，前者會影響讀者理解單步設計與完整成本。

## C1：DiffusionAD 的「單步」被展開參考寫成一次 forward

- 建議優先級：定版前修正。範圍小，不需重畫。不是阻止網站目前使用的功能故障。
- 路由：`#view=lesson&lesson=ad-diffad&slide=1` →「工程參考：展開文字因果鏈與設定核對點」→ 第 2 步。
- 維護來源：`_course_content/topics/ad-diffad.json`，`mechanism_steps[1].title`（約第 38 行）及 `.body`。
- 現文標題「測試圖一次 forward 得到 restoration」，內文仍將 test ROI 經 one-step denoiser 簡化成一條恢復。
- 相反，新主線 `beginner_path.visuals[0].caption` 明說同圖的高／低兩種噪聲尺度，且「每個尺度用單步估計，不代表整套只呼叫一次網路」。此限定應同步到展開步驟。
- 第一手核對：[作者程式 DDPM.py](https://github.com/HuiZhang0812/DiffusionAD/blob/main/models/DDPM.py)，`norm_guided_one_step_denoising_eval` 對 `normal_t` 和 `noisier_t` 各呼叫一次 `calc_loss`；`calc_loss` 內呼叫 `model(x_t, t)`。 [eval.py](https://github.com/HuiZhang0812/DiffusionAD/blob/main/eval.py) 在此恢復後另呼叫分割模型。故不能用「一次 forward」概括整套。
- 建議改意：標題「兩個噪聲尺度各做單步估計」；正文交代高噪聲正常估計引導低噪聲恢復，之後原圖／恢復交定位網路。保留每尺度單步與全流程成本之別。
- 驗收：主線、展開因果鏈、相關操作卡和 model.md 的限定一致；瀏覽器實際展開核對，不能只改未使用欄位。

## C2：五課六處展開步驟仍是標題與段落配錯

建議優先級：與 C1 同批有限文字收尾。以下都在正確主線後的收合工程因果鏈，不能稱整課機制缺失；但該區宣稱逐步核對，標題應回答其內文。

| 課／來源 `_course_content/topics/` | 欄位（零起算） | 實際錯位 | 最小修正方向 |
|---|---|---|---|
| `u-net.json` | `mechanism_steps[0]` | 標題「像素標註教任務」，正文講下採樣整合範圍、細節變粗 | 補像素標註如何提供監督，或改標題對應下採樣 |
| `yolo-seg.json` | `mechanism_steps[0]` | 標題「先有實例標註」，正文講共享原型與 A/B 係數 | 補逐件框／遮罩監督，將原型說明放下一步 |
| `yolo-seg.json` | `mechanism_steps[1]` | 標題「共享底圖，各自組合」，正文只有重疊漏檢與計數限制 | 說明每件係數組合共享原型、形成各件遮罩 |
| `ad-efficientad.json` | `mechanism_steps[0]` | 標題「正常資料教學生」，正文直接跳到教師／學生同看待測圖與速度 | 分清正常訓練如何更新學生，與固定權重的待測比較 |
| `convlstm.json` | `mechanism_steps[1]` | 標題「卷積更新狀態」，正文僅說原始論文是降雨、工業需編碼器和任務頭 | 補新輸入和舊狀態如何經卷積更新記憶 |
| `videomae.json` | `mechanism_steps[1]` | 標題「只編碼可見塊再重建」，正文只講部署時不需要重建解碼器 | 補訓練可見塊編碼及遮蔽像素重建，再交代部署切換 |

來源中的 `diagram` 如複製同一字段，修正時一併核對；不應只修改 diagram 而漏掉 renderer 真正用的 `.title/.body`。

## 可延後的教學改善

- 時序課的首讀題，例如 RAFT「一定要選 RAFT 嗎」、ByteTrack「降低門檻能保證 ID 嗎」，答案較容易從警語猜出。保留作基本誤解題合理；下一版若有真人回饋，可將其中一題改成兩個都可行方案並給節拍／資料條件，要求取捨。不是每課都要加題。
- 一些工程比較表仍用較多英語術語。新版主線比較已有清楚中文且預設可見，這屬深讀負擔；不因此推翻新版主線，也不建議為定版臨時全量改寫。
- 缺乏真人學習測試與共同模型效能實測仍是證據限制。現行頁面多數已誠實標示示意，不能把這些限制自動視為新增阻礙或要求全面訓練模型。

## 覆蓋與限制

- 58 課逐課人工閱讀的字段：`learnerBrief` 工作／交付／第一步，`beginner_path` 各主圖標題、caption、callouts，全部 `mechanism_steps` 標題／正文，`comparison`、`selection`、`micro_example`、`transfer_check`。另讀 renderer `beginnerVisualsHTML`、`teachingPrimerHTML`、`causalChainHTML` 與 `teachingSynthesisHTML`，核對真正顯示哪一份文字。
- 首讀 `micro_example` 可見、答案需展開；文字因果鏈和完整比較／POC 在收合參考。所有字段存在不等於所有字段預設可見。
- 每課 coverage 見 `recheck-content-coverage.md`；渲染文字證據見 `recheck-rendered-content.json`。已完成 58 rows、58 個不同預設文字；58 課首讀題及展開機制的字段/DOM比對皆成功，`recheck-content-coverage.json` 的 DOM mismatch 為 0。HTML SHA-256 為 `43c3557afba4300ad67425bdaba432e0a3582a14e227af0144711db1c0e75e28`。抽取脚本保留在同目錄。
- 本審查不宣稱 319 張圖或全部深讀章節逐像素／逐字重新檢查，未評圖像分數，未新增模型推論、未修改產品、未發布。桌面／手機互動与實際截圖由其他審查分工獨立提供，最後以主 Agent 反證裁決為準。

## 最終 checkpoint

- 已完成：上述人工字段重讀、58 課預設／展開 DOM 擷取、58 列 coverage；C1/C2 均在實際展開文字重現。主 Agent 已獨立重看公開 DiffusionAD／U-Net 截圖，並核實作者程式兩次 denoiser 呼叫。
- 外部來源：`recheck-external-rendered-anchors.json` 保存 58 課實際展開 DOM 的 35 個唯一外部 href；未發現多個 URL 拼接成單一 href，未重複做網路請求驗證。第一次抽取因 Playwright 呼叫把 arg 傳為位置參數而失敗，改成關鍵字參數重跑後 58/58 完成；這是審查腳本錯誤，非產品錯誤。
- 官方來源快照：`recheck-diffusionad-official-DDPM.py`，URL 與 SHA-256 見 `recheck-diffusionad-source.json`。只做只讀來源核對，沒有執行作者模型。
- 未完成／下一步：C1/C2 尚未實作；交主 Agent 統合其他審查與定版建議。沒有產品改動、沒有測試新增、沒有 Git 或發布动作；使用者核准 pending。

# WI-039：現行教材語意獨立審查

日期：2026-09-13。範圍為審查，不修改教材、圖片、生成器或 Git。採用 teaching-review-cycle 的證據分層；沒有給未實看圖像評分，也不以過往通過測試代替語意核對。

## 基準與結論

審查 `docs/index.html` 的實際 `course-data`，SHA-256：`561617fdc2b77614a024b573857597a48632c5b51eba910d536e6dc11652c8f3`。嵌入 JSON 在 HTML 第 747 行，因此以下用 topic ID 與 JSON 欄位精確定位，不以未使用的原始欄位當證據。主 Agent 已回報公開站雜湊相符；本子審查沒有另外取得公開 HTML 雜湊。

結論：抽查的新版主線比舊文字參考更一致；但尚不適合宣稱所有教材文字已定版。建議先修下列兩項 P1，第三項是可安排的文案清理。這不表示需要重畫全部教材。

## 1. P1／定版前修：AnomalyGPT 的「模型專屬因果鏈」仍混入應用治理流程

位置：`topics[id=ad-anomalygpt].teachingStory.mechanism_steps[1..3]`，`docs/index.html:747`。

- 第二步內文：`test ROI 和宣告的 specialist evidence 經固定 preprocessing、visual tokens、learned prompt、bridge/LVLM，產生結構化文字候選與image-decoder region。`
- 第三步內文：`response schema 要求 evidence-region ID、observed/inferred分離、uncertainty/abstain、SOP/retrieval revision和next confirmation action。`
- 第四步是 grounding／owner／PASS、REVIEW、HOLD 的應用交接規則。

同課新版 `slides[1].plain.relation` 卻明確解釋內建定位支路，並寫「不把任意外部檢測器當必要輸入」；`slides[2].plain.relation` 也寫「額外外部檢測器是應用整合選擇，不是原模型必需支路」。因此問題不是應用治理本身錯誤，而是未標明它是選用整合，卻放在「模型專屬因果鏈」內，足以让進階讀者誤讀原模型的輸入及原生交付。

技術校準：[作者官方專案頁](https://anomalygpt.github.io/) 說明以視覺文字特徵匹配的 image decoder 取得定位，再以 prompt learner 將相關語意接入 LLM；上述 SOP／retrieval schema 並不能由此視為原模型必備結構。這裡採用的是角色界線判斷，並非宣稱應用不能另接外部檢測器。

建議：機制區按「影像表示 → 內建定位 → 提示 → 問答」重述，將 evidence schema／SOP／owner 另標為應用端選填整合。驗收需同時看新版主線與展開因果鏈，兩處對必需輸入的說法一致。

## 2. P1／定版前修：ConvNeXt 與 V-JEPA 的文字機制仍有組裝錯位

位置：兩課 `teachingStory.mechanism_steps[0..1]`，`docs/index.html:747`。

| 課程／步驟 | 標題 | 實際內文重點 | 問題 |
|---|---|---|---|
| ConvNeXt／1 | 有標註的工件 | `depthwise操作逐通道看鄰域，後續點式操作混合通道` | 講的是第二步「空間與通道分工」，不是資料／輸入準備。 |
| ConvNeXt／2 | 空間與通道分工 | `不代表每種尺寸和硬體都更快。比較同解析度、批量及完整前後處理。` | 重點變成成本比較，未在本步解釋分工。 |
| V-JEPA／1 | 可見影片內容 | `目標編碼器的權重隨上下文編碼器緩慢更新` | 跳到目標更新，未說本步可見區如何進上下文編碼器。 |
| V-JEPA／2 | 預測特徵對齊目標 | `用有標註資料訓練任務頭，才產生夾取階段候選` | 已跳到下游任務，與訓練中的預測／目標比較不符。 |

這些句子未必各自技術錯誤，但順序會破壞因果閱讀。V-JEPA 新版 `slides[1].plain.relation` 已有可見 tokens、目標編碼器與同位置特徵比較的完整敘述，可作同頁一致性參考；不需重新發明機制。

建議：把每步的輸入、操作、輸出對回其標題；不要再按段落索引從 terms／summary 抽句。驗收由不看主圖的讀者逐步讀文字，仍能追蹤角色與順序。

## 3. P2／可安排清理：因果理由與設定核對欄仍大量顯示維護佔位文字

位置：多課 `mechanism_steps[*].why`、`.anchor`，`docs/index.html:747`；實际渲染位於 `tools/build_interactive_learning_html.py:2723` 附近。

全 58 課的 232 個機制步驟中，116 個 `why` 完全等於「由本課核心機制連接工作用途」，164 個 anchor 以 `WI` 開頭。實頁例如 ConvNeXt 顯示：

> 因為：由本課核心機制連接工作用途
>
> 設定核對：WI030-1

這不構成模型事實錯誤，但並未回答「因為什麼」，工單步驟 ID 也不是使用者能核對的設定。因果鏈前言又承諾「核對每一步要鎖定的設定與為什麼」，文字功能因此落空。

建議：確有教學用途的理由保留並具體化；沒有內容的理由可不顯示。WI 編號保留在來源追溯資料，實際設定欄填取像／骨幹／前處理／資料切分等與本步相關條件。此項可在兩個 P1 之後處理，不需因此宣稱全課核心原理失效。

同屬文案清理、較低優先的校對例子：新版主線仍有明確簡體殘字。

位置：`topics[id=dinov2].slides[3].prompt` 為「DINOv2：外观差異不等於不良」；`topics[id=ad-anomalygpt].slides[0].plain.takeaway` 為「合成影像、遮罩與文字要描述同一處异常。」均在 `docs/index.html:747`。

`观`、`异` 不是繁體；應校正為「觀」「異」。這與先前評論把「範圍／採樣」等原本就正確的繁體字列成錯誤不同。本輪只列明確例子，不宣稱已逐字校對全站；也不建議把模型名、程式碼與引用全文盲目轉換。

## 已確認保留的修正

- DINO 的真值／正負去噪／影像初始化三步已分開；slide 3 標籤也已變為「訓練時如何學會區分」。不再重報 WI-034 的舊錯位。
- YOLOE 第四步 why 已回到範例背景、取像與邊界核對，沒有旧版突兀的 LRPC 答句。
- ResNet 殘差步驟已對回兩路相加；DINOv2 首步不再放整段情境 summary。
- 對全部 58 課做精確字串比對，`summary == mechanism_steps[0].body` 為 0；這只證明該重複模式消失，不證明所有首步語意均正確。
- 抽查的 PatchCore、DINOv2、ControlNet、DefectFill、TF-IDG 等仍清楚區分特徵／候選／生成資料與品質真值；未發現需要撤回整套教學方向的證據。

## 實際檢查與限制

七家族分層抽查共 18 課的機制標題及內文：geometry：ECC；classification：ResNet、ConvNeXt、ViT、Keypoint R-CNN、Pose；detector：DINO、YOLOE；anomaly：PatchCore、WinCLIP、AnomalyGPT；video：ByteTrack、V-JEPA；foundation：DINOv2、DINOv3；diffusion：ControlNet、DefectFill、TF-IDG。對相關疑點另讀編譯後 slides 的 plain 欄位、選型文字與自測；不是宣稱 58 課逐字全審。

核對 renderer：`causalChainHTML` 使用實際 `mechanism_steps.title/body/why/anchor`，`legacyCausalReferenceHTML` 將它置於 details；`teachingPrimerHTML` 也確實使用 `micro_example`，不是其他未渲染的同名假設欄位。

以 Playwright／Edge 讀取本機 `/docs/index.html#view=lesson&lesson=<id>&slide=4`，對 ConvNeXt、V-JEPA、AnomalyGPT、DINOv2 四課確認 `.causal-chain` 預設不可見，展開後 `.inner_text()` 出現上述實際文字。因此 P1 主要位於展開參考區，不應描述成預設主圖全部錯誤。

未執行：模型推論、全站逐圖新評分、手機視覺審查、真人學習試驗、對未抽查課程逐句技術查證。沒有改產品檔、沒有提交或發布。

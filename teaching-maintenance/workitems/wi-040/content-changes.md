# WI-040 三課文字機制修正

日期：2026-09-13。承接 WI-039 的兩項內容 P1；本子任務只修改三個主題 JSON 的 `mechanism_steps`，沒有執行 build、Git 或發布。

## 實際改動

| 來源 | 四步順序 | 修正目的 |
|---|---|---|
| `_course_content/topics/convnext.json` | 工件影像與類別準備 → 空間與通道分工 → 分類交付 → 品質及成本驗證 | 第一段回到輸入／類別，depthwise 與通道混合回到第二步，效能比較移至驗證；不把新架構當效能保證。 |
| `_course_content/topics/v-jepa.json` | 可見影片 → 同位置目標特徵 → 工作任務頭 → 獨立影片驗證 | 分清 2024 原版預訓練與下游；可見區進上下文編碼器，完整影片進目標編碼器，訓練比較特徵，動作類別另由任務頭學習。 |
| `_course_content/topics/ad-anomalygpt.json` | 成對訓練資料 → 內建定位 → 位置提示與回答 → 應用端核對 | 去除把外部 specialist evidence／SOP schema 寫成原模型必備機制的誤導；明列外部檢測器、SOP 檢索及結構化欄位屬應用整合。 |

每一步都同步修改 `title`、`body`、`why`、`anchor` 及 `diagram` 的同名鏡像欄位。這三課的理由已具體說明因果；設定核對已改為可核對的資料／模型／處理條件，沒有繼續顯示 WI 工單編號。圖片、首讀路徑、工程 slides、練習及其他頂層欄位全部保持原值。

技術依據沿用同課已核對的 `mental_model`／新版工程 slides，以及 WI-039 記錄的 [AnomalyGPT 作者說明](https://anomalygpt.github.io/)；未新增模型效能數字或宣稱實測。

## 已執行驗證

- 三個來源 JSON 均重新解析成功。
- 每課仍為四個機制步驟；每步四個文字欄位與 diagram 鏡像完全相同。
- 寫入前後逐一比較所有非 `mechanism_steps` 頂層欄位，均完全相同；因此沒有改動圖片引用、首讀路徑或工程 slides。
- 語意核對：ConvNeXt 首步交代影像／標籤，第二步交代運算分工；V-JEPA 前兩步留在預訓練、第三步才進任務頭；AnomalyGPT 明示內建位置圖與應用端選用整合的角色不同。

來源寫入後 SHA-256：

| Topic | SHA-256 |
|---|---|
| convnext | `8193af7e1d00ae5609f191a2860b7b01b4d83dd20567d12ee4b791129bc17d82` |
| v-jepa | `f762fef4be5a3f9c8bb8cfb913d9bce6c979e03d89dc52df3df80794c943145d` |
| ad-anomalygpt | `fe8d7dab1c0baa554369f814d4f3a5ca2de93b3fefe95492544685dad9cbcf65` |

## 待整合驗證

主 Agent 接續構建後，需核對 course 與 docs 編譯資料是否包含以上機制句、三課實頁展開因果鏈是否顯示同一版本，並跑必要回歸。這份來源驗證不代表公開版已更新，也不代表圖片新評分或使用者已認可。

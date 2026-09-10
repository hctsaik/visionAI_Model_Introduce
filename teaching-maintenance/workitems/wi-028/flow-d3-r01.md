# WI-028 少量追點，還是整張位移？ r01
- lesson objective: 只需少量穩定點可先追點，需要全圖位移再比較稠密光流。
- page type: D — 依解釋或對照責任選擇。
- primary reading path: 具體影片問題 → 方法與參考 → 可見結果及限制 → 工作接手。
- major visual nodes:
  1. 共同兩幀輸入
  2. Lucas–Kanade稀疏追點
  3. RAFT稠密位移
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，沿用金屬主體、淡細框及就近對應，不搬頁碼或原文案。
- pale-yellow takeaway: #FFF4CC：只需少量穩定點可先追點，需要全圖位移再比較稠密光流。
- source: https://docs.opencv.org/4.x/d4/dee/tutorial_optical_flow.html ; https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123470392.pdf
- evidence: AI生成教學示意，非模型推論或性能比較。
- generation: built-in imagegen；desktop16:9、mobile獨立上下重排；actual PNG review pending；user approval pending。
- learning applied: WI-027來源／特徵分清，WI-029排除舊圖文字污染，WI-028時刻／位置／輸出責任核對。

## 逐圖因果 brief 與逐字必要標籤
第一區同L刻痕銀板兩幀小幅右移，分支分別進第二第三區，兩方法之間無箭頭。第二區「Lucas–Kanade」同銀板只有三個角點右向箭頭，其他區空白；準備小卡「選角點／窗口」，短句「少量位置的移動」。第三區「RAFT」相同銀板全圖格点箭頭，物件右向、背景零位移小點，準備卡「預訓練權重／運算預算」，短句「每個像素的位移估計」。底下共同待測清單「對應錯誤、耗時、記憶體」不補假數字。兩圖同大小同場景同位移，不以色彩比較準確率。

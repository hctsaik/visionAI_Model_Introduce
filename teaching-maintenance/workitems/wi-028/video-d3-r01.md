# WI-028 記住序列、補像素、預測特徵：學習方式不同 r01
- lesson objective: 先對齊工作任務，再比較訓練資料、輸出與維護成本。
- page type: D — 依解釋或對照責任選擇。
- primary reading path: 具體影片問題 → 方法與參考 → 可見結果及限制 → 工作接手。
- major visual nodes:
  1. ConvLSTM的狀態更新
  2. VideoMAE的像素重建
  3. V-JEPA的特徵預測
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，沿用金屬主體、淡細框及就近對應，不搬頁碼或原文案。
- pale-yellow takeaway: #FFF4CC：先對齊工作任務，再比較訓練資料、輸出與維護成本。
- source: https://arxiv.org/abs/1506.04214 ; https://arxiv.org/abs/2203.12602 ; https://arxiv.org/abs/2404.08471
- evidence: AI生成教學示意，非模型推論或性能比較。
- generation: built-in imagegen；desktop16:9、mobile獨立上下重排；actual PNG review pending；user approval pending。
- learning applied: WI-027來源／特徵分清，WI-029排除舊圖文字污染，WI-028時刻／位置／輸出責任核對。

## 逐圖因果 brief 與逐字必要標籤
三個主要獨立對照區，同銀色夾爪動作片段，區間無串接箭頭。第一區「ConvLSTM」連續小影片到沿時間相連的抽象空間記憶格，標「新影格＋舊狀態」「依任務訓練」。第二區「VideoMAE」遮蔽影片塊到重建像素圖片，原始像素作目標，標「預訓練：補像素」。第三區「V-JEPA」遮蔽影片塊到抽象向量，與目標編碼器向量對照，絕不能畫輸出重建照片，標「預訓練：預測特徵」。每區最下以小的任務頭方塊標「工作輸出另接任務頭」；這是學習責任比較不是三個互換的現成模型。共同短註「固定影片／取樣／標註與測試」，不列假性能。

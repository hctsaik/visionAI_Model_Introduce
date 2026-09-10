# WI-028 框出工件，和認出同一段軌跡，是兩件事 r01
- lesson objective: 需要跨幀計數時，先有可靠偵測，再驗證身分關聯。
- page type: D — 依解釋或對照責任選擇。
- primary reading path: 具體影片問題 → 方法與參考 → 可見結果及限制 → 工作接手。
- major visual nodes:
  1. 同一段輸送帶影片
  2. 逐幀偵測只找框
  3. 偵測加ByteTrack接軌跡
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，沿用金屬主體、淡細框及就近對應，不搬頁碼或原文案。
- pale-yellow takeaway: #FFF4CC：需要跨幀計數時，先有可靠偵測，再驗證身分關聯。
- source: https://arxiv.org/abs/2110.06864
- evidence: AI生成教學示意，非模型推論或性能比較。
- generation: built-in imagegen；desktop16:9、mobile獨立上下重排；actual PNG review pending；user approval pending。
- learning applied: WI-027來源／特徵分清，WI-029排除舊圖文字污染，WI-028時刻／位置／輸出責任核對。

## 逐圖因果 brief 與逐字必要標籤
三區同銀色L板穿越一條垂直計數線。第一區三影格左→中→右，共同输入分支。第二區「只有逐幀偵測」三幀各有一框但無ID、無連線，標「每張都找到框」「尚未知道是同一件」；不要把框數3當物件數3結論。第三區「偵測＋ByteTrack」相同三幀框加ID7和一條軌跡，計數線旁標「跨線事件另計」。附短標「遮擋後會不會換ID？」，應用計數不是追蹤器原生輸出，不能畫成偵測不用於追蹤。

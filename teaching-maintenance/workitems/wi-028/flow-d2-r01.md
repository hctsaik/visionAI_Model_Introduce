# WI-028 沒有可靠對應，位移圖也可能猜錯 r01
- lesson objective: 先看對應是否可信，再把位移交給後續量測。
- page type: D — 依解釋或對照責任選擇。
- primary reading path: 具體影片問題 → 方法與參考 → 可見結果及限制 → 工作接手。
- major visual nodes:
  1. 紋理可見的小位移
  2. 反光或遮擋失去對應
  3. 回查原片與可靠區
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，沿用金屬主體、淡細框及就近對應，不搬頁碼或原文案。
- pale-yellow takeaway: #FFF4CC：先看對應是否可信，再把位移交給後續量測。
- source: https://docs.opencv.org/4.x/d4/dee/tutorial_optical_flow.html ; https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123470392.pdf
- evidence: AI生成教學示意，非模型推論或性能比較。
- generation: built-in imagegen；desktop16:9、mobile獨立上下重排；actual PNG review pending；user approval pending。
- learning applied: WI-027來源／特徵分清，WI-029排除舊圖文字污染，WI-028時刻／位置／輸出責任核對。

## 逐圖因果 brief 與逐字必要標籤
三區固定相機同一帶L刻痕金屬片向右小移。第一區「角點看得清楚」：前後局部L角均清楚，蓝色小右箭頭能對應。第二區「反光蓋住刻痕」：後一影格同角位置強高光白塊，看不到L；另一局部被實體遮擋條蓋住，兩者不能畫出已知真實对应，橘虛線問號箭頭表示估計。第三區「只用可信線索」：原片覆蓋藍色可信點位移與橘色不可靠區；短句「LK：追丟點重找」「RAFT：遮擋區仍是估計」「量測另需校正」。不存在用平滑漂亮光流保證真值。

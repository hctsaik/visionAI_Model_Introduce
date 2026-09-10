# WI-028 RAFT：反覆查找對應，估計整張位移 r01
- lesson objective: 光流是像素位移估計，遮擋與反光仍要另查。
- page type: C — 依解釋或對照責任選擇。
- primary reading path: 具體影片問題 → 方法與參考 → 可見結果及限制 → 工作接手。
- major visual nodes:
  1. 兩張影格抽特徵
  2. 查詢全配對線索並更新
  3. 交出稠密光流
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，沿用金屬主體、淡細框及就近對應，不搬頁碼或原文案。
- pale-yellow takeaway: #FFF4CC：光流是像素位移估計，遮擋與反光仍要另查。
- source: https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123470392.pdf
- evidence: AI生成教學示意，非模型推論或性能比較。
- generation: built-in imagegen；desktop16:9、mobile獨立上下重排；actual PNG review pending；user approval pending。
- learning applied: WI-027來源／特徵分清，WI-029排除舊圖文字污染，WI-028時刻／位置／輸出責任核對。

## 逐圖因果 brief 與逐字必要標籤
固定視角灰色輸送帶上一塊帶黑色L刻痕銀色板往右移。第一區「兩張影格」上下两图同板小幅右移，各自連到抽象藍色特徵格子，標「各自抽特徵」，特徵不是照片切片。第二區「查對應，再更新」：放大的來源格點連到候選位置相似度格，深淺藍小矩陣中兩個可能候選，短標「全配對線索」；下面初始短箭頭到更新後右向箭頭，中間自循環箭頭標「反覆查詢」，不要輸入影格循環倒退。第三區「稠密位移」：同板影格覆蓋規則格點，板上許多同向右箭頭、靜止帶上小圓點零移動，刻痕位置保持；右緣遮擋區用橘虛線標「遮擋：估計」，下方「回原片核對」。不畫追蹤ID、不宣稱精確速度、無虛構效能數字。

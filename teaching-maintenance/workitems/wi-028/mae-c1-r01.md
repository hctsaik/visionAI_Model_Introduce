# WI-028 VideoMAE：遮住影片，學會補回像素線索 r01
- lesson objective: 補像素是預訓練練習，工作判斷要另接任務頭。
- page type: C — 依解釋或對照責任選擇。
- primary reading path: 具體影片問題 → 方法與參考 → 可見結果及限制 → 工作接手。
- major visual nodes:
  1. 影片遮住大部分時空塊
  2. 只編碼可見塊再重建
  3. 影片特徵接任務頭
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，沿用金屬主體、淡細框及就近對應，不搬頁碼或原文案。
- pale-yellow takeaway: #FFF4CC：補像素是預訓練練習，工作判斷要另接任務頭。
- source: https://arxiv.org/abs/2203.12602
- evidence: AI生成教學示意，非模型推論或性能比較。
- generation: built-in imagegen；desktop16:9、mobile獨立上下重排；actual PNG review pending；user approval pending。
- learning applied: WI-027來源／特徵分清，WI-029排除舊圖文字污染，WI-028時刻／位置／輸出責任核對。

## 逐圖因果 brief 與逐字必要標籤
以固定相機拍同一銀色夾爪接近銀色方片的三時刻短片為題。第一區「遮住時空塊」：三影格同網格位置多數被淺灰遮罩覆蓋，跨影格同格被遮形成tube遮蔽，不把整段未來全遮；少量可見夾爪邊緣。第二區「用可見內容補像素」：少數可見藍token進編碼器，加入淺灰遮蔽token到解碼器，输出一張有格線的重建夾爪影像，橘虛框指遮蔽位置；原始未遮影格另用細虛線到重建比較點標「原始像素作訓練目標」，不可原圖直接餵可見編碼器；標「預訓練」。第三區「接工作任務」：完整新片段到編碼器抽象向量，再到另有動作標註訓練的分類頭，輸出「夾取階段候選」，不輸出mask或缺陷；短標「部署不用重建解碼器」。訓練與部署大區分明，無精度數字。

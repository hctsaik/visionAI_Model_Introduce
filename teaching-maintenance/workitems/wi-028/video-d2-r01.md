# WI-028 關鍵動作沒拍進去，影片特徵也不夠 r01
- lesson objective: 先讓關鍵動作進入輸入，再驗證影片模型的判斷。
- page type: D — 依解釋或對照責任選擇。
- primary reading path: 具體影片問題 → 方法與參考 → 可見結果及限制 → 工作接手。
- major visual nodes:
  1. 完整夾取片段
  2. 取樣漏掉短暫滑落
  3. 回看原片與調整時間窗
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，沿用金屬主體、淡細框及就近對應，不搬頁碼或原文案。
- pale-yellow takeaway: #FFF4CC：先讓關鍵動作進入輸入，再驗證影片模型的判斷。
- source: https://arxiv.org/abs/2203.12602 ; https://arxiv.org/abs/2404.08471
- evidence: AI生成教學示意，非模型推論或性能比較。
- generation: built-in imagegen；desktop16:9、mobile獨立上下重排；actual PNG review pending；user approval pending。
- learning applied: WI-027來源／特徵分清，WI-029排除舊圖文字污染，WI-028時刻／位置／輸出責任核對。

## 逐圖因果 brief 與逐字必要標籤
三區同工業夾爪與銀片。第一區「原始完整片段」四個小時刻：接近→提起→短暫滑落→再夾起；只在第三幀看到銀片滑離夾爪，橘圈標「短暫事件」。第二區「稀疏取樣」只選第一和第四時刻，缺中間事件，兩被選小圖必須對應第一區相同位置與姿態，標「輸入沒看見滑落」。第三區「調整取樣再測」時間線密一點，橘事件所在影格被納入，接「動作標註與測試」資料夾，不直接給模型成功結論。適用VideoMAE與V-JEPA下游，無生成未来画面、无分数。

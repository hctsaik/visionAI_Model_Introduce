# WI-028 ConvLSTM：把位置與時間一起留在記憶裡 r01
- lesson objective: 新影格與舊狀態一起更新，任務輸出仍需專門訓練。
- page type: C — 依解釋或對照責任選擇。
- primary reading path: 具體影片問題 → 方法與參考 → 可見結果及限制 → 工作接手。
- major visual nodes:
  1. 連續影格的空間線索
  2. 卷積更新狀態
  3. 任務頭判讀片段
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，沿用金屬主體、淡細框及就近對應，不搬頁碼或原文案。
- pale-yellow takeaway: #FFF4CC：新影格與舊狀態一起更新，任務輸出仍需專門訓練。
- source: https://arxiv.org/abs/1506.04214
- evidence: AI生成教學示意，非模型推論或性能比較。
- generation: built-in imagegen；desktop16:9、mobile獨立上下重排；actual PNG review pending；user approval pending。
- learning applied: WI-027來源／特徵分清，WI-029排除舊圖文字污染，WI-028時刻／位置／輸出責任核對。

## 逐圖因果 brief 與逐字必要標籤
工業教學改編：同一金屬夾爪在固定位置依序張開、接近银色方片、夾住；三個影格有清楚先後。第一區「連續影格」顯示上述三狀態，不把未來畫面當現在輸入。第二區「保留位置的記憶」：三個相同座標小格圖沿時間左至右（手機上下），每張影格向自己的格圖輸入，前一格狀態箭頭進下一格；當前夾爪兩側對應格區更新、無關區淡去，標「卷積更新」「保留／加入／忘掉」。格圖用抽象格塊不是縮小原照片，不能暗示機械結構自動記得。第三區「任務頭」：訓練資料夾標「有標註的動作片段」用虛線訓練箭頭連分類頭，下方部署狀態特徵實線流向同頭再到「夾取階段候選」，旁邊回看片段按鈕。標「工業應用示意」，原始單元非現成夾爪模型，不寫已證明夾緊或成功。

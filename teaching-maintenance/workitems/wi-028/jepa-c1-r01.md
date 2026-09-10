# WI-028 V-JEPA：預測被遮住部分的特徵 r01
- lesson objective: 預測的是特徵，不是重畫影片；任務判斷另行學習。
- page type: C — 依解釋或對照責任選擇。
- primary reading path: 具體影片問題 → 方法與參考 → 可見結果及限制 → 工作接手。
- major visual nodes:
  1. 可見影片內容
  2. 預測特徵對齊目標
  3. 特徵接工作任務
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，沿用金屬主體、淡細框及就近對應，不搬頁碼或原文案。
- pale-yellow takeaway: #FFF4CC：預測的是特徵，不是重畫影片；任務判斷另行學習。
- source: https://arxiv.org/abs/2404.08471
- evidence: AI生成教學示意，非模型推論或性能比較。
- generation: built-in imagegen；desktop16:9、mobile獨立上下重排；actual PNG review pending；user approval pending。
- learning applied: WI-027來源／特徵分清，WI-029排除舊圖文字污染，WI-028時刻／位置／輸出責任核對。

## 逐圖因果 brief 與逐字必要標籤
以2024原版V-JEPA，同一銀色夾爪接近銀色方片三時刻影片。第一區「只看可見部分」：三格影片各有灰色遮蔽塊，剩餘可見區進上下文編碼器，輸出抽象藍格。第二區「預測被遮區特徵」：上行可見特徵進預測器，輸出藍色特徵向量條；下行完整原影片進目標編碼器後只取同被遮位置，輸出綠框藍色向量條標「目標特徵」，兩向量用比較括號而非變成像素畫面，標「訓練時對齊」。目標編碼器用權重緩慢更新的小虛線表示可省，不能把目標特徵當人工真值、不能把完整影格餵預測器。第三區「部署接任務頭」：新影片到已學編碼器到抽象影片特徵，再到有動作標註訓練的任務頭，候選文字「夾取階段」，小字「2024原版教學示意」。沒有未來影片生成或機器人控制箭頭。

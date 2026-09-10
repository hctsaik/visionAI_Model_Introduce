# WI-028 背景相減：先記住背景，再找出新來的工件 r01
- lesson objective: 背景模型記住常態，前景只是需要查看的候選。
- page type: C — 依解釋或對照責任選擇。
- primary reading path: 具體影片問題 → 方法與參考 → 可見結果及限制 → 工作接手。
- major visual nodes:
  1. 累積固定場景
  2. 目前畫面對照背景
  3. 前景候選與回看
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，沿用金屬主體、淡細框及就近對應，不搬頁碼或原文案。
- pale-yellow takeaway: #FFF4CC：背景模型記住常態，前景只是需要查看的候選。
- source: https://docs.opencv.org/4.13.0/d1/dc5/tutorial_background_subtraction.html
- evidence: AI生成教學示意，非模型推論或性能比較。
- generation: built-in imagegen；desktop16:9、mobile獨立上下重排；actual PNG review pending；user approval pending。
- learning applied: WI-027來源／特徵分清，WI-029排除舊圖文字污染，WI-028時刻／位置／輸出責任核對。

## 逐圖因果 brief 與逐字必要標籤
主體固定俯視灰色輸送帶，有固定兩條側軌，银色方形工件向右經過。第一大區「先學背景」：多張不同時間的空帶與工件曾經過的影片縮圖，向下箭頭到同座標乾淨空帶背景，旁邊三個像素位置的灰階小分布表示常見外觀，標「累積常見外觀」，不是唯一一張照片。第二大區「對照現在」：上方同空帶背景，下方目前一片銀色方塊位於中央，短比較括號，不把背景變成工件；標「新工件不同於背景」。第三大區「前景候選」：同座標黑底遮罩中央一個白方形，旁邊小型原影片回看標「檢查進入區域」；底下橘色短註「陰影需另處理」。本圖是二值前景示意、背景相減不是物件分類。

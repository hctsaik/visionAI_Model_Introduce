# WI-028 Lucas–Kanade：用局部紋理追住同一個點 r01
- lesson objective: 追得到的角點提供位移，追丟的點要重新確認。
- page type: C — 依解釋或對照責任選擇。
- primary reading path: 具體影片問題 → 方法與參考 → 可見結果及限制 → 工作接手。
- major visual nodes:
  1. 挑可辨認角點
  2. 在鄰域找小位移
  3. 交出點的移動
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，沿用金屬主體、淡細框及就近對應，不搬頁碼或原文案。
- pale-yellow takeaway: #FFF4CC：追得到的角點提供位移，追丟的點要重新確認。
- source: https://docs.opencv.org/4.x/d4/dee/tutorial_optical_flow.html
- evidence: AI生成教學示意，非模型推論或性能比較。
- generation: built-in imagegen；desktop16:9、mobile獨立上下重排；actual PNG review pending；user approval pending。
- learning applied: WI-027來源／特徵分清，WI-029排除舊圖文字污染，WI-028時刻／位置／輸出責任核對。

## 逐圖因果 brief 與逐字必要標籤
固定相機看同一塊帶L形刻痕的銀色矩形金屬板。第一區「選一個角點」：金屬板上的黑色L形轉角以小藍圓框定位，放大鏡用細定位線連到真正同一角，不是孔心。第二區「鄰域一起找」：兩張放大的L形紋理窗上下對齊，後一張L角向右微移；藍色虛線搜索小窗，短右向箭頭連同一L角的舊新位置；標「亮度近似不變」「附近點一起移動」。可在底部放大小不同的兩層縮圖，標「金字塔先粗後細」；不可畫成神經網路訓練。第三區「點位移」：同金屬板只有三個L角點各自的藍箭頭，非整片密集箭頭；其中被遮蔽一個點橘色×旁標「追丟重找」，接手「核對位移」。不要物件ID、真實毫米數。

# WI-028 工件沒動，亮度變了也會觸發差分 r01
- lesson objective: 大片變化先查光照與相機，不能直接當作工件移動。
- page type: D — 依解釋或對照責任選擇。
- primary reading path: 具體影片問題 → 方法與參考 → 可見結果及限制 → 工作接手。
- major visual nodes:
  1. 光照穩定的静止工件
  2. 同位置照明突然變亮
  3. 廣泛變化與回查光源
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，沿用金屬主體、淡細框及就近對應，不搬頁碼或原文案。
- pale-yellow takeaway: #FFF4CC：大片變化先查光照與相機，不能直接當作工件移動。
- source: https://docs.opencv.org/4.13.0/d1/dc5/tutorial_background_subtraction.html
- evidence: AI生成教學示意，非模型推論或性能比較。
- generation: built-in imagegen；desktop16:9、mobile獨立上下重排；actual PNG review pending；user approval pending。
- learning applied: WI-027來源／特徵分清，WI-029排除舊圖文字污染，WI-028時刻／位置／輸出責任核對。

## 逐圖因果 brief 與逐字必要標籤
三區同一俯視銀方片與灰帶、位置大小完全相同。第一區「原本光照」：兩張相同亮度靜止片與小全黑差分。第二區「只有燈光變亮」：同方片同位置，第二張整幅更亮，燈旁橘色閃電；不加缺口、不移動相機。第三區「差分也會亮」：整片近白遮罩，不只物件邊界；橘色標「亮度變化，不等於移動」，下面同相機與光源旋鈕標「先固定曝光與光源」。三大區是條件比較，不從無變化圖演算法生成燈光。

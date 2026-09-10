# WI-028 ByteTrack：低分框也可能接回同一個工件 r01
- lesson objective: 先匹配高分框，再用低分框補回有依據的軌跡。
- page type: C — 依解釋或對照責任選擇。
- primary reading path: 具體影片問題 → 方法與參考 → 可見結果及限制 → 工作接手。
- major visual nodes:
  1. 偵測器交出高低分框
  2. 先高分再低分關聯
  3. 維持軌跡並計數
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，沿用金屬主體、淡細框及就近對應，不搬頁碼或原文案。
- pale-yellow takeaway: #FFF4CC：先匹配高分框，再用低分框補回有依據的軌跡。
- source: https://arxiv.org/abs/2110.06864
- evidence: AI生成教學示意，非模型推論或性能比較。
- generation: built-in imagegen；desktop16:9、mobile獨立上下重排；actual PNG review pending；user approval pending。
- learning applied: WI-027來源／特徵分清，WI-029排除舊圖文字污染，WI-028時刻／位置／輸出責任核對。

## 逐圖因果 brief 與逐字必要標籤
同一輸送帶上兩塊銀色矩形工件，主要工件有黑色L刻痕。第一區「偵測器先找框」：上一幀主工件框標ID 7，下一幀L板被上方遮擋條擋部分仍有橘色低分框，另一個工件完整藍色高分框，不編虛構分數。第二區「兩次關聯」：上行顯示已存在另一軌跡預測框與高分框疊合標「先接高分」，下行顯示ID7的虛線預測位置與橘色低分框重疊標「未配對，再看低分」；一個遠離兩軌跡的小噪聲框打叉標「無法配對就捨棄」，不能從噪聲啟動新ID。第三區「接回 ID 7」：三時刻同L板向右移，遮擋前中後標ID7，用一條路徑連中心；單條計數線，旁邊「跨線事件另計」。偵測器、追蹤關聯、應用計數三責任要清楚，無ReID外觀網路冒稱必需。


## Selected revision
byte-c1-r03-mobile.png; exact correction prompts retained in sibling JSON; actual native and display-size PNG review completed in image-review.md. User approval pending.

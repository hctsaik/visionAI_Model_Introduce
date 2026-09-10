# WI-030 對稱或遮住時，完整的點也可能配錯
- lesson objective: 低誤差不保證點配對正確；有多解就補證據。
- page type: D — 依具體因果／條件差異教工作判斷。
- primary reading path: 可辨認的方向 → 遮住方向線索 → 保留疑問再補觀測 → 依輸出界線核對原圖與工作條件
- major visual nodes:
  1. 可辨認的方向
  2. 遮住方向線索
  3. 保留疑問再補觀測
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看材質與細框；內容另設計。
- pale-yellow takeaway: #FFF4CC：低誤差不保證點配對正確；有多解就補證據。
- source: https://docs.opencv.org/4.13.0/d5/d1f/calib3d_solvePnP.html
- evidence: AI生成教學示意，非模型推論與效能實測。
- generation: built-in imagegen，桌面16:9，手機獨立重排；actual PNG review pending；user approval pending。

## Visual brief
一片近對稱矩形金屬板四角孔，但左上有獨特小缺口作方向線索。第一區缺口可見，點A左上B右上C右下D左下。第二區紙片只遮住左上缺口，其餘物件四孔仍可見；同一物件旁用兩套方向箭頭表示0度/180度候選（不要填數字，標「兩種合理方向」），A/B/C/D可能整體對調，沒有自動挑正確。第三區換視角露缺口或加非對稱標記的两個替代小示意，用「或」分隔不是串接；標「核對點身分」「再求解」。不畫機器人操作或假精度。

## Validation intent
查來源定位、同物件不變量、訓練／推論兩路、輸出責任；原生與936/328px實看，按v1.0逐圖分項，不能以正文補分。

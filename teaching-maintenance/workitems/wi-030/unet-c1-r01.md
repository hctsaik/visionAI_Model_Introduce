# WI-030 U-Net：把整體線索和細節接回像素
- lesson objective: 遮罩學的是標註的區域；邊界與尺寸仍須驗證。
- page type: C — 依具體因果／條件差異教工作判斷。
- primary reading path: 像素標註教任務 → 縮小理解，再接回細節 → 交出區域遮罩 → 依輸出界線核對原圖與工作條件
- major visual nodes:
  1. 像素標註教任務
  2. 縮小理解，再接回細節
  3. 交出區域遮罩
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看材質與細框；內容另設計。
- pale-yellow takeaway: #FFF4CC：遮罩學的是標註的區域；邊界與尺寸仍須驗證。
- source: https://arxiv.org/abs/1505.04597
- evidence: AI生成教學示意，非模型推論與效能實測。
- generation: built-in imagegen，桌面16:9，手機獨立重排；actual PNG review pending；user approval pending。

## Visual brief
俯視銀色板中間一條彎曲深色焊縫；第一區同一原圖和人工標註焊縫遮罩並列，標「原圖」「人工標註」。第二區新原圖進U形編碼解碼路徑，左邊高解析特徵有細縫，中低解析特徵較粗，右邊上採樣逐步恢復；兩條同尺度跳接把左方細節送右方與深層線索合併。至少看見一個細節從左到右，同尺度相連不是連原圖到輸出。第三區同樣彎焊縫的橘色預測區域疊同原图；小局部放大比較邊界偏差，用「量邊界誤差」箭頭，不畫尺寸數值。

## Validation intent
查來源定位、同物件不變量、訓練／推論兩路、輸出責任；原生與936/328px實看，按v1.0逐圖分項，不能以正文補分。

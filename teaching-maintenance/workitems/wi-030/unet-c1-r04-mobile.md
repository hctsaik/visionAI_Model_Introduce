# WI-030 U-Net：把整體線索和細節接回像素 — mobile
- lesson objective: 遮罩學的是標註的區域；邊界與尺寸仍須驗證。
- page type: C
- primary reading path: 像素標註教任務 → 縮小理解，再接回細節 → 交出區域遮罩 → 核對輸出與工作條件
- major visual nodes:
  1. 像素標註教任務
  2. 縮小理解，再接回細節
  3. 交出區域遮罩
- named guide-conformant reference page: teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png
- pale-yellow takeaway: #FFF4CC：遮罩學的是標註的區域；邊界與尺寸仍須驗證。
- source: https://arxiv.org/abs/1505.04597
- generation: built-in imagegen；教學示意非模型實測。
- actual PNG review: reviewed；原生與936/328px證據見prototype-review.md；這是候選選定，不是使用者核准。
- user approval: pending

## 版本與生成意圖
產物：unet-c1-r04-mobile.png。原型生成前已有同故事r01及逐版preflight，本檔彙整實際選用版本，保留歷史。

{"prompt":"完整獨立重排為768x2048手機直向三大區。第一區同一彎焊縫原圖與人工標註配對。第二區完整U形編碼解碼：輸入→左上藍大特徵→左中綠→左下紅小→右下紅小→右中綠→右上藍大→遮罩。兩條同尺度跳接藍到藍、綠到綠，底部紅到紅是主路徑不可斷。每欄標編碼整合／解碼恢復，各特徵用抽象像素線索非實測。第三區同一原圖局部的人工與預測邊界兩張對照，預測橘輪廓略偏，不画誤差尺寸箭頭，標『對照邊界，另行量測』。繁體中文粗體在328px讀懂，白底淡藍細框无序號，唯一#FFF4CC燈泡原結論，教學示意。","reference":"unet-c1-r04-desktop.png"}


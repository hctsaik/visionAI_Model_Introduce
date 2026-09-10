# WI-030 U-Net：把整體線索和細節接回像素 — desktop
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
產物：unet-c1-r04-desktop.png。原型生成前已有同故事r01及逐版preflight，本檔彙整實際選用版本，保留歷史。

{"prompt":"重製中央核心，不更改左右案例。中央畫真正完整U形流程，必須有六塊不同尺寸抽象特徵圖：左上最大藍→左中較小綠→左下最小紅→右下最小紅→右中較大綠→右上最大藍。底部左紅到右紅必須有向右箭頭連上，不能断開。左欄標『編碼：整合範圍』，右欄標『解碼：恢復尺度』。兩條跨接箭頭只在藍與綠同尺度之間，标『同尺度跳接』。中央上方一個小原圖箭頭進左上蓝，右上蓝箭头進右區遮罩。特徵圖內用抽象藍綠像素塊加一條焊縫線索，不用完整寫實照片冒充張量。右區原圖局部對照保留，同源紋理位置相同，無量測箭頭。不得移除任何上述主路徑箭頭或必要標籤。","reference":"unet-c1-r03-desktop.png"}


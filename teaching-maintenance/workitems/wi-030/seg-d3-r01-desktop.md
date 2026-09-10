# WI-030 要同類區域，還是每件各一張遮罩？ — desktop
- lesson objective: 先決定輸出責任；同類區域不等於每件身分。
- page type: D
- primary reading path: 共同兩件输入 → 語意分割 → 實例分割 → 核對輸出與工作條件
- major visual nodes:
  1. 共同兩件输入
  2. 語意分割
  3. 實例分割
- named guide-conformant reference page: teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png
- pale-yellow takeaway: #FFF4CC：先決定輸出責任；同類區域不等於每件身分。
- source: https://arxiv.org/abs/1505.04597
- generation: built-in imagegen；教學示意非模型實測。
- actual PNG review: reviewed；原生與936/328px證據見prototype-review.md；這是候選選定，不是使用者核准。
- user approval: pending

## 版本與生成意圖
產物：seg-d3-r01-desktop.png。原型生成前已有同故事r01及逐版preflight，本檔彙整實際選用版本，保留歷史。

{"prompt":"製作繁體中文工業AI教學PNG，白底淡藍細框、大深藍粗體字、寫實金屬件配抽象特徵示意，16:9約1672x941，恰好3個大節點，不畫序號徽章或深色頁腳。標題「要同類區域，還是每件各一張遮罩？」。三區「共同兩件输入 → 語意分割 → 實例分割」。場景：兩個同類金屬墊圈左右不重疊，原圖孔清楚。分兩平行分支不串接：U-Net／SegFormer語意分割兩個環形區同藍色，標「同類像素同色」；YOLO-Seg兩件分藍橘不同mask，標「同類也分開每件」。所有孔留空、相對位置不改。底部標「區域標註」與「實例標註」資料不同，量測仍另校正。。資料箭頭只接正確入口；輸入照片先編碼成抽象特徵，不把照片直接當特徵。分支與比較不可誤畫串接。相同工件位置、孔洞與同原圖的前後不變量逐一保持。每區用可見操作與結果教意義，不以密集文字卡代替。唯一底部#FFF4CC燈泡「先決定輸出責任；同類區域不等於每件身分。」。小註『教學示意，非實測』。936px寬仍讀懂，控制小字。參考只借材質細框，完全新畫內容。"}


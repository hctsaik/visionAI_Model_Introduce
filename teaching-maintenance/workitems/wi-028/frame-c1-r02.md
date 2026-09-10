# WI-028 Frame Difference 原型 r01
- lesson objective: 兩張影格相減找出變化，停住的物件可能消失，差分不等於完整輪廓。
- page type: C — 用同一工件由影格到差分結果解釋原理。
- primary reading path: 輸送帶影格 → 同位置亮度比較 → 移動前後留下變化區 → 回影片檢查事件。
- major visual nodes:
  1. 固定相機的兩張影格：銀色方形金屬塊從左移到右，部分重疊。
  2. 比較同一像素：重疊區未變，只有左右兩帶改變。
  3. 變化遮罩與事件回看：黑底上左右兩條白帶，中央黑色，不能當兩個物件。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看兩張首選，沿用金屬主體、淡細框、對應關係與大圖，不搬頁碼或舊文案。
- pale-yellow takeaway: #FFF4CC：差分找出哪裡變了，再回影片確認發生什麼。
- source: https://docs.opencv.org/4.x/d2/de8/group__core__array.html ; 定義為同位置絕對亮度差及門檻，受控示意。
- evidence: AI 生成教學示意；不是模型推論，也不是現場效能測試。
- generation: built-in imagegen；桌面16:9，手機獨立直向重排；actual PNG review pending；user approval pending。

## Prompt intent / exact labels
繁體中文、白底、細淡藍圓角框、海軍藍標題、三大主節點左至右、粗藍因果箭頭。半寫實金屬方塊與灰色輸送帶，相機固定。標題「Frame Difference：找出兩張畫面的變化」。第一區「同一工件，兩個時間點」：兩張同大小灰背景裁切上下排列，前一張銀灰方塊在左，後一張右移一小段，固定視角無旋轉、物體亮度相同，使用平坦頂面方形。
第二區「比較同位置」：以重疊圖顯示兩個相同方形，前框藍色實線、後框橘色虛線，中央重疊大區淡灰，左／右非重疊窄區明示；短標籤「中央沒變」「兩側改變」。本區是對應示意不是照片疊加實測。
第三區「白色＝變化」：同座標黑色遮罩，只有左右兩條等寬白帶，中間大區保持黑色；短句「不是兩個物件」「回看事件片段」，下面小型影片縮圖顯示同一塊移動方塊，不引入其他物件。
底部唯一淡黃#FFF4CC燈泡結論：「差分找出哪裡變了，再回影片確認發生什麼。」小字「教學示意」。無頁碼、無logo，不從參考複製校正或contract內容，不自行補數字。字大、留白、主要證據占畫面大部分。
# r02 修正記錄
將輸入照片換成同視角俯視銀色方片，向右移約四分之一片寬；中間75%重疊，遮罩兩側白帶，回看片段同向位移。刪除區塊序號及長段落。手機沿用三區上下直排，區內兩影格上下對照，圖內字級需在328px內容寬度可讀；單黃結論完整保留。

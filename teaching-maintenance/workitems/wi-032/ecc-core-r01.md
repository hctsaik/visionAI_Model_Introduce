# WI-032 ECC 原型：讓重合的過程看得見
- lesson objective: ECC反覆比較外觀相關並更新幾何變換，把已接近的兩張圖對齊；輸出變換，不判定缺陷。
- page type: C — 以同一金屬支架的偏移、取樣比較、更新與交付呈現機制。
- primary reading path: 模板與小偏移待對圖 → 以目前變換重採樣並比較外觀相關 → 更新後同位置邊緣差縮小 → 交出變換與獨立殘差核對
- major visual nodes:
  1. 模板與待對圖的同一L形金屬支架，兩孔、右上缺口固定。
  2. 同一孔邊緣放大：warp前雙邊錯開、更新後重合；外觀波形就近對照。
  3. 交出變換後的對齊影像，保留獨立殘差驗證與下游檢查區域。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 2026-09-11已實看，借用具體材質、放大對應、淡藍細框與留白，不複製多欄或舊文字。
- pale-yellow takeaway: #FFF4CC：ECC把已接近的影像微調對齊；缺陷仍要另外檢查。
- evidence: AI生成概念示意，無效能數值，不是ECC真實輸出；歷史真實案例另保留。
- source: https://docs.opencv.org/4.x/dc/d6b/group__video__track.html
- generation: built-in imagegen；桌機16:9；手機另排直向。actual PNG review pending；user approval pending。

## 可見證據與資料關係
整頁主體是同一支架兩張灰階照片，以及同一左孔的邊緣放大。模板用藍色實線、待對用橘色虛線；局部均與模板同座標、同尺度。中央分成更新前後兩個子狀態，前有明顯雙邊和錯峰，後重合；圖註「概念示意，非等比例」。外觀相關說明必須靠同邊緣強度曲線的相似形狀與位置改善，不只放名詞。重採樣後再比相關、再更新變換；不承諾每一輪單調提高。右側顯示變換交給warp，對齊影像上的ROI維持同孔位置。殘差是另行核對，不能說是findTransformECC的原生回傳值。

## 逐字重點文案
標題「ECC：反覆比外觀，把小偏移修回來」；副標「對位算法｜不需訓練權重｜教學示意」。三區「兩張圖已經接近」「重採樣、比相關、更新」「交出變換，再核對」。短標「模板」「待對圖」「更新前」「更新後」「同一孔邊緣放大」「幾何變換」「獨立殘差核對」。底部單一結論如上。

## 本輪修正與驗收
解決WI-031：重複小照片／看不出殘差。有效支架與放大區占主要面積，中央清楚顯示兩條邊的位置真的改變；不用0.2px文字假裝肉眼可見精度。不得增加人物、重複小卡、無關PCB、頁碼與假分數。桌機原圖／頁內及手機360px分別審查；有失敗先修原型，不批量套用。

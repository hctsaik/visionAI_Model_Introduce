# CLIP 工程圖 2：圖文各自編碼，才比較方向

- lesson objective: 讀者能從同一工件的影像與候選文字，追到兩個獨立編碼器、共同表示比較及候選排名。
- page type: C — 解釋雙路匯合；不是影像編碼器接文字編碼器。
- primary reading path: 工件與文字輸入 → 分別編碼 → 相似度與候選限制 → 依排名找圖並覆核
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍色標頭、具體工件與黃色結論，刪除細密側欄與縮小英文。
- pale-yellow takeaway: 圖文各走一條路，匯合後才比較候選。 #FFF4CC
- major visual nodes:
  1. 同一金屬支架影像與三條文字分別經影像／文字編碼器，兩路並行。
  2. 示意單位向量在共同空間比較角度，三候選方向不同。
  3. 候選分數長條與覆核動作，排名不提供缺陷位置。

## 視覺與來源契約

工件為新建原生 SVG 金屬支架，兩孔和缺口固定；不是改寫歷史照片。影像與文字都只變成表示，原件不消失。向量與分數為可追算二維示意：影像方向 0 度；支架 15 度、齒輪 60 度、軸承 80 度，cosine 約 0.97／0.50／0.17，不代表 CLIP 實測。先以線條／夾角看差異，再看數值。

關係：影像→影像編碼器→影像表示；文字→文字編碼器→文字表示；兩者→相似度。兩編碼器之間無箭頭。比較線與角度不冒充位置對應或缺陷熱圖。

來源：https://arxiv.org/abs/2103.00020 與 https://github.com/openai/CLIP 。參考既有 CLIP-02 可见影像路徑→文字路徑錯接及排名熱點，本輪必須消除。GEO-21 舊圖雖被前輪列參考，實看有頁碼／藍色結論／六欄，不採作本輪合格母版。

生成模式：全新 SVG 幾何與標註，瀏覽器轉 PNG。桌機 1672×941；手機獨立直向畫布，360px 等效審讀。預期產物 clip-engineering-2-r03-desktop.png、clip-engineering-2-r03-mobile.png。

五份權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md；原生 PNG review pending，頁內 review pending，user approval pending。不把通過 preflight 當視覺核准。

Revision: prototype-review.md records the r01 boundary and representation corrections.

Revision r03: equal X/Y radius preserves unit-vector angles.

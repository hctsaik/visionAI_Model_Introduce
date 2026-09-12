# AnomalyDINO：先判斷旋轉是否被允許

- lesson objective: 旋轉擴充改變正常涵蓋，朝向規格仍須另驗。
- page type: D — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 共同工件：刻字有方向 → 自由擺放：可測旋轉參考 → 標誌朝上：不可放寬方向
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 旋轉擴充改變正常涵蓋，朝向規格仍須另驗。 #FFF4CC
- major visual nodes:
  1. 共同工件：刻字有方向；具體視覺 adino-upright
  2. 自由擺放：可測旋轉參考；具體視覺 adino-rotate-free
  3. 標誌朝上：不可放寬方向；具體視覺 adino-rotate-required

## 機制、證據與修正

同一帶A-01刻字的板連同所有孔位/字一起剛性旋轉180度。若規格允許自由方向，可測旋轉參考是否減少誤報；若標誌必須朝上，就不能以納入倒置參考來消除方向錯誤，另做方向檢查。兩路是不同工作規格，不是演算法串接。

來源：https://arxiv.org/html/2405.14529v2 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG L形刻痕板、A-01刻字板或三格圓柱托盤，依各圖聲明；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

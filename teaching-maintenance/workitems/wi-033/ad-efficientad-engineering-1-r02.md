# EfficientAD：正常品教三個角色合作

- lesson objective: 教師固定，學生兩組輸出與AE各有訓練目標。
- page type: C — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 正常托盤與固定教師 → 學生第一組學教師 → AE與學生第二組一起學
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 教師固定，學生兩組輸出與AE各有訓練目標。 #FFF4CC
- major visual nodes:
  1. 正常托盤與固定教師；具體視覺 eff-teacher
  2. 學生第一組學教師；具體視覺 eff-student1
  3. AE與學生第二組一起學；具體視覺 eff-train-global

## 機制、證據與修正

選定預訓練輕量教師並固定；學生第一組以正常影像學教師特徵，原方法另有hard-feature與外部預訓練圖penalty。AE由整圖重建教師特徵，學生第二組學AE重建；使用正常資料訓練，真缺陷留作獨立檢查。學生兩組共享前層，不是兩個互不相關模型。

來源：https://arxiv.org/html/2303.14535v3 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG L形刻痕板、A-01刻字板或三格圓柱托盤，依各圖聲明；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

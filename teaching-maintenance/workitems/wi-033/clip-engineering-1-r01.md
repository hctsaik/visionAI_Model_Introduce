# CLIP：用描述整理零件照片

- lesson objective: 文字定義候選，影像與描述的相似度幫你找圖。
- page type: C — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 照片庫裡有不同零件 → 把工作需求寫成候選 → 用候選排名找出照片
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 文字定義候選，影像與描述的相似度幫你找圖。 #FFF4CC
- major visual nodes:
  1. 照片庫裡有不同零件；具體視覺 catalog
  2. 把工作需求寫成候選；具體視覺 descriptions
  3. 用候選排名找出照片；具體視覺 retrieval

## 機制、證據與修正

工件照片與候選描述各自編碼。新增描述可定義新的比較集合，無須為每次檢索重新訓練固定類別頭；預訓練及域內驗證仍不可省略。相似度排名不是缺陷位置或合格證明。

來源：https://arxiv.org/abs/2103.00020 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG 金屬支架／齒輪／軸承；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

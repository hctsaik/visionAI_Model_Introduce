# DINOv3：一張圖保留多個局部表示

- lesson objective: 骨幹交出特徵，局部位置與下游工作仍要對齊。
- page type: C — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 輸入一個墊圈影像 → 每個區塊各有特徵 → 下游才解讀相似或不同
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 骨幹交出特徵，局部位置與下游工作仍要對齊。 #FFF4CC
- major visual nodes:
  1. 輸入一個墊圈影像；具體視覺 dino-washer
  2. 每個區塊各有特徵；具體視覺 dino-patchfeatures
  3. 下游才解讀相似或不同；具體視覺 dino-nearest

## 機制、證據與修正

以ViT骨幹為例，影像轉成patch token並與其他位置交換資訊，輸出局部及全局表示。局部表示保留對應位置，但每個向量包含上下文，不等於該格像素值。異常判斷、分類或匹配要接下游方法；特徵色圖不是現成缺陷分數。

來源：https://arxiv.org/html/2508.10104v1 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG 金屬支架／齒輪／軸承；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

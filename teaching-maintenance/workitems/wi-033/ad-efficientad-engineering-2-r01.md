# EfficientAD：局部與全局比較對象不同

- lesson objective: 局部比T/S1，全局比AE/S2；校正尺度後才融合。
- page type: C — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 同一待測托盤送入三者 → 兩路各比對應的表示 → 正常驗證資料校正後融合
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 局部比T/S1，全局比AE/S2；校正尺度後才融合。 #FFF4CC
- major visual nodes:
  1. 同一待測托盤送入三者；具體視覺 eff-test
  2. 兩路各比對應的表示；具體視覺 eff-two-diffs
  3. 正常驗證資料校正後融合；具體視覺 eff-calibrate

## 機制、證據與修正

同一托盤有中間缺件及右側污點；T與學生第一組S1的通道均方差產生local，AE與學生第二組S2的差產生global，不能誤畫T減AE或直接原圖減重建照片。用未參與訓練的正常驗證分布各自做分位數線性尺度對齊，再平均兩圖；最大值作整圖分數。熱區僅示意，不保證兩路專抓某種缺陷。

來源：https://arxiv.org/html/2303.14535v3 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG L形刻痕板、A-01刻字板或三格圓柱托盤，依各圖聲明；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

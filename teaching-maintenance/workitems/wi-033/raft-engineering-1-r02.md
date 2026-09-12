# RAFT：先把兩張影格变成配對線索

- lesson objective: 兩張圖建立相關性，第一張圖另提供更新情境。
- page type: C — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 固定影格對與模型版本 → 兩圖特徵建立全配對 → 第一圖提供更新情境
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 兩張圖建立相關性，第一張圖另提供更新情境。 #FFF4CC
- major visual nodes:
  1. 固定影格對與模型版本；具體視覺 flow-pair
  2. 兩圖特徵建立全配對；具體視覺 raft-correlation
  3. 第一圖提供更新情境；具體視覺 raft-context

## 機制、證據與修正

固定原始RAFT權重、解析度、padding和迭代數。共享特徵網路抽兩圖表示後，建立全位置配對相關性及多尺度池化；第一圖經context encoder提供隱狀態與情境。相關性是候選配對線索，不是最終光流或每個像素的可靠度。

來源：https://arxiv.org/abs/2003.12039 ; https://github.com/princeton-vl/RAFT/blob/master/core/raft.py 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG L形刻痕板、A-01刻字板或三格圓柱托盤，依各圖聲明；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

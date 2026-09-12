# RAFT：依目前位置查詢，再修正光流

- lesson objective: 用目前光流查相關性，更新量加回後繼續修正。
- page type: C — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 在目前估計周圍查線索 → 更新單元融合四種資訊 → 加上更新量，再查下一輪
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 用目前光流查相關性，更新量加回後繼續修正。 #FFF4CC
- major visual nodes:
  1. 在目前估計周圍查線索；具體視覺 raft-lookup
  2. 更新單元融合四種資訊；具體視覺 raft-update
  3. 加上更新量，再查下一輪；具體視覺 raft-refine

## 機制、證據與修正

原始RAFT以目前座標查詢多尺度相關性；更新單元接相關性、目前光流、context與隱狀態，輸出位移增量並更新隱狀態。新光流=舊光流+增量，固定解析度反覆更新，最後上採樣。圖中(1,0)+(1,1)=(2,1)只解釋更新算術，不是實際模型收斂或逐輪保證改善。

來源：https://arxiv.org/abs/2003.12039 ; https://github.com/princeton-vl/RAFT/blob/master/core/raft.py 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG L形刻痕板、A-01刻字板或三格圓柱托盤，依各圖聲明；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

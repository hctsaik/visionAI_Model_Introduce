# RAFT：增加迭代是否值得，要同題量

- lesson objective: 迭代設定改變成本，效果仍用同一資料驗證。
- page type: D — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 同資料與同一初始設定 → 較少迭代的候選 → 較多迭代的候選
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 迭代設定改變成本，效果仍用同一資料驗證。 #FFF4CC
- major visual nodes:
  1. 同資料與同一初始設定；具體視覺 flow-work
  2. 較少迭代的候選；具體視覺 raft-fewer
  3. 較多迭代的候選；具體視覺 raft-more

## 機制、證據與修正

固定同一權重、影格對、解析度、precision和硬體，只改更新次數；在同一有效性標註上比较錯誤、覆蓋與耗時，不能保證更多迭代一定改善，也不能把彩色光流當精度證據。保留較少迭代也可能合理。

來源：https://arxiv.org/abs/2003.12039 ; https://github.com/princeton-vl/RAFT/blob/master/core/raft.py 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG L形刻痕板、A-01刻字板或三格圓柱托盤，依各圖聲明；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

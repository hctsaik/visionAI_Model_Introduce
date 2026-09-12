# RAFT：稠密數值要配合有效性核對

- lesson objective: 輸出向量不等於看見對應，遮擋區要另驗。
- page type: C — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 同一工件輸出稠密場 → 反光與遮擋另查一致性 → 算進相關性與迭代成本
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 輸出向量不等於看見對應，遮擋區要另驗。 #FFF4CC
- major visual nodes:
  1. 同一工件輸出稠密場；具體視覺 flow-dense
  2. 反光與遮擋另查一致性；具體視覺 raft-reject
  3. 算進相關性與迭代成本；具體視覺 raft-cost

## 機制、證據與修正

保存兩影格、原尺寸、前處理、權重、迭代設定與位移場；遮擋/反射可能沒有可見對應但仍輸出數值。可用往返一致性作應用檢查，仍不是遮擋真值或原始RAFT原生置信輸出。完整成本包含特徵、相關性、更新和上採樣，並量記憶體。

來源：https://arxiv.org/abs/2003.12039 ; https://github.com/princeton-vl/RAFT/blob/master/core/raft.py 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG L形刻痕板、A-01刻字板或三格圓柱托盤，依各圖聲明；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

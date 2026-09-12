# Lucas–Kanade：同題比較稀疏與稠密

- lesson objective: 先確定需要哪些位置，再比較錯誤與完整成本。
- page type: D — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 同一影格對與工作需求 → LK：只驗被選中的點 → RAFT：另驗整張位移場
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 先確定需要哪些位置，再比較錯誤與完整成本。 #FFF4CC
- major visual nodes:
  1. 同一影格對與工作需求；具體視覺 flow-work
  2. LK：只驗被選中的點；具體視覺 flow-sparse
  3. RAFT：另驗整張位移場；具體視覺 flow-dense

## 機制、證據與修正

同一L形工件、影格間隔和原圖；若工作只需少數穩定角點，LK可作基準。需要稠密場時加入RAFT；在共同可評位置比較位移錯誤，另報各自覆蓋率和端到端耗時，不能把不同輸出數量當成精度優勢。

來源：https://docs.opencv.org/4.13.0/d4/dee/tutorial_optical_flow.html 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG L形刻痕板、A-01刻字板或三格圓柱托盤，依各圖聲明；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

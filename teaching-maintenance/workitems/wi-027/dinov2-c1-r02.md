# WI-027 DINOv2 核心原型 r02
- lesson objective: 展示特徵學習與下游檢索的兩方比較，不把相同特徵條畫成不同順位。
- page type: C — 訓練、部署、檢索的因果。
- primary reading path: 同圖不同視圖 → Teacher目標引導Student → 單模型抽特徵 → 與庫比較找候選。
- major visual nodes:
  1. 同圖全景與孔位局部視圖。
  2. Teacher 提供學習目標給 Student。
  3. 部署 encoder 交出整圖及局部特徵。
  4. 待查特徵和參考庫特徵匯入比較，再輸出相似支架。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 實看主體及就近证據。
- pale-yellow takeaway: #FFF4CC：先把影像學成特徵，再由下游決定怎麼用。
- correction: r01 第四區支架與齒輪特徵條相同，待查條未接到比較且先標出候選。改為三方可見輸入、齒輪不同示意表示、比較後再顯示支架候選；不以正文補圖。
- evidence: 教學示意，不是相似度實測；訓練特徵條只表示匹配目標。
- generation: built-in imagegen edit r01，其他區全圖回查。actual review pending；user approval pending。

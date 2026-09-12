# AnomalyDINO：每個局部找最近正常

- lesson objective: 最近距離保留位置，組成候選異常圖。
- page type: C — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 同一待測影像抽局部表示 → 全庫搜尋相近正常特徵 → 距離回映同一局部位置
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 最近距離保留位置，組成候選異常圖。 #FFF4CC
- major visual nodes:
  1. 同一待測影像抽局部表示；具體視覺 adino-query
  2. 全庫搜尋相近正常特徵；具體視覺 adino-distance
  3. 距離回映同一局部位置；具體視覺 adino-location

## 機制、證據與修正

待測整圖與參考共用DINOv2權重及相容前處理。每個test token以餘弦距離在normal memory找最近者；圖中0.40、0.62、0.55為教學給定距離，最小0.40不代表已足夠正常。局部距離上採樣/平滑形成位置圖；整件分數另聚合最高1%patch距離，不能把熱圖當精密輪廓。

來源：https://arxiv.org/html/2405.14529v2 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG L形刻痕板、A-01刻字板或三格圓柱托盤，依各圖聲明；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

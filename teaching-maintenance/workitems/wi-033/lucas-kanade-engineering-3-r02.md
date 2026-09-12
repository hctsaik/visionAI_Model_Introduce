# Lucas–Kanade：把可追的點與失效分開

- lesson objective: 保存點對、時間與有效性，再決定能否接量測。
- page type: C — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 同名點保留前後座標 → 失敗位置退出追蹤 → 像素位移另接校正與時間
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 保存點對、時間與有效性，再決定能否接量測。 #FFF4CC
- major visual nodes:
  1. 同名點保留前後座標；具體視覺 flow-points
  2. 失敗位置退出追蹤；具體視覺 lk-reject
  3. 像素位移另接校正與時間；具體視覺 flow-measure

## 機制、證據與修正

保存前後影格ID、座標、時間差、狀態與殘差；追丟或一致性差的點不可沿用舊箭頭。需要物理位移或速度時，另有相機運動處理、平面/深度條件與尺度校正，不能把像素向量直接標成毫米或物件ID。

來源：https://docs.opencv.org/4.13.0/d4/dee/tutorial_optical_flow.html 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG L形刻痕板、A-01刻字板或三格圓柱托盤，依各圖聲明；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2400。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

# 同一線痕，位置熱圖和輪廓回答不同問題

- lesson objective: 先選要位置還是輪廓，再準備資料與驗證。
- page type: D — 按本圖資料處理或同条件比較安排。
- primary reading path: 具體工件／問題 → 共同原圖：下中線痕 → 異常檢測：可疑位置 → 監督分割：已定義輪廓
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/docs/course-delivery/section-pages/06-foundation-vision-vlm/images/final/FDNIN-01-foundation-input-contract_v03.png` — 已實看；沿用淺底、藍標頭、具體輸入與黃色結論，不沿用細字與側欄。
- pale-yellow takeaway: 先選要位置還是輪廓，再準備資料與驗證。 #FFF4CC
- major visual nodes:
  1. 共同原圖：下中線痕；具體視覺 deep-board-input
  2. 異常檢測：可疑位置；具體視覺 deep-output-location
  3. 監督分割：已定義輪廓；具體視覺 deep-output-contour

## 機制、證據與修正

深讀4章同題比較，移除替代輸出之間的因果箭頭。固定同一A-01線痕；EfficientAD正常訓練得位置線索，監督分割需已定義目標的輪廓標註。若要實體面積另需校正與誤差驗證；圖中框與輪廓皆教學設定。

來源：https://arxiv.org/html/2303.14535v3 。影像、文字、表示與輸出角色分開；線只連實際資料入口，替代方案無跨欄因果箭頭。工件為新建 SVG L形刻痕板、A-01刻字板或三格圓柱托盤，依各圖聲明；相同件的孔洞、缺口不變。文字、分數和框只負責已宣告的教學問題，非實際模型推論。

生成：原生 SVG→PNG；桌機1672×941、手機768×2304。圖像與頁內360px均須實看，檢查候選身份、箭頭、換行與圖內邊界。承接 prototype-review.md 已通過的CLIP雙路原型，但每張仍需獨立評分，不自動沿用分數。

權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。PNG review pending；page review pending；user approval pending。

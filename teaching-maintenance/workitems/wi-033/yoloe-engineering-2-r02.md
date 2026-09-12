# YOLOE：圈選範例，聚合成提示表示
- lesson objective: 提示區域變成表示，再與待測區域比較。
- page type: C
- primary reading path: 參考圖圈出電阻A → SAVPE按啟動權重聚合 → 待測圖交出框與遮罩 → 提示區域變成表示，再與待測區域比較。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 提示區域變成表示，再與待測區域比較。 #FFF4CC
- major visual nodes:
  1. 參考圖圈出電阻A；b4-ye-roi
  2. SAVPE按啟動權重聚合；b4-ye-pool
  3. 待測圖交出框與遮罩；b4-ye-output

本圖限定視覺提示模式SAVPE。語意特徵與ROI啟動分支產生加權聚合，例用兩位置[2,0]/[0,2]及0.75/0.25得到[1.5,0.5]解釋聚合，非真實模型維度或權重。提示表示與待測區域表示比對，A/B可同類相似，不等於相同料號。文字RepRTA和免提示LRPC是其他模式，不畫成必須順序執行。
來源：https://arxiv.org/abs/2503.07465
生成模式：新建精確SVG→桌機1672×941、手機768×2304 PNG；不編修既有點陣素材。已實看本批原主線的具體工件，保留PCB雙電阻、L支架與雙圓接頭的身份。各家族先原型實看再擴展其他工程；DINOv2/Gemini主反例另統一同件。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

修訂：r01 PNG部分圖形／文字缺畫，SVG節點完整；改用disable-gpu並等字型/500ms繪製。NMS前後尺度一致，YOLOE遮罩覆蓋完整電阻並透明保留料號；DINO遮蔽視圖名稱精確。所有候選仍需逐張原生審查。

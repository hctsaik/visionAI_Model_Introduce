# 原版LLaVA：把影像表示接進語言模型
- lesson objective: 投影橋接影像與文字，回答仍要有可見證據。
- page type: C
- primary reading path: 同一接頭影像經視覺編碼 → 投影後與問題文字一起送入 → 語言模型逐token產生回答 → 投影橋接影像與文字，回答仍要有可見證據。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 投影橋接影像與文字，回答仍要有可見證據。 #FFF4CC
- major visual nodes:
  1. 同一接頭影像經視覺編碼；b4-llava-encode
  2. 投影後與問題文字一起送入；b4-llava-project
  3. 語言模型逐token產生回答；b4-llava-answer

以原版LLaVA為界：預訓練視覺編碼器輸出表示，學習線性投影接入語言模型的embedding空間，再與問題文字共同產生回答。圖內小向量僅說明不同維度的橋接，不是該模型實際維度。右側空螺絲座支持未見螺絲，不能推出漏裝或振動鬆脫等原因。
來源：https://arxiv.org/abs/2304.08485
生成模式：新建精確SVG→桌機1672×941、手機768×2304 PNG；不編修既有點陣素材。已實看本批原主線的具體工件，保留PCB雙電阻、L支架與雙圓接頭的身份。各家族先原型實看再擴展其他工程；DINOv2/Gemini主反例另統一同件。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

修訂：r01 PNG部分圖形／文字缺畫，SVG節點完整；改用disable-gpu並等字型/500ms繪製。NMS前後尺度一致，YOLOE遮罩覆蓋完整電阻並透明保留料號；DINO遮蔽視圖名稱精確。所有候選仍需逐張原生審查。

# Grounding DINO：詞與區域共同定位
- lesson objective: 文字参与候選和解碼，交付詞語與框。
- page type: C
- primary reading path: 影像與文字各自編碼 → 詞token與區域交換訊息 → 詞引導query，解碼成框 → 文字参与候選和解碼，交付詞語與框。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 文字参与候選和解碼，交付詞語與框。 #FFF4CC
- major visual nodes:
  1. 影像與文字各自編碼；b4-ground-input
  2. 詞token與區域交換訊息；b4-ground-align
  3. 詞引導query，解碼成框；b4-ground-output

以同PCB的resistor文字查詢；影像特徵與文字token在feature enhancer互動，language-guided query selection挑相關起點，cross-modality decoder再利用兩種表示修框。圖中詞區域數字是相容性教學例，不是置信度實測。輸出詞語相關分數及框，並非像素遮罩。
來源：https://arxiv.org/abs/2303.05499
生成模式：新建精確SVG→桌機1672×941、手機768×2304 PNG；不編修既有點陣素材。已實看本批原主線的具體工件，保留PCB雙電阻、L支架與雙圓接頭的身份。各家族先原型實看再擴展其他工程；DINOv2/Gemini主反例另統一同件。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

修訂：r01 PNG部分圖形／文字缺畫，SVG節點完整；改用disable-gpu並等字型/500ms繪製。NMS前後尺度一致，YOLOE遮罩覆蓋完整電阻並透明保留料號；DINO遮蔽視圖名稱精確。所有候選仍需逐張原生審查。

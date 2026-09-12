# Gemini影像介面：請求、回覆、查證
- lesson objective: JSON能解析，只代表格式；內容仍要對原圖。
- page type: C
- primary reading path: 固定影像、問題與欄位要求 → 服務回傳可解析的JSON → 逐欄回原圖查可見證據 → JSON能解析，只代表格式；內容仍要對原圖。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: JSON能解析，只代表格式；內容仍要對原圖。 #FFF4CC
- major visual nodes:
  1. 固定影像、問題與欄位要求；b4-gemini-request
  2. 服務回傳可解析的JSON；b4-gemini-json
  3. 逐欄回原圖查可見證據；b4-gemini-check

依公開Gemini API說明輸入/輸出，不臆測私有編碼器。以同一左右圓接頭，左有螺絲右空座，示意JSON先錯填兩側present；解析成功後逐欄對照原圖，右側應記not_visible且原因unknown。所有回覆為作者設計反例，未呼叫API；實際部署另固定可用模型、schema與輸入設定。
來源：https://ai.google.dev/gemini-api/docs/structured-output
生成模式：新建精確SVG→桌機1672×941、手機768×2304 PNG；不編修既有點陣素材。已實看本批原主線的具體工件，保留PCB雙電阻、L支架與雙圓接頭的身份。各家族先原型實看再擴展其他工程；DINOv2/Gemini主反例另統一同件。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

修訂：r01 PNG部分圖形／文字缺畫，SVG節點完整；改用disable-gpu並等字型/500ms繪製。NMS前後尺度一致，YOLOE遮罩覆蓋完整電阻並透明保留料號；DINO遮蔽視圖名稱精確。所有候選仍需逐張原生審查。

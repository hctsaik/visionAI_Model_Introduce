# Qwen2-VL：可變token也保留位置
- lesson objective: 動態解析度與位置編碼，仍受原像素限制。
- page type: C
- primary reading path: 解析度不同，形成可變token數 → M-RoPE保留時空位置 → 與問題一起讀出可見文字 → 動態解析度與位置編碼，仍受原像素限制。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 動態解析度與位置編碼，仍受原像素限制。 #FFF4CC
- major visual nodes:
  1. 解析度不同，形成可變token數；b4-qwen-dynamic
  2. M-RoPE保留時空位置；b4-qwen-position
  3. 與問題一起讀出可見文字；b4-qwen-answer

限定Qwen2-VL：Naive Dynamic Resolution讓不同輸入形成可變視覺token數；M-RoPE將時間、高度、寬度位置納入旋轉位置表示，文字使用相應的一維位置處理。小格數為示意；像素預算/處理器限制仍會丟失小字。圖示同標籤批號B08，沒有從模糊B0?補造答案。
來源：https://arxiv.org/abs/2409.12191
生成模式：新建精確SVG→桌機1672×941、手機768×2304 PNG；不編修既有點陣素材。已實看本批原主線的具體工件，保留PCB雙電阻、L支架與雙圓接頭的身份。各家族先原型實看再擴展其他工程；DINOv2/Gemini主反例另統一同件。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

修訂：r01 PNG部分圖形／文字缺畫，SVG節點完整；改用disable-gpu並等字型/500ms繪製。NMS前後尺度一致，YOLOE遮罩覆蓋完整電阻並透明保留料號；DINO遮蔽視圖名稱精確。所有候選仍需逐張原生審查。

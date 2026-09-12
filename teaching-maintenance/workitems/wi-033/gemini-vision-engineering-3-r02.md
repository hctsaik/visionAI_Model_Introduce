# Gemini Vision：格式與內容分開驗
- lesson objective: 版本、請求與回覆都保存，異常欄位交覆核。
- page type: C
- primary reading path: 保留請求版本與固定原圖 → 先驗格式，再查可見內容 → 低可信與缺欄位交人工 → 版本、請求與回覆都保存，異常欄位交覆核。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 版本、請求與回覆都保存，異常欄位交覆核。 #FFF4CC
- major visual nodes:
  1. 保留請求版本與固定原圖；b4-gemini-contract
  2. 先驗格式，再查可見內容；b4-gemini-check
  3. 低可信與缺欄位交人工；b4-vlm-audit

部署時固定可用模型標識、請求設定與schema，記錄服務版本變動和原始回覆。JSON/schema通過只證明格式，仍逐欄對照影像；低可信、拒答、缺欄位及服務失敗都需要可追溯處理。
來源：https://ai.google.dev/gemini-api/docs/structured-output
模式：新精確SVG→1672×941及768×2304PNG；八家族原型已實看通過。三節點、單讀序，保留原有效主線與具體工件身份。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

修訂：工程1專注任務/交付，與工程2機制圖去除整張重複；Gemini使用公開模型識別/schema設定，不暗示私有processor。覆核文字縮短留邊距。更新節點：保留請求版本與固定原圖 → 先驗格式，再查可見內容 → 低可信與缺欄位交人工。PNG審查pending。

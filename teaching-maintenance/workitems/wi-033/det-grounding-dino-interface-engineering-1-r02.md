# Grounding DINO：用詞語指定想找什麼
- lesson objective: 文字可以引導定位，專業料號仍需另驗。
- page type: C
- primary reading path: 同PCB加上resistor查詢 → 詞token與影像區域互動 → 交付詞語相關的框 → 文字可以引導定位，專業料號仍需另驗。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 文字可以引導定位，專業料號仍需另驗。 #FFF4CC
- major visual nodes:
  1. 同PCB加上resistor查詢；b4-ground-input
  2. 詞token與影像區域互動；b4-ground-align
  3. 交付詞語相關的框；b4-ground-output

開放詞彙偵測接受影像與文字，透過兩模態互動和語言引導query定位相關區域；輸出框與詞語相關分數。輸入resistor可說明想找的類別，不能保證辨識103/272的電性或料號。
來源：https://arxiv.org/abs/2303.05499
模式：新精確SVG→1672×941及768×2304PNG；八家族原型已實看通過。三節點、單讀序，保留原有效主線與具體工件身份。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

修訂：工程1專注任務/交付，與工程2機制圖去除整張重複；Gemini使用公開模型識別/schema設定，不暗示私有processor。覆核文字縮短留邊距。更新節點：影像與文字定義想找的類別 → 一個詞語對應兩件物件 → 交付詞語相關的框。PNG審查pending。

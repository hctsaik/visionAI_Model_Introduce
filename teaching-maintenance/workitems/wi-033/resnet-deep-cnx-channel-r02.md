# ConvNeXt：同位置再混通道
- lesson objective: 合併所有通道後，仍有GELU、投影與殘差。
- page type: C
- primary reading path: 固定位置，先看通道69的貢獻 → 同位置的通道9與通道4 → 三項加其餘通道與偏置 → 合併所有通道後，仍有GELU、投影與殘差。
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`
- pale-yellow takeaway: 合併所有通道後，仍有GELU、投影與殘差。 #FFF4CC
- major visual nodes:
  1. 固定位置，先看通道69的貢獻
  2. 同位置的通道9與通道4
  3. 三項加其餘通道與偏置

來源：_course_content/generated-concepts/convnext/convnext-e01-03-channels.svg。沿用本機值；展示前三大貢獻。重排既有SVG的證據區塊；原內嵌場景、實測值與來源保留，不重造實測數字。三主節點手機768×2800，桌機原圖保留。每片依明確viewBox引用既有向量，不改既有PNG。先檢查兩家族原型再擴展。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。

修訂：BN算式放大；跨欄箭頭改由段落間箭頭表達，移除裁切後無目標殘段，圖內數值/圖格不改。解碼器四尺度採2×2排列，完整拼接與結果獨立放大。待實看。

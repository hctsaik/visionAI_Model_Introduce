# WI-029 資料不同，起步方法就不同 r02
- lesson objective: 在同一墊圈缺口檢查任務下，比較正常參考與缺陷標註的資料及輸出責任。
- page type: D — 比較條件與行動差異。
- primary reading path: 同一工作：找墊圈缺口 → 正常參考路線：局部特徵比對 → 缺陷標註路線：學習缺口區域 → 兩路都回原圖覆核與實測
- major visual nodes:
  1. 同一工作：找墊圈缺口
  2. 正常參考路線：局部特徵比對
  3. 缺陷標註路線：學習缺口區域
  4. 兩路都回原圖覆核與實測
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，沿用實體工件、薄藍框及就近證據，不照搬七欄。
- pale-yellow takeaway: #FFF4CC：只有正常品可先找可疑處；要學缺陷輪廓，仍要準備對應標註。
- evidence: 生成教學示意，不是真實模型推論或效能比較。墊圈右側外緣缺口；局部來源與原圖一致。
- generation: built-in imagegen；桌面16:9、手機獨立直向重排。實際PNG與936/326px審查pending；使用者核准pending。
- prompt intent: Four major groups with same steel washer shape (central hole, outer right 3-o'clock V notch on defect specimens). 1 task query defective washer large, label 找右緣缺口. 2 independent route top label 正常參考：PatchCore 範例; multiple INTACT washer reference photos -> blue abstract patch feature bank; query defect washer separately -> feature strip joins bank at local comparison -> orange fuzzy suspicious region at right rim labelled 可疑位置，不是精確輪廓. 3 separate alternative label 缺陷標註：分割模型; intact plus notched training washer photos with matching manual highlight at right notch -> training; new notched query -> compact model -> right notch predicted colored pixels labelled 預測輪廓，仍需核對. Do not connect routes2 and3 sequentially. 4 large original notched washer and localized source crop with two small route outputs side-by-side, label 同測試集核對，保留人工覆核. No good/bad winning performance claim. Visually show extra annotation effort in supervised branch.
- authority: CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md；沿用WI-027全圖重查、分清示意與實測及原圖與特徵。


- correction: r01正常品缺陷標註誤畫中央白孔，特徵庫誤用照片切片，桌面把兩路串接；r02改正常缺陷mask全黑、特徵為抽象向量條、兩路独立、測試影像先編碼再比對。

- correction: 手機正常參考及正常標註影像仍有缺口，填回完整外緣；其他缺陷查詢保留。

# WI-029 先把沒看過的工件，留給最後驗證 r01
- lesson objective: 按實體工件隔離建置、調參與最後測試，避免同工件重拍洩漏。
- page type: C — 追蹤輸入、方法、證據及行動。
- primary reading path: 以實體工件分組 → 建置：學特徵或模型 → 調參：選定並固定門檻 → 最後測試：只驗證不再調
- major visual nodes:
  1. 以實體工件分組
  2. 建置：學特徵或模型
  3. 調參：選定並固定門檻
  4. 最後測試：只驗證不再調
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看，沿用實體工件、薄藍框及就近證據，不照搬七欄。
- pale-yellow takeaway: #FFF4CC：同一工件的重拍留在同一組；最後測試不拿來調門檻。
- evidence: 生成教學示意，不是真實模型推論或效能比較。墊圈右側外緣缺口；局部來源與原圖一致。
- generation: built-in imagegen；桌面16:9、手機獨立直向重排。實際PNG與936/326px審查pending；使用者核准pending。
- prompt intent: Four major groups. 1 trays of top-down steel washers with simple physical ID tags A, B, C. A group has 2 overlapping photos of identical INTACT washer; B group has distinct washer with RIGHT V notch; C group has another washer with RIGHT shallow notch. Include both normal/defect generic specimens in each split where appropriate, do not imply B/C onlydefects. Label 依實體工件分組，重拍不跨組. 2 build folder labelled 建置資料 (A組) showing intact washer photos -> feature/model icon. 3 calibration folder labelled 調參資料 (B組) showing normal AND notched washer beside threshold slider and lock icon, title 固定門檻. 4 final test folder labelled 最後測試 (C組) with different normal AND notched washers, model under locked settings -> original vs suspicious result & audit tick; label 只量錯誤，不再調參. Important division is distinct physicalgroups, NOT sequential movement of samephotos throughtrainandtest; arrows between2/3/4 carry configuration/model only, blue labels 模型 / 固定設定, no backwardsarrow fromfinaltest.
- authority: CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md；沿用WI-027全圖重查、分清示意與實測及原圖與特徵。


- correction: 首區只教同一工件重拍一起分組，後面三組為不同資料夾；移除易誤解的A/B/C實體代號和小型正常判定圖，模型／固定設定箭頭不搬資料。

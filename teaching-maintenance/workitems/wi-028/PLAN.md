# WI-028 時序八课重製

目標：以具體工作影片教清八種方法各自的線索、輸出、準備工作、失敗條件及選型理由。
授權：使用者 2026-09-10 截圖八題；延續 WI-028 記錄的完整交付流程。實作與驗證、自評、使用者核准分開。

- [x] 保存八題來源與16張現版畫面，查第一手來源、實看 GEO-02／GEO-21 參考。
- [x] 18故事核心、反例與共同比較逐圖 brief／preflight；代表原型桌面／手機生成與原生、936／328px實看，自評95／94，使用者核准pending。
- 即將執行：其餘17故事各自桌面／手機PNG生成與逐圖修正，prompt、成品與結果JSON保存在本目錄；不把原型分數套用其他圖。整合與測試未完成。
- [x] Frame Difference、Background Subtraction、Lucas–Kanade、RAFT 桌面／手機圖文。
- [x] ByteTrack、ConvLSTM、VideoMAE、V-JEPA 桌面／手機圖文。
- [x] 整合 topics、learner briefs、model.md，重建 course/docs。
- [x] 逐圖／整頁證據，桌面手機、自測、放大、HTTP／資產一致與必要回歸。
- [ ] 學習回寫、保存副本、Git／公開版本核對。

## Checkpoint
- 最後完成：核對技能與適用規範，Git 工作目錄乾淨。
- 即將執行：保存基準、來源調查與逐圖設計；產物放在本目錄。
- 實際驗證：尚未跑本輪測試；生成未開始，無本輪生成程序；使用者核准 pending。
- 下一步：先讀取八題現有 JSON 及前輪整合／驗證介面，保存可恢复來源。
- 新checkpoint：16張基準完成；首圖r01已生成及實看，輸入位移與差分重疊不符，判需修訂，不評達標。即將r02及手機原型；未整合／測試。Browser discovery=[]，已讀troubleshooting，基準以本機Playwright完成。

## Active checkpoint — 36 final assets integrated
- [x] Eight lesson texts, 18 story pairs (36 PNG), native and display-size visual review.
- [x] Eight topic JSON, learner briefs and model Markdown integrated; exact PNG dimensions added to strict validator.
- In progress: HTML build process; UI/HTTP tests not yet run. Next: complete sequential course/docs build then 48 page states and final-page reading checks.
- Preflight batch glob also accidentally included two review logs, which failed missing-objective as expected; all 31 actual briefs passed. Review logs are not preflights.
- Final assets: selected-assets.json; evidence: image-review.md; user approval pending.

## Release checkpoint
- Completed: 36 PNG, eight lesson integrations and self-reviews; 48 UI states, 144 zooms, 16 final states, 72 HTTP hashes and 1292 bundle hashes. Focused tests passed; legacy ChArUco schema failure recorded as pre-existing, not a pass.
- In progress: rebuilding metadata status, snapshotting durable sources, commit/push and public verification. User review pending; not model inference.

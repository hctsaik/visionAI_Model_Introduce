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
- [x] 學習回寫、保存副本、Git／公開版本核對。

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

## Published-source checkpoint
- Content commit ca7254653d5f025617fff1885132063328adf67a pushed successfully.
- GitHub Pages run 34494424414 in progress. First public check returned previous HTML; this is not a pass. Await deployment completion before retrying public hashes.
- scope-verification.json confirms exactly the requested eight topics changed; other 50, including ChArUco, are identical to baseline.


## WI-028 完成紀錄 — 八個時序 Topic
- [x] Frame Difference、Background Subtraction、Lucas–Kanade、RAFT、ByteTrack、ConvLSTM、VideoMAE、V-JEPA 圖文已製作並公開。
- [x] 18個故事、36張桌機／手機PNG；每課核心、反例、比較、自測與操作卡；來源與生成提示、修正紀錄、逐圖及整頁分項自評均落盤。
- [x] 48頁面狀態／144次圖片放大Escape、自測導覽、16閱讀狀態、72本機HTTP圖片hash、1292引用資產及HTML一致；聚焦pytest 7 tests+4 subtests及bundle 1 test通過。
- [x] ca7254653d5f025617fff1885132063328adf67a 已推送；Pages run34494424414成功；公開HTML與36PNG hash符合成品。首次部署前舊HTML檢查失敗保留為歷史，完成後重查通過。
- 範圍確認：僅八課改動，其他50課相同。全站legacy verifier既有ChArUco inline schema失敗仍存在，未算通過；原工程圖未納入這輪首讀評分。
- 啟用：selected-assets.json；實證：image-review.md、page-review.md、validation-summary.json、scope-verification.json、public-release-verification.json。公開入口 https://hctsaik.github.io/visionAI_Model_Introduce/#view=lesson&lesson=frame-difference&slide=1 。
- 使用者成品核准：pending。圖像為教學示意，無模型推論／現場效能或真人學習測試。下一步僅依使用者成品回饋開新修訂，保留本輪版本與證據。

## WI-042 ????????2026-09-13?

?????????????????????? [authoring](workitems/wi-042/authoring/)?????? [REPORT](workitems/wi-042/REPORT.md) ? [PLAN](workitems/wi-042/PLAN.md)?WI-041 ??????????????????????????checkpoint?????????????

?????????????????????????????????authoring????????????WI-042??????????????????update-verifier.py???PNG??docs????????

## WI-033 第二部分52課本機完成（2026-09-12）

[報告](workitems/wi-033/REPORT.md)、[逐圖資產](workitems/wi-033/final-selected-assets.json)、[全52課驗證](workitems/wi-033/verification-all52.json)及[維護核對](workitems/wi-033/maintenance-verification.json)保存第二部分成果。52課208組工程故事、指定主線／深讀修正，共460張新啟用PNG；使用者核准pending，尚未commit/push或發布。

維護副本保存原生SVG、版本preflight、審查/失敗/驗證紀錄、生成與整合程式、頁面JSON/文字、基準來源及52課authoring。啟用PNG位於docs，完整頁面截圖和歷史PNG仍在本機workitems/wi-033；不是整個工作區備份。從PLAN核對現行引用後接續，不直接重跑舊生成器。根Markdown與已安裝skill仍為編輯權威。

## WI-032 發布完成（2026-09-11）

第一部分六課成果已 commit 並 push：2e218926e2ff5d1a8d21ca5cb7bbe381fde27819；GitHub Pages 部署成功，公開 93 個檔案逐一 hash 與已提交內容一致（本機部分 Markdown 為 CRLF，Git 為 LF，文字內容一致）。發布證據為 workitems/wi-032/public-release-verification.json。最新學習及接續資料同步保存在 Git 的 teaching-maintenance。使用者成品核准仍 pending；第二部分 52 課未開始，下次依根 Overall_Review.md 第二部分接續。此段取代下方歷史未發布狀態。

## WI-032：Overall Review第一部分（本機完成、未發布）

[總計畫](project/Overall_Review.md)將58課分成6課重建與52課局部修正；前6課已完成主線、工程層、手機圖、自測與交付。[報告](workitems/wi-032/REPORT.md)、[學習](project/TEACHING_REVIEW_LOG.md)、[驗證](workitems/wi-032/final-verification.json)與全部brief已保存。使用者核准pending。

authoring保存六課來源與builder／測試；native保存64個選定SVG，baseline保存22份改前來源。啟用PNG在docs對應路徑；原型、截圖與失敗稿的完整本機紀錄在專案workitems/wi-032。快照內報告的本機相對截圖／頁面連結需回到原工作項目查看；本資料夾不宣稱包含所有歷史圖片。不要重跑製作脚本覆蓋最終版本，先從PLAN及啟用manifest核對接續狀態。

# Teaching maintenance snapshots

## Local audit: WI-031 (2026-09-11)

All 58 topics were re-audited, including engineering figures and five sets of eight advanced chapters: 0 fully compliant, 52 targeted revisions, 6 main-story rebuilds. This is a diagnostic audit, not a new production release or per-asset numeric scoring.

The [full audit report](../workitems/wi-031/REPORT.md), 58-row results, screenshots and verification remain in the local authoring workspace. They are not included in this preservation snapshot or the published site; the relative report link requires that workspace. Current reusable learning is synchronized in `project/`. WI-030 below remains the latest production snapshot.

## Latest production: WI-030

Twelve lessons were rebuilt: PatchCore, PaDiM, AnomalyDINO, EfficientAD,
ResNet, ConvNeXt, ViT, U-Net, SegFormer, YOLO-Seg, Keypoint R-CNN and Pose Pipeline.
The 42 PNGs cover 21 distinct stories. Each lesson has a core mechanism,
failure case, comparison, conditional self-check and practical handoff guidance.
Five existing advanced chapter sets are preserved behind an opt-in collapsed entry.

Resume from [the workitem plan](workitems/wi-030/PLAN.md).
[Validation](workitems/wi-030/validation-summary.json),
[individual image reviews](workitems/wi-030/image-review.md) and
[page reviews](workitems/wi-030/page-review.md) separate author assessment,
tool checks and pending user acceptance. The existing unrelated ChArUco
legacy-verifier failure is recorded explicitly.

`workitems/wi-030/authoring/` preserves the changed topic sources, model Markdown,
learner briefs, builders, focused tests and generation/integration scripts.
Versioned prompts and preflights are alongside the plan; final PNGs are in `docs/`.
Original rejected PNGs and full browser screenshots remain in the local workspace.
This is a continuation snapshot, not a complete backup of every authoring asset.

## WI-027 scope

Seven foundation and vision-language lessons were rebuilt with 30 desktop/mobile PNGs, three first-read stories per lesson, explanations, comparisons, self-checks and operating cards. `workitems/wi-027/` preserves selected assets, versioned briefs, generation intentions, source references and individual image/page assessments. Validation covers 42 interaction states, 126 image zoom checks, 14 final page states, 60 local HTTP hashes and five regression tests. User review remains pending; illustrations are not model measurements.

The clean Pages bundle omits unused historical assets; the authoring copies remain local. These snapshots preserve reusable Markdown learning and review evidence, not the complete authoring workspace or rejected image drafts.

This directory versions the shared teaching lessons and reusable skill. It is
outside `docs/` and is not part of the GitHub Pages payload.

## Sources and editing

- `project/`: copies of `IMAGE_STYLE_GUIDE.md`, `TEACHING_REVIEW_LOG.md`,
  `TEACHING_SCORING_RUBRIC.md`, and `TEACHING_WEBPAGE_GUIDE.md` from the
  visionAI workspace root (`C:/code/claude/visionAI` on the authoring machine).
- `skills/teaching-review-cycle/`: complete installed skill from
  `C:/Users/hctsa/.codex/skills/teaching-review-cycle`.
- `manifest.json`: source locations and SHA-256 hashes at synchronization.
- `workitems/wi-024/`: image/page self-assessments and the final local release
  audit for the four supplied detector lessons. The PNGs are published in `docs/`.

The original workspace files and installed skill remain the editing authorities.
These are preservation copies, not a second independently maintained review log.
After editing the authorities, synchronize the corresponding copies, validate the
skill, inspect the diff, and commit the snapshot and manifest together. Do not
copy credentials, caches, or unrelated installed skills into this directory.

## Restore

On another machine, first compare any existing files and preserve local changes.
Copy the four files in `project/` to the destination visionAI workspace root.
Copy `skills/teaching-review-cycle/` to the destination Codex skills directory.
The paths in `references/visionai.md` are historical location hints; adapt them
to the new workspace. Validate the restored skill with the local skill-creator
`scripts/quick_validate.py` when available.

Historical links in the review log can refer to authoring assets and local
evidence that are not included here. This snapshot preserves the rules and
learning record; it is not a complete backup of the course authoring workspace.

## WI-023 scope

- Preserve the WI-021 learning formalized in WI-022 without changing rubric weights.
- Include all five files of the review skill so its relative references resolve.
- Validate snapshot/source hashes and skill format before committing.
- Verify the pushed commit against `origin/main`; record the result in workspace
  `WORKITEMS.md`. Git history is the authoritative snapshot revision.

## WI-024 scope

- Rebuild the four supplied lessons with 20 distinct desktop/mobile PNGs.
- Preserve operation geometry, separate alternative modes from sequential steps,
  and verify the actual rendered summary fields.
- Sync the four authority Markdown files, complete review skill, and three audit
  records. Original generation prompts, rejected drafts, authoring scripts and
  full browser screenshots remain in the local workspace; this is not a full
  authoring backup. User acceptance and the two unspecified lessons remain pending.

## WI-026 scope

- Publish eight generation/restoration lessons with 38 desktop/mobile PNGs.
- Preserve five local validation and assessment reports in `workitems/wi-026/`,
  plus the updated shared teaching rules and review log. Reports describe the
  pre-publication checks; Git and Pages deployment are verified separately.
- Original prompts, authoring sources, rejected drafts and browser screenshots
  remain in the local workspace. User acceptance remains separate from publishing.

## WI-029 scope

- Rebuild foundations and production around six work cases, with twelve independently reviewed desktop/mobile PNGs, Markdown-driven copy, self-checks and a traceable hypothetical workload comparison.
- Preserve the Markdown sources, source list, image manifest, UI fragments, parser, builders, tests, briefs, generation intent and review/validation reports in `workitems/wi-029/`. The `authoring/` subtree mirrors course-root paths; restore those paths into an existing authoring workspace. Published PNGs live in `docs/`.
- These additions preserve the changed authoring components, not the entire course source tree. Rejected images and browser screenshots remain local. Existing historical workitem snapshots are retained as dated checkpoints; shared `project/` files contain current learning.
- User acceptance remains separate from self-review and technical verification. Publication evidence follows the content commit.

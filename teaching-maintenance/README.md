# Teaching maintenance snapshots

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

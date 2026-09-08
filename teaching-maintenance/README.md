# Teaching maintenance snapshots

This directory versions the WI-022 teaching lessons and reusable skill. It is
outside `docs/` and is not part of the GitHub Pages payload.

## Sources and editing

- `project/`: copies of `IMAGE_STYLE_GUIDE.md`, `TEACHING_REVIEW_LOG.md`,
  `TEACHING_SCORING_RUBRIC.md`, and `TEACHING_WEBPAGE_GUIDE.md` from the
  visionAI workspace root (`C:/code/claude/visionAI` on the authoring machine).
- `skills/teaching-review-cycle/`: complete installed skill from
  `C:/Users/hctsa/.codex/skills/teaching-review-cycle`.
- `manifest.json`: source locations and SHA-256 hashes at synchronization.

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

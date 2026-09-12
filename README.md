# Vision AI Model Introduce

Interactive Traditional-Chinese course for selecting, understanding, and
operationally validating Vision AI model families.

The published site is a self-contained GitHub Pages bundle under `docs/`.
After pushing to GitHub, enable **Settings → Pages → Deploy from a branch** and
choose `main` with the `/docs` folder. The site URL will be:

`https://hctsaik.github.io/visionAI_Model_Introduce/`

## Update the published site

This repository is the deployable static snapshot. Regenerate the `docs/`
bundle from the full course workspace, then replace and commit `docs/` here.
The bundle contains `interactive-learning.html` as `docs/index.html` and the
visual assets and lesson documents it references. It intentionally excludes local browser
caches, prompt intermediates, raw image-generation material, and presentation
source files.

The latest revision (WI-035) adds a three-step PoC workbench with model-specific
guidance, draft progress, editable previews, Markdown export, and protected
example imports. It also corrects mechanism text in 19 lessons and detector
selection summaries. See [the change report](teaching-maintenance/workitems/wi-035/REPORT.md)
and [reusable teaching lessons](teaching-maintenance/project/TEACHING_WEBPAGE_GUIDE.md).
Draft completeness indicates filled fields, not validated model performance.

An earlier teaching revision (WI-030) rebuilds four anomaly-detection lessons
and eight classification, segmentation and pose lessons with 42 distinct
desktop/mobile PNG illustrations, conditional self-checks and operating guidance.
These are instructional illustrations, not measured model inference results.
The original engineering reference diagrams remain available in their folded sections.
The bundle also includes every lesson's linked model and image-manifest Markdown.

Teaching rules and the reusable review skill are versioned in
[teaching-maintenance](teaching-maintenance/README.md), with their source and
restore instructions. These maintenance snapshots are separate from the Pages bundle.

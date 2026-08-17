# Vision AI Model Introduce

Interactive Traditional-Chinese course for selecting, understanding, and
operationally validating Vision AI model families.

The published site is a self-contained GitHub Pages bundle under `docs/`.
After pushing to GitHub, enable **Settings → Pages → Deploy from a branch** and
choose `main` with the `/docs` folder. The site URL will be:

`https://hctsaik.github.io/visionAI_Model_Introduce/`

## Update the published site

In the full course workspace, rebuild the lesson and Pages bundle:

```powershell
python tools/build_interactive_learning_html.py
python tools/build_github_pages_site.py --clean
```

The bundle only contains `interactive-learning.html` as `docs/index.html` and
the 1,114 image assets it references. It intentionally excludes local browser
caches, prompt intermediates, raw image-generation material, and presentation
source files.

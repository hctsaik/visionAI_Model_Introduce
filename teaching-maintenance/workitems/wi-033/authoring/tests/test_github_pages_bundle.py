from __future__ import annotations

import importlib.util
import json
import re
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILDER_PATH = ROOT / "tools" / "build_github_pages_site.py"
SPEC = importlib.util.spec_from_file_location("github_pages_builder", BUILDER_PATH)
assert SPEC and SPEC.loader
BUILDER = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BUILDER
SPEC.loader.exec_module(BUILDER)


class GitHubPagesBundleTests(unittest.TestCase):
    def test_handoff_documents_requested_by_lesson_links_ship_with_identical_content(self) -> None:
        html = BUILDER.SOURCE_HTML.read_text(encoding="utf-8")
        data = json.loads(re.search(r'<script id="course-data" type="application/json">(.*?)</script>', html, re.S)[1])
        assets = set(BUILDER.referenced_assets(html))
        for topic in data['topics']:
            for key in ('modelPath', 'manifestPath'):
                document = Path(topic[key])
                with self.subTest(topic=topic['id'], link=key):
                    self.assertIn(document, assets)
                    self.assertEqual((ROOT / document).read_bytes(), (ROOT / 'docs' / document).read_bytes())

    def test_every_referenced_static_asset_is_available_for_deployment(self) -> None:
        assets = BUILDER.referenced_assets(BUILDER.SOURCE_HTML.read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(assets), 1186)
        topic = json.loads((ROOT / '_course_content/topics/ad-anomalydino.json').read_text(encoding='utf-8'))
        expected = {Path(view[key]) for chapter in topic['deep_dive']['chapters']
                    for view in chapter.get('reading_views', []) for key in ('image', 'mobile_image')}
        self.assertTrue(expected.issubset(set(assets)), 'Every selectable/mobile view must ship in the bundle')
        self.assertTrue(all((ROOT / asset).is_file() for asset in assets))


if __name__ == "__main__":
    unittest.main()

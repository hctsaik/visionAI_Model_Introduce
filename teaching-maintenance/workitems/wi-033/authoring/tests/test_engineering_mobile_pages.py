"""Authored engineering metadata survives validation without weakening legacy routes."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import build_interactive_learning_html as builder


class EngineeringMobileTests(unittest.TestCase):
    def setUp(self):
        self.pages = json.loads((ROOT / '_course_content/topics/charuco.json').read_text(encoding='utf-8'))['engineering_slides']

    def test_mobile_source_survives_and_manifest_owns_desktop(self):
        pages = builder._clean_engineering_slides(self.pages, 'test')
        result = builder.page_payload({}, {}, 0, ('manifest.png', 'active/manifest.png'), {'engineering_slides': pages})
        self.assertEqual(result['image'], 'active/manifest.png')
        self.assertEqual(result['mobileImage'], self.pages[0]['mobile_image'])
        self.assertEqual(result['mobileHeight'], 2770)
        self.assertEqual(result['plain'], self.pages[0]['plain'])

    def test_missing_page_wrong_dimensions_and_unsafe_path_rejected(self):
        with self.assertRaises(ValueError):
            builder._clean_engineering_slides(self.pages[:3], 'test')
        for field, value in [('mobile_width', 999), ('mobile_height', '2770'), ('mobile_image', '../outside.png'), ('mobile_image', 'https://example.com/img.png')]:
            pages = copy.deepcopy(self.pages); pages[0][field] = value
            with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                builder._clean_engineering_slides(pages, 'test')

    def test_missing_meaningful_stage_rejected(self):
        pages = copy.deepcopy(self.pages); pages[0]['stages'][0]['body'] = ''
        with self.assertRaises(ValueError):
            builder._clean_engineering_slides(pages, 'test')


if __name__ == '__main__':
    unittest.main()

"""The explicitly supported mobile canvas must not relax crop/path validation."""
import sys
import tempfile
import unittest
from pathlib import Path
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from build_interactive_learning_html import _validate_concept_visual_asset

class TallMobileArtworkTests(unittest.TestCase):
    def test_native_mobile_canvas_and_invalid_neighbor(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'image.png'
            for size in ((724, 2171), (724, 2172), (861, 1827), (725, 2167), (725, 2169), (725, 2170), (727, 2164), (728, 2161), (726, 2167), (1672, 940), (1673, 940), (768, 2046), (768, 2048), (881, 1785), (887, 1774), (955, 1647), (1024, 1536)):
                Image.new('RGB', size, 'white').save(path)
                _validate_concept_visual_asset(path)
            Image.new('RGB', (724, 2173), 'white').save(path)
            with self.assertRaises(ValueError):
                _validate_concept_visual_asset(path)

if __name__ == '__main__':
    unittest.main()

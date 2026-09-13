from pathlib import Path
import copy
import importlib.util
import tempfile
import unittest
from unittest.mock import patch
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('release_verifier',ROOT/'tools/verify_interactive_learning_html.py')
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)

class ReleaseVerifierTests(unittest.TestCase):
    def test_native_mobile_dimensions_must_match_declared_size(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'roadmap-model-selection').mkdir()
            rel='roadmap-model-selection/mobile.png'
            Image.new('RGB',(768,2770)).save(root/rel)
            v.verify_asset(root/'index.html',rel,'roadmap-model-selection/',(768,2770))
            with self.assertRaisesRegex(ValueError,'dimensions'):
                v.verify_asset(root/'index.html',rel,'roadmap-model-selection/',(768,2304))

    def test_unsafe_and_missing_assets_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            html=Path(tmp)/'index.html'
            for rel in ['../outside.png','_course_content/../../outside.png','C:/outside.png','_course_content\\outside.png']:
                with self.subTest(path=rel),self.assertRaises(ValueError):v.checked_local_path(html,rel)
            with self.assertRaises(FileNotFoundError):
                v.verify_asset(html,'roadmap-model-selection/missing.png','roadmap-model-selection/')

    def test_wrong_native_dimensions_and_invalid_svg_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);p=root/'_course_content/generated-concepts';p.mkdir(parents=True)
            Image.new('RGB',(20,20)).save(p/'bad.png')
            with self.assertRaisesRegex(ValueError,'dimensions'):
                v.verify_concept_asset(root/'index.html','_course_content/generated-concepts/bad.png')
            (p/'bad.svg').write_text('<svg width="1672" height="941" viewBox="0 0 1672 941"><broken>',encoding='utf8')
            with self.assertRaisesRegex(ValueError,'Invalid concept SVG'):
                v.verify_concept_asset(root/'index.html','_course_content/generated-concepts/bad.svg')

    def test_corrupted_embedded_contract_is_not_accepted(self):
        data=v.embedded_course_data((ROOT/'interactive-learning.html').read_text(encoding='utf8'))
        mutations=[('display',lambda d:d['topics'][0]['teachingStory']['inline_visuals'][0].update(display='unknown')),
                   ('diagram',lambda d:d['topics'][0]['teachingStory']['mechanism_steps'][0].pop('diagram'))]
        for name,mutate in mutations:
            broken=copy.deepcopy(data);mutate(broken)
            with self.subTest(name=name),patch.object(v,'embedded_course_data',return_value=broken),self.assertRaises(ValueError):
                v.validate(ROOT/'interactive-learning.html')

    def test_current_poc_hooks_are_required(self):
        text=(ROOT/'interactive-learning.html').read_text(encoding='utf8')
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'index.html';p.write_text(text.replace('parseProgressBackup','missingBackupParser'),encoding='utf8')
            with self.assertRaisesRegex(ValueError,'parseProgressBackup'):v.validate(p)

    def test_mobile_crop_uses_its_canvas_and_rejects_out_of_bounds(self):
        v.verify_crop([0,0,768,2770],(768,2770),'native mobile')
        v.verify_crop([1258,280,360,465],(1672,941),'legacy mobile step')
        for crop in [[0,0,769,2770],[-1,0,100,100],[0,0,100,2771],[0,0,0,200],[True,0,10,10]]:
            with self.subTest(crop=crop),self.assertRaises(ValueError):
                v.verify_crop(crop,(768,2770),'native mobile')

if __name__=='__main__':unittest.main()

"""Reviewed comparisons may be shared; accidental model aliases still fail."""
import importlib.util,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('detector_verifier',R/'tools/verify_interactive_learning_html.py')
V=importlib.util.module_from_spec(spec);spec.loader.exec_module(V)

class DetectorComparisonSharingTest(unittest.TestCase):
 def test_two_six_topic_comparisons_and_original_alias_are_allowed(self):
  for base in [R,R/'docs']:
   assets=[]
   for kind in ['known','prompt']:
    p=(base/f'_course_content/generated-concepts/det-yolo-dense/det-yolo-dense-d01-compare-{kind}.svg').resolve()
    assets.extend([p]*6)
   assets.extend([(base/'unique.svg').resolve()]*2)
   V.verify_concept_reference_counts(base/'index.html',assets,14)
 def test_unreviewed_repeated_model_image_is_rejected(self):
  with self.assertRaises(ValueError):V.verify_concept_reference_counts(R/'index.html',[R/'alias.svg']*3,3)
 def test_incomplete_detector_family_sharing_is_rejected(self):
  p=(R/'_course_content/generated-concepts/det-yolo-dense/det-yolo-dense-d01-compare-known.svg').resolve()
  with self.assertRaises(ValueError):V.verify_concept_reference_counts(R/'index.html',[p]*2,2)
 def test_missing_reference_is_rejected(self):
  with self.assertRaises(ValueError):V.verify_concept_reference_counts(R/'index.html',[R/'one.svg'],2)

if __name__=='__main__':unittest.main()

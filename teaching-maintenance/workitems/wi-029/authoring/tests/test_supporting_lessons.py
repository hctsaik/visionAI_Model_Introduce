import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from supporting_lessons import parse_lesson

ROOT = Path(__file__).resolve().parents[1]

class SupportingLessonsTests(unittest.TestCase):
    def test_both_markdown_lessons_have_visible_decisions_and_exercises(self):
        for view in ('foundations', 'production'):
            lesson = parse_lesson((ROOT / f'_course_content/supporting-lessons/{view}.md').read_text(encoding='utf-8'))
            self.assertEqual(len(lesson['chapters']), 3)
            for chapter in lesson['chapters']:
                self.assertGreater(len(chapter['tradeoff']), 50)
                self.assertGreater(len(chapter['answer']), 50)

    def test_missing_answer_or_duplicate_chapter_cannot_silently_publish(self):
        source = (ROOT / '_course_content/supporting-lessons/foundations.md').read_text(encoding='utf-8')
        with self.assertRaises(ValueError):
            parse_lesson(source.replace('### 解析', '### 備註', 1))
        with self.assertRaises(ValueError):
            parse_lesson(source.replace('## fdn-data |', '## fdn-visible |'))

if __name__ == '__main__':
    unittest.main()
def test_cli_renders_supporting_lessons(tmp_path):
    import subprocess
    import sys
    from pathlib import Path
    root = Path(__file__).resolve().parents[1]
    output = tmp_path / 'course.html'
    subprocess.run([sys.executable, str(root / 'tools/build_interactive_learning_html.py'), '--output', str(output)], check=True, capture_output=True)
    html = output.read_text(encoding='utf-8')
    assert '__WORKPLACE_' not in html
    assert 'function workplaceLessonHTML(view)' in html
    assert 'workplace-figure' in html

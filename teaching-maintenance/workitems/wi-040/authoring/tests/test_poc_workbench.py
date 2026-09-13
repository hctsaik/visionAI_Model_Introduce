"""Demand-led PoC journeys in a real browser, with isolated persisted state."""
from pathlib import Path
import json
import os
import unittest
from playwright.sync_api import sync_playwright

BASE = os.environ.get('VISIONAI_TEST_URL', 'http://127.0.0.1:8000/docs/index.html')
KEY = 'vision-ai-model-selection-learning-v1'
CASES = [
    ('normal', dict(task='defect', defectKind='novel', detail='location', visibility='clear', data='normal'), '正常'),
    ('fixed', dict(task='count', placement='fixed', visibility='clear', data='normal'), '逐格'),
    ('instances', dict(task='contour', separation='each', overlap='touching', visibility='clear', data='masks'), '輪廓'),
    ('millimetres', dict(task='measure', unit='mm', plane='planar', calibration='none', visibility='clear', data='few'), '尺寸'),
    ('text', dict(task='text', textGoal='transcribe', visibility='clear', data='few'), '文字'),
    ('poor_image', dict(task='defect', defectKind='novel', detail='location', visibility='poor', data='normal'), '取像'),
]


class PocWorkbenchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pw = sync_playwright().start()
        cls.browser = cls.pw.chromium.launch(channel='msedge', headless=True)

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.pw.stop()

    def setUp(self):
        self.context = self.browser.new_context(viewport={'width': 1440, 'height': 1000}, accept_downloads=True)
        self.page = self.context.new_page()
        self.errors = []
        self.page.on('pageerror', lambda error: self.errors.append(str(error)))

    def tearDown(self):
        self.context.close()
        self.assertEqual(self.errors, [])

    def open(self):
        self.page.goto(BASE + '#view=poc')
        self.page.locator('#poc-answer').wait_for(state='visible')

    def click(self, action):
        self.page.locator(f'[data-action="{action}"]:visible').first.click()

    def saved(self):
        return self.page.evaluate('(key)=>JSON.parse(localStorage.getItem(key))', KEY)

    def answer(self, question, value):
        select = self.page.locator('#poc-answer')
        self.assertEqual(select.get_attribute('data-poc-answer'), question)
        select.select_option(value)
        self.assertEqual(self.page.locator('#poc-answer').get_attribute('data-poc-answer'), question,
                         'Selecting an option must not advance without Continue')
        self.click('poc-next')

    def finish(self, answers):
        visited = []
        for _ in range(15):
            select = self.page.locator('#poc-answer:visible')
            if not select.count():
                break
            question = select.get_attribute('data-poc-answer')
            self.assertNotIn(question, visited, 'A confirmed question repeated')
            self.assertIn(question, answers, 'Unexpected branch requires explicit assessment')
            self.assertEqual(self.page.locator('textarea:visible').count(), 0)
            self.assertEqual(self.page.locator('#poc-model').count(), 0)
            visited.append(question)
            self.answer(question, answers[question])
        else:
            self.fail('Journey never reached a result')
        self.assertTrue(self.page.locator('#poc-result').is_visible())
        return visited

    def backup(self):
        details = self.page.locator('.poc-backup:not(#poc-legacy)')
        if details.get_attribute('open') is None:
            details.locator('summary').click()

    def test_six_demand_scenarios_without_model_or_free_text(self):
        for name, answers, expected in CASES:
            with self.subTest(name=name):
                self.page.goto(BASE)
                self.page.evaluate('(key)=>localStorage.removeItem(key)', KEY)
                self.page.reload()
                self.open()
                self.finish(answers)
                self.assertIn(expected, self.page.locator('#poc-result').inner_text())
                self.assertEqual(self.page.locator('#poc-model').count(), 0)
                self.click('poc-preview')
                self.assertTrue(self.page.locator('#poc-preview').is_visible())

    def test_generation_does_not_require_existing_image(self):
        self.open()
        visited = self.finish(dict(task='generate', generationUse='display'))
        self.assertEqual(visited, ['task', 'generationUse'])

    def test_unknown_answer_provides_next_step(self):
        self.open()
        self.finish(dict(task='unknown'))
        self.assertGreater(len(self.page.locator('#poc-result').inner_text()), 50)

    def test_backtracking_invalidates_confirmation_and_recomputes_result(self):
        self.open()
        self.finish(CASES[1][1])
        before = self.page.locator('#poc-result').inner_text()
        self.page.locator('[data-action="poc-edit"][data-question="placement"]').click()
        self.answer('placement', 'free')
        self.assertNotIn('data', self.saved()['poc']['_flow']['confirmed'])
        self.finish(dict(visibility='clear', data='normal'))
        after = self.page.locator('#poc-result').inner_text()
        self.assertNotEqual(before, after)
        self.assertNotIn('逐格', self.page.locator('#poc-result h2').first.inner_text())

    def test_reload_restores_confirmed_answers_and_current_question(self):
        self.open()
        self.answer('task', 'count')
        self.page.locator('#poc-answer').select_option('fixed')
        self.page.reload()
        self.page.locator('#poc-answer').wait_for()
        self.assertEqual(self.page.locator('#poc-answer').get_attribute('data-poc-answer'), 'placement')
        self.assertEqual(self.page.locator('#poc-answer').input_value(), 'fixed')
        self.assertIn('task', self.saved()['poc']['_flow']['confirmed'])
        self.assertNotIn('placement', self.saved()['poc']['_flow']['confirmed'])

    def test_legacy_draft_preserved_during_new_journey(self):
        legacy = {'task': '既有自由文字', 'output': '舊版輸出', 'model': 'det-dino-detector', '_notes': {'task': '現場原始補充'}}
        self.page.goto(BASE)
        self.page.evaluate('([key,poc])=>localStorage.setItem(key,JSON.stringify({poc}))', [KEY, legacy])
        self.page.reload()
        self.open()
        self.assertTrue(self.page.locator('#poc-legacy').count())
        self.page.locator('#poc-legacy summary').click()
        self.assertIn('既有自由文字', self.page.locator('#poc-legacy').inner_text())
        self.finish(CASES[1][1])
        for key, value in legacy.items():
            self.assertEqual(self.saved()['poc'][key], value)
        self.backup()
        with self.page.expect_download() as download:
            self.click('export-progress')
        exported = json.loads(Path(download.value.path()).read_text(encoding='utf8'))
        for key, value in legacy.items():
            self.assertEqual(exported['poc'][key], value)

    def test_markdown_contains_result_and_print_preview(self):
        self.open()
        self.finish(CASES[3][1])
        self.click('poc-preview')
        with self.page.expect_download() as download:
            self.click('export-poc-markdown')
        text = Path(download.value.path()).read_text(encoding='utf8')
        self.assertIn('尺寸', text)
        self.assertIn('校正', text)
        self.page.emulate_media(media='print')
        self.assertTrue(self.page.locator('#poc-preview').is_visible())

    def test_json_roundtrip_preserves_branch_answers(self):
        self.open()
        self.answer('task', 'count')
        self.answer('placement', 'fixed')
        expected = self.saved()['poc']['_flow']
        self.backup()
        with self.page.expect_download() as download:
            self.click('export-progress')
        path = download.value.path()
        self.page.locator('[data-action="poc-edit"][data-question="task"]').first.click()
        self.answer('task', 'generate')
        self.backup()
        self.page.once('dialog', lambda dialog: dialog.accept())
        self.page.locator('#import-progress').set_input_files(path)
        self.page.wait_for_function('(key)=>JSON.parse(localStorage.getItem(key)).poc._flow.answers.task==="count"', arg=KEY)
        self.assertEqual(self.saved()['poc']['_flow'], expected)

    def test_reset_and_undo_preserve_learning(self):
        self.open()
        self.answer('task', 'count')
        before = self.saved()['poc']
        self.page.evaluate('(key)=>{const d=JSON.parse(localStorage.getItem(key));d.completed.resnet=true;localStorage.setItem(key,JSON.stringify(d));}', KEY)
        self.page.reload()
        self.backup()
        self.page.once('dialog', lambda dialog: dialog.accept())
        self.click('poc-reset')
        self.assertTrue(self.saved()['completed']['resnet'])
        self.assertFalse(self.saved()['poc'].get('_flow', {}).get('confirmed', []))
        self.click('poc-undo')
        self.assertEqual(self.saved()['poc'], before)

    def test_example_cancel_and_undo(self):
        self.open()
        self.answer('task', 'generate')
        before = self.saved()['poc']
        self.page.once('dialog', lambda dialog: dialog.dismiss())
        self.click('fill-poc-example')
        self.assertEqual(self.saved()['poc'], before)
        self.page.once('dialog', lambda dialog: dialog.accept())
        self.click('fill-poc-example')
        self.assertNotEqual(self.saved()['poc']['_flow']['answers'], before['_flow']['answers'])
        self.click('poc-undo')
        self.assertEqual(self.saved()['poc'], before)

    def test_storage_failure_is_visible(self):
        self.page.add_init_script("Storage.prototype.setItem=function(){throw new Error('quota')}")
        self.open()
        self.page.locator('#poc-answer').select_option('count')
        self.assertIn('無法儲存', self.page.locator('#poc-status').inner_text())

    def test_mobile_keyboard_and_no_horizontal_overflow(self):
        self.page.set_viewport_size({'width': 390, 'height': 844})
        self.open()
        self.page.locator('#poc-answer').focus()
        self.page.keyboard.press('ArrowDown')
        self.page.keyboard.press('Enter')
        self.assertEqual(self.page.locator('#poc-answer').get_attribute('data-poc-answer'), 'task')
        answers = CASES[2][1]
        for _ in range(15):
            self.assertLessEqual(self.page.evaluate('document.documentElement.scrollWidth'), 390)
            select = self.page.locator('#poc-answer:visible')
            if not select.count():
                break
            question = select.get_attribute('data-poc-answer')
            self.answer(question, answers[question])
        self.assertTrue(self.page.locator('#poc-result').is_visible())
        self.click('poc-preview')
        self.assertLessEqual(self.page.evaluate('document.documentElement.scrollWidth'), 390)

    def test_lesson_handoff_keeps_candidate_as_context(self):
        self.open()
        legacy = {'task':'原任務', 'model':'resnet', 'output':'原輸出不可覆寫'}
        self.page.evaluate('([key,poc])=>{const d=JSON.parse(localStorage.getItem(key))||{};d.poc=poc;localStorage.setItem(key,JSON.stringify(d));}', [KEY, legacy])
        self.page.reload()
        self.page.goto(BASE + '#view=lesson&lesson=det-dino-detector')
        self.page.locator('[data-action="send-to-poc"]').click()
        self.page.locator('#poc-answer').wait_for()
        self.assertEqual(self.page.locator('#poc-model').count(), 0)
        self.assertEqual(self.saved()['poc']['_courseNotes'][0]['id'], 'det-dino-detector')
        self.page.reload()
        for key,value in legacy.items():
            self.assertEqual(self.saved()['poc'][key],value)
        self.assertEqual(self.page.locator('#poc-answer').get_attribute('data-poc-answer'), 'task')


if __name__ == '__main__':
    unittest.main()

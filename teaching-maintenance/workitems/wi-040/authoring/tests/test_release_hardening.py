"""WI-040 release gates: backup integrity and the novice home-to-PoC journey."""
import json
import os
import unittest
from playwright.sync_api import sync_playwright

BASE = os.environ.get('VISIONAI_TEST_URL', 'http://127.0.0.1:8000/docs/index.html')
KEY = 'vision-ai-model-selection-learning-v1'


class ReleaseHardeningTests(unittest.TestCase):
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

    def open_seeded(self):
        self.page.goto(BASE + '#view=poc')
        seed = self.backup(version=2)
        seed['poc'] = {'task': '舊草稿不可遺失', '_notes': {'task': '補充也須保留'},
                       '_flow': {'version': 1, 'answers': {'task': 'count'}, 'confirmed': ['task'], 'current': ''}}
        self.page.evaluate('([key,value])=>localStorage.setItem(key,JSON.stringify(value))', [KEY, seed])
        self.page.reload()
        self.page.locator('#poc-answer').wait_for(state='visible')
        self.page.locator('.poc-backup').last.locator('summary').click()

    @staticmethod
    def backup(version=2):
        result = {'version': version, 'completed': {'resnet': '2026-09-13T00:00:00Z'},
                  'visited': {'resnet': '2026-09-13T00:00:00Z'}, 'bookmarks': ['resnet'],
                  'last': 'resnet', 'theme': 'light'}
        if version != 1:
            result['poc'] = {'task': '合法備份的任務'}
        return result

    def raw_saved(self):
        return self.page.evaluate('(key)=>localStorage.getItem(key)', KEY)

    def upload(self, payload):
        content = payload if isinstance(payload, bytes) else json.dumps(payload, ensure_ascii=False).encode('utf8')
        self.page.locator('#import-progress').set_input_files([])
        self.page.locator('#import-progress').set_input_files(
            {'name': 'progress.json', 'mimeType': 'application/json', 'buffer': content})

    def test_invalid_backups_are_rejected_before_confirmation_without_mutating_state(self):
        malformed = self.backup()
        malformed['completed'] = []
        bad_bookmarks = self.backup()
        bad_bookmarks['bookmarks'] = 'resnet'
        bad_poc = self.backup()
        bad_poc['poc'] = []
        wrong_type = self.backup()
        wrong_type['backupType'] = 'another-application'
        cases = {'unrelated': {'hello': 'world'}, 'empty': {}, 'array': [], 'invalid_json': b'{',
                 'unsupported_version': self.backup(999), 'malformed_record': malformed,
                 'malformed_bookmarks': bad_bookmarks, 'malformed_poc': bad_poc,
                 'wrong_backup_type': wrong_type}
        for label, payload in cases.items():
            with self.subTest(label=label):
                self.open_seeded()
                before = self.raw_saved()
                dialogs = []
                def dismiss(dialog):
                    dialogs.append(dialog.message)
                    dialog.dismiss()
                self.page.on('dialog', dismiss)
                self.upload(payload)
                self.page.wait_for_function("document.getElementById('toast').textContent.includes('無法')")
                self.assertEqual(dialogs, [], 'Invalid data must not reach a replacement confirmation')
                self.assertEqual(self.raw_saved(), before)
                self.page.remove_listener('dialog', dismiss)

    def test_supported_legacy_v1_and_v2_backups_are_accepted(self):
        for version in (1, 2):
            with self.subTest(version=version):
                self.open_seeded()
                expected = self.backup(version)
                self.page.once('dialog', lambda dialog: dialog.accept())
                self.upload(expected)
                self.page.wait_for_function("document.getElementById('toast').textContent.includes('已匯入')")
                saved = json.loads(self.raw_saved())
                for key, value in expected.items():
                    self.assertEqual(saved[key], 2 if key == 'version' else value, key)
                self.assertEqual(saved.get('poc'), expected.get('poc', {}))

    def test_storage_failure_preserves_saved_and_visible_original(self):
        self.open_seeded()
        before = self.raw_saved()
        old_question = self.page.locator('#poc-question-title').inner_text()
        self.page.evaluate("()=>{Storage.prototype.setItem=function(){throw new Error('test storage unavailable');};}")
        self.page.once('dialog', lambda dialog: dialog.accept())
        self.upload(self.backup())
        self.page.wait_for_function("document.getElementById('toast').textContent.includes('原進度已保留')")
        self.assertEqual(self.raw_saved(), before)
        self.assertEqual(self.page.locator('#poc-question-title').inner_text(), old_question)
        self.assertEqual(self.page.locator('#poc-answer').get_attribute('data-poc-answer'), 'placement')

    def test_cancel_valid_import_keeps_exact_original_state(self):
        self.open_seeded()
        before = self.raw_saved()
        dialogs = []
        def cancel(dialog):
            dialogs.append(dialog.message)
            dialog.dismiss()
        self.page.once('dialog', cancel)
        with self.page.expect_event('dialog'):
            self.upload(self.backup())
        self.assertEqual(len(dialogs), 1)
        self.assertEqual(self.raw_saved(), before)

    def test_new_export_has_application_identity_and_roundtrips(self):
        self.open_seeded()
        before = json.loads(self.raw_saved())
        with self.page.expect_download() as info:
            self.page.locator('[data-action="export-progress"]').click()
        exported = json.loads(info.value.path().read_text(encoding='utf8'))
        self.assertEqual(exported['backupType'], 'vision-ai-learning-progress')
        self.assertEqual(exported['version'], 2)
        for key, value in before.items():
            self.assertEqual(exported[key], value, key)
        self.page.once('dialog', lambda dialog: dialog.accept())
        self.upload(exported)
        self.page.wait_for_function("document.getElementById('toast').textContent.includes('已匯入')")
        restored = json.loads(self.raw_saved())
        for key, value in before.items():
            self.assertEqual(restored[key], value, key)

    def test_home_primary_action_opens_task_without_model_knowledge(self):
        for width in (390, 1440):
            with self.subTest(width=width):
                self.page.set_viewport_size({'width': width, 'height': 1000})
                self.page.goto(BASE + '#view=home')
                action = self.page.locator('main .hero-actions [data-action="go"][data-view="poc"]')
                self.assertEqual(action.count(), 1)
                self.assertTrue(action.is_visible())
                self.assertIn('primary', action.get_attribute('class').split())
                self.assertGreater(self.page.locator('main .hero-actions [data-action="lesson"]').count(), 0,
                                   'A direct course-reading path must remain available')
                self.assertLessEqual(self.page.evaluate('document.documentElement.scrollWidth'), width)
                action.click()
                self.page.locator('#poc-answer').wait_for(state='visible')
                self.assertEqual(self.page.locator('#poc-answer').get_attribute('data-poc-answer'), 'task')
                self.assertEqual(self.page.locator('#poc-model').count(), 0)
                self.page.locator('#poc-answer').select_option('count')
                self.page.locator('[data-action="poc-next"]').click()
                self.assertEqual(self.page.locator('#poc-answer').get_attribute('data-poc-answer'), 'placement')
                self.page.evaluate('(key)=>localStorage.removeItem(key)', KEY)
                self.page.reload()


if __name__ == '__main__':
    unittest.main()

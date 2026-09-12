"""Behavior checks on the built PoC page with isolated browser storage."""
from pathlib import Path
import json, os, unittest
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[1]
BASE=os.environ.get('VISIONAI_TEST_URL','http://127.0.0.1:8000/docs/index.html')
KEY='vision-ai-model-selection-learning-v1'

class PocWorkbenchTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.pw=sync_playwright().start();cls.browser=cls.pw.chromium.launch(channel='msedge',headless=True)
 @classmethod
 def tearDownClass(cls):cls.browser.close();cls.pw.stop()
 def setUp(self):
  self.context=self.browser.new_context(viewport={'width':1440,'height':1000},accept_downloads=True)
  self.page=self.context.new_page();self.errors=[];self.page.on('pageerror',lambda e:self.errors.append(str(e)))
 def tearDown(self):self.context.close();self.assertEqual(self.errors,[])
 def open(self):self.page.goto(BASE+'#view=poc');self.page.locator('#poc-task').wait_for(state='attached')
 def click(self,action):self.page.locator('[data-action="'+action+'"]').filter(visible=True).first.click()
 def step(self,n):self.page.locator('.poc-step-nav button').nth(n).click()
 def test_step_navigation_persistence_and_missing_focus(self):
  self.open();self.assertEqual(self.page.locator('[data-poc-panel]:visible').count(),1)
  self.page.locator('#poc-task').fill('檢查墊圈漏裝');self.page.locator('#poc-output').fill('逐件候選框')
  self.step(1);self.page.locator('#poc-baseline').fill('人工清點');self.step(2)
  self.page.reload();self.assertTrue(self.page.locator('#poc-owner').is_visible())
  self.step(0);self.assertEqual(self.page.locator('#poc-task').input_value(),'檢查墊圈漏裝')
  self.page.locator('[data-action="poc-missing"][data-field="data"]').click()
  self.assertEqual(self.page.locator(':focus').get_attribute('id'),'poc-data')
 def test_model_search_hints_preserve_existing_content(self):
  self.open();self.page.locator('#poc-output').fill('我的既有交付');self.step(1)
  self.page.locator('#poc-model-search').fill('DINO');self.assertIn('找到',self.page.locator('#poc-model-count').inner_text())
  self.page.locator('#poc-model').select_option('det-dino-detector')
  self.assertIn('DINO',self.page.locator('#poc-model-guide').inner_text());self.click('poc-model-hints')
  self.step(0);self.assertEqual(self.page.locator('#poc-output').input_value(),'我的既有交付')
  self.step(2);self.assertTrue(self.page.locator('#poc-evidence').input_value())
  self.click('poc-undo');self.assertEqual(self.page.locator('#poc-evidence').input_value(),'')
 def test_example_cancel_replace_undo_and_learning_preserved(self):
  self.open();self.page.locator('#poc-task').fill('保留草稿')
  self.page.once('dialog',lambda d:d.dismiss());self.click('fill-poc-example');self.assertEqual(self.page.locator('#poc-task').input_value(),'保留草稿')
  self.page.once('dialog',lambda d:d.accept());self.click('fill-poc-example');self.assertIn('9 / 9',self.page.locator('#poc-summary').inner_text())
  self.click('poc-undo');self.assertEqual(self.page.locator('#poc-task').input_value(),'保留草稿')
  self.page.evaluate('(key)=>{const d=JSON.parse(localStorage.getItem(key));d.completed.resnet=true;localStorage.setItem(key,JSON.stringify(d));}',KEY)
  self.page.reload();self.page.locator('.poc-backup summary').click();self.page.once('dialog',lambda d:d.accept());self.click('poc-reset')
  stored=self.page.evaluate('(key)=>JSON.parse(localStorage.getItem(key))',KEY)
  self.assertTrue(stored['completed']['resnet']);self.assertEqual(stored['poc'],{})
 def test_preview_markdown_and_print_keep_long_text(self):
  self.open();long='逐件核對原圖\n'*100+'最後一行證據';self.page.locator('#poc-task').fill(long);self.click('poc-preview')
  self.assertIn('最後一行證據',self.page.locator('#poc-preview').inner_text())
  with self.page.expect_download() as download:self.click('export-poc-markdown')
  content=Path(download.value.path()).read_text(encoding='utf8');self.assertIn(long,content);self.assertIn('待補充',content)
  self.step(0);self.page.emulate_media(media='print');self.assertTrue(self.page.locator('#poc-preview').is_visible());self.assertFalse(self.page.locator('#poc-form').is_visible())
  self.assertIn('最後一行證據',self.page.locator('#poc-preview').inner_text())
 def test_storage_failure_is_visible(self):
  self.page.add_init_script("Storage.prototype.setItem=function(){throw new Error('quota');}")
  self.open();self.page.locator('#poc-task').fill('尚未保存');self.assertIn('無法儲存',self.page.locator('#poc-status').inner_text())
 def test_mobile_keyboard_and_preview(self):
  self.page.set_viewport_size({'width':390,'height':844});self.open();self.page.locator('#poc-task').focus();self.page.keyboard.type('AOI');self.page.keyboard.press('Tab')
  self.assertEqual(self.page.locator(':focus').get_attribute('id'),'poc-output')
  for n in range(3):
   self.step(n);self.assertLessEqual(self.page.evaluate('document.documentElement.scrollWidth'),390)
  self.click('poc-preview');self.assertTrue(self.page.locator('#poc-preview').is_visible());self.assertLessEqual(self.page.evaluate('document.documentElement.scrollWidth'),390)
 def test_json_roundtrip_and_legacy_draft(self):
  self.open();self.page.locator('#poc-task').fill('既有七欄草稿');self.page.locator('.poc-backup summary').click()
  with self.page.expect_download() as download:self.click('export-progress')
  file=download.value.path();self.page.locator('#poc-task').fill('暫時修改')
  self.page.once('dialog',lambda d:d.accept());self.page.locator('#import-progress').set_input_files(file)
  self.page.wait_for_function("document.querySelector('#poc-task').value==='既有七欄草稿'")
  self.step(1);self.assertEqual(self.page.locator('#poc-baseline').input_value(),'');self.step(2);self.assertEqual(self.page.locator('#poc-owner').input_value(),'')
 def test_lesson_handoff(self):
  self.open();self.page.goto(BASE+'#view=lesson&lesson=det-dino-detector');self.page.locator('[data-action="send-to-poc"]').click()
  self.page.locator('#poc-task').wait_for();self.step(1);self.assertEqual(self.page.locator('#poc-model').input_value(),'det-dino-detector')

if __name__=='__main__':unittest.main()

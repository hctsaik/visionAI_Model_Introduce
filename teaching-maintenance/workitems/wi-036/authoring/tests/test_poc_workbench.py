"""Choice-first workflows with isolated browser storage."""
from pathlib import Path
import json,os,unittest
from playwright.sync_api import sync_playwright
BASE=os.environ.get('VISIONAI_TEST_URL','http://127.0.0.1:8000/docs/index.html');KEY='vision-ai-model-selection-learning-v1'
class PocWorkbenchTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.pw=sync_playwright().start();cls.browser=cls.pw.chromium.launch(channel='msedge',headless=True)
 @classmethod
 def tearDownClass(cls):cls.browser.close();cls.pw.stop()
 def setUp(self):
  self.context=self.browser.new_context(viewport={'width':1440,'height':1000},accept_downloads=True);self.page=self.context.new_page();self.errors=[];self.page.on('pageerror',lambda e:self.errors.append(str(e)))
 def tearDown(self):self.context.close();self.assertEqual(self.errors,[])
 def open(self):self.page.goto(BASE+'#view=poc');self.page.locator('#poc-task').wait_for(state='attached')
 def click(self,a):self.page.locator(f'[data-action="{a}"]').filter(visible=True).first.click()
 def step(self,n):self.page.locator('.poc-step-nav button').nth(n).click()
 def answer(self,key,index=1):self.page.locator('#poc-'+key).select_option(index=index)
 def test_complete_without_free_text(self):
  self.open()
  for n,keys in enumerate([['task','output'],['data','baseline','contract'],['evidence','hold','owner']]):
   self.step(n);self.assertEqual(self.page.locator('textarea:visible').count(),0)
   for key in keys:self.answer(key)
   if n==1:self.page.locator('#poc-model').select_option('det-dino-detector')
  self.assertIn('9 / 9',self.page.locator('#poc-summary').inner_text());self.click('poc-preview');self.assertNotIn('待補充',self.page.locator('#poc-preview').inner_text())
 def test_dependent_output_preserved_and_flagged(self):
  self.open();self.answer('task',1);self.answer('output');value=self.page.locator('#poc-output').input_value();self.answer('task',2)
  self.assertEqual(value,self.page.locator('#poc-output').input_value());self.assertIn('任務已變更',self.page.locator('.poc-choice-warning').inner_text());self.assertIn('1 / 9',self.page.locator('#poc-summary').inner_text())
  self.page.locator('#poc-output').select_option(label='整張影像的類別與分數');self.assertEqual(self.page.locator('.poc-choice-warning').count(),0)
 def test_navigation_reload_and_focus(self):
  self.open();self.answer('task');value=self.page.locator('#poc-task').input_value();self.step(2);self.page.reload();self.assertTrue(self.page.locator('#poc-owner').is_visible());self.step(0);self.assertEqual(value,self.page.locator('#poc-task').input_value());self.page.locator('[data-action="poc-missing"][data-field="data"]').click();self.assertEqual(self.page.locator(':focus').get_attribute('id'),'poc-data')
 def test_custom_notes_export_and_print(self):
  self.open();self.page.locator('#poc-task').select_option('__custom__');long='原圖核對\n'*80+'最後一行';self.page.locator('#poc-custom-task').fill(long);self.page.locator('#poc-note-task').fill('現場備註');self.click('poc-preview')
  with self.page.expect_download() as d:self.click('export-poc-markdown')
  text=Path(d.value.path()).read_text(encoding='utf8');self.assertIn(long,text);self.assertIn('現場備註',text);self.step(0);self.page.emulate_media(media='print');self.assertTrue(self.page.locator('#poc-preview').is_visible());self.assertIn('最後一行',self.page.locator('#poc-preview').inner_text())
 def test_legacy_draft_preserved(self):
  self.page.add_init_script(f"localStorage.setItem({json.dumps(KEY)},JSON.stringify({{poc:{{task:'既有自由文字',output:'舊版輸出'}}}}))");self.open();self.assertEqual(self.page.locator('#poc-task').input_value(),'__custom__');self.assertEqual(self.page.locator('textarea:visible').count(),0);self.page.locator('#poc-task').locator('..').locator('summary').click();self.assertEqual(self.page.locator('#poc-custom-task').input_value(),'既有自由文字');self.click('poc-preview');self.assertIn('舊版輸出',self.page.locator('#poc-preview').inner_text())
 def test_example_cancel_replace_undo(self):
  self.open();self.answer('task');before=self.page.locator('#poc-task').input_value();self.page.once('dialog',lambda d:d.dismiss());self.click('fill-poc-example');self.assertEqual(before,self.page.locator('#poc-task').input_value());self.page.once('dialog',lambda d:d.accept());self.click('fill-poc-example');self.assertIn('9 / 9',self.page.locator('#poc-summary').inner_text());self.assertEqual(self.page.locator('textarea:visible').count(),0);self.click('poc-undo');self.assertEqual(before,self.page.locator('#poc-task').input_value())
 def test_model_search_hints_keep_answer(self):
  self.open();self.answer('output');value=self.page.locator('#poc-output').input_value();self.step(1);self.page.locator('#poc-model-search').fill('DINO');self.page.locator('#poc-model').select_option('det-dino-detector');self.click('poc-model-hints');self.step(0);self.assertEqual(value,self.page.locator('#poc-output').input_value());self.step(2);self.assertEqual(self.page.locator('#poc-evidence').input_value(),'__custom__')
 def test_json_roundtrip(self):
  self.open();self.answer('task');value=self.page.locator('#poc-task').input_value();self.page.locator('.poc-backup summary').click()
  with self.page.expect_download() as d:self.click('export-progress')
  path=d.value.path();self.answer('task',2);self.page.locator('.poc-backup summary').click();self.page.once('dialog',lambda d:d.accept());self.page.locator('#import-progress').set_input_files(path);self.page.wait_for_function('(v)=>document.querySelector("#poc-task").value===v',arg=value)
 def test_reset_preserves_learning(self):
  self.open();self.answer('task');self.page.evaluate('(k)=>{let d=JSON.parse(localStorage.getItem(k));d.completed.resnet=true;localStorage.setItem(k,JSON.stringify(d));}',KEY);self.page.reload();self.page.locator('.poc-backup summary').click();self.page.once('dialog',lambda d:d.accept());self.click('poc-reset');d=self.page.evaluate('(k)=>JSON.parse(localStorage.getItem(k))',KEY);self.assertTrue(d['completed']['resnet']);self.assertEqual(d['poc'],{})
 def test_storage_failure(self):
  self.page.add_init_script("Storage.prototype.setItem=function(){throw new Error('quota')}");self.open();self.answer('task');self.assertIn('無法儲存',self.page.locator('#poc-status').inner_text())
 def test_mobile_keyboard(self):
  self.page.set_viewport_size({'width':390,'height':844});self.open();self.page.locator('#poc-task').focus();self.page.keyboard.press('ArrowDown');self.page.keyboard.press('Enter')
  for n in range(3):self.step(n);self.assertEqual(self.page.locator('textarea:visible').count(),0);self.assertLessEqual(self.page.evaluate('document.documentElement.scrollWidth'),390)
 def test_lesson_handoff(self):
  self.page.goto(BASE+'#view=lesson&lesson=det-dino-detector');self.page.locator('[data-action="send-to-poc"]').click();self.page.locator('#poc-task').wait_for();self.step(1);self.assertEqual(self.page.locator('#poc-model').input_value(),'det-dino-detector')
if __name__=='__main__':unittest.main()

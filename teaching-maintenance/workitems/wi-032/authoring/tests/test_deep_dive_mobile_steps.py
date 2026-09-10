"""Optional mobile steps preserve the diagram and reject invalid authored crops."""
import json
import unittest
from test_interactive_navigation import BUILDER, ROOT
from test_resnet_deep_dive import edge_executable

def lesson():
    return json.loads((ROOT/'_course_content/topics/ad-efficientad.json').read_text(encoding='utf-8'))['deep_dive']

class MobileStepsTests(unittest.TestCase):
    def test_old_contract_remains_supported(self):
        data=lesson()
        data['chapters'][5].pop('mobile_steps')
        clean=BUILDER._clean_deep_dive(data,'test')
        self.assertNotIn('mobile_steps',clean['chapters'][5])

    def test_invalid_crops_are_rejected(self):
        for crop in [[-1,0,20,20],[0,0,0,20],[1600,0,100,20],[0,900,20,60],[True,0,20,20],[0,0,1.5,20]]:
            with self.subTest(crop=crop):
                data=lesson()
                data['chapters'][5]['mobile_steps'][0]['crop']=crop
                with self.assertRaises(ValueError): BUILDER._clean_deep_dive(data,'test')

    def test_mobile_vertical_case_and_full_diagram_access(self):
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            browser=p.chromium.launch(executable_path=edge_executable(),headless=True,args=['--allow-file-access-from-files'])
            page=browser.new_page(viewport={'width':390,'height':844})
            page.goto((ROOT/'interactive-learning.html').as_uri()+'#view=lesson&lesson=ad-efficientad&slide=6')
            chapter=page.locator('[data-deep-dive-chapter="6"]')
            steps=chapter.locator('.deep-dive-mobile-steps li')
            self.assertEqual(steps.count(),5)
            self.assertFalse(chapter.locator('.deep-dive-image-link').is_visible())
            boxes=steps.evaluate_all('(nodes)=>nodes.map(n=>{const b=n.getBoundingClientRect();return {top:b.top+scrollY,bottom:b.bottom+scrollY,left:b.left,right:b.right}})')
            previous_bottom=0
            for box in boxes:
                self.assertGreaterEqual(box['top'],previous_bottom)
                self.assertLessEqual(box['right'],391)
                self.assertGreaterEqual(box['left'],0)
                previous_bottom=box['bottom']
            chapter.locator('[data-action="open-concept"]').click()
            self.assertEqual(page.locator('dialog[open]').count(),1)
            page.keyboard.press('Escape')
            page.set_viewport_size({'width':1440,'height':1000})
            self.assertTrue(chapter.locator('.deep-dive-image-link').is_visible())
            self.assertFalse(chapter.locator('.deep-dive-mobile-steps').is_visible())
            browser.close()

if __name__=='__main__': unittest.main()

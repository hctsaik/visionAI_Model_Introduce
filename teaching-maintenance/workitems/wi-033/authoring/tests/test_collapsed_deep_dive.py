"""Opt-in first-read lessons retain validated advanced chapters."""
import json
import unittest
from test_interactive_navigation import BUILDER, ROOT
from test_resnet_deep_dive import edge_executable

class CollapsedDeepDiveTests(unittest.TestCase):
    def data(self):
        return json.loads((ROOT/'_course_content/topics/resnet.json').read_text(encoding='utf-8'))['deep_dive']

    def test_optional_boolean_preserves_all_chapters(self):
        data=self.data()
        data.pop('default_collapsed',None)
        old=BUILDER._clean_deep_dive(data,'legacy')
        self.assertNotIn('default_collapsed',old)
        data['default_collapsed']=True
        new=BUILDER._clean_deep_dive(data,'first-read')
        self.assertTrue(new.pop('default_collapsed'))
        self.assertEqual(new,old)
        for bad in ('true',1,None,[]):
            with self.subTest(value=bad):
                data['default_collapsed']=bad
                with self.assertRaises(ValueError):
                    BUILDER._clean_deep_dive(data,'invalid')

    def test_first_read_and_both_reference_navigation_paths(self):
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            browser=p.chromium.launch(executable_path=edge_executable(),headless=True,args=['--allow-file-access-from-files'])
            for width in (1440,360):
                page=browser.new_page(viewport={'width':width,'height':900})
                base=(ROOT/'interactive-learning.html').as_uri()+'#view=lesson&lesson=resnet&slide='
                page.goto(base+'1')
                advanced=page.locator('.legacy-deep-reference')
                self.assertFalse(advanced.evaluate('(n)=>n.open'))
                self.assertEqual(page.locator('.beginner-visual').count(),3)
                self.assertTrue(page.locator('.beginner-visual').first.is_visible())
                advanced.locator(':scope > summary').click()
                advanced.locator('[data-action="deep-dive-chapter"][data-chapter="2"]').first.click()
                self.assertTrue(page.locator('#deep-dive-resnet-2').is_visible())
                advanced.locator('[data-action="deep-dive-chapter"][data-chapter="1"]').first.click()
                self.assertTrue(advanced.evaluate('(n)=>n.open'))
                advanced.locator(':scope > summary').click()
                formal=page.locator('.formal-slide-reference:not(.legacy-deep-reference)').filter(has=page.locator('[data-action="jump-step"]'))
                formal.locator(':scope > summary').click()
                formal.locator('[data-action="jump-step"][data-step="2"]').first.click()
                self.assertFalse(advanced.evaluate('(n)=>n.open'))
                self.assertTrue(page.locator('#step-resnet-2').is_visible())
                page.goto(base+'3')
                self.assertTrue(advanced.evaluate('(n)=>n.open'))
                self.assertTrue(page.locator('#deep-dive-resnet-3').is_visible())
                page.close()
            browser.close()

if __name__=='__main__': unittest.main()

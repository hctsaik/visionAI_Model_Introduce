"""Regression: oversized SVGs must expose both edges in the mobile lightbox."""
from pathlib import Path
import unittest
from playwright.sync_api import sync_playwright
from test_resnet_deep_dive import edge_executable

ROOT = Path(__file__).resolve().parents[1]

class ConceptZoomEdgesTests(unittest.TestCase):
    def test_mobile_zoom_starts_at_left_and_can_reach_right_edge(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(executable_path=edge_executable(),headless=True,args=['--allow-file-access-from-files'])
            page = browser.new_page(viewport={'width':390,'height':844})
            page.goto((ROOT/'interactive-learning.html').as_uri()+'#view=lesson&lesson=ad-efficientad&slide=1')
            page.locator('.deep-dive-figure [data-action="open-concept"]').first.click()
            wrap = page.locator('.lightbox-image-wrap')
            self.assertTrue(wrap.evaluate('(e)=>e.firstElementChild.getBoundingClientRect().left>=e.getBoundingClientRect().left'))
            wrap.evaluate('(e)=>{e.scrollLeft=e.scrollWidth}')
            self.assertTrue(wrap.evaluate('(e)=>e.firstElementChild.getBoundingClientRect().right<=e.getBoundingClientRect().right+1'))
            page.keyboard.press('Escape')
            self.assertEqual(page.locator('dialog[open]').count(),0)
            browser.close()

if __name__=='__main__': unittest.main()

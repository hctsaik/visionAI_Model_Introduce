"""Focused contract and browser QA for the ResNet eight-chapter deep dive."""

from __future__ import annotations

import json
import os
import shutil
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOPIC_PATH = ROOT / "_course_content" / "topics" / "resnet.json"
HTML_PATH = ROOT / "interactive-learning.html"
SVG_NS = {"svg": "http://www.w3.org/2000/svg"}
EXPECTED_IDS = (
    "task-output",
    "residual-addition",
    "stage-shapes",
    "train-infer-bn",
    "pooling-observability",
    "calibration-ood",
    "variants-evidence",
    "selection-decision",
)


def topic() -> dict:
    return json.loads(TOPIC_PATH.read_text(encoding="utf-8"))


def deep_dive_paths() -> list[Path]:
    return [ROOT / chapter["image"] for chapter in topic()["deep_dive"]["chapters"]]


def edge_executable() -> str:
    candidates = (
        Path(os.environ.get("PROGRAMFILES(X86)", r"C:\Program Files (x86)"))
        / "Microsoft" / "Edge" / "Application" / "msedge.exe",
        Path(os.environ.get("PROGRAMFILES", r"C:\Program Files"))
        / "Microsoft" / "Edge" / "Application" / "msedge.exe",
    )
    for candidate in candidates:
        if candidate.is_file():
            return str(candidate)
    found = shutil.which("msedge") or shutil.which("msedge.exe")
    if not found:
        raise FileNotFoundError("Microsoft Edge is required for ResNet browser QA")
    return found


class ResNetDeepDiveTests(unittest.TestCase):
    def test_authored_contract_has_eight_ordered_source_backed_chapters(self) -> None:
        deep = topic()["deep_dive"]
        chapters = deep["chapters"]
        self.assertEqual(EXPECTED_IDS, tuple(chapter["id"] for chapter in chapters))
        self.assertTrue((ROOT / deep["concept_path"]).is_file())
        source_ids = {source["id"] for source in deep["sources"]}
        self.assertGreaterEqual(len(source_ids), 5)
        for chapter in chapters:
            self.assertEqual(3, len(chapter["points"]))
            self.assertTrue(set(chapter["source_ids"]) <= source_ids)
            self.assertTrue(chapter["check"]["question"])
            self.assertTrue(chapter["check"]["answer"])

    def test_all_chapter_visuals_are_full_canvas_and_readable(self) -> None:
        paths = deep_dive_paths()
        self.assertEqual(8, len(paths))
        for path in paths:
            self.assertTrue(path.is_file(), path)
            root = ET.fromstring(path.read_text(encoding="utf-8"))
            self.assertEqual("1672", root.attrib["width"], path.name)
            self.assertEqual("941", root.attrib["height"], path.name)
            self.assertEqual("0 0 1672 941", root.attrib["viewBox"], path.name)
            for node in root.findall(".//svg:text", SVG_NS):
                value = "".join(node.itertext()).strip()
                if value:
                    self.assertGreaterEqual(float(node.attrib["font-size"]), 18, (path.name, value))

    def test_generated_anchor_is_present_and_text_free(self) -> None:
        anchor = ROOT / "_course_content/generated-concepts/resnet/resnet-industrial-known-class-anchor_v03.png"
        self.assertTrue(anchor.is_file())
        # The opening view teaches motivation; its companion retains the workpiece.
        first_chapter = topic()["deep_dive"]["chapters"][0]
        chapter_svgs = "\n".join(
            (ROOT / view["image"]).read_text(encoding="utf-8")
            for view in first_chapter["reading_views"]
        )
        self.assertIn(anchor.name, chapter_svgs)

    def test_browser_text_bboxes_stay_inside_every_svg(self) -> None:
        from playwright.sync_api import sync_playwright

        errors: list[str] = []
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(
                executable_path=edge_executable(),
                headless=True,
                args=["--allow-file-access-from-files"],
            )
            page = browser.new_page(viewport={"width": 1672, "height": 941})
            for path in deep_dive_paths():
                page.goto(path.resolve().as_uri(), wait_until="load")
                rows = page.locator("text").evaluate_all(
                    """nodes => nodes.map(node => {
                        const box = node.getBBox();
                        return {value: node.textContent || '', x: box.x, y: box.y,
                                width: box.width, height: box.height};
                    })"""
                )
                for row in rows:
                    if (
                        row["x"] < -1
                        or row["y"] < -1
                        or row["x"] + row["width"] > 1673
                        or row["y"] + row["height"] > 942
                    ):
                        errors.append(f"{path.name}: {row['value']!r} leaves canvas {row}")
            browser.close()
        self.assertEqual([], errors)

    def test_runtime_renders_only_the_new_deep_dive_and_supports_slide_eight(self) -> None:
        from playwright.sync_api import sync_playwright

        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(
                executable_path=edge_executable(),
                headless=True,
                args=["--allow-file-access-from-files"],
            )
            page = browser.new_page(viewport={"width": 1440, "height": 1000})
            page.goto(
                HTML_PATH.resolve().as_uri() + "#view=lesson&lesson=resnet&slide=8",
                wait_until="load",
            )
            page.wait_for_selector('[data-deep-dive="resnet"]')
            self.assertEqual(8, page.locator(".deep-dive-chapter").count())
            expected_views = sum(len(ch.get("reading_views") or [ch]) for ch in topic()["deep_dive"]["chapters"])
            deep = page.locator('[data-deep-dive="resnet"]')
            self.assertEqual(expected_views, deep.locator(".deep-dive-figure").count())
            self.assertEqual(expected_views, deep.locator(".deep-dive-image-link object, .deep-dive-image-link img").count())
            expected_mobile = sum(v.get("mobile_display_mode") == "full-mobile"
                                  for ch in topic()["deep_dive"]["chapters"]
                                  for v in ch.get("reading_views", []))
            self.assertEqual(expected_mobile, deep.locator(".deep-dive-figure img.full-mobile-reading").count())
            # Companion comparisons add assets while retaining eight chapters
            # and one selected reading panel within each chapter.
            self.assertEqual(8, deep.locator(".reading-view-panel:not([hidden])").count())
            self.assertEqual(0, deep.locator(".teaching-primer").count())
            self.assertEqual(0, deep.locator(".formal-slide-reference").count())
            self.assertEqual("step", page.locator('.deep-dive-nav [aria-current="step"]').get_attribute("aria-current"))
            self.assertIn("slide=8", page.url)

            mobile = browser.new_page(viewport={"width": 390, "height": 844}, device_scale_factor=1)
            mobile.goto(
                HTML_PATH.resolve().as_uri() + "#view=lesson&lesson=resnet&slide=4",
                wait_until="load",
            )
            mobile.wait_for_selector('[data-deep-dive="resnet"]')
            mobile.wait_for_timeout(500)
            dimensions = mobile.evaluate(
                """() => {
                    const nav = document.querySelector('.deep-dive-nav');
                    const active = nav.querySelector('.active');
                    const navBox = nav.getBoundingClientRect();
                    const activeBox = active.getBoundingClientRect();
                    return {viewport: window.innerWidth,
                            document: document.documentElement.scrollWidth,
                            chapters: document.querySelectorAll('.deep-dive-chapter').length,
                            activeVisible: activeBox.left >= navBox.left - 1 &&
                                           activeBox.right <= navBox.right + 1};
                }"""
            )
            self.assertEqual(8, dimensions["chapters"])
            self.assertLessEqual(dimensions["document"], dimensions["viewport"] + 1)
            self.assertTrue(dimensions["activeVisible"])
            browser.close()


if __name__ == "__main__":
    unittest.main()

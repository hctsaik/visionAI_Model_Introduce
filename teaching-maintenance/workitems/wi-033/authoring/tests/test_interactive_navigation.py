from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILDER_PATH = ROOT / "tools" / "build_interactive_learning_html.py"

SPEC = importlib.util.spec_from_file_location("interactive_builder_navigation_test", BUILDER_PATH)
assert SPEC and SPEC.loader
BUILDER = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BUILDER
SPEC.loader.exec_module(BUILDER)


class InteractiveNavigationTests(unittest.TestCase):
    def test_sidebar_navigation_resets_to_the_new_section_start(self) -> None:
        template = BUILDER.HTML_TEMPLATE
        self.assertIn("function routeKey(route)", template)
        self.assertIn("function scrollToRouteStart()", template)
        self.assertIn('window.scrollTo({ top: 0, left: 0, behavior: reduceMotion ? "auto" : "smooth" })', template)
        self.assertIn('heading.focus({ preventScroll: true })', template)
        self.assertIn("const shouldMoveToPageStart = (pendingRouteNavigation || routeChanged)", template)

    def test_reselecting_the_active_sidebar_item_is_not_a_dead_click(self) -> None:
        template = BUILDER.HTML_TEMPLATE
        self.assertIn("if (location.hash === nextHash) {", template)
        self.assertIn("pendingRouteNavigation = true;", template)
        self.assertIn("render();\n        return;", template)

    def test_deep_linked_reference_steps_keep_their_step_scroll(self) -> None:
        template = BUILDER.HTML_TEMPLATE
        self.assertIn('&& !(route.view === "lesson" && route.slide > 1);', template)
        self.assertIn("requestAnimationFrame(() => jumpStep(route.lesson, route.slide));", template)


if __name__ == "__main__":
    unittest.main()

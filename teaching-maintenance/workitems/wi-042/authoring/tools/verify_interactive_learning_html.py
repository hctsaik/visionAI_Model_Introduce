"""Validate the generated offline Vision AI teaching page.

This intentionally checks the public HTML artifact rather than just the source
specifications: all 58 topic lessons, all shared foundation/production visual
assets, and the key offline learning interactions must survive the build step.
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_HTML = ROOT / "interactive-learning.html"
sys.path.insert(0, str(ROOT / "tools"))
# Share only the accepted native media dimensions with the authoring contract.
# Payload schema, path boundaries, decoding and release checks remain independent.
from build_interactive_learning_html import _validate_concept_visual_asset
from build_github_pages_site import referenced_assets
REQUIRED_TEXT = (
    "從第一張教學圖開始",
    "四圖連續導讀",
    "30 秒讀懂這張圖",
    "工程師操作卡",
    "共同工程前提",
    "從 POC 到量產",
    "POC 選型畫布",
    "function pocHTML()",
    "POC_DECISION.evaluate",
    "data-poc-answer",
    "poc-next",
    "parseProgressBackup",
    "重新選問題",
    "localStorage",
    "open-lightbox",
    "jump-step",
)
FORBIDDEN_TEXT = (
    "快速自測",
    "quiz-choice",
    "data-action=\"quiz\"",
    "答對：",
    "再想一次：",
    "data-action=\"set-slide\"",
)
ARCHITECTURE_TERM_TOPICS = {"ad-dinomaly", "ad-invad", "ad-ddad"}


def verify_concept_reference_counts(html_path: Path, assets: list[Path], expected: int) -> None:
    """Allow the two reviewed six-topic comparisons, retaining accidental-alias checks."""
    counts = Counter(assets)
    shared_excess = 0
    for kind in ("known", "prompt"):
        path = (html_path.parent / (
            "_course_content/generated-concepts/det-yolo-dense/"
            f"det-yolo-dense-d01-compare-{kind}.svg"
        )).resolve()
        count = counts[path]
        if count not in (0, 6):
            raise ValueError(f"D01 comparison must serve all six detector topics: {path} / {count}")
        shared_excess += max(0, count - 1)
    minimum_unique = expected - 1 - shared_excess  # Retain the pre-D01 one-alias allowance.
    if len(assets) != expected or len(counts) < minimum_unique:
        raise ValueError(
            f"Expected {expected} concept-image references and at least {minimum_unique} "
            f"unique images after reviewed sharing, found {len(assets)} / {len(counts)}"
        )


def embedded_course_data(document: str) -> dict:
    match = re.search(
        r'<script id="course-data" type="application/json">(.*?)</script>',
        document,
        flags=re.DOTALL,
    )
    if not match:
        raise ValueError("Missing embedded #course-data JSON")
    payload = json.loads(match.group(1))
    if not isinstance(payload, dict):
        raise ValueError("Embedded course data must be an object")
    return payload



def checked_local_path(html_path: Path, relative: str) -> Path:
    if not isinstance(relative, str) or not relative or "\\" in relative:
        raise ValueError(f"Invalid local asset path: {relative!r}")
    path = Path(relative)
    if path.is_absolute() or ".." in path.parts or ":" in relative:
        raise ValueError(f"Unsafe local asset path: {relative!r}")
    root = html_path.parent.resolve()
    asset = (root / path).resolve()
    if not asset.is_relative_to(root):
        raise ValueError(f"Local asset leaves release root: {relative!r}")
    return asset


def verify_asset(html_path: Path, relative: str, expected_root: str, expected_size: tuple[int, int] | None = None) -> Path:
    if not isinstance(relative, str) or not relative.startswith(expected_root):
        raise ValueError(f"Unsafe or unexpected asset path: {relative!r}")
    asset = checked_local_path(html_path, relative)
    if not asset.is_file():
        raise FileNotFoundError(f"Missing referenced asset: {asset}")
    if expected_size is None:
        _validate_concept_visual_asset(asset)
    with Image.open(asset) as image:
        if expected_size is not None and (
            any(type(n) is not int or n <= 0 for n in expected_size) or image.size != expected_size
        ):
            raise ValueError(f"Declared image dimensions do not match {image.size}: {asset}")
        image.verify()
    return asset


def verify_concept_asset(html_path: Path, relative: str) -> Path:
    """Concept bridges may be generated PNGs or precise inline-SVG diagrams."""

    if not isinstance(relative, str) or not relative.startswith("_course_content/generated-concepts/"):
        raise ValueError(f"Unsafe or unexpected concept asset path: {relative!r}")
    asset = checked_local_path(html_path, relative)
    if not asset.is_file():
        raise FileNotFoundError(f"Missing referenced concept asset: {asset}")
    if asset.suffix.lower() == ".png":
        _validate_concept_visual_asset(asset)
        with Image.open(asset) as image:
            image.verify()
        return asset
    if asset.suffix.lower() == ".svg":
        svg = asset.read_text(encoding="utf-8")
        _validate_concept_visual_asset(asset)
        if "\ufffd" in svg:
            raise ValueError(f"Concept SVG contains a Unicode replacement character: {asset}")
        try:
            document = ElementTree.fromstring(svg)
        except ElementTree.ParseError as exc:
            raise ValueError(f"Invalid concept SVG: {asset}") from exc
        text_content = " ".join(part.strip() for part in document.itertext() if part.strip())
        managed_suffixes = (
            "-causal-chain_v01.svg",
            "-worked-example_v01.svg",
            "-comparison_v01.svg",
            "-boundary-cases_v01.svg",
        )
        if asset.name.endswith(managed_suffixes):
            lone_punctuation = {
                ".", ",", ";", ":", "!", "?",
                chr(0x3001), chr(0x3002), chr(0xFF0C), chr(0xFF01),
                chr(0xFF1F), chr(0xFF1B), chr(0xFF1A),
            }
            orphan_lines = [
                "".join(node.itertext()).strip()
                for node in document.iter()
                if node.tag.rsplit("}", 1)[-1] == "text"
                and "".join(node.itertext()).strip() in lone_punctuation
            ]
            if orphan_lines:
                raise ValueError(
                    f"Generated concept SVG has orphan punctuation lines {orphan_lines}: {asset}"
                )
        if asset.name.endswith(managed_suffixes) and len(text_content) < 80:
            raise ValueError(f"Generated concept SVG has too little learner-facing explanation: {asset}")
        if asset.name.endswith("-causal-chain_v01.svg"):
            required_labels = ("因為：", "工程圖核對", "candidate")
            missing = [label for label in required_labels if label not in text_content]
            if missing:
                raise ValueError(
                    f"Causal-chain SVG is missing its learner-facing anchors {missing}: {asset}"
                )
        return asset
    raise ValueError(f"Unsupported concept asset type: {asset}")


def verify_inline_asset(html_path: Path, relative: str) -> Path:
    """Validate a paragraph-adjacent SVG mechanism aid.

    Inline aids deliberately use a compact 720×360 canvas.  They are not the
    1672×941 image-led bridge assets validated by :func:`verify_concept_asset`.
    Treating the two roles as identical was making the public-page verifier
    reject every otherwise valid lesson.
    """

    if not isinstance(relative, str) or not relative.startswith("_course_content/generated-concepts/"):
        raise ValueError(f"Unsafe or unexpected inline visual path: {relative!r}")
    asset = checked_local_path(html_path, relative)
    if not asset.is_file():
        raise FileNotFoundError(f"Missing referenced inline visual: {asset}")
    if asset.suffix.lower() != ".svg":
        raise ValueError(f"Inline mechanism visual must be SVG: {asset}")
    svg = asset.read_text(encoding="utf-8")
    if not re.search(r'<svg\b[^>]*\bwidth="720"[^>]*\bheight="360"[^>]*\bviewBox="0 0 720 360"', svg):
        raise ValueError(f"Unexpected inline SVG dimensions: {asset}")
    if "\ufffd" in svg:
        raise ValueError(f"Inline SVG contains a Unicode replacement character: {asset}")
    try:
        ElementTree.fromstring(svg)
    except ElementTree.ParseError as exc:
        raise ValueError(f"Invalid inline SVG: {asset}") from exc
    return asset


def verify_crop(crop: list[int], bounds: tuple[int, int], label: str) -> None:
    if not isinstance(crop, list) or len(crop) != 4 or any(type(n) is not int for n in crop):
        raise ValueError(f"{label}: invalid crop")
    x, y, width, height = crop
    if min(x,y) < 0 or min(width,height) <= 0 or x+width > bounds[0] or y+height > bounds[1]:
        raise ValueError(f"{label}: crop outside visual")


def validate(html_path: Path) -> None:
    if not html_path.is_file():
        raise FileNotFoundError(html_path)
    document = html_path.read_text(encoding="utf-8")
    if "\ufffd" in document:
        raise ValueError("HTML contains Unicode replacement characters")
    missing_text = [text for text in REQUIRED_TEXT if text not in document]
    if missing_text:
        raise ValueError(f"Missing expected learning UI text/hooks: {missing_text}")
    forbidden_text = [text for text in FORBIDDEN_TEXT if text in document]
    if forbidden_text:
        raise ValueError(f"Obsolete quiz/tab UI remains in public HTML: {forbidden_text}")
    if "fetch(" in document:
        raise ValueError("Offline HTML must not fetch local course data")

    # Python's stdlib parser provides a useful static HTML well-formedness
    # smoke check without requiring a browser or a network connection.
    from html.parser import HTMLParser

    class _Parser(HTMLParser):
        pass

    parser = _Parser()
    parser.feed(document)
    parser.close()

    course = embedded_course_data(document)
    topics = course.get("topics")
    if not isinstance(topics, list) or len(topics) != 58:
        raise ValueError(f"Expected 58 topics, found {len(topics) if isinstance(topics, list) else 'invalid'}")
    ids = [topic.get("id") for topic in topics]
    if len(set(ids)) != 58 or any(not item for item in ids):
        raise ValueError("Topic IDs must be 58 unique non-empty values")

    images: list[Path] = []
    concept_images: list[Path] = []
    first_read_images: list[Path] = []
    deep_dive_images: list[Path] = []
    for topic in topics:
        topic_id = topic.get("id")
        learner = topic.get("learnerBrief")
        learner_fields = ("problem", "deliverable", "first", "hold", "terms")
        if not isinstance(learner, dict) or any(not learner.get(field) for field in learner_fields):
                raise ValueError(f"{topic_id}: missing first-read learner brief")
        if not isinstance(learner["terms"], list) or len(learner["terms"]) < 2:
            raise ValueError(f"{topic_id}: learner brief needs term explanations")
        teaching = topic.get("teachingStory")
        if not isinstance(teaching, dict):
            raise ValueError(f"{topic_id}: missing required model-specific teaching story")
        required_story_fields = {
            "model", "badge", "title", "scenario", "promise", "mental_model", "micro_example",
            "mechanism_steps", "inline_visuals", "visual_intro", "concept_visuals", "boundary_cases", "comparison", "selection", "poc",
            "comparison_headers", "teach_back", "transfer_check", "review_trace", "slide_reading",
        }
        allowed_story_fields = required_story_fields | {"beginner_path", "deep_dive", "takeaway", "engineering_slides"}
        if not required_story_fields <= set(teaching) or not set(teaching) <= allowed_story_fields:
            raise ValueError(f"{topic_id}: incomplete model-specific teaching story")
        if teaching.get("model") != topic.get("model"):
            raise ValueError(f"{topic_id}: teaching-story model name mismatch")
        if not isinstance(teaching.get("mechanism_steps"), list) or len(teaching["mechanism_steps"]) != 4:
            raise ValueError(f"{topic_id}: teaching story needs four causal steps")
        for step_index, step in enumerate(teaching["mechanism_steps"], start=1):
            if not isinstance(step, dict) or not {"title", "body", "why", "anchor", "diagram"} <= set(step) or set(step) - {"title", "body", "why", "anchor", "diagram", "inline_image"}:
                raise ValueError(f"{topic_id}: invalid causal step {step_index}")
            if any(not isinstance(step[k], str) or not step[k].strip() for k in ("title", "body", "why", "anchor")):
                raise ValueError(f"{topic_id}: empty causal step text {step_index}")
            diagram = step.get("diagram")
            if not isinstance(diagram, dict) or set(diagram) != {"title", "body", "why", "anchor"}:
                raise ValueError(f"{topic_id}: missing diagram copy for causal step {step_index}")
            if any(not isinstance(value, str) or not value for value in diagram.values()):
                raise ValueError(f"{topic_id}: empty diagram copy for causal step {step_index}")
        inline_visuals = teaching.get("inline_visuals")
        inline_fields = {"id", "image", "label", "not_claim", "alt", "cue", "display"}
        if not isinstance(inline_visuals, list) or len(inline_visuals) != 4:
            raise ValueError(f"{topic_id}: teaching story needs four inline mechanism visuals")
        for visual_index, visual in enumerate(inline_visuals, start=1):
            if not isinstance(visual, dict) or set(visual) != inline_fields:
                raise ValueError(f"{topic_id}: invalid inline mechanism visual {visual_index}")
            if not all(isinstance(visual.get(field), str) and visual[field] for field in inline_fields):
                raise ValueError(f"{topic_id}: incomplete inline mechanism visual {visual_index}")
            if visual["display"] == "inline":
                verify_inline_asset(html_path, visual["image"])
            elif visual["display"] == "full-width":
                verify_concept_asset(html_path, visual["image"])
            else:
                raise ValueError(f"{topic_id}: invalid inline display mode")
        if not isinstance(teaching.get("boundary_cases"), list) or len(teaching["boundary_cases"]) < 3:
            raise ValueError(f"{topic_id}: teaching story needs boundary cases")
        if not isinstance(teaching.get("comparison"), list) or len(teaching["comparison"]) < 3:
            raise ValueError(f"{topic_id}: teaching story needs nearest-method comparison")
        comparison_headers = teaching.get("comparison_headers")
        if not isinstance(comparison_headers, dict) or set(comparison_headers) != {"title", "basis", "output"}:
            raise ValueError(f"{topic_id}: teaching story needs model-specific comparison headers")
        if any(not isinstance(value, str) or not value for value in comparison_headers.values()):
            raise ValueError(f"{topic_id}: incomplete model-specific comparison headers")
        poc = teaching.get("poc")
        if not isinstance(poc, dict) or set(poc) != {"title", "steps", "hold", "acceptance"}:
            raise ValueError(f"{topic_id}: teaching story needs POC acceptance design")
        acceptance = poc.get("acceptance")
        if not isinstance(acceptance, dict) or set(acceptance) != {"baseline", "measure", "negative_control", "owner"}:
            raise ValueError(f"{topic_id}: incomplete POC acceptance design")
        if any(not isinstance(value, str) or not value for value in acceptance.values()):
            raise ValueError(f"{topic_id}: empty POC acceptance field")
        transfer = teaching.get("transfer_check")
        if not isinstance(transfer, dict) or set(transfer) != {"title", "scenario", "question", "answer"}:
            raise ValueError(f"{topic_id}: teaching story needs a transfer check")
        if any(not isinstance(value, str) or not value for value in transfer.values()):
            raise ValueError(f"{topic_id}: incomplete transfer check")
        trace = teaching.get("review_trace")
        if not isinstance(trace, dict) or set(trace) != {"authority", "scope", "claims"}:
            raise ValueError(f"{topic_id}: teaching story needs claim traceability")
        claims = trace.get("claims")
        if not isinstance(trace.get("authority"), str) or not trace["authority"] or not isinstance(trace.get("scope"), str) or not trace["scope"]:
            raise ValueError(f"{topic_id}: incomplete claim traceability")
        if not isinstance(claims, list) or len(claims) < 6:
            raise ValueError(f"{topic_id}: claim traceability needs six claims")
        if any(not isinstance(claim, dict) or set(claim) != {"id", "field", "source"} or not all(isinstance(value, str) and value for value in claim.values()) for claim in claims):
            raise ValueError(f"{topic_id}: invalid claim trace entry")
        concept_visuals = teaching.get("concept_visuals")
        if not isinstance(concept_visuals, list) or (len(concept_visuals) < 3 and not (concept_visuals == [] and teaching.get("beginner_path"))):
            raise ValueError(f"{topic_id}: teaching story needs a beginner path or three concept bridge visuals")
        visual_fields = {"id", "placement", "title", "prompt", "caption", "image", "alt", "sequence", "callouts"}
        placements: set[str] = set()
        visual_ids: set[str] = set()
        for visual in concept_visuals:
            if not isinstance(visual, dict) or set(visual) != visual_fields:
                raise ValueError(f"{topic_id}: invalid concept bridge visual")
            if visual.get("placement") not in {"after_micro_example", "after_causal_chain", "before_boundary_cases", "after_comparison"}:
                raise ValueError(f"{topic_id}: invalid concept bridge placement")
            if visual.get("id") in visual_ids:
                raise ValueError(f"{topic_id}: duplicate concept bridge id")
            placements.add(visual["placement"])
            visual_ids.add(visual["id"])
            if not all(isinstance(visual.get(field), str) and visual[field] for field in ("id", "title", "prompt", "caption", "image", "alt")):
                raise ValueError(f"{topic_id}: incomplete concept bridge text")
            if not isinstance(visual.get("sequence"), int):
                raise ValueError(f"{topic_id}: concept bridge needs a sequence")
            callouts = visual.get("callouts")
            if not isinstance(callouts, list) or len(callouts) < 3:
                raise ValueError(f"{topic_id}: concept bridge needs at least three callouts")
            if any(not isinstance(item, dict) or not item.get("title") or not item.get("body") for item in callouts):
                raise ValueError(f"{topic_id}: invalid concept bridge callout")
            concept_images.append(verify_concept_asset(html_path, visual.get("image")))
        if not {"after_causal_chain", "before_boundary_cases", "after_comparison"} <= placements and not (not concept_visuals and teaching.get("beginner_path")):
            raise ValueError(f"{topic_id}: missing a required teaching-visual placement")

        beginner_path = teaching.get("beginner_path")
        if beginner_path is not None:
            if not isinstance(beginner_path, dict) or set(beginner_path) != {"title", "intro", "visuals"}:
                raise ValueError(f"{topic_id}: invalid image-led beginner path")
            if not all(isinstance(beginner_path.get(field), str) and beginner_path[field] for field in ("title", "intro")):
                raise ValueError(f"{topic_id}: incomplete image-led beginner path")
            beginner_visuals = beginner_path.get("visuals")
            if not isinstance(beginner_visuals, list) or len(beginner_visuals) < 3:
                raise ValueError(f"{topic_id}: image-led beginner path needs at least three visuals")
            beginner_ids: set[str] = set()
            for visual_index, visual in enumerate(beginner_visuals, start=1):
                if not isinstance(visual, dict) or not (visual_fields - {"placement"}) <= set(visual) or set(visual) - (visual_fields - {"placement"}) - {"reading_views", "core_ideas"}:
                    raise ValueError(f"{topic_id}: invalid image-led visual {visual_index}")
                if "core_ideas" in visual and type(visual["core_ideas"]) is not bool:
                    raise ValueError(f"{topic_id}: core_ideas must be a boolean")
                if visual.get("id") in beginner_ids:
                    raise ValueError(f"{topic_id}: duplicate image-led visual id")
                beginner_ids.add(visual["id"])
                if not all(isinstance(visual.get(field), str) and visual[field] for field in ("id", "title", "prompt", "caption", "image", "alt")):
                    raise ValueError(f"{topic_id}: incomplete image-led visual text")
                if not isinstance(visual.get("sequence"), int):
                    raise ValueError(f"{topic_id}: image-led visual needs a sequence")
                callouts = visual.get("callouts")
                if not isinstance(callouts, list) or len(callouts) < 2:
                    raise ValueError(f"{topic_id}: image-led visual needs at least two callouts")
                if any(not isinstance(item, dict) or not item.get("title") or not item.get("body") for item in callouts):
                    raise ValueError(f"{topic_id}: invalid image-led visual callout")
                if "reading_views" in visual:
                    views = visual["reading_views"]
                    if not isinstance(views, list) or not 1 <= len(views) <= 6:
                        raise ValueError(f"{topic_id}: invalid reading views")
                    for view in views:
                        fields = {"title", "image", "alt", "mobile_image", "mobile_crop"}
                        if not isinstance(view, dict) or (not fields <= set(view) or set(view) - fields - {"mobile_display_mode", "mobile_intrinsic_width", "mobile_intrinsic_height", "desktop_intrinsic_width", "desktop_intrinsic_height"}) or not all(isinstance(view[k], str) and view[k].strip() for k in fields - {"mobile_crop"}):
                            raise ValueError(f"{topic_id}: invalid reading view fields")
                        for key in ("image", "mobile_image"):
                            relative = view[key]
                            path = Path(relative)
                            if path.is_absolute() or ".." in path.parts or "\\" in relative or not relative.startswith("_course_content/generated-concepts/"):
                                raise ValueError(f"{topic_id}: unsafe reading view path")
                            verify_concept_asset(html_path, relative)
                        crop = view["mobile_crop"]
                        if not isinstance(crop, list) or len(crop) != 4 or any(type(v) is not int for v in crop):
                            raise ValueError(f"{topic_id}: invalid reading view crop")
                        x,y,w,h = crop
                        if view.get("mobile_display_mode", "crop") not in {"crop", "full-mobile"}:
                            raise ValueError(f"{topic_id}: invalid mobile display mode")
                        if view.get("mobile_display_mode") == "full-mobile":
                            with Image.open(checked_local_path(html_path, view["mobile_image"])) as im:
                                bounds = im.size
                            if bounds != (view.get("mobile_intrinsic_width", 720), view.get("mobile_intrinsic_height", 1660)):
                                raise ValueError(f"{topic_id}: mobile intrinsic dimensions mismatch")
                        else:
                            bounds = (1672, 941)
                        verify_crop(crop, bounds, f"{topic_id}: reading view")
                    if views[0]["image"] != visual["image"]:
                        raise ValueError(f"{topic_id}: reading view does not match visual image")
                asset = verify_concept_asset(html_path, visual["image"])
                first_read_images.append(asset)
                if visual_index == 1 and asset.suffix.lower() != ".png":
                    raise ValueError(f"{topic_id}: first image-led visual must be a raster PNG work example")
        deep_dive = teaching.get("deep_dive")
        if deep_dive is not None:
            deep_fields = {"title", "intro", "concept_path", "chapters", "sources"}
            if not isinstance(deep_dive, dict) or (not deep_fields <= set(deep_dive) or set(deep_dive) - deep_fields - {"default_collapsed"}):
                raise ValueError(f"{topic_id}: invalid model deep dive")
            if not all(isinstance(deep_dive.get(field), str) and deep_dive[field] for field in ("title", "intro", "concept_path")):
                raise ValueError(f"{topic_id}: incomplete model deep dive")
            if "default_collapsed" in deep_dive and type(deep_dive["default_collapsed"]) is not bool:
                raise ValueError(f"{topic_id}: default_collapsed must be boolean")
            concept_path = checked_local_path(html_path, deep_dive["concept_path"])
            if not concept_path.is_file() or concept_path.suffix.lower() != ".md":
                raise ValueError(f"{topic_id}: missing deep-dive concept document")
            sources = deep_dive.get("sources")
            source_fields = {"id", "label", "url", "scope"}
            if not isinstance(sources, list) or len(sources) < 3:
                raise ValueError(f"{topic_id}: deep dive needs source references")
            if any(
                not isinstance(source, dict)
                or set(source) != source_fields
                or not all(isinstance(source.get(field), str) and source[field] for field in source_fields)
                or not source["url"].startswith("https://")
                for source in sources
            ):
                raise ValueError(f"{topic_id}: invalid deep-dive source")
            source_ids = {source["id"] for source in sources}
            if len(source_ids) != len(sources):
                raise ValueError(f"{topic_id}: duplicate deep-dive source id")
            chapters = deep_dive.get("chapters")
            chapter_fields = {
                "id", "nav", "title", "summary", "image", "alt", "sequence",
                "points", "check", "source_ids",
            }
            if not isinstance(chapters, list) or len(chapters) != 8:
                raise ValueError(f"{topic_id}: deep dive needs eight chapters")
            chapter_ids: set[str] = set()
            for chapter_index, chapter in enumerate(chapters, start=1):
                if not isinstance(chapter, dict) or not chapter_fields <= set(chapter) or set(chapter) - chapter_fields - {"mobile_steps", "reading_views"}:
                    raise ValueError(f"{topic_id}: invalid deep-dive chapter {chapter_index}")
                if "reading_views" in chapter:
                    views = chapter["reading_views"]
                    if "mobile_steps" in chapter or not isinstance(views, list) or not 1 <= len(views) <= 6:
                        raise ValueError(f"{topic_id}: invalid reading views")
                    for view in views:
                        fields = {"title", "image", "alt", "mobile_image", "mobile_crop"}
                        if not isinstance(view, dict) or (not fields <= set(view) or set(view) - fields - {"mobile_display_mode", "mobile_intrinsic_width", "mobile_intrinsic_height", "desktop_intrinsic_width", "desktop_intrinsic_height"}) or not all(isinstance(view[k], str) and view[k].strip() for k in fields - {"mobile_crop"}):
                            raise ValueError(f"{topic_id}: invalid reading view fields")
                        for key in ("image", "mobile_image"):
                            relative = view[key]
                            path = Path(relative)
                            if path.is_absolute() or ".." in path.parts or "\\" in relative or not relative.startswith("_course_content/generated-concepts/"):
                                raise ValueError(f"{topic_id}: unsafe reading view path")
                            verify_concept_asset(html_path, relative)
                        crop = view["mobile_crop"]
                        if not isinstance(crop, list) or len(crop) != 4 or any(type(v) is not int for v in crop):
                            raise ValueError(f"{topic_id}: invalid reading view crop")
                        x,y,w,h = crop
                        if view.get("mobile_display_mode", "crop") not in {"crop", "full-mobile"}:
                            raise ValueError(f"{topic_id}: invalid mobile display mode")
                        if view.get("mobile_display_mode") == "full-mobile":
                            with Image.open(checked_local_path(html_path, view["mobile_image"])) as im:
                                bounds = im.size
                            if bounds != (view.get("mobile_intrinsic_width", 720), view.get("mobile_intrinsic_height", 1660)):
                                raise ValueError(f"{topic_id}: mobile intrinsic dimensions mismatch")
                        else:
                            bounds = (1672, 941)
                        verify_crop(crop, bounds, f"{topic_id}: reading view")
                    if views[0]["image"] != chapter["image"]:
                        raise ValueError(f"{topic_id}: reading view does not match chapter image")
                if "mobile_steps" in chapter:
                    steps = chapter["mobile_steps"]
                    if not isinstance(steps, list) or not 2 <= len(steps) <= 8:
                        raise ValueError(f"{topic_id}: invalid mobile steps")
                    for step in steps:
                        if not isinstance(step, dict) or set(step) != {"title", "body", "crop"} or not all(isinstance(step[k], str) and step[k].strip() for k in ("title", "body")):
                            raise ValueError(f"{topic_id}: invalid mobile step text")
                        crop = step["crop"]
                        if not isinstance(crop, list) or len(crop) != 4 or any(type(v) is not int for v in crop):
                            raise ValueError(f"{topic_id}: invalid mobile crop")
                        x, y, w, h = crop
                        verify_crop(crop, (1672, 941), f"{topic_id}: mobile step")
                if chapter.get("sequence") != chapter_index:
                    raise ValueError(f"{topic_id}: unexpected deep-dive chapter order")
                if chapter.get("id") in chapter_ids:
                    raise ValueError(f"{topic_id}: duplicate deep-dive chapter id")
                chapter_ids.add(chapter["id"])
                if not all(isinstance(chapter.get(field), str) and chapter[field] for field in ("id", "nav", "title", "summary", "image", "alt")):
                    raise ValueError(f"{topic_id}: incomplete deep-dive chapter text")
                if not isinstance(chapter.get("points"), list) or len(chapter["points"]) < 3:
                    raise ValueError(f"{topic_id}: deep-dive chapter needs three learning points")
                check = chapter.get("check")
                if not isinstance(check, dict) or set(check) != {"question", "answer"} or not all(check.values()):
                    raise ValueError(f"{topic_id}: deep-dive chapter needs a self check")
                chapter_sources = chapter.get("source_ids")
                if not isinstance(chapter_sources, list) or not chapter_sources or not set(chapter_sources) <= source_ids:
                    raise ValueError(f"{topic_id}: deep-dive chapter has invalid source links")
                deep_dive_images.append(verify_concept_asset(html_path, chapter["image"]))
        if not isinstance(teaching.get("slide_reading"), list) or len(teaching["slide_reading"]) != 4:
            raise ValueError(f"{topic_id}: teaching story needs four diagram-reading entries")
        slides = topic.get("slides")
        if not isinstance(slides, list) or len(slides) != 4:
            raise ValueError(f"{topic_id}: expected four teaching slides")
        for expected_index, slide in enumerate(slides, start=1):
            if slide.get("index") != expected_index:
                raise ValueError(f"{topic_id}: unexpected slide order")
            if not isinstance(slide.get("engineering"), dict):
                raise ValueError(f"{topic_id}: missing per-image engineering takeaway")
            plain = slide.get("plain")
            if not isinstance(plain, dict) or any(not plain.get(field) for field in ("look", "relation", "takeaway")):
                raise ValueError(f"{topic_id}: missing plain-language slide guide")
            slide_terms = slide.get("terms", [])
            if not isinstance(slide_terms, list) or any(not isinstance(term, str) or not term for term in slide_terms):
                raise ValueError(f"{topic_id}: invalid per-slide term explanations")
            images.append(verify_asset(html_path, slide.get("image"), "roadmap-model-selection/"))
            if "mobileImage" in slide:
                verify_asset(html_path, slide["mobileImage"], "roadmap-model-selection/", (slide.get("mobileWidth"), slide.get("mobileHeight")))
        if topic_id in ARCHITECTURE_TERM_TOPICS:
            architecture_terms = slides[1].get("terms", [])
            if not isinstance(architecture_terms, list) or len(architecture_terms) < 2:
                raise ValueError(f"{topic_id}: missing architecture-slide term explanations")
        brief = topic.get("engineeringBrief")
        if not isinstance(brief, dict) or not isinstance(brief.get("locks"), list) or len(brief["locks"]) != 4:
            raise ValueError(f"{topic_id}: incomplete engineering operation card")

    if len(images) != 232 or len(set(images)) != 232:
        raise ValueError(f"Expected 232 unique active images, found {len(images)} / {len(set(images))}")
    expected_concept_images = sum(len(topic["teachingStory"]["concept_visuals"]) for topic in topics)
    # Migrated first-read comparisons are checked in beginner_path above.
    # Preserve the accidental-alias guard for any remaining legacy bridges.
    verify_concept_reference_counts(html_path, concept_images, expected_concept_images)
    deep_dive_topic_count = sum(
        1 for topic in topics if topic["teachingStory"].get("deep_dive")
    )
    expected_deep_dive_images = deep_dive_topic_count * 8
    # Comparison chapters may intentionally reuse a previously inspected case.
    # Validate every reference above; uniqueness is not a teaching contract.
    if len(deep_dive_images) != expected_deep_dive_images:
        raise ValueError(
            f"Expected {deep_dive_topic_count} eight-image model deep dives, "
            f"found {len(deep_dive_images)} / {len(set(deep_dive_images))} images"
        )
    rendered_stories = [topic for topic in topics if isinstance(topic.get("teachingStory"), dict)]
    if len(rendered_stories) != 58:
        raise ValueError("Expected every topic to have a complete teaching story")
    if 'class="teaching-primer"' not in document or 'class="teaching-synthesis"' not in document or "function conceptVisualsHTML(topic, placement)" not in document or 'conceptVisualsHTML(topic, "after_causal_chain")' not in document or 'data-learning-path="image-led"' not in document or 'data-deep-dive="${escapeHTML(topic.id)}"' not in document:
        raise ValueError("Public HTML is missing the full-course teaching-story rendering hooks")
    if "輸入畫面 → 整理出可比較線索 → 算出候選結果 → 回到原圖確認。" in document:
        raise ValueError("Public HTML still contains the obsolete generic causal explanation")

    supporting = course.get("supporting")
    family_support = course.get("familySupport")
    if not isinstance(supporting, dict) or not isinstance(family_support, dict):
        raise ValueError("Missing shared foundations/production course content")
    expected_collections = {"foundations": 18, "production": 24}
    shared_images: list[Path] = []
    for name, expected_count in expected_collections.items():
        collection = supporting.get(name)
        items = collection.get("items") if isinstance(collection, dict) else None
        if not isinstance(items, list) or len(items) != expected_count:
            raise ValueError(f"{name}: expected {expected_count} shared pages")
        shared_images.extend(
            verify_asset(html_path, item.get("image"), "course-delivery/section-pages/")
            for item in items
        )

    expected_family_counts = {
        "geometry": 7,
        "classification": 6,
        "detector": 6,
        "anomaly": 10,
        "video": 5,
        "foundation": 6,
        "diffusion": 5,
    }
    for family, expected_count in expected_family_counts.items():
        items = family_support.get(family)
        if not isinstance(items, list) or len(items) != expected_count:
            raise ValueError(f"{family}: expected {expected_count} shared comparison pages")
        shared_images.extend(
            verify_asset(html_path, item.get("image"), "course-delivery/section-pages/")
            for item in items
        )
    if len(shared_images) != 87 or len(set(shared_images)) != 87:
        raise ValueError(f"Expected 87 unique shared images, found {len(shared_images)} / {len(set(shared_images))}")
    assets = referenced_assets(document)
    for relative in assets:
        asset = checked_local_path(html_path, relative.as_posix())
        if not asset.is_file():
            raise FileNotFoundError(f"Missing deployed reference: {asset}")
    print(f"PASS: {html_path.name}")
    print(f"  deployed references including mobile/SVG dependencies/documents: {len(assets)}")
    print(f"  topics: {len(topics)}")
    print(f"  topic images: {len(images)} (accepted native dimensions)")
    print(f"  concept bridge images: {len(set(concept_images))} unique / {len(concept_images)} lesson references (accepted native dimensions)")
    print(f"  image-led first-read visuals: {len(first_read_images)} across {sum(1 for topic in topics if topic['teachingStory'].get('beginner_path'))} migrated topics")
    print(f"  model deep-dive visuals: {len(deep_dive_images)} across {deep_dive_topic_count} deep-dive topics")
    print(f"  shared foundations / production / comparison images: {len(shared_images)} (accepted native dimensions)")
    print(f"  unique desktop teaching assets across the above layers: {len(set(images + concept_images + first_read_images + deep_dive_images + shared_images))}")
    print("  lesson flow: 58 model-specific lessons; optional eight-chapter deep dives; current demand-led PoC hooks present")
    print("  offline data: embedded; no fetch()")
    print("  HTML parser: passed")


if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_HTML
    validate(target)

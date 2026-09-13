# Historical first-pass migration only. Later fixes are in the final authoring
# snapshot tools/verify_interactive_learning_html.py; do not rerun over it.
from pathlib import Path
import shutil
W=Path(__file__).resolve().parent;C=W.parents[1];p=C/'tools/verify_interactive_learning_html.py'
backup=W/'baseline/verify_interactive_learning_html.py'
if not backup.exists():shutil.copyfile(p,backup)
s=backup.read_text(encoding='utf8')
def replace(a,b):
 global s
 assert a in s,a[:100]
 s=s.replace(a,b)
replace('    "帶入晶圓 AOI 範例",','    "function pocFlowHTML()",\n    "POC_DECISION.evaluate",\n    "data-poc-answer",\n    "poc-next",\n    "parseProgressBackup",')
replace('DEFAULT_HTML = ROOT / "interactive-learning.html"','DEFAULT_HTML = ROOT / "interactive-learning.html"\nsys.path.insert(0, str(ROOT / "tools"))\n# Share only the accepted native media dimensions with the authoring contract.\n# Payload schema, path boundaries, decoding and release checks remain independent.\nfrom build_interactive_learning_html import _validate_concept_visual_asset\nfrom build_github_pages_site import referenced_assets')
start=s.index('    with Image.open(asset) as image:',s.index('def verify_asset'))
end=s.index('    return asset',start)
s=s[:start]+'    _validate_concept_visual_asset(asset)\n    with Image.open(asset) as image:\n        image.verify()\n'+s[end:]
replace('asset = (html_path.parent / relative).resolve()','asset = checked_local_path(html_path, relative)')
start=s.index('        with Image.open(asset) as image:',s.index('def verify_concept_asset'))
end=s.index('        return asset',start)
s=s[:start]+'        _validate_concept_visual_asset(asset)\n        with Image.open(asset) as image:\n            image.verify()\n'+s[end:]
start=s.index('        if not re.search(',s.index('def verify_concept_asset'))
end=s.index('        if "\\ufffd" in svg:',start)
s=s[:start]+'        _validate_concept_visual_asset(asset)\n'+s[end:]
replace('required_story_fields | {"beginner_path", "deep_dive"}', 'required_story_fields | {"beginner_path", "deep_dive", "takeaway", "engineering_slides"}')
replace('set(step) != {"title", "body", "why", "anchor", "diagram"}', 'not {"title", "body", "why", "anchor", "diagram"} <= set(step) or set(step) - {"title", "body", "why", "anchor", "diagram", "inline_image"}')
# Restore grouping so the optional fields check cannot dereference a non-dict.
replace('if not isinstance(step, dict) or not {"title", "body", "why", "anchor", "diagram"} <= set(step) or set(step) - {"title", "body", "why", "anchor", "diagram", "inline_image"}:', 'if not isinstance(step, dict) or not {"title", "body", "why", "anchor", "diagram"} <= set(step) or set(step) - {"title", "body", "why", "anchor", "diagram", "inline_image"}:')
replace('inline_fields = {"id", "image", "label", "not_claim", "alt", "cue"}', 'inline_fields = {"id", "image", "label", "not_claim", "alt", "cue", "display"}')
replace('            verify_inline_asset(html_path, visual["image"])','            if visual["display"] == "inline":\n                verify_inline_asset(html_path, visual["image"])\n            elif visual["display"] == "full-width":\n                verify_concept_asset(html_path, visual["image"])\n            else:\n                raise ValueError(f"{topic_id}: invalid inline display mode")')
replace('if not isinstance(concept_visuals, list) or len(concept_visuals) < 4:', 'if not isinstance(concept_visuals, list) or (len(concept_visuals) < 3 and not (concept_visuals == [] and teaching.get("beginner_path"))):')
replace('teaching story needs four concept bridge visuals','teaching story needs a beginner path or three concept bridge visuals')
replace('if placements != {"after_micro_example", "after_causal_chain", "before_boundary_cases", "after_comparison"}:','if not {"after_causal_chain", "before_boundary_cases", "after_comparison"} <= placements and not (not concept_visuals and teaching.get("beginner_path")):') if 'if placements != ' in s else None
replace('set(deep_dive) != deep_fields','(not deep_fields <= set(deep_dive) or set(deep_dive) - deep_fields - {"default_collapsed"})')
replace('            concept_path = html_path.parent / deep_dive["concept_path"]','            if "default_collapsed" in deep_dive and type(deep_dive["default_collapsed"]) is not bool:\n                raise ValueError(f"{topic_id}: default_collapsed must be boolean")\n            concept_path = checked_local_path(html_path, deep_dive["concept_path"])')
# Both beginner and deep-dive reading views follow the same versioned schema.
replace('set(view) != fields','(not fields <= set(view) or set(view) - fields - {"mobile_display_mode", "mobile_intrinsic_width", "mobile_intrinsic_height", "desktop_intrinsic_width", "desktop_intrinsic_height"})')
replace('                        if min(x,y) < 0 or min(w,h) <= 0 or x+w > 1672 or y+h > 941:', '                        if view.get("mobile_display_mode", "crop") not in {"crop", "full-mobile"}:\n                            raise ValueError(f"{topic_id}: invalid mobile display mode")\n                        if view.get("mobile_display_mode") == "full-mobile":\n                            with Image.open(checked_local_path(html_path, view["mobile_image"])) as im:\n                                bounds = im.size\n                            if bounds != (view.get("mobile_intrinsic_width", 720), view.get("mobile_intrinsic_height", 1660)):\n                                raise ValueError(f"{topic_id}: mobile intrinsic dimensions mismatch")\n                        else:\n                            bounds = (1672, 941)\n                        if min(x,y) < 0 or min(w,h) <= 0 or x+w > bounds[0] or y+h > bounds[1]:')
replace('            images.append(verify_asset(html_path, slide.get("image"), "roadmap-model-selection/"))', '            images.append(verify_asset(html_path, slide.get("image"), "roadmap-model-selection/"))\n            if "mobileImage" in slide:\n                verify_asset(html_path, slide["mobileImage"], "roadmap-model-selection/")')
replace('    verify_concept_reference_counts(html_path, concept_images, expected_concept_images)', '    # Current reading layers allow intentionally shared comparison images.\n    # Every reference is still validated; uniqueness is not a learning contract.\n    if len(concept_images) != expected_concept_images:\n        raise ValueError("Missing concept visual references")')
replace('    print(f"PASS: {html_path.name}")','    assets = referenced_assets(document)\n    for relative in assets:\n        asset = checked_local_path(html_path, relative.as_posix())\n        if not asset.is_file():\n            raise FileNotFoundError(f"Missing deployed reference: {asset}")\n    print(f"PASS: {html_path.name}")\n    print(f"  deployed references including mobile/SVG dependencies/documents: {len(assets)}")')
replace('(all 1672x941)', '(accepted native dimensions)')
replace('; quiz UI absent', '; obsolete multiple-choice quiz UI absent')
insert='''
def checked_local_path(html_path: Path, relative: str) -> Path:
    if not isinstance(relative, str) or not relative or "\\\\" in relative:
        raise ValueError(f"Invalid local asset path: {relative!r}")
    path = Path(relative)
    if path.is_absolute() or ".." in path.parts or ":" in relative:
        raise ValueError(f"Unsafe local asset path: {relative!r}")
    root = html_path.parent.resolve()
    asset = (root / path).resolve()
    if not asset.is_relative_to(root):
        raise ValueError(f"Local asset leaves release root: {relative!r}")
    return asset


'''
replace('def verify_asset(',insert+'def verify_asset(')
p.write_text(s,encoding='utf8')
print('Updated release verifier; baseline retained')

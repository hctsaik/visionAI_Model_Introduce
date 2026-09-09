"""Build the self-contained GitHub Pages bundle for the interactive course."""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_HTML = ROOT / "interactive-learning.html"
DEFAULT_OUTPUT = ROOT / "docs"
ASSET_PATH = re.compile(
    r'(?:_course_content|course-delivery|roadmap-model-selection)/[^"\']+?\.(?:png|jpg|jpeg|webp|svg)',
    re.IGNORECASE,
)
CONCEPT_DOCUMENT_PATH = re.compile(
    r'"concept_path"\s*:\s*"(roadmap-model-selection/[^"\']+?\.md)"',
    re.IGNORECASE,
)
SVG_LOCAL_ASSET = re.compile(
    r'(?:href|xlink:href)=["\']([^"\'#?]+?\.(?:png|jpg|jpeg|webp|svg))["\']',
    re.IGNORECASE,
)


def referenced_assets(html: str) -> list[Path]:
    """Return every local visual and deep-dive document the lesson requests."""

    assets = (
        {Path(match) for match in ASSET_PATH.findall(html)}
        | {Path(match) for match in CONCEPT_DOCUMENT_PATH.findall(html)}
        | {Path(match) for match in re.findall(r'_course_content/supporting-lessons/(?:foundations|production)\.md', html)}
    )
    pending = [path for path in assets if path.suffix.lower() == ".svg"]
    inspected: set[Path] = set()
    while pending:
        svg_path = pending.pop()
        if svg_path in inspected:
            continue
        inspected.add(svg_path)
        source = ROOT / svg_path
        if not source.is_file():
            continue
        for match in SVG_LOCAL_ASSET.findall(source.read_text(encoding="utf-8")):
            dependency_source = (ROOT / svg_path.parent / Path(match)).resolve()
            try:
                dependency = dependency_source.relative_to(ROOT.resolve())
            except ValueError as exc:
                raise ValueError(
                    f"SVG asset dependency leaves the project root: {svg_path} -> {match}"
                ) from exc
            if dependency not in assets:
                assets.add(dependency)
                if dependency.suffix.lower() == ".svg":
                    pending.append(dependency)
    return sorted(assets)


def build(output: Path, *, clean: bool) -> tuple[int, int]:
    output = output.resolve()
    if output == ROOT.resolve():
        raise ValueError("The GitHub Pages output directory cannot be the project root")
    if output.exists() and clean:
        shutil.rmtree(output)
    output.mkdir(parents=True, exist_ok=True)

    html = SOURCE_HTML.read_text(encoding="utf-8")
    assets = referenced_assets(html)
    missing = [path for path in assets if not (ROOT / path).is_file()]
    if missing:
        sample = ", ".join(str(path) for path in missing[:5])
        raise FileNotFoundError(f"Missing {len(missing)} referenced asset(s): {sample}")

    shutil.copy2(SOURCE_HTML, output / "index.html")
    (output / ".nojekyll").write_text("\n", encoding="utf-8")
    total_bytes = (output / "index.html").stat().st_size
    for asset in assets:
        source = ROOT / asset
        target = output / asset
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        total_bytes += source.stat().st_size
    return len(assets), total_bytes


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a GitHub Pages course bundle")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--clean", action="store_true", help="replace the existing output directory")
    args = parser.parse_args()
    assets, total_bytes = build(args.output, clean=args.clean)
    print(f"Wrote {args.output.resolve() / 'index.html'}")
    print(f"Assets: {assets}; size: {total_bytes / 1024 / 1024:.1f} MB")


if __name__ == "__main__":
    main()

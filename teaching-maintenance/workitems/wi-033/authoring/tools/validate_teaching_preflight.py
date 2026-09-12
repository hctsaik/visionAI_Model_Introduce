"""Machine-check the five-file teaching preflight before a visual is promoted.

This is intentionally a gate, not a visual-quality oracle.  It verifies that a
workitem states the required lesson decision, reference, node count and
takeaway, and that the topic packet points to the same evidence.  Final PNG
inspection and user acceptance remain separate states.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


REQUIRED_FILES = {
    "CLAUDE.md",
    "IMAGE_STYLE_GUIDE.md",
    "TEACHING_REVIEW_LOG.md",
    "TEACHING_SCORING_RUBRIC.md",
    "TEACHING_WEBPAGE_GUIDE.md",
}


def field(text: str, name: str) -> str:
    match = re.search(rf"^- {re.escape(name)}:\s*(.+)$", text, re.MULTILINE)
    if not match:
        raise ValueError(f"missing preflight field: {name}")
    value = match.group(1).strip()
    if not value:
        raise ValueError(f"empty preflight field: {name}")
    return value


def validate(brief_path: Path, topic_path: Path | None = None) -> dict[str, object]:
    brief_path = brief_path.resolve()
    if topic_path is not None:
        topic_path = topic_path.resolve()
    text = brief_path.read_text(encoding="utf-8")
    objective = field(text, "lesson objective")
    page_type = field(text, "page type")
    reading_path = field(text, "primary reading path")
    reference = field(text, "named guide-conformant reference page")
    takeaway = field(text, "pale-yellow takeaway")
    if not re.search(r"\b[CD]\b", page_type):
        raise ValueError("page type must declare C or D")
    if reading_path.count("→") < 3:
        raise ValueError("primary reading path must contain problem/input → method → evidence/limit → action")
    node_lines = re.findall(r"^\s+\d+\.\s+.+$", text, re.MULTILINE)
    if len(node_lines) not in {3, 4}:
        raise ValueError(f"major visual nodes must contain exactly 3 or 4 entries, found {len(node_lines)}")
    if "#FFF4CC" not in text and "#fff4cc" not in text:
        raise ValueError("preflight must name the pale-yellow #FFF4CC takeaway")
    ref_path = reference.split("`")[1] if "`" in reference else reference.split(" —", 1)[0].strip()
    root = Path(__file__).resolve().parents[3]
    if not (root / ref_path).is_file():
        raise ValueError(f"reference page does not exist: {ref_path}")
    result: dict[str, object] = {
        "brief": brief_path.as_posix(),
        "objective": objective,
        "page_type": page_type,
        "node_count": len(node_lines),
        "reference": ref_path,
        "takeaway": takeaway,
        "required_files_present": sorted(path in {p.name for p in root.iterdir()} for path in REQUIRED_FILES),
    }
    missing = sorted(REQUIRED_FILES - {p.name for p in root.iterdir()})
    if missing:
        raise ValueError(f"required Markdown files missing: {missing}")
    if topic_path is not None:
        topic = json.loads(topic_path.read_text(encoding="utf-8"))
        packet = topic.get("teaching_preflight")
        if not isinstance(packet, dict):
            raise ValueError("topic packet has no teaching_preflight metadata")
        if packet.get("brief") != brief_path.relative_to(root).as_posix():
            raise ValueError("topic teaching_preflight.brief does not point to this brief")
        if packet.get("story") not in {"C", "D"}:
            raise ValueError("topic teaching_preflight.story must be C or D")
        if packet.get("major_visual_nodes") != len(node_lines):
            raise ValueError("topic node count does not match preflight")
        if packet.get("visual_status") == "approved":
            raise ValueError("user approval cannot be inferred by this gate")
        result["topic_visual_status"] = packet.get("visual_status")
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("brief", type=Path)
    parser.add_argument("--topic", type=Path)
    args = parser.parse_args()
    result = validate(args.brief, args.topic)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

from pathlib import Path
import sys
W=Path(__file__).resolve().parent;C=W.parents[1];R=C.parents[1]
note='## WI-041 完整 freeze 前審查\n\n'+sys.argv[1]+'\n\n唯一 checklist：teaching-images/vision-ai-model-selection/workitems/wi-041/PLAN.md。\n\n'
for p in [R/'WORKITEMS.md',C/'BEGINNER_VISUAL_TODO.md',C/'BEGINNER_VISUAL_STATUS.md']:p.write_text(note+p.read_text(encoding='utf8'),encoding='utf8')

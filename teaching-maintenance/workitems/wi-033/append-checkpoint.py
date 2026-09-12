from pathlib import Path
W=Path(__file__).resolve().parent;C=W.parents[1];R=C.parents[1]
note=(W/'checkpoint-note.md').read_text(encoding='utf-8')
for p in [R/'WORKITEMS.md',C/'BEGINNER_VISUAL_TODO.md',C/'BEGINNER_VISUAL_STATUS.md']:
 p.write_text(note+'\n\n'+p.read_text(encoding='utf-8'),encoding='utf-8')
with (W/'PLAN.md').open('a',encoding='utf-8') as f:f.write('\n\n'+note)

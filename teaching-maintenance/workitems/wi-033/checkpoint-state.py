from pathlib import Path
import json
W=Path(__file__).resolve().parent;C=W.parents[1];R=C.parents[1]
rows=json.loads((W/'inventory.json').read_text(encoding='utf-8'));done=[r for r in rows if r['status']=='local_complete']
message=f"第二部分完成 {len(done)}/52 課本機修正與驗證："+'、'.join(r['model'] for r in done)+'。'+(W/'current-action.md').read_text(encoding='utf-8').strip()+' 第二部分未commit/push，使用者成品核准pending。'
for p in [R/'WORKITEMS.md',C/'BEGINNER_VISUAL_TODO.md',C/'BEGINNER_VISUAL_STATUS.md',R/'Overall_Review.md']:
 s=p.read_text(encoding='utf-8');i=s.find('\n## ',3)
 if s.startswith('## WI-033') and i>=0:s=s[i:]
 p.write_text('## WI-033 最新 checkpoint（2026-09-12）\n\n'+message+' 細項入口：teaching-images/vision-ai-model-selection/workitems/wi-033/PLAN.md。\n'+s,encoding='utf-8')
with (W/'PLAN.md').open('a',encoding='utf-8') as f:f.write('\n## 接續 checkpoint\n\n'+message+'\n')

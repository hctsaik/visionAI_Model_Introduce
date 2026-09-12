import json,runpy
from pathlib import Path
W=Path(__file__).resolve().parent
m=runpy.run_path(str(W/'plan-batch6-prototypes.py'));owners=[d[0] for d in m['defs']]
p=W/'engineering-plan.json';rows=json.loads(p.read_text(encoding='utf-8'));out=[]
for r in rows:
 if r['owner'] in owners and r['index']==2:
  r['version']='r02';f=W/(r['id']+'-r02.md');f.write_text(m['brief'](r)+'\n修正r01實際審查：分組相加雙側符號、特徵格與字距、DDAD加噪原件含刮傷、Win同尺寸重疊窗、Byte第二工件、影片背景與文字分離。\n',encoding='utf-8');out.append(m['v'].validate(f))
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8');(W/'batch6-prototype-r02-preflight-validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
(W/'checkpoint-note.md').write_text('### WI-033 第六批16原型實看與修正\n\n第五批完成，累計33/52。第六批r01逐張原生實看，發現兩窗尺寸矛盾/第二工件缺失/圖文重疊/長字溢出；r02八份preflight通過，即將渲染16PNG。尚未再審、擴展24故事或整合。使用者核准pending，全部52課持續。\n',encoding='utf-8');runpy.run_path(str(W/'append-checkpoint.py'))

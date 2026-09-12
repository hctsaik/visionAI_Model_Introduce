from pathlib import Path
import json,subprocess,sys,runpy
W=Path(__file__).resolve().parent
owners=['ad-patchcore','ad-padim','ad-subspacead','ad-stfpm','ad-rd4ad','ad-ae','ad-draem','ad-uniad']
ids=[r['id'] for r in json.loads((W/'engineering-plan.json').read_text(encoding='utf-8')) if r['owner'] in owners and r['index'] in [1,3,4]];assert len(ids)==24
note='''### WI-033 第五批其餘48工程PNG即將渲染

24故事preflight與具體SVG路由已完成，原型16PNG已審；即將render.py产出24故事48張PNG，尚未實看/整合。新增容量、污染、正則化、全維投影、AE複製/孔模糊與跨類驗證例，保持同件；PatchCore第二章2張手機已生成待審。完成25/52，使用者核准pending，全部52課持續。下一步逐張審查並整合第五批。產物workitems/wi-033。
'''
(W/'checkpoint-note.md').write_text(note,encoding='utf-8');runpy.run_path(str(W/'append-checkpoint.py'))
subprocess.run([sys.executable,str(W/'render.py'),*ids],check=True)

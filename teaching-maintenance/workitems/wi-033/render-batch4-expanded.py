from pathlib import Path
import json,subprocess,sys,runpy
W=Path(__file__).resolve().parent
rows=[r for r in json.loads((W/'engineering-plan.json').read_text(encoding='utf-8')) if r['panels'][0]['graphic'].startswith('b4-') and r['index']!=2]
assert len(rows)==24
note='''### WI-033 第四批其餘24工程故事即將渲染

八原型16PNG已原生審查，DINOv2 r03其餘r02；其餘24故事preflight與具體SVG路由已完成。即將render-batch4-expanded.py產出48張1672×941/768×2304候選PNG，尚未原生實看/整合/頁內驗證。使用原PCB雙電阻、L支架與接頭/銘牌的機制、映射、查庫距離及交付例；不跑模型。DINOv2/Gemini兩主反例仍待獨立修正。完成17/52，下一步逐圖審查與兩主反例，再整合八課。產物在workitems/wi-033，使用者核准pending。
'''
(W/'checkpoint-note.md').write_text(note,encoding='utf-8');runpy.run_path(str(W/'append-checkpoint.py'))
subprocess.run([sys.executable,'-X','utf8',str(W/'render.py'),*[r['id'] for r in rows]],check=True)

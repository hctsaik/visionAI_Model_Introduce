from pathlib import Path
import json,importlib.util
W=Path(__file__).resolve().parent;C=W.parents[1]
p=W/'engineering-plan.json';rows=json.loads(p.read_text(encoding='utf-8'));r=next(x for x in rows if x['id']=='dinov2-engineering-2');r['version']='r03';r['detail']+=' Teacher目標[.2,.8]與Student預測[.6,.4]只作對齊示意，並非真實表示维度。'
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
p=W/'dinov2-engineering-2-r03.md';p.write_text((W/'dinov2-engineering-2-r02.md').read_text(encoding='utf-8')+'\n新增具體Teacher目標與Student預測兩維示意，讓箭頭兩端有對齊對象。未重跑模型，PNG審查pending。\n',encoding='utf-8')
spec=importlib.util.spec_from_file_location('v',C/'tools/validate_teaching_preflight.py');v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v);v.validate(p)
print('DINOv2 r03 preflight passed; two PNGs pending')

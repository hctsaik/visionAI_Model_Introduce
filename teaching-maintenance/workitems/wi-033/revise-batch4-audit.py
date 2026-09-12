from pathlib import Path
import json,importlib.util,runpy,subprocess,sys
W=Path(__file__).resolve().parent;C=W.parents[1]
p=W/'engineering-plan.json';rows=json.loads(p.read_text(encoding='utf-8'));ids=[];checks=[]
spec=importlib.util.spec_from_file_location('v',C/'tools/validate_teaching_preflight.py');v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
for r in rows:
 if not any(x['graphic']=='b4-det-audit' for x in r['panels']):continue
 r['version']='r02';ids.append(r['id'])
 r['panels'][-1]['title']='另驗定位偏移與漏框'
 path=W/(r['id']+'-r02.md');s=(W/(r['id']+'-r01.md')).read_text(encoding='utf-8')+'\n修訂：末格改為另驗定位偏移與漏框。避免把高重疊同類重複框放在明確NMS去重後，造成同一算例前後矛盾。此處是另一測試例，不是假稱中格輸出失效。原生審查pending。\n';path.write_text(s,encoding='utf-8');checks.append(v.validate(path))
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8');(W/'batch4-audit-r02-preflight-validation.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2),encoding='utf-8')
note='''### WI-033 第四批桌機審查：驗收例前後一致

24工程候選48PNG與兩反例4PNG產出，正在逐張原生看。前三種detector工程3末格原畫高重疊重複框，接在明確NMS後容易造成同算例矛盾；改為「另驗定位偏移與漏框」，保留前述去重算例。三份r02 preflight通過，即將重渲染6PNG；其他桌機與全部手機審查未完，未整合。完成17/52，使用者核准pending。
'''
(W/'checkpoint-note.md').write_text(note,encoding='utf-8');runpy.run_path(str(W/'append-checkpoint.py'))
subprocess.run([sys.executable,'-X','utf8',str(W/'render.py'),*ids],check=True)

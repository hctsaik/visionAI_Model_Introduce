from pathlib import Path
import json,importlib.util,runpy
W=Path(__file__).resolve().parent;C=W.parents[1]
owners=['ad-patchcore','ad-padim','ad-subspacead','ad-stfpm','ad-rd4ad','ad-ae','ad-draem','ad-uniad']
p=W/'engineering-plan.json';rows=json.loads(p.read_text(encoding='utf-8'))
spec=importlib.util.spec_from_file_location('v',C/'tools/validate_teaching_preflight.py');v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v);out=[]
for r in rows:
 if r['owner'] not in owners or r['index']!=2:continue
 r['version']='r02';target=W/(r['id']+'-r02.md')
 target.write_text((W/(r['id']+'-r01.md')).read_text(encoding='utf-8')+'\n## r02 原生桌機審查修正\n八張r01桌機已實看，手機未審未啟用。PatchCore距離簡式避免超框，PaDiM縮短分布標籤且標q/縮小橢圓避免壓算式；Subspace殘差工件上移，RD瓶頸上移避免壓圖說；STFPM三層改明示已對齊網格同位置p；AE標q，DRAEM補實際合成mask小圖，UniAD明示p中心局部取用。三節點/讀序/結論不變。即將渲染16PNG；原生/頁內/user仍pending。\n',encoding='utf-8');out.append(v.validate(target))
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8');(W/'batch5-prototype-r02-preflight-validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
note='''### WI-033 第五批原型桌機審查補修

第四批已完整本機完成，累計25/52。第五批八張r01桌機原生實看，發現PatchCore/PaDiM文字超框、PaDiM橢圓壓算式、RD瓶頸壓圖說；同時補STFPM已對齊同位置、AE q與DRAEM mask、UniAD局部範圍。八份r02 preflight通過，即將渲染16PNG，r01未整合。第五批手機、擴展24故事/PatchCore第二章深讀待做；使用者核准pending，全部52課繼續。
'''
(W/'checkpoint-note.md').write_text(note,encoding='utf-8');runpy.run_path(str(W/'append-checkpoint.py'))

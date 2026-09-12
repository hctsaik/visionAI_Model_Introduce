from pathlib import Path
import json,runpy,importlib.util
W=Path(__file__).resolve().parent;C=W.parents[1]
m=runpy.run_path(str(W/'plan-batch7-prototypes.py'))
notes={'convlstm':'下一步明畫卷積門控與X(t+1)，避免誤讀直接預測圖像。','videomae':'解碼重建格上移，與caption保留間距。','v-jepa':'目標格與EMA文字分離。','defectfill':'候選A改為淡刮傷，不把正常原圖配非零距離。','anomalydiffusion':'恢復原板上方兩孔，保留大左下小右下雙傷；條件pill與caption分離。','controlnet':'輪廓外框與孔框同用白線。','inpainting':'保持原下方黑污點，不任意換成刮傷。'}
rows=json.loads((W/'engineering-plan.json').read_text(encoding='utf-8'))
sp=importlib.util.spec_from_file_location('v',C/'tools/validate_teaching_preflight.py');v=importlib.util.module_from_spec(sp);sp.loader.exec_module(v);out=[]
for r in rows:
 if r['owner'] in notes and r['index']==2:
  assert r['version']=='r01';r['version']='r02';r['detail']+=' r01實看修正：'+notes[r['owner']]
  p=W/(r['id']+'-r02.md');p.write_text(m['brief'](r),encoding='utf-8');out.append(v.validate(p))
(W/'engineering-plan.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
(W/'batch7-prototype-r02-preflight-validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
(W/'batch7-prototype-r01-review.json').write_text(json.dumps({'reviewed':22,'revisions':notes,'retained':['tf-idg','diffusion-restoration','deblur','super-resolution'],'native_review':'all 22 viewed; seven need revision; other four pass','user_approval':'pending'},ensure_ascii=False,indent=2),encoding='utf-8')
(W/'checkpoint-note.md').write_text('### WI-033 第七批22原型實看與修正\n\n11課桌機/手機22PNG已逐張實看。7課需修正狀態語意、孔位/污點身份或圖說間距，r02 preflight通過；即將渲染14修正版，尚未再審。其餘4課原型原生通過。33擴展、SR主反例與整合驗頁未完成；完成仍41/52。產物batch7-prototype-r01-review與r02-preflight-validation。全部52課持續，使用者核准pending。\n',encoding='utf-8')
runpy.run_path(str(W/'append-checkpoint.py'))

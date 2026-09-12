from pathlib import Path
import json,runpy,importlib.util,subprocess,sys
W=Path(__file__).resolve().parent;C=W.parents[1];m=runpy.run_path(str(W/'plan-batch7-prototypes.py'))
notes={'convlstm-engineering-3':'时间刻度及標籤各自定位，避免SVG空白合併。','videomae-engineering-3':'时间刻度及標籤各自定位。','v-jepa-engineering-3':'时间刻度及標籤各自定位。','videomae-engineering-4':'99格/1格都明寫平方差，避免把差100誤讀成平方後1萬。','diffusion-restoration-engineering-1':'比較A估計與原觀測，依噪聲模型檢殘差；不宣稱知道真實n。','diffusion-restoration-engineering-3':'依噪聲模型驗殘差，並將結論寫成明確可做的條件核對。','diffusion-restoration-engineering-4':'錯退化反例保留完整同板，在右外框畫多重邊；噪聲容許條件明寫。','deblur-engineering-3':'真邊/估計/差值移出影像並以同色標明，避免跨邊界。'}
rows=json.loads((W/'engineering-plan.json').read_text(encoding='utf-8'));sp=importlib.util.spec_from_file_location('v',C/'tools/validate_teaching_preflight.py');v=importlib.util.module_from_spec(sp);sp.loader.exec_module(v);checks=[]
for r in rows:
 if r['id'] not in notes:continue
 assert r['version']=='r01';r['version']='r02';r['detail']+=' r01實看修正：'+notes[r['id']]
 if r['id']=='diffusion-restoration-engineering-3':r['takeaway']='退化條件改變，模型與驗證也要重新核對。'
 p=W/(r['id']+'-r02.md');p.write_text(m['brief'](r),encoding='utf-8');checks.append(v.validate(p))
(W/'engineering-plan.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
(W/'batch7-expanded-r02-preflight-validation.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2),encoding='utf-8')
(W/'batch7-expanded-r01-review.json').write_text(json.dumps(dict(native_reviewed=66,revisions=notes,main_r02_review='2 PNG viewed; passed native',user_approval='pending'),ensure_ascii=False,indent=2),encoding='utf-8')
(W/'checkpoint-note.md').write_text('### WI-033 第七批66擴展與SR原生實看\n\n33擴展桌機/手機66PNG全部逐張實看，8故事需修时间刻度、平方差名詞、噪聲驗證/同板反例或文字跨影像；r02 preflight通過，即將渲染16PNG，尚未再審。SR同件主反例r02兩PNG已實看通過，尚未接入。完成41/52；工程整合/44頁狀態/回歸/全站驗證未跑。全部52課持續，使用者核准pending。\n',encoding='utf-8');runpy.run_path(str(W/'append-checkpoint.py'))
subprocess.run([sys.executable,str(W/'render.py'),*notes],check=True)

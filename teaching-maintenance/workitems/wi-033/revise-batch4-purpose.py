from pathlib import Path
import json,importlib.util,subprocess,sys,runpy
W=Path(__file__).resolve().parent;C=W.parents[1]
p=W/'engineering-plan.json';rows=json.loads(p.read_text(encoding='utf-8'))
defs={'det-grounding-dino-interface-engineering-1':[('影像與文字定義想找的類別','ground-task'),('一個詞語對應兩件物件','ground-link'),('交付詞語相關的框','ground-output')],'llava-engineering-1':[('同接頭加上檢查問題','vlm-task'),('先核對左右可見內容','vlm-observation'),('交付描述與未知原因','vlm-result')],'gemini-vision-engineering-1':[('同接頭加上檢查問題','vlm-task'),('先定義左右與原因欄位','gemini-fields'),('回原圖核對可見內容','vlm-observation')],'llava-engineering-3':None,'gemini-vision-engineering-3':None}
spec=importlib.util.spec_from_file_location('v',C/'tools/validate_teaching_preflight.py');v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v);out=[]
for r in rows:
 if r['id'] not in defs:continue
 r['version']='r02'
 if defs[r['id']]:r['panels']=[dict(title=a,graphic='b4-'+b) for a,b in defs[r['id']]]
 if r['id']=='gemini-vision-engineering-1':r['detail']='依公開影像API的輸入與輸出介面設計工作欄位，未呼叫服務或猜測私有骨幹。先固定接頭與問題，定義left/right可見狀態及cause未知欄位，再回原圖核對；欄位設計不是API回覆，格式不能保證內容。工程2才深入請求與錯誤JSON處理。'
 path=W/(r['id']+'-r02.md');s=(W/(r['id']+'-r01.md')).read_text(encoding='utf-8')+'\n修訂：工程1專注任務/交付，與工程2機制圖去除整張重複；Gemini使用公開模型識別/schema設定，不暗示私有processor。覆核文字縮短留邊距。更新節點：'+' → '.join(x['title'] for x in r['panels'])+'。PNG審查pending。\n';path.write_text(s,encoding='utf-8');out.append(v.validate(path))
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8');(W/'batch4-purpose-r02-preflight-validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
note='''### WI-033 第四批工程分工補修

24張擴展桌機r01已實看，全部手機尚待看；三個detector工程3 r02產出未複核。Grounding/LLaVA/Gemini工程1與工程2整張過度重複，改工程1為任務、詞區域對應與欄位交付；工程2保留機制。另縮短LLaVA/Gemini覆核文字，Gemini設定改公開模型識別/schema。五份r02 preflight通過，即將渲染10PNG，未整合。原型仍16PNG通過，兩主反例4PNG待看。完成17/52，使用者核准pending。
'''
(W/'checkpoint-note.md').write_text(note,encoding='utf-8');runpy.run_path(str(W/'append-checkpoint.py'))
subprocess.run([sys.executable,'-X','utf8',str(W/'render.py'),*defs],check=True)

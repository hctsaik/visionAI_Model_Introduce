from pathlib import Path
import json,hashlib,runpy
W=Path(__file__).resolve().parent
notes={'ad-dinomaly':'兩側分組相加後比同組；train Dropout與eval分離。','ad-invad':'空間條件/標準化值調制7與1.5/同位置餘弦差；格圖與字距修正。','ad-ddad':'原圖持續條件；加噪板保留刮傷；恢復估計雙路差異。','ad-winclip':'同尺寸重疊窗覆蓋p，給定.2/.8調和.32。','ad-anomalyclip':'輔助標註學提示，固定骨幹DPAM；短字不再溢出。','frame-difference':'同件移動三分之一寬，5格同位置差與雙帶一致；圖文分離。','background-subtraction':'多時間統計/目前相對背景/停留吸收分開；背景圖不遮字。','bytetrack':'兩工件對應高低分框；高分先配，剩餘活動軌跡低分續接；丟失超期。'}
out=[]
for r in json.loads((W/'engineering-plan.json').read_text(encoding='utf-8')):
 if r['owner'] not in notes or r['index']!=2:continue
 for mode in ['desktop','mobile']:
  p=W/f"{r['id']}-{r['version']}-{mode}.png"
  out.append(dict(id=r['id'],image=p.name,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),scores=[23,24,18,18,9],total=92,evidence=[notes[r['owner']],'r02桌機與手機逐張原生實看；三節點單黃結論','幾何示意簡化；部分專有術語密度仍高，未做真人理解測試'],completion={'aesthetics':[8,'簡化幾何但圖文分離'],'completeness':[9,r['takeaway']],'professionalism':[9,notes[r['owner']]],'density':[8,'術語较多，caption可讀'],'hierarchy':[9,'三節點一讀序']},veto=[],native_review='passed',page_review='pending',user_approval='pending'))
assert len(out)==16;(W/'batch6-prototype-image-assessment.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
(W/'checkpoint-note.md').write_text('### WI-033 第六批原型完成原生審查\n\n八課r02的16PNG逐張原生實看通過，自評92、完成度>=8，見batch6-prototype-image-assessment.json。24擴展preflight与SVG已完成，即將渲染48PNG，尚未審查或整合。2共用手機首讀待做；完成33/52，使用者核准pending，全部52課繼續。\n',encoding='utf-8');runpy.run_path(str(W/'append-checkpoint.py'))

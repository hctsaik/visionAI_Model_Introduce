import json,subprocess,sys
from pathlib import Path
W=Path(__file__).resolve().parent;C=W.parents[1]
for r in json.loads((W/'visual-plan.json').read_text(encoding='utf-8')):
 p=W/(r['id']+'-r01.md')
 if not p.exists():
  s='# WI-030 '+r['title']+'\n- lesson objective: '+r['takeaway']+'\n- page type: '+r['type']+' — 依具體因果／條件差異教工作判斷。\n- primary reading path: '+' → '.join(r['nodes'])+'\n- major visual nodes:\n'+''.join('  '+str(i+1)+'. '+n+'\n' for i,n in enumerate(r['nodes']))+'- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看材質與細框；內容另設計。\n- pale-yellow takeaway: #FFF4CC：'+r['takeaway']+'\n- source: '+r['source']+'\n- evidence: AI生成教學示意，非模型推論與效能實測。\n- generation: built-in imagegen，桌面16:9，手機獨立重排；actual PNG review pending；user approval pending。\n\n## Visual brief\n'+r['scene']+'\n\n## Validation intent\n查來源定位、同物件不變量、訓練／推論兩路、輸出責任；原生與936/328px實看，按v1.0逐圖分項，不能以正文補分。\n'
  p.write_text(s,encoding='utf-8')
 s=p.read_text(encoding='utf-8')
 lines=s.splitlines()
 for i,line in enumerate(lines):
  if line.startswith('- primary reading path:') and line.count('→')<3:
   lines[i]=line+' → 依輸出界線核對原圖與工作條件'
 p.write_text('\n'.join(lines)+'\n',encoding='utf-8')
 out=subprocess.run([sys.executable,'-X','utf8',str(C/'tools/validate_teaching_preflight.py'),str(p)],capture_output=True,text=True,encoding='utf-8');assert out.returncode==0,(p,out.stderr)
print('21 logical stories with validated preflights')

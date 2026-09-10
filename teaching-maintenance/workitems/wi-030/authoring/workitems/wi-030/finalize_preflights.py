import json,subprocess,sys
from pathlib import Path
W=Path(__file__).resolve().parent;C=W.parents[1]
plans={r['id']:r for r in json.loads((W/'visual-plan.json').read_text(encoding='utf-8'))}
selected=json.loads((W/'selected-assets.json').read_text(encoding='utf-8'))
for id,row in selected.items():
 r=plans[id]
 for mode in ['desktop','mobile']:
  stem=Path(row[mode]).stem;p=W/(stem+'.md')
  promptfile=W/(stem+'-prompt.json')
  prompt=promptfile.read_text(encoding='utf-8') if promptfile.exists() else '原始生成意圖見本故事歷史preflight及prototype-review.md。'
  s='# WI-030 '+r['title']+' — '+mode+'\n- lesson objective: '+r['takeaway']+'\n- page type: '+r['type']+'\n- primary reading path: '+' → '.join(r['nodes'])+' → 核對輸出與工作條件\n- major visual nodes:\n'+''.join('  '+str(i+1)+'. '+n+'\n' for i,n in enumerate(r['nodes']))+'- named guide-conformant reference page: teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png\n- pale-yellow takeaway: #FFF4CC：'+r['takeaway']+'\n- source: '+r['source']+'\n- generation: built-in imagegen；教學示意非模型實測。\n- actual PNG review: reviewed；原生與936/328px證據見prototype-review.md；這是候選選定，不是使用者核准。\n- user approval: pending\n\n## 版本與生成意圖\n產物：'+row[mode]+'。原型生成前已有同故事r01及逐版preflight，本檔彙整實際選用版本，保留歷史。\n\n'+prompt+'\n'
  p.write_text(s,encoding='utf-8')
  subprocess.run([sys.executable,'-X','utf8',str(C/'tools/validate_teaching_preflight.py'),str(p)],check=True,stdout=subprocess.DEVNULL)
print('Validated',len(selected)*2,'selected preflights')

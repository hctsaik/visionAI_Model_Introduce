from pathlib import Path
import json,importlib.util,runpy,subprocess,sys
W=Path(__file__).resolve().parent;C=W.parents[1]
p=W/'engineering-plan.json';rows=json.loads(p.read_text(encoding='utf-8'))
defs=[('dinov2','同一支架的小缺口，特徵仍可能很相近','相近特徵不能證明完整，先回原圖查細節。',[('同L支架，只改一小段邊緣','dino-failure-pair'),('表示很近，不代表允收','dino-failure-vectors'),('回同一缺口查可見線索','dino-failure-detail')],'改用首讀同L支架兩孔工件，完整/缺口只在右緣小段不同。兩維特徵[.20,.80]/[.21,.79]距離約.014是作者給定反例，不是模型實測；近距離不代表沒有缺口。先核對原圖，必要時比較局部取樣或下游方法，不期待門檻補回已丟失線索。'),('gemini-vision','同一圓接頭：JSON能解析仍可能填錯','格式通過不等於內容通過，欄位要對回原圖。',[('左有螺絲，右是空座','gemini-failure-input'),('反例JSON錯填右側present','gemini-json'),('分開驗格式與可見內容','gemini-failure-gates')],'保留主線左右圓接頭，左有螺絲右空座。作者設計的JSON把兩側填present，格式可解析但右欄與影像矛盾；應核對not_visible，原因仍未知。未呼叫API、未猜測內部模型結構。')]
out=[];ids=[]
spec=importlib.util.spec_from_file_location('v',C/'tools/validate_teaching_preflight.py');v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
for o,title,take,panels,detail in defs:
 rid=o+'-main-failure';ids.append(rid)
 if not any(r['id']==rid for r in rows):rows.append(dict(id=rid,owner=o,index=0,version='r01',title=title,takeaway=take,kind='D',mobile_height=2304,panels=[dict(title=a,graphic='b4-'+b) for a,b in panels],steps=[],detail=detail,source=next(r['source'] for r in rows if r['owner']==o),review='pending'))
 path=W/(rid+'-r01.md');body='# '+title+'\n- lesson objective: '+take+'\n- page type: D\n- primary reading path: '+' → '.join([a for a,b in panels]+[take])+'\n- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`\n- pale-yellow takeaway: '+take+' #FFF4CC\n- major visual nodes:\n'+'\n'.join(f'  {i+1}. {a}；{b}' for i,(a,b) in enumerate(panels))+'\n\n'+detail+'\n模式：新精確SVG→1672×941／768×2304PNG。原主線實看，三節點同件反例。\n權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。\nPNG review pending；page review pending；user approval pending。\n';path.write_text(body,encoding='utf-8');out.append(v.validate(path))
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8');(W/'batch4-main-failure-preflight-validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
note='''### WI-033 兩個同件主反例即將渲染

第四批24故事48工程PNG正在渲染，尚未逐圖看。兩個主反例preflight通過：DINOv2同L支架右緣小缺口＋給定近距離反例；Gemini主線同圓接頭的格式/內容雙檢查。即將產出4PNG，未審查/整合/驗頁；不新增模型實測。產物workitems/wi-033/{dinov2,gemini-vision}-main-failure-r01-*.png。完成17/52，所有後續課程持續，使用者核准pending。
'''
(W/'checkpoint-note.md').write_text(note,encoding='utf-8');runpy.run_path(str(W/'append-checkpoint.py'))
subprocess.run([sys.executable,'-X','utf8',str(W/'render.py'),*ids],check=True)

import json,shutil,re,hashlib,sys
from pathlib import Path
from PIL import Image
W=Path(__file__).resolve().parent;C=W.parents[1];sys.path.insert(0,str(C/'tools'))
from sync_model_learning_bridges import bridge,replace_bridge
data=json.loads((W/'lesson-content.json').read_text(encoding='utf-8'))
plans={r['id']:r for r in json.loads((W/'visual-plan.json').read_text(encoding='utf-8'))}
selected=json.loads((W/'selected-assets.json').read_text(encoding='utf-8'))
lp=C/'_course_content/learner-briefs.json';learn=json.loads(lp.read_text(encoding='utf-8'))
owners={'flow-d2':'lucas-kanade','video-d2':'videomae','change-d3':'frame-difference','flow-d3':'lucas-kanade','track-d3':'bytetrack','video-d3':'convlstm'}
groups={
'change-d3':[
 {'model':'Frame Difference','normality':'前一影格或指定時刻；選取間隔、門檻和事件規則','candidate':'像素變化；停住後可能消失'},
 {'model':'背景相減','normality':'初始化和更新背景模型；處理光照／陰影','candidate':'相對常態的前景；停久可能被吸收'},
 {'model':'工件偵測／占位感測','normality':'偵測需相應類別資料，感測器需現場安裝與驗證','candidate':'類別框或占位訊號；代價依任務比較'}],
'flow-d3':[
 {'model':'Lucas–Kanade稀疏追點','normality':'不需權重；選角點、窗口、金字塔與幀間隔','candidate':'選定點位移；需檢查追丟與錯配'},
 {'model':'原始RAFT','normality':'預訓練權重、相容前處理、迭代與運算預算','candidate':'稠密像素位移；遮擋仍可能不可靠'},
 {'model':'傳統稠密光流基準','normality':'如Farnebäck；設定尺度和局部估計參數','candidate':'稠密位移；同影片比較誤差、覆蓋及成本'}],
'track-d3':[
 {'model':'逐幀偵測','normality':'相應類別框標註與偵測器；先測漏檢','candidate':'每張框；不直接維持身分'},
 {'model':'偵測＋SORT基準','normality':'相同偵測框、運動預測與關聯設定','candidate':'軌跡ID；遮擋及漏檢可能斷軌'},
 {'model':'偵測＋ByteTrack','normality':'相同偵測器；先高分、再低分補未配對軌跡','candidate':'軌跡ID；計數另設規則並測ID切換'}],
'video-d3':[
 {'model':'ConvLSTM應用','normality':'連續片段、任務標註；訓練空間記憶與任務頭','candidate':'依任務定義的序列輸出；管理狀態／重置'},
 {'model':'VideoMAE原版','normality':'像素重建預訓練；可用現有權重，需下游標註','candidate':'影片表示＋任務頭；重建不是現場判定'},
 {'model':'V-JEPA 2024原版','normality':'特徵預測預訓練；可用現有權重，需下游標註','candidate':'影片表示＋任務頭；不是未來影片生成'}]}
for slug in sys.argv[1:] or data:
 a=data[slug];p=C/'_course_content/topics'/f'{slug}.json';t=json.loads(p.read_text(encoding='utf-8'))
 visuals=[];manifest=[]
 for i,id in enumerate(a['assets']):
  r=plans[id];record=selected[id];urls=[];sizes=[]
  for mode in ['desktop','mobile']:
   assert record.get(mode+'_reviewed'),(id,mode,'not reviewed')
   src=W/record[mode];folder=C/'_course_content/generated-concepts'/owners.get(id,slug);folder.mkdir(exist_ok=True)
   dest=folder/('wi028-'+src.name);shutil.copy2(src,dest);size=Image.open(dest).size
   urls.append(dest.relative_to(C).as_posix());sizes.append(size)
   manifest.append({'id':id,'mode':mode,'image':urls[-1],'size':size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'generation':'built-in imagegen','evidence':'illustrative, not model inference','user_review':'pending'})
  caption=[a['core'],a['failure'],a['compare']][i]
  if id=='conv-d2':caption+=' 圖中的夾爪小圖用來表示狀態意義，不是記憶張量的實際外觀。'
  alt=r['title']+'。'+caption+' AI生成教學示意，非模型實測。'
  view={'title':r['title'],'image':urls[0],'mobile_image':urls[1],'alt':alt,'mobile_crop':[0,0,*sizes[1]],'mobile_display_mode':'full-mobile','desktop_intrinsic_width':sizes[0][0],'desktop_intrinsic_height':sizes[0][1],'mobile_intrinsic_width':sizes[1][0],'mobile_intrinsic_height':sizes[1][1]}
  cs=[a['ideas']+[['交付與接手',a['output']]],[['看哪裡',a['failure']],['接著怎麼做',a['action']]],[['怎麼選',a['compare']],['資料與完整成本',a['change']]]][i]
  visuals.append({'id':'wi028-'+id,'title':r['title'],'prompt':[a['problem'],'觀察哪個條件改變，讓原本的結果不夠可靠？','相同工作需求下，資料、輸出與成本如何取捨？'][i],'caption':caption,'image':urls[0],'alt':alt,'callouts':[{'title':x,'body':y} for x,y in cs],'reading_views':[view],'core_ideas':i==0})
 q=a['quiz'];t.update({'badge':a['kind'],'title':a['title'],'scenario':{'title':a['problem'],'body':a['problem']},'promise':{'title':'交付結果與接手工作','body':a['output']},'mental_model':{'title':a['kind'],'body':a['core'],'limit':a['failure']},'micro_example':dict(zip(['title','setup','prediction','reveal'],q)),'visual_intro':a['core'],'selection':a['compare']+' '+a['change'],'teach_back':{'question':'它改變什麼？何時選另一種做法？','answer':a['core']+' '+a['compare']},'transfer_check':dict(zip(['title','scenario','question','answer'],q)),'comparison':groups[a['assets'][2]],'comparison_headers':{'title':plans[a['assets'][2]]['title'],'basis':'所需資料與方法差異','output':'輸出與維護責任'}})
 t['beginner_path']={'title':'從必要原理、具體反例到工作取捨','intro':a['problem']+' 下列圖像、特徵及回答為教學示意，不是模型實測。','visuals':visuals}
 desc=[a['ideas'][0][1],a['ideas'][1][1],a['output'],a['evidence']]
 t['mechanism_steps']=[{'title':n,'body':d,'why':'由本課核心機制連接工作用途','anchor':f'WI028-{i+1}','diagram':{'title':n,'body':d,'why':'詳見本課版本與來源','anchor':f'WI028-{i+1}'}} for i,(n,d) in enumerate(zip(plans[a['assets'][0]]['nodes']+['工作核對與接手'],desc))]
 t['boundary_cases']=[{'condition':'本課具體反例','effect':a['failure'],'action':a['action']},{'condition':'更換產品、模型或輸入設定','effect':a['change'],'action':a['first']},{'condition':'把示意當成實際推論','effect':'本課特徵、排序、回答及圖像僅用於解釋，不支持現場準確率或耗時結論。','action':a['evidence']}]
 t['poc']={'title':'以真實工作資料做小規模比較','steps':[a['first'],a['change'],a['evidence']],'hold':a['action'],'acceptance':{'baseline':'既有流程或最簡單可行方法','measure':a['evidence'],'negative_control':a['failure'],'owner':'實作與影像核對負責人'}}
 t['quality_status']={'label':'新版已整合，驗證中','state':'needs_revision','round':'WI-028','reason':'首讀重製已整合；逐圖及整頁證據另記，使用者成品核准pending。'}
 core_record=selected[a['assets'][0]]
 t['teaching_preflight']={'brief':'teaching-images/vision-ai-model-selection/workitems/wi-028/'+core_record['desktop'].replace('-desktop.png','.md'),'mobile_brief':'teaching-images/vision-ai-model-selection/workitems/wi-028/'+core_record['mobile'].replace('-mobile.png','.md'),'story':'C','major_visual_nodes':len(plans[a['assets'][0]]['nodes']),'visual_status':'self-reviewed','user_review':'pending'}
 t['review_trace']['scope']='WI-028 八個時序主題首讀圖文與手機PNG、反例、比較及自測；原工程slide保留，未以首讀評分代替工程圖審查。'
 t['review_trace']['claims']=[x for x in t['review_trace']['claims'] if not x['id'].startswith('wi028-')]+[{'id':'wi028-first-read','field':'beginner_path + core + selection + transfer','source':plans[a['assets'][0]]['source']}]
 p.write_text(json.dumps(t,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 learn[slug].update({'problem':a['problem'],'first':a['first'],'hold':a['action'],'deliverable':a['output'],'evidence':a['evidence'],'terms':[a['kind']]+[x+'：'+y for x,y in a['ideas']]})
 mp=C/t['review_trace']['authority'];s=replace_bridge(mp.read_text(encoding='utf-8'),bridge(slug,t))
 section='<!-- wi028-model-core:start -->\n## WI-028 核心做法與工作取捨\n\n'+'\n\n'.join(a[k] for k in ['core','failure','compare','change','first','evidence'])+'\n\n來源：'+plans[a['assets'][0]]['source']+'\n\n版本及示意界線見工作項目 sources.md。使用者成品核准pending。\n<!-- wi028-model-core:end -->'
 s=re.sub(r'<!-- (?:f02|wi028)-model-core:start -->.*?<!-- (?:f02|wi028)-model-core:end -->',lambda _:section,s,flags=re.S);
 if '<!-- wi028-model-core:start -->' not in s:s+='\n\n'+section+'\n'
 mp.write_text(s,encoding='utf-8')
 (W/f'{slug}-active-assets.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8');print('Integrated',slug)
lp.write_text(json.dumps(learn,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

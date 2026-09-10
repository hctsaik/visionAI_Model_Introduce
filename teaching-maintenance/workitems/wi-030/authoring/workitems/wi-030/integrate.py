import json,shutil,re,hashlib,sys
from pathlib import Path
from PIL import Image
W=Path(__file__).resolve().parent;C=W.parents[1];sys.path.insert(0,str(C/'tools'))
from sync_model_learning_bridges import bridge,replace_bridge
data=json.loads((W/'lesson-content.json').read_text(encoding='utf-8'))
plans={r['id']:r for r in json.loads((W/'visual-plan.json').read_text(encoding='utf-8'))}
selected=json.loads((W/'selected-assets.json').read_text(encoding='utf-8'))
lp=C/'_course_content/learner-briefs.json';learn=json.loads(lp.read_text(encoding='utf-8'))
owners={id:r['owner'] for id,r in plans.items()}
groups={
'ad-d3':[
 {'model':'PatchCore','normality':'正常CNN局部特徵＋代表子集庫','candidate':'局部最近鄰差異；維護庫大小與覆蓋'},
 {'model':'PaDiM','normality':'每位置平均與共變異','candidate':'位置條件距離；維護對位與分布'},
 {'model':'AnomalyDINO','normality':'DINOv2區塊特徵正常參考','candidate':'特徵相似度；維護表示與參考'},
 {'model':'EfficientAD','normality':'正常訓練教師／學生與AE關係','candidate':'局部＋全域差；維護權重及校準'}],
'class-d3':[
 {'model':'ResNet','normality':'類別標註；殘差特徵相加','candidate':'已知類別；同資料測錯誤與成本'},
 {'model':'ConvNeXt','normality':'類別標註；現代空間／通道卷積','candidate':'已知類別；不能以模型新舊排名'},
 {'model':'ViT','normality':'類別標註；區塊表示與注意力','candidate':'已知類別；注意力不是輪廓真值'}],
'seg-d3':[
 {'model':'U-Net','normality':'像素標註；編碼解碼同尺度跳接','candidate':'語意區域；邊界與尺度需另驗'},
 {'model':'SegFormer','normality':'像素標註；階層特徵多尺度融合','candidate':'語意區域；不自動提供每件ID'},
 {'model':'YOLOv8-seg例','normality':'每件標註；原型＋每件係數','candidate':'每件框與遮罩；漏檢重疊逐件驗'}],
'pose-d3':[
 {'model':'Keypoint R-CNN','normality':'每件框與點名標註；工業任務訓練','candidate':'2D點及物件歸屬'},
 {'model':'幾何與相機資料','normality':'同名3D點、內參畸變與一致單位','candidate':'把2D點接到幾何問題'},
 {'model':'PnP姿態流程','normality':'足夠正確對應；適用求解與多解驗證','candidate':'物體→相機姿態；接工站需外參'}]}
for slug in sys.argv[1:] or data:
 a=data[slug];p=C/'_course_content/topics'/f'{slug}.json';t=json.loads(p.read_text(encoding='utf-8'))
 visuals=[];manifest=[]
 for i,id in enumerate(a['assets']):
  r=plans[id];record=selected[id];urls=[];sizes=[]
  for mode in ['desktop','mobile']:
   assert record.get(mode+'_reviewed'),(id,mode,'not reviewed')
   src=W/record[mode];folder=C/'_course_content/generated-concepts'/owners.get(id,slug);folder.mkdir(exist_ok=True)
   dest=folder/('wi030-'+src.name);shutil.copy2(src,dest);size=Image.open(dest).size
   urls.append(dest.relative_to(C).as_posix());sizes.append(size)
   manifest.append({'id':id,'mode':mode,'image':urls[-1],'size':size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'generation':'built-in imagegen','evidence':'illustrative, not model inference','user_review':'pending'})
  caption=[a['core'],a['failure'],a['compare']][i]
  
  alt=r['title']+'。'+caption+' AI生成教學示意，非模型實測。'
  view={'title':r['title'],'image':urls[0],'mobile_image':urls[1],'alt':alt,'mobile_crop':[0,0,*sizes[1]],'mobile_display_mode':'full-mobile','desktop_intrinsic_width':sizes[0][0],'desktop_intrinsic_height':sizes[0][1],'mobile_intrinsic_width':sizes[1][0],'mobile_intrinsic_height':sizes[1][1]}
  cs=[a['ideas']+[['交付與接手',a['output']]],[['看哪裡',a['failure']],['接著怎麼做',a['action']]],[['怎麼選',a['compare']],['資料與完整成本',a['change']]]][i]
  visuals.append({'id':'wi030-'+id,'title':r['title'],'prompt':[a['problem'],'觀察哪個條件改變，讓原本的結果不夠可靠？','相同工作需求下，資料、輸出與成本如何取捨？'][i],'caption':caption,'image':urls[0],'alt':alt,'callouts':[{'title':x,'body':y} for x,y in cs],'reading_views':[view],'core_ideas':i==0})
 q=a['quiz'];t.update({'badge':a['kind'],'title':a['title'],'scenario':{'title':a['problem'],'body':a['problem']},'promise':{'title':'交付結果與接手工作','body':a['output']},'mental_model':{'title':a['kind'],'body':a['core'],'limit':a['failure']},'micro_example':dict(zip(['title','setup','prediction','reveal'],q)),'visual_intro':a['core'],'selection':a['compare']+' '+a['change'],'teach_back':{'question':'它改變什麼？何時選另一種做法？','answer':a['core']+' '+a['compare']},'transfer_check':dict(zip(['title','scenario','question','answer'],q)),'comparison':groups[a['assets'][2]],'comparison_headers':{'title':plans[a['assets'][2]]['title'],'basis':'所需資料與方法差異','output':'輸出與維護責任'}})
 t['beginner_path']={'title':'從必要原理、具體反例到工作取捨','intro':a['problem']+' 下列圖像、特徵及回答為教學示意，不是模型實測。','visuals':visuals}
 desc=[a['ideas'][0][1],a['ideas'][1][1],a['output'],a['evidence']]
 t['mechanism_steps']=[{'title':n,'body':d,'why':'由本課核心機制連接工作用途','anchor':f'WI030-{i+1}','diagram':{'title':n,'body':d,'why':'詳見本課版本與來源','anchor':f'WI030-{i+1}'}} for i,(n,d) in enumerate(zip(plans[a['assets'][0]]['nodes']+['工作核對與接手'],desc))]
 t['boundary_cases']=[{'condition':'本課具體反例','effect':a['failure'],'action':a['action']},{'condition':'更換產品、模型或輸入設定','effect':a['change'],'action':a['first']},{'condition':'把示意當成實際推論','effect':'本課特徵、排序、回答及圖像僅用於解釋，不支持現場準確率或耗時結論。','action':a['evidence']}]
 t['poc']={'title':'以真實工作資料做小規模比較','steps':[a['first'],a['change'],a['evidence']],'hold':a['action'],'acceptance':{'baseline':'既有流程或最簡單可行方法','measure':a['evidence'],'negative_control':a['failure'],'owner':'實作與影像核對負責人'}}
 if 'deep_dive' in t:t['deep_dive']['default_collapsed']=True
 t['quality_status']={'label':'新版已整合，驗證中','state':'needs_revision','round':'WI-030','reason':'首讀重製已整合；逐圖及整頁證據另記，使用者成品核准pending。'}
 core_record=selected[a['assets'][0]]
 t['teaching_preflight']={'brief':'teaching-images/vision-ai-model-selection/workitems/wi-030/'+core_record['desktop'].replace('.png','.md'),'mobile_brief':'teaching-images/vision-ai-model-selection/workitems/wi-030/'+core_record['mobile'].replace('.png','.md'),'story':'C','major_visual_nodes':len(plans[a['assets'][0]]['nodes']),'visual_status':'self-reviewed','user_review':'pending'}
 t['review_trace']['scope']='WI-030 十二課首讀圖文與手機PNG、反例、比較及自測；原工程slide保留，未以首讀評分代替工程圖審查。'
 t['review_trace']['claims']=[x for x in t['review_trace']['claims'] if not x['id'].startswith('wi030-')]+[{'id':'wi030-first-read','field':'beginner_path + core + selection + transfer','source':plans[a['assets'][0]]['source']}]
 p.write_text(json.dumps(t,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 learn[slug].update({'problem':a['problem'],'first':a['first'],'hold':a['action'],'deliverable':a['output'],'evidence':a['evidence'],'terms':[a['kind']]+[x+'：'+y for x,y in a['ideas']]})
 mp=C/t['review_trace']['authority'];s=replace_bridge(mp.read_text(encoding='utf-8'),bridge(slug,t))
 section='<!-- wi030-model-core:start -->\n## WI-030 核心做法與工作取捨\n\n'+'\n\n'.join(a[k] for k in ['core','failure','compare','change','first','evidence'])+'\n\n來源：'+plans[a['assets'][0]]['source']+'\n\n版本及示意界線見工作項目 sources.md。使用者成品核准pending。\n<!-- wi030-model-core:end -->'
 s=re.sub(r'<!-- (?:f02|wi030)-model-core:start -->.*?<!-- (?:f02|wi030)-model-core:end -->',lambda _:section,s,flags=re.S);
 if '<!-- wi030-model-core:start -->' not in s:s+='\n\n'+section+'\n'
 mp.write_text(s,encoding='utf-8')
 (W/f'{slug}-active-assets.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8');print('Integrated',slug)
lp.write_text(json.dumps(learn,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

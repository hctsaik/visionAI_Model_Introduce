from pathlib import Path
import json,re,shutil,sys,hashlib
from PIL import Image
W=Path(__file__).resolve().parent;C=W.parents[1]
inventory={r['id']:r for r in json.loads((W/'inventory.json').read_text(encoding='utf-8'))}
rows=json.loads((W/'engineering-plan.json').read_text(encoding='utf-8'))
reviews={r['image']:r for p in W.glob('*image-assessment.json') for r in json.loads(p.read_text(encoding='utf-8'))}
owners=sys.argv[1:];assert owners,'Explicit owner scope required'
manifest=[]
for owner in owners:
 meta=inventory[owner];tp=C/meta['topic_source'];t=json.loads(tp.read_text(encoding='utf-8'));folder=(C/meta['model_path']).parent
 old=(W/'baseline'/meta['manifest_path']).read_text(encoding='utf-8')
 original=[(re.search(r'`([^`]+-0[1-4])`',line).group(1),re.search(r'`(images/final/[^`]+\.png)`',line).group(1)) for line in old.splitlines() if re.search(r'`([^`]+-0[1-4])`',line)]
 assert len(original)==4
 selected=sorted([r for r in rows if r['owner']==owner and r['index'] in [1,2,3,4]],key=lambda r:r['index']);assert len(selected)==4
 lines=['# '+t['model']+' slide manifest','','| slide_id | 教學目標 | 版型 | active asset | 狀態 |','| --- | --- | --- | --- | --- |'];slides=[]
 for r in selected:
  sid=original[r['index']-1][0];urls=[];sizes=[]
  for mode in ['desktop','mobile']:
   src=W/f"{r['id']}-{r['version']}-{mode}.png";review=reviews[src.name]
   assert review['native_review']=='passed' and review['sha256']==hashlib.sha256(src.read_bytes()).hexdigest()
   dest=folder/'images/final'/f"WI033-{sid}-{r['version']}-{mode}.png";shutil.copyfile(src,dest);urls.append(dest.relative_to(C).as_posix());sizes.append(Image.open(dest).size)
   manifest.append(dict(id=r['id'],mode=mode,path=urls[-1],sha256=review['sha256'],native_review='passed',page_review='pending',user_approval='pending'))
  look='先看'+r['panels'][0]['title']+'，再核對'+r['panels'][1]['title']+'，最後看'+r['panels'][2]['title']+'。'
  family_terms={'pose':['R/t：物體座標到相機座標的旋轉／平移。','重投影：把已知3D點投回影像，與同名觀測點比較。'],'dinov3':['patch：影像的局部區塊，特徵可包含其他位置的資訊。','Gram：同一影像內，各patch特徵兩兩相似關係的矩陣。'],'ad-diffad':['A/R：原始影像與恢復影像，兩者都送進分割。','N：高噪聲分支的正常估計，用來引導恢復。'],'ad-anomalygpt':['位置圖：模型內建圖文匹配支路產生的定位線索。','提示學習器：把定位線索轉為LLM能使用的提示表示。']}
  terms=r.get('terms',family_terms.get(owner,['表示：模型把輸入轉成可比較的資料。','示意結果：解釋流程，不代表本輪模型實測。']))
  s=dict(title=r['title'],question=r['takeaway'],plain=dict(look=look,relation=r['detail'],takeaway=r['takeaway']),terms=terms,guide=[r['detail'],look],stages=[{'title':p['title'],'body':r['steps'][i] if r.get('steps') else p['title']+'；請對照圖內輸入、變化與結果。'} for i,p in enumerate(r['panels'])],misconception=t['mental_model']['limit'],alt=r['title']+'。'+r['takeaway']+' 教學示意，非模型實測。',mobile_image=urls[1],mobile_width=sizes[1][0],mobile_height=sizes[1][1],engineering=dict(takeaway=r['takeaway'],nextAction=t['micro_example']['reveal'],redLine=t['mental_model']['limit']),source=r['source'])
  s['engineering'].update(nextAction=r.get('next_action',t['poc']['steps'][0]),redLine=t['poc']['hold'])
  slides.append(s);lines.append(f"| `{sid}` | {r['title']} | {r['kind']} | `{Path(urls[0]).relative_to(folder.relative_to(C)).as_posix()}` | native_reviewed_page_pending_user_pending |")
 t['engineering_slides']=slides;t['slide_reading']=[dict(title=s['title'],question=s['question'],**s['plain'],terms=s['terms']) for s in slides]
 # The old optional bridge repeats the superseded generic engineering figures.
 t['concept_visuals']=[]
 t['review_trace']['scope']='WI-033：工程層四圖與手機比較修正；首讀有效內容保留。原生圖已審，整頁與使用者審閱另記。'
 if owner in ['clip','siglip']:
  comparison=next(r for r in rows if r['id']=='alignment-comparison');src=W/'alignment-comparison-r01-mobile.png';assert reviews[src.name]['native_review']=='passed'
  dest=C/'_course_content/generated-concepts/clip/wi033-alignment-comparison-r01-mobile.png';shutil.copyfile(src,dest)
  v=t['beginner_path']['visuals'][2];rv=v['reading_views'][0];rv['mobile_image']=dest.relative_to(C).as_posix();rv['mobile_crop']=[0,0,768,2304];rv['mobile_intrinsic_width']=768;rv['mobile_intrinsic_height']=2304
  rv['alt']=v['title']+'。桌機為原有生成示意；手機為 WI-033 原生SVG比較示意，均非模型實測。'
 tp.write_text(json.dumps(t,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 lines+=['','## 保留的歷史來源（非目前啟用）']+[f'- [{sid}]({img})' for sid,img in original]
 (folder/'slide-manifest.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
 mp=folder/'model.md';body=mp.read_text(encoding='utf-8');section='<!-- wi033-engineering:start -->\n## WI-033 工程圖修正\n\n'
 for r in selected:section+='### '+r['title']+'\n\n'+r['detail']+'\n\n'+r['takeaway']+'\n\n來源：'+r['source']+'\n\n'
 section+='<!-- wi033-engineering:end -->'
 body=re.sub(r'<!-- wi033-engineering:start -->.*?<!-- wi033-engineering:end -->','',body,flags=re.S).rstrip()+'\n\n'+section+'\n';mp.write_text(body,encoding='utf-8')
 print('Integrated local source:',owner)
(W/('active-assets-'+'-'.join(owners)+'.json')).write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')

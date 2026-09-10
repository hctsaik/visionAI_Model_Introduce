from pathlib import Path
import json,re,shutil,hashlib
from PIL import Image
W=Path(__file__).resolve().parent;C=W.parents[1]
rows=json.loads((W/'engineering-plan.json').read_text(encoding='utf-8'));lessons=json.loads((W/'lesson-content.json').read_text(encoding='utf-8'))
manifest=[]
for slug,a in lessons.items():
 p=C/'_course_content/topics'/f'{slug}.json';t=json.loads(p.read_text(encoding='utf-8'));folder=(C/t['review_trace']['authority']).parent
 old=(W/'baseline'/folder.relative_to(C)/'slide-manifest.md').read_text(encoding='utf-8')
 original=[(re.search(r'`([^`]+-0[1-4])`',line).group(1),re.search(r'`(images/final/[^`]+\.png)`',line).group(1)) for line in old.splitlines() if re.search(r'`([^`]+-0[1-4])`',line)]
 assert len(original)==4
 newlines=['# '+t['model']+' slide manifest','','| slide_id | 教學目標 | 版型 | active asset | 狀態 |','| --- | --- | --- | --- | --- |']
 slides=[]
 for r in [r for r in rows if r['owner']==slug]:
  n=r['index'];sid,oldimage=original[n-1];urls=[];sizes=[]
  for mode in ['desktop','mobile']:
   # The one further spacing correction has its own version.
   version='r06' if r['id']=='sift-engineering-1' else ('r05' if r['id']=='yolo-world-engineering-2' else 'r04')
   src=W/f"{r['id']}-{version}-{mode}.png";assert src.exists(),src
   dest=folder/'images/final'/f'WI032-{sid}-{version}-{mode}.png';shutil.copy2(src,dest);urls.append(dest.relative_to(C).as_posix());sizes.append(Image.open(dest).size)
   manifest.append(dict(id=r['id'],mode=mode,image=urls[-1],size=sizes[-1],sha256=hashlib.sha256(dest.read_bytes()).hexdigest(),generation='new SVG rendered by browser',evidence='illustrative, not model inference',actual_page_review='pending',user_review='pending'))
  assert sizes[0]==(1672,941)
  reading=dict(title=r['title'],question=r['takeaway'],look='先看'+r['nodes'][0]+'，再看'+r['nodes'][1]+'，最後核對'+r['nodes'][2]+'。',relation=r['detail'],takeaway=r['takeaway'],terms=[])
  item=dict(title=r['title'],question=r['takeaway'],plain={k:reading[k] for k in ['look','relation','takeaway']},terms=[],guide=[r['detail'],'讀圖：'+' → '.join(r['nodes'])],stages=[{'title':v['title'],'body':'；'.join(v['lines'])} for v in r['panels']],misconception=a['failure'] if n==4 else '示意只解釋本步驟，不可當作模型實測或省略後續核對。',alt=r['title']+'。'+r['takeaway']+' 教學示意，非本輪模型實測。',mobile_image=urls[1],mobile_width=sizes[1][0],mobile_height=sizes[1][1],engineering={'takeaway':r['takeaway'],'nextAction':a['first'],'redLine':a['action']},source=r['source'])
  if slug=='ecc' and n==4:
   evidence=(folder/oldimage).relative_to(C).as_posix()
   item['evidence_links']=[{'title':'保留的反光／遮擋／視差案例原圖（依原圖標示判讀，本輪未重跑）','image':evidence}]
  slides.append(item)
  item['terms']=[v['title']+'：'+'；'.join(v['lines']) for v in r['panels'][:2]]
  newlines.append(f"| `{sid}` | {r['title']} | {r['kind']} | `{Path(urls[0]).relative_to(folder.relative_to(C)).as_posix()}` | implementation_pending_validation_user_review |")
 t['engineering_slides']=slides
 t['slide_reading']=[dict(title=s['title'],question=s['question'],**s['plain'],terms=s['terms']) for s in slides]
 # Superseded visuals must not reappear in optional teaching bridges.
 t['concept_visuals']=[]
 t['review_trace']['scope']='WI-032：六課主線及工程層圖文重建；既有ECC案例保留。頁內驗證與使用者核准另記。'
 p.write_text(json.dumps(t,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 newlines+=['','## 保留的既有來源','','本輪新工程圖為機制示意；以下舊圖留存以便核對既有案例及版本，不代表本輪新實測。']+[f'- [{sid} 原圖]({img})' for sid,img in original]
 (folder/'slide-manifest.md').write_text('\n'.join(newlines)+'\n',encoding='utf-8')
 mp=folder/'model.md';body=mp.read_text(encoding='utf-8');section='<!-- wi032-engineering:start -->\n## 工程層：輸入、機制、部署與限制\n\n'
 for r in [r for r in rows if r['owner']==slug]:section+='### '+r['title']+'\n\n'+r['detail']+'\n\n'+r['takeaway']+'\n\n來源：'+r['source']+'\n\n'
 section+='<!-- wi032-engineering:end -->'
 body=re.sub(r'<!-- wi032-engineering:start -->.*?<!-- wi032-engineering:end -->','',body,flags=re.S).rstrip()+'\n\n'+section+'\n';mp.write_text(body,encoding='utf-8')
 print('Integrated engineering',slug)
(W/'engineering-active-assets.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')

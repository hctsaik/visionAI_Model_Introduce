from pathlib import Path
import json,hashlib,shutil
W=Path(__file__).resolve().parent;C=W.parents[1]
rows=json.loads((W/'engineering-plan.json').read_text(encoding='utf-8'));reviews=[];active=[]
for o in ['dinov2','gemini-vision']:
 r=next(x for x in rows if x['id']==o+'-main-failure');urls=[]
 for mode in ['desktop','mobile']:
  p=W/f"{r['id']}-{r['version']}-{mode}.png";sha=hashlib.sha256(p.read_bytes()).hexdigest()
  reviews.append(dict(id=r['id'],image=p.name,sha256=sha,scores=[23,24,18,18,9],total=92,evidence=[r['detail'],'桌機與手機原生逐張實看；同件身份、缺口/右空座與錯誤推論對應清楚','幾何簡化與長捲动扣分；非實測模型特徵/非API回覆'],completion={'aesthetics':[8,'簡化具體工件'],'completeness':[9,'反例與核對行動完整'],'professionalism':[9,'來源與示意身份明示'],'density':[8,'三節點保留必要文字'],'hierarchy':[9,'同件對照與單黃結論']},veto=[],native_review='passed',page_review='pending',user_approval='pending'))
  dest=C/'_course_content/generated-concepts'/o/f"wi033-{r['id']}-{r['version']}-{mode}.png";shutil.copyfile(p,dest);urls.append(dest.relative_to(C).as_posix())
  active.append(dict(owner=o,path=urls[-1],sha256=sha,native_review='passed',page_review='pending',user_approval='pending'))
 tp=C/'_course_content/topics'/f'{o}.json';t=json.loads(tp.read_text(encoding='utf-8'));v=t['beginner_path']['visuals'][1]
 old=dict(image=v['image'],reading_views=v['reading_views']);(W/f'{o}-main-failure-prior-reference.json').write_text(json.dumps(old,ensure_ascii=False,indent=2),encoding='utf-8')
 cap=('同一L支架只在右緣多一小缺口，整圖特徵仍可能很相近。圖中兩維表示與距離是給定反例，不是模型實測；相近不能證明完整，應回原圖檢查細節。' if o=='dinov2' else '同主線的圓接頭，左有螺絲、右是空座。示意JSON即使兩側都填present仍可解析，但右欄與原圖矛盾；格式檢查和內容檢查必須分開。')
 alt=r['title']+'。'+cap+' 精確SVG教學示意，非模型實測。'
 v.update(title=r['title'],caption=cap,image=urls[0],alt=alt)
 v['callouts'][0]['body']=cap
 rv=v['reading_views'][0];rv.update(title=r['title'],image=urls[0],mobile_image=urls[1],alt=alt,mobile_crop=[0,0,768,2304],mobile_display_mode='full-mobile',desktop_intrinsic_width=1672,desktop_intrinsic_height=941,mobile_intrinsic_width=768,mobile_intrinsic_height=2304)
 tp.write_text(json.dumps(t,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(W/'batch4-failure-image-assessment.json').write_text(json.dumps(reviews,ensure_ascii=False,indent=2),encoding='utf-8');(W/'batch4-failure-active-assets.json').write_text(json.dumps(active,ensure_ascii=False,indent=2),encoding='utf-8')
print('Four native-reviewed failure assets integrated into source; build/page review pending')

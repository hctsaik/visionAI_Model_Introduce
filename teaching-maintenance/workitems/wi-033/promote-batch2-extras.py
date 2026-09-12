from pathlib import Path
import json,hashlib,shutil
from PIL import Image
W=Path(__file__).resolve().parent;C=W.parents[1]
rows={r['id']:r for r in json.loads((W/'engineering-plan.json').read_text(encoding='utf-8'))}
reviews={r['image']:r for r in json.loads((W/'batch2-image-assessment.json').read_text(encoding='utf-8'))}
active=[]
def asset(id,owner,mode):
 r=rows[id];src=W/f"{id}-{r['version']}-{mode}.png";review=reviews[src.name]
 assert review['native_review']=='passed' and review['sha256']==hashlib.sha256(src.read_bytes()).hexdigest()
 dest=C/f"_course_content/generated-concepts/{owner}/wi033-{id}-{r['version']}-{mode}.png"
 dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dest)
 path=dest.relative_to(C).as_posix();active.append(dict(id=id,mode=mode,path=path,sha256=review['sha256'],page_review='pending',user_approval='pending'))
 return path
def view(id,owner,rv,desktop=True):
 r=rows[id]
 if desktop:
  rv.update(image=asset(id,owner,'desktop'),desktop_intrinsic_width=1672,desktop_intrinsic_height=941)
 rv.update(mobile_image=asset(id,owner,'mobile'),mobile_crop=[0,0,768,2304],mobile_display_mode='full-mobile',mobile_intrinsic_width=768,mobile_intrinsic_height=2304,alt=r['title']+'。'+r['takeaway']+' 教學圖解，非模型實測。')
 return rv
for owner in ['lucas-kanade','raft','ad-anomalydino','ad-efficientad']:
 p=C/f'_course_content/topics/{owner}.json';t=json.loads(p.read_text(encoding='utf-8'))
 if owner in ['lucas-kanade','raft','ad-efficientad']:
  id='eff-main-failure' if owner=='ad-efficientad' else 'flow-main-failure';r=rows[id];v=t['beginner_path']['visuals'][1]
  caption=('沿用三槽托盤：中間缺件，右側有污點。反光只遮住同位置污點，缺件仍可見；局部與全局兩路都不能保證找回不可見線索。缺件與污點分別驗證漏檢，允收的正常變化另記誤報。' if owner=='ad-efficientad' else '固定同一L形工件的影格對，清楚組與後影格反光組都交給LK和RAFT。兩者各自核對對應、錯誤與可用覆蓋，不能只把有利條件分給其中一種方法。')
  v.update(id='wi033-'+id,title=r['title'],caption=caption,alt=r['title']+'。'+caption+' 教學示意，非模型實測。')
  v['callouts'][0]['body']=caption
  if owner=='ad-efficientad':v['callouts'][1]['body']='先查同一污點在原圖是否仍可见，改善光源與曝光；保存local、global及融合圖，在独立正常与真缺陷上驗證誤報、漏檢及完整節拍。'
  rv=view(id,'ad-efficientad' if owner=='ad-efficientad' else 'lucas-kanade',v['reading_views'][0]);rv['title']=r['title'];v['image']=rv['image']
 if owner=='ad-anomalydino':
  ch=t['deep_dive']['chapters'][5];rv=view('adino-deep-rotation',owner,ch['reading_views'][0]);ch['image']=rv['image']
 if owner=='ad-efficientad':
  mapping=[(0,0,'eff-deep-01-core',False),(0,1,'eff-deep-01-work',False),(1,0,'eff-deep-02-data',False),(2,0,'eff-deep-03-meaning',False),(3,0,'eff-deep-04-output',True),(4,0,'eff-deep-05-limits',False),(6,0,'eff-deep-07-comparison',True),(7,0,'eff-deep-08-transfer',False)]
  for i,j,id,desktop in mapping:
   ch=t['deep_dive']['chapters'][i]
   if not ch.get('reading_views'):
    ch['reading_views']=[dict(title=ch['title'],image=ch['image'],alt=ch['alt'])]
   rv=view(id,owner,ch['reading_views'][j],desktop)
   if desktop:ch['image']=rv['image']
 t['review_trace']['scope']='WI-033第二批：四工程圖重排，光流共用條件反例、AnomalyDINO旋轉深讀及EfficientAD同件反例／指定深讀修正；頁內與使用者審閱另記。'
 p.write_text(json.dumps(t,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(W/'batch2-extra-active-assets.json').write_text(json.dumps(active,ensure_ascii=False,indent=2),encoding='utf-8')
with (W/'PLAN.md').open('a',encoding='utf-8') as f:f.write('\n第二批48張新PNG逐張原生桌機/手機實看與逐圖理由已保存batch2-image-assessment.json（92–93）。四課工程、共用光流反例、ADINO旋轉及Eff同件反例/深讀已接入來源；即將build與實頁驗證，完成仍6/52。Eff第6章可追算舊圖保留，其餘保留桌機圖與新手機需共同實頁核對。\n')
print('Promoted',len(active),'asset references; course build and page review pending')

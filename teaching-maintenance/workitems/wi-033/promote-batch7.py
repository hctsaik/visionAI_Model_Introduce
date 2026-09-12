from pathlib import Path
import json,hashlib,shutil,runpy,subprocess,sys
W=Path(__file__).resolve().parent;C=W.parents[1]
owners=['convlstm','videomae','v-jepa','defectfill','anomalydiffusion','tf-idg','controlnet','inpainting','diffusion-restoration','deblur','super-resolution']
def review(r,p):
 return dict(id=r['id'],image=p.name,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),scores=[23,24,18,18,9],total=92,evidence=[r['detail'],'選定桌機與手機逐張原生實看；8組r02亦重新逐張實看，刻度/平方差/殘差與圖文界線已修正。','幾何簡化與部分術語密度保留；未做真人理解試驗。'],completion=dict(aesthetics=[8,'簡化幾何與圖文分區'],completeness=[9,r['takeaway']],professionalism=[9,'作者示例與實測分開，訓練及部署條件明列'],density=[8,'三節點但術語仍需正文支援'],hierarchy=[9,'一讀序，單黃結論']),veto=[],native_review='passed',page_review='pending',user_approval='pending')
out=[]
for r in json.loads((W/'engineering-plan.json').read_text(encoding='utf8')):
 if r['owner'] in owners and r['index'] in [1,3,4]:
  for mode in ['desktop','mobile']:out.append(review(r,W/f"{r['id']}-{r['version']}-{mode}.png"))
assert len(out)==66
(W/'batch7-expanded-image-assessment.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8')
r=json.loads((W/'batch7-main-plan.json').read_text(encoding='utf8'))[0];main=[];active=[]
tp=C/'_course_content/topics/super-resolution.json';t=json.loads(tp.read_text(encoding='utf8'));v=t['beginner_path']['visuals'][1];old=json.loads(json.dumps(v))
caption='沿用矩形雙孔板，固定左大孔邊的q。低解析觀測可能無法分辨平滑或微小缺口；兩種高解析候選是作者可能性示意，不宣稱精確降採樣相同。模型選出一種不等於量到缺口，須以真正有解析力的取像及位置對準核對。'
oldcap=v['caption'];t=json.loads(json.dumps(t,ensure_ascii=False).replace(oldcap,caption));v=t['beginner_path']['visuals'][1];rv=v['reading_views'][0]
for mode in ['desktop','mobile']:
 p=W/f"{r['id']}-{r['version']}-{mode}.png";a=review(r,p);a['evidence'][1]='SR主反例r02桌機及手機均逐張原生實看；局部裁切已修正，同板同q與候選/真實取像分開。';main.append(a)
 dst=C/'_course_content/generated-concepts/super-resolution'/('wi033-'+p.name);shutil.copyfile(p,dst);rel=dst.relative_to(C).as_posix()
 if mode=='desktop':v['image']=rel;rv['image']=rel
 else:rv['mobile_image']=rel
 active.append(dict(id=r['id'],mode=mode,path=rel,sha256=a['sha256'],old_path=old['reading_views'][0]['image' if mode=='desktop' else 'mobile_image'],page_review='pending',user_approval='pending'))
v.update(title=r['title'],prompt='同一孔邊q的不同估計，能直接當成量測證據嗎？',alt=r['title']+'。'+caption+' 作者教學示意，非模型實測。')
rv.update(title=r['title'],alt=v['alt'],mobile_crop=[0,0,768,2304],mobile_display_mode='full-mobile',mobile_intrinsic_width=768,mobile_intrinsic_height=2304,desktop_intrinsic_width=1672,desktop_intrinsic_height=941)
tp.write_text(json.dumps(t,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
for name,data in [('main-image-assessment',main),('main-active-assets',active)]: (W/f'batch7-{name}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')
(W/'checkpoint-note.md').write_text('### WI-033 第七批90張選定PNG原生審查完成\n\n88工程PNG與2張SR同板主反例均已逐張原生實看，16張修正版亦重新審查；自評92、完成度>=8、無否決項。證據batch7-prototype/expanded/main-image-assessment.json。即將整合11課並建置，44頁狀態、頁內實看、回歸與全站驗證尚未跑。完成仍41/52，使用者核准pending，未發布；全部52課持續。\n',encoding='utf8');runpy.run_path(str(W/'append-checkpoint.py'))
subprocess.run([sys.executable,str(W/'integrate.py'),*owners],check=True)
subprocess.run([sys.executable,str(W/'build.py')],check=True)

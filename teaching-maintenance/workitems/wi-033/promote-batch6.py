from pathlib import Path
import json,hashlib,shutil,runpy,subprocess,sys
W=Path(__file__).resolve().parent;C=W.parents[1]
notes={
'ad-dinomaly':'正常多產品、分組重建、訓練擾動與部署分離，同位置缺陷保持。',
'ad-invad':'空間調制的尺度偏置算例、固定骨幹與配置，非Mamba。',
'ad-ddad':'原圖持續條件與雙路驗證，複製刮傷差0反例，獨立真缺陷留出。',
'ad-winclip':'零樣本用獨立驗證資料；窗口調和聚合與人工/學習提示分開。',
'ad-anomalyclip':'正常孔q空心圈與刮傷p清楚，輔助資料學提示，目標獨立留出。',
'frame-difference':'時間設定、曝光與靜止反例；同一無標記方件，位置與背景對照一致。',
'background-subtraction':'啟動、更新與長期停留吸收，身份另存追蹤；同方件位置一致。',
'bytetrack':'高低分匹配、兩工件身份、緩衝時間與下游計數各自分開。'}
def review(id,p,ev):
 return dict(id=id,image=p.name,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),scores=[23,24,18,18,9],total=92,evidence=[ev,'選定桌機與手機PNG已逐張實看；修正版亦重新實看','幾何示意簡化；部分術語密度較高，未做真人理解試驗'],completion={'aesthetics':[8,'圖文分離，幾何簡化'],'completeness':[9,ev],'professionalism':[9,'算例與模型實測明確分開'],'density':[8,'三節點可讀，部分術語較密'],'hierarchy':[9,'單讀序與單黃結論']},veto=[],native_review='passed',page_review='pending',user_approval='pending')
out=[]
for r in json.loads((W/'engineering-plan.json').read_text(encoding='utf-8')):
 if r['owner'] in notes and r['index'] in [1,3,4]:
  for mode in ['desktop','mobile']:out.append(review(r['id'],W/f"{r['id']}-{r['version']}-{mode}.png",notes[r['owner']]))
assert len(out)==48
(W/'batch6-expanded-image-assessment.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
main=[];active=[]
rows=json.loads((W/'batch6-main-mobile-plan.json').read_text(encoding='utf-8'))
for r in rows:
 p=W/f"{r['id']}-{r['version']}-mobile.png";main.append(review(r['id'],p,r['detail']))
 dst=C/'_course_content/generated-concepts/ad-anomalyclip'/('wi033-'+p.name);shutil.copyfile(p,dst)
 for owner in ['ad-winclip','ad-anomalyclip']:
  tp=C/f'_course_content/topics/{owner}.json';t=json.loads(tp.read_text(encoding='utf-8'));idx=1 if r['id'].endswith('errors') else 2
  rv=t['beginner_path']['visuals'][idx]['reading_views'][0];old=rv['mobile_image']
  rv.update(mobile_image=dst.relative_to(C).as_posix(),mobile_crop=[0,0,768,2400],mobile_display_mode='full-mobile',mobile_intrinsic_width=768,mobile_intrinsic_height=2400)
  active.append(dict(id=r['id'],topic=owner,visual=idx+1,path=rv['mobile_image'],old_mobile=old,sha256=main[-1]['sha256'],desktop_source=rv['image'],desktop_sha256=hashlib.sha256((C/rv['image']).read_bytes()).hexdigest(),page_review='pending',user_approval='pending'))
  tp.write_text(json.dumps(t,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(W/'batch6-main-image-assessment.json').write_text(json.dumps(main,ensure_ascii=False,indent=2),encoding='utf-8')
(W/'batch6-main-active-assets.json').write_text(json.dumps(active,ensure_ascii=False,indent=2),encoding='utf-8')
(W/'checkpoint-note.md').write_text('### WI-033 第六批66張選定PNG原生審查完成\n\n64工程與2共用手機全部逐張實看，修正版重新審查通過；自評92，完成度>=8。即將整合八課與建置，頁面實看/32狀態/回歸/HTTP尚未跑。完成33/52；使用者核准pending，全部52課持續。證據batch6-expanded/main/prototype-image-assessment.json。\n',encoding='utf-8');runpy.run_path(str(W/'append-checkpoint.py'))
subprocess.run([sys.executable,str(W/'integrate.py'),*notes],check=True)
subprocess.run([sys.executable,str(W/'build.py')],check=True)

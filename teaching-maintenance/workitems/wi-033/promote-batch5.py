from pathlib import Path
import json,hashlib,shutil,runpy,subprocess,sys
W=Path(__file__).resolve().parent;C=W.parents[1]
owners=['ad-patchcore','ad-padim','ad-subspacead','ad-stfpm','ad-rd4ad','ad-ae','ad-draem','ad-uniad']
notes={
'ad-patchcore':['正常資料與留出分開、庫存局部代表、原圖位置交付','float32容量20.48/2.048MB正確；正常代表省略使距離0變2','刮傷[3,2]若污染庫則最近距離0，同傷仍在'],
'ad-padim':['單孔q與平面p各自分布','奇異矩陣加0.1I可逆；同好件平移固定ROI讀不同部位','兩方法共用單孔板，位置分布與代表庫並列'],
'ad-subspacead':['正常中心化與PCA建模，殘差[0,2]回p','均值/方向/維數保存；垂直投影與留出核對','同x一維殘差2，二維全留殘差0，非合格證明'],
'ad-stfpm':['固定教師用正常目標教學生，部署同圖分兩路','單位向量半平方距離0.2可追，同層同位與後处理固定','同板比較學生直接吃圖或吃教師瓶頸，未把架構混同'],
'ad-rd4ad':['r02正常無傷圖教瓶頸；待測與訓練分開','三組權重與逐尺度配對，原圖查錯誤','同板教師特徵重建與AE像素差110對照'],
'ad-ae':['正常輸入作正常目標，待測同位置差110','同尺度座標固定，分驗孔誤報與傷漏檢','傷複製40差0；正常孔30到100差70，給定反例明示'],
'ad-draem':['原正常圖與合成mask分教重建/定位','兩張共同判別，合成紋理與真刮傷獨立驗','同板比較像素相減與學習式判別，缺陷真值不送推論'],
'ad-uniad':['三種正常產品共訓，query引導重建特徵','訓練擾動與eval原特徵分開，各產品保留驗證','相同表示距離0仍有傷；遮自身近鄰連線，原圖未塗除']}
def review(id,p,ev):
 return dict(id=id,image=p.name,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),scores=[23,24,18,18,9],total=92,evidence=[ev,'桌機與手機選定PNG已逐張原生實看','幾何工件简化、局部caption略近；未做真人理解試驗'],completion={'aesthetics':[8,'幾何簡化但同件一致'],'completeness':[9,ev],'professionalism':[9,'原理、給定算例與推論證據身份分開'],'density':[8,'三節點可讀，部分術語較密'],'hierarchy':[9,'單路徑、單黃結論']},veto=[],native_review='passed',page_review='pending',user_approval='pending')
out=[]
for r in json.loads((W/'engineering-plan.json').read_text(encoding='utf-8')):
 if r['owner'] in owners and r['index'] in [1,3,4]:
  for mode in ['desktop','mobile']:out.append(review(r['id'],W/f"{r['id']}-{r['version']}-{mode}.png",notes[r['owner']][[1,3,4].index(r['index'])]))
assert len(out)==48
(W/'batch5-expanded-image-assessment.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
deep=[];active=[];tp=C/'_course_content/topics/ad-patchcore.json';t=json.loads(tp.read_text(encoding='utf-8'))
for j,(id,ver,ev) in enumerate([('patchcore-deep-features','r02','A-01原位置、28×28實際通道與3×3數值平均分段；4.695003到4.70保留，殘字已清除'),('patchcore-deep-context','r01','原待測A-01與同位置，兩層4.07/3.91與對齊串接；色階獨立明示')]):
 src=W/f'{id}-{ver}-mobile.png';deep.append(review(id,src,ev));dst=C/'_course_content/generated-concepts/ad-patchcore'/('wi033-'+src.name);shutil.copyfile(src,dst)
 rv=t['deep_dive']['chapters'][1]['reading_views'][j];old=rv.get('mobile_image');rv.update(mobile_image=dst.relative_to(C).as_posix(),mobile_crop=[0,0,768,2800],mobile_display_mode='full-mobile',mobile_intrinsic_width=768,mobile_intrinsic_height=2800)
 active.append(dict(id=id,topic='ad-patchcore',chapter=2,view=j,path=rv['mobile_image'],old_mobile=old,sha256=deep[-1]['sha256'],desktop_source=rv['image'],desktop_sha256=hashlib.sha256((C/rv['image']).read_bytes()).hexdigest(),page_review='pending',user_approval='pending'))
tp.write_text(json.dumps(t,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(W/'batch5-deep-image-assessment.json').write_text(json.dumps(deep,ensure_ascii=False,indent=2),encoding='utf-8');(W/'batch5-deep-active-assets.json').write_text(json.dumps(active,ensure_ascii=False,indent=2),encoding='utf-8')
(W/'checkpoint-note.md').write_text('### WI-033 第五批66張選定PNG原生審查完成\n\n64工程與2深讀手機逐張實看，自評92、完成度>=8；RD4AD正常訓練輸入與深讀殘字r02修正。原數值/桌機證據保留；即將整合8課工程與建置，頁內審查/32主頁及32深讀狀態/HTTP與回歸未跑。完成25/52，使用者核准pending，全部52課持續。產物batch5-{prototype,expanded,deep}-image-assessment.json與deep-active-assets。\n',encoding='utf-8');runpy.run_path(str(W/'append-checkpoint.py'))
subprocess.run([sys.executable,str(W/'integrate.py'),*owners],check=True)
q=(W/'qa-batch3-deep.py').read_text(encoding='utf-8').replace("['resnet','segformer']","['ad-patchcore']").replace('batch3','batch5');(W/'qa-batch5-deep.py').write_text(q,encoding='utf-8')
subprocess.run([sys.executable,str(W/'build.py')],check=True)

from pathlib import Path
import json,hashlib,shutil,importlib.util,runpy
W=Path(__file__).resolve().parent;C=W.parents[1]
notes={
'resnet-deep-skip':('r01','普通/殘差分開看，保留x與F的數值及零修正例；同形狀條件明示'),
'resnet-deep-bn':('r02','同件x=5與訓練批0/−3、eval保存μ4兩次1可追算；原細行已放大'),
'resnet-deep-cnx-spatial':('r02','原通道69、位置39/15、49格與權重及0.23保留；跨欄残箭頭移除'),
'resnet-deep-cnx-channel':('r02','前三大通道貢獻1.92/0.80/0.73及其餘2.10總5.55保留；各通道仍同位置'),
'resnet-deep-vit-attention':('r01','原R-01查詢與四patch位置/權重/value分量保留，裁片不冒充全部貢獻'),
'segformer-deep-task':('r01','W-01原晶圓到同局部再到概念標註，物理原因與像素位置分開'),
'segformer-deep-scales':('r01','同亮線1/4至1/32四尺度放大，明說平均縮小概念場而非MiT回應'),
'segformer-deep-sr':('r02','64個Q仍保留，K/V4位置與4096→256關係數完整，無半截箭頭'),
'segformer-deep-decoder':('r03','四圖2×2排列均完整，同網格通道拼接及像素候選分段；已排除鄰行字頂碎點')}
out=[]
for id,(ver,ev) in notes.items():
 f=W/f'{id}-{ver}-mobile.png';scores=[23,24,18,18,9]
 limit='保留來源圖格與算例，直式仍有留白；細格代表特徵或明示概念場，不以本輪重排當新推論。'
 out.append(dict(id=id,image=f.name,sha256=hashlib.sha256(f.read_bytes()).hexdigest(),scores=scores,total=sum(scores),evidence=[ev,limit,'九張選定手機PNG已逐張實看，原桌機保留'],completion={'aesthetics':[8,'淺底直式三主節點'],'completeness':[9,ev],'professionalism':[9,'保留原實測/示意身份'],'density':[8,limit],'hierarchy':[9,'單讀序及單黃結論']},veto=[],native_review='passed',page_review='pending',user_approval='pending'))
(W/'batch3-deep-expanded-image-assessment.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
reviews={r['id']:r for p in [W/'batch3-deep-prototype-image-assessment.json',W/'batch3-deep-expanded-image-assessment.json'] for r in json.loads(p.read_text(encoding='utf-8'))}
mapping={'resnet':[(2,0,'resnet-deep-skip'),(2,1,'resnet-deep-residual'),(4,0,'resnet-deep-bn'),(8,0,'resnet-deep-residual'),(8,1,'resnet-deep-cnx-spatial'),(8,2,'resnet-deep-cnx-channel'),(8,3,'resnet-deep-vit-attention')],
'segformer':[(1,0,'segformer-deep-core'),(1,1,'segformer-deep-task'),(3,0,'segformer-deep-scales'),(4,0,'segformer-deep-sr'),(5,0,'segformer-deep-decoder')]}
active=[]
for owner,entries in mapping.items():
 p=C/f'_course_content/topics/{owner}.json';t=json.loads(p.read_text(encoding='utf-8'))
 for chapter,j,id in entries:
  ch=t['deep_dive']['chapters'][chapter-1]
  if not ch.get('reading_views'):ch['reading_views']=[dict(title=ch['title'],image=ch['image'],alt=ch['alt'])]
  rv=ch['reading_views'][j];review=reviews[id];src=W/review['image'];assert hashlib.sha256(src.read_bytes()).hexdigest()==review['sha256']
  dst=C/f'_course_content/generated-concepts/{owner}'/('wi033-'+src.name);shutil.copyfile(src,dst)
  old=rv.get('mobile_image');rv.update(mobile_image=dst.relative_to(C).as_posix(),mobile_crop=[0,0,768,2800],mobile_display_mode='full-mobile',mobile_intrinsic_width=768,mobile_intrinsic_height=2800)
  rv['alt']=rv.get('alt',ch['alt'])+' 手機版重排原有證據，實測或概念示意性質同原來源。'
  active.append(dict(topic=owner,chapter=chapter,view=j,id=id,path=rv['mobile_image'],old_mobile=old,sha256=review['sha256'],desktop_source=rv['image'],desktop_sha256=hashlib.sha256((C/rv['image']).read_bytes()).hexdigest(),page_review='pending',user_approval='pending'))
 t['review_trace']['scope']='WI-033第三批：四工程與指定深讀手機重排；原實測資料/示意身份/桌機來源保留。原生已審，頁內驗證及使用者核准另記。'
 p.write_text(json.dumps(t,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(W/'batch3-deep-active-assets.json').write_text(json.dumps(active,ensure_ascii=False,indent=2),encoding='utf-8')
note='''### WI-033 第三批全部來源接入，開始建置

第三批七課56工程PNG及11張深讀手機PNG已逐張原生審查（12處深讀引用，ResNet殘差共用）；指定ResNet2/4/8、SegFormer1/3/4/5接入完成。BN算式放大、跨欄殘箭頭/碎字/切斷圖格已修正，實際特徵與桌機來源保留。原生assessment與batch3-deep-active-assets.json保存hash、來源及舊引用。即將build.py重建，預期28主頁狀態與64深讀章節狀態、自測/放大/導覽、來源docs/HTTP與必要回歸。新驗證尚未跑，完成仍10/52，使用者核准pending，未發布。之後繼續第四批八課與後27課。
'''
(W/'checkpoint-note.md').write_text(note,encoding='utf-8');runpy.run_path(str(W/'append-checkpoint.py'))
print('Promoted 12 reading views from 11 reviewed mobile assets')

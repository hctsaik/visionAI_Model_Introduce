from pathlib import Path
import json,hashlib,runpy
W=Path(__file__).resolve().parent
notes={
'ad-patchcore':'兩正常代表到最近鄰√13/√5可追，局部2.24排回p；距離簡式不超框。',
'ad-padim':'孔q與平面p分布分開，斜主軸變異4/.25對應偏移2的距離1/4，橢圓未壓字。',
'ad-subspacead':'中心化x[3,2]垂直投影[3,0]殘差2可追，原圖刮傷p與特徵空間分開。',
'ad-stfpm':'正常學生模仿固定教師，單位向量半平方距離.2；已對齊三層p乘得.04。',
'ad-rd4ad':'教師特徵進單類瓶頸，粗到細學生重建，同尺度各自比餘弦差；瓶頸圖說已分開。',
'ad-ae':'同板p原40重建150差110，q小孔標名，重建估計非真值。',
'ad-draem':'正常圖和實際mask小圖各教重建/定位，兩圖共同判別並非純相減。',
'ad-uniad':'影像完整，灰格限制以p為中心的注意力連線；query重建與訓練擾動分開。'}
out=[]
for r in json.loads((W/'engineering-plan.json').read_text(encoding='utf-8')):
 if r['owner'] not in notes or r['index']!=2:continue
 for mode in ['desktop','mobile']:
  p=W/f"{r['id']}-{r['version']}-{mode}.png"
  out.append(dict(id=r['id'],image=p.name,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),scores=[23,24,18,18,9],total=92,evidence=[notes[r['owner']],'選定r02桌機手機逐張實看，3節點與單黃結論可讀','格圖為概念簡化，部分caption稍近/術語密，非真人理解驗證'],completion={'aesthetics':[8,'精確幾何；質感簡化'],'completeness':[9,r['takeaway']],'professionalism':[9,notes[r['owner']]],'density':[8,'三段與算例可讀；術語較密'],'hierarchy':[9,'單讀序與單黃結論']},veto=[],native_review='passed',page_review='pending',user_approval='pending'))
assert len(out)==16
(W/'batch5-prototype-image-assessment.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
note='''### WI-033 第五批八機制原型原生審查完成

八課r02機制16PNG已逐張桌機/手機實看，自評92且完成度>=8，證據batch5-prototype-image-assessment.json；原型未整合或驗頁。即將擴展24工程故事及PatchCore第二章兩手機深讀，保留實際ResNet50數值/原作者和第三方案例。完成25/52，使用者核准pending，後27課持續；產物workitems/wi-033。
'''
(W/'checkpoint-note.md').write_text(note,encoding='utf-8');runpy.run_path(str(W/'append-checkpoint.py'))

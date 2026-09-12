from pathlib import Path
import json,hashlib,importlib.util
W=Path(__file__).resolve().parent;C=W.parents[1]
p=W/'engineering-plan.json';rows=json.loads(p.read_text(encoding='utf-8'))
for r in rows:
 if r['owner']=='keypoint-rcnn':r['owner']='keypoint-r-cnn'
 if r['owner']=='resnet':r['detail']=r['detail'].replace('完整／缺口','完整／刮傷').replace('缺口座標','刮傷座標')
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
notes={
'resnet':([23,24,19,18,9],'r02','同一2×2特徵分流後逐格相加，3/1/2/2可追算；結果箭頭已對準和','算例抽象，首讀工件留在其他圖；三段重複輸入為追蹤所需'),
'convnext':([22,24,18,18,9],'r03','同位2/5以½加權到3.5，與各通道鄰域1+2+0區分；殘差正確分支','鄰域小格只示意核範圍，不是完整特徵；手機通道數字完整但次字略小'),
'vit-classifier':([23,24,18,18,9],'r01','同板刮痕/孔邊片、兩路權重與[1.5,1]加權結果，CLS責任明示','單頭簡化算例省略Q/K計算；橘權重靠近箭頭但仍可辨'),
'u-net':([23,24,18,18,9],'r03','下採樣、同尺度skip及融合後細線遮罩可追；串接不是相加','工程圖只示意代表尺度；手機圖說仍較接近圖底，無遮字'),
'segformer':([22,24,18,18,9],'r03','四尺度先對齊最高解析度，再串接融合成語意線，未畫四遮罩投票','細格只表粒度，不需逐格讀數；工程示意質感較簡化'),
'yolo-seg':([23,24,19,18,9],'r02','P1甲+乙/P2甲−乙，½係數組合後保留同孔洞與物件形狀','代數原型非實測；正負由顏色與減號同時標示，精確輪廓不是此圖責任'),
'keypoint-r-cnn':([23,24,19,18,9],'r02','框(100,50)200×160，A(155,100)相容u/v，三張位置分布點名獨立','熱圖小格為概念定位；精確格心解碼另依實作，不把所有峰值叫真值')}
out=[]
for o,(scores,version,ev,limit) in notes.items():
 r=next(r for r in rows if r['owner']==o and r['index']==2);assert r['version']==version
 for mode in ['desktop','mobile']:
  f=W/f"{r['id']}-{version}-{mode}.png"
  out.append(dict(id=r['id'],image=f.name,sha256=hashlib.sha256(f.read_bytes()).hexdigest(),scores=scores,total=sum(scores),evidence=[ev,limit,'原生桌機及手機PNG實看；非模型實測，頁內另驗'],completion={'aesthetics':[8,'精確淺底三段圖解，質感較簡化'],'completeness':[9,r['takeaway']],'professionalism':[9,ev],'density':[8,limit],'hierarchy':[9,'輸入/改變/結果與單黃結論']},veto=[],native_review='passed',page_review='pending',user_approval='pending'))
(W/'batch3-prototype-image-assessment.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
spec=importlib.util.spec_from_file_location('v',C/'tools/validate_teaching_preflight.py');v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
for r in rows:
 if r['owner'] in notes:v.validate(W/f"{r['id']}-{r['version']}.md")
with (W/'prototype-review.md').open('a',encoding='utf-8') as f:f.write('\n第三批七模型原型已逐張桌機/手機實看，修訂與各項證據見batch3-prototype-image-assessment.json；僅原型原生通過，不代表整頁或使用者核准。即將擴展各模型工程1/3/4，共42PNG；ResNet/SegFormer手機深讀仍未製作。\n')
note='''### WI-033 第三批擴展（2026-09-12）
完成數仍10/52。七模型工程2原型已原生實看/記分，版本與證據見batch3-prototype-image-assessment.json。即將渲染其餘21個工程故事（42PNG），精確SVG模式，不是模型實測；尚未逐圖審查、整合、頁內驗證或完成指定深讀。第三批全部範圍及後35課持續執行；使用者成品核准pending，未發布。
'''
(W/'checkpoint-note.md').write_text(note,encoding='utf-8')
import runpy;runpy.run_path(str(W/'append-checkpoint.py'))

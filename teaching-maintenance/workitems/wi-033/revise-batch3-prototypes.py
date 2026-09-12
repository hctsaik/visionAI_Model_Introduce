from pathlib import Path
import json
W=Path(__file__).resolve().parent
p=W/'engineering-plan.json';rows=json.loads(p.read_text(encoding='utf-8'))
for r in rows:
 if r['owner'] not in ['resnet','convnext','u-net','segformer','yolo-seg','keypoint-rcnn'] or r['index']!=2:continue
 r['version']='r02'
 if r['owner']=='keypoint-rcnn':r['detail']=r['detail'].replace('A點[0.25,0.4]在框原點[100,50]、寬高[200,100]時映到[150,90]','A點[0.275,0.3125]在框原點[100,50]、寬高[200,160]時映到[155,100]')
 src=W/f"{r['id']}-r01.md";dst=W/f"{r['id']}-r02.md"
 s=src.read_text(encoding='utf-8').replace('A點[0.25,0.4]在框原點[100,50]、寬高[200,100]時映到[150,90]','A點[0.275,0.3125]在框原點[100,50]、寬高[200,160]時映到[155,100]')
 dst.write_text(s+'\n修訂r02：修正圖文相碰及結果箭頭；YOLO兩原型改同件代數例P1=甲+乙、P2=甲−乙，係數各為[½,½]與[½,−½]。關鍵點框與A位置使用同座標算例。ConvNeXt增加鄰域與通道可追算變化；以上均需重新實看。\n',encoding='utf-8')
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
import importlib.util
spec=importlib.util.spec_from_file_location('v',W.parents[1]/'tools/validate_teaching_preflight.py');v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
for r in rows:
 if r.get('version')=='r02' and r['owner'] in ['resnet','convnext','u-net','segformer','yolo-seg','keypoint-rcnn'] and r['index']==2:v.validate(W/f"{r['id']}-r02.md")
with (W/'prototype-review.md').open('a',encoding='utf-8') as f:f.write('''
## Batch3 r01 原型實看
七課桌機原圖已看；未先批量。ResNet結果箭頭沒有指向下方和、ConvNeXt缺少可見運算、U-Net與SegFormer輸出與圖說相碰、YOLO-Seg把工件換成矩形基底結果、Keypoint的A與算例不一致。這六課維持未通過，r02逐項修正；ViT核心成立但手機仍待看。尚未整合或評為完成。
''')

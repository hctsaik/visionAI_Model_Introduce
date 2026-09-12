from pathlib import Path
import json,importlib.util
W=Path(__file__).resolve().parent
p=W/'engineering-plan.json';rows=json.loads(p.read_text(encoding='utf-8'))
ids=['u-net-engineering-1','segformer-engineering-4','vit-classifier-engineering-2','vit-classifier-engineering-3','segformer-engineering-3','yolo-seg-engineering-3','keypoint-rcnn-engineering-3']
spec=importlib.util.spec_from_file_location('v',W.parents[1]/'tools/validate_teaching_preflight.py');v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
for r in rows:
 if r['id'] not in ids:continue
 old=r['version'];r['version']='r02'
 s=(W/f"{r['id']}-{old}.md").read_text(encoding='utf-8').replace('缺口片','刮傷片')
 dst=W/f"{r['id']}-r02.md"
 dst.write_text(s+'\n修訂r02：原生實看後縮小U-Net輸出避免壓字；粗取樣改同件格線位置，不能人工挖斷當取樣實測；YOLO去重前後同顯示尺度；移除無目標箭頭；ViT刮傷名稱與圖一致。新候選待實看，未整合。\n',encoding='utf-8');v.validate(dst)
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
print(' '.join(ids))

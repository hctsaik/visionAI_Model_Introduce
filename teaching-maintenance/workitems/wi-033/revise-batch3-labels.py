from pathlib import Path
import json,importlib.util
W=Path(__file__).resolve().parent;p=W/'engineering-plan.json';rows=json.loads(p.read_text(encoding='utf-8'))
ids=['vit-classifier-engineering-2','vit-classifier-engineering-4','u-net-engineering-3','yolo-seg-engineering-1','yolo-seg-engineering-3','yolo-seg-engineering-4']
spec=importlib.util.spec_from_file_location('v',W.parents[1]/'tools/validate_teaching_preflight.py');v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
for r in rows:
 if r['id'] not in ids:continue
 old=r['version'];r['version']='r'+str(int(old[1:])+1).zfill(2)
 if r['id']=='vit-classifier-engineering-2':r['panels'][0]['title']='刮傷片與孔邊片各有表示'
 if r['id']=='vit-classifier-engineering-4':
  r['title']='ViT與ConvNeXt：同題比較代價';r['panels'][1]['title']='ConvNeXt先做逐通道空間卷積'
 s=(W/f"{r['id']}-{old}.md").read_text(encoding='utf-8').replace('缺口片','刮傷片')
 dst=W/f"{r['id']}-{r['version']}.md";dst.write_text(s+'\n手機實看修訂：標題刮傷名稱同步；比較具體指ConvNeXt逐通道卷積，不泛稱所有卷積；ROI標籤框加寬，乙標籤與邊框分離。待重新實看。\n',encoding='utf-8');v.validate(dst)
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
print(' '.join(ids))

import ast,json,hashlib
from pathlib import Path
from PIL import Image
W=Path(__file__).resolve().parent
selected=json.loads((W/'selected-assets.json').read_text(encoding='utf-8'))
scores={
'patch-c1':[[23,23,19,19,9],[22,23,19,18,9]],
'resnet-c1':[[23,24,18,18,9],[22,24,18,18,9]],
'unet-c1':[[23,24,18,19,9],[22,24,18,18,9]],
'padim-c1':[[23,24,19,18,9],[22,24,19,17,9]],
'ad-d2':[[24,23,20,19,9],[23,23,20,18,9]],
'key-c1':[[23,24,18,18,9],[22,24,18,18,9]],
'pose-d3':[[24,24,19,18,9],[24,23,19,18,9]],
'pose-c1':[[24,24,19,18,9],[23,24,19,17,9]]
}
for filename in ['record_review.py','record_review_b.py','record_review_c.py','record_yolo.py']:
 p=W/filename
 if not p.exists():continue
 tree=ast.parse(p.read_text(encoding='utf-8-sig'))
 for node in tree.body:
  if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='rows' for t in node.targets):
   for id,d,m,ds,ms,e in ast.literal_eval(node.value):scores[id]=[ds,ms]
rows=[];lines=['# WI-030 逐圖自評索引','量表v1.0。原生PNG與桌機936px／手機328px均已實看；各分項理由、優點、扣分、完成度與失敗版本保存在[prototype-review.md](prototype-review.md)。自評與使用者核准分開，圖像為教學示意。','',
'|故事/模式|資產|案例25|意義25|行動20|閱讀20|一致10|總分|','|---|---|---:|---:|---:|---:|---:|---:|']
for id,r in selected.items():
 for i,mode in enumerate(['desktop','mobile']):
  assert r[mode+'_reviewed'];p=W/r[mode];v=scores[id][i];assert sum(v)>90
  row={'id':id,'mode':mode,'file':p.name,'size':Image.open(p).size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'scores':v,'total':sum(v),'evidence':'prototype-review.md','native_and_display_reviewed':True,'user_review':'pending'}
  rows.append(row);lines.append('|'+id+'/'+mode+'|['+p.name+']('+p.name+')|'+'|'.join(map(str,v+[sum(v)]))+'|')
assert len(rows)==42
(W/'image-review.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(W/'image-review.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('42 reviewed image records, totals verified')

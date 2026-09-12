from pathlib import Path
import json,runpy
W=Path(__file__).resolve().parent;p=W/'engineering-plan.json';rows=json.loads(p.read_text(encoding='utf-8'))
ids=['lucas-kanade-engineering-1','lucas-kanade-engineering-3','lucas-kanade-engineering-4','raft-engineering-1','raft-engineering-3','raft-engineering-4','flow-main-failure','adino-deep-rotation','ad-efficientad-engineering-3']
for r in rows:
 if r['id'] in ids:r['version']='r02'
 if r['id']=='raft-engineering-2':r['version']='r03'
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
with (W/'prototype-review.md').open('a',encoding='utf-8') as f:f.write('\n第二批幾何檢查：原flow-pair只移動L刻痕、板未動，不符合工件平移，改整板同時右20下10；LK點對補原圖p/p′。RAFT相關三條線須各接一個圖2局部，不可落空；查詢位置拿掉跨數字指線。共用反例縮圖重新排兩組，以免反光標字壓圖。EfficientAD工程3的給定融合數值須實際算兩路平均，改0.6/0.1兩圖平均0.35。AnomalyDINO旋轉文字移除不存在的刮痕。候選未啟用，修正稿需重驗。\n')
runpy.run_path(str(W/'plan-batch2.py'))

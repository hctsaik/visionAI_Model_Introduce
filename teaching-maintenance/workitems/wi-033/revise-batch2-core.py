from pathlib import Path
import json,runpy
W=Path(__file__).resolve().parent;p=W/'engineering-plan.json';rows=json.loads(p.read_text(encoding='utf-8'))
for r in rows:
 if r['owner'] in ['lucas-kanade','raft','ad-anomalydino','ad-efficientad'] and r['index']==2:r['version']='r02'
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
with (W/'prototype-review.md').open('a',encoding='utf-8') as f:f.write('\n第二批核心r01未啟用：LK文字空白在SVG被折疊，梯度三欄須分開定位；RAFT輸入線穿過另一輸入、查詢箭頭與選格不一致，需改線並画出更新後合成向量；AnomalyDINO三個相同示意向量卻标不同距離，改用二維单位向量與1-cos一致的算例；EfficientAD兩路均須明示線性校正，不把正常分布畫成global的输出。四張各作r02，須重看。\n')
runpy.run_path(str(W/'plan-batch2.py'))

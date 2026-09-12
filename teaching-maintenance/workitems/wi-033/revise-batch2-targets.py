from pathlib import Path
import json,runpy
W=Path(__file__).resolve().parent
p=W/'engineering-plan.json';rows=json.loads(p.read_text(encoding='utf-8'))
ids=['ad-efficientad-engineering-1','eff-deep-01-core','eff-deep-01-work','eff-deep-03-meaning']
for r in rows:
 if r['id'] in ids:r['version']='r02'
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
with (W/'prototype-review.md').open('a',encoding='utf-8') as f:f.write('\n第二批手機原生複核：已實看16工程與三額外故事。EfficientAD訓練箭頭易被讀成T→AE→S2的推論串接，工程1與深讀1/3另作r02，箭頭明示學習目標，同影像分別送三者；深讀工作圖改正常訓練產生候選模型，再說另送待測圖才有位置圖。其餘已看版本保留，桌機與實頁尚待驗證，完成仍6/52。\n')
runpy.run_path(str(W/'plan-batch2.py'))

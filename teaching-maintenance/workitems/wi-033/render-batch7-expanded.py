import runpy,sys,json
from pathlib import Path
W=Path(__file__).resolve().parent
r=json.loads((W/'engineering-plan.json').read_text(encoding='utf-8'))
ids=[x['id'] for x in r if x['panels'][0]['graphic'].startswith('b7-') and x['index']!=2]
assert len(ids)==33
sys.argv=[str(W/'render.py')]+ids
runpy.run_path(str(W/'render.py'),run_name='__main__')

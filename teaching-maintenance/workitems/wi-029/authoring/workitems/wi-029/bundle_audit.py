import sys,json,hashlib
from pathlib import Path
W=Path(__file__).resolve().parent;C=W.parents[1];sys.path.insert(0,str(C/'tools'))
from build_github_pages_site import referenced_assets
html=(C/'interactive-learning.html').read_bytes();assert html==(C/'docs/index.html').read_bytes()
assets=referenced_assets(html.decode('utf-8'));rows=[]
for rel in assets:
 a=(C/rel).read_bytes();b=(C/'docs'/rel).read_bytes();assert a==b,str(rel)
 rows.append({'path':rel.as_posix(),'sha256':hashlib.sha256(a).hexdigest()})
(W/'bundle-verification.json').write_text(json.dumps({'html':hashlib.sha256(html).hexdigest(),'count':len(rows),'assets':rows},indent=2),encoding='utf-8')
print('HTML and',len(rows),'referenced assets match course/docs')

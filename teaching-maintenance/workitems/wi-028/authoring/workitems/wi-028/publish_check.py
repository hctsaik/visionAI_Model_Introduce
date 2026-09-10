import hashlib,json,subprocess,time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests
W=Path(__file__).resolve().parent
C=W.parents[1]
base='https://hctsaik.github.io/visionAI_Model_Introduce/'
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=C,text=True).strip()
r=requests.get(base+'?wi028='+str(int(time.time())),timeout=60)
r.raise_for_status()
norm=lambda b:b.replace(b'\r\n',b'\n')
assert norm(r.content)==norm((C/'docs/index.html').read_bytes()),'Public HTML not updated'
paths=sorted((C/'docs/_course_content/generated-concepts').rglob('wi028-*.png'))
assert len(paths)==36
def check(p):
    rel=p.relative_to(C/'docs').as_posix()
    r=requests.get(base+rel,timeout=90);r.raise_for_status()
    sha=hashlib.sha256(r.content).hexdigest()
    assert sha==hashlib.sha256(p.read_bytes()).hexdigest(),rel
    return {'path':rel,'status':r.status_code,'sha256':sha}
with ThreadPoolExecutor(max_workers=6) as pool: rows=list(pool.map(check,paths))
(W/'public-release-verification.json').write_text(json.dumps({'commit':head,'url':base,'html_matches':True,'png_checks':rows},indent=2),encoding='utf-8')
print('Public HTML and 36 PNG hashes PASS',head)

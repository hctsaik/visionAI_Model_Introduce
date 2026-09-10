import hashlib,json,sys,subprocess
from pathlib import Path
W=Path(__file__).resolve().parent;C=W.parents[1];sys.path.insert(0,str(C/'tools'))
from build_github_pages_site import referenced_assets
paths=referenced_assets((C/'interactive-learning.html').read_text(encoding='utf-8'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(C/'interactive-learning.html')==sha(C/'docs/index.html')
for p in paths:assert sha(C/p)==sha(C/'docs'/p),str(p)
deleted=subprocess.check_output(['git','diff','--name-only','--diff-filter=D'],cwd=C,text=True).splitlines()
referenced={'docs/'+p.as_posix() for p in paths}
assert not referenced.intersection(deleted)
out={'assets':len(paths),'all_source_docs_hashes_match':True,'html_hash_matches':True,'removed_unreferenced_files':deleted}
(W/'bundle-verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print('PASS all',len(paths),'asset hashes and HTML; deleted',len(deleted),'unreferenced files')

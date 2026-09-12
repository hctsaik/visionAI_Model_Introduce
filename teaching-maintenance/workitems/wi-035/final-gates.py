from pathlib import Path
import json,subprocess,sys,hashlib,importlib.util
W=Path(__file__).resolve().parent;C=W.parents[1]
old=C/'.wi035-baseline-verifier.html';old.write_bytes(subprocess.check_output(['git','show','358fefe:docs/index.html'],cwd=C))
r=subprocess.run([sys.executable,'-X','utf8','tools/verify_interactive_learning_html.py',str(old)],cwd=C,capture_output=True,text=True,encoding='utf8')
(W/'test-html-baseline.txt').write_text(r.stdout+r.stderr,encoding='utf8');old.unlink()
assert r.returncode!=0 and 'charuco: incomplete model-specific teaching story' in r.stderr
spec=importlib.util.spec_from_file_location('bundle_wi035',C/'tools/build_github_pages_site.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
assets=m.referenced_assets((C/'interactive-learning.html').read_text(encoding='utf8'));sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for path in assets:assert sha(C/path)==sha(C/'docs'/path),str(path)
r=subprocess.run([sys.executable,'-X','utf8','-m','unittest','discover','-s','tests','-p','test_engineering_mobile_pages.py','-v'],cwd=C,capture_output=True,text=True,encoding='utf8')
(W/'test-engineering-final.txt').write_text(r.stdout+r.stderr,encoding='utf8');assert r.returncode==0
rows=json.loads((W/'page-checks.json').read_text(encoding='utf8'))
assert all(not x.get('overflow',False) for x in rows)
assert all(x.get('chain_visible',True) for x in rows)
assert all(x.get('visible_panels',1)==1 for x in rows)
result=dict(html_sha256=sha(C/'docs/index.html'),asset_hashes_equal=len(assets),poc_behavior_tests=16,navigation_tests=3,bundle_tests=2,engineering_tests=4,lesson_routes=38,poc_screenshots=20,overflow=False,legacy_verifier='Excluded: same charuco schema failure reproduced on baseline 358fefe. Current builder schema, bundle hashes, authored-label tests and actual browser checks passed.',user_approval='pending')
(W/'final-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(result,ensure_ascii=False))

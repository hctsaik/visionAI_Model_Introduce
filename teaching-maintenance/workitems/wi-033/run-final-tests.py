from pathlib import Path
import subprocess,sys,json
W=Path(__file__).resolve().parent;C=W.parents[1]
extra=sys.argv[1:] and sys.argv[1]=='extra'
names=['test_tall_mobile_artwork.py','test_deep_dive_mobile_steps.py','test_resnet_deep_dive.py','test_segformer_deep_dive.py','test_collapsed_deep_dive.py','test_concept_zoom_edges.py'] if extra else ['test_engineering_mobile_pages.py','test_github_pages_bundle.py','test_interactive_navigation.py']
cmd=[sys.executable,'-m','pytest',*['tests/'+n for n in names],'-q']
r=subprocess.run(cmd,cwd=C,capture_output=True,text=True,encoding='utf8',errors='replace')
(W/('final-extra-tests.json' if extra else 'batch7-tests.json')).write_text(json.dumps(dict(command=cmd,exit_code=r.returncode,stdout=r.stdout,stderr=r.stderr),ensure_ascii=False,indent=2),encoding='utf8')
print(r.stdout);print(r.stderr);sys.exit(r.returncode)

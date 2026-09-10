import json,subprocess,sys
from pathlib import Path
W=Path(__file__).resolve().parent;C=W.parents[1];sys.path.insert(0,str(C/'tools'))
from verify_interactive_learning_html import embedded_course_data
old=embedded_course_data(subprocess.check_output(['git','show','9a5c147:docs/index.html'],cwd=C).decode('utf-8'))
new=embedded_course_data((C/'docs/index.html').read_text(encoding='utf-8'))
a={t['id']:t for t in old['topics']};b={t['id']:t for t in new['topics']}
changed=[k for k in a if a[k]!=b[k]];expected=list(json.loads((W/'lesson-content.json').read_text(encoding='utf-8')))
assert set(changed)==set(expected),(changed,expected)
assert a['charuco']==b['charuco']
out={'changed_topics':changed,'unchanged_topics':len(a)-len(changed),'charuco_payload_unchanged':True,'baseline_commit':'9a5c147','content_commit':'ca72546'}
(W/'scope-verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(out)

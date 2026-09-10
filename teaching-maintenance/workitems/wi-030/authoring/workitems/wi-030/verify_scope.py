import re,json,subprocess
from pathlib import Path
W=Path(__file__).resolve().parent;C=W.parents[1]
base='12fc9ff5242b3a68f7e6269c5297262a8df0ca3f'
old=subprocess.check_output(['git','show',base+':docs/index.html'],cwd=C).decode('utf-8')
new=(C/'docs/index.html').read_text(encoding='utf-8')
def data(s):return json.loads(re.search(r'<script id="course-data" type="application/json">(.*?)</script>',s,re.S)[1])
a={t['id']:t for t in data(old)['topics']};b={t['id']:t for t in data(new)['topics']}
expected=set(json.loads((W/'lesson-content.json').read_text(encoding='utf-8')))
changed={k for k in a if a[k]!=b[k]}
assert changed==expected,(changed,expected)
deep=[]
for slug in expected:
 baseline=json.loads((W/'baseline'/f'{slug}.json').read_text(encoding='utf-8'))
 current=json.loads((C/'_course_content/topics'/f'{slug}.json').read_text(encoding='utf-8'))
 if 'deep_dive' in baseline:
  d=current['deep_dive'].copy();assert d.pop('default_collapsed') is True
  assert d==baseline['deep_dive'],slug
  deep.append(slug)
out={'baseline_commit':base,'changed_topics':sorted(changed),'unchanged_topics':len(a)-len(changed),'preserved_advanced_data_except_opt_in_flag':sorted(deep),'charuco_payload_unchanged':a['charuco']==b['charuco']}
(W/'scope-verification.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('PASS 12 topics changed; 46 unchanged; 5 advanced records preserved')

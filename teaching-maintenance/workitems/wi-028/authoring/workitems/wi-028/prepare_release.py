import json
from pathlib import Path
W=Path(__file__).resolve().parent;C=W.parents[1]
# Preserve historical snapshot records; only refresh this workitem and shared authority.
s=(W.parent/'wi-029/sync_maintenance.py').read_text(encoding='utf-8').replace('WI-029','WI-028').replace('wi-029','wi-028')
start=s.index("for src in (C/'_course_content/supporting-lessons')")
end=s.index("new['project/CLAUDE.md']",start)
s=s[:start]+'''for slug in json.loads((W/'lesson-content.json').read_text(encoding='utf-8')):
 src=C/'_course_content/topics'/f'{slug}.json'
 new['workitems/wi-028/authoring/_course_content/topics/'+src.name]=src
 t=json.loads(src.read_text(encoding='utf-8'));rel=t['review_trace']['authority']
 new['workitems/wi-028/authoring/'+rel]=C/rel
for rel in ['_course_content/learner-briefs.json','tools/build_interactive_learning_html.py','tests/test_tall_mobile_artwork.py']:
 new['workitems/wi-028/authoring/'+rel]=C/rel
for src in W.glob('*.py'):new['workitems/wi-028/authoring/workitems/wi-028/'+src.name]=src
''' + s[end:]
(W/'sync_maintenance.py').write_text(s,encoding='utf-8')
s=(W.parent/'wi-027/publish_check.py').read_text(encoding='utf-8').replace('wi027','wi028').replace('==30','==36').replace('30 PNG','36 PNG')
(W/'publish_check.py').write_text(s,encoding='utf-8')
p=W/'verify_bundle.py';s=p.read_text(encoding='utf-8');start=s.index(",'build_retry':");end=s.index('}',start);s=s[:start]+s[end:];p.write_text(s,encoding='utf-8')
print('Release verification prepared, not run; no publication yet')

from pathlib import Path
import json,runpy,sys,hashlib,urllib.parse
W=Path(__file__).resolve().parent;C=W.parents[1]
a=json.loads((W/'inventory.json').read_text(encoding='utf8'));owners=[r['id'] for r in a];assert len(owners)==52 and all(r['status']=='local_complete' for r in a)
sys.argv=[str(W/'verify-batch.py'),*owners];runpy.run_path(str(W/'verify-batch.py'),run_name='__main__')
v=json.loads((W/'verification-all52.json').read_text(encoding='utf8'));assert len(v['changed_topics'])==52 and v['unchanged_topics']==6 and v['ui_states']==208
# Reuse only matching previously observed image versions; do not relabel older screenshots as new captures.
known={}
for p in W.glob('verification-*.json'):
 if p.name=='verification-all52.json':continue
 for row in json.loads(p.read_text(encoding='utf8')).get('http',[]):
  rel=urllib.parse.unquote(urllib.parse.urlparse(row['url']).path).lstrip('/').removeprefix('docs/')
  known.setdefault(rel,set()).add(row['sha256'])
reused=[]
for owner in owners:
 for row in json.loads((W/'pages'/owner/'report.json').read_text(encoding='utf8')):
  for im in row['images']:
   rel=urllib.parse.unquote(urllib.parse.urlparse(im['src']).path).lstrip('/').removeprefix('docs/');sha=hashlib.sha256((C/rel).read_bytes()).hexdigest();assert sha in known.get(rel,set()),rel
   reused.append(dict(topic=owner,path=rel,sha256=sha))
v.update(qa_evidence_policy='208 page states accumulated across seven batches; final 44 captured on current HTML. Prior image versions reused only after matching recorded HTTP SHA. All 52 current HTTP links and bundle hashes rechecked now.',verified_image_references=len(reused),image_version_evidence=reused)
(W/'verification-all52.json').write_text(json.dumps(v,ensure_ascii=False,indent=2),encoding='utf8')
print('All 52 current links and reviewed image versions verified')

import json,re,hashlib,sys,urllib.request,urllib.parse,concurrent.futures
from pathlib import Path
W=Path(__file__).resolve().parent;C=W.parents[1];sys.path.insert(0,str(C/'tools'))
from build_github_pages_site import referenced_assets
owners=sys.argv[1:];assert owners
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
html=(C/'interactive-learning.html').read_text(encoding='utf-8');old=(W/'baseline/interactive-learning.html').read_text(encoding='utf-8')
def data(s):return json.loads(re.search(r'<script id="course-data" type="application/json">(.*?)</script>',s,re.S)[1])
a={t['id']:t for t in data(old)['topics']};b={t['id']:t for t in data(html)['topics']}
changed=sorted(k for k in a if a[k]!=b[k]);assert set(owners)<=set(changed)
assert sha(C/'interactive-learning.html')==sha(C/'docs/index.html')
assets=referenced_assets(html)
for rel in assets:assert sha(C/rel)==sha(C/'docs'/rel),rel
paths=set();states=[]
for owner in owners:
 rows=json.loads((W/'pages'/owner/'report.json').read_text(encoding='utf-8'));assert len(rows)==4 and all(r['complete'] for r in rows)
 states+=rows
 for r in rows:
  for im in r['images']:
   rel=urllib.parse.unquote(urllib.parse.urlparse(im['src']).path).lstrip('/');rel=rel.removeprefix('docs/');paths.add(rel)
 for key in ['modelPath','manifestPath']:paths.add(b[owner][key])
 for width in [360,1440]:
  reading=(W/'pages'/owner/f'docs-{width}-reading.txt').read_text(encoding='utf-8');t=json.loads((C/'_course_content/topics'/f'{owner}.json').read_text(encoding='utf-8'))
  expanded=(W/'pages'/owner/f'docs-{width}-expanded.txt').read_text(encoding='utf-8')
  # Some lessons intentionally put model background in a collapsed reference.
  # Verify it in the actual expanded-page capture; the exercise stays first-read.
  assert t['mental_model']['body'] in expanded,(owner,width,'expanded model background')
  assert t['micro_example']['reveal'] in reading,(owner,width,'exercise explanation')
  assert all(v['title'] in reading for v in t['beginner_path']['visuals']),(owner,width,'main visual titles')
def check(args):
 prefix,rel=args;url='http://127.0.0.1:8000/'+prefix+urllib.parse.quote(rel,safe='/')
 with urllib.request.urlopen(url,timeout=30) as r:buf=r.read();status=r.status
 digest=hashlib.sha256(buf).hexdigest();assert digest==sha(C/rel),url
 return dict(url=url,status=status,sha256=digest)
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:http=list(pool.map(check,[(p,r) for p in ['','docs/'] for r in sorted(paths)]))
result=dict(owners=owners,changed_topics=changed,unchanged_topics=58-len(changed),html_sha256=sha(C/'interactive-learning.html'),bundle_assets=len(assets),bundle_hashes_match=True,ui_states=len(states),zoom_checks=sum(r['zoom_checks'] for r in states),answers=sum(r['answer'] for r in states),navigation=sum(r['navigation'] for r in states),http_checks=len(http),http=http,user_approval='pending',published=False,model_inference=False)
(W/('verification-all52.json' if len(owners)==52 else 'verification-'+'-'.join(owners)+'.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print({k:v for k,v in result.items() if k!='http'},flush=True)

import json,re,hashlib,sys,urllib.request,concurrent.futures
from pathlib import Path
W=Path(__file__).resolve().parent;C=W.parents[1];sys.path.insert(0,str(C/'tools'))
from build_github_pages_site import referenced_assets
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
html=(C/'interactive-learning.html').read_text(encoding='utf-8');old=(W/'baseline/interactive-learning.html').read_text(encoding='utf-8')
def data(s):return json.loads(re.search(r'<script id="course-data" type="application/json">(.*?)</script>',s,re.S)[1])
a={t['id']:t for t in data(old)['topics']};b={t['id']:t for t in data(html)['topics']}
slugs=list(json.loads((W/'lesson-content.json').read_text(encoding='utf-8')))
changed=sorted(k for k in a if a[k]!=b[k]);assert changed==sorted(slugs),changed
assert sha(C/'interactive-learning.html')==sha(C/'docs/index.html')
assets=referenced_assets(html)
for rel in assets:assert sha(C/rel)==sha(C/'docs'/rel),rel
records=[]
for slug in slugs:
 rows=json.loads((W/'pages'/slug/'report.json').read_text(encoding='utf-8'))
 assert len(rows)==4 and all(r['complete'] for r in rows),slug
 records+=rows
 for width in [360,1440]:
  reading=(W/'pages'/slug/f'docs-{width}-reading.txt').read_text(encoding='utf-8')
  topic=json.loads((C/'_course_content/topics'/f'{slug}.json').read_text(encoding='utf-8'))
  assert topic['mental_model']['body'] in reading,(slug,'core missing')
  assert topic['micro_example']['reveal'] in reading,(slug,'quiz missing')
  assert len(topic['beginner_path']['visuals'][0]['callouts'])==3
  assert 'candidate' not in reading.lower(),(slug,'production marker')
main=[]
for slug in slugs:main+=json.loads((W/f'{slug}-active-assets.json').read_text(encoding='utf-8'))
main={r['image']:r for r in main};engineering=json.loads((W/'engineering-active-assets.json').read_text(encoding='utf-8'))
assert len(main)==28 and len(engineering)==48
assert len({r['sha256'] for r in engineering})==48
assert not {r['sha256'] for r in main.values()} & {r['sha256'] for r in engineering}
paths=set(main)|{r['image'] for r in engineering}
for row in list(main.values())+engineering:assert sha(C/row['image'])==row['sha256']
for slug in slugs:
 for key in ['modelPath','manifestPath']:paths.add(b[slug][key])
 for slide in b[slug]['slides']:
  for link in slide.get('evidenceLinks',[]):paths.add(link['image'])
http=[]
def check(args):
 prefix,rel=args;url='http://127.0.0.1:8000/'+prefix+urllib.parse.quote(rel,safe='/')
 with urllib.request.urlopen(url,timeout=30) as r:buf=r.read();status=r.status
 digest=hashlib.sha256(buf).hexdigest();assert digest==sha(C/rel),url
 return {'url':url,'status':status,'sha256':digest}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
 http=list(pool.map(check,[(prefix,rel) for prefix in ['','docs/'] for rel in sorted(paths)]))
retained=json.loads((W/'retained-evidence.json').read_text(encoding='utf-8'))
for r in retained:assert sha(C/r['source'])==sha(C/r['image'])==r['sha256']
result={'html_sha256':sha(C/'interactive-learning.html'),'changed_topics':changed,'unchanged_topics':58-len(changed),'bundle_assets':len(assets),'all_bundle_hashes_match':True,'main_pngs':len(main),'engineering_pngs':len(engineering),'retained_png_copies':len(retained),'main_engineering_hash_overlap':False,'ui_states':len(records),'zoom_checks':sum(r['zoom_checks'] for r in records),'answers':sum(r['answer'] for r in records),'navigation':sum(r['navigation'] for r in records),'http_checks':len(http),'http':http,'model_inference_performed':False,'human_learning_test':False,'user_approval':'pending','published':False}
(W/'final-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print({k:v for k,v in result.items() if k!='http'},flush=True)

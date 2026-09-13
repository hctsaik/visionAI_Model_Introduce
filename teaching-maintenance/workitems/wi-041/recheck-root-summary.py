from pathlib import Path
import json,hashlib
W=Path(__file__).resolve().parent;C=W.parents[1]
def read(n):return json.loads((W/n).read_text(encoding='utf8'))
content=read('recheck-content-coverage.json');images=read('recheck-file-image-decode.json');pub=read('recheck-public-verification.json');assets=read('recheck-asset-audit.json');anchors=read('recheck-external-rendered-anchors.json');sources=read('recheck-source-links.json')
assert len(content)==58 and all(x['default_question_present'] and x['expanded_mechanism_present'] for x in content)
assert len(images)==116 and all(len({r['topic'] for r in images if r['width']==w})==58 for w in [1440,390])
assert all(i['ok'] for r in images for i in r['images'])
assert all(x['equal'] for x in assets['assets']) and not assets['failures']['public_assets']
assert hashlib.sha256((C/'docs/index.html').read_bytes()).hexdigest()==pub['public_html_sha256']
assert (C/'docs/index.html').read_bytes()==(C/'interactive-learning.html').read_bytes()
actual={x['href'] for r in anchors['rows'] for x in r['links']};tested={x['url'] for x in sources['results']};assert actual<=tested
browser=[]
for w in [1440,390]:
    d=read(f'recheck-coverage-{w}.json')
    browser.append({'width':w,'lessons':len(d['lessons']),'unique_lessons':len({r['topic'] for r in d['lessons']}),'slides':sum(len(r.get('slides',[])) for r in d['lessons']),'common_routes':len(d.get('routes',[])),'fatal':d.get('fatal'),'note':'8000 image errors retained; use separate decode and stable HTTP evidence'})
summary={'html_sha256':pub['public_html_sha256'],'content_rows':len(content),'image_decode_states':len(images),'image_decode_checks':sum(len(r['images']) for r in images),'decode_failures':0,'assets':len(assets['assets']),'external_rendered_unique_hrefs':len(actual),'source_urls':len(tested),'browser':browser,'findings':'6 lessons text; not implemented','legacy_verifier':'failed on obsolete AOI UI text; not a green gate','user_approval':'pending','product_modified':False}
(W/'recheck-root-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(summary,ensure_ascii=False))

import hashlib,json,re,subprocess,sys,time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests
W=Path(__file__).resolve().parent
C=W.parents[1];R=C.parents[1]
def sha(b): return hashlib.sha256(b).hexdigest()
def checkpoint(message):
    for p in [R/'WORKITEMS.md',C/'BEGINNER_VISUAL_TODO.md',C/'BEGINNER_VISUAL_STATUS.md']:
        p.write_text('## WI-032-P 發布 checkpoint（2026-09-11）\n\n'+message+'\n\n'+p.read_text(encoding='utf-8'),encoding='utf-8')
mode=sys.argv[1]
if mode=='prepare':
    checkpoint('使用者已明確授權 commit + push。正在整理第一部分六課與最新學習／接續紀錄，尚未提交；完成後核對遠端與公開網站。第二部分 52 課保持未開始，下次由 Overall_Review.md 第二部分接續。細項見 workitems/wi-032/PLAN.md 的 WI-032-P。')
    html=(C/'docs/index.html').read_bytes()
    expected=json.loads((W/'final-verification.json').read_text(encoding='utf-8'))['final_html_freeze']['reviewed_sha256']
    assert sha(html)==expected
    assert html==(C/'interactive-learning.html').read_bytes()
    untracked=subprocess.check_output(['git','ls-files','--others','--exclude-standard','docs'],cwd=C,text=True).splitlines()
    parked=[]
    for rel in untracked:
        p=C/rel
        if p.suffix=='.png' and 'WI032-' in p.name and p.name.encode() not in html:
            dest=W/'unused-publish-candidates'/p.name
            dest.parent.mkdir(exist_ok=True)
            assert not dest.exists()
            p.rename(dest);parked.append(rel)
    (W/'release-precheck.json').write_text(json.dumps({'html_sha256':expected,'unused_candidates_preserved_outside_docs':parked},indent=2),encoding='utf-8')
    print('Reviewed HTML unchanged; preserved unused candidates:',len(parked))
elif mode=='public':
    head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=C,text=True).strip()
    base='https://hctsaik.github.io/visionAI_Model_Introduce/'
    paths=[C/'docs/index.html']
    html=paths[0].read_text(encoding='utf-8')
    paths += [p for p in (C/'docs').rglob('*.png') if 'wi032' in p.name.lower() and p.name in html]
    data=json.loads(re.search(r'<script id="course-data" type="application/json">(.*?)</script>',html,re.S)[1])
    slugs=set(json.loads((W/'lesson-content.json').read_text(encoding='utf-8')))
    paths += [C/'docs'/t[k] for t in data['topics'] if t['id'] in slugs for k in ['modelPath','manifestPath']]
    def check(p):
        rel=p.relative_to(C/'docs').as_posix()
        res=requests.get(base+rel+'?wi032='+head,timeout=45);res.raise_for_status()
        assert sha(res.content)==sha(p.read_bytes()),rel
        return {'path':rel,'sha256':sha(res.content),'status':res.status_code}
    with ThreadPoolExecutor(max_workers=6) as pool: rows=list(pool.map(check,paths))
    (W/'public-release-verification.json').write_text(json.dumps({'commit':head,'url':base,'checks':rows,'checked_files':len(rows),'user_approval':'pending','part_two':'not_started'},indent=2),encoding='utf-8')
    print('Public byte checks PASS:',len(rows),head)

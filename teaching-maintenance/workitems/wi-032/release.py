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
        committed=subprocess.check_output(['git','show',head+':docs/'+rel],cwd=C)
        assert sha(res.content)==sha(committed),rel
        local=p.read_bytes()
        if p.suffix=='.md':
            assert local.replace(b'\r\n',b'\n')==committed.replace(b'\r\n',b'\n'),rel
        else: assert local==committed,rel
        return {'path':rel,'sha256':sha(res.content),'status':res.status_code,'matches_committed_bytes':True,'local_line_endings_only':local!=committed}
    with ThreadPoolExecutor(max_workers=6) as pool: rows=list(pool.map(check,paths))
    (W/'public-release-verification.json').write_text(json.dumps({'commit':head,'url':base,'checks':rows,'checked_files':len(rows),'user_approval':'pending','part_two':'not_started'},indent=2),encoding='utf-8')
    print('Public byte checks PASS:',len(rows),head)
elif mode=='record':
    evidence=json.loads((W/'public-release-verification.json').read_text(encoding='utf-8'))
    message=f"第一部分六課成果已 commit 並 push：{evidence['commit']}；GitHub Pages 部署成功，公開 {evidence['checked_files']} 個檔案逐一 hash 與已提交內容一致（本機部分 Markdown 為 CRLF，Git 為 LF，文字內容一致）。發布證據為 workitems/wi-032/public-release-verification.json。最新學習及接續資料同步保存在 Git 的 teaching-maintenance。使用者成品核准仍 pending；第二部分 52 課未開始，下次依根 Overall_Review.md 第二部分接續。此段取代下方歷史未發布狀態。"
    checkpoint(message)
    for p in [R/'Overall_Review.md',W/'REPORT.md',C/'teaching-maintenance/README.md']:
        p.write_text('## WI-032 發布完成（2026-09-11）\n\n'+message+'\n\n'+p.read_text(encoding='utf-8'),encoding='utf-8')
    p=W/'PLAN.md';s=p.read_text(encoding='utf-8').replace('- [ ] 核對 Pages 結果與公開內容，保存發布證據及接續狀態。','- [x] 核對 Pages 結果與公開內容，保存發布證據及接續狀態。')
    p.write_text(s+'\n\n發布完成 checkpoint：'+message+'\n公開 API 已核對 Pages run 34538018042 success。即將將本發布證據另行提交及推送；該紀錄提交不更動 docs 教材。\n',encoding='utf-8')

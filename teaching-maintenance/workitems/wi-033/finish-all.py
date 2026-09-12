from pathlib import Path
import json,hashlib,re,runpy,subprocess,sys,urllib.request
W=Path(__file__).resolve().parent;C=W.parents[1];R=C.parents[1]
load=lambda n:json.loads((W/n).read_text(encoding='utf8'))
assert load('maintenance-verification.json')['status']=='passed'
v=load('verification-all52.json');a=load('final-selected-assets.json');assert a['active_pngs']==460
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(C/'interactive-learning.html')==sha(C/'docs/index.html')==v['html_sha256']
for route in ['interactive-learning.html','docs/index.html']:
 with urllib.request.urlopen('http://127.0.0.1:8000/'+route) as q:assert hashlib.sha256(q.read()).hexdigest()==v['html_sha256']
links=[]
for link in re.findall(r'\]\(([^)]+)\)',(W/'REPORT.md').read_text(encoding='utf8')):
 if link.startswith(('http://','https://')):continue
 assert (W/link).exists(),link;links.append(link)
diff=subprocess.run(['git','diff','--check'],cwd=C,capture_output=True,text=True);assert diff.returncode==0,diff.stdout+diff.stderr
out=dict(status='local_complete',complete_lessons=52,pending_implementation=0,active_pngs=460,engineering_pngs=416,html_sha256=v['html_sha256'],bundle_assets=1370,latest_http_checks=1506,accumulated_main_states=208,accumulated_zoom_checks=1472,accumulated_deep_states=160,latest_main_states=44,latest_tests=24,latest_subtests=130,mobile_caption_topics=58,mobile_captions=178,report_local_links_checked=len(links),git_diff_check=dict(exit_code=diff.returncode,stdout=diff.stdout,stderr=diff.stderr),maintenance='maintenance-verification.json',user_approval='pending',published=False,model_inference=False,evidence_policy=v['qa_evidence_policy'])
(W/'final-verification.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8')
p=W/'PLAN.md';p.write_text(p.read_text(encoding='utf8').replace('- [ ] 全站必要回歸','- [x] 全站必要回歸'),encoding='utf8')
p=W/'REPORT.md';p.write_text(p.read_text(encoding='utf8').replace('維護副本將保存於','維護副本已保存並核對於')+'\n最終交付核對：[final-verification.json](final-verification.json)；維護副本：[maintenance-verification.json](maintenance-verification.json)。\n',encoding='utf8')
note='''## WI-033 最終完成：第二部分52/52課（2026-09-12）

- 狀態：本機實作、逐圖／逐課審查、必要驗證、學習與維護副本完成；實作待辦0。使用者成品核准pending，未commit／push／發布，沒有新增模型推論。
- 成果：52課208组工程故事（416桌機／手機PNG）及指定主圖／深讀修正，共460張新啟用PNG；逐圖自評91–93，五項完成度>=8、無否決項。第一部分6課教材資料未改。
- 證據：workitems/wi-033/REPORT.md、final-selected-assets.json、verification-all52.json、final-verification.json、maintenance-verification.json；相對於teaching-images/vision-ai-model-selection。
- 實際驗證：1370來源/docs資產一致、最終1506HTTP與兩HTML入口hash一致；累計208主頁1472放大、160深讀，最後44主頁在最終HTML重拍。最終24 tests/130 subtests、58課178手機圖說及git diff --check通過；未宣稱所有歷史套件通過。
- 接續：唯一checklist在workitems/wi-033/PLAN.md，已全勾選。本輪授權範圍無未完成項及阻礙；後續依使用者成品回饋或發布指示另續。以下較早checkpoint保留作歷史，不代表仍待製作。
'''
(W/'checkpoint-note.md').write_text(note,encoding='utf8');runpy.run_path(str(W/'append-checkpoint.py'))
p=R/'Overall_Review.md';p.write_text(note+'\n'+p.read_text(encoding='utf8'),encoding='utf8')
print('All implementation, reviews, tests and documentation complete; refreshing final snapshot records')
subprocess.run([sys.executable,str(W/'sync-maintenance.py')],check=True)

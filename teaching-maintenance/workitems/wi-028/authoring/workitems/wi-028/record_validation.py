import json
from pathlib import Path
W=Path(__file__).resolve().parent;C=W.parents[1]
slugs=list(json.loads((W/'lesson-content.json').read_text(encoding='utf-8')))
reports=[r for s in slugs for r in json.loads((W/('qa-'+s)/'report.json').read_text(encoding='utf-8'))]
assert len(reports)==48 and sum(r['zoom_loaded_escape'] for r in reports)==144
out={'states':48,'zooms':144,'final_page_states':len(json.loads((W/'final-page-checks.json').read_text(encoding='utf-8'))),'http_png_checks':72,'pytest':'7 tests + 4 subtests; bundle 1 test passed','legacy_verifier':'FAIL existing charuco inline visual 1 schema; see WI-018 history','user_review':'pending','model_inference':'not performed; educational illustrations'}
(W/'validation-summary.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for slug in slugs:
 p=C/'_course_content/topics'/(slug+'.json');t=json.loads(p.read_text(encoding='utf-8'))
 t['quality_status']={'label':'首讀圖文已核對','state':'self-reviewed','round':'WI-028','reason':'新版首讀逐圖與整頁自評、桌機手機互動驗證完成；使用者核准pending。原工程圖未納入本輪分數。'}
 p.write_text(json.dumps(t,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Recorded actual validation; quality self-reviewed, user pending')

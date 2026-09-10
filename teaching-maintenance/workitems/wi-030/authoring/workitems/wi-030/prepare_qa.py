from pathlib import Path
W=Path(__file__).resolve().parent
for name in ['qa_lesson.py','run_qa.py','http_assets.py','final_pages.py','verify_bundle.py']:
 s=(W.parent/'wi-028'/name).read_text(encoding='utf-8').replace('wi028','wi030').replace('wi-028','wi-030').replace('WI-028','WI-030')
 if name=='qa_lesson.py':
  s=s.replace("nxt=page.get_by_role('button').filter(has_text='→').last", "nxt=page.locator('.lesson-footer button').last")
  s=s.replace("image_records=[]", "image_records=[]\n            if page.locator('.legacy-deep-reference').count():\n                assert not page.locator('.legacy-deep-reference').evaluate('(e)=>e.open')")
 if name=='run_qa.py':s=s.replace(')[1:]',')')
 (W/name).write_text(s,encoding='utf-8')
print('QA prepared; execution awaits full integration')

from pathlib import Path
W=Path(__file__).resolve().parent;C=W.parents[1]
sync=(C/'workitems/wi-038/sync.py').read_text(encoding='utf8').replace('wi-038','wi-040').replace('WI-038','WI-040').replace('wi-037','wi-039')
sync=sync.replace("'tests/test_poc_workbench.py']", "'tests/test_poc_workbench.py','tests/test_release_hardening.py','_course_content/topics/convnext.json','_course_content/topics/v-jepa.json','_course_content/topics/ad-anomalygpt.json']")
(W/'sync.py').write_text(sync,encoding='utf8')
public=(C/'workitems/wi-038/verify-public.py').read_text(encoding='utf8')
public=public.replace("page.goto(url+'#view=poc');assert page.locator('#poc-model').count()==0", "page.goto(url+'#view=home');page.locator('main .hero-actions [data-view=\"poc\"]').click();page.locator('#poc-answer').wait_for();assert page.locator('#poc-model').count()==0")
(W/'verify-public.py').write_text(public,encoding='utf8')
print('Prepared snapshot and public-verification scripts')

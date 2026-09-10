import hashlib,json
from pathlib import Path
W=Path(__file__).resolve().parent;C=W.parents[1]
read=lambda p:json.loads(p.read_text(encoding='utf-8'))
pages=read(W/'page-review.json');images=read(W/'image-review.json');final=read(W/'final-page-checks.json')
qa=[r for p in W.glob('qa-*/report.json') for r in read(p)]
assert len(qa)==72 and sum(r['zoom_loaded_escape'] for r in qa)==216
assert all(r['answer'] and r['navigation'] and not r['page_errors'] and not r['overflow'] for r in qa)
assert len(final)==24 and all(r['conditional_quiz_answer_checked'] and r['core_comparison_and_cost_visible'] and not r['errors'] and not r['overflow'] for r in final)
assert len(images)==42 and min(r['total'] for r in images)>90
assert len(pages)==12 and all(r['total']>90 and not r['veto'] for r in pages)
http=read(W/'http-assets.json');assert len(http)==84 and all(r['status']==200 for r in http)
bundle=read(W/'bundle-verification.json');assert bundle['assets']==1347 and bundle['all_source_docs_hashes_match'] and bundle['html_hash_matches']
handoff=read(W/'handoff-http.json');assert len(handoff)==24 and all(r['status']==200 for r in handoff)
out={'workitem':'WI-030','html_sha256':hashlib.sha256((C/'docs/index.html').read_bytes()).hexdigest(),
 'ui_states':72,'zoom_decode_escape':216,'final_reading_and_revised_quiz_states':24,'pngs':42,'stories':21,'local_http_hash_checks':84,
 'image_score_range':[min(r['total'] for r in images),max(r['total'] for r in images)],'page_score_range':[min(r['total'] for r in pages),max(r['total'] for r in pages)],
 'selected_preflights':{'count':42,'result':'passed before integration; per-version files retained'},
 'focused_pytest':{'result':'passed','tests':9,'subtests':10,'files':['test_collapsed_deep_dive.py','test_tall_mobile_artwork.py','test_deep_dive_mobile_steps.py','test_interactive_navigation.py'],'evidence':'actual completed session 48486 before quiz-only and self-review metadata changes'},
 'bundle_pytest':{'result':'passed','tests':2,'subtests':116,'file':'test_github_pages_bundle.py','evidence':'completed session 73750 after fixing handoff document inclusion; earlier one-test result retained in checkpoint history'},
 'handoff_document_http_hash_checks':24,
 'legacy_full_verifier':{'result':'failed','message':'ValueError: charuco: invalid inline mechanism visual 1','scope':'existing unchanged ChArUco; not counted as passing'},
 'scope':read(W/'scope-verification.json'),'bundle':bundle,'public_release':'pending separate public-release-verification.json',
 'user_approval':'pending','model_inference_performed':False,'human_learning_test_performed':False,
 'evidence_scope':'72-state interaction covers unchanged PNG/UI; final 24-state run covers revised quiz and final metadata. Legacy engineering images were preserved, not rerated.'}
(W/'validation-summary.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Validated aggregate evidence: 72 + 24 states, 216 zoom/Escape, 84 HTTP hashes, 42 PNG')

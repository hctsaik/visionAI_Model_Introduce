from pathlib import Path
import json,runpy
W=Path(__file__).resolve().parent
d=json.loads((W/'batch3-deep-report.json').read_text(encoding='utf-8'))
assert len(d)==64 and all(r['complete'] for r in d)
(W/'batch3-tests-supplement.json').write_text(json.dumps(dict(result='2 passed, 7 deselected in 21.23s',prior='15 passed, 120 subtests passed; two old runtime assertions failed',fix='scope deep-dive assertions to deep container, count desktop and authored full-mobile separately; beginner main remains outside',command='python -m pytest tests/test_resnet_deep_dive.py tests/test_segformer_deep_dive.py -q -k runtime_renders_only'),indent=2),encoding='utf-8')
(W/'batch3-deep-page-review.json').write_text(json.dumps(dict(status='passed',reviewed=['resnet/docs-360-c02-v01','resnet/docs-360-c02-v02','resnet/docs-360-c04-v01','resnet/docs-360-c08-v02','resnet/docs-360-c08-v03','resnet/docs-360-c08-v04','segformer/docs-360-c01-v01','segformer/docs-360-c01-v02','segformer/docs-360-c03-v01','segformer/docs-360-c04-v01','segformer/docs-360-c05-v01'],evidence='11 selected new deep mobile designs viewed individually in actual docs at 360px. Equations, original anchor images, scale grids, 3-panel flow and captions visible without clipping. Native assessment remains separate. Long vertical scrolling and smaller historical metadata are limitations.',automated_states=64,user_approval='pending'),indent=2),encoding='utf-8')
note='''### WI-033 第三批測試與深讀完成、第四批即將渲染

第三批17項測試已通過（原15 tests/120 subtests，補驗2 tests/21.23s）；深讀64狀態通過，11種新手機圖已逐張頁內實看，證據batch3-tests-supplement.json、batch3-deep-page-review.json。ResNet與ConvNeXt主頁各4狀態通過，其餘五課正在QA，尚待全部頁面實看與HTTP資產核對，完成數仍10/52。第四批8工程2原型已通過preflight並完成新SVG場景程式，即將render.py產出16PNG；未原生審、未整合。預期workitems/wi-033/*-engineering-2-r01-{desktop,mobile}.png。後續24工程故事、兩個主反例與後27課持續執行。使用者核准pending，未發布。
'''
(W/'checkpoint-note.md').write_text(note,encoding='utf-8');runpy.run_path(str(W/'append-checkpoint.py'))

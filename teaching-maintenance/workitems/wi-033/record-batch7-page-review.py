from pathlib import Path
import json,hashlib,sys,runpy
W=Path(__file__).resolve().parent;p=W/'batch7-page-view-ledger.json'
a=json.loads(p.read_text(encoding='utf8')) if p.exists() else {}
for owner in sys.argv[1:]:
 files=[W/f'pages/{owner}/docs-{width}-engineering-{i}.png' for width in [1440,360] for i in range(1,5)]
 a[owner]=dict(actual_viewed=True,files=[dict(path=f.relative_to(W).as_posix(),sha256=hashlib.sha256(f.read_bytes()).hexdigest()) for f in files],notes='兩尺寸四工程均逐張實看：三節點可讀，手機縱向閱讀與底部放大入口完整；部分術語仍需正文。',user_approval='pending')
p.write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf8')
(W/'checkpoint-note.md').write_text(f'### WI-033 第七批頁內審查checkpoint\n\n11課88工程PNG與2張SR主反例已整合並建置，1370資產。8 tests/120 subtests通過（114.91秒）；44頁狀態QA持續。已逐張頁內實看{len(a)}課{len(a)*8}工程截圖，名單及hash見batch7-page-view-ledger.json；V-JEPA三首讀手機圖說間距另實看通過。尚未完成其餘頁內/全站驗證與收尾，不增加41/52完成數。使用者核准pending，未發布，全部52課持續。\n',encoding='utf8');runpy.run_path(str(W/'append-checkpoint.py'))

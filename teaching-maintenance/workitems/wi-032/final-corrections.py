from pathlib import Path
import json,subprocess,sys,shutil
W=Path(__file__).resolve().parent;C=W.parents[1]
id='sift-engineering-1'
p=W/'engineering-plan.json';rows=json.loads(p.read_text(encoding='utf-8'))
next(r for r in rows if r['id']==id)['title']='SIFT先找特徵，再交給配對器'
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
p=W/(id+'-r06.md');p.write_text((W/(id+'-r04.md')).read_text(encoding='utf-8')+'\n## r06 手機實頁修正\n標題改為「SIFT先找特徵，再交給配對器」，避免matcher被拆成m／atcher。節點、閱讀路徑、參考及單一takeaway不變。原生與實頁驗證pending；user approval pending。\n',encoding='utf-8')
subprocess.run([sys.executable,'-X','utf8',str(C/'tools/validate_teaching_preflight.py'),str(p)],check=True,stdout=subprocess.DEVNULL)
p=W/'render-engineering.py';s=p.read_text(encoding='utf-8').replace("+'-r05-'+mode","+'-r06-'+mode");p.write_text(s,encoding='utf-8')
subprocess.run([sys.executable,'-X','utf8',str(p),id],check=True)
p=W/'integrate-engineering.py';s=p.read_text(encoding='utf-8').replace("version='r05' if r['id']=='yolo-world-engineering-2' else 'r04'","version='r06' if r['id']=='sift-engineering-1' else ('r05' if r['id']=='yolo-world-engineering-2' else 'r04')");p.write_text(s,encoding='utf-8')
subprocess.run([sys.executable,'-X','utf8',str(p)],check=True)
# A figure-only screenshot excludes fixed site chrome; viewport evidence keeps it.
p=W/'qa-pages.py';s=p.read_text(encoding='utf-8').replace("fig.screenshot(path=str(O/f'{prefix}-main-{i}.png'))","fig.screenshot(path=str(O/f'{prefix}-main-{i}.png'),style='.topbar,.skip-link{visibility:hidden!important}')").replace("fig.screenshot(path=str(O/f'{prefix}-engineering-{i}.png'))","fig.screenshot(path=str(O/f'{prefix}-engineering-{i}.png'),style='.topbar,.skip-link{visibility:hidden!important}')");p.write_text(s,encoding='utf-8')

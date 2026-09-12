from pathlib import Path
import subprocess,json,hashlib,shutil,runpy
W=Path(__file__).resolve().parent;C=W.parents[1];R=C.parents[1];S=C/'teaching-maintenance'
def git(*args):
 r=subprocess.run(['git',*args],cwd=C,capture_output=True,text=True,encoding='utf8',errors='replace')
 if r.returncode:raise RuntimeError(r.stdout+r.stderr)
 return r.stdout
status=git('status','--porcelain','-z','--untracked-files=all').split('\0')
paths=[s[3:] for s in status if s];assert paths and all(p.startswith(('docs/','teaching-maintenance/')) for p in paths)
assert git('rev-list','--left-right','--count','HEAD...origin/main').split()==['0','0']
assert git('branch','--show-current').strip()=='main'
large=[(p,(C/p).stat().st_size) for p in paths if (C/p).is_file() and (C/p).stat().st_size>=100_000_000];assert not large,large
note='''## WI-033 Git提交／推送授權（2026-09-12）

使用者明確要求「Git check in push」。52課本機成果及驗證已完成；已fetch，main與origin/main無領先或落後。即將提交docs網站包及teaching-maintenance維護副本，再push origin main；沒有force push。沿用最終24 tests/130 subtests與1506HTTP驗證，教材內容未再修改。成品核准仍pending，Git推送與網站部署狀態分開。

- [ ] 提交已驗證成果，核對暫存範圍與差異。
- [ ] Push後核對遠端HEAD與本機一致，保存實際提交SHA。
'''
(W/'checkpoint-note.md').write_text(note,encoding='utf8');runpy.run_path(str(W/'append-checkpoint.py'))
(W/'GIT-RELEASE.md').write_text(note,encoding='utf8')
sources={'workitems/wi-033/WORKITEMS.md':R/'WORKITEMS.md','workitems/wi-033/BEGINNER_VISUAL_TODO.md':C/'BEGINNER_VISUAL_TODO.md','workitems/wi-033/BEGINNER_VISUAL_STATUS.md':C/'BEGINNER_VISUAL_STATUS.md','workitems/wi-033/PLAN.md':W/'PLAN.md','workitems/wi-033/GIT-RELEASE.md':W/'GIT-RELEASE.md','workitems/wi-033/git-checkin.py':Path(__file__)}
m=json.loads((S/'manifest.json').read_text(encoding='utf8'));known={r['snapshot']:r for r in m['files']}
for rel,src in sources.items():
 dst=S/rel;shutil.copyfile(src,dst)
 if rel not in known:known[rel]={'snapshot':rel};m['files'].append(known[rel])
 known[rel].update(source=str(src),sha256=hashlib.sha256(dst.read_bytes()).hexdigest())
(S/'manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
git('add','--','docs','teaching-maintenance')
check=subprocess.run(['git','diff','--cached','--check'],cwd=C,capture_output=True,text=True,encoding='utf8',errors='replace')
(W/'git-staged-check.json').write_text(json.dumps(dict(exit_code=check.returncode,stdout=check.stdout,stderr=check.stderr),ensure_ascii=False,indent=2),encoding='utf8')
assert check.returncode==0,check.stdout[:3000]
print(git('diff','--cached','--shortstat'),flush=True)
result=git('commit','-m','Complete part two revisions across 52 vision AI lessons')
(W/'git-commit-output.txt').write_text(result,encoding='utf8');print(result.splitlines()[0]);print(git('rev-parse','HEAD'))

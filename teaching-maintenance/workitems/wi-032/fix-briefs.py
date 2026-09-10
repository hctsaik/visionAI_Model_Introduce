import json
from pathlib import Path
W=Path(__file__).resolve().parent; C=W.parents[1]; R=C.parents[1]
p=C/'_course_content/learner-briefs.json'; data=json.loads(p.read_text(encoding='utf-8'))
for slug, brief in json.loads((W/'compact-briefs.json').read_text(encoding='utf-8')).items():
    assert all(len(s)<=68 for s in brief.values())
    data[slug].update(brief)
p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
status='六課新版主線28張與工程層48張PNG、正文與自測已整合至來源；新增工程手機直向圖及捲動放大。首讀摘要超長已精簡，正在重新建置及實頁驗證。原圖自評與頁面驗證分開；目前未發布、使用者核准pending。下一步：建置course/docs，逐課核對桌機／手機、放大、自測、導覽及資產一致性。產物：workitems/wi-032；完整歷程見PLAN.md。'
for p in [R/'WORKITEMS.md',C/'BEGINNER_VISUAL_TODO.md',C/'BEGINNER_VISUAL_STATUS.md']:
    s=p.read_text(encoding='utf-8'); first=s.find('\n## ',1)
    p.write_text('## WI-032 最新接續狀態（取代下方舊checkpoint）\n'+status+'\n'+s[first:],encoding='utf-8')
p=R/'Overall_Review.md';s=p.read_text(encoding='utf-8').replace('候選製作中／尚未整合','來源已整合／實頁驗證中');p.write_text(s,encoding='utf-8')

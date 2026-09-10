import json,hashlib
from pathlib import Path
W=Path(__file__).resolve().parent; C=W.parents[1];R=C.parents[1]
read=lambda p:json.loads(p.read_text(encoding='utf-8'))
images=read(W/'image-review.json');pages=read(W/'page-review.json');final=read(W/'final-page-checks.json')
assert len(images)==42 and len(pages)==12 and len(final)==24
for r in images:
 assert r['total']>90 and r['native_and_display_reviewed']
 assert hashlib.sha256((W/r['file']).read_bytes()).hexdigest()==r['sha256']
for r in pages:
 assert r['total']>90 and not r['veto']
 p=C/'_course_content/topics'/f"{r['slug']}.json"; t=read(p)
 t['quality_status']={'label':'首讀圖文已核對','state':'self-reviewed','round':'WI-030','reason':'新版逐圖與整頁自評、桌機手機驗證完成；使用者成品核准pending。原工程圖未納入本輪分數。'}
 p.write_text(json.dumps(t,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
checkpoint='''
## WI-030 最終審查 checkpoint（2026-09-11）
21故事42張PNG逐圖原生與936/328px審查完成，分數91–96，啟用版本及hash見selected-assets.json、image-review.json；十二課預設主線完成逐頁閱讀，自評92–93，證據與扣分見page-review.md。五課既有deep_dive資料保留，只增加預設收合旗標；原工程內容未算本輪評分。使用者成品核准pending。
72頁面狀態／216次解碼放大Escape／自測及導覽通過；最後自測改為帶條件的合理替代選擇，另測24桌機手機狀態，確認新解答實際展開可讀。84HTTP圖片hash、1231引用資產及HTML一致、12課變更／46課不變／5課舊章資料保留均通過。聚焦pytest 9 tests＋10 subtests、bundle 1 test通過。舊全站verifier仍在未改動ChArUco inline schema失敗，不計為通過。
即將執行：僅更新自評狀態後最後重建HTML與docs，刷新hash及範圍證據，保存teaching-maintenance快照，再依本輪既有授權commit/push並核對公開HTML與42PNG。現在公開站尚未更新；發布未完成。必要來源與prompt意圖在workitems/wi-030，截圖及原生PNG亦保存在該持久目錄。沒有模型推論或真人學習實測。
'''
for p in [W/'PLAN.md', R/'WORKITEMS.md', C/'BEGINNER_VISUAL_TODO.md', C/'BEGINNER_VISUAL_STATUS.md']:
 with p.open('a',encoding='utf-8') as f:f.write('\n'+checkpoint)
p=W/'PLAN.md';s=p.read_text(encoding='utf-8');lines=s.splitlines()
for i,line in enumerate(lines):
 if line.startswith('- [ ]') and '共用學習' not in line and 'Git' not in line:lines[i]=line.replace('- [ ]','- [x]',1)
p.write_text('\n'.join(lines)+'\n',encoding='utf-8')
learning='''
### WI-030 自測與入口驗證（2026-09-11）
沿用既有自測規則：題目不能只把「錯誤捷徑」對上顯而易見的正解；提供至少兩條在不同工作條件下成立的路線，讓讀者說明先核對的限制、資料與完整成本。解答必須寫出替代路線何時成立，而非只加一句「也可以」。本輪十二課已重寫並在24個實際桌機手機狀態展開核對；這是內容與介面證據，尚非真人學習成效。
建置經驗：複製發布bundle成功不代表HTML已由新來源重建；先build_interactive_learning_html，再build_github_pages_site，並核對實際預設可見內容。舊進階章節收合後，仍需驗證章節2→1、直接hash與工程圖導覽，不能因首圖可见就略過。失敗與修正保留在WI-030 PLAN及測試證據。
'''
for p in [R/'TEACHING_WEBPAGE_GUIDE.md',R/'TEACHING_REVIEW_LOG.md']:
 with p.open('a',encoding='utf-8') as f:f.write('\n'+learning)
print('Self-review status and durable checkpoints updated; publication still pending')

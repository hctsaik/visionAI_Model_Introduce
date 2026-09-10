from pathlib import Path
import json,hashlib,shutil
W=Path(__file__).resolve().parent; C=W.parents[1]; R=C.parents[1]
v=json.loads((W/'final-verification.json').read_text(encoding='utf-8'))
assert v['classification_counts']=={'符合':0,'需要重建':6,'局部修正':52}
assert (W/'REPORT.md').is_file() and len(json.loads((W/'results.json').read_text(encoding='utf-8')))==58
status='''## WI-031 最終完成：58課Markdown標準審查（2026-09-11）

- 狀態：審查與學習落盤完成，取代本檔下方WI-031執行中checkpoint。全課符合0、局部修正52、主線重建6：ChArUco、ECC、SIFT、LightGlue、DINO detector、YOLO-World。
- 完成範圍：58課桌機／手機主線、每課4工程圖、五課40深讀章節。52課主線可保留，工程／指定深讀／手機需局部修正；不等於58課全部重建，也不沿用舊首讀分數判整課通過。
- 產物：teaching-images/vision-ai-model-selection/workitems/wi-031/REPORT.md（58課總表、保留／修正範圍、優先序與證據）、results.json、observations.md、final-verification.json；細項入口PLAN.md。
- 實際驗證：116頁狀態、376放大、116自測、116導覽完成；80深讀章節尺寸狀態／148視圖；644資產course/docs與基準hash一致、HTML未變；66共享主圖hash核對。188手機圖說0字形重疊，13過早白圖重查正常。305報告連結與424逐課證據路徑通過。
- 學習：根IMAGE_STYLE_GUIDE.md、TEACHING_WEBPAGE_GUIDE.md、TEACHING_REVIEW_LOG.md已回寫，v1.0配分不變。人工缺口分類，沒有替644圖逐張編造完整分數；本輪未重跑模型、未做真人學習測試。
- 授權／下一步：本輪審查工作無未完成項與阻礙。教材未修改，未commit/push/發布；使用者成品核准不由審查推定。後續收到重製指示時從REPORT的6課P1與局部語意錯圖另開工作項，不自動啟動生成。

'''
for p in [R/'WORKITEMS.md',C/'BEGINNER_VISUAL_TODO.md',C/'BEGINNER_VISUAL_STATUS.md']:
    old=p.read_text(encoding='utf-8')
    if not old.startswith('## WI-031 最終完成：'):p.write_text(status+old,encoding='utf-8')
p=W/'PLAN.md'
s=p.read_text(encoding='utf-8').replace('- [ ] 核對58課總數、共享圖證據與首讀／進階範圍，完成總表、优先級及共用學習。','- [x] 核對58課總數、共享圖證據與首讀／進階範圍，完成總表、优先級及共用學習。')
if '## 最終驗收' not in s:
    s+='\n## 最終驗收\n\n'+status
p.write_text(s,encoding='utf-8')
S=C/'teaching-maintenance'; p=S/'manifest.json'; m=json.loads(p.read_text(encoding='utf-8'))
synced=[]
for row in m['files']:
    if row['snapshot'].startswith('project/'):
        src=Path(row['source']); dest=S/row['snapshot']
        shutil.copyfile(src,dest)
        row['sha256']=hashlib.sha256(src.read_bytes()).hexdigest()
        assert hashlib.sha256(dest.read_bytes()).hexdigest()==row['sha256']
        synced.append(row['snapshot'])
m['latest_local_audit']='WI-031; audit evidence remains at workitems/wi-031 in authoring workspace; not published'
p.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
p=S/'README.md'; old=p.read_text(encoding='utf-8')
note='''## Local audit: WI-031 (2026-09-11)

All 58 topics were re-audited, including engineering figures and five sets of eight advanced chapters: 0 fully compliant, 52 targeted revisions, 6 main-story rebuilds. This is a diagnostic audit, not a new production release or per-asset numeric scoring.

The [full audit report](../workitems/wi-031/REPORT.md), 58-row results, screenshots and verification remain in the local authoring workspace. They are not included in this preservation snapshot or the published site; the relative report link requires that workspace. Current reusable learning is synchronized in `project/`. WI-030 below remains the latest production snapshot.

'''
if '## Local audit: WI-031' not in old:
    p.write_text(old.replace('## Latest: WI-030',note+'## Latest production: WI-030',1),encoding='utf-8')
(W/'documentation-verification.json').write_text(json.dumps({'durable_status_files':3,'checklist_complete':'- [ ]' not in s,'synchronized_authority_snapshots':synced,'production_changed':False,'commit_push':False},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Completed WI-031; synchronized',len(synced),'authority snapshots')

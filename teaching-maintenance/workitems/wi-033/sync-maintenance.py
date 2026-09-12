from pathlib import Path
import json,hashlib,shutil
W=Path(__file__).resolve().parent;C=W.parents[1];R=C.parents[1];S=C/'teaching-maintenance'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
mp=S/'manifest.json';m=json.loads(mp.read_text(encoding='utf8'));m['workitem']='WI-033';new={}
for src in W.iterdir():
 if src.is_file() and src.suffix in {'.md','.json','.py','.svg','.tsv'}:new['workitems/wi-033/'+src.name]=src
for src in (W/'pages').rglob('*'):
 if src.is_file() and src.suffix in {'.json','.txt'}:new['workitems/wi-033/'+src.relative_to(W).as_posix()]=src
for src in (W/'baseline').rglob('*'):
 if src.is_file() and src.suffix in {'.md','.json','.html'}:new['workitems/wi-033/'+src.relative_to(W).as_posix()]=src
for name,src in [('WORKITEMS.md',R/'WORKITEMS.md'),('BEGINNER_VISUAL_TODO.md',C/'BEGINNER_VISUAL_TODO.md'),('BEGINNER_VISUAL_STATUS.md',C/'BEGINNER_VISUAL_STATUS.md')]:new['workitems/wi-033/'+name]=src
for name in ['CLAUDE.md','IMAGE_STYLE_GUIDE.md','TEACHING_REVIEW_LOG.md','TEACHING_SCORING_RUBRIC.md','TEACHING_WEBPAGE_GUIDE.md','Overall_Review.md']:new['project/'+name]=R/name
for r in json.loads((W/'inventory.json').read_text(encoding='utf8')):
 for rel in [f"_course_content/topics/{r['id']}.json",r['manifest_path']]:new['workitems/wi-033/authoring/'+rel]=C/rel
 src=(C/r['manifest_path']).parent/'model.md';new['workitems/wi-033/authoring/'+src.relative_to(C).as_posix()]=src
for rel in ['_course_content/learner-briefs.json','tools/build_interactive_learning_html.py','tools/build_github_pages_site.py','tools/validate_teaching_preflight.py','tests/test_engineering_mobile_pages.py','tests/test_tall_mobile_artwork.py','tests/test_collapsed_deep_dive.py','tests/test_github_pages_bundle.py','tests/test_deep_dive_mobile_steps.py','tests/test_interactive_navigation.py','tests/test_resnet_deep_dive.py','tests/test_segformer_deep_dive.py','tests/test_concept_zoom_edges.py']:new['workitems/wi-033/authoring/'+rel]=C/rel
skill=Path('C:/Users/hctsa/.codex/skills/teaching-review-cycle')
for src in skill.rglob('*.md'):new['skills/teaching-review-cycle/'+src.relative_to(skill).as_posix()]=src
known={r['snapshot']:r for r in m['files']}
def copy(rel,src):
 dest=S/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dest);digest=sha(src);assert sha(dest)==digest
 if rel not in known:known[rel]=dict(snapshot=rel);m['files'].append(known[rel])
 known[rel].update(source=str(src),sha256=digest)
for rel,src in new.items():copy(rel,src)
for r in m['files']:assert sha(S/r['snapshot'])==r['sha256'],r['snapshot']
reportrel='workitems/wi-033/maintenance-verification.json';newcount=len(new)+(reportrel not in new)
report=dict(status='passed',current_copied_files=newcount,total_manifest_files=len(m['files'])+(reportrel not in known),source_equals_snapshot=True,user_approval='pending',published=False,scope='Shared authorities, installed teaching skill Markdown, WI-033 plans/reviews/native SVG/scripts, page JSON/text evidence, baseline source, 52 topic/model/manifest sources and current builders/tests. Full PNG screenshots and rejected raster drafts remain in local workitem; active PNGs are in docs.')
rp=W/'maintenance-verification.json';rp.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8');copy(reportrel,rp)
for r in m['files']:assert sha(S/r['snapshot'])==r['sha256'],r['snapshot']
mp.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
p=S/'README.md';s=p.read_text(encoding='utf8');note='''## WI-033 第二部分52課本機完成（2026-09-12）

[報告](workitems/wi-033/REPORT.md)、[逐圖資產](workitems/wi-033/final-selected-assets.json)、[全52課驗證](workitems/wi-033/verification-all52.json)及[維護核對](workitems/wi-033/maintenance-verification.json)保存第二部分成果。52課208組工程故事、指定主線／深讀修正，共460張新啟用PNG；使用者核准pending，尚未commit/push或發布。

維護副本保存原生SVG、版本preflight、審查/失敗/驗證紀錄、生成與整合程式、頁面JSON/文字、基準來源及52課authoring。啟用PNG位於docs，完整頁面截圖和歷史PNG仍在本機workitems/wi-033；不是整個工作區備份。從PLAN核對現行引用後接續，不直接重跑舊生成器。根Markdown與已安裝skill仍為編輯權威。

'''
if note.splitlines()[0] not in s:p.write_text(note+s,encoding='utf8')
print('Saved',newcount,'current snapshots; verified',len(m['files']),'manifest hashes')

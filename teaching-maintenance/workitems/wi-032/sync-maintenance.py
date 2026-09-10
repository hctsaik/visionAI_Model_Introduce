import json,hashlib,shutil,re
from pathlib import Path
W=Path(__file__).resolve().parent;C=W.parents[1];R=C.parents[1];S=C/'teaching-maintenance'
p=S/'manifest.json';m=json.loads(p.read_text(encoding='utf-8'));m['workitem']='WI-032';new={}
for src in (W.parent/'wi-031').iterdir():
 if src.is_file() and src.suffix in {'.md','.json','.py','.tsv'}:
  new['workitems/wi-031/'+src.name]=src
for src in list(W.glob('*.md'))+list(W.glob('*.json'))+list(W.glob('*.py')):
 new['workitems/wi-032/'+src.name]=src
for src in (W/'pages').glob('*/report.json'):new['workitems/wi-032/'+src.relative_to(W).as_posix()]=src
for src in (W/'baseline').rglob('*'):
 if src.is_file():new['workitems/wi-032/'+src.relative_to(W).as_posix()]=src
for name,src in [('WORKITEMS.md',R/'WORKITEMS.md'),('BEGINNER_VISUAL_TODO.md',C/'BEGINNER_VISUAL_TODO.md'),('BEGINNER_VISUAL_STATUS.md',C/'BEGINNER_VISUAL_STATUS.md')]:new['workitems/wi-032/'+name]=src
for name in ['CLAUDE.md','IMAGE_STYLE_GUIDE.md','TEACHING_REVIEW_LOG.md','TEACHING_SCORING_RUBRIC.md','TEACHING_WEBPAGE_GUIDE.md','Overall_Review.md']:new['project/'+name]=R/name
for slug in json.loads((W/'lesson-content.json').read_text(encoding='utf-8')):
 src=C/'_course_content/topics'/f'{slug}.json';new['workitems/wi-032/authoring/'+src.relative_to(C).as_posix()]=src
 t=json.loads(src.read_text(encoding='utf-8'));src=C/t['review_trace']['authority']
 for file in [src,src.parent/'slide-manifest.md']:new['workitems/wi-032/authoring/'+file.relative_to(C).as_posix()]=file
for rel in ['_course_content/learner-briefs.json','tools/build_interactive_learning_html.py','tools/build_github_pages_site.py','tests/test_engineering_mobile_pages.py','tests/test_tall_mobile_artwork.py','tests/test_collapsed_deep_dive.py','tests/test_github_pages_bundle.py','tests/test_deep_dive_mobile_steps.py','tests/test_interactive_navigation.py']:new['workitems/wi-032/authoring/'+rel]=C/rel
for row in json.loads((W/'engineering-active-assets.json').read_text(encoding='utf-8')):
 version=re.search(r'-(r\d+)-',row['image'])[1];src=W/f"{row['id']}-{version}-{row['mode']}.svg";new['workitems/wi-032/native/'+src.name]=src
for row in json.loads((W/'selected-assets.json').read_text(encoding='utf-8')).values():
 for mode in ['desktop','mobile']:
  src=(W/row[mode]).with_suffix('.svg')
  if src.exists():new['workitems/wi-032/native/'+src.name]=src
known={r['snapshot']:r for r in m['files']}
for rel,src in new.items():
 dest=S/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dest)
 row=known.get(rel)
 if row is None:row={'snapshot':rel,'source':str(src)};m['files'].append(row)
 row['source']=str(src);row['sha256']=hashlib.sha256(dest.read_bytes()).hexdigest()
for row in m['files']:assert hashlib.sha256((S/row['snapshot']).read_bytes()).hexdigest()==row['sha256'],row['snapshot']
p.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
p=S/'README.md';s=p.read_text(encoding='utf-8')
note='''## WI-032：Overall Review第一部分（本機完成、未發布）

[總計畫](project/Overall_Review.md)將58課分成6課重建與52課局部修正；前6課已完成主線、工程層、手機圖、自測與交付。[報告](workitems/wi-032/REPORT.md)、[學習](project/TEACHING_REVIEW_LOG.md)、[驗證](workitems/wi-032/final-verification.json)與全部brief已保存。使用者核准pending。

authoring保存六課來源與builder／測試；native保存64個選定SVG，baseline保存22份改前來源。啟用PNG在docs對應路徑；原型、截圖與失敗稿的完整本機紀錄在專案workitems/wi-032。快照內報告的本機相對截圖／頁面連結需回到原工作項目查看；本資料夾不宣稱包含所有歷史圖片。不要重跑製作脚本覆蓋最終版本，先從PLAN及啟用manifest核對接續狀態。

'''
if '## WI-032：Overall Review第一部分' not in s:s=note+s
p.write_text(s,encoding='utf-8')
print('Saved',len(new),'WI-032/current authority snapshots; verified',len(m['files']),'manifest hashes')

from pathlib import Path
import json,re,shutil,hashlib
W=Path(__file__).resolve().parent;C=W.parents[1]
# Keep source snapshots before changing the builder or formal manifests.
files=[C/'tools/build_interactive_learning_html.py']
data=json.loads((W/'lesson-content.json').read_text(encoding='utf-8'))
for slug in data:
 t=json.loads((C/'_course_content/topics'/f'{slug}.json').read_text(encoding='utf-8'));files.append((C/t['review_trace']['authority']).parent/'slide-manifest.md')
for p in files:
 target=W/'baseline'/p.relative_to(C);target.parent.mkdir(parents=True,exist_ok=True)
 if not target.exists():shutil.copy2(p,target)
groups={
 'geometry-compare':[
  {'model':'ChArUco','normality':'已知尺寸標靶、多位置與傾角觀測','candidate':'內參／畸變；姿態與工站關係另求'},
  {'model':'SIFT＋matcher','normality':'局部紋理清楚；尺度方向描述與比對','candidate':'影像點對；幾何估計與驗證另接'},
  {'model':'LightGlue＋extractor','normality':'相容預訓練權重、點與描述；上下文配對','candidate':'點對與信心；納入完整計算成本'},
  {'model':'ECC','normality':'合理起點、外觀穩定；密集相關迭代','candidate':'warp與相關值；獨立殘差另驗'}],
 'detector-compare':[
  {'model':'DINO detector','normality':'固定類別框標註與監督訓練／微調','candidate':'框／類別／分數；換類別涉及資料與模型'},
  {'model':'YOLO-World','normality':'預訓練視覺語言模型與文字詞彙','candidate':'詞彙對應候選框；更新表示及現場驗證'},
  {'model':'比較方式','normality':'同批影像、同硬體、獨立逐件真值','candidate':'漏檢、錯類、完整耗時與維護／覆核成本'}]}
s=(W.parent/'wi-030/integrate.py').read_text(encoding='utf-8').replace('wi030','wi032').replace('WI030','WI032').replace('wi-030','wi-032').replace('WI-030','WI-032')
s=re.sub(r'groups=\{.*?\}\nfor slug',lambda _: 'groups='+repr(groups)+'\nfor slug',s,flags=re.S)
s=s.replace("selected=json.loads", "plans['ecc-core']={'id':'ecc-core','owner':'ecc','title':'ECC：依外觀微調幾何對齊','nodes':['模板與合理起點','重採樣、相關與更新','warp與獨立核對'],'source':'https://docs.opencv.org/4.13.0/dc/d6b/group__video__track.html'}\nselected=json.loads")
s=s.replace('AI生成教學示意，非模型實測。','教學示意，非模型實測。')
s=s.replace("'generation':'built-in imagegen'","'generation':'native SVG rendered by browser' if src.with_suffix('.svg').exists() else 'built-in imagegen'")
s=s.replace("'十二課首讀圖文與手機PNG、反例、比較及自測；原工程slide保留，未以首讀評分代替工程圖審查。'","'六課首讀／工程圖文與手機PNG、反例、比較及自測；驗證與使用者核准另記。'")
s=s.replace("'WI-032 十二課首讀圖文與手機PNG、反例、比較及自測；原工程slide保留，未以首讀評分代替工程圖審查。'","'WI-032 六課首讀及工程層重建；頁內驗證與使用者核准另記。'")
s=s.replace("core_record['desktop'].replace('.png','.md')","core_record['brief']")
s=s.replace("core_record['mobile'].replace('.png','.md')","core_record['brief']")
# These plans deliberately use three panels; don't accidentally nest their callouts.
s=s.replace("cs=[a['ideas']+[['交付與接手',a['output']]],[['看哪裡'", "cs=[a['ideas']+[['交付與接手',a['output']]],[['看哪裡'")
(W/'integrate-main.py').write_text(s,encoding='utf-8')
sel=json.loads((W/'selected-assets.json').read_text(encoding='utf-8'))
for id,r in sel.items():
 r['brief']=f'{id}-native-r05.md' if 'native' in r['desktop'] else 'charuco-core-r05.md' if id=='charuco-core' else f'{id}-r01.md'
 assert (W/r['brief']).exists(),r
(W/'selected-assets.json').write_text(json.dumps(sel,ensure_ascii=False,indent=2),encoding='utf-8')
print('Prepared main integration and backed up 6 manifests + builder; no lesson integrated yet')

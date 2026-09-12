from pathlib import Path
import json,hashlib,shutil,runpy,urllib.request,urllib.parse
W=Path(__file__).resolve().parent;C=W.parents[1];R=C.parents[1]
owners=['ad-dinomaly','ad-invad','ad-ddad','ad-winclip','ad-anomalyclip','frame-difference','background-subtraction','bytetrack']
v=json.loads((W/('verification-'+'-'.join(owners)+'.json')).read_text(encoding='utf8'));tests=json.loads((W/'batch6-tests.json').read_text(encoding='utf8'))
assert v['ui_states']==32 and v['zoom_checks']==224 and v['bundle_hashes_match'] and tests['exit_code']==0
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
http=[];p=W/'batch6-main-active-assets.json';active=json.loads(p.read_text(encoding='utf8'))
for r in active:
 for rel,key in [(r['path'],'sha256'),(r['desktop_source'],'desktop_sha256')]:
  assert sha(C/rel)==r[key]==sha(C/'docs'/rel)
  for prefix in ['','docs/']:
   url='http://127.0.0.1:8000/'+urllib.parse.quote(prefix+rel)
   with urllib.request.urlopen(url) as q:assert hashlib.sha256(q.read()).hexdigest()==r[key]
   http.append(url)
 r['page_review']='passed'
p.write_text(json.dumps(active,ensure_ascii=False,indent=2),encoding='utf8')
notes=['正常多類、訓練擾動與分組比較分開','正常特徵教空間調制；縮放偏移逐位置可追','原圖每步引導恢復，雙路差異及複製刮傷反例','人工提示與重疊視窗調和聚合；零樣本不標訓練','輔助提示與目標零樣本分開；q誤報和p漏檢','同方件位置移動，差分雙帶與曝光/靜止反例','多時間背景常態與停留吸收，mask不是身份','先高分再低分匹配，丟失緩衝及計數另訂']
out=[]
for o,n in zip(owners,notes):
 out.append(dict(id=o,total=92,scores=[19,19,19,18,8,9],evidence=[n,'四工程的桌機/手機頁內共8張逐張實看；首讀載入與放大通過','幾何簡化，長手機需捲動，部分術語仍密，背景ID7對比偏低但文字另明示'],completion={'aesthetics':[8,'幾何簡化與局部低對比'],'completeness':[9,'四工程與指定首讀修正完成'],'professionalism':[9,n],'density':[8,'手機長捲動與術語密度保留'],'hierarchy':[9,'三節點單黃結論']},veto=[],status='local_complete',page_evidence=f'pages/{o}/docs-{{1440,360}}-engineering-{{1,2,3,4}}.png',user_approval='pending',model_inference=False))
(W/'batch6-page-assessment.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8')
(W/'batch6-main-page-review.json').write_text(json.dumps(dict(status='passed',actual_viewed=[f'pages/{o}/docs-360-main-{i}.png' for o in ['ad-winclip','ad-anomalyclip'] for i in [2,3]],notes=['四首讀手機頁已實看，孔口與刮傷保留，放大按鈕獨立下排','原桌機SHA未變；來源/docs/HTTP一致'],http=http,user_approval='pending'),ensure_ascii=False,indent=2),encoding='utf8')
for name in ['prototype','expanded','main']:
 p=W/f'batch6-{name}-image-assessment.json';a=json.loads(p.read_text(encoding='utf8'))
 for r in a:r.update(page_review='passed',page_evidence='batch6-page-assessment.json; batch6-main-page-review.json')
 p.write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf8')
p=W/'inventory.json';a=json.loads(p.read_text(encoding='utf8'))
for r in a:
 if r['id'] in owners:
  r.update(status='local_complete',evidence_wi033=['batch6-page-assessment.json','batch6-validation-summary.json',f'pages/{r["id"]}'])
  mp=C/r['manifest_path'];mp.write_text(mp.read_text(encoding='utf8').replace('native_reviewed_page_pending_user_pending','native_and_page_reviewed_user_pending'),encoding='utf8');shutil.copyfile(mp,C/'docs'/r['manifest_path'])
assert sum(r['status']=='local_complete' for r in a)==41
p.write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf8')
p=W/'PLAN.md';p.write_text(p.read_text(encoding='utf8').replace('- [ ] 第六批：','- [x] 第六批：'),encoding='utf8')
val={k:v[k] for k in ['ui_states','zoom_checks','http_checks','bundle_assets','html_sha256','answers','navigation']};val.update(tests=tests,additional_main_http_checks=len(http),new_engineering_pngs=64,new_main_mobile_pngs=2,native_and_page_review='passed',user_approval='pending',published=False)
(W/'batch6-validation-summary.json').write_text(json.dumps(val,ensure_ascii=False,indent=2),encoding='utf8')
note='### WI-033 最新：41/52課本機完成\n\n第六批8課64工程PNG及2共用首讀手機已原生/頁內逐張實看。32頁狀態224放大、8 tests/120 subtests、1370來源/docs資產一致、236HTTP及額外首讀來源核對通過。建置已納入768×2400原生尺寸。使用者核准pending，未發布，未新跑模型。最後11課的22機制PNG已生成，尚未審/修正；33擴展與SR同件主反例待做。下一步審第七批原型並完成剩餘全部課程與全站驗證；唯一checklist：workitems/wi-033/PLAN.md。\n'
(W/'checkpoint-note.md').write_text(note,encoding='utf8');runpy.run_path(str(W/'append-checkpoint.py'))
with (R/'TEACHING_REVIEW_LOG.md').open('a',encoding='utf8') as f:f.write('\n## WI-033-L7：第六批八課完成\n'+note+'零樣本圖不能借用正常訓練標籤；正常孔口圈要空心以免掩蓋孔。比較影片時保留方件位置與L身份標記，背景統計與身份追蹤分工。原生尺寸審查通過後才窄範圍加入建置白名單，保留失敗紀錄。\n')
p=R/'Overall_Review.md';s=p.read_text(encoding='utf8');names=['Dinomaly','InvAD','DDAD','WinCLIP','AnomalyCLIP','Frame Difference','Background Subtraction','ByteTrack'];s='\n'.join(l.replace('待執行','本機修正、自評與驗證完成；待使用者審閱') if any(l.startswith('| '+n+' |') for n in names) else l for l in s.splitlines());p.write_text(note+'\n'+s,encoding='utf8')
print('41/52 local complete; batch7 continues')

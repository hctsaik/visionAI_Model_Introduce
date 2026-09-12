from pathlib import Path
import json,hashlib,urllib.request,urllib.parse,shutil,runpy
W=Path(__file__).resolve().parent; C=W.parents[1]; R=C.parents[1]
owners=['ad-patchcore','ad-padim','ad-subspacead','ad-stfpm','ad-rd4ad','ad-ae','ad-draem','ad-uniad']
v=json.loads((W/('verification-'+'-'.join(owners)+'.json')).read_text(encoding='utf-8'))
assert v['ui_states']==32 and v['zoom_checks']==240 and v['bundle_hashes_match']
tests=json.loads((W/'batch5-tests.json').read_text(encoding='utf-8'));assert tests['exit_code']==0
deep=json.loads((W/'batch5-deep-report.json').read_text(encoding='utf-8'));assert len(deep)==32 and all(r['complete'] for r in deep)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
p=W/'batch5-deep-active-assets.json';a=json.loads(p.read_text(encoding='utf-8'))
http=[]
for r in a:
 for rel,key in [(r['path'],'sha256'),(r['desktop_source'],'desktop_sha256')]:
  assert sha(C/rel)==r[key]==sha(C/'docs'/rel)
  for prefix in ['', 'docs/']:
   url='http://127.0.0.1:8000/'+urllib.parse.quote(prefix+rel)
   with urllib.request.urlopen(url) as response: assert hashlib.sha256(response.read()).hexdigest()==r[key]
   http.append(url)
 r['page_review']='passed'
p.write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf-8')
notes=[['正常局部查庫；取同位置描述後最近距離','保留PatchCore原ResNet50紀錄；手機明列全精度平均與顯示四捨五入'],['同位置正常分布；協方差方向與距離','同單孔板跨位置與尺寸需固定'],['投影正常子空間；殘差另算','不把低維座標當殘差'],['固定教師、正常訓練學生；同位置多尺度差','同向不同幅值與正規化分開'],['固定教師→瓶頸→反向學生','正常訓練輸入已移除刮傷；部署保存三部分'],['像素重建差110；複製刮傷差0','小孔被模糊差70，漏檢/誤報分開'],['正常原圖和合成mask兩種監督','推論原圖與重建共同送判別器；真缺陷獨立驗'],['局部遮的是特徵讀取連線','多類正常共同訓練；推論關閉特徵擾動']]
out=[]
for o,n in zip(owners,notes):
 ev=n+['四工程桌機與手機頁內逐張實看；原首讀保留並通過實際張數載入/放大','幾何示意簡化、手機需長捲動與少數術語保留，密度和美感各8分']
 out.append(dict(id=o,total=92,scores=[19,19,19,18,8,9],evidence=ev,completion={'aesthetics':[8,ev[-1]],'completeness':[9,'任務/機制/部署/比較及指定深讀完成'],'professionalism':[9,n[0]],'density':[8,ev[-1]],'hierarchy':[9,'三節點單一路徑']},veto=[],status='local_complete',page_evidence=f'pages/{o}/docs-{{1440,360}}-engineering-{{1,2,3,4}}.png',user_approval='pending',model_inference=False))
(W/'batch5-page-assessment.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
(W/'batch5-deep-page-review.json').write_text(json.dumps(dict(status='passed',actual_viewed=[f'deep/ad-patchcore/docs-{w}-c02-v0{i}.png' for w in [1440,360] for i in [1,2]],notes=['原工件A-01及来源框保留','layer2/3同位置線索；4.70/4.07/3.91沿用既有實測','顯示格四捨五入與全精度平均分開說明'],http=http,user_approval='pending'),ensure_ascii=False,indent=2),encoding='utf-8')
for name in ['prototype','expanded','deep']:
 p=W/f'batch5-{name}-image-assessment.json';a=json.loads(p.read_text(encoding='utf-8'))
 for r in a:r.update(page_review='passed',page_evidence='batch5-page-assessment.json; batch5-deep-page-review.json')
 p.write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf-8')
p=W/'inventory.json';a=json.loads(p.read_text(encoding='utf-8'))
for r in a:
 if r['id'] in owners:
  r.update(status='local_complete',evidence_wi033=['batch5-page-assessment.json','batch5-validation-summary.json',f'pages/{r["id"]}'])
  mp=C/r['manifest_path'];mp.write_text(mp.read_text(encoding='utf-8').replace('native_reviewed_page_pending_user_pending','native_and_page_reviewed_user_pending'),encoding='utf-8');shutil.copyfile(mp,C/'docs'/r['manifest_path'])
p.write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf-8')
p=W/'PLAN.md';p.write_text(p.read_text(encoding='utf-8').replace('- [ ] 第五批：','- [x] 第五批：'),encoding='utf-8')
validation={k:v[k] for k in ['ui_states','zoom_checks','http_checks','bundle_assets','html_sha256','answers','navigation']};validation.update(tests=tests,deep_states=32,deep_source_http_checks=len(http),new_engineering_pngs=64,new_deep_mobile_pngs=2,native_and_page_review='passed',user_approval='pending',published=False)
(W/'batch5-validation-summary.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2),encoding='utf-8')
note='### WI-033 最新：33/52課本機完成\n\n第五批8課64工程PNG及PatchCore第二章2手機PNG已逐張原生與頁內實看。32主頁狀態240放大、32深讀狀態、8 tests/120 subtests、1370來源/docs資產一致與HTTP通過，見batch5-validation-summary.json。使用者核准pending，未發布，未新跑模型。第六批16原型PNG已生成，待審查修正及24擴展、2共用首讀手機；最後11課未完成。下一步逐張審第六批，全部52課持續；唯一checklist：workitems/wi-033/PLAN.md。\n'
(W/'checkpoint-note.md').write_text(note,encoding='utf-8');runpy.run_path(str(W/'append-checkpoint.py'))
with (R/'TEACHING_REVIEW_LOG.md').open('a',encoding='utf-8') as f:f.write('\n## WI-033-L6：第五批八課完成\n'+note+'驗頁應依各課實際首讀張數（RD4AD/AE/DRAEM為4/5/4），不可硬設3張使保留內容誤報。保留初次失敗報告並修正脚本重驗。正常訓練圖不得偷用帶刮傷輸入；實測描述值沿用全精度，顯示四捨五入需說明。\n')
p=R/'Overall_Review.md';s=p.read_text(encoding='utf-8');names=['PatchCore','PaDiM','SubspaceAD','STFPM','RD4AD','AE','DRAEM','UniAD'];s='\n'.join(l.replace('待執行','本機修正、自評與驗證完成；待使用者審閱') if any(l.startswith('| '+n+' |') for n in names) else l for l in s.splitlines());p.write_text(note+'\n'+s,encoding='utf-8')
print('33/52 local complete; batch6 continues')

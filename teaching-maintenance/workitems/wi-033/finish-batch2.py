from pathlib import Path
import json,hashlib,shutil
W=Path(__file__).resolve().parent;C=W.parents[1];R=C.parents[1]
v=json.loads((W/'verification-lucas-kanade-raft-ad-anomalydino-ad-efficientad.json').read_text(encoding='utf-8'))
d=json.loads((W/'batch2-deep-report.json').read_text(encoding='utf-8'));caps=json.loads((W/'caption-verification.json').read_text(encoding='utf-8'))
assert v['ui_states']==16 and len(d)==64 and all(r['complete'] for r in d) and len(caps['topics'])==58
notes={
'lucas-kanade':['同L形工件、清楚/反光兩組共同輸入，輸出p到p′','局部梯度算例u=2/v=1可追算，單邊與無紋理限制可見','保存坐標、status、時間與相機校正後接物理量','與RAFT同資料比較選點及覆蓋，不將稠密當更可信','四工程桌機手機讀圖可追；手機需要長捲動','鏡面件情境允許改善照明、加標記與整體對位'],
'raft':['同影格對建立稠密位移，反光區仍可能輸出數值','全配對/情境/隱狀態共同更新，(1,0)+(1,1)=(2,1)','輸出向量不是追蹤ID；遮擋一致性是外部核對','比較更新次數和LK需求，沒有捏造模型勝負','四工程三段可讀；少數英文次字與長捲動扣分','只需三點的CPU情境允許LK基準'],
'ad-anomalydino':['同四孔A-01刮痕位置連續，旋轉含刻字共同變換','整圖DINOv2出tokens，局部查全庫最近距離','庫來源與前處理需相容；位置圖與整圖分數分開','污染參考可降距離，旋轉是否正常依工作規格','新旋轉/工程手機可讀；舊有效深讀沿用WI-031審查，未虛增逐圖分數','少正常樣本情境先補覆蓋，特徵不足再評其他方案'],
'ad-efficientad':['首讀同托盤缺件與污點，深讀另有明示A-01算例','T/S1與AE/S2比較，正常分位數校正後融合','兩路、融合與原圖一同核對；位置熱圖不是輪廓','換產品重訓/校正對比查庫與監督分割成本','七章手机重排和保留第六章逐段實看；長元素截圖合成錯誤已另取細節','兩路與獨立裝配規則並列可接受取捨']}
out=[]
for o,ev in notes.items():
 out.append(dict(id=o,scores=[19,19,19,18,8,9],total=92,evidence=ev,completion={'aesthetics':[8,'精確圖解與保留主線質感略異'],'completeness':[9,'已列工程/主反例/指定深讀修正完整'],'professionalism':[9,ev[1]],'density':[8,ev[4]],'hierarchy':[9,'首讀、四工程、深讀分工']},veto=[],status='local_complete',user_approval='pending',page_evidence=f'pages/{o}',deep_evidence='batch2-deep-report.json; deep-detail-report.json',model_inference=False))
(W/'batch2-page-assessment.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
for name in ['batch2-image-assessment.json','active-assets-lucas-kanade-raft-ad-anomalydino-ad-efficientad.json','batch2-extra-active-assets.json']:
 p=W/name;a=json.loads(p.read_text(encoding='utf-8'))
 for r in a:r.update(page_review='passed',page_evidence='batch2-page-assessment.json; pages; deep; deep-detail-report.json')
 p.write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf-8')
p=W/'inventory.json';a=json.loads(p.read_text(encoding='utf-8'))
for r in a:
 if r['id'] in notes:
  r.update(status='local_complete',evidence_wi033=['batch2-page-assessment.json','batch2-deep-report.json','deep-detail-report.json',f'pages/{r["id"]}'])
  mp=C/r['manifest_path'];mp.write_text(mp.read_text(encoding='utf-8').replace('native_reviewed_page_pending_user_pending','native_and_page_reviewed_user_pending'),encoding='utf-8');shutil.copyfile(mp,C/'docs'/r['manifest_path'])
p.write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf-8')
p=W/'PLAN.md';s=p.read_text(encoding='utf-8').replace('- [ ] 第二批：','- [x] 第二批：');p.write_text(s,encoding='utf-8')
validation=dict(tests='11 passed, 126 subtests passed in 112.67s',command='python -m pytest tests/test_engineering_mobile_pages.py tests/test_deep_dive_mobile_steps.py tests/test_github_pages_bundle.py tests/test_interactive_navigation.py -q',main_states=16,zooms=112,http=116,assets=1364,deep_states=64,mobile_caption_topics=58,mobile_captions=178,html_sha256=v['html_sha256'],user_approval='pending',published=False)
(W/'batch2-validation-summary.json').write_text(json.dumps(validation,indent=2),encoding='utf-8')
with (R/'TEACHING_REVIEW_LOG.md').open('a',encoding='utf-8') as f:f.write('''
## WI-033-L3：第二批四課收尾與第三批原型學習
第二部分10/52課本機完成。第二批48張新PNG原生及頁內審查、四課主頁/指定深讀、11 tests/126 subtests完成；細項與扣分見workitems/wi-033/batch2-page-assessment.json、batch2-validation-summary.json。使用者成品核准pending，未模型實測或真人理解測試，未發布。
既有指南的證據分層再次成立：圖片decode須等lazy/picture真正選圖載入；長SVG裁切元素截圖曾出現空白/放大紋理，逐步捲到同位置後正常，沒有因此重畫正確來源。逐段截圖見deep-detail-report.json；全站58課178手機圖說間距通過。標題另行/按鈕下排的CSS補修已回歸。
第三批原型在擴展前發現：YOLO係數圖不能把支架結果换成無關矩形；關鍵點算例必須與圖上ROI和A座標完全一致；細格底部不能接觸圖說。修正版本與實看紀錄見prototype-review.md。這些沿用身份/圖文一致原則，不改量表門檻。
''')
note='''### WI-033 最新：10/52課本機完成（2026-09-12）

第一、二批共10課完成修正與必要驗證；第二批48張新PNG、16主頁/112放大/116HTTP/1364資產一致、64深讀章節狀態、58課178手機圖說間距，11 tests/126 subtests通過。長元素截圖錯誤已逐段補證據，第六章來源保留，未當破圖。證據：workitems/wi-033/batch2-validation-summary.json與batch2-page-assessment.json。
第三批7課28故事preflight已寫，七個工程2原型修正中；其餘35課尚未製作。即將完成第三批原型審查並擴展其他工程/指定深讀，所有未完成仍待辦。使用者要求一口氣完成52課；使用者成品核准pending，未commit/push/發布。唯一checklist：workitems/wi-033/PLAN.md。
'''
(W/'checkpoint-note.md').write_text(note,encoding='utf-8')
import runpy;runpy.run_path(str(W/'append-checkpoint.py'))
p=R/'Overall_Review.md';s=p.read_text(encoding='utf-8');names=['Lucas–Kanade','RAFT','AnomalyDINO','EfficientAD'];s='\n'.join(l.replace('待執行','本機修正、自評與驗證完成；待使用者審閱') if any(l.startswith('| '+n+' |') for n in names) else l for l in s.splitlines());p.write_text(note+'\n'+s,encoding='utf-8')
print('10/52 local complete; third batch continues')

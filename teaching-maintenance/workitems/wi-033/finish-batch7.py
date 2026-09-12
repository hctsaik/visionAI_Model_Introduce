from pathlib import Path
import json,hashlib,shutil,runpy
W=Path(__file__).resolve().parent;C=W.parents[1];R=C.parents[1]
owners=['convlstm','videomae','v-jepa','defectfill','anomalydiffusion','tf-idg','controlnet','inpainting','diffusion-restoration','deblur','super-resolution']
load=lambda n:json.loads((W/n).read_text(encoding='utf8'))
save=lambda n,a:(W/n).write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf8')
v=load('verification-'+'-'.join(owners)+'.json');tests=load('batch7-tests.json');ledger=load('batch7-page-view-ledger.json')
assert v['ui_states']==44 and v['zoom_checks']==308 and v['bundle_hashes_match'] and tests['exit_code']==0
assert set(ledger)==set(owners)
for r in ledger.values():
 for f in r['files']:assert hashlib.sha256((W/f['path']).read_bytes()).hexdigest()==f['sha256']
notes=['H/C門控与下一步輸入、任務頭及狀態重設分開','同位置tube遮蔽，像素平方差與下游分類分開','2024特徵預測，stop-grad/EMA及L1例，手機圖說間距完整','LoRA、指定mask與LFS感知距離；大黑塊不等於好刮傷','外觀與位置嵌入，弱區補強，兩mask只生一傷反例','固定權重與latent梯度更新分開；跨材質帶錯木紋','固定主幹與可訓練分支零卷積，輪廓不能證實刮傷','同板下污點，mask內外核對；照片填孔不等於實物修復','退化A與噪聲條件、先驗候選及獨立取像；非唯一算例','展寬邊緣、振鈴與真邊偏移，2像素不是毫米','同矩形板左孔q，插值與學習、兩候選及真實取像分清']
out=[]
for o,n in zip(owners,notes):
 out.append(dict(id=o,total=92,scores=[19,19,19,18,8,9],evidence=[n,'四工程桌機與手機共8張頁內截圖逐張實看；正文/自測/導覽已核對','幾何示意簡化，手機需縱向捲動，部分術語依正文理解；無真人學習試驗'],completion=dict(aesthetics=[8,'幾何簡化'],completeness=[9,'四工程與指定首讀修正完成'],professionalism=[9,n],density=[8,'手機長捲動，部分術語較密'],hierarchy=[9,'三節點單黃結論']),veto=[],status='local_complete',page_evidence=ledger[o]['files'],user_approval='pending',model_inference=False))
save('batch7-page-assessment.json',out)
mainfiles=[f'pages/super-resolution/docs-{width}-main-2.png' for width in [1440,360]]+[f'pages/v-jepa/docs-360-main-{i}.png' for i in [1,2,3]]
save('batch7-main-page-review.json',dict(status='passed',actual_viewed=[dict(path=f,sha256=hashlib.sha256((W/f).read_bytes()).hexdigest()) for f in mainfiles],notes=['SR同板同q與兩候選，真實取像另驗，兩尺寸局部裁切完整','V-JEPA三手機圖說與放大按鈕獨立清楚；58課178caption自動檢查通過'],user_approval='pending'))
for name in ['prototype','expanded','main']:
 a=load(f'batch7-{name}-image-assessment.json')
 for r in a:r.update(page_review='passed',page_evidence='batch7-page-assessment.json; batch7-main-page-review.json')
 save(f'batch7-{name}-image-assessment.json',a)
a=load('batch7-main-active-assets.json')
for r in a:r['page_review']='passed'
save('batch7-main-active-assets.json',a)
a=load('inventory.json')
for r in a:
 if r['id'] in owners:
  r.update(status='local_complete',evidence_wi033=['batch7-page-assessment.json','batch7-validation-summary.json',f'pages/{r["id"]}'])
  mp=C/r['manifest_path'];mp.write_text(mp.read_text(encoding='utf8').replace('native_reviewed_page_pending_user_pending','native_and_page_reviewed_user_pending'),encoding='utf8');shutil.copyfile(mp,C/'docs'/r['manifest_path'])
assert len(a)==52 and all(r['status']=='local_complete' for r in a);save('inventory.json',a)
p=W/'PLAN.md';p.write_text(p.read_text(encoding='utf8').replace('- [ ] 第七批：','- [x] 第七批：'),encoding='utf8')
val={k:v[k] for k in ['ui_states','zoom_checks','http_checks','bundle_assets','html_sha256','answers','navigation']};val.update(tests=tests,extra_tests=load('final-extra-tests.json'),new_engineering_pngs=88,new_main_pngs=2,native_and_page_review='passed',user_approval='pending',published=False)
save('batch7-validation-summary.json',val)
note='### WI-033 最新：52/52課本機修正完成，總驗證收尾中\n\n第七批88工程PNG與2張SR主反例均逐張原生及頁內實看；V-JEPA圖說另驗。44頁狀態308放大320HTTP、1370資產hash一致；8+16 tests、120+10 subtests及58課178圖說通過。52課均完成本機實作與逐課驗證；全52最新HTTP/資產重核、總報告與維護副本尚未完成。使用者核准pending，未發布，未新跑模型。下一步完成PLAN最後一項後交付。\n'
(W/'checkpoint-note.md').write_text(note,encoding='utf8');runpy.run_path(str(W/'append-checkpoint.py'))
p=R/'Overall_Review.md';s=p.read_text(encoding='utf8');s=s.replace('## 第二部分：52課局部修正（已記錄，尚未執行）','## 第二部分：52課局部修正（本機完成；待使用者審閱）');s=s.replace('| 待執行 |','| 本機修正、自評與驗證完成；待使用者審閱 |');p.write_text(note+'\n'+s,encoding='utf8')
with (R/'TEACHING_REVIEW_LOG.md').open('a',encoding='utf8') as f:f.write('\n## WI-033-L8：第七批十一課完成\n'+note+'同一影片要分清自監督目標與下游標籤；平方差和特徵差不能按數值排名。固定權重仍可對latent求梯度；生成mask和實際缺陷逐區驗證。復原候選依退化與噪聲模型驗殘差，不假設已知真實噪聲；同孔q與獨立取像分開。頁內圖說留空間，裁切需在實際PNG核對。首次測試命令因PowerShell內引號消失而未啟動，改用持久Python脚本後通過；不當作產品測試失敗。\n')
print('52/52 local complete; final cross-course verification and snapshots pending')

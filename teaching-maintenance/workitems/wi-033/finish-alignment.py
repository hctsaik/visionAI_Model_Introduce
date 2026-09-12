from pathlib import Path
import json,shutil
W=Path(__file__).resolve().parent;C=W.parents[1];R=C.parents[1]
proof=json.loads((W/'verification-clip-siglip.json').read_text(encoding='utf-8'));assert proof['ui_states']==8 and proof['bundle_hashes_match']
for name in ['alignment-image-assessment.json','siglip-core-assessment.json','alignment-active-assets.json']:
 p=W/name;rows=json.loads(p.read_text(encoding='utf-8'))
 for r in rows:r['page_review']='passed';r['page_evidence']='pages/clip and pages/siglip; native + rendered desktop/mobile individually inspected'
 p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
assess=[]
for owner in ['clip','siglip']:
 reasons=['工件檢索需求与候選身份相符，圖片是示意','雙路編碼與訓練/部署分開，舊串接工程圖已退出','操作卡列模型、候選、未知件與覆核；完整耗時可量','同圖同候選比較，未以損失名稱推論勝負','新手機圖可直接讀；保留主線少量副標仍偏細','遷移題要求補候選/各自門檻及域內驗證']
 assess.append(dict(id=owner,scores=[19,19,19,18,8,9],total=92,evidence=reasons,completion={'aesthetics':[8,'新工程藍標頭與黃結論清楚，既有生成主線有風格差異'],'completeness':[9,'首讀、反例、比較、自測、四工程與交付俱全'],'professionalism':[9,'無編碼器串接或偽定位；分數非實測'],'density':[8,'手機仍需長捲動，原比較已減量'],'hierarchy':[9,'主線與工程層分明，放大只補細節']},veto=[],status='local_complete',user_approval='pending',model_inference=False))
(W/'alignment-page-assessment.json').write_text(json.dumps(assess,ensure_ascii=False,indent=2),encoding='utf-8')
p=W/'inventory.json';rows=json.loads(p.read_text(encoding='utf-8'))
for r in rows:
 if r['id'] in ['clip','siglip']:
  r.update(status='local_complete',evidence_wi033=['alignment-page-assessment.json','verification-clip-siglip.json','pages/'+r['id']],user_approval='pending')
  mp=C/r['manifest_path'];s=mp.read_text(encoding='utf-8').replace('native_reviewed_page_pending_user_pending','native_and_page_reviewed_user_pending');mp.write_text(s,encoding='utf-8');shutil.copyfile(mp,C/'docs'/r['manifest_path'])
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
message='CLIP／SigLIP本機修正、自評與驗證完成，第二部分2/52。18張啟用新PNG逐張原生／頁內實看；8頁狀態、56放大、8自測／導覽、56 HTTP與1351資產hash通過；8 tests／120 subtests通過，SigLIP手機核心補修後四頁狀態另通過。其餘50課未完成。Pose四工程及DINOv3訓練原型已實看，尚待評分整合；DINOv3其餘與DiffusionAD／AnomalyGPT原型即將製作。下一步從PLAN第一批未完成處接續。第一部分已發布；第二部分未commit/push，使用者核准pending。'
for p in [R/'WORKITEMS.md',C/'BEGINNER_VISUAL_TODO.md',C/'BEGINNER_VISUAL_STATUS.md']:
 s=p.read_text(encoding='utf-8');i=s.find('\n## ',3)
 if s.startswith('## WI-033') and i>=0:s=s[i:]
 p.write_text('## WI-033 最新 checkpoint（2026-09-12）\n\n'+message+'細項：teaching-images/vision-ai-model-selection/workitems/wi-033/PLAN.md。\n'+s,encoding='utf-8')
with (W/'PLAN.md').open('a',encoding='utf-8') as f:f.write('\n## CLIP／SigLIP 完成本機修正\n\n- [x] CLIP：四工程與共用手機比較，原生／頁內／來源HTTP驗證。\n- [x] SigLIP：四工程、共用手機比較与手機核心，原生／頁內／來源HTTP驗證。\n\n'+message+'證據：alignment-page-assessment.json、verification-clip-siglip.json；首批其餘四課不可打勾。\n')
p=R/'Overall_Review.md';s=p.read_text(encoding='utf-8')
for name in ['CLIP','SigLIP']:
 lines=s.splitlines();s='\n'.join(line.rsplit('待執行',1)[0]+'本機修正、自評與驗證完成；待使用者審閱 |' if line.startswith('| '+name+' |') and '待執行' in line else line for line in lines)+'\n'
p.write_text('## WI-033 最新進度：2／52（2026-09-12）\n\n'+message+'\n\n'+s,encoding='utf-8')
with (R/'TEACHING_REVIEW_LOG.md').open('a',encoding='utf-8') as f:f.write('''
## WI-033-L1：第二部分前兩課完成與學習（2026-09-12）

- 舊工程圖的箭頭可能推翻正確正文：CLIP/SigLIP原來把兩編碼器串接，改成兩路表示再比較；用不同圖文表示與可追候選順位交代輸出。更名標籤不足以修正。
- 原型座標也要驗證：CLIP方向圖曾使用不同X/Y半徑，修成同半徑；Gram算例需對稱與合理四捨五入。圖形漂亮不等於數學成立。
- 手機驗收要看真正頁面：既有SigLIP核心仍密，補作三段原生SVG，不只修原清單中的比較圖。取樣尺寸採768×2304，不放寬全站尺寸契約。
- 新工程圖保留具體工件與明確工作輸出，不再用泛用PCB熱點表示檢索結果。已有有效主線保留，工程圖另有責任。
- 兩課完成證據在WI-033，18新PNG自評91–93，頁面92；8頁狀態56放大、56 HTTP及1351資產一致。這是內部圖文審查與工具驗證，沒有模型推論、真人學習測試或使用者成品核准。
- 後续50課仍待完成；Pose分支原型修過「只有名詞、沒有點位變化」的問題，接下來依同樣實際輸入／中間變化／交付逐課核對。唯一細項入口為workitems/wi-033/PLAN.md。
''')

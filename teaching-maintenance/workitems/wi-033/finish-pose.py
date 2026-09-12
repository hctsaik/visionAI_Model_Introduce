from pathlib import Path
import json,shutil,runpy
W=Path(__file__).resolve().parent;C=W.parents[1];R=C.parents[1]
v=json.loads((W/'verification-pose.json').read_text(encoding='utf-8'));assert v['ui_states']==4 and v['http_checks']==32
assessment=dict(id='pose',scores=[19,19,19,18,8,9],total=92,evidence=['同名影像点/CAD、遮擋與工站需求清楚','兩種2D方法分支，PnP/Rt/重投影分工成立','K、畸變、單位、外參與失敗狀態可接手','找點可串接姿態，非互斥排名；標記/視角有取捨','桌機手機主線与八新工程PNG均實看，工程次字偏細','遮擋且不能永久標記的遷移題須考慮表面/校正/節拍'],completion={'aesthetics':[8,'新原生工程與既有生成主線風格略不同'],'completeness':[9,'首讀、自測、四工程及操作卡俱全'],'professionalism':[9,'三點僅示意，不宣稱唯一PnP'],'density':[8,'工程手機長捲動，但點身份可辨'],'hierarchy':[9,'主線与展開層分清']},veto=[],status='local_complete',user_approval='pending',model_inference=False)
(W/'pose-page-assessment.json').write_text(json.dumps([assessment],ensure_ascii=False,indent=2),encoding='utf-8')
for name in ['pose-image-assessment.json','active-assets-pose.json']:
 p=W/name;rows=json.loads(p.read_text(encoding='utf-8'))
 for r in rows:r['page_review']='passed';r['page_evidence']='pages/pose; native and desktop/mobile rendered figures inspected'
 p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
p=W/'inventory.json';rows=json.loads(p.read_text(encoding='utf-8'))
for r in rows:
 if r['id']=='pose':
  r.update(status='local_complete',evidence_wi033=['pose-page-assessment.json','verification-pose.json','pages/pose'])
  mp=C/r['manifest_path'];mp.write_text(mp.read_text(encoding='utf-8').replace('native_reviewed_page_pending_user_pending','native_and_page_reviewed_user_pending'),encoding='utf-8');shutil.copyfile(mp,C/'docs'/r['manifest_path'])
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
p=R/'Overall_Review.md';s=p.read_text(encoding='utf-8');lines=s.splitlines();s='\n'.join(line.replace('待執行','本機修正、自評與驗證完成；待使用者審閱') if line.startswith('| Pose Pipeline |') else line for line in lines)+'\n';p.write_text(s,encoding='utf-8')
with (W/'PLAN.md').open('a',encoding='utf-8') as f:f.write('\n- [x] Pose：八工程PNG原生／頁內與完整課程審查；4狀態28放大、32HTTP、1351資產一致。證據pose-page-assessment.json與verification-pose.json。\n')
runpy.run_path(str(W/'checkpoint-state.py'))

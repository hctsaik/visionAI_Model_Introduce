from pathlib import Path
import json,shutil,runpy
W=Path(__file__).resolve().parent;C=W.parents[1];R=C.parents[1]
owners=['det-yolo-dense','det-rtdetr','det-grounding-dino-interface','yoloe','dinov2','llava','qwen-vl','gemini-vision']
v=json.loads((W/('verification-'+'-'.join(owners)+'.json')).read_text(encoding='utf-8'))
assert v['ui_states']==32 and v['zoom_checks']==224 and v['bundle_hashes_match']
tests=json.loads((W/'batch4-tests.json').read_text(encoding='utf-8'));assert tests['failed']==0
notes={
'det-yolo-dense':['同PCB兩電阻，YOLOv8式多位置候選','四候選分數排序/同類IoU去重，框幾何可追','模型座標減補邊除比例，另驗定位偏移與漏框','同PCB與RT-DETR按逐件錯誤/完整成本比較'],
'det-rtdetr':['query集合逐步修框，交付候選框','一對一分工限定訓練，推論分數篩選','少層/多層更新需同資料驗品质','與YOLO共用工件，NMS省去不保證勝出'],
'det-grounding-dino-interface':['resistor一詞對應PCB兩件','詞區域相容數值及雙向交互為示意','固定提示與門檻，分數不是定位誤差','開放詞與固定類別比較不預設勝負'],
'yoloe':['文字/視覺/免提示為不同模式入口','SAVPE加權[1.5,.5]可算，半透明遮罩保留印字','保存ROI與逐件遮罩來源','103/272同類不同規格，外觀不證可互換'],
'dinov2':['同L支架抽特徵，任務頭另接','teacher目標、student預測、EMA與部署分開','查庫同空間距離.283/.141可算','同件背景變化與小缺口反例；近距離不證完整'],
'llava':['同接頭左有右未見，未知原因分開','原版線性投影橋接視覺和文字','保存圖/問題/processor/回答，覆核可見部位','固定ROI分類與可追問VLM按交付比較'],
'qwen-vl':['同銘牌批號B08局部讀取','Qwen2-VL可變token與t/h/w位置','像素預算要連小字/未知率驗證','共同欄位真值比較OCR與VLM，不捏造性能'],
'gemini-vision':['同圓接頭與left/right/cause欄位','只畫公開請求回覆，不猜私有架構','JSON格式與可見內容兩項檢查','固定座位本機分類與API按資料流/錯誤成本比較']}
out=[]
for o in owners:
 ev=notes[o]+['四工程桌機手機頁內逐張實看；幾何简化、長頁與部分專有術語扣分','自測解釋與可接受取捨可展開，兩網址桌機手機均通過']
 out.append(dict(id=o,total=92,scores=[19,19,19,18,8,9],evidence=ev,completion={'aesthetics':[8,'精確示意圖與保留首讀質感略異'],'completeness':[9,'四工程和指定同件反例完成'],'professionalism':[9,ev[1]],'density':[8,ev[4]],'hierarchy':[9,'任務/機制/部署/比較分工']},veto=[],status='local_complete',page_evidence=f'pages/{o}/docs-{{1440,360}}-engineering-{{1,2,3,4}}.png',preserved_main='WI-031 audited sources preserved except two WI-033 same-object failure figures; all main images load/zoom/text verified',user_approval='pending',model_inference=False))
(W/'batch4-page-assessment.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
(W/'batch4-failure-page-review.json').write_text(json.dumps(dict(status='passed',actual_viewed=[f'pages/{o}/docs-{w}-main-2.png' for o in ['dinov2','gemini-vision'] for w in [1440,360]],notes=['DINOv2同支架缺口、.014算例及同位置放大對應','Gemini同圓接頭，格式通過/內容錯誤有分開驗'],user_approval='pending'),ensure_ascii=False,indent=2),encoding='utf-8')
for name in ['batch4-prototype-image-assessment.json','batch4-expanded-image-assessment.json','batch4-failure-image-assessment.json']:
 p=W/name;a=json.loads(p.read_text(encoding='utf-8'))
 for r in a:r.update(page_review='passed',page_evidence='batch4-page-assessment.json; batch4-failure-page-review.json')
 p.write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf-8')
p=W/'inventory.json';a=json.loads(p.read_text(encoding='utf-8'))
for r in a:
 if r['id'] in owners:
  r.update(status='local_complete',evidence_wi033=['batch4-page-assessment.json','batch4-validation-summary.json',f'pages/{r["id"]}'])
  mp=C/r['manifest_path'];mp.write_text(mp.read_text(encoding='utf-8').replace('native_reviewed_page_pending_user_pending','native_and_page_reviewed_user_pending'),encoding='utf-8');shutil.copyfile(mp,C/'docs'/r['manifest_path'])
p.write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf-8')
p=W/'PLAN.md';p.write_text(p.read_text(encoding='utf-8').replace('- [ ] 第四批：','- [x] 第四批：'),encoding='utf-8')
validation={k:v[k] for k in ['ui_states','zoom_checks','http_checks','bundle_assets','html_sha256','answers','navigation']};validation.update(tests=tests,new_engineering_pngs=64,new_main_failure_pngs=4,native_and_page_review='passed',user_approval='pending',published=False)
(W/'batch4-validation-summary.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2),encoding='utf-8')
with (R/'TEACHING_REVIEW_LOG.md').open('a',encoding='utf-8') as f:f.write('''\n## WI-033-L5：第四批八課完成與驗證更正\n64工程PNG及4同件主反例逐張原生/頁內實看；32狀態224放大，8 tests/120 subtests與來源docs/HTTP驗證通過，詳batch4-validation-summary.json。任務與機制不整張重複，NMS後驗收另列定位偏移/漏框，VLM回答與原因分開。更正L4「PNG缺畫」推斷：獨立重拍與逐像素比對一致，見render-diagnostic-result.json；是審查顯示誤判，未證明disable-gpu修復圖像。驗證腳本另修正模型背景應在展開後查核，未更動教材以迎合檢查。完成25/52，使用者核准pending，未發布。\n''')
note='''### WI-033 最新：25/52課本機完成

第四批8課已完成64工程PNG/4同件主反例，逐張原生與頁內審查；32頁面狀態224放大、8 tests/120 subtests、來源docs及HTTP一致通過。證據batch4-page-assessment.json、batch4-failure-page-review.json、batch4-validation-summary.json；使用者核准pending，未發布。驗證脚本已依實際收合設計在展開後查模型背景，重驗通過；先前PNG缺畫誤判已撤回。
第五批8課機制原型16PNG已生成尚未原生審；24工程擴展與PatchCore深讀手機第二章待做。下一步逐張審原型/修正，再擴展整合驗頁；後19課繼續，全部52課授權不縮減。產物與唯一checklist：workitems/wi-033/PLAN.md。
'''
(W/'checkpoint-note.md').write_text(note,encoding='utf-8');runpy.run_path(str(W/'append-checkpoint.py'))
p=R/'Overall_Review.md';s=p.read_text(encoding='utf-8');names=['YOLO dense detector','RT-DETR','Grounding DINO','YOLOE','DINOv2','LLaVA','Qwen-VL','Gemini Vision'];s='\n'.join(l.replace('待執行','本機修正、自評與驗證完成；待使用者審閱') if any(l.startswith('| '+n+' |') for n in names) else l for l in s.splitlines());p.write_text(note+'\n'+s,encoding='utf-8')
print('25/52 local complete; batch5 continues')

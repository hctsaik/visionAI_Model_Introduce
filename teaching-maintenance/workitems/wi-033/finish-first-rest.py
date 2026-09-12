from pathlib import Path
import json,shutil,runpy
W=Path(__file__).resolve().parent;C=W.parents[1];R=C.parents[1]
proof='verification-dinov3-ad-diffad-ad-anomalygpt.json';v=json.loads((W/proof).read_text(encoding='utf-8'));assert v['ui_states']==12
notes={
'dinov3':['接頭主線及同墊圈缺口反例分工明示，縮圖不換件','Gram教師/學生對称算例與部署分開，不把局部顏色當分割','換骨幹重建相容庫，輸入/成本/驗證可接手','同任務比較DINOv2/v3，允許各自相容前處理','主線手機四段偏長；新反例与八工程三段可讀','遷移題要求留出集、任務命中、建庫与記憶體成本'],
'ad-diffad':['相同原圖與恢復，局部刮痕與正常孔邊反例可追','兩尺度N引導低噪聲恢復，A/R進學習分割','保存A/R/位置圖；完整時間含兩分支、分割与前後處理','與DRAEM/DDAD分數來源不同，無共同測量不排名','工程手機讀得出箭頭和A/R；保留主線部分次字細','題目涵蓋細傷、大缺陷與門檻，承認速度/漏檢取捨'],
'ad-anomalygpt':['同金屬板p細痕/q孔邊，手機三圖已減量','固定encoder/LLM，內建定位經提示器入LLM；三種輸入清楚','model.md与raw比較表舊外部證據說法已修正','三方法同定位任務，再比額外對話工時與錯誤','新手機三段實頁328px可讀；工程次字仍偏細','遷移題允許保留只看位置流程，文字流暢不是有據']}
out=[]
for id,why in notes.items():out.append(dict(id=id,scores=[19,19,19,18,8,9],total=92,evidence=why,completion={'aesthetics':[8,'保留生成主線與新SVG風格略異'],'completeness':[9,'主線、反例、比較、自測、工程與操作卡'],'professionalism':[9,why[1]],'density':[8,why[4]],'hierarchy':[9,'首讀与展開工程分開']},veto=[],status='local_complete',user_approval='pending',model_inference=False))
(W/'first-rest-page-assessment.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
for name in ['first-rest-image-assessment.json','gpt-mobile-image-assessment.json','active-assets-dinov3-ad-diffad-ad-anomalygpt.json']:
 p=W/name;rows=json.loads(p.read_text(encoding='utf-8'))
 for row in rows:row.update(page_review='passed',page_evidence='pages/dinov3, pages/ad-diffad, pages/ad-anomalygpt; native and actual desktop/mobile figures inspected')
 p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
p=W/'inventory.json';rows=json.loads(p.read_text(encoding='utf-8'))
for row in rows:
 if row['id'] in notes:
  row.update(status='local_complete',evidence_wi033=['first-rest-page-assessment.json',proof,'pages/'+row['id']])
  mp=C/row['manifest_path'];mp.write_text(mp.read_text(encoding='utf-8').replace('native_reviewed_page_pending_user_pending','native_and_page_reviewed_user_pending'),encoding='utf-8');shutil.copyfile(mp,C/'docs'/row['manifest_path'])
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
p=R/'Overall_Review.md';lines=p.read_text(encoding='utf-8').splitlines();p.write_text('\n'.join(s.replace('待執行','本機修正、自評與驗證完成；待使用者審閱') if any(s.startswith('| '+name+' |') for name in ['DINOv3','DiffusionAD','AnomalyGPT']) else s for s in lines)+'\n',encoding='utf-8')
p=W/'PLAN.md';s=p.read_text(encoding='utf-8').replace('- [ ] 第一批：','- [x] 第一批：');p.write_text(s+'\n第一批六課完成本機修正。新增本三課29張啟用PNG原生與頁內審查；12狀態、84放大、自測/導覽、來源HTTP与全站資產hash通過，數量以verification-dinov3-ad-diffad-ad-anomalygpt.json為準。其餘46課仍待修，使用者核准pending。\n',encoding='utf-8')
(W/'current-action.md').write_text('第一批六課修正完成，第二批正在核對LK／RAFT共同反例、AnomalyDINO旋轉案例与EfficientAD深讀缺口；即將建立各自機制原型。52課授權範圍不縮減；其餘批次尚未製作。第一批8 tests／120 subtests通過，後續主圖改動另跑實頁補驗。',encoding='utf-8')
with (R/'TEACHING_REVIEW_LOG.md').open('a',encoding='utf-8') as f:f.write('''
## WI-033-L2：機制修正必須走到來源與整頁（2026-09-12）

Pose、DINOv3、DiffusionAD及AnomalyGPT工程圖與指定手機/反例本機完成；第一批累計6/52。分數和證據見workitems/wi-033，不代表使用者已核准，未做模型推論或真人學習測試。

- DINOv3反例的粗格必須由同一缺口幾何取樣，不能換成另一種環形或任意熱圖。用解析式格平均保留可追算來源，並寫明是輸入取樣示意。
- DiffusionAD去除刮傷是恢復方向，不可直接叫漏檢；要追A/R共同進分割後的最終位置。正常去噪訓練圖也不可誤帶刮痕。
- AnomalyGPT內建位置經prompt learner影響回答。外部specialist、retrieval與structured schema是應用可選擴充，修圖時須同步查raw comparison與model.md，不能只新增一段正確文字而留下舊錯流程。
- Pose示意點身份優先於裝飾；三點示意不可暗示能唯一求PnP。兩種2D找點方法需畫替代分支。
- 原生圖可讀不保證手機頁可讀。AnomalyGPT三張首讀手機改為三段並實看328px圖框，保留p/q身份；桌機有效主線保留。評分仍沿用v1，工程手機細字和長捲動列扣分理由。
- 來源建置失敗後不能繼續bundle；新增fail-fast建置入口，讓錯誤先停在來源階段。已跑的8 tests／120 subtests與新增圖的實頁補驗分開記錄。

下批核對：LK與RAFT同時接受相同清楚/反光影像；旋轉反例的刻字須與整件一起旋轉；EfficientAD的global比較對象是AE與Student第二輸出，替代输出不可串成因果。
''')
runpy.run_path(str(W/'checkpoint-state.py'))

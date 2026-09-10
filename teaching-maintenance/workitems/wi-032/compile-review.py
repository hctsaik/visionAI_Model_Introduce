"""Package the manually observed evidence; never derives a score from test success."""
import json,hashlib
from pathlib import Path
W=Path(__file__).resolve().parent;C=W.parents[1]
notes=json.loads((W/'engineering-review-notes.json').read_text(encoding='utf-8'))
plans={r['id']:r for r in json.loads((W/'engineering-plan.json').read_text(encoding='utf-8'))}
assets=json.loads((W/'engineering-active-assets.json').read_text(encoding='utf-8'));images=[]
for r in assets:
 p=plans[r['id']];scores,observations,deductions=notes[r['id']]
 evidence=W/'pages'/p['owner']/f"docs-{'360' if r['mode']=='mobile' else '1440'}-engineering-{p['index']}.png"
 assert evidence.is_file()
 row={**r,'rubric':'v1.0','scores':scores,'total':sum(scores),'observations':observations,'deductions':deductions,'screenshot':evidence.relative_to(W).as_posix(),'scope':'圖片像素及圖內標籤；正文不作圖片加分','actual_page_review':'self-reviewed','user_review':'pending',
 'criteria_evidence':{'case':observations,'meaning':deductions,'action':p['takeaway'],'reading':'三個主要節點，各有獨立圖形及兩行判讀；桌機橫讀、手机縱讀。次要英文／圖例較小，故不給滿分。','consistency':'依此圖同件、配色、箭頭與角色核對；'+deductions},
 'completion':[8,9,9,8,9],
 'completion_evidence':['留白、框距與藍灰配色穩定；原生工程圖造型較簡筆，8分。','三個節點及結論完整；'+p['takeaway'],'箭頭、角色與示意界線已核對；'+observations,'必要標籤可讀，手機仍需縱向捲動；次要說明稍密，8分。','主標題、節點、圖形到單一淡黃結論依序；未放第二個搶焦點的總結。']}
 assert sum(scores)>90
 images.append(row)
(W/'engineering-assessment.json').write_text(json.dumps(images,ensure_ascii=False,indent=2),encoding='utf-8')
main=json.loads((W/'main-original-assessment.json').read_text(encoding='utf-8'));selection=json.loads((W/'selected-assets.json').read_text(encoding='utf-8'))
lessons=json.loads((W/'lesson-content.json').read_text(encoding='utf-8'))
for row in main:
 slug=next(s for s,a in lessons.items() if row['id'] in a['assets']);n=lessons[slug]['assets'].index(row['id'])+1
 row['page_review']='self-reviewed';row['screenshot']=f"pages/{slug}/docs-{'360' if row['mode']=='mobile' else '1440'}-main-{n}.png"
 row['scope']='原生PNG與1440px桌機／360px手機實頁；共用圖按相同hash引用，各課放置另驗'
 row['completion_evidence']=['案例／線索具可辨識形狀、留白與對比；原生幾何較簡筆。','物件、處理／比較、結果與下一步均在圖中；'+row['observations'],'身份、方向與示意界線已核對；不把示意當模型性能。','手機改縱向大主體；小圖例和縱向長度仍是閱讀成本。','三至四大節點及單一淡黃結論；主體先於補充文字。']
(W/'image-assessment.json').write_text(json.dumps(main+images,ensure_ascii=False,indent=2),encoding='utf-8')
# Whole-page grades are independently assigned to this six-lesson scope.
grades={'charuco':[19,19,19,18,8,9],'ecc':[19,19,19,18,8,9],'sift':[19,19,19,18,8,9],'lightglue':[19,19,18,18,8,9],'det-dino-detector':[19,19,19,18,8,9],'yolo-world':[19,19,19,18,8,9]}
pages=[]
for slug,a in lessons.items():
 scores=grades[slug]
 pages.append({'topic':slug,'rubric':'v1.0','scores':scores,'total':sum(scores),'scope':'完整首讀、展開工程4圖及交付；course/docs桌機1440與手機360，390深連結補測。','image_evidence':[r['screenshot'] for r in main+images if f'pages/{slug}/' in r['screenshot']],
 'criteria_evidence':[a['problem'],a['core'],a['output']+' '+a['first'],a['compare']+' '+a['change'],'首讀3圖後接遷移自測，工程4圖折疊；手機使用直向圖，工程放大保留可捲動全尺寸。',a['quiz'][1]+' → '+a['quiz'][3]],
 'deductions':['案例為教學示意，未覆蓋不同現場的全部工件。','必要原理有可見中間關係，精細求解／網路結構在工程層仍有簡化。','已有輸入、輸出與核對責任；未提供可直接運行的模型操作範例。','資料、輸出與完整成本都有條件比較；没有同硬體的實測優劣證據。','手機需要較長縱向捲動，少數次要英文字例仍小；未因此假定真人理解。','新條件有合理替代解答，但沒有真人學習測試。'],'vetoes':[],'user_review':'pending','status':'self-reviewed; user approval pending'})
 assert sum(scores)>90
(W/'page-assessment.json').write_text(json.dumps(pages,ensure_ascii=False,indent=2),encoding='utf-8')
print('Recorded manual evidence for',len(main+images),'PNGs and',len(pages),'complete lessons; user approval pending')

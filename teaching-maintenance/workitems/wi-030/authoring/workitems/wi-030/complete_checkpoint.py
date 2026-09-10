import json
from pathlib import Path
W=Path(__file__).resolve().parent;C=W.parents[1];R=C.parents[1]
public=json.loads((W/'public-release-verification.json').read_text(encoding='utf-8'))
deployment=json.loads((W/'deployment-status.json').read_text(encoding='utf-8'))
assert public['html_matches'] and len(public['png_checks'])==42 and len(public['handoff_document_checks'])==116
assert all(r['status']==200 for r in public['png_checks']+public['handoff_document_checks'])
assert deployment['commit']==public['commit'] and any(r['conclusion']=='success' for r in deployment['runs'])
h=public['commit'];run=next(r['id'] for r in deployment['runs'] if r['conclusion']=='success')
s=f'''
## WI-030 完成與公開版本（2026-09-11）
- [x] 四個異常偵測與八個分類／分割／姿態Topic共12課已重作並發布；21個故事、42張桌機手機PNG，必要原理、反例、比較、自測及操作卡完整。
- [x] 逐圖原生及936/328px自評、十二課整頁閱讀完成；實際驗證72頁面狀態、216次圖片解碼放大Escape、24最終閱讀／新解答狀態、84本機PNG HTTP/hash。
- [x] 最終1347引用資產及HTML來源／docs一致；僅12課教材JSON變動，其他46課一致，五課既有深讀資料保留。文件打包修正涵蓋58課共116既有文件，2 tests／116 subtests及12課24文件HTTP/hash通過。聚焦UI／型別／尺寸回歸9 tests／10 subtests通過。
- [x] 內容commit `{h}` 已push；Pages run {run} 成功。公開HTML、42PNG與116 Markdown文件逐一HTTP及內容hash核對成功，證據public-release-verification.json。
- [x] 共用學習已写回IMAGE_STYLE_GUIDE.md、TEACHING_WEBPAGE_GUIDE.md與TEACHING_REVIEW_LOG.md；版本／prompt／來源／自評／實際驗證及可恢復修改保存在workitems/wi-030與teaching-maintenance快照。
- 限制：舊全站verifier仍在未改動ChArUco inline schema失敗，未算通過。原工程圖未重審，不用本輪首讀分數代表舊工程內容。所有新圖為教學示意，無本輪模型推論、現場效能或真人學習測試。
- 狀態：實作、驗證與公開發布完成；使用者成品核准pending。下一步僅依使用者實際成品回饋開修訂，不把自評通過當作核准。即將把公開驗證紀錄同步並另做紀錄commit；不再改教材。
'''
for p in [W/'PLAN.md',R/'WORKITEMS.md',C/'BEGINNER_VISUAL_TODO.md',C/'BEGINNER_VISUAL_STATUS.md']:
 with p.open('a',encoding='utf-8') as f:f.write('\n'+s)
p=W/'PLAN.md';text=p.read_text(encoding='utf-8').replace('- [ ] 分項評分、共用學習回寫、持久快照、Git與公開版本核對。','- [x] 分項評分、共用學習回寫、持久快照、Git與公開版本核對。');p.write_text(text,encoding='utf-8')
p=R/'WORKITEMS.md';text=p.read_text(encoding='utf-8').replace('- 狀態：進行中；本輪替代已完成WI-028作為當前目標。基準12fc9ff且Git乾淨；尚未產圖／整合／測試，使用者核准pending。','- 狀態：WI-030實作、驗證及公開發布完成；內容commit '+h+'。使用者成品核准pending，歷史checkpoint保留如下。').replace('- 接續唯一細項：teaching-images/vision-ai-model-selection/workitems/wi-030/PLAN.md。下一步保存12課基準、實看參考，先PatchCore原型再擴展。','- 接續唯一細項：teaching-images/vision-ai-model-selection/workitems/wi-030/PLAN.md。下一步依使用者成品回饋開修訂；不用舊自評代替回饋。');p.write_text(text,encoding='utf-8')
p=W/'validation-summary.json';d=json.loads(p.read_text(encoding='utf-8'));d['public_release']={'status':'verified','commit':h,'pages_run':run,'png_hashes':42,'handoff_documents':116,'evidence':'public-release-verification.json'};p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (R/'TEACHING_REVIEW_LOG.md').open('a',encoding='utf-8') as f:f.write('\nWI-030收尾：12課42PNG自評與實頁審查、發布驗證完成；公開HTML／42PNG／116文件一致。實際範圍、逐項扣分及既有ChArUco失敗見workitems/wi-030；使用者核准pending。\n')
print('Completion and public evidence recorded',h)

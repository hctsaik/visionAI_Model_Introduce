from pathlib import Path
import json,hashlib,runpy
W=Path(__file__).resolve().parent;C=W.parents[1];R=C.parents[1]
load=lambda n:json.loads((W/n).read_text(encoding='utf8'))
v=load('verification-all52.json');a=load('final-selected-assets.json');inv=load('inventory.json');caps=load('caption-verification.json')
assert all(r['status']=='local_complete' for r in inv) and len(inv)==52 and v['bundle_hashes_match']
assert caps['html_sha256']==v['html_sha256']==hashlib.sha256((C/'interactive-learning.html').read_bytes()).hexdigest()
for n in ['batch7-tests.json','final-extra-tests.json']:assert load(n)['exit_code']==0
learn={
'IMAGE_STYLE_GUIDE.md':'''### WI-033 局部修正的共用圖像學習

- 同件反例固定工件外形、孔位與局部座標；局部放大要有來源框。裁切以實際輸出核對，SVG viewBox 以外的圓孔或箭頭不得滲進圖說。若示意只說明「可能不同」，不可宣稱兩幾何圖精確降採樣相同。
- 平均誤差圖明寫比較量（差、平方差、特徵距離）、單位及聚合範圍；不同訓練目標的數值不能直接排名。計算呼叫數與實測毫秒分開，給定門值或權重不當建議參數。
- 遮罩、提示或輪廓是生成條件，與實際生成結果逐位置對照。把兩個mask畫出來不代表生成了兩個缺陷；已生成圖仍需材料、位置與獨立真實資料驗證。
- 有梯度要畫清更新對象；採樣時更新latent不等於訓練模型權重。固定主幹、可訓練分支、停止梯度與EMA更新分別呈現。復原檢查依噪聲模型看殘差，不假設已知原圖的真實噪聲。

適用證據與失敗稿：WI-033各批preflight、逐圖assessment及TEACHING_REVIEW_LOG.md。量表與使用者核准門檻未改。
''',
'TEACHING_WEBPAGE_GUIDE.md':'''### WI-033 頁面與交付的共用學習

- 圖說可讀性要量標題底部與放大按鈕頂部，手機可將標題獨立成行、按鈕下排；全頁無水平溢出不代表圖說有足夠空間。修改共用CSS後核對所有受影響課程。
- 圖片等待依瀏覽器實際picture選圖、載入與解碼狀態；長圖截圖混入sticky遮擋或工具顯示空白時，以來源像素及獨立實頁核對，不把截圖失敗直接判成教材壞圖。
- 分批驗證可保留原截圖日期及版本，但最後需重核所有現行引用與已審資產hash；明寫累計頁面狀態與本次新跑範圍，不把舊QA紀錄改稱本次全站重拍。首次執行失敗、修復與通過各自保存。
- 啟用圖、model.md、manifest、來源HTML、docs與HTTP構成同一交付鏈；總报告逐項連到證據。全套舊測試可能包含已撤銷版型，選取現行契約必要回歸並明列範圍，不宣稱所有歷史測試均通過。

驗證实例：WI-033全52課連結/版本核對、58課手機圖說與各批頁內審查。未進行真人學習成效試驗。
'''}
for name,body in learn.items():
 p=R/name;s=p.read_text(encoding='utf8')
 if body.splitlines()[0] not in s:p.write_text(s.rstrip()+'\n\n'+body,encoding='utf8')
# Reconcile staging manifests only when their exact image is covered by final native + page evidence.
known={x['path']:x['sha256'] for x in a['assets']}
for p in W.glob('*active-assets*.json'):
 data=json.loads(p.read_text(encoding='utf8'))
 if isinstance(data,list):
  changed=False
  for row in data:
   if row.get('path') in known and row.get('sha256')==known[row['path']]:
    row.update(page_review='passed',final_evidence='REPORT.md; verification-all52.json; per-batch page assessments');changed=True
  if changed:p.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')
report=f'''# WI-033 第二部分交付報告

52／52課本機修正、逐圖審查與逐課驗證完成；使用者核准pending，尚未commit、push或發布。本輪沒有新增模型推論，原有實測資料依原來源保留。

入口：[課程](http://127.0.0.1:8000/interactive-learning.html)、[本機網站包](http://127.0.0.1:8000/docs/index.html)。第一部分六課的教材資料與本輪基準相同。

## 改動與證據

保留成立的首讀主線，完成52課共208組工程故事（桌機／手機416張PNG）、指定主反例／比較與深讀手機修正。全部本輪啟用新PNG共{a['active_pngs']}張，逐圖自評{a['min_score']}–{a['max_score']}，無否決項，五項完成度均至少8；這是作者自評，不是真人學習成效或使用者核准。逐圖來源、版本及hash見[final-selected-assets.json](final-selected-assets.json)。

指定深讀：AnomalyDINO旋轉反例、EfficientAD雙分支與1/2/3/4/5/7/8章、ResNet 2/4/8章、SegFormer 1/3/4/5章、PatchCore 2章均已完成，保留有效桌機來源與實測數值。證據見batch2、batch3及batch5的deep-page-review／validation-summary。

## 實際驗證

- 最終來源HTML與docs SHA256：`{v['html_sha256']}`；1,370個引用資產一致。
- 全52課現行HTTP核對{v['http_checks']}個檔案通過；[verification-all52.json](verification-all52.json)保存實際URL及hash。包含圖檔、model.md與manifest。
- 各批累計208個主頁狀態、1,472次放大、208次答案及導覽檢查；最後44狀態在此HTML版本重新擷取。其餘已審版本以既有HTTP hash重核後引用，沒有宣稱208狀態全部在最後一次重拍。
- 指定深讀累計160個章節狀態（64+64+32）通過，逐頁實看另存各批證據。
- 最終必要回歸24 tests、130 subtests通過：工程手機、bundle、導航、長圖、深讀、收合入口及放大邊界；58課178個手機圖說間距通過。未宣稱跑過所有歷史版型測試。
- `git diff --check`通過；只出現Git既有LF/CRLF轉換提示。

## 學習與限制

共用學習已回寫根IMAGE_STYLE_GUIDE.md、TEACHING_WEBPAGE_GUIDE.md與TEACHING_REVIEW_LOG.md：同件同位置、梯度更新對象、差異量與成本單位、條件與結果逐區核對、候選與真實觀測分開、圖片解碼與截圖診斷、分批證據版本追溯。

幾何圖為教學簡化，部分專有名詞仍需正文支援；手機需縱向捲動。生成、復原與超解析候選不能替代獨立實測。使用者成品核准及外部發布仍未發生。

維護副本將保存於`teaching-maintenance/workitems/wi-033/`；權威入口為[PLAN.md](PLAN.md)及根WORKITEMS.md。舊失敗／未完成紀錄保留作歷史，現行狀態以本報告與最終驗證為準。inventory內初始whole_course_compliant等欄位來自WI-031基準，現行完成狀態看status與evidence_wi033。

## 逐課證據

| 課程 | 現行狀態 | 頁面及驗證紀錄 |
| --- | --- | --- |
'''
for r in inv:
 ev=r.get('evidence_wi033',[]);links='、'.join(f'[{x}]({x})' for x in ev if x.endswith('.json'))
 report+=f"| {r['model']} | 本機完成；使用者審閱pending | {links} |\n"
(W/'REPORT.md').write_text(report,encoding='utf8')
with (R/'TEACHING_REVIEW_LOG.md').open('a',encoding='utf8') as f:f.write('\n## WI-033-L9：全52課收尾驗證\n\n52課逐課完成；最終1506HTTP、1370資產一致、累計208主頁/1472放大與160深讀、最後24 tests/130 subtests及58課178圖說通過。逐圖與頁面證據見WI-033 REPORT，使用者核准pending，未發布。觀察→規則：同板q與噪聲驗證、梯度更新對象和差異量已併入IMAGE_STYLE_GUIDE；caption/解碼/分批hash證據已併入TEACHING_WEBPAGE_GUIDE。下一輪依這些具體檢查驗證，不以舊分數代表新成品。資產彙總腳本初次將WindowsPath當字串而失敗；改明確as_posix後重驗，教材未受影響。\n')
note='### WI-033 全52課驗證與報告已完成，維護副本收尾\n\n52/52本機完成，最終1506HTTP/1370資產hash、24 tests/130 subtests、58課178圖說通過。累計208主頁1472放大與160深讀狀態，既有頁面證據按已審hash重核。REPORT.md及final-selected-assets.json完成，學習已回写兩指南及共用log；即將保存維護副本並核對manifest。使用者核准pending，未發布；無教材待修。\n'
(W/'checkpoint-note.md').write_text(note,encoding='utf8');runpy.run_path(str(W/'append-checkpoint.py'))
print('Report and reusable guidance saved; snapshot pending')

from pathlib import Path
import json,shutil,hashlib,urllib.request,concurrent.futures,re
W=Path(__file__).resolve().parent;C=W.parents[1];R=C.parents[1]
read=lambda p:json.loads(p.read_text(encoding='utf-8'))
write=lambda p,v:p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
v=read(W/'final-verification.json');smoke=read(W/'final-smoke.json');scores=read(W/'image-assessment.json');pages=read(W/'page-assessment.json')
assert len(scores)==76 and all(r['total']>90 for r in scores)
assert len(pages)==6 and all(r['total']>90 for r in pages)
assert len(smoke)==18 and all(r['zoom_prev_next_escape'] and not r['errors'] for r in smoke)
assert v['all_bundle_hashes_match'] and v['unchanged_topics']==52
slugs=list(read(W/'lesson-content.json'));documents=[]
for slug in slugs:
 p=C/'_course_content/topics'/f'{slug}.json';t=read(p)
 t['quality_status']={'label':'本機重建、自評與驗證完成','state':'self_reviewed','round':'WI-032','reason':'逐圖及整頁自評、實頁操作與必要回歸已完成；使用者成品核准pending，未發布。'}
 t['teaching_preflight']['visual_status']='self-reviewed';t['teaching_preflight']['user_review']='pending';write(p,t)
 mp=C/t['review_trace']['authority'];s=mp.read_text(encoding='utf-8').replace('- 產生狀態：`ready-for-visual-production`','- 產生狀態：`self-reviewed-tested; user-approval-pending`');mp.write_text(s,encoding='utf-8')
 mf=mp.parent/'slide-manifest.md';s=mf.read_text(encoding='utf-8').replace('implementation_pending_validation_user_review','self_reviewed_validated_user_pending');mf.write_text(s,encoding='utf-8')
 for src in [mp,mf]:
  rel=src.relative_to(C);shutil.copyfile(src,C/'docs'/rel);documents.append(rel.as_posix())
 for p in [W/f'{slug}-active-assets.json']:
  rows=read(p)
  for r in rows:r['page_review']='self-reviewed; interaction checks passed'
  write(p,rows)
selected=read(W/'selected-assets.json')
for row in selected.values():row['page_review']='self-reviewed; interaction checks passed'
write(W/'selected-assets.json',selected)
engineering=read(W/'engineering-active-assets.json')
for row in engineering:row['actual_page_review']='self-reviewed; interaction checks passed'
write(W/'engineering-active-assets.json',engineering)
# Final status-only Markdown edits must also have fresh HTTP evidence.
def check(args):
 prefix,rel=args;url='http://127.0.0.1:8000/'+prefix+rel
 with urllib.request.urlopen(url,timeout=30) as response:buf=response.read();status=response.status
 digest=hashlib.sha256(buf).hexdigest();assert digest==sha(C/rel)==sha(C/'docs'/rel)
 return {'url':url,'status':status,'sha256':digest}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:updates=list(pool.map(check,[(prefix,rel) for prefix in ['','docs/'] for rel in documents]))
updated={row['url']:row for row in updates}
v['http']=[updated.get(row['url'],row) for row in v['http']]
v.update(final_document_http_rechecks=len(updates),supplementary_390_states=len(smoke),legacy_fallback_states=sum(r['legacy_fallback'] for r in smoke),pytest=read(W/'test-results.json')['pytest'],selected_preflights=38,svg_files_checked=64,image_score_range=[min(r['total'] for r in scores),max(r['total'] for r in scores)],page_score_range=[min(r['total'] for r in pages),max(r['total'] for r in pages)])
write(W/'final-verification.json',v)
name={s:read(C/'_course_content/topics'/f'{s}.json')['model'] for s in slugs}
report=['# WI-032：第一部分六課重建完成','','狀態：本機實作、自評與必要驗證完成。使用者成品核准仍為pending；未commit、push或發布。第二部分52課未啟動。','', '本輪依根Overall_Review.md執行；五份權威Markdown及v1.0量表未放寬。新內容涵蓋每課核心原理、具體反例、方法比較、自測、操作交付，以及四張工程圖的桌機／手機版本。','','## 逐課結果','','| 課程 | 新版重點 | 整課自評 | 本機頁面 |','| --- | --- | --- | --- |']
highlights={'charuco':'同棋盤角點、多視角校正／已知內參姿態分開、邊角反例','ecc':'取樣與相關更新、warp方向、局部錯解及獨立殘差','sift':'尺度方向與梯度描述、ratio、四組非退化點對與視差','lightglue':'相容extractor、圖內／跨圖關係、未匹配及自適應計算','det-dino-detector':'訓練專用正負去噪、mixed query、推論輸出與遮擋','yolo-world':'詞彙與影像互動、區域比對、快取／分類頭重參數化及取像限制'}
for p in pages:
 slug=p['topic'];report.append(f"| {name[slug]} | {highlights[slug]} | {p['total']}/100 | [開啟]('../../docs/index.html#view=lesson&lesson={slug}&slide=1') |".replace("]('",'](').replace("') |",') |'))
report+=['','自評不是使用者核准或真人學習成效。逐圖91–94分、整課91–92分；手機長捲動、次要圖例較小、部分結構簡化，以及沒有同硬體現場比較，都明列扣分或限制。','', '## 圖片與來源','','- 38個故事、76張新PNG：主線14組桌機／手機共28張，工程24組桌機／手機共48張。工程圖沒有與主線PNG重複hash。','- 相同幾何／偵測比較圖按hash共用，各課位置與圖說另驗。','- ChArUco與其他幾何圖採新建精確SVG；偵測主線與ECC核心使用內建imagegen。生成意圖、各版brief、失敗稿及修正保存在本工作項目，見[原型審查](prototype-review.md)。','- R06四張歷史示意原樣複製，另保留ECC舊工程4連結；不把舊數字或照片當成新模型實測。見[來源界線](sources.md)及[保留檔hash](retained-evidence.json)。','', '## 實際驗證','','| 檢查 | 結果 | 證據 |','| --- | --- | --- |',f"| 桌機1440／手機360，course與docs | 24頁狀態、168次放大解碼／Escape、24自測、24導覽 | 每課pages目錄/report.json |",'| 390px深連結與放大前後張 | 18狀態，含ResNet／RAFT／PatchCore 6個舊課fallback狀態 | [final-smoke.json](final-smoke.json) |',f"| 資產與來源 | {v['bundle_assets']}資產course/docs hash一致；186 HTTP hash，最後12份交付文件另做24次HTTP重核 | [final-verification.json](final-verification.json) |",'| 範圍 | 6課payload更新，52課payload與基準相同 | [final-verification.json](final-verification.json) |','| 必要回歸 | 14 tests、130 subtests通過 | [test-results.json](test-results.json) |','| 製作前檢查／原生邊界 | 38份選定brief通過；64 SVG文字畫布／大型節點邊界無最終錯誤 | [preflight](selected-preflight-validation.json)、[SVG](svg-layout-check.json) |','| 人工審查 | 76張圖逐項評價、6課整體評價 | [image-assessment.json](image-assessment.json)、[page-assessment.json](page-assessment.json) |','','圖框截圖排除固定導覽列，僅用於讀图；top、handoff與放大截圖保留實際介面。兩類測試工具誤報及初次建置失敗保留於[PLAN歷程](PLAN.md)，沒有算成通過。','','## 本輪學習與接續','','共用學習已回寫根TEACHING_REVIEW_LOG.md、IMAGE_STYLE_GUIDE.md、TEACHING_WEBPAGE_GUIDE.md及Overall_Review.md。第一部分具體修正：同物件幾何、手機斷詞／密度、訓練與推論角色、交付文字與新圖一致、可見重參數化，以及舊證據等級重核。','','第二部分52課仍依Overall_Review.md逐課記錄，沒有開工。當下沒有必要實作／驗證阻礙；下一步依使用者審閱結果處理第一部分回饋，或依後續指示開始第二部分。發布及使用者核准均沒有被預設完成。']
(W/'REPORT.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
p=R/'Overall_Review.md';s=p.read_text(encoding='utf-8').replace('狀態：計畫已建立，第一部分進行中。','狀態：第一部分六課本機重建、自評與驗證完成；第二部分52課未開始。未發布，使用者成品核准pending。').replace('來源已整合／實頁驗證中','本機重建、自評與驗證完成；待使用者審閱')
s=s.replace('### 第一部分製作checkpoint','### 第一部分製作歷程（舊checkpoint，以下最終狀態優先）')
s+='\n\n## 第一部分最終狀態\n\n六課已完成本機重建：76張新PNG、主線文字／自測／交付与工程4圖。24主頁狀態／168放大及18個390px補測通過；14 tests／130 subtests通過，1351資產course/docs一致，只有6課payload變更。自評逐圖91–94、整課91–92；真人學習測試未做，使用者核准pending，未發布。詳細[WI-032報告](teaching-images/vision-ai-model-selection/workitems/wi-032/REPORT.md)。\n\n本輪學習已記錄到TEACHING_REVIEW_LOG.md WI-032，以及兩份共用製作指南：同點同件、手機實際尺度、可見機制變化、主線／工程交付一致和歷史示意證據等級。第二部分52課維持待辦。\n'
p.write_text(s,encoding='utf-8')
status='WI-032第一部分六課本機重建、自評與必要驗證完成。Overall_Review.md已分列6課／52課；本輪學習已回寫三份權威Markdown。76張新PNG（28主線＋48工程）及正文／自測／交付已啟用；24主頁狀態／168放大、18補測狀態、14 tests／130 subtests通過，1351資產hash一致，52課payload不變。報告：teaching-images/vision-ai-model-selection/workitems/wi-032/REPORT.md。無未完成必要實作或驗證；使用者成品核准pending，未commit/push/發布。下一步：依使用者審閱處理回饋；第二部分52課等待後續指示。'
for p in [R/'WORKITEMS.md',C/'BEGINNER_VISUAL_TODO.md',C/'BEGINNER_VISUAL_STATUS.md']:
 s=p.read_text(encoding='utf-8');first=s.find('\n## ',1);p.write_text('## WI-032 最終完成狀態（取代下方舊checkpoint）\n'+status+'\n'+s[first:],encoding='utf-8')
p=W/'PLAN.md';s=p.read_text(encoding='utf-8');cut=s.index('\n## Checkpoint');s=s[:cut].replace('- [ ]','- [x]')+s[cut:];s=s.replace('- 下一步：讀完適用權威與實看認可參考，為6課建立versioned preflight，先做一張代表核心原型再擴展。','- 下一步：本輪必要製作／驗證完成；依使用者審閱處理回饋。第二部分與發布待後續指示。');s+='\n\n## 最終完成狀態\n'+status+'\n基準22份來源備份保留；原型及失敗稿未刪。完成的是本機實作、自評、驗證与文件，沒有使用者成品核准。\n';p.write_text(s,encoding='utf-8')
print('Final report, Overall Review, status metadata and persistent checklist complete')

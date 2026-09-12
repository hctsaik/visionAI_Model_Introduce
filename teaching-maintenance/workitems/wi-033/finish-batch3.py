from pathlib import Path
import json,shutil,runpy
W=Path(__file__).resolve().parent;C=W.parents[1];R=C.parents[1]
owners=['resnet','convnext','vit-classifier','u-net','segformer','yolo-seg','keypoint-r-cnn']
v=json.loads((W/('verification-'+'-'.join(owners)+'.json')).read_text(encoding='utf-8'))
d=json.loads((W/'batch3-deep-report.json').read_text(encoding='utf-8'))
assert v['ui_states']==28 and v['bundle_hashes_match'] and len(d)==64 and all(x['complete'] for x in d)
assert json.loads((W/'batch3-deep-page-review.json').read_text(encoding='utf-8'))['status']=='passed'
notes={
'resnet':['同件完整/刮傷對應類別；保留已審首讀','殘差x+F(x)逐格可追，形狀改變須對齊；深讀原實測值保留','前處理、類別映射與錯分回原圖核對','同件換背景測捷徑，位置輸出另需標註','四工程桌機手機與指定深讀實看；長捲動、歷史次標小字扣分','自測允許先補資料而不只加深模型'],
'convnext':['共同支架與整件分類，不把分數當位置','逐通道鄰域、同位通道混合與殘差各有具體圖證','保存裁切、類別順序及部署錯分成本','同資料對比ResNet/ConvNeXt，不以年代定勝負','四工程桌機手機逐張實看；簡化幾何與空白扣分','自測保留穩定ResNet或有條件分流都可接受'],
'vit-classifier':['同件切片加位置，分類頭交類別','Q權重乘V可追算，非缺陷機率；刮傷與孔邊身份一致','解析度/token配對成本與留出集錯分類別一起驗','共同分類任務比較ConvNeXt空間通道與跨片交流','四工程桌機手機逐張實看；分片示意和較長術語扣分','自測分類覆核與像素分割依交付需求選'],
'u-net':['同焊線影像/像素標註/輸出對應','同尺度串接細節，上採樣後再學融合；不是直接相加','ROI/resize/padding映回原圖，量測另校正','同位置連續/中斷對比，不能只看大區域重疊','四工程桌機手機實看無壓字；抽象格圖與長捲動扣分','整圖/重疊切圖須比較上下文、細線及節拍'],
'segformer':['同件四尺度，輸出仍是語意類別','投影/對齊/串接後分類，深讀保留原概念/實測身份','粗取樣不能補回線索，映回原圖才量邊界','與U-Net共用標註比較；不混語意與逐件ID','四工程及五種指定深讀手機實看；小格僅示意，長頁扣分','自測允許受限連通區方案，須驗相接例外'],
'yolo-seg':['兩件同類支架保留甲乙與孔洞','共享P與每件c給出可追代數例，組合後依框取遮罩','框索引/係數索引一起過濾，去重前後幾何一致','同件語意/實例比較，孔洞背景未填滿','四工程桌機手機實看；輪廓是概念而非實測扣分','自測允許先改分料/視角或補重疊標註'],
'keypoint-r-cnn':['支架A缺口角/B/C孔心點名一致','同ROI內三張位置分布，A映回(155,100)可算','遮擋估計与可見證據分開，PnP另有幾何責任','同件具名點/像素區域依交付需求比較','四工程桌機手機實看；ROI小工件與術語較密扣分','自測可先交2D，不預設本輪需要3D']}
out=[]
for o in owners:
 for mode in ['1440','360']:
  for n in range(1,5):assert (W/'pages'/o/f'docs-{mode}-engineering-{n}.png').exists()
 ev=notes[o]
 out.append(dict(id=o,total=92,scores=[19,19,19,18,8,9],evidence=ev,completion={'aesthetics':[8,'精確三段圖，與保留首讀質感略異'],'completeness':[9,'四工程及指定深讀完成'],'professionalism':[9,ev[1]],'density':[8,ev[4]],'hierarchy':[9,'首讀/工程/深讀責任清楚']},veto=[],status='local_complete',page_evidence=f'pages/{o}; batch3-deep-page-review.json',preserved_main='unchanged WI-031 audited sources; automated actual page load/zoom/text checks passed',user_approval='pending',model_inference=False))
(W/'batch3-page-assessment.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
for name in ['batch3-prototype-image-assessment.json','batch3-expanded-image-assessment.json','batch3-deep-prototype-image-assessment.json','batch3-deep-expanded-image-assessment.json']:
 p=W/name;a=json.loads(p.read_text(encoding='utf-8'))
 # Historical unselected candidates retain their status.
 selected={f"{x['id']}-{x['version']}-{m}.png" for x in json.loads((W/'engineering-plan.json').read_text(encoding='utf-8')) if x['owner'] in owners for m in ['desktop','mobile']}
 for r in a:
  if 'deep' in name or r.get('image') in selected:r.update(page_review='passed',page_evidence='batch3-page-assessment.json; batch3-deep-page-review.json')
 p.write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf-8')
p=W/'inventory.json';a=json.loads(p.read_text(encoding='utf-8'))
for r in a:
 if r['id'] in owners:
  r.update(status='local_complete',evidence_wi033=['batch3-page-assessment.json','batch3-validation-summary.json',f'pages/{r["id"]}'])
  mp=C/r['manifest_path'];mp.write_text(mp.read_text(encoding='utf-8').replace('native_reviewed_page_pending_user_pending','native_and_page_reviewed_user_pending'),encoding='utf-8');shutil.copyfile(mp,C/'docs'/r['manifest_path'])
p.write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf-8')
p=W/'PLAN.md';p.write_text(p.read_text(encoding='utf-8').replace('- [ ] 第三批：','- [x] 第三批：'),encoding='utf-8')
validation=dict(tests='15 passed, 120 subtests passed; 2 corrected runtime tests subsequently passed in 21.23s',test_evidence=['batch3-tests-r01.json','batch3-tests-supplement.json'],main_states=28,zooms=196,http=196,assets=1365,deep_states=64,new_engineering_pngs=56,new_deep_mobile_pngs=11,deep_mobile_references=12,html_sha256=v['html_sha256'],user_approval='pending',published=False)
(W/'batch3-validation-summary.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2),encoding='utf-8')
with (R/'TEACHING_REVIEW_LOG.md').open('a',encoding='utf-8') as f:f.write('''\n## WI-033-L4：第三批七課本機完成\n56工程PNG及11種深讀手機重排，逐張原生與頁內審查。28主頁/196放大/196HTTP/1365資產一致、64深讀章節、17 tests與120 subtests通過，細項在batch3-validation-summary.json。原實測特徵/歷史圖錨點與概念身份保留；viewBox精確clip避免旁欄文字滲入，額外手機媒體須分別計數且測試限定深讀容器。局部工程用同件同尺度；標籤不得壓孔/邊界；注意力不是缺陷機率。第四批PNG曾有SVG節點存在但raster缺畫，候選未啟用，正在用軟體繪製及等待字型補驗；不能只憑檔存在給分。完成17/52，未發布，使用者審閱pending。\n''')
note='''### WI-033 最新：17/52課本機完成（2026-09-12）

第三批七課完成本機修正與驗證：56工程PNG、11深讀手機PNG（12引用）；28主頁/196放大/196HTTP/1365資產一致、64深讀狀態、17 tests及120 subtests通過。逐張原生與頁內證據在batch3-page-assessment.json、batch3-deep-page-review.json、batch3-validation-summary.json。保留首讀主線與原實测數據，使用者成品核准pending，未發布。
第四批8課工程2共16張r02候選已渲染，尚未原生複核或整合；r01缺畫未啟用，改disable-gpu及等待字型。下一步審查r02後擴展24工程故事、DINOv2/Gemini同件主反例，再驗八課。後27課仍待製作，持續完成全部52課授權。唯一checklist在workitems/wi-033/PLAN.md。
'''
(W/'checkpoint-note.md').write_text(note,encoding='utf-8');runpy.run_path(str(W/'append-checkpoint.py'))
p=R/'Overall_Review.md';s=p.read_text(encoding='utf-8');names=['ResNet','ConvNeXt','ViT','U-Net','SegFormer','YOLO-Seg','Keypoint R-CNN'];s='\n'.join(l.replace('待執行','本機修正、自評與驗證完成；待使用者審閱') if any(l.startswith('| '+n+' |') for n in names) else l for l in s.splitlines());p.write_text(note+'\n'+s,encoding='utf-8')
print('17/52 local complete; batch4 continues')

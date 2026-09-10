import json, hashlib, re
from pathlib import Path
from collections import Counter
W=Path(__file__).resolve().parent
C=W.parents[1]
R=C.parents[1]
read=lambda p:json.loads(p.read_text(encoding='utf-8'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
dump=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
inv=read(W/'inventory.json'); assets=read(W/'assets.json'); base=read(W/'baseline.json')
shared=read(W/'shared-image-evidence.json')
findings={}
for line in (W/'findings.tsv').read_text(encoding='utf-8').splitlines():
    slug,keep,fix=line.split('\t'); assert slug not in findings
    findings[slug]=(keep,fix)
assert len(inv)==len(findings)==58
assert set(findings)=={r['id'] for r in inv}
rebuild={'charuco','ecc','sift','lightglue','det-dino-detector','yolo-world'}
records=[s for t in inv for s in read(W/'pages'/t['id']/'report.json')]
deep=read(W/'deep-capture.json'); rechecks=read(W/'deep-recheck.json')
captions=read(W/'caption-layout.json')
public=read(W/'public-inventory.json')
verification={
    'topic_count':len(inv),'page_states':len(records),
    'complete_states':sum(x.get('complete',False) for x in records),
    'zoom_checks':sum(x.get('zoom_checks',0) for x in records),
    'answers_opened':sum(x.get('answer_opened',False) for x in records),
    'navigation_changed':sum(x.get('navigation_changed',False) for x in records),
    'page_errors':[x for x in records if x.get('errors')],
    'whole_page_overflow_states':sum(bool(x.get('default_overflow') or x.get('expanded_overflow')) for x in records),
    'caption_count':len(captions),'caption_overlap_count':sum(bool(x['overlap_chars']) for x in captions),
    'deep_chapter_width_states':len(deep),'deep_view_captures':sum(len(x['views']) for x in deep),
    'rechecked_premature_blank_captures':len(rechecks),
    'recheck_files_exist':all((W/x['recheck']).is_file() for x in rechecks),
    'active_assets':len(assets),
    'changed_course_assets':[a['path'] for a in assets if not (C/a['path']).is_file() or sha(C/a['path'])!=a['sha256']],
    'docs_asset_mismatches':[a['path'] for a in assets if not (C/'docs'/a['path']).is_file() or sha(C/'docs'/a['path'])!=a['sha256']],
    'html_unchanged':sha(C/'docs/index.html')==base['html_sha256'],
    'course_docs_html_equal':sha(C/'docs/index.html')==sha(C/'interactive-learning.html'),
    'shared_main_asset_paths':len(shared),
    'shared_hashes_unchanged':all(sha(C/a['path'])==a['sha256'] for a in shared),
    'public_html_matches_at_capture':public['html_matches'],
}
assert verification['complete_states']==verification['page_states']==116
assert verification['answers_opened']==verification['navigation_changed']==116
assert not verification['page_errors'] and not verification['whole_page_overflow_states']
assert not verification['changed_course_assets'] and not verification['docs_asset_mismatches']
assert verification['html_unchanged'] and verification['course_docs_html_equal'] and verification['shared_hashes_unchanged']
assert verification['deep_chapter_width_states']==80 and verification['deep_view_captures']==148
assert verification['recheck_files_exist'] and not verification['caption_overlap_count']
results=[]
for t in inv:
    slug=t['id']; keep,fix=findings[slug]
    evidence=[f'pages/{slug}/1440-reading.txt',f'pages/{slug}/panel-desktop-1.png',f'pages/{slug}/panel-mobile-1.png',f'pages/{slug}/panel-engineering-1.png',f'pages/{slug}/panel-engineering-2.png',f'pages/{slug}/report.json']
    assert all((W/p).is_file() for p in evidence)
    deep_paths=[]
    if t['deep_chapters']:
        deep_paths=[str(p.relative_to(W)).replace('\\','/') for p in sorted((W/'deep'/slug).glob('panel-*.png'))]
    results.append({'id':slug,'model':t['model'],'family':t['family'],
        'classification':'需要重建' if slug in rebuild else '局部修正',
        'main_story':'需要重建' if slug in rebuild else '可保留，局部修正見範圍',
        'whole_course_compliant':False,'engineering':'有實質缺口，按受影響圖重畫',
        'deep':'八章已審；局部修正' if t['deep_chapters'] else '本課無八章深讀層',
        'keep':keep,'fix':fix,'priority':'P1 主線重建' if slug in rebuild else 'P2 局部修正；語意錯接先修',
        'evidence':evidence,'deep_evidence':deep_paths,
        'asset_manifest':'inventory.json','all_layer_scores':None,
        'grading_note':'證據導向缺口分類，未逐張重打完整數字分數；不沿用舊自評',
        'user_approval':'pending','implementation_this_audit':'未修改教材'})
counts=Counter(x['classification'] for x in results)
assert counts=={'需要重建':6,'局部修正':52}
verification['classification_counts']={'符合':0,**dict(counts)}
verification['result_evidence_links_checked']=sum(len(x['evidence'])+len(x['deep_evidence']) for x in results)
dump(W/'results.json',results)
dump(W/'final-verification.json',verification)
families={'geometry':'幾何／校正','classification':'分類／分割／姿態','detector':'物件偵測','anomaly':'異常偵測','video':'影片／時序','foundation':'視覺基礎／多模態','diffusion':'生成／影像復原'}
report='''# WI-031：58課依Markdown標準重新審查

審查完成日期：2026-09-11。審查的是當前58個Topic，另外兩個補充單元不計入。教材與發布檔未修改。

## 判斷結果

| 整課分類 | 課數 | 意義 |
| --- | ---: | --- |
| 符合標準 | **0** | 本輪沒有一課能連同展開工程圖一起判定全課符合。 |
| 局部修正 | **52** | 主線故事、機制及反例可保留；工程圖、指定深讀圖或手機排版需修正。局部可能包含整組工程圖重畫。 |
| 需要重建 | **6** | ChArUco、ECC、SIFT、LightGlue、DINO detector、YOLO-World；核心機制或主要閱讀路徑需要重建。 |

**這個結論不代表58課都要推倒重來。** 52課新版首讀主線多數已有具體案例、可追的中間變化及反例；主要落差是仍然啟用的舊工程圖。6課的問題則已影響首讀教學本身。先前某一輪首讀自評通過，不等於本輪包含所有展開層的整課合格。

## 標準與判定方式

以專案五份權威Markdown為準：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_WEBPAGE_GUIDE.md、TEACHING_SCORING_RUBRIC.md、TEACHING_REVIEW_LOG.md，並參照閱讀層契約。基準檔案hash見[baseline.json](baseline.json)。本輪未改量表權重或門檻。

- 圖片：案例25／機制25／人的行動20／閱讀20／一致性10；頁面：工作20／機制20／交付20／比較20／閱讀10／遷移自測10。原標準要求頁與每張圖各大於90、完整度達標且無否決項。
- 本輪是重新診斷與分類，**沒有替644個資產各編一個分數**。發現「只有名詞沒有可見機制」、「輸出類型畫錯」、「替代方案誤串成流程」等實質缺口，即不能宣稱已符合嚴格整課門檻。逐課指出缺口，而不靠舊分數推算通過。
- 比較要在同一工作與相同條件下成立；圖要看得到方法造成的改變，不能只換模型名稱。主線、工程、深讀分開判斷；有來源的實測與生成示意分開。
- 小頁碼徽章或單純間距擁擠不是主線重建理由；進階公式及有因果必要的第五節點也不一律否決。自評、技術檢查與使用者成品核准分開，本輪未推定使用者核准。

## 家族統計

| 家族 | 課數 | 符合 | 局部修正 | 主線重建 |
| --- | ---: | ---: | ---: | ---: |
'''
for fam,name in families.items():
    group=[x for x in results if x['family']==fam]
    n=sum(x['id'] in rebuild for x in group)
    report+=f'| {name} | {len(group)} | 0 | {len(group)-n} | {n} |\n'
report+='''
## 逐課總表

每課名稱連到本輪保存的主線正文；「主圖／手機／工程」連到實際截圖。更多同課圖、自測、操作卡與互動紀錄位於同一資料夾。共享圖以[相同路徑及hash清單](shared-image-evidence.json)重用視覺證據，各課正文和引用仍逐課檢查。全部機器可讀結果見[results.json](results.json)。

'''
for fam,name in families.items():
    report+=f'### {name}\n\n| 課程 | 分類 | 可保留 | 需要修正／重建的範圍 | 截圖證據 |\n| --- | --- | --- | --- | --- |\n'
    for x in results:
        if x['family']!=fam: continue
        p=f"pages/{x['id']}"
        report+=f"| [{x['model']}]({p}/1440-reading.txt) | **{x['classification']}** | {x['keep']} | {x['fix']} | [主圖]({p}/panel-desktop-1.png)／[手機]({p}/panel-mobile-1.png)／[工程1–2]({p}/panel-engineering-1.png)／[工程3–4]({p}/panel-engineering-2.png) |\n"
    report+='\n'
report+='''## 五課深讀：40章另行審查

| 課程 | 保留的內容 | 局部修正 |
| --- | --- | --- |
| ResNet | 退化、跳接、實際特徵、BN中心化、pooling位置損失、条件取捨 | 手機2/4/8章數值與細字；[桌機](deep/resnet/panel-1440-01.png)、[手機](deep/resnet/panel-360-01.png)及同資料夾其餘視圖。 |
| SegFormer | 窗口共享、四尺度、K/V縮減、通道拼接、train/infer、工作比較 | 手機1章靠邊標題及3–5章细網格／標註；[手機](deep/segformer/panel-360-01.png)。 |
| PatchCore | 特徵來源、coreset、查庫、不同分數實作、污染及公開漏檢／誤報 | 手機2章數值偏小、部分圖工件小留白大；[手機](deep/ad-patchcore/panel-360-01.png)。保留公開原始案例。 |
| AnomalyDINO | 固定DINOv2、最高1%算術、庫污染與作者實例 | 6章旋轉反例的刻字方向不一致，應用同圖剛性旋轉重建；其他手機細圖重排；[深讀文字](deep/ad-anomalydino/1440-chapter-6.txt)。 |
| EfficientAD | T/S1、AE/S2、校正融合，第6章直式分段 | 手機1章舊視圖縮太小，2/3/4/5/7/8章依賴橫滑；4章替代輸出串接改分支；7章補可見建庫／訓練差別；[手機](deep/ad-efficientad/panel-360-01.png)。 |

各課全部深讀截圖路徑列在results.json的deep_evidence；[deep-capture.json](deep-capture.json)列出章節與視圖，[deep-recheck.json](deep-recheck.json)指向需替代初次白圖的重查截圖。

## 建議處理順序

1. **P1：6課核心重建。** 先固定同一工件、單一路徑、可见中間變化與反例；ChArUco分清校正／姿態，ECC放大殘差，SIFT顯示描述子與篩選，LightGlue顯示候選更新，DINO detector顯示去噪訓練，YOLO-World顯示文字表示如何影響出框。保留既有可追溯實例。
2. **先修會教錯的局部圖。** CLIP／SigLIP並行編碼、Pose替代流程、DINOv3訓練／推論、DiffusionAD恢復與檢測、AnomalyGPT內建定位、LK／RAFT同條件反例，以及AnomalyDINO旋轉圖、EfficientAD深讀替代輸出。
3. **P2：逐家族清理舊工程圖。** 按真實輸出畫分類分數、語意／實例遮罩、具身份的點、R/t、偵測框、查庫距離、光流、追蹤ID、回答欄位或復原影像。58課工程層都至少有實質缺口；這不是要求不分內容地重畫232張。ECC工程4等有效案例可保留，其餘按原圖驗收。
4. **P2：指定手機與深讀圖重排。** 優先EfficientAD深讀橫滑，接著小字、公式缺字、長標題遮蓋／省略及工件太小。保留已成立的直式主線。

後續製作應另建工作項，依原技能做版本化preflight、實際PNG及整頁檢查；本輪只提出可執行範圍，沒有開始換圖或发布。

## 證據與驗證界線

'''
report+=f"- 58課 × 1440／360px＝{len(records)}頁面狀態，全部完成；{verification['zoom_checks']}次主圖放大檢查、116次自測答案展開、116次導覽切換。未見page error或整頁水平溢出。容器內橫滑仍另列閱讀缺口。\n"
report+='''- 主線圖文、比較、反例、自測／操作卡，以及每課4張工程圖均實看；5課40個深讀章節，共80章節尺寸狀態、148個視圖擷取並審讀。補看兩課inline SVG手機圖。不是只看檔名或首頁。
- 644個啟用資產在擷取時公開HTTP可達，公開HTML與本機正規化後一致；收尾再核644資產course/docs hash與基準一致、HTML未變。公開資產未逐一GET比hash，沒有宣稱644張都在公開站逐張人工評分。
- 66個主線資產路徑被多課共用；hash已重核。人工視覺證據依同圖重用，非重複算成不同設計。
- 188個360px主線圖說以逐字DOM Range量測，0處字形與放大按鈕重疊。原先擁擠截圖只列間距改善，撤回遮字推測。sticky header／skip link的擷取覆蓋不作教材缺陷。
- 深讀13張初次白圖是切換後擷取過早，等載入後13張均正常；保留初次與重查證據，不列網站空白故障。EfficientAD橫滑圖已看桌機完整內容與手機起始呈現，沒有聲稱擷取每個橫滑位置。
- 本輪未重跑模型、未重現每項論文數據、未做真人學習測試，也沒有逐張完整數字評分。幾何疑點的第一手查證見[technical-verification.md](technical-verification.md)。
- 工具／來源：內建瀏覽器不可用後改用本機Playwright Edge檢查相同發布HTML；公開核對見[public-inventory.json](public-inventory.json)，最終彙整見[final-verification.json](final-verification.json)，逐步人工發現與誤判撤回見[observations.md](observations.md)。

## 接續與保存

審查結果、58筆分類、具體修正范围與驗證已保存本資料夾。根WORKITEMS.md、BEGINNER_VISUAL_TODO.md、BEGINNER_VISUAL_STATUS.md連回本報告；可重用學習寫回根TEACHING_REVIEW_LOG.md與兩份指南。這些是本機持久Markdown，未把聊天或程序ID當唯一紀錄。本輪沒有commit、push或發布。
'''
(W/'REPORT.md').write_text(report,encoding='utf-8')
links=re.findall(r'\]\(([^)]+)\)',report)
local=[x for x in links if not x.startswith(('https:','http:','#'))]
assert all((W/x).exists() for x in local),[x for x in local if not (W/x).exists()]
print(json.dumps(verification,ensure_ascii=False,indent=2))
print('REPORT links verified:',len(local))

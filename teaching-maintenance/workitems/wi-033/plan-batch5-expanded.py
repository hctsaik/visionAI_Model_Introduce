from pathlib import Path
import json,importlib.util,runpy
W=Path(__file__).resolve().parent;C=W.parents[1];p=W/'engineering-plan.json';rows=json.loads(p.read_text(encoding='utf-8'))
owners=['ad-patchcore','ad-padim','ad-subspacead','ad-stfpm','ad-rd4ad','ad-ae','ad-draem','ad-uniad'];proto={r['owner']:r for r in rows if r['owner'] in owners and r['index']==2}
def add(o,n,title,take,panels,detail,kind='C'):
 rid=o+'-engineering-'+str(n);assert not any(r['id']==rid for r in rows)
 rows.append(dict(id=rid,owner=o,index=n,version='r01',kind=kind,mobile_height=2304,title=title,takeaway=take,panels=[dict(title=a,graphic='b5-'+b) for a,b in panels],steps=[],detail=detail,source=proto[o]['source'],terms=proto[o]['terms'],review='pending'))
add('ad-patchcore',1,'PatchCore：用確認正常的局部當參考','正常庫定義見過什麼，輸出仍需人工覆核。',[('同金屬板：先分正常與驗證','split-0'),('正常資料建立可查的庫','pc-coreset'),('交付局部距離及回查位置','pc-delivery')],'建立正常參考只使用已確認正常影像；待測與留出資料不回灌。固定特徵擷取與庫版本，輸出局部距離圖及影像分數，交原圖覆核。這個任務不預先列完缺陷類別，也不直接交付尺寸。')
add('ad-patchcore',3,'PatchCore：縮庫，要連正常覆蓋一起驗','庫小可以省資源，漏掉正常變化會有代價。',[('特徵版本必須與庫一致','pc-contract'),('代表數量影響儲存成本','pc-cost'),('漏掉正常代表可能升高距離','pc-coverage')],'保存骨幹、層、前處理、聚合、coreset及索引。給定10000×512 float32特徵約20.48MB，留1000代表約2.048MB，未含索引/其他模型成本；只是容量算例，不能宣稱查找快十倍。縮库後用獨立正常與真缺陷驗證。')
add('ad-patchcore',4,'PatchCore：庫裡混入刮傷，就可能漏報','低距離可能只是正常庫被污染。',[('同板刮傷p保持不變','scratch-0'),('正常代表與p仍有距離','pc-distance'),('若把同刮傷加入正常庫','pc-contamination')],'同特徵p=[3,2]原本最近正常[2,0]距離√5，誤把[3,2]存為正常後最近距離0。原圖缺陷没有改變；本例只展示局部查庫污染，非實際模型結果。保留資料審核及追溯，不以距離0當品質保證。','D')
add('ad-padim',1,'PaDiM：固定位置，各自建立正常範圍','孔口與平面不同，各自和同位置正常比較。',[('固定單孔板與取像位置','scratch-1'),('每一位置都有自己的統計','padim-fit'),('交出位置距離，回查工件','padim-map')],'適合相機/工件位置受控的局部異常檢查。正常樣本擷取同位置特徵來估計平均和相關性；孔口與平面本來不同。交出馬氏距離圖與影像分數，幾何偏移和正常光線也需驗證，不自動認定缺陷。')
add('ad-padim',3,'PaDiM：位置與統計必須一起保存','換取像或特徵，位置分布也要重新核對。',[('固定網格與特徵處理','padim-contract'),('樣本不足時統計不穩定','padim-regularize'),('同好件位移也須另外驗','padim-shift')],'保存輸入對齊、特徵選維、平均/協方差、正則化及評分設定。協方差要能穩定求解，樣本少或高度相關可能近奇異；可依實作加入正則項，但不保證補足資料。工件位移要用獨立正常樣本驗。')
add('ad-padim',4,'PaDiM與PatchCore：正常的存法不同','同題驗證位置統計與代表庫，各自的假設。',[('同單孔板與相同允收','scratch-1'),('PaDiM保存同位置分布','padim-fit'),('PatchCore保存局部正常代表','pc-coreset')],'比較同一工件/資料切分/允收成本：PaDiM保存各位置高斯統計；PatchCore查跨正常局部的代表庫。圖內PatchCore無孔板僅原型符號不適合跨件比較，工程比較圖須以同單孔板替換來源示意；不聲稱任一方案固定更準。','D')
add('ad-subspacead',1,'SubspaceAD：正常方向是資料擬合出來的','免骨幹訓練，仍要建立可比較的正常子空間。',[('同板正常與獨立驗證分開','split-2'),('固定骨幹與PCA建模','sub-fit'),('交付未被解釋的局部殘差','sub-residual')],'固定DINOv2不更新梯度，正常資料估計均值與低維PCA方向；待測投影殘差形成異常線索。免訓練指骨幹不做梯度更新，不表示免正常資料/擬合/部署驗證；保留原同板主線。')
add('ad-subspacead',3,'SubspaceAD：保留維度就是模型設定','均值、方向與保留維度都必須能重現。',[('保存中心化與投影設定','sub-contract'),('同一x投影到保留方向','sub-project'),('用留出集驗殘差與覆核成本','sub-validation')],'保存骨幹/前處理、正常樣本、均值μ、正交基U和保留維度k；實際投影需先減μ再加回。圖中μ=0是算例簡化。更改k或特徵設定要重新評估正常誤報和真缺陷漏檢，不能只看擬合誤差下降。')
add('ad-subspacead',4,'SubspaceAD：留全維，連異常也能投回去','殘差變小，可能是保留的方向太多。',[('同一待測特徵x保持不變','sub-project'),('只留一維：殘差長度2','sub-one'),('兩維全留：殘差變成0','sub-full')],'延續中心化x=[3,2]；只留水平一維，投影[3,0]殘差2；二維全保留，投影等於x，殘差0。這是線性投影的確切算例，说明增加維度不保證異常檢測更好。','D')
add('ad-stfpm',1,'STFPM：把正常反應教給學生','學生學正常教師反應，差異只是回查線索。',[('同板正常資料教學生','split-2'),('固定教師，正常資料更新學生','stf-train'),('部署比較同圖兩路特徵','stf-branches')],'使用正常影像訓練學生匹配固定教師的多尺度特徵，推論同待測影像送兩路並整合差異。交付可疑位置及影像分數；教師和學生也可能對缺陷反應相似，需留出真缺陷驗證。')
add('ad-stfpm',3,'STFPM：保存兩路權重與逐層配對','同尺度同位置的配對，比單看熱區更重要。',[('教師與學生要成對版本化','stf-contract'),('單位置距離先正規化','stf-distance'),('映回原圖後驗誤報與漏檢','validation-2')],'保存教師權重、學生checkpoint、前處理、特徵層/正規化/插值及彙整方式。推論固定兩路，按同位置與同層計差，不能混不同層或拿熱區直接量尺寸。用未見正常和真缺陷評門檻與覆核量。')
add('ad-stfpm',4,'STFPM與RD4AD：學生吃的輸入不同','同樣比較特徵，兩種學生路徑要分清。',[('同板A與同一檢查任務','scratch-2'),('STFPM學生直接讀同張圖','stf-branches'),('RD4AD學生讀教師的嵌入','rd-decode')],'STFPM教師和同架構學生直接接收同影像；RD4AD由教師表示經瓶頸送反向學生重建。兩者皆在正常資料學習並比特徵，但學生輸入和重建路徑不同；同留出集比代價，不捏造優劣。','D')
add('ad-rd4ad',1,'RD4AD：正常資料教瓶頸與反向學生','先固定教師，正常資料再訓練重建表示。',[('同板正常與驗證資料分開','split-2'),('教師特徵教瓶頸與學生','rd-bottleneck'),('輸出特徵差異供位置覆核','rd-delivery')],'教師固定，正常訓練更新單類瓶頸與反向學生。重建的是多尺度特徵，與同尺度教師表示比較形成位置線索；不是由模型修復物理工件，沒有尺寸或允收保證。')
add('ad-rd4ad',3,'RD4AD：教師、瓶頸、學生是一組','三組權重與尺度配對固定，才能重現差異。',[('三部分保存為同一版本','rd-contract'),('教師與重建逐尺度配對','rd-compare'),('原圖與位置結果一起驗','validation-2')],'保存教師、瓶頸和學生權重及各層的配對、前處理、插值、餘弦差與彙整。避免只部署學生而沒有教師嵌入來源；域內正常光澤和小刮傷都需獨立驗。')
add('ad-rd4ad',4,'RD4AD與AE：重建的對象不同','特徵重建與像素重建，不能共用同一解讀。',[('同一金屬板刮傷p','scratch-2'),('RD4AD比較教師與重建表示','rd-compare'),('AE比較原圖40與重建150','ae-difference')],'在同檢查工件上，RD4AD重建特徵並比餘弦差；AE基線重建像素並在相同位置相減。像素差110和特徵差不是同一尺度的數字，不能直接比較大小判方法好壞。','D')
add('ad-ae',1,'AE：用正常影像學壓縮與還原','重建提供對照，差異大小還須驗證。',[('同板正常資料與測試分開','split-2'),('正常影像教編碼與解碼','ae-train'),('待測同位置相減形成線索','ae-difference')],'正常訓練影像作為AE重建目標；測試原圖與重建估計同位置比較。保留40/150/110原算例，位置差異供原圖覆核；原圖不能在推論時被重建結果取代作真值。')
add('ad-ae',3,'AE：前處理與重建誤差一起固定','同座標、同尺度，差值才可比較。',[('對齊原圖與重建的座標','ae-contract'),('同位置取絕對差值110','ae-difference'),('分開驗小孔誤報與刮傷漏檢','ae-errors')],'保存模型、輸入灰階/RGB範圍、resize/裁切、差異定義與門檻。原圖和重建需要相同座標與像素範圍；既要看刮傷是否留下差異，也要驗正常孔被模糊的誤報，不能只看平均重建損失。')
add('ad-ae',4,'AE：重建得像，也可能漏掉刮傷','差值小不是合格證明，要看差異從何而來。',[('同板刮傷p的原值40','ae-input'),('若重建也複製成40','ae-copy'),('正常小孔q卻可能被模糊','ae-hole')],'同刮傷p原40若被重建成40，絕對差0仍有刮傷；正常小孔q若由30模糊成100，差70可能誤報。後者是新增明示給定反例，非實測，與原主線保持同件大小孔身份。','D')
add('ad-draem',1,'DRAEM：正常圖配合合成異常來教','合成提供訓練目標，驗證仍要用真缺陷。',[('同板正常與獨立真缺陷驗證','split-2'),('兩種監督各有明確來源','draem-train'),('交付學習式位置圖與原圖','draem-seg')],'以正常圖和生成的局部異常建立重建/判別監督，測試使用原圖與重建共同分割。合成mask是訓練真值，不是部署必需輸入，也不保證代表真缺陷。')
add('ad-draem',3,'DRAEM：兩個網路與合成策略一起管','版本能重現流程，真缺陷才能檢驗轉移。',[('保存重建與判別版本','draem-contract'),('原圖與重建一起到判別器','draem-pair'),('合成外觀與真刮傷分開驗','draem-transfer')],'保存兩網路權重、合成來源/區域策略、前處理及位置評分設定。部署不提供真值mask；合成訓練例與真刮傷存在差距，要用獨立真缺陷/正常驗證漏檢誤報和完整延遲。')
add('ad-draem',4,'DRAEM與AE：判別位置不是直接相減','兩張圖同樣作對照，後段判定不同。',[('同一金屬板刮傷p','scratch-2'),('AE以同位置像素差給線索','ae-difference'),('DRAEM用兩張圖學位置','draem-pair')],'同工件比較AE差異基線與DRAEM判別分割：前者直接定義像素差，後者學原圖與重建的joint embedding和位置分類。需分開資料成本與真缺陷驗證，不把DRAEM簡化成AE相減。','D')
add('ad-uniad',1,'UniAD：多類正常，共用重建模型','共用模型仍要涵蓋每類正常變化。',[('金屬板與其他正常類共同準備','uni-multiclass'),('固定骨幹後學重建表示','uni-training'),('同位置原特徵與重建比較','uni-rebuild')],'多類正常資料共訓一個重建模型，固定預訓練骨幹，減少每類獨立模型的維護負擔。不能因共用模型就混淆類別允收；每個產品仍需獨立保留驗證與可追溯輸出。')
add('ad-uniad',3,'UniAD：訓練擾動與推論設定分開','部署讀原特徵，保存遮蔽與query設定。',[('訓練：擾動特徵再學還原','uni-training'),('推論：關閉訓練擾動','uni-eval'),('按每個產品核對錯誤','uni-validation')],'保存骨幹、重建模型、逐層query、注意力鄰域與訓練擾動設定。推論使用eval設定而非繼續訓練噪聲擾動；位置圖回原圖並按類別評正常誤報/缺陷漏檢，單一平均分數可能掩蓋弱類別。')
add('ad-uniad',4,'UniAD：限制照抄，不等於必定抓到缺陷','注意力限制是設計手段，差異仍需真例驗證。',[('若原特徵與重建完全一樣','uni-shortcut'),('限制p讀取自己的近鄰','uni-mask'),('仍用同件缺陷和正常驗證','validation-2')],'相同捷徑使任何輸入都能重建，位置差異可能消失；neighbor mask/learned query/特徵擾動針對此問題，但並不保證每個異常產生大差異。圖中注意力格不等於擦掉原圖，避免把方法動機當結果保證。','D')
# Comparison must keep the same input object as PaDiM.
next(r for r in rows if r['id']=='ad-padim-engineering-4')['panels'][2]['graphic']='b5-pc-coreset-onehole'
spec=importlib.util.spec_from_file_location('v',C/'tools/validate_teaching_preflight.py');v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v);out=[]
for r in rows:
 if r['owner'] not in owners or r['index']==2:continue
 path=W/(r['id']+'-r01.md');s='# '+r['title']+'\n- lesson objective: '+r['takeaway']+'\n- page type: '+r['kind']+'\n- primary reading path: '+' → '.join([x['title'] for x in r['panels']]+[r['takeaway']])+'\n- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`\n- pale-yellow takeaway: '+r['takeaway']+' #FFF4CC\n- major visual nodes:\n'+'\n'.join(f"  {i+1}. {x['title']}；{x['graphic']}" for i,x in enumerate(r['panels']))+'\n'+r['detail']+'\n來源：'+r['source']+'\n模式：新精確SVG→1672×941/768×2304PNG，原生八家族原型已審；三節點單讀序，保留同件身份與首讀。\n權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。\nPNG review pending；page review pending；user approval pending。\n';path.write_text(s,encoding='utf-8');out.append(v.validate(path))
assert len(out)==24
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8');(W/'batch5-expanded-preflight-validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
note='''### WI-033 第五批24擴展故事preflight通過

八機制16PNG已原生審；其餘24故事的任務/部署/比較preflight通過，即將完成具體SVG場景並渲染48PNG，未產出/審查/整合。PatchCore兩手機深讀候選已產出尚未實看。比較保持同件孔位，容量/污染/全維投影/AE複製均為作者給定算例。完成25/52，使用者核准pending，全部52課持續；產物workitems/wi-033。
'''
(W/'checkpoint-note.md').write_text(note,encoding='utf-8');runpy.run_path(str(W/'append-checkpoint.py'))
print('24 expanded preflights passed')

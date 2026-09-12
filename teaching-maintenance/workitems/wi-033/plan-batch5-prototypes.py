from pathlib import Path
import json,importlib.util,runpy
W=Path(__file__).resolve().parent;C=W.parents[1]
rows=json.loads((W/'engineering-plan.json').read_text(encoding='utf-8'))
defs=[
('ad-patchcore','PatchCore：查最近正常特徵，再排回位置','局部距離來自特徵查庫，熱區要回原圖核對。',[('正常特徵挑選代表子集','pc-coreset'),('待測p查最近正常代表','pc-distance'),('每個距離排回原位置','pc-map')],'固定CNN抽正常局部特徵，以coreset保留代表子集；待測局部在同特徵空間查最近鄰。二維例p=[3,2]，r1=[0,0]距離3.61，r2=[2,0]距離2.24；p位置排回2.24。圖中小網格僅局部距離示意，整圖分數還有原法的重加權，不能把局部距離說成缺陷機率。','https://arxiv.org/abs/2106.08265'),
('ad-padim','PaDiM：同位置的方向，改變距離','距離要讀同位置的平均與相關方向。',[('p與q分別累積正常分布','padim-fit'),('同樣偏移，方向代價不同','padim-direction'),('位置距離映回原圖','padim-map')],'每個空間位置建立多變量高斯模型，待測特徵對照同位置的平均與正則化協方差。示意在主軸座標u/v的變異數4/.25，兩個長度2偏移：沿u的馬氏距離1，沿v距離4；u/v為斜向相關軸，非工件座標。孔口q與平面p不可混合套用。','https://arxiv.org/abs/2011.08785'),
('ad-subspacead','SubspaceAD：畫出投影與正交殘差','未被正常方向解釋的殘差，才是異常線索。',[('正常特徵擬合PCA方向','sub-fit'),('同一待測特徵正交投影','sub-project'),('殘差長度排回局部p','sub-residual')],'固定DINOv2提取patch特徵並用正常資料擬合PCA。給定已中心化特徵x=[3,2]與保留方向U=[1,0]，投影[3,0]，殘差[0,2]長度2。二維幾何例不代表工件平面或實際特徵維度；完整公式需保留均值，圖中明示mu=0。','https://github.com/CLendering/SubspaceAD'),
('ad-stfpm','STFPM：兩路同尺度、同位置比較','教師學生的逐層差異，經對齊後整合。',[('同圖分到固定教師與學生','stf-branches'),('單位置正規化特徵對照','stf-distance'),('各層差異對齊再整合','stf-merge')],'教師與學生架構相同，正常訓練只更新學生；推論兩路都固定。以單位向量T=[1,0]、S=[.8,.6]為例，半平方L2距離=.2。原方法上採樣各層位置差異後逐點相乘，給定p三層.2/.4/.5得到.04；這是機制算例，不是異常機率或量測輪廓。','https://arxiv.org/html/2103.04257v3'),
('ad-rd4ad','RD4AD：从瓶頸反向重建教師特徵','學生從教師嵌入重建，逐尺度對照教師。',[('教師多尺度特徵進瓶頸','rd-bottleneck'),('學生由粗到細還原特徵','rd-decode'),('同尺度兩份表示逐一比','rd-compare')],'固定教師編碼器抽多尺度特徵，可訓練one-class瓶頸和反向學生解碼器以正常資料學重建。學生輸入是教師嵌入，不是原圖；對應尺度的教師與重建特徵以餘弦差異比較並映回位置。教師高低尺度與學生逆向重建對應清楚，不把輸出說成修復照片。','https://openaccess.thecvf.com/content/CVPR2022/html/Deng_Anomaly_Detection_via_Reverse_Distillation_From_One-Class_Embedding_CVPR_2022_paper.html'),
('ad-ae','AE：同位置40與150，差值110','比較原圖與重建估計，重建不是正常真值。',[('同板刮傷p的原圖像素','ae-input'),('壓縮還原成重建估計','ae-reconstruct'),('同位置取絕對差值','ae-difference')],'本課為影像自編碼器基線：正常圖訓練壓縮與重建，推論原圖與重建同位置取差。沿用首讀原圖p灰階40、重建150、絕對差110的作者算例；AE若連刮傷一起重建可能漏檢，正常小孔模糊也會誤報。這裡的絕對像素差是明確選定基線，不概括所有AE評分。','https://arxiv.org/html/2103.04257v3'),
('ad-draem','DRAEM：兩種監督，兩張圖判別','重建提供對照，判別器學習位置輸出。',[('正常圖與合成mask各教一事','draem-train'),('待測原圖與重建共同輸入','draem-pair'),('判別網路學可疑位置','draem-seg')],'訓練以正常圖作重建目標、合成異常mask作判別定位目標；推論待測影像經重建，原影像與重建一起送判別網路。位置圖不是單純像素相減，推論不提供真值mask。保留同板A刮傷p；合成外觀只是訓練工具，仍需真缺陷驗證。','https://arxiv.org/abs/2108.07610'),
('ad-uniad','UniAD：限制注意力照抄，再重建','遮的是特徵取用連線，原影像仍完整。',[('同圖抽特徵，原圖不擦除','uni-input'),('p不能讀自己與近鄰','uni-mask'),('query引導重建後比特徵','uni-rebuild')],'多類正常共同訓練重建模型，固定骨幹。neighbor-masked attention限制當前位置讀自己及近鄰的連線；layer-wise query與訓練特徵擾動降低相同捷徑。推論不做訓練擾動，將原特徵與重建同位置差異映回位置；本圖5x5只是注意力鄰域示意，不是固定輸入尺寸。','https://arxiv.org/abs/2206.03687')]
spec=importlib.util.spec_from_file_location('v',C/'tools/validate_teaching_preflight.py');v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
out=[]
for owner,title,take,panels,detail,source in defs:
 rid=owner+'-engineering-2';assert not any(x['id']==rid for x in rows)
 r=dict(id=rid,owner=owner,index=2,version='r01',title=title,takeaway=take,kind='C',mobile_height=2304,panels=[dict(title=a,graphic='b5-'+b) for a,b in panels],steps=[],detail=detail,source=source,terms=['特徵：模型的中間表示，與影像像素分開。','圖中數值：作者給定算例，不是本輪模型實測。'],review='pending');rows.append(r)
 path=W/(rid+'-r01.md')
 body='# '+title+'\n- lesson objective: '+take+'\n- page type: C\n- primary reading path: '+' → '.join([a for a,b in panels]+[take])+'\n- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`\n- pale-yellow takeaway: '+take+' #FFF4CC\n- major visual nodes:\n'+'\n'.join(f'  {i+1}. {a}；{b}' for i,(a,b) in enumerate(panels))+'\n\n'+detail+'\n來源：'+source+'\n模式：新精確SVG→1672×941/768×2304PNG，非既有點陣編修。八課原首讀桌機已實看：PatchCore無孔板、PaDiM單孔板，其餘左上大孔/右下小孔板及右側刮傷p，保持身份；先機制原型再擴展。\n權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。\nPNG review pending；page review pending；user approval pending。\n'
 path.write_text(body,encoding='utf-8');out.append(v.validate(path))
(W/'engineering-plan.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8');(W/'batch5-prototype-preflight-validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
note='''### WI-033 第四批建置完成、第五批機制原型preflight

第四批已建置1371資產/963.7MB；32主頁狀態與8 tests/120 subtests執行中，尚未整批完成。第五批八課原首讀桌機已逐張實看，查核論文/官方repo；八份機制原型preflight通過。即將製作16PNG：查庫距離、位置協方差、正交投影、STFPM逐層差、RD瓶頸反向重建、AE差110、DRAEM雙監督、UniAD注意力連線。其餘24工程故事與PatchCore第二章手機尚未製作。產物workitems/wi-033，完成仍17/52，使用者核准pending；全部52課持續。
'''
(W/'checkpoint-note.md').write_text(note,encoding='utf-8');runpy.run_path(str(W/'append-checkpoint.py'))

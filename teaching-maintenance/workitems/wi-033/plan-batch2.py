from pathlib import Path
import json,runpy
W=Path(__file__).resolve().parent
rows=json.loads((W/'engineering-plan.json').read_text(encoding='utf-8'))
src={'lucas-kanade':'https://docs.opencv.org/4.13.0/d4/dee/tutorial_optical_flow.html','raft':'https://arxiv.org/abs/2003.12039 ; https://github.com/princeton-vl/RAFT/blob/master/core/raft.py','ad-anomalydino':'https://arxiv.org/html/2405.14529v2','ad-efficientad':'https://arxiv.org/html/2303.14535v3'}
terms={'lucas-kanade':['Ix/Iy：影像水平方向／垂直方向的亮度梯度。','It：同位置跨影格的亮度變化。'],'raft':['相關性：兩張影格特徵位置間的配對相似線索。','更新量：更新單元對目前光流提出的位移修正。'],'ad-anomalydino':['token：整張影像經DINOv2後，每個位置的局部表示。','餘弦距離：以特徵方向比較局部有多不同。'],'ad-efficientad':['T/S1：固定教師與學生第一組輸出。','AE/S2：自編碼器與學生第二組輸出；兩者差產生全局圖。']}
def add(owner,i,title,conclusion,panels,detail,kind='C',rid=None):
 rid=rid or f'{owner}-engineering-{i}'
 if any(r['id']==rid for r in rows):return
 rows.append(dict(id=rid,owner=owner,index=i,version='r01',title=title,kind=kind,takeaway=conclusion,panels=[dict(title=t,graphic=g) for t,g in panels],detail=detail,terms=terms[owner],steps=[],source=src[owner],review='pending',mobile_height=2304 if i==0 else 2400))
add('lucas-kanade',1,'Lucas–Kanade：先讓角點有可追的鄰域','清楚角點、穩定影格與小位移，是局部解的起點。',[('同相機相鄰影格','flow-pair'),('角點提供兩方向線索','lk-texture'),('金字塔先粗後細','lk-pyramid')],'同一L形標记随工件平移；先固定相機、時間間隔及取像，選有雙方向梯度的角點。金字塔由粗到細估計位移，傳遞估計再修細；它擴大可處理位移，但不能補回被反光遮住的內容。')
add('lucas-kanade',2,'Lucas–Kanade：多個像素一起限制位移','局部梯度支持共同位移，解出數字後仍要檢查。',[('局部像素提供亮度變化','lk-gradients'),('共同的小位移符合多條式子','lk-equations'),('把解變成可核對的向量','lk-solution')],'在小位移、局部共同運動與亮度一致假設下，每個像素給Ix·u+Iy·v+It≈0。教學給定三組梯度(1,0,-2)、(0,1,-1)、(1,1,-3)，共同解u=2、v=1，單位是影格間像素位移。真實資料以最小平方近似求解，再查矩陣條件、殘差及往返一致性；示意數值不是對插圖執行光流的結果。')
add('lucas-kanade',3,'Lucas–Kanade：把可追的點與失效分開','保存點對、時間與有效性，再決定能否接量測。',[('同名點保留前後座標','flow-points'),('失敗位置退出追蹤','lk-reject'),('像素位移另接校正與時間','flow-measure')],'保存前後影格ID、座標、時間差、狀態與殘差；追丟或一致性差的點不可沿用舊箭頭。需要物理位移或速度時，另有相機運動處理、平面/深度條件與尺度校正，不能把像素向量直接標成毫米或物件ID。')
add('lucas-kanade',4,'Lucas–Kanade：同題比較稀疏與稠密','先確定需要哪些位置，再比較錯誤與完整成本。',[('同一影格對與工作需求','flow-work'),('LK：只驗被選中的點','flow-sparse'),('RAFT：另驗整張位移場','flow-dense')],'同一L形工件、影格間隔和原圖；若工作只需少數穩定角點，LK可作基準。需要稠密場時加入RAFT；在共同可評位置比較位移錯誤，另報各自覆蓋率和端到端耗時，不能把不同輸出數量當成精度優勢。',kind='D')
add('raft',1,'RAFT：先把兩張影格变成配對線索','兩張圖建立相關性，第一張圖另提供更新情境。',[('固定影格對與模型版本','flow-pair'),('兩圖特徵建立全配對','raft-correlation'),('第一圖提供更新情境','raft-context')],'固定原始RAFT權重、解析度、padding和迭代數。共享特徵網路抽兩圖表示後，建立全位置配對相關性及多尺度池化；第一圖經context encoder提供隱狀態與情境。相關性是候選配對線索，不是最終光流或每個像素的可靠度。')
add('raft',2,'RAFT：依目前位置查詢，再修正光流','用目前光流查相關性，更新量加回後繼續修正。',[('在目前估計周圍查線索','raft-lookup'),('更新單元融合四種資訊','raft-update'),('加上更新量，再查下一輪','raft-refine')],'原始RAFT以目前座標查詢多尺度相關性；更新單元接相關性、目前光流、context與隱狀態，輸出位移增量並更新隱狀態。新光流=舊光流+增量，固定解析度反覆更新，最後上採樣。圖中(1,0)+(1,1)=(2,1)只解釋更新算術，不是實際模型收斂或逐輪保證改善。')
add('raft',3,'RAFT：稠密數值要配合有效性核對','輸出向量不等於看見對應，遮擋區要另驗。',[('同一工件輸出稠密場','flow-dense'),('反光與遮擋另查一致性','raft-reject'),('算進相關性與迭代成本','raft-cost')],'保存兩影格、原尺寸、前處理、權重、迭代設定與位移場；遮擋/反射可能沒有可見對應但仍輸出數值。可用往返一致性作應用檢查，仍不是遮擋真值或原始RAFT原生置信輸出。完整成本包含特徵、相關性、更新和上採樣，並量記憶體。')
add('raft',4,'RAFT：增加迭代是否值得，要同題量','迭代設定改變成本，效果仍用同一資料驗證。',[('同資料與同一初始設定','flow-work'),('較少迭代的候選','raft-fewer'),('較多迭代的候選','raft-more')],'固定同一權重、影格對、解析度、precision和硬體，只改更新次數；在同一有效性標註上比较錯誤、覆蓋與耗時，不能保證更多迭代一定改善，也不能把彩色光流當精度證據。保留較少迭代也可能合理。',kind='D')
add('lucas-kanade',0,'沒有可靠對應，兩種光流都要核對','LK與RAFT都看相同輸入；數值不能補回不可見對應。',[('共用兩組影格：清楚／反光','flow-common-cases'),('LK：兩條件都檢查點對','flow-common-lk'),('RAFT：兩條件都檢查向量','flow-common-raft')],'保留原L形刻痕案例。清楚組與反光組使用同一前影格、相同平移；反光組只遮住後影格刻痕。LK與RAFT各自接受完整兩組輸入，分別檢查點或稠密向量，不在圖中編造實測成敗。回原圖與往返一致性核對，物理量測另需校正。',kind='D',rid='flow-main-failure')
add('ad-anomalydino',1,'AnomalyDINO：固定模型，正常局部存庫','免額外訓練，仍要選乾淨正常參考並建立相容庫。',[('少量乾淨正常影像','adino-support'),('整圖進固定DINOv2','adino-encode'),('局部表示連同來源存庫','adino-memory')],'本課少樣本路徑用固定預訓練DINOv2抽整張影像的局部tokens，保留選定正常樣本的特徵與來源。不是逐張裁片重新訓練，也不是零設定；取像、resize及選用mask/rotation需寫清，未見正常與真缺陷另外留出。')
add('ad-anomalydino',2,'AnomalyDINO：每個局部找最近正常','最近距離保留位置，組成候選異常圖。',[('同一待測影像抽局部表示','adino-query'),('全庫搜尋相近正常特徵','adino-distance'),('距離回映同一局部位置','adino-location')],'待測整圖與參考共用DINOv2權重及相容前處理。每個test token以餘弦距離在normal memory找最近者；圖中0.40、0.62、0.55為教學給定距離，最小0.40不代表已足夠正常。局部距離上採樣/平滑形成位置圖；整件分數另聚合最高1%patch距離，不能把熱圖當精密輪廓。')
add('ad-anomalydino',3,'AnomalyDINO：換參考就要重驗正常定義','保存參考版本，誤報與漏檢要一起比較。',[('固定待測件與原參考庫','adino-clean'),('只增加一個刮傷參考','adino-contamination'),('重跑相同留出案例','adino-revalidate')],'固定模型與前處理只增加候選時，最近距離不會增加；若新增參考含缺陷，原本异常可能變得相近。用同一刮痕、原候選距離0.40/0.55、新污染候選0.03說明算術，不宣稱真實模型結果。更新後同时測正常與真缺陷，保存庫來源並量建庫、查詢及記憶體。')
add('ad-anomalydino',4,'AnomalyDINO：先判斷旋轉是否被允許','旋轉擴充改變正常涵蓋，朝向規格仍須另驗。',[('共同工件：刻字有方向','adino-upright'),('自由擺放：可測旋轉參考','adino-rotate-free'),('標誌朝上：不可放寬方向','adino-rotate-required')],'同一帶A-01刻字的板連同所有孔位/字一起剛性旋轉180度。若規格允許自由方向，可測旋轉參考是否減少誤報；若標誌必須朝上，就不能以納入倒置參考來消除方向錯誤，另做方向檢查。兩路是不同工作規格，不是演算法串接。',kind='D')
add('ad-anomalydino',0,'旋轉前，先問方向是否屬於規格','整件與刻字一起旋轉；正常參考不能改寫允收規格。',[('原件：A-01刻字朝上','adino-upright'),('同件剛性旋轉180度','adino-rotated'),('自由擺放與朝上規格分開','adino-rotation-rule')],'修正原深讀6章旋轉圖：以同一個SVG工件群組做180度旋轉，孔、缺口與刻字全部一起變換，沒有重畫另一件或保留正向刻字。若允收自由方向，可驗旋轉參考；朝向本身是缺陷則另立規則。此圖不替換遮罩/接線視圖。',kind='D',rid='adino-deep-rotation')
add('ad-efficientad',1,'EfficientAD：正常品教三個角色合作','教師固定，學生兩組輸出與AE各有訓練目標。',[('正常托盤與固定教師','eff-teacher'),('學生第一組學教師','eff-student1'),('AE與學生第二組一起學','eff-train-global')],'選定預訓練輕量教師並固定；學生第一組以正常影像學教師特徵，原方法另有hard-feature與外部預訓練圖penalty。AE由整圖重建教師特徵，學生第二組學AE重建；使用正常資料訓練，真缺陷留作獨立檢查。學生兩組共享前層，不是兩個互不相關模型。')
add('ad-efficientad',2,'EfficientAD：局部與全局比較對象不同','局部比T/S1，全局比AE/S2；校正尺度後才融合。',[('同一待測托盤送入三者','eff-test'),('兩路各比對應的表示','eff-two-diffs'),('正常驗證資料校正後融合','eff-calibrate')],'同一托盤有中間缺件及右側污點；T與學生第一組S1的通道均方差產生local，AE與學生第二組S2的差產生global，不能誤畫T減AE或直接原圖減重建照片。用未參與訓練的正常驗證分布各自做分位數線性尺度對齊，再平均兩圖；最大值作整圖分數。熱區僅示意，不保證兩路專抓某種缺陷。')
add('ad-efficientad',3,'EfficientAD：保留兩路，才知道融合改了什麼','兩路與融合圖一起驗，完整流程一起計時。',[('保存局部、全局與融合','eff-ablation'),('回同托盤核對兩種錯誤','eff-review'),('相機到覆核的完整時間','eff-cost')],'保存原圖、原始local/global圖、正常分位數校正及融合結果。用獨立正常與真缺陷對照各分支及融合錯誤；同時量取像、前處理、教師/學生/AE、映回與交付的完整耗時，不能從論文毫秒數推定產線節拍。')
add('ad-efficientad',4,'EfficientAD：換產品要更新哪些部分','模型與正常校正一起重驗，不能只換產品名稱。',[('新產品有不同正常外觀','eff-new-product'),('適配學生／AE與分數尺度','eff-maintenance'),('同留出集比較更新前後','eff-update-check')],'換產品先確認正常訓練涵蓋；按需要重新訓練學生與AE，重新建立正常驗證分位數，保留舊版作對照。固定教師版本不代表下游分數可直接沿用；比較正常誤報、真缺陷漏檢、訓練/校正成本與每件耗時，不能只記模型檔大小。')
add('ad-efficientad',0,'同一托盤，換取像仍可能漏掉異常','先核對原圖線索，再驗兩路與融合結果。',[('共同托盤：缺件與污點','eff-test'),('反光只遮住右側污點','eff-glare'),('同一資料檢查兩路與融合','eff-review')],'接續首讀托盤中間缺件、右側污點。反光條件只改取像並遮住右側污點，沒有換成金屬板刮痕。局部/全局仍可能有錯誤，缺件可見不保證一定檢出；以兩類正常/異常留出樣本核對，不編造模型成功圖。',kind='D',rid='eff-main-failure')
(W/'engineering-plan.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
with (W/'PLAN.md').open('a',encoding='utf-8') as f:f.write('\n第二批即將製作16工程與3個主/深讀故事，共19組桌機手機SVG候選。先看四課工程2原型：LK梯度算例、RAFT查詢更新、AnomalyDINO局部查庫、EfficientAD雙分支。EfficientAD七章手機另外排版，未在本19組內宣稱完成。候選與正式引用分開；render前preflight逐份驗證。\n')
runpy.run_path(str(W/'plan-alignment.py'))
# Correct the common scaffold for this batch's actual objects/dimensions.
for r in rows:
 if r['owner'] not in src:continue
 p=W/f"{r['id']}-{r['version']}.md";s=p.read_text(encoding='utf-8').replace('金屬支架／齒輪／軸承','L形刻痕板、A-01刻字板或三格圓柱托盤，依各圖聲明')
 if r.get('mobile_height')==2304:s=s.replace('手機768×2400','手機768×2304')
 p.write_text(s,encoding='utf-8')

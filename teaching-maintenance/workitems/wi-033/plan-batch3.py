from pathlib import Path
import json,importlib.util
W=Path(__file__).resolve().parent;C=W.parents[1]
rows=json.loads((W/'engineering-plan.json').read_text(encoding='utf-8'))
sources={'resnet':'https://arxiv.org/abs/1512.03385','convnext':'https://arxiv.org/abs/2201.03545','vit-classifier':'https://arxiv.org/abs/2010.11929','u-net':'https://arxiv.org/abs/1505.04597','segformer':'https://arxiv.org/abs/2105.15203','yolo-seg':'https://docs.ultralytics.com/reference/nn/modules/head/#ultralytics.nn.modules.head.Segment','keypoint-rcnn':'https://arxiv.org/abs/1703.06870'}
def add(o,i,title,take,panels,detail,kind='C'):
 rid=f'{o}-engineering-{i}'
 if any(r['id']==rid for r in rows):return
 rows.append(dict(id=rid,owner=o,index=i,version='r01',title=title,takeaway=take,kind=kind,mobile_height=2304,panels=[dict(title=a,graphic=b) for a,b in panels],steps=[],detail=detail,source=sources[o],terms=['特徵：由影像學到的中間表示，並非標註真值。','本圖示意：解釋模型責任，不代表新模型實測。'],review='pending'))
add('resnet',1,'ResNet：先把整張照片分到已知類別','整圖分類要類別標註，細傷位置不會自動交付。',[('同件照片與類別標註','b3-res-data'),('殘差逐步更新影像表示','b3-res-residual'),('分類頭交出整件分數','b3-res-score')],'沿用支架完整／缺口兩類工作例。用有標註的整圖訓練分類器，殘差分支學相對輸入的修正；分類頭彙整特徵後交付類別分數，無法直接交付缺口座標。圖中分數是給定示意。')
add('resnet',2,'ResNet：保留輸入，再加上學到的修正','同形狀才能逐位置相加；換形狀需先對齊。',[('輸入x分成兩條路','b3-res-split'),('主路學修正F(x)','b3-res-delta'),('對齊後逐項相加','b3-res-sum')],'用同位置2×2特徵教學例：x=[2,1;0,3]，F(x)=[1,0;2,-1]，相加得到[3,1;2,2]。直通路是輸入特徵而非原圖；形狀不同時需投影或其他對齊。展示殘差核心，啟用函數與其他層於正文說明，不把加法當缺陷消除。')
add('resnet',3,'ResNet：分類結果要連回原圖與標籤','保存類別映射與前處理，換批次後重驗誤判。',[('鎖定裁切與類別映射','b3-res-contract'),('彙整表示再讀出分數','b3-res-pool'),('回原圖核对錯分樣本','b3-res-review')],'推論固定裁切、resize、標準化、權重與類別順序。分類頭使用彙整特徵，不把可視化特徵圖當缺陷位置。保存分數與原圖，分批次驗漏判與誤判；全域平均會弱化某些細小線索，是否漏判仍需資料驗證。')
add('resnet',4,'ResNet：背景變了，分類依據仍要成立','同件換背景測捷徑，定位需求另選位置輸出。',[('同件放在兩種背景','b3-common-background'),('分類器只給整件類別','b3-res-scope'),('需要位置時比較分割','b3-res-alternative')],'相同支架與缺口只改背景，檢查模型是否依背景而非工件分類。若要缺陷位置，另評分割及其像素標註成本；ResNet可當骨幹，但本分類頭不因有熱圖可視化就變成分割器。',kind='D')
add('convnext',1,'ConvNeXt：卷積也能逐步整理分類線索','先定義類別，再用分層卷積彙整影像。',[('有標籤的支架照片','b3-res-data'),('空間與通道各做一次混合','b3-cnx-block'),('彙整後交出類別分數','b3-cnx-score')],'原始ConvNeXt是純卷積骨幹，借鑑現代設計但不是自注意力Transformer。分層下採樣整理影像，區塊含depthwise空間卷積、通道混合與殘差；下游分類頭和標註定義類別。')
add('convnext',2,'ConvNeXt：先看鄰域，再組合不同線索','空間混合不跨通道，通道混合在同位置組合。',[('每通道各看空間鄰域','b3-cnx-spatial'),('同位置混合各通道','b3-cnx-channel'),('殘差保留原本表示','b3-cnx-residual')],'原始區塊用7×7 depthwise卷積，各通道獨立混合鄰域；之後LayerNorm、通道擴張、GELU、通道縮回及layer scale，再加直通路。圖用小鄰域和兩通道示意角色，不聲稱展示完整實際張量。')
add('convnext',3,'ConvNeXt：效率要連同解析度一起驗','保存模型配置，測完整分類流程與錯分代價。',[('固定影像裁切與解析度','b3-cnx-contract'),('由多尺度特徵彙整分類','b3-cnx-pool'),('比較時間與細傷錯分','b3-cnx-review')],'相同產品固定測試集與裁切，記錄ConvNeXt尺寸、精度格式、硬體與整條流程延遲。較小模型或輸入不保證可保留細傷線索；比較整件錯分及人工覆核，不用論文單一指標代替本地選型。')
add('convnext',4,'ConvNeXt與ResNet：先固定同一分類任務','兩者都需域內驗證，架構新舊不能替代結果。',[('共同照片與類別定義','b3-class-common'),('ResNet殘差卷積路徑','b3-res-residual'),('ConvNeXt空間通道路徑','b3-cnx-block')],'兩個候選各用相容前處理，固定產品、類別、訓練資料及留出樣本。比較錯分類型、訓練資源、完整延遲；保留ResNet作合理起點，不能把ConvNeXt現代化設計當所有資料上都較準的保證。',kind='D')
add('vit-classifier',1,'ViT：把影像區塊變成可交流的表示','切片保留位置，分類仍需資料與任務頭。',[('同件影像切成區塊','b3-vit-patches'),('各片加入位置表示','b3-vit-tokens'),('分類token讀出整件分數','b3-vit-cls')],'原始ViT把不重疊patch線性投影成token，加入位置嵌入及分類token；Transformer交換資訊，最後CLS表示經分類頭讀出類別。本課是分類器，不把patch熱圖當分割。')
add('vit-classifier',2,'ViT：一個位置也會參考其他區塊','注意力加權其他表示，位置身份仍要保留。',[('缺口片與孔邊片各有表示','b3-vit-query'),('依內容形成參考權重','b3-vit-attention'),('加權更新，再由CLS分類','b3-vit-update')],'示意某query对兩個value加權0.75和0.25；value [2,0]與[0,4]加權成[1.5,1]。這是單頭簡化算例，實際還含多頭投影、殘差、正規化和MLP。注意力不是物理缺陷機率，也不能用線寬宣稱模型實测解釋。')
add('vit-classifier',3,'ViT：改切片設定，細節與成本都會變','先確認細傷還可見，再測分類與記憶體。',[('同一細痕與輸入取樣','b3-vit-resolution'),('切片尺度改變token數','b3-vit-cost'),('保留同件測試與錯分類型','b3-vit-review')],'改解析度會改token數及注意力成本；改patch尺寸涉及模型配置與權重相容性，不能隨意把現有權重改為另一尺寸。先查實際輸入可見線索，再比較分類、記憶體及延遲；圖中的格子是分片概念而非真實注意力圖。')
add('vit-classifier',4,'ViT與卷積：同題比較資料與計算代價','全局交流是能力來源，不保證小資料就更準。',[('相同分類照片與標籤','b3-class-common'),('卷積先聚合局部鄰域','b3-cnx-spatial'),('注意力跨片交換資訊','b3-vit-attention')],'在相同產品和標籤下比較預訓練、可調整資料量、輸入解析度及硬體成本；卷積局部先驗可能適合部分小資料任務，ViT利用大規模預訓練仍需域內驗證。候選可並行，不畫成必須串接。',kind='D')
add('u-net',1,'U-Net：標出每個像素屬於哪一類','像素標註教會區域，輸出仍需回原圖核對。',[('原圖與細焊線標註','b3-unet-data'),('編碼與解碼接回細節','b3-unet-bridge'),('逐像素分類得到語意遮罩','b3-unet-output')],'沿用板上細焊線工作例，以對齊的影像和像素類別標註訓練。收縮路徑取得上下文，擴張路徑結合對應高解析度特徵恢復定位；輸出是語意區域，不自帶校正後尺寸。')
add('u-net',2,'U-Net：粗尺度找上下文，細尺度補位置','跳接提供對應特徵，解碼器仍要學會融合。',[('下採樣：位置變粗','b3-unet-encode'),('同尺度特徵沿跳接送達','b3-unet-skip'),('上採樣融合後逐像素分類','b3-unet-decode')],'原始U-Net以crop and concatenate把編碼特徵送到匹配尺度的解碼器，並非每條skip都逐元素相加。示意省略卷積邊界尺寸，但保留同尺度配對與融合；遮罩由學習分類得到，不直接複製原圖邊緣。')
add('u-net',3,'U-Net：像素位置先映回，再談尺寸','記錄resize與裁切，像素遮罩不能直接當毫米。',[('裁切與縮放都留下映射','b3-unet-contract'),('遮罩回到原圖同一位置','b3-unet-map'),('輪廓核對後才另接量測','b3-unet-review')],'保存ROI、resize比例、padding及類別映射，將預測映回原图再核對細線斷裂、孔洞與邊界誤差。量測另需相機校正及誤差驗證；IoU高不保證細線連通或毫米誤差達標。')
add('u-net',4,'U-Net：看起來像一條線，仍可能斷一格','同件檢查細線連通，不能只看大區域重疊。',[('同一焊線跨過細縫','b3-unet-line'),('候選遮罩在細處斷裂','b3-unet-gap'),('核對連通與邊界，再選型','b3-unet-boundary')],'同一細線的真值和示意候選只在中央窄處不同；大區域重疊可能掩蓋斷線。固定標註規則與解析度，比較U-Net和多尺度Transformer候選的邊界、连通、錯分及延遲，不把單一IoU排名當唯一決策。',kind='D')
add('segformer',1,'SegFormer：四個尺度一起判讀每個位置','多尺度補上下文，輸出仍是語意類別圖。',[('板面影像與像素標註','b3-unet-data'),('分層編碼產生四尺度','b3-seg-scales'),('對齊融合成語意遮罩','b3-seg-output')],'MiT分層Transformer產生四種尺度特徵；輕量MLP解碼器投影、對齊、串接和融合後輸出語意類別。它不自動給每個相同類別物件獨立身份，與實例分割區分。')
add('segformer',2,'SegFormer：先對齊尺度，再融合線索','四路特徵共同進解碼器，不是四張遮罩投票。',[('四尺度的格位各不相同','b3-seg-scales'),('各自投影並上採樣對齊','b3-seg-align'),('串接融合後逐像素分類','b3-seg-fuse')],'四尺度表示先用MLP統一通道維度，再對齊到同一空間尺度，串接後用MLP融合及分類。顯示同一焊線位置在各尺度的對應，不能把四幅彩格當四次獨立模型分割，也不以框取代輸出遮罩。')
add('segformer',3,'SegFormer：解析度與細邊界一起驗','多尺度不能補回取像已消失的細線。',[('原圖細線與較粗取樣','b3-seg-resolution'),('融合輸出映回原圖','b3-unet-map'),('核對細線、邊界與時間','b3-seg-review')],'雖不依赖固定位置編碼，仍需依模型和實作處理輸入尺寸與padding，不能說任意尺寸均等好。測同一細線在不同解析度的可見性、邊界誤差與整條流程成本；不把插值出更多像素當新增觀測。')
add('segformer',4,'SegFormer與U-Net：共同標註才可比較','語意相同、標註一致，再比細節與運算代價。',[('共同細線影像與真值','b3-unet-line'),('U-Net用對應跳接融合','b3-unet-bridge'),('SegFormer用四尺度融合','b3-seg-align')],'同一產品、同一像素標註規則及留出影像，兩候選各用相容前處理。比較細線連通、邊界、換產品適配及完整延遲；圖只展示機制差異，不編造候選熱圖勝負。',kind='D')
add('yolo-seg',1,'YOLO-Seg：同類零件也要各有一張遮罩','每件有框、類別與遮罩，身份只屬當前影像。',[('两件同類支架各自標註','b3-yseg-data'),('共享影像特徵產生兩路','b3-yseg-branches'),('每件係數組合出自己的遮罩','b3-yseg-output')],'以YOLOv8式prototype和mask coefficients路徑說明。訓練需各實例的類別與輪廓，推論保留各物件框、分數和實例遮罩；圖中甲乙只是這張影像的實例，不是跨影格追蹤ID。')
add('yolo-seg',2,'YOLO-Seg：共用原型，每件用不同係數','原型乘各件係數，再依物件框取回遮罩。',[('共享特徵產生原型圖','b3-yseg-proto'),('每個候選各有係數','b3-yseg-coef'),('組合、裁框、映回影像','b3-yseg-combine')],'檢測頭預測框/類別和每個候選的mask coefficients；Proto支路產生共享basis maps。保留候選的係數線性組合原型，经相應後處理與裁框映回。兩原型是簡化代數例，實際通道數與後處理依所用版本；不能把每張原型直接叫某件物體。')
add('yolo-seg',3,'YOLO-Seg：遮罩要和同一個框一起交付','把框、類別與遮罩綁定，映回原圖再核對。',[('候選框與係數保持配對','b3-yseg-pair'),('去重保留後產生對應遮罩','b3-yseg-filter'),('原圖檢查孔洞與相鄰件','b3-yseg-review')],'遵循實作的候選過濾與去重，索引必須同步框、類別、係數，不能將甲框配乙mask。映回需還原letterbox，輪廓不能填掉空孔；定位與量測仍須另外驗證，遮罩不是亞像素尺寸真值。')
add('yolo-seg',4,'語意與實例分割：同類是否需要分成兩件','需要逐件交付時，比較實例標註與分離品質。',[('同一影像有兩件支架','b3-yseg-scene'),('語意：兩件都屬支架類','b3-yseg-semantic'),('實例：甲乙各有遮罩','b3-yseg-output')],'共同输入与物件外观不变。语意遮罩同色表示同類，不一定提供逐件身份；實例分割分出甲乙，可支援後續逐件統計。重疊與遮擋仍可能分錯，需要標註與域內驗證；不聲稱必然比語意分割更適合所有工作。',kind='D')
add('keypoint-rcnn',1,'Keypoint R-CNN：先找物件，再找具名點','點的身份要先定義，座標不能混成無名熱區。',[('支架A缺口、B/C孔心','b3-kpt-data'),('每件ROI保留相對位置','b3-kpt-roi'),('A/B/C各有自己的位置分布','b3-kpt-heatmaps')],'把Mask R-CNN的關鍵點支路用於自訂工件，需重新定義並標註關鍵點身份；人體預訓練權重不直接懂支架孔心。每個ROI的每個關鍵點有位置分布，經解碼映回原圖，不是任意紅色熱區。')
add('keypoint-rcnn',2,'Keypoint R-CNN：ROI座標要映回原圖','同一個點沿ROI與原圖映射，A/B/C不能互換。',[('原圖框出同一件支架','b3-kpt-roi'),('ROI內各點分開解碼','b3-kpt-decode'),('依框位與尺度映回原圖','b3-kpt-map')],'ROIAlign取得對齊特徵，關鍵點頭分別產生K個位置heatmaps。圖用連續ROI座標示意x=x0+u*w、y=y0+v*h；實作還要遵循格心、resize與padding約定。A點[0.25,0.4]在框原點[100,50]、寬高[200,100]時映到[150,90]。')
add('keypoint-rcnn',3,'Keypoint R-CNN：遮住的點也可能被猜出','估計位置與可見證據分開，可信度不足要覆核。',[('遮擋覆住同件的C孔','b3-kpt-occluded'),('模型仍可能給C的估計','b3-kpt-estimate'),('原圖核對後才接幾何求解','b3-kpt-review')],'不可把每個輸出座標當已見到真實點。可見性標註與模型回傳的score/visibility欄位需按實作解讀；保留原圖、具名座標與分數，遮擋點單獨評估。接PnP另需K、畸變、3D對應與足够非退化點。')
add('keypoint-rcnn',4,'關鍵點與分割：要具名位置還是整片區域','按交付選標註：具名點、輪廓與姿態各有責任。',[('同一支架工作需求','b3-kpt-data'),('關鍵點：A/B/C具名座標','b3-kpt-scope'),('分割：逐像素物件區域','b3-kpt-mask')],'固定同一支架影像，若要孔中心身份對應可評關鍵點；若要整片邊界可評分割。兩者都不單獨保證物理姿態或毫米尺寸；按可見性、標註成本、幾何誤差與後續用途比較。',kind='D')
(W/'engineering-plan.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
spec=importlib.util.spec_from_file_location('preflight',C/'tools/validate_teaching_preflight.py');v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
results=[]
for r in rows:
 if r['owner'] not in sources:continue
 p=W/f"{r['id']}-{r['version']}.md"
 body=f"""# {r['title']}
- lesson objective: {r['takeaway']}
- page type: {r['kind']} — 真實資料變換用C，同條件比較用D。
- primary reading path: {' → '.join(p['title'] for p in r['panels'])} → {r['takeaway']}
- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png` — 已實看具體工件與映射、短句、單黃结論；不沿用多欄小字。
- pale-yellow takeaway: {r['takeaway']} #FFF4CC
- major visual nodes:
"""+'\n'.join(f"  {i+1}. {p['title']}；證據場景 {p['graphic']}" for i,p in enumerate(r['panels']))+f"""

## 輸入、方法、輸出與證據
{r['detail']}
來源：{r['source']}。保留WI-031已成立首讀，新工程圖各自有責任。共用圖元只保存相同工件，不用改名熱圖代替各方法。三段箭頭僅表示本頁實際資料或推論關係，D頁無跨方法因果箭頭。
生成模式：新建精確SVG再渲染PNG，桌機1672×941，手機768×2304。分類支架或分割細焊線按本圖身份固定，不冒充本輪模型實測。每模型先工程2原型，實看前不擴展；逐張原生與頁內尺寸另評。
權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。
PNG review pending；page review pending；user approval pending。
"""
 p.write_text(body,encoding='utf-8');results.append(v.validate(p))
(W/'batch3-preflight-validation.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
assert len(results)==28
print('Batch 3:',len(results),'preflights')

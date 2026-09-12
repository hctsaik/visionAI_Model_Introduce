from pathlib import Path
import json,re
W=Path(__file__).resolve().parent; C=W.parents[1]
def read(p):return json.loads(p.read_text(encoding='utf8'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
first={
'dinov2':'同一影像產生不同裁切與擾動視圖，分別交给 Teacher／Student 建立整圖與局部學習目標；這是預訓練資料處理，不是部署時替工件新增類別。',
'dinov3':'影像切成局部區塊後，由骨幹形成每個位置的特徵；Gram anchoring 在訓練中約束這些局部表示的相互關係，避免只保留整圖辨識而丟失局部結構。',
'clip':'預訓練使用影像與相應文字配對，讓配對表示更接近、未配對表示可區分；部署時再比較新影像與使用者指定的候選文字。',
'siglip':'準備配對及未配對的影像／文字，分別編碼成表示；訓練對每一對計算 sigmoid 目標，不把一組候選先正規化成加總為一。',
'llava':'將原圖與檢查問題作為兩種輸入：影像先轉成視覺特徵，問題則作為文字上下文；照片不會直接變成可靠的檢測結論。',
'qwen-vl':'將原始長銘牌和讀取問題交給選定版本的處理器；先保留可辨識的小字與左右布局，再依像素限制形成視覺序列。',
'gemini-vision':'把待查影像與明確的檢查問題放入請求，保留原圖識別；服務以這些條件產生候選回答，後續仍須人工回圖核對。',
'defectfill':'以少量真實刮傷照片及對應人工遮罩提供外觀和位置監督，再調整生成模型的部分權重；遮罩是準備資料的一部分，不是生成後自動得到的真值。',
'anomalydiffusion':'從少量帶遮罩的缺陷參考學外觀表示，另把目標遮罩編成位置條件；外觀與位置分開提供，才能嘗試在正常影像的新位置生成缺陷候選。',
'tf-idg':'提供正常金屬板、缺陷參考與目標遮罩；先把參考和正常圖反演到生成過程可使用的表示，再以外觀和形狀條件引導生成。',
'controlnet':'把金屬板外框與兩孔位置表示成輪廓條件圖，送入控制分支；文字描述補充外觀需求，輪廓圖提供空間布局線索。',
'inpainting':'保留原始照片並指定要改寫的遮罩區域；模型讀取周邊影像與可選文字條件，僅把輸出當用途已說明的填補候選。',
'diffusion-restoration':'把帶雜訊或模糊的觀測影像作為限制，依方法指定退化條件或觀測模型；復原要估計可能的清晰影像，原始觀測仍須保留。',
'deblur':'曝光期間工件位移會把同一邊緣累積到多個位置，形成拖影；先確認這種退化，再選用相應的反推或學習方法。',
'super-resolution':'低解析取像把細節合併成少量像素；以這張觀測及指定倍率作輸入，估計較高解析的候選，不能假設遺失細節已被唯一決定。',
'resnet':'先把工件影像依固定前處理送入網路，卷積逐步抽取特徵；已知類別由訓練資料定義，分類頭須與要區分的工件類別相符。',
}
extra={
'llava':{1:'視覺編碼器從原圖抽取特徵，保留可供問答使用的影像線索；這一步交出表示，不直接產生已驗證的檢測框。',2:'投影層把視覺特徵接到語言模型可使用的表示空間，和問題一起形成上下文，再生成文字回答；視覺語言對齊與指令資料幫助兩者合作。'},
'siglip':{2:'每個配對／未配對的目標共同更新影像與文字編碼器，讓兩種表示可比較；部署時的相似分數仍需現場驗證，不能當已校準的正確率。'},
'controlnet':{1:'經訓練的控制分支把輪廓條件轉成控制訊號，注入基礎去噪網路的對應層；條件提供布局限制，基礎模型的先驗仍影響外觀。',2:'去噪網路結合文字、輪廓控制與目前含噪表示，逐步形成影像候選；若新增條件類型或適配產業資料，需準備相應資料並訓練控制分支。'},
'inpainting':{2:'模型在原圖周邊、遮罩與其他條件下逐步形成填補區，再依管線解碼及合成；遮罩外是否精確保留需逐像素核對，填補紋理不是新觀測證據。'},
'super-resolution':{1:'插值以鄰近像素估算新增位置，使輪廓較平滑；它不會憑空恢復感測器未記錄的細節，可作為比較基準。',2:'學習方法利用影像先驗與低解析觀測估計細邊緣；SR3 以逐步去噪產生候選，前饋方法可一次輸出。使用前核對倍率與退化條件，新增紋理仍需獨立證據。'},
'resnet':{1:'直接路徑保留輸入特徵，卷積分支學殘差，兩路相加形成下一層表示；尺寸或通道不同時需投影匹配，不能任意相加。',2:'分類頭把整張工件 ROI 的特徵轉成已知類別分數，交由分流規則或人工覆核；預訓練只是起點，仍要用現場類別資料調整與驗證，不直接提供每件輪廓。'},
}
changed=[]
for id,body in first.items():
 p=C/f'_course_content/topics/{id}.json';d=read(p)
 for i,b in {0:body,**extra.get(id,{})}.items():
  step=d['mechanism_steps'][i];step['body']=b
  step['why']='核對本步輸入與輸出，才能判斷下一步是否接得上。'
  if 'diagram' in step:step['diagram'].update(title=step['title'],body=b,why=step['why'])
 write(p,d);changed.append(id)
p=C/'_course_content/topics/det-dino-detector.json';d=read(p)
steps=[('訓練準備真值','訓練影像提供要學的物件類別與框。真值用於監督一般偵測查詢，也用於建立帶噪的訓練輔助查詢。'),('正負去噪訊號','訓練時對真值類別及框加入擾動；較接近真值的正查詢學重建原物件，較遠的負查詢學背景，幫助模型區分相近候選。這個輔助分支在正式推論時移除。'),('影像初始化與正式推論','Mixed query selection 從影像特徵候選選位置初始化，搭配可學內容查詢，再更新類別與框。這是一般偵測查詢的初始化方式；推論只讀影像，不用真值框或去噪輔助查詢。')]
for step,(title,body) in zip(d['mechanism_steps'],steps):
 step.update(title=title,body=body,why='分清訓練輔助分支與一般偵測流程，避免把真值當作推論輸入。');step['diagram'].update(title=title,body=body,why=step['why'])
d['engineering_slides'][2]['label']='訓練時如何學會區分'
d['poc']['steps'][1]='在相同保留工件上比較 DINO 與既有固定類別偵測器；記錄標註／微調成本、輸入尺寸與查詢數，量包含前後處理和人工覆核的完整延遲。新增類別或改取像時重新驗證。'
write(p,d);changed.append('det-dino-detector')
p=C/'_course_content/topics/yolo-world.json';d=read(p)
bodies=['將選定詞彙交給文字編碼器形成表示；固定詞彙可提前計算並重用，改詞彙或模型版本後要更新並重驗。','預訓練學到視覺區域與語言的關係；模型利用文字表示參與影像特徵整理及區域比對。部署可重參數化重用固定詞彙資訊，並非每張圖都必須重跑文字編碼。','將影像區域與選定詞彙的表示比對，輸出候選框、類別與分數；候選詞不是完整業務規則，尺寸、輪廓或品質仍需其他方法。']
for step,body in zip(d['mechanism_steps'],bodies):step['body']=body;step['diagram']['body']=body
write(p,d);changed.append('yolo-world')
p=C/'_course_content/topics/yoloe.json';d=read(p);step=d['mechanism_steps'][3];step['why']='範例含背景或取像改變都可能讓提示偏離目標；把遮罩邊緣對回原圖，才能判斷是提示、取像還是分割需要改善。';step['diagram']['why']=step['why'];write(p,d);changed.append('yoloe')
# Keep a uniform purpose for the six detector-card introductions, not identical text.
p=C/'_course_content/learner-briefs.json';d=read(p)
for id,firstline in {'det-dino-detector':'固定類別且能準備框標註時，如何比較 DINO 的漏檢與完整成本？','det-yolo-dense':'固定類別的逐件偵測，如何核對密集候選、篩選與漏件成本？','det-rtdetr':'需要逐件框時，如何比較免 NMS 設計的準確度與完整延遲？','det-grounding-dino-interface':'類別名稱經常變更時，文字提示產生的候選框能否满足現場需求？','yolo-world':'常換候選詞彙時，如何驗證文字偵測的漏檢與詞彙更新成本？','yoloe':'需要文字或範例提示與遮罩時，如何核對提示品質及分割邊界？'}.items():d[id]['first']=firstline
write(p,d)
for p in (C/'_batch_specs').glob('*.json'):
 d=read(p)
 def contract(x):
  if isinstance(x,dict):
   if x.get('slug')=='det-dino-detector':x['takeaway']='類別固定且能準備框標註時，可比較 DINO；以現場漏檢、定位與完整成本決定是否採用。'
   for v in x.values():contract(v)
  elif isinstance(x,list):
   for v in x:contract(v)
 old=json.dumps(d,ensure_ascii=False);contract(d)
 if old!=json.dumps(d,ensure_ascii=False):write(p,d)
# Proofread text leaves only. Paths, IDs and source links retain exact identity.
replacements={'训练时':'訓練時','共同输入与物件外观不变。语意':'共同輸入與物件外觀不變。語意','说明':'說明','时间':'時間','纹理':'紋理','给':'給','满足':'滿足','先选':'先選'}
edits=[]
def proof(x,path=''):
 if isinstance(x,dict):return {k:(v if k in {'id','image','mobile_image','path','source','slug','anchor','modelPath','manifestPath'} or k.endswith('_path') else proof(v,path+'.'+k)) for k,v in x.items()}
 if isinstance(x,list):return [proof(v,path+f'[{i}]') for i,v in enumerate(x)]
 if isinstance(x,str):
  old=x
  x=re.sub(r'\s*r01實看修正：[^。]*。','',x)
  for a,b in replacements.items():x=x.replace(a,b)
  if x!=old:edits.append(dict(field=path,before=old,after=x))
 return x
for p in [*sorted((C/'_course_content/topics').glob('*.json')),C/'_course_content/learner-briefs.json']:
 d=read(p);new=proof(d,p.name)
 if new!=d:write(p,new)
p=C/'_course_content/poc-workbench.js';p.write_text(p.read_text(encoding='utf8').replace('先选','先選'),encoding='utf8')
write(W/'content-changes.json',dict(mechanism_topics=changed,wording_edits=edits))
print('Updated mechanism topics:',len(changed),'wording leaves:',len(edits))

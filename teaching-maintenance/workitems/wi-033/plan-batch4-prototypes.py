from pathlib import Path
import json,importlib.util
W=Path(__file__).resolve().parent;C=W.parents[1]
rows=json.loads((W/'engineering-plan.json').read_text(encoding='utf-8'))
defs=[
('det-yolo-dense','YOLOv8式：候選重複，按分數去重','NMS整理重複框，最後仍要回原圖查漏件。', [('同一影像產生四個候選','b4-yolo-candidates'),('分數排序，再比重疊','b4-yolo-nms'),('保留A與B的兩個框','b4-yolo-output')],'同一PCB有103與272兩顆電阻；A有三個重複候選，分數0.93/0.87/0.76，B為0.91。教學例採同類別NMS，A的候選IoU超過0.5，因此依分數保留A0.93與B0.91。門檻和分數為給定算例，不是模型推論。這裡限定YOLOv8式密集偵測，不推廣到所有YOLO版本。','https://docs.ultralytics.com/models/yolov8/'),
('det-rtdetr','RT-DETR：訓練分工，推論逐步修框','一對一匹配是訓練責任，推論仍需篩選與核對。',[('訓練：query對應真值','b4-rt-match'),('推論：從起點框逐步調整','b4-rt-refine'),('輸出框與分數，沒有NMS','b4-rt-output')],'训练时一對一匹配讓不同query學不同物件，沒有匹配的query學背景。推論不讀真值：混合編碼與query選擇提供起點，decoder反覆取影像線索更新框。示意q1對A、q2對B、q3未過分數篩選。省去NMS不代表無門檻、零重複或固定更快。','https://arxiv.org/abs/2304.08069'),
('det-grounding-dino-interface','Grounding DINO：詞與區域共同定位','文字参与候選和解碼，交付詞語與框。',[('影像與文字各自編碼','b4-ground-input'),('詞token與區域交換訊息','b4-ground-align'),('詞引導query，解碼成框','b4-ground-output')],'以同PCB的resistor文字查詢；影像特徵與文字token在feature enhancer互動，language-guided query selection挑相關起點，cross-modality decoder再利用兩種表示修框。圖中詞區域數字是相容性教學例，不是置信度實測。輸出詞語相關分數及框，並非像素遮罩。','https://arxiv.org/abs/2303.05499'),
('yoloe','YOLOE：圈選範例，聚合成提示表示','提示區域變成表示，再與待測區域比較。',[('參考圖圈出電阻A','b4-ye-roi'),('SAVPE按啟動權重聚合','b4-ye-pool'),('待測圖交出框與遮罩','b4-ye-output')],'本圖限定視覺提示模式SAVPE。語意特徵與ROI啟動分支產生加權聚合，例用兩位置[2,0]/[0,2]及0.75/0.25得到[1.5,0.5]解釋聚合，非真實模型維度或權重。提示表示與待測區域表示比對，A/B可同類相似，不等於相同料號。文字RepRTA和免提示LRPC是其他模式，不畫成必須順序執行。','https://arxiv.org/abs/2503.07465'),
('dinov2','DINOv2：先學表示，部署再抽特徵','訓練的Teacher目標與部署的骨幹要分開。',[('同一支架產生不同視圖','b4-dino-views'),('Teacher提供目標給Student','b4-dino-learn'),('部署只抽取整圖與局部特徵','b4-dino-deploy')],'DINOv2組合整圖自蒸餾及局部遮蔽目標等訓練設計；Teacher用Student權重的EMA更新，目標停止梯度，Student學對齊表示而非重建原像素。部署使用選定的預訓練骨幹抽整圖和patch表示，下游分類、查庫或分割另接。圖中支架與數值皆教學示意，未重跑模型。','https://arxiv.org/abs/2304.07193'),
('llava','原版LLaVA：把影像表示接進語言模型','投影橋接影像與文字，回答仍要有可見證據。',[('同一接頭影像經視覺編碼','b4-llava-encode'),('投影後與問題文字一起送入','b4-llava-project'),('語言模型逐token產生回答','b4-llava-answer')],'以原版LLaVA為界：預訓練視覺編碼器輸出表示，學習線性投影接入語言模型的embedding空間，再與問題文字共同產生回答。圖內小向量僅說明不同維度的橋接，不是該模型實際維度。右側空螺絲座支持未見螺絲，不能推出漏裝或振動鬆脫等原因。','https://arxiv.org/abs/2304.08485'),
('qwen-vl','Qwen2-VL：可變token也保留位置','動態解析度與位置編碼，仍受原像素限制。',[('不同長寬比形成不同token數','b4-qwen-dynamic'),('M-RoPE保留時空位置','b4-qwen-position'),('與問題一起讀出可見文字','b4-qwen-answer')],'限定Qwen2-VL：Naive Dynamic Resolution讓不同輸入形成可變視覺token數；M-RoPE將時間、高度、寬度位置納入旋轉位置表示，文字使用相應的一維位置處理。小格數為示意；像素預算/處理器限制仍會丟失小字。圖示同標籤批號B08，沒有從模糊B0?補造答案。','https://arxiv.org/abs/2409.12191'),
('gemini-vision','Gemini影像介面：請求、回覆、查證','JSON能解析，只代表格式；內容仍要對原圖。',[('固定影像、問題與欄位要求','b4-gemini-request'),('服務回傳可解析的JSON','b4-gemini-json'),('逐欄回原圖查可見證據','b4-gemini-check')],'依公開Gemini API說明輸入/輸出，不臆測私有編碼器。以同一左右圓接頭，左有螺絲右空座，示意JSON先錯填兩側present；解析成功後逐欄對照原圖，右側應記not_visible且原因unknown。所有回覆為作者設計反例，未呼叫API；實際部署另固定可用模型、schema與輸入設定。','https://ai.google.dev/gemini-api/docs/structured-output')]
spec=importlib.util.spec_from_file_location('v',C/'tools/validate_teaching_preflight.py');v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
results=[]
for owner,title,take,panels,detail,source in defs:
 rid=owner+'-engineering-2'
 r=dict(id=rid,owner=owner,index=2,version='r01',title=title,takeaway=take,kind='C',mobile_height=2304,panels=[dict(title=a,graphic=b) for a,b in panels],steps=[],detail=detail,source=source,terms=['表示：模型由輸入得到的中間資料，並非標註真值。','本圖數值：作者給定的教學示意，不是本輪模型實測。'],review='pending')
 if not any(x['id']==rid for x in rows):rows.append(r)
 path=W/(rid+'-r01.md')
 body='# '+title+'\n- lesson objective: '+take+'\n- page type: C\n- primary reading path: '+' → '.join([a for a,b in panels]+[take])+'\n- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`\n- pale-yellow takeaway: '+take+' #FFF4CC\n- major visual nodes:\n'+'\n'.join(f'  {i+1}. {a}；{b}' for i,(a,b) in enumerate(panels))+'\n\n'+detail+'\n來源：'+source+'\n生成模式：新建精確SVG→桌機1672×941、手機768×2304 PNG；不編修既有點陣素材。已實看本批原主線的具體工件，保留PCB雙電阻、L支架與雙圓接頭的身份。各家族先原型實看再擴展其他工程；DINOv2/Gemini主反例另統一同件。\n權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。\nPNG review pending；page review pending；user approval pending。\n'
 path.write_text(body,encoding='utf-8');results.append(v.validate(path))
(W/'engineering-plan.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
(W/'batch4-prototype-preflight-validation.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
print('8 prototype preflights; other 24 engineering stories and 2 failure cases still pending')

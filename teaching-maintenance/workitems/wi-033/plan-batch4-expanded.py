from pathlib import Path
import json,importlib.util
W=Path(__file__).resolve().parent;C=W.parents[1]
p=W/'engineering-plan.json';rows=json.loads(p.read_text(encoding='utf-8'));proto={r['owner']:r for r in rows if r['index']==2 and r['panels'][0]['graphic'].startswith('b4-')}
def add(o,i,title,take,panels,detail,kind='C'):
 rid=f'{o}-engineering-{i}'
 if any(x['id']==rid for x in rows):return
 rows.append(dict(id=rid,owner=o,index=i,version='r01',title=title,takeaway=take,kind=kind,mobile_height=2304,panels=[dict(title=a,graphic='b4-'+b) for a,b in panels],steps=[],detail=detail,source=proto[o]['source'],terms=proto[o]['terms'],review='pending'))
add('det-yolo-dense',1,'YOLOv8式：從有標註的物件學出框','框與類別來自訓練，不能用熱點代替框。',[('同PCB逐件標類別與框','det-labels'),('多尺度特徵產生密集候選','yolo-dense'),('去重後交出兩件的位置','yolo-output')],'同PCB電阻A103/B272皆標resistor框；YOLOv8式骨幹與neck融合多尺度特徵，head預測類別與框，候選經門檻及NMS整理。輸出是影像框與類別，不是輪廓或物理尺寸；格位只示意候選位置。')
add('det-yolo-dense',3,'YOLO：去重設定也屬於交付條件','模型、前處理與門檻一起固定，再驗漏件。',[('縮放補邊後仍須映回','det-map'),('同類候選按門檻去重','yolo-nms'),('逐件核對漏框與重複框','det-audit')],'保留resize/letterbox映射、類別順序、權重、分數與IoU門檻。還原原圖座標後逐件驗漏框、重複與定位誤差，時間包括前後處理。圖中框分數為教學例，不是當前推論。')
add('det-yolo-dense',4,'YOLO與RT-DETR：同一PCB比較交付','比較逐件錯誤與完整延遲，不只看有無NMS。',[('同影像、類別與留出件','det-labels'),('YOLO：密集候選與NMS','yolo-candidates'),('RT-DETR：query直接交框','rt-output')],'共同任務與硬體下，各用相容前處理與已驗證門檻，比較漏框、重複框、定位、記憶體及端到端時間。RT-DETR省NMS不保證本機更快；YOLOv8式作合理可部署基準。','D')
add('det-rtdetr',1,'RT-DETR：query逐步定位各個物件','輸出是物件框；一對一匹配只在訓練使用。',[('同PCB有兩個標註框','det-labels'),('混合編碼後選query起點','rt-encode'),('decoder更新後輸出框','rt-output')],'多尺度骨幹特徵經高效混合編碼器，query選擇提供decoder的初始查詢；decoder利用影像特徵更新框與分數。一對一匹配用來訓練責任，不在推論讀標註真值。')
add('det-rtdetr',3,'RT-DETR：修框次數也要連品質驗','減少decoder層可改成本，不能預設品質不變。',[('固定影像與起點query','rt-encode'),('較少或較多次更新','rt-depth'),('交付原圖框並驗錯誤','det-audit')],'若使用的實作支援選擇decoder輸出層，可評較少更新的速度/精度取捨；需固定checkpoint、輸入與門檻，並在部署硬體實測。模型輸出映回原圖，不拿query分數當物理定位誤差。')
add('det-rtdetr',4,'RT-DETR與YOLO：比較工作代價','去掉NMS是一項設計，域內結果才決定取捨。',[('共同PCB與逐件驗收','det-labels'),('RT-DETR以query修框','rt-refine'),('YOLO以分數整理候選','yolo-nms')],'固定影像、類別、硬體與成本範圍，分別調整候選門檻並比較逐件錯誤。不能把training matching放進推論，也不能以NMS是否存在代替完整延遲測試。','D')
add('det-grounding-dino-interface',1,'Grounding DINO：用詞語指定想找什麼','文字可以引導定位，專業料號仍需另驗。',[('同PCB加上resistor查詢','ground-input'),('詞token與影像區域互動','ground-align'),('交付詞語相關的框','ground-output')],'開放詞彙偵測接受影像與文字，透過兩模態互動和語言引導query定位相關區域；輸出框與詞語相關分數。輸入resistor可說明想找的類別，不能保證辨識103/272的電性或料號。')
add('det-grounding-dino-interface',3,'Grounding DINO：提示詞也是設定','保存提示與門檻，框映回原圖後逐件核對。',[('固定查詢與模型設定','ground-prompt'),('詞與框門檻影響保留','ground-threshold'),('核對原圖框與漏件','det-audit')],'保存模型版本、提示詞、詞語門檻/框門檻和影像映射。文字變更可能改變候選，因此不能只保存圖片與框而漏提示；領域名稱與相似零件須獨立驗證。')
add('det-grounding-dino-interface',4,'文字偵測與專用偵測：同題試驗','類別常變可試文字提示，穩定任務可訓練專用頭。',[('同一PCB與驗收類別','det-labels'),('文字查詢resistor','ground-input'),('固定類別監督訓練','yolo-dense')],'開放文字查詢適合探索類別，但工業域詞語與小零件仍需驗。固定類別可比較標註訓練的專用YOLO/RT-DETR；以資料成本、漏框與部署成本選，而不把兩種模型串成必經流程。','D')
add('yoloe',1,'YOLOE：選一種提示模式來找物件','提示是任務入口，交付仍是框與遮罩。',[('文字或視覺ROI指定目標','ye-modes'),('視覺提示聚合成表示','ye-pool'),('與待測區域對應並輸出','ye-output')],'YOLOE支援文字、視覺與免提示等模式；此圖後兩步展示視覺SAVPE。不同提示機制是替代入口，不是每次先RepRTA再SAVPE再LRPC的固定順序。提示對應區域，不保證識別精確料號。')
add('yoloe',3,'YOLOE：把提示與結果一起留存','提示ROI、模式與權重都要可追溯。',[('參考圖與ROI固定版本','ye-roi'),('框與遮罩保持物件配對','ye-output'),('同件逐件核對與回存','ye-audit')],'視覺模式保存參考影像、ROI及提示處理設定，文字模式保存文字，免提示模式另記詞庫設定。所有模式都保存權重、前處理、門檻與輸出座標映射；查相似件誤報、漏件及遮罩邊界。')
add('yoloe',4,'YOLOE：提示方便，料號仍要查證','外觀相似可以被找出，精確規格需要其他證據。',[('兩顆電阻外觀相似','det-labels'),('範例A可找出A與B','ye-output'),('讀料號並核對工作規格','det-partnumber')],'以A103和B272為同類不同印字的反例：視覺提示可能同時匹配兩顆電阻，不代表它們可互換。精確料號可加OCR、標籤或專用分類且各自驗證；提示易用性不能替代工作驗收。','D')
add('dinov2',1,'DINOv2：先抽表示，再定義下游任務','骨幹交特徵，分類與異常判定還要另接。',[('同一L支架作輸入','dino-input'),('骨幹抽整圖與局部表示','dino-deploy'),('下游可分類或查庫','dino-downstream')],'DINOv2預訓練表示可支援整圖與密集下游；本身不是工廠缺陷分類規格。部署選定骨幹和前處理，抽特徵後才用標註頭或參考庫決定任務；圖中向量為示意。')
add('dinov2',3,'DINOv2：查庫必須使用相容特徵','換骨幹或前處理，舊庫不能直接混用。',[('正常支架建立參考庫','dino-bank'),('待測表示查同一特徵空間','dino-distance'),('把排名與原圖一起核對','dino-review')],'固定checkpoint、輸入縮放、正規化、所抽層與特徵彙整方式，參考庫與query必須相容。示意距離排名不等於缺陷概率；換設定需重建庫或驗證相容轉換，並用留出正常/異常評估。')
add('dinov2',4,'DINOv2：外观差異不等於不良','同件特徵受條件影響，判定要回到工作規格。',[('同一支架只改背景','dino-background'),('相似度分數仍可能改變','dino-shift'),('比較查庫與有標註任務頭','dino-downstream')],'控制同支架幾何與孔位，只改背景檢查表示是否穩定。特徵可能對背景、照明或小細節敏感，也可能忽略特定缺陷；需要下游資料決定允收。此反例與主要首讀統一為同L支架，不換成墊圈。','D')
add('llava',1,'LLaVA：影像與問題共同形成回答','可見描述與原因推測要分開交付。',[('固定同接頭及檢查問題','llava-encode'),('影像投影與文字共同輸入','llava-project'),('回答再對照可見部位','llava-answer')],'以原版LLaVA的投影橋接為界，不把所有家族版本當相同架構。固定接頭左有螺絲右空座，回答可描述右未見螺絲，但照片不能證明原因；所有回答為教學設計。')
add('llava',3,'LLaVA：原圖、問題與版本一起保存','回答要可追溯，錯誤與不確定都要留存。',[('固定影像前處理與問題','vlm-contract'),('要求左右分開描述','llava-answer'),('核對證據後交人工覆核','vlm-audit')],'保存checkpoint、processor、完整問題及生成設定，記錄原圖與回答。對同一接頭逐側查證，不能因句子流暢就放行；需要定位輪廓或自動放行時另建驗證，不把語言回答當校正後尺寸。')
add('llava',4,'LLaVA與專用視覺：先定義交付','可追問的回答與固定座位判定，各驗各的成本。',[('共同接頭與左右座位','vlm-scene'),('VLM回答可見描述','llava-answer'),('固定ROI可用專用分類','vlm-roi')],'同接頭若只問固定座位有無螺絲，可比較ROI分類或規則；若工作需要開放問題與說明，可評VLM。两者仍須影像證據、未知處理及漏判成本，不能只按模型大小決定。','D')
add('qwen-vl',1,'Qwen2-VL：讀文字也要保留位置','視覺token保留線索，回答仍須逐欄核對。',[('同一銘牌的可見批號','qwen-input'),('動態token加上位置表示','qwen-position'),('與問題共同讀出B08','qwen-answer')],'限定Qwen2-VL，以批號B08說明視覺與文字輸入共同讀取內容；M-RoPE保留時空位置，模型輸出形式依所用版本與提示。局部圖是原銘牌工作例的簡化，不代表實測OCR結果。')
add('qwen-vl',3,'Qwen2-VL：像素預算要與小字一起驗','節省token前，先確認關鍵字仍能看清。',[('固定銘牌與processor設定','qwen-budget'),('保留可讀字與不確定欄位','qwen-uncertain'),('逐欄驗文字與完整耗時','qwen-check')],'固定processor、像素上下限、長寬比、模型及生成設定。壓低像素預算可能失去小字；保存原圖並逐欄核對，輸入不清時可重拍或保留未知，不靠語言先驗補造批號。')
add('qwen-vl',4,'Qwen2-VL與OCR：按文字工作選型','固定欄位可試OCR，問答需求再比較VLM。',[('共同銘牌與批號真值','qwen-input'),('OCR讀固定欄位','qwen-ocr'),('VLM用問題讀同一欄','qwen-answer')],'共同原圖和欄位真值下比較OCR與VLM的字元錯誤、不確定處理、版面變化與延遲。VLM的描述能力不保證精確字串更可靠；兩者都須依原圖驗證，不編造工具勝負。','D')
add('gemini-vision',1,'Gemini Vision：交付可以核對的欄位','要求欄位能幫助核對，但不保證內容正確。',[('固定影像、問題與欄位','gemini-request'),('示意服務回覆JSON','gemini-json'),('回原圖核對每個欄位','gemini-check')],'只描述公開影像API的請求和回覆，未呼叫服務或猜測私有骨幹。固定同圓接頭，JSON可解析但右present是作者設計反例；用圖中右空座核對not_visible，原因unknown。')
add('gemini-vision',3,'Gemini Vision：格式與內容分開驗','版本、請求與回覆都保存，異常欄位交覆核。',[('保留請求版本與固定原圖','gemini-contract'),('先驗格式，再查可見內容','gemini-check'),('低可信與缺欄位交人工','vlm-audit')],'部署時固定可用模型標識、請求設定與schema，記錄服務版本變動和原始回覆。JSON/schema通過只證明格式，仍逐欄對照影像；低可信、拒答、缺欄位及服務失敗都需要可追溯處理。')
add('gemini-vision',4,'雲端VLM與專用模型：同件比較','按問題彈性、資料流與錯誤成本選擇。',[('共同圓接頭與檢查目標','vlm-scene'),('影像API產生可追問回覆','gemini-request'),('固定座位另評本機分類','vlm-roi')],'以相同接頭和允收定義比較雲端API與本機專用視覺；包含網路耗時、資料流、服務可用性、維護與逐項錯誤。不能將API便利性或固定格式當自動放行證據，也不虛構內部架構。','D')
spec=importlib.util.spec_from_file_location('v',C/'tools/validate_teaching_preflight.py');v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
out=[]
for r in rows:
 if r['owner'] not in proto or r['index']==2:continue
 path=W/(r['id']+'-r01.md')
 body=f"# {r['title']}\n- lesson objective: {r['takeaway']}\n- page type: {r['kind']}\n- primary reading path: "+' → '.join([x['title'] for x in r['panels']]+[r['takeaway']])+f"\n- named guide-conformant reference page: `teaching-images/vision-ai-model-selection/course-delivery/section-pages/01-geometry-alignment-measurement/images/final/GEO-02-common-contract_v01.png`\n- pale-yellow takeaway: {r['takeaway']} #FFF4CC\n- major visual nodes:\n"+'\n'.join(f"  {i+1}. {x['title']}；{x['graphic']}" for i,x in enumerate(r['panels']))+'\n\n'+r['detail']+'\n來源：'+r['source']+'\n模式：新精確SVG→1672×941及768×2304PNG；八家族原型已實看通過。三節點、單讀序，保留原有效主線與具體工件身份。\n權威：CLAUDE.md、IMAGE_STYLE_GUIDE.md、TEACHING_REVIEW_LOG.md、TEACHING_SCORING_RUBRIC.md、TEACHING_WEBPAGE_GUIDE.md。\nPNG review pending；page review pending；user approval pending。\n'
 path.write_text(body,encoding='utf-8');out.append(v.validate(path))
assert len(out)==24
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8');(W/'batch4-expanded-preflight-validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print('24 expanded preflights passed; main failure cases separate and pending')

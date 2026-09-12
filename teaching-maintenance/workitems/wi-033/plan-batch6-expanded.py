from pathlib import Path
import json,runpy
W=Path(__file__).resolve().parent;p=W/'engineering-plan.json';rows=json.loads(p.read_text(encoding='utf-8'));m=runpy.run_path(str(W/'plan-batch6-prototypes.py'));owners=[d[0] for d in m['defs']];proto={r['owner']:r for r in rows if r['owner'] in owners and r['index']==2}
def add(o,n,title,take,panels,detail,kind='C'):
 rid=o+'-engineering-'+str(n);assert not any(r['id']==rid for r in rows)
 rows.append(dict(id=rid,owner=o,index=n,version='r01',kind=kind,mobile_height=2304,title=title,takeaway=take,panels=[dict(title=a,graphic='b6-'+b) for a,b in panels],detail=detail,source=proto[o]['source'],terms=proto[o]['terms'],review='pending'))
add('ad-dinomaly',1,'Dinomaly：多类正常，共用重建路徑','共同訓練仍需逐產品驗證。',[('三種產品的正常資料','dino-data'),('固定骨幹，更新重建路徑','dino-train'),('位置差異交原圖覆核','ad-delivery')],'固定DINOv2，多類正常共同訓練MLP及解碼器；位置差異是覆核線索。各類正常變化與真缺陷分開留出，不用整體平均掩蓋弱類。')
add('ad-dinomaly',3,'Dinomaly：訓練擾動，部署要關閉','保存層分組與eval設定，才可重現差異。',[('訓練Dropout，推論關閉','dino-drop'),('保存重建與分組版本','dino-contract'),('按產品驗誤報和漏檢','class-validation')],'保存骨幹、MLP、解碼器、使用層和分組、前處理及評分。Dropout只於訓練；放鬆逐層配對與難位置訓練策略不等於省略驗證。部署需eval，變更分組後重新驗。')
add('ad-dinomaly',4,'Dinomaly：低重建差，不保證無刮傷','限制照抄是手段，缺陷仍要用真例驗證。',[('同板刮傷p仍然存在','ad-scratch'),('若原與重建表示相同','dino-copy'),('獨立正常與缺陷分開驗','ad-validate')],'給定原與重建表示同為[.6,.8]，餘弦差0；原圖刮傷仍在。Dropout和線性注意力針對照抄捷徑，不保證每个缺陷有大差異。','D')
add('ad-invad',1,'InvAD：正常特徵教空間重建','重建表示回比原表示，提供檢查位置。',[('正常與驗證同件分開','ad-split'),('空間條件教逐階重建','inv-train'),('輸出位置分數及原圖','ad-delivery')],'2024 InvAD用多類正常訓練特徵反演，固定編碼器，更新條件和重建模組。輸入影像形成每尺度空間條件，交付特徵差圖與影像分數，非照片修復。')
add('ad-invad',3,'InvAD：SSM設定隨重建模型交付','特徵、空間條件和評分要配套。',[('保存特徵與SSM版本','inv-contract'),('逐位置縮放與偏移','inv-modulate'),('推論餘弦差再回原圖','inv-compare')],'保存編碼器、尺度融合與SSM、解碼器、標準化/前處理和評分。訓練MSE與推論餘弦差不能混為同一量；SSM指Spatial Style Modulation，不是Mamba。')
add('ad-invad',4,'InvAD：位置條件不能平均成一數','保留空間差異，才保留不同位置的調制。',[('同一z在p與q調制不同','inv-modulate'),('若平均條件，兩點都4.25','inv-average'),('仍需回原圖驗位置差異','ad-validate')],'給定p縮放2偏移1、q縮放.5偏移0，z=3得到7/1.5。若把兩位置條件平均成縮放1.25偏移.5，兩者都4.25，失去空間區別。本例只揭示平均的資訊損失，不是模型效能實測。','D')
add('ad-ddad',1,'DDAD：恢復估計作為檢查對照','正常資料教恢復，原圖保留作比較。',[('正常學習與真缺陷驗證分開','ad-split'),('去噪與特徵適配各有角色','dd-train'),('兩路差異供位置覆核','dd-compare')],'正常資料訓練擴散去噪與特徵適配，推論由待測影像引導恢復並比像素與特徵差。交付原圖、恢復估計及分數，R不能取代原圖作正常真值。')
add('ad-ddad',3,'DDAD：採樣成本要計完整流程','步數是設定，速度與檢查錯誤要一起驗。',[('固定步數、引導與隨機設定','dd-contract'),('成本隨去噪呼叫累積','dd-cost'),('同件留出驗位置與延遲','ad-validate')],'保存噪聲/採樣/引導強度、特徵適配和整合權重。給定每步4ms，20步80ms、50步200ms，只是去噪呼叫算例，未含前後處理；不保證增加步數提高檢測。')
add('ad-ddad',4,'DDAD：恢復若保留刮傷，也可能漏檢','恢復得像，不代表原圖沒有缺陷。',[('同板原刮傷位置p','ad-scratch'),('若R複製p，像素差為0','dd-copy'),('兩路分數仍要真例驗證','dd-compare')],'給定原p=40、恢復p=40，像素差0仍有刮傷；特徵差可能補充，也可能同樣小。原與恢復的相似並不是檢出證據，獨立驗漏檢。','D')
add('ad-winclip',1,'WinCLIP：文字與局部視窗檢查新件','固定模型仍要固定提示、取像與驗證。',[('同板待測p與正常留出','ad-split'),('人工文字狀態配局部視窗','win-task'),('交出可疑位置並回看原件','ad-delivery')],'目標零樣本WinCLIP以人工文字狀態和視窗表示評局部異常，無目標訓練仍須目標留出驗證。WinCLIP+可另加少量正常視覺參考，需明列實際使用模式。')
add('ad-winclip',3,'WinCLIP：零樣本與正常參考要分清','增加正常參考，資料與庫版本也成為設定。',[('人工提示與視窗固定','win-contract'),('加正常參考是WinCLIP+','win-reference'),('反光誤報與細傷漏檢分開驗','clip-errors')],'保存CLIP版本、人工提示、視窗尺度/聚合、前處理；WinCLIP+另外保存正常參考和視覺比對。不能用+的結果宣稱未用正常參考，也不把相似分數當概率。')
add('ad-winclip',4,'WinCLIP與AnomalyCLIP：提示來源不同','同件比較人工提示與學習提示的成本。',[('同板p與同一驗收題','ad-scratch'),('WinCLIP由人工組提示','win-prompts'),('AnomalyCLIP用輔助資料學提示','ac-train')],'兩方法均以CLIP語意與局部特徵提供異常線索；前者人工設計文字，後者使用輔助標註學物件無關提示。同資料與錯誤成本比較，不預設固定排名。','D')
add('ad-anomalyclip',1,'AnomalyCLIP：目標零樣本仍有學習來源','目標未訓練，提示曾由輔助資料學習。',[('輔助資料與目標板分開','ac-provenance'),('固定骨幹比已學兩狀態','ac-match'),('位置與整圖分數分工','ac-local')],'輔助正常/異常和局部標註學提示，目標類別未參與學習。保存提示來源，目標部署仍需驗漏檢/誤報；本輪沒有新訓練或推論。')
add('ad-anomalyclip',3,'AnomalyCLIP：學到的提示需要版本','提示、骨幹與局部注意力一起固定。',[('保存學習來源與提示','ac-contract'),('局部p對正常異常兩狀態','ac-match'),('正常反光與缺陷分開驗','clip-errors')],'保存輔助資料/切分、prompt checkpoint、骨幹、DPAM、前處理/分數設定。目標零樣本不免獨立驗證；更換提示或影像解析度都可能改變局部結果。')
add('ad-anomalyclip',4,'AnomalyCLIP：語意相似也可能看錯位置','可疑分數要能對回可見證據。',[('同板正常q與刮傷p','clip-pair'),('給定反例：q誤報，p漏檢','clip-errors'),('固定留出集比較兩提示法','clip-compare')],'正常孔反光q可能被判異常，細傷p可能未見；圖為作者反例，沒有模型分數。以同一取像、真值和允收成本比較人工與學習提示，不能只看文字描述流暢。','D')
add('frame-difference',1,'Frame Difference：找前後變化的位置','差分回答哪裡變了，物件數需另推論。',[('固定相機看同一方件','fd-frames'),('逐座標差異再過門檻','fd-threshold'),('兩條變化帶交後段處理','fd-bands')],'相鄰灰階前後相減取絕對值，再二值門檻。給定差80大於示意門檻30為前景，但0不亮；門檻不是建議值。不能直接把帶數當件數。')
add('frame-difference',3,'Frame Difference：相機與時間間隔要固定','不同取像條件，差異的原因也會改變。',[('保存前後時間与相機設定','fd-contract'),('全畫面變亮也會有差','fd-flash'),('停住物件兩幀差為0','fd-still')],'保存幀距、曝光、相機位置、ROI、灰階/門檻與後處理。曝光跳變或震動造成非物件運動差；靜止物件會消失於兩幀差。異常動作或缺陷判定須下游另作。')
add('frame-difference',4,'相鄰差分與背景相減：參考不同','同件停住，兩方法的時間記憶不同。',[('同一方件已停住','fd-still'),('前後相同：相鄰差為0','fd-zero'),('相對舊背景仍可能是前景','bg-compare')],'相鄰差分只比較選定兩幀；背景相減對歷史常態比較，初停物件可仍為前景，但背景更新後也可能被吸收。此差異不代表方法固定更準。','D')
add('background-subtraction',1,'背景相減：先建立场景常態','前景是相對背景的變化，不是物件類別。',[('多時間建立背景模型','bg-history'),('當前方件與背景比較','bg-compare'),('遮罩交後段定位與追蹤','bg-delivery')],'固定相機常用MOG2累積背景，交付前景mask。mask不自帶類別或永久ID；後段需處理陰影/雜訊、連通區或偵測與追蹤。')
add('background-subtraction',3,'背景相減：啟動與更新速度都要驗','先穩定背景，再評停留和光照變化。',[('起始背景尚不穩定','bg-warmup'),('更新快慢有不同取捨','bg-rate'),('部署保存狀態和陰影處理','bg-contract')],'相機重置或場景切换須重建背景。較快更新能適應變化，也可能較快吸收停留物；較慢更新可能留下照明變化前景。保存history/learningRate、陰影標籤處理與重置規則，實際驗證，不給固定適用參數。')
add('background-subtraction',4,'背景相減：物件沒動，不保證一直亮','背景模型會更新，遮罩不等於物件存在。',[('方件到場，先有前景','bg-compare'),('長期停留可能被吸收','bg-update'),('要保留物件身份，另接追蹤','bg-track')],'前景mask空不代表現場無物件。停留物件可能被模型吸收；需保存事件/狀態並視任務接偵測追蹤，而追蹤本身也有丟失限制。','D')
add('bytetrack',1,'ByteTrack：跨幀接身份，計數另定義','框先偵測，ID靠配對，過線再計數。',[('偵測器交每幀框與分數','byte-detections'),('高低兩輪續接身份','byte-match'),('ID7越線由下游記一次','byte-count')],'ByteTrack輸入逐幀偵測框、分數與時間順序；輸出追蹤ID和框。計數線、方向與重複事件政策在下游，單有追蹤不等於完成可靠計數。')
add('bytetrack',3,'ByteTrack：幀率與丟失緩衝要配套','驗完整影片的斷軌與重複計數。',[('保存偵測與關聯設定','byte-contract'),('同樣緩衝幀數，時間不同','byte-buffer'),('遮擋回來可能換ID','byte-switch')],'保存偵測器、分數/匹配門檻、幀率/時間順序、track_buffer與事件規則。給定30幀在30fps是1秒，在10fps是3秒；實作可能按fps縮放，須核對有效幀數。跨攝影機切換應重置，不能沿用不相關ID。')
add('bytetrack',4,'ByteTrack：低分框要有配對證據','孤立低分不能憑空建成可靠新物件。',[('ID7的低分框可接現有軌跡','byte-match'),('孤立低分框不新建ID','byte-isolated'),('新高分候選仍需確認','byte-new')],'低分再匹配使用剩餘未配對活動軌跡，孤立低分不直接建新ID。高分新候選也需依實作確認和後續續接；偵測誤框與長遮擋仍可能造成錯ID。','D')
out=[]
for r in rows:
 if r['owner'] in owners and r['index']!=2:
  f=W/(r['id']+'-r01.md');f.write_text(m['brief'](r),encoding='utf-8');out.append(m['v'].validate(f))
assert len(out)==24;p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8');(W/'batch6-expanded-preflight-validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
(W/'checkpoint-note.md').write_text('### WI-033 第六批24擴展preflight完成\n\n第六批r02原型渲染中，24擴展故事已定義並驗preflight；即將完成具體SVG場景，原型再審後生成。新增均為作者算例，保持原工件與時間身份；兩共用CLIP手機待做。完成33/52，使用者核准pending，全部52課繼續。\n',encoding='utf-8');runpy.run_path(str(W/'append-checkpoint.py'))

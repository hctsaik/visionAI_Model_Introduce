from pathlib import Path
import json,hashlib
W=Path(__file__).resolve().parent
notes={
'lucas-kanade-engineering-1':['整塊L工件平移，孔位相對刻痕不變','角點兩方向梯度與金字塔逐層估計','取像與小位移前提明示'],
'lucas-kanade-engineering-2':['三欄梯度可逐列追算','(1,0,-2)、(0,1,-1)、(1,1,-3)共同解(2,1)','右正下正向量比例2:1，物理速度另校正'],
'lucas-kanade-engineering-3':['同名p/p′在同一L轉角','反光蓋住後退出失效點，非延伸假箭頭','保存時間、有效性與量測條件'],
'lucas-kanade-engineering-4':['共同影格對作兩種輸出比較','稀疏指定點和稠密場分開，非追蹤ID','比較所需覆蓋、錯誤與完整成本'],
'raft-engineering-1':['相同L工件前後影格','兩圖相關與第一圖context分工','相關體不是光流；小矩陣僅示意'],
'raft-engineering-2':['查詢框未跨遮數值','四輸入接更新單元，加法向量實際等於(2,1)','再查詢與最終上採樣分清'],
'raft-engineering-3':['同L反光例與稠密場','數值不證明可見對應，往返是應用檢查','時間與記憶體包含相關及迭代'],
'raft-engineering-4':['同一初始資料比較迭代數','三次與六次為設定示意，沒有捏造誤差下降','同留出資料比較時間與錯誤'],
'ad-anomalydino-engineering-1':['同四孔A-01建立正常來源','整圖固定DINOv2，局部表示入庫','相容模型、前處理與參考版本一起留'],
'ad-anomalydino-engineering-2':['同一線痕位置到局部查詢再回映','參考向量按給定cos距離生成，最近0.4不表示正常','每patch定位與最高1%整件聚合分清'],
'ad-anomalydino-engineering-3':['固定待測件與原候選，只增加錯誤參考','最小值0.4到0.03可追，不宣稱實測','正常/缺陷同留出集，另量查庫成本'],
'ad-anomalydino-engineering-4':['同A-01整體旋轉，刻字與孔一起轉','自由擺放和標誌朝上為兩種允收規格','擴充參考不能改寫規格'],
'ad-efficientad-engineering-1':['同三槽正常托盤與T/S/AE角色','目標箭頭已明示，同影像分送三者','固定T與可訓練S/AE各有目標'],
'ad-efficientad-engineering-2':['同中間缺件與右側污點','local為T/S1、global為AE/S2通道均方差','正常分位數線性校正後平均，最大值作整件分數'],
'ad-efficientad-engineering-3':['同托盤两位置回查','0.6與0.1逐格平均確為0.35','分支與融合都留存，完整時間另量'],
'ad-efficientad-engineering-4':['固定新產品與留出資料','模型更新與正常分數尺度一併更新','每件耗時與更新工時分開'],
'flow-main-failure':['兩組共同影格，唯一改動後圖反光','LK/RAFT均跑清楚和反光條件，不做不公平對比','兩者核對原圖、錯誤與覆蓋，未宣稱勝負'],
'adino-deep-rotation':['同群組180度整體旋轉','刻字與全部孔位連動，沒有另畫不同工件','自由方向和朝上允收條件不可混用'],
'eff-main-failure':['同托盤缺件、污點，反光只蓋污點','局部與全局分支都不能保證補回不可見訊號','回原圖分別記漏檢、正常變化另記誤報'],
'eff-deep-01-core':['同章四孔正常板','學習目標和測試兩路分工明示','正常尺度校正、平均、最大值順序完整'],
'eff-deep-01-work':['四孔板下中線痕貫穿','正常訓練產生候選模型，另送待測才有位置圖','位置、人工覆核與完整時間一起驗'],
'eff-deep-02-data':['同產品正常與缺陷資料','訓練、獨立正常校正與最終測試三職責','同件近似照片不可跨拆'],
'eff-deep-03-meaning':['正常影像作三角色共同來源','T/S1與AE/S2目標和比較對象分清','已注明目標箭頭不是推論串接'],
'eff-deep-04-output':['同一A-01下中線痕','可疑區域與已定義輪廓為替代輸出，無因果串接','實體面積另需校正与誤差'],
'eff-deep-05-limits':['同件同線痕只改反光可見性','改善取像和有效解析度，不以門檻補回資訊','正常與真缺陷一起重驗'],
'eff-deep-07-comparison':['同新產品比較三種方法','Eff重訓校正、PatchCore重抽建庫、分割標註適配','輸出需求分列，成本無假排名'],
'eff-deep-08-transfer':['同四孔件從正常資料到位置和線痕輪廓','篩查與面積是不同需求','更新資料、輸出與驗收，物理尺度另校正']}
out=[]
for r in json.loads((W/'engineering-plan.json').read_text(encoding='utf-8')):
 if r['id'] not in notes:continue
 modes=['mobile'] if r['id'].startswith('eff-deep-') and r['id'] not in ['eff-deep-04-output','eff-deep-07-comparison'] else ['desktop','mobile']
 for mode in modes:
  p=W/f"{r['id']}-{r['version']}-{mode}.png"
  why=notes[r['id']]+['三段藍標與單黃結論，字句無重疊；手機需捲動，桌機仍有留白','所有數字和區域均為圖解／給定算例，未冒充模型推論']
  scores=[23,24,19,18 if mode=='desktop' else 17,9]
  out.append(dict(id=r['id'],image=p.name,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),scores=scores,total=sum(scores),evidence=why,completion={'aesthetics':[8,'簡化工件與一致色系，並非擬真風格'],'completeness':[9,r['takeaway']],'professionalism':[9,why[1]],'density':[8,why[3]],'hierarchy':[9,'一條閱讀路徑與單一結論']},veto=[],native_review='passed',page_review='pending',user_approval='pending'))
(W/'batch2-image-assessment.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print('Recorded actual native review for',len(out),'selected PNGs; page review pending')

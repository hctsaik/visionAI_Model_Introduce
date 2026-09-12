from pathlib import Path
import json,runpy
W=Path(__file__).resolve().parent
n=runpy.run_path(str(W/'plan-batch2.py'));add=n['add'];rows=n['rows'];owner='ad-efficientad'
def deep(id,title,end,panels,detail,kind='C'):add(owner,0,title,end,panels,detail,kind,rid='eff-deep-'+id)
deep('01-core','EfficientAD：局部特徵與整體重建合作','兩路分工不同，正常尺度對齊後一起驗。',[('正常影像讓三個角色學習','deep-eff-learn'),('局部T/S1，全局AE/S2','eff-two-diffs'),('正常驗證尺度對齊再融合','eff-calibrate')],'保留深讀核心的T/S/AE分工；手機改直向三段，用同章四孔板。學生第一組學T、AE學T、第二組學AE；T固定。local/global各自正常分位數校正後平均，最大值作整件分數；實測節拍另量。')
deep('01-work','先找可疑位置，也要能跟上工作','位置與耗時都要驗；熱圖只幫你開始覆核。',[('同一A-01有可見線痕','deep-board-input'),('從正常資料學候選模型','deep-eff-candidate'),('位置回原圖，完整流程計時','deep-board-review')],'重排深讀1章第二工作視圖；同一A-01四孔板與下中線痕，正常訓練、待測位置、人工覆核與端到端時間。圖解示意，不能替代實際缺陷驗證或量測。')
deep('02-data','正常資料要乾淨，也要涵蓋合理變化','訓練、校正與最終測試分開，先查資料來源。',[('已確認正常：用來訓練','deep-data-train'),('獨立正常：用來校正','deep-data-calibrate'),('正常與真缺陷：留作測試','deep-data-test')],'重排手機2章資料分工。已確認正常影像訓練學生/AE；未參與訓練的正常驗證影像建立分位數尺度；另留正常/真缺陷作最終測試。同一工件近似照片不可跨拆，單批資料不能代表全部產品變化。')
deep('03-meaning','三個角色，分清訓練目標與測試差異','T固定、S1學T、AE學T、S2學AE；兩路分別比較。',[('正常訓練：T教S1','deep-train-local'),('正常訓練：AE與S2','eff-train-global'),('測試：兩路比較對象','eff-two-diffs')],'手機3章明示三種訓練目標；箭頭為學習目標關係，AE與Student都是從同影像計算，並非Teacher輸出作AE模型輸入。測試local比較T與S1，global比較AE與S2。學生兩組輸出共享前層。')
deep('04-output','同一線痕，位置熱圖和輪廓回答不同問題','先選要位置還是輪廓，再準備資料與驗證。',[('共同原圖：下中線痕','deep-board-input'),('異常檢測：可疑位置','deep-output-location'),('監督分割：已定義輪廓','deep-output-contour')],'深讀4章同題比較，移除替代輸出之間的因果箭頭。固定同一A-01線痕；EfficientAD正常訓練得位置線索，監督分割需已定義目標的輪廓標註。若要實體面積另需校正與誤差驗證；圖中框與輪廓皆教學設定。',kind='D')
deep('05-limits','看不清的細痕，不能只靠調門檻','先改善取像，再用正常與真缺陷驗證。',[('共同原圖：可見線痕','deep-board-input'),('反光遮住相同位置','deep-board-glare'),('保留可見訊號再重验','deep-board-reacquire')],'重排深讀5手機：同一A-01與下中線痕，僅反光遮住線索。升門檻可能壓低正常誤報又漏掉細傷；先查取像、正常涵蓋及有效解析度，保留原圖重验。不可用新造熱圖冒充模型漏檢。',kind='D')
deep('07-comparison','換同一產品，三種方法各要準備什麼','比較同一用途與完整成本，更新時重做的事也要算。',[('EfficientAD：重訓與校正','deep-compare-efficient'),('PatchCore：重建正常特徵庫','deep-compare-patchcore'),('監督分割：標註與適配','deep-compare-seg')],'深讀7桌機手機各三段，固定同一新四孔板產品，EfficientAD更新學生/AE及正常分位數，PatchCore重抽特徵/coreset建庫並驗門檻，監督分割補目標輪廓標註與適配。前兩者位置篩查可同題比；分割輸出需求另列。比較資料工時、訓練/建庫、查詢/推論、記憶體、錯誤與覆核量，沒有共同實測不排名。',kind='D')
deep('08-transfer','需求從可疑位置變成刮痕面積','需求改變時，資料、輸出與驗收也要改。',[('目前：只有正常影像','deep-data-train'),('先篩查：找可疑位置','deep-output-location'),('改要面積：輪廓與校正','deep-transfer-area')],'重排深讀8手機；仍是同一四孔板與下中線痕。只有正常品可先比較EfficientAD/PatchCore作可疑位置篩查；若需求變為定義刮傷面積，補輪廓標註及分割验证，實體面積再需校正/誤差。條件不適合可換方法，不沿用熱圖當精密輪廓。',kind='D')
(W/'engineering-plan.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
with (W/'PLAN.md').open('a',encoding='utf-8') as f:f.write('\n即將生成EfficientAD深讀8組候選：1章核心/工作、2/3/4/5/7/8；4/7桌機手機都替换，其餘只啟用手機。第6可追算流程保留，所有章節正文與自測保留必要涵義。預期10張啟用PNG，尚未審查/整合。\n')
runpy.run_path(str(W/'plan-batch2.py'))

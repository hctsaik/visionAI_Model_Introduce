from pathlib import Path
import json,hashlib,runpy
W=Path(__file__).resolve().parent;m=runpy.run_path(str(W/'plan-batch7-prototypes.py'));owners=[d[0] for d in m['defs']]
rows=json.loads((W/'engineering-plan.json').read_text(encoding='utf-8'));out=[]
evidence=['門控.5×.4+.8×.5=.6；C/H與下一步輸入清楚分離。','tube位置一致；可見編碼、mask解碼與像素監督分開。','完整目標stop-grad/EMA；兩維L1=.15可追算。','淡傷A與深傷B同板同mask；LFS給定距離不當真實度。','原上方兩孔与大左下/小右下mask保持一致；弱區補強與結果核對。','模型權重固定與latent梯度更新分開，兩刮傷區位置一致。','白外框及雙孔形成條件；零初始化與後續可訓練分開。','同板黑污點、遮罩與編修對照；接縫/外部核對。','同板退化及先驗候選；兩像素平均同50說明非唯一。','同一直邊展寬與振鈴可見，独立清晰觀測分開。','矩形雙孔板固定左孔q；兩組子像素平均50可追算。']
for r in rows:
 if r['owner'] not in owners or r['index']!=2:continue
 ev=evidence[owners.index(r['owner'])]
 for mode in ['desktop','mobile']:
  f=W/f"{r['id']}-{r['version']}-{mode}.png"
  out.append(dict(id=r['id'],image=f.name,sha256=hashlib.sha256(f.read_bytes()).hexdigest(),scores=[23,24,18,18,9],total=92,evidence=[ev,'逐張原生實看；三節點單黃結論、caption與圖形分離。','幾何示意簡化，術語密度仍高；未做真人學習測試。'],completion=dict(aesthetics=[8,'簡化工件，主要身份與位置清楚'],completeness=[9,ev],professionalism=[9,'原論文機制與作者示例分開'],density=[8,'部分英文術語仍需正文支援'],hierarchy=[9,'三節點、一讀序、一結論']),veto=[],native_review='passed',page_review='pending',user_approval='pending'))
assert len(out)==22
(W/'batch7-prototype-image-assessment.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
(W/'checkpoint-note.md').write_text('### WI-033 第七批機制原生審查完成\n\n11課選定22PNG逐張原生實看，7課r02修正重審；逐圖自評92、完成度>=8且無否決項，證據batch7-prototype-image-assessment.json。即將定義33擴展故事與SR同件主反例，尚未渲染／整合或驗頁。完成仍41/52；使用者核准pending，全部52課持續。\n',encoding='utf-8');runpy.run_path(str(W/'append-checkpoint.py'))

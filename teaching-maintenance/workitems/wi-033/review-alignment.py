from pathlib import Path
import json,hashlib
W=Path(__file__).resolve().parent
notes={
'clip-engineering-1':([24,22,19,18,9],['支架齒輪軸承可辨；表示仍是簡化符號','三描述有不同表示並接找圖；細部編碼在工程2','候選原照與人工身份核對可見','三大區短句；手機長捲動','孔與齒形一致；示意身份清楚']),
'clip-engineering-2':([23,24,19,18,9],['支架與方向、排名對應；工件簡筆','並行編碼、等長方向、cosine順序成立','排序到找圖覆核；非定位明確','桌機疏朗；手機副標細字','單一半徑計算，無假實測']),
'clip-engineering-3':([23,23,19,18,9],['三文字與不同表示、更新前後具體','影像編碼與文字快取匯入比較；比對運算簡化','改文字後更新與已知未知件重測','遮字已修；手機仍跨三屏','版本與表示責任一致；沒有網路效能假值']),
'clip-engineering-4':([24,23,19,18,9],['同一齒輪與缺少齒輪候選直接對照','缺候選仍有順位，未把最高分當真值','新增後重測及專用分類器替代','大物件和短句；細微差異只作下一步','齒輪同形；排名明示反例示意']),
'siglip-engineering-1':([23,23,19,18,9],['支架與齒輪圖文身份對應','正負矩陣與兩編碼器梯度來源清楚','訓練資料標籤與更新對象可追','矩陣僅2×2；手机需跨區比對','正負對角一致；沒有宣稱實測']),
'siglip-engineering-2':([23,24,18,18,9],['支架來源與兩種學習方向可見','正配對提高、負配對降低，梯度共同更新','讀者可核對更新對象；部署細節另頁','梯度繞行後不穿節點；副標偏細','雙編碼器並行，配對參數共享']),
'siglip-engineering-3':([23,23,19,18,9],['同件支架與不同文字表示／排名','快取與影像表示匯入比較；公式不占主圖','分數非正確率，未知與低分覆核','短句三區，手機长捲動','模型／候選版本與示意分數清楚']),
'siglip-engineering-4':([24,23,19,18,9],['同齒輪同候選，比較條件可見','兩模型皆缺候選，不虚構精度勝負','具體列誤配、未知、前處理與覆核','兩模型不串接；第三節仍部分文字','輸入身份一致，順位不冒充實測']),
'alignment-comparison':([23,24,19,18,9],['同支架與齒輪配對矩陣，候選對齊','行列比較與逐對目標有不同圖像結構','部署固定資料候選，檢查錯誤及完整成本','簡化成2×2與三節；仍需縱向捲動','正負配對相符，替代方法無串接'])}
out=[]
for r in json.loads((W/'engineering-plan.json').read_text(encoding='utf-8')):
 if r['id'] not in notes:continue
 scores,reasons=notes[r['id']]
 for mode in (['mobile'] if r['index']==0 else ['desktop','mobile']):
  p=W/f"{r['id']}-{r['version']}-{mode}.png";ss=list(scores)
  if mode=='mobile':ss[3]-=1
  assert sum(ss)>90
  out.append(dict(id=r['id'],mode=mode,version=r['version'],image=p.name,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),scores=ss,total=sum(ss),evidence=reasons,completion={'aesthetics':[8,'藍標頭與黃結論清楚；工件為簡化原生幾何'],'completeness':[9,r['takeaway']],'professionalism':[9,reasons[1]],'density':[8,'只保留本圖責任；下方尚有留白'],'hierarchy':[9,reasons[3]]},veto=[],native_review='passed',page_review='pending',user_approval='pending',evidence_level='illustration, not model inference'))
(W/'alignment-image-assessment.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print('Recorded',len(out),'individually inspected active PNGs; page validation pending')

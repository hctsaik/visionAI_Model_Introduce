from pathlib import Path
import json
W=Path(__file__).resolve().parent;C=W.parents[1]
p=C/'_course_content/topics/ad-efficientad.json';t=json.loads(p.read_text(encoding='utf-8'))
old=t['mental_model']['limit'];new='同一托盤的右側污點被反光遮住，兩路都可能缺少可用線索；中間缺件仍可見，也必須另外驗證。異常熱圖不能補回看不見的資訊，污點與漏裝的驗證不可互相代替。'
def walk(x):
 if isinstance(x,str):return x.replace(old,new)
 if isinstance(x,list):return [walk(v) for v in x]
 if isinstance(x,dict):return {k:walk(v) for k,v in x.items()}
 return x
t=walk(t);p.write_text(json.dumps(t,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
mp=C/'roadmap-model-selection/anomaly-detection/ad-efficientad/model.md';s=mp.read_text(encoding='utf-8').replace(old,new)
mark='## WI-033 原論文運算對照'
if mark not in s:s+='\n'+mark+'\n\n原方法的學生有兩組輸出S1/S2，共享前層；AE由影像重建T特徵，S2學習AE輸出。測試local為T與S1逐位置通道均方差，global為AE與S2均方差。兩圖各用獨立正常驗證的分位數作線性校正，再取平均；整件分數取融合圖最大值。應用若更改融合或聚合方式，須列為額外變體，不當成原論文預設。來源：https://arxiv.org/html/2303.14535v3 。\n'
mp.write_text(s,encoding='utf-8')

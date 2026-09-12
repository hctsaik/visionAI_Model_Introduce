from pathlib import Path
import json,hashlib
W=Path(__file__).resolve().parent
notes={
1:([23,23,19,18,9],['同名A/B/C固定工件部位，三點只作示意','K/畸變、平面例與R/t責任分開','CAD單位、校正与解法須固定','三區可讀，軸旁Z=0較小','同形孔位與點名；無假解算數據']),
2:([24,24,18,18,9],['兩件同型支架保持位置','先框後點與未分組點到實例明顯不同','有身份2D點交付，PnP另頁','不串接替代法，手機兩組點仍可辨','A/B/C與物件1/2一致']),
3:([23,23,19,18,9],['觀測與投影重疊及各點殘差可見','R/t→相機投影→逐點比較；未把熱圖當姿態','保存身份、可見性、外參與單位','橘實心/綠空心圖例已修','示意殘差不冒充精確量測']),
4:([24,23,19,18,9],['同件缺口遮擋與相似孔洞','小殘差不能排除錯誤身份','標記/額外視角與校正節拍取捨','候選分區清楚，機制細節另頁','不以小分數直接放行'])}
out=[]
for row in json.loads((W/'engineering-plan.json').read_text(encoding='utf-8')):
 if row['owner']!='pose':continue
 ss,why=notes[row['index']]
 for mode in ['desktop','mobile']:
  p=W/f"{row['id']}-{row['version']}-{mode}.png";sc=list(ss)
  if mode=='mobile':sc[3]-=1
  out.append(dict(id=row['id'],image=p.name,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),scores=sc,total=sum(sc),evidence=why,completion={'aesthetics':[8,'藍頭黃結論，原生幾何較簡化'],'completeness':[9,row['takeaway']],'professionalism':[9,why[1]],'density':[8,'保留本圖責任，手機長捲動'],'hierarchy':[9,why[3]]},veto=[],native_review='passed',page_review='pending',user_approval='pending'))
(W/'pose-image-assessment.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')

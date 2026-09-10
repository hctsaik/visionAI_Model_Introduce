from pathlib import Path
import json
w=Path(__file__).resolve().parent
mapping=str.maketrans(dict(zip('与这图输结参较选实对应现线为标节库侧动变数处统务拟体张费发课组从进过真见证换断状态阶赖独给面积个点现两', '與這圖輸結參較選實對應現線為標節庫側動變數處統務擬體張費發課組從進過真見證換斷狀態階賴獨給面積個點現兩')))
for name in ['content.py','integrate.py']:
 p=w/name;s=p.read_text(encoding='utf-8').translate(mapping).replace('兩塊不同旋轉的L形件','兩塊L形件').replace('已找出L形件的影像點','已找出四孔U形件的影像點')
 p.write_text(s,encoding='utf-8')
p=w/'visual-plan.json';data=json.loads(p.read_text(encoding='utf-8'))
for r in data:
 if r['id']=='instance-d2':r['takeaway']='先查漏檢與分件，再把遮罩交給計數。'
p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Authored sources normalized')

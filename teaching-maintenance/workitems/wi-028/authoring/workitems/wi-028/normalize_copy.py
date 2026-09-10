from pathlib import Path
W=Path(__file__).resolve().parent
mapping=str.maketrans(dict(zip('与这图输结参较选实对应现线为标节库侧动变数处统务拟体张费发课组从进过真','與這圖輸結參較選實對應現線為標節庫側動變數處統務擬體張費發課組從進過真')))
for name in ['lesson-content.json','integrate.py']:
 p=W/name;s=p.read_text(encoding='utf-8');p.write_text(s.translate(mapping).translate(str.maketrans('见证换断状态阶赖独','見證換斷狀態階賴獨')),encoding='utf-8')
print('Normalized authored Traditional Chinese copy only')

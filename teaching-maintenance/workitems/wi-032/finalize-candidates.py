from pathlib import Path
import json,subprocess,sys,ctypes
W=Path(__file__).resolve().parent;C=W.parents[1]
fn=ctypes.windll.kernel32.LCMapStringW
def traditional(s):
 n=fn(0x0404,0x04000000,s,len(s),None,0)
 if not n:raise ctypes.WinError()
 buf=ctypes.create_unicode_buffer(n+1)
 if not fn(0x0404,0x04000000,s,len(s),buf,n):raise ctypes.WinError()
 return buf.value
assert traditional('图像与训练')=='圖像與訓練'
for name in ['lesson-content.json','engineering-plan.json','engineering-plan.py','render-engineering.py']:
 p=W/name;p.write_text(traditional(p.read_text(encoding='utf-8')),encoding='utf-8')
p=W/'engineering-plan.json';rows=json.loads(p.read_text(encoding='utf-8'))
r=next(r for r in rows if r['id']=='yolo-world-engineering-2')
r['detail']='以論文v3的RepVL-PAN為例，Text-guided CSPLayer把影像／詞彙相似經max與sigmoid形成權重，乘回影像特徵；Image-Pooling Attention另用池化的影像資訊更新文字表示。區域與詞彙相似度用於類別評分，框回歸另負責位置。圖只展開文字引導權重與區域比對，矩陣深淺為示意，不是實際權重輸出。部署版本可能省略或改寫模組，需按官方設定核對。'
r['source']='https://arxiv.org/html/2401.17270v3'
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
for r in rows:
 p=W/(r['id']+'-r04.md')
 p.write_text((W/(r['id']+'-r03.md')).read_text(encoding='utf-8')+'\n## r04 最終候選\n已依實圖修正對應、2D座標、八方向、正負分支及有標籤矩陣。桌機與手機原生／實頁核對仍需完成。來源：'+r['source']+'\n'+r['detail']+'\n',encoding='utf-8')
 subprocess.run([sys.executable,'-X','utf8',str(C/'tools/validate_teaching_preflight.py'),str(p)],check=True,stdout=subprocess.DEVNULL)
p=W/'render-engineering.py';s=p.read_text(encoding='utf-8').replace("+'-r03-'+mode","+'-r04-'+mode");p.write_text(s,encoding='utf-8')
print('Traditional Chinese and 24 r04 preflights ready; render next')

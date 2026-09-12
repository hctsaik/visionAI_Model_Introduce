from pathlib import Path
W=Path(__file__).resolve().parent
for name in ['qa-pages.py','qa-batch2-deep.py']:
 p=W/name;s=p.read_text(encoding='utf-8')
 if 'from stable_image import READY' not in s:s='from stable_image import READY\n'+s
 s=s.replace("'(i)=>i.decode()'",'READY')
 s=s.replace("'(i)=>i.tagName===\"IMG\"?i.decode():new Promise(r=>i.contentDocument?.documentElement?r():i.addEventListener(\"load\",r,{once:true}))'",'READY')
 p.write_text(s,encoding='utf-8')

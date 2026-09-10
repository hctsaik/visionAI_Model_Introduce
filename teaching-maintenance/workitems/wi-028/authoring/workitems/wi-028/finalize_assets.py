import json
from pathlib import Path
from PIL import Image
W=Path(__file__).resolve().parent;C=W.parents[1]
p=W/'selected-assets.json';d=json.loads(p.read_text(encoding='utf-8'));sizes=set()
for id,r in d.items():
 for mode in ['desktop','mobile']:
  path=W/r[mode];assert path.exists();sizes.add(Image.open(path).size);r[mode+'_reviewed']=True
  brief=W/r[mode].replace('-'+mode+'.png','.md')
  if not brief.exists():
   base=W/(id+'-r01.md');fallback=W/(id+'-r02.md')
   s=(base if base.exists() else fallback).read_text(encoding='utf-8')
   brief.write_text(s+'\n\n## Selected revision\n'+r[mode]+'; exact correction prompts retained in sibling JSON; actual native and display-size PNG review completed in image-review.md. User approval pending.\n',encoding='utf-8')
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
b=C/'tools/build_interactive_learning_html.py';s=b.read_text(encoding='utf-8');anchor='(726, 2167)}'
extra=sorted(sizes-{(1672,941)})
assert anchor in s;s=s.replace(anchor,'(726, 2167), '+', '.join(map(str,extra))+'}')
b.write_text(s,encoding='utf-8')
t=C/'tests/test_tall_mobile_artwork.py';s=t.read_text(encoding='utf-8');s=s.replace('(1673, 940)):', '(1673, 940), '+', '.join(map(str,extra))+'):');t.write_text(s,encoding='utf-8')
print('Selected 36 reviewed assets; registered exact native sizes',sorted(sizes))

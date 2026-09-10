import json,sys
from pathlib import Path
from PIL import Image
W=Path(__file__).resolve().parent
for slug in sys.argv[1:] or json.loads((W/'lesson-content.json').read_text(encoding='utf-8')):
 # Evidence-only collage, no resizing and no teaching asset modification.
 d=Image.open(W/f'final-{slug}-1440-core.png').crop((304,0,1440,1000))
 m=Image.open(W/f'final-{slug}-360-core.png')
 out=Image.new('RGB',(d.width+m.width,max(d.height,m.height)),'white');out.paste(d,(0,0));out.paste(m,(d.width,0));out.save(W/f'page-review-{slug}-core.png')
 panels=[Image.open(W/f'final-{slug}-360-{part}.png') for part in ['top','operations','quiz']]
 out=Image.new('RGB',(sum(p.width for p in panels),max(p.height for p in panels)),'white');x=0
 for p in panels:out.paste(p,(x,0));x+=p.width
 out.save(W/f'page-review-{slug}-reading.png')
print('Evidence panels saved at original display scale')

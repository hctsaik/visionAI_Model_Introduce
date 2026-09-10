from pathlib import Path
from PIL import Image
W=Path(__file__).resolve().parent; O=W/'size-views';O.mkdir(exist_ok=True)
for p in W.glob('*.png'):
 im=Image.open(p);w=328 if 'mobile' in p.name else 936
 im.resize((w,round(im.height*w/im.width)),Image.Resampling.LANCZOS).save(O/p.name)
 print(p.name,im.size)

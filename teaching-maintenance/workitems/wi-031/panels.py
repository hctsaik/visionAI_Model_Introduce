import sys
from pathlib import Path
from PIL import Image
W=Path(__file__).resolve().parent
for slug in sys.argv[1:]:
 O=W/'pages'/slug
 for kind,pattern in [('desktop','1440-v*.png'),('mobile','360-v*.png'),('engineering','1440-engineering-*.png')]:
  paths=sorted(O.glob(pattern))
  for n in range(0,len(paths),2):
   imgs=[Image.open(p).convert('RGB') for p in paths[n:n+2]]
   out=Image.new('RGB',(sum(i.width for i in imgs),max(i.height for i in imgs)), 'white');x=0
   for i in imgs:out.paste(i,(x,0));x+=i.width
   out.save(O/f'panel-{kind}-{n//2+1}.png')
print('Saved evidence panels without resizing teaching figures')

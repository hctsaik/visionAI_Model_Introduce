"""Original SVG teaching diagrams. Raster assets are not edited by this tool."""
from pathlib import Path
import json,math,asyncio,sys,html
from playwright.async_api import async_playwright
W=Path(__file__).resolve().parent
B='#1765CA';N='#172B43';G='#238854';O='#CE7917';L='#B9D4EF';PALE='#F5F9FF'
def rect(x,y,w,h,fill=PALE,stroke=L,r=12):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
def text(x,y,s,size=27,col=N,weight=500,anchor='start'):return f'<text x="{x}" y="{y}" font-size="{size}" fill="{col}" font-weight="{weight}" text-anchor="{anchor}">{html.escape(str(s))}</text>'
def line(x,y,xx,yy,col=B,sw=4,dash=False):return f'<line x1="{x}" y1="{y}" x2="{xx}" y2="{yy}" stroke="{col}" stroke-width="{sw}"'+(' stroke-dasharray="7 7"' if dash else '')+'/>'
def arrow(x,y,xx,yy,col=B,sw=5):
 a=math.atan2(yy-y,xx-x);p=[(xx,yy),(xx-14*math.cos(a)+7*math.sin(a),yy-14*math.sin(a)-7*math.cos(a)),(xx-14*math.cos(a)-7*math.sin(a),yy-14*math.sin(a)+7*math.cos(a))]
 return line(x,y,xx,yy,col,sw)+'<polygon points="'+' '.join(f'{a:.1f},{b:.1f}' for a,b in p)+'" fill="'+col+'"/>'
def circle(x,y,r=8,col=B,fill=None):return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill or col}" stroke="{col}" stroke-width="3"/>'
def group(x,y,s,body):return f'<g transform="translate({x},{y}) scale({s})">{body}</g>'
def plate(x,y,s=1,defect=False,points=False):
 a='<path d="M0,0 H95 L120,35 H250 V160 H0 Z" fill="url(#steel)" stroke="#73899E" stroke-width="4"/>'
 for xx in [60,190]:a+=circle(xx,102,24,'#73899E',PALE)
 a+=line(14,18,75,18,'#FFFFFF',6)
 if defect:a+='<path d="M137,50 l-12,18 18,11 -11,20" stroke="#B94C42" stroke-width="6" fill="none"/>'
 if points:
  for xx,yy,label in [(95,0,'A'),(60,102,'B'),(190,102,'C')]:a+=circle(xx,yy,7,O)+text(xx+10,yy-10,label,24,O,700)
 return group(x,y,s,a)
def feature(x,y,values,col=B):
 return ''.join(rect(x+26*i,y,21,45*abs(v),col if v>0 else L,'none',2) for i,v in enumerate(values))
def pill(x,y,w,label,col=B):return rect(x,y,w,43,col,col,12)+text(x+w/2,y+30,label,26,'white',700,'middle')
def bars(labels,values):
 out=''
 for i,(lab,v) in enumerate(zip(labels,values)):
  yy=45+i*100;out+=text(15,yy,lab,29)+rect(150,yy-27,250,30,'#E4EDF7','none',3)+rect(150,yy-27,250*v,30,B if i==0 else '#8AB2DE','none',3)+text(420,yy,str(round(v,2)),27,B)
 return out
def graphic(k):
 if k.startswith('b7-'):
  from batch7_graphics import graphic as batch7
  return batch7(k)
 if k.startswith('b6-'):
  from batch6_graphics import graphic as batch6
  return batch6(k)
 if k.startswith('b5-'):
  from batch5_graphics import graphic as batch5
  return batch5(k)
 if k.startswith('b4-'):
  from batch4_graphics import graphic as batch4
  return batch4(k)
 if k.startswith('b3-'):
  from batch3_graphics import graphic as batch3
  return batch3(k)
 if k=='clip-dual':
  a=plate(10,30,.47)+text(10,145,'支架影像',25)+arrow(140,75,178,75)+pill(187,45,190,'影像編碼器')+arrow(385,75,420,75)+group(430,53,.65,feature(0,0,[.6,1,.3],B))
  a+=text(15,285,'支架／齒輪／軸承',25)+rect(10,183,127,46,'white',L,8)+text(22,216,'文字候選',24,G)+arrow(140,206,178,206,G)+pill(187,182,190,'文字編碼器',G)+arrow(385,206,420,206,G)
  for j,vals in enumerate([[1,.5,.8],[.3,1,.2],[.8,.4,1]]):a+=group(430,167+j*34,.65,feature(0,0,vals,G))
  return a+text(15,337,'兩路各自編碼',31,B,700)+text(15,383,'向量先正規化，再比較',28)
 if k=='cosine':
  a=line(70,290,440,290,L,2)+line(70,290,70,35,L,2)
  for deg,col,label in [(0,B,'影像'),(15,G,'支架'),(60,O,'齒輪'),(80,'#7B81B4','軸承')]:
   xx=70+240*math.cos(math.radians(deg));yy=290-240*math.sin(math.radians(deg));a+=arrow(70,290,xx,yy,col,5)+text(xx+10,yy+5,label,27,col)
  return a+text(15,350,'方向接近 → 相似度較高',29)+text(15,396,'二維教學例，非實測特徵',25)
 if k=='clip-rank':return bars(['支架','齒輪','軸承'],[.97,.5,.17])+line(15,320,475,320,L,2)+text(15,367,'先找相關照片，再核對原圖',27)+text(15,410,'排名不提供缺陷位置',28,O)
 from alignment_graphics import graphic as alignment
 try:return alignment(k)
 except ValueError:
  from semantic_graphics import graphic as semantic
  try:return semantic(k)
  except ValueError:
   from gpt_mobile_graphics import graphic as gpt_mobile
   try:return gpt_mobile(k)
   except ValueError:
    from batch2_graphics import graphic as batch2
    return batch2(k)
def split(s,n=18):
 if len(s)<=n:return [s]
 cut=s.find('：')+1
 if cut<3 or cut>n:
  comma=s.rfind('，',6,n)
  cut=comma+1 if comma>=6 else n
 if len(s)-cut<=2:cut=max(8,len(s)//2)
 return [s[:cut]]+split(s[cut:],n)
def make(row,mobile):
 w,h=(768,row.get('mobile_height',2400)) if mobile else (1672,941)
 s=f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><defs><linearGradient id="steel"><stop stop-color="#A1B2C3"/><stop offset=".43" stop-color="#E2EAF1"/><stop offset="1" stop-color="#8B9DAF"/></linearGradient></defs><style>text{{font-family:"Microsoft JhengHei",sans-serif}}</style>'+rect(0,0,w,h,'white','none',0)
 for i,v in enumerate(split(row['title'],18) if mobile else [row['title']]):s+=text(28,58+i*52,v,40 if mobile else 46,N,800)
 s+=text(28,165 if mobile else 117,'工程圖解｜教學示意，非模型實測',26,'#526B81')
 for i,p in enumerate(row['panels']):
  x,y,z=(50,195+i*((h-375)/3),1.24 if h<2400 else 1.3) if mobile else (25+555*i,163,1)
  a=rect(0,0,510,500,PALE,L,17)+pill(15,13,480,p['title'])+group(8,66,.965,graphic(p['graphic']))
  s+=group(x,y,z,a)
  if row['kind']=='C':
   if mobile and i<2:s+=arrow(w/2,y+500*z+3,w/2,y+(h-375)/3-3)
   elif not mobile and i<2:s+=arrow(x+518,y+225,x+542,y+225)
 if not mobile:
  for i,st in enumerate(row.get('steps',[])):s+=text(35+555*i,705,st,28,N,650)
 by=h-(180 if mobile else 136)
 s+=rect(24,by,w-48,150 if mobile else 108,'#FFF4CC','#EAB24B',15)
 s+=circle(58,by+40,15,'#D99B23','#FFE5A2')+rect(50,by+56,16,10,'#D99B23','none',2)
 for j,v in enumerate(split(row['takeaway'],20) if mobile else [row['takeaway']]):s+=text(89 if j==0 else 45,by+52+j*46,v,31 if mobile else 34,N,800)
 return s+'</svg>',w,h
async def main():
 rows=json.loads((W/'engineering-plan.json').read_text(encoding='utf-8'))
 ids=set(sys.argv[1:]);rows=[r for r in rows if not ids or r['id'] in ids]
 async with async_playwright() as p:
  b=await p.chromium.launch(channel='msedge',headless=True,args=['--disable-gpu'])
  for row in rows:
   for mode in ['desktop','mobile']:
    svg,w,h=make(row,mode=='mobile');dest=W/f"{row['id']}-{row.get('version','r01')}-{mode}.svg"
    assert not dest.exists(),'Version already exists: '+str(dest)
    dest.write_text(svg,encoding='utf-8');page=await b.new_page(viewport={'width':w,'height':h},device_scale_factor=1)
    await page.goto(dest.as_uri());await page.evaluate('document.fonts.ready');await page.wait_for_timeout(500)
    await page.screenshot(path=str(dest.with_suffix('.png')));await page.close()
  await b.close()
 print('Rendered',len(rows)*2,'candidate PNGs; actual review pending')
if __name__=='__main__':asyncio.run(main())

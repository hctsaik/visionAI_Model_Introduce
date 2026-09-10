from pathlib import Path
import html, json, math, asyncio, cv2, re
from playwright.async_api import async_playwright
W=Path(__file__).resolve().parent
N='#153454'; B='#1765CA'; O='#E98B1D'; G='#17876B'; L='#C1D8EF'
def text(x,y,s,size=30,color=N,weight=500,anchor='start'):
 return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}">{html.escape(s)}</text>'
def rect(x,y,w,h,fill='white',stroke=L,r=16):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
def line(x,y,x2,y2,col=B,width=4,dash=''):
 return f'<path d="M{x},{y} L{x2},{y2}" fill="none" stroke="{col}" stroke-width="{width}" stroke-dasharray="{dash}"/>'
def arrow(x,y,x2,y2,col=B):
 a=math.atan2(y2-y,x2-x); d=13
 return line(x,y,x2,y2,col,5)+f'<path d="M{x2},{y2} L{x2-d*math.cos(a-.45)},{y2-d*math.sin(a-.45)} L{x2-d*math.cos(a+.45)},{y2-d*math.sin(a+.45)} Z" fill="{col}"/>'
def board(x,y,scale=1,skew=0,rot=0,label=True):
 # Every cell, marker, and A share this board frame. No separately redrawn views.
 s=f'<g transform="translate({x},{y}) rotate({rot}) skewX({skew}) scale({scale})">'
 s+=rect(-10,-10,320,270,'#C7CDD3','#8793A0',5)+rect(0,0,300,250,'white','#647484',0)
 for row in range(5):
  for col in range(6):
   if (row+col)%2==1:s+=rect(col*50,row*50,50,50,'#28323D','#28323D',0)
   else:
    # Unique real 4x4 ArUco codes, including their one-cell black border.
    s+=rect(col*50+10,row*50+10,30,30,'#14202B','#14202B',0)
    marker_id=(row*6+col)//2
    marker=cv2.aruco.generateImageMarker(cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50),marker_id,6)
    for i in range(6):
     for j in range(6):
      if marker[i,j]>0:s+=rect(col*50+10+j*5,row*50+10+i*5,5,5,'white','none',0)
 s+='<rect x="-7" y="-20" width="30" height="10" rx="2" fill="#E98B1D"/>'
 s+='<circle cx="50" cy="50" r="9" fill="#E98B1D" stroke="white" stroke-width="3"/>'
 if label:s+=text(62,40,'A',26,O,800)
 return s+'</g>'
def grid(x,y,w=165,h=125,bent=False):
 out=rect(x,y,w,h,'#F6F9FC',L,5)
 for i in range(1,6):
  xx=x+w*i/6
  out+=f'<path d="M{xx},{y} Q{xx+(22 if bent else 0)},{y+h/2} {xx},{y+h}" fill="none" stroke="#71879D" stroke-width="2"/>'
 for i in range(1,5):
  yy=y+h*i/5
  out+=f'<path d="M{x},{yy} Q{x+w/2},{yy+(18 if bent else 0)} {x+w},{yy}" fill="none" stroke="#71879D" stroke-width="2"/>'
 return out
def panel1(w,h):
 s=text(25,52,'已知板上位置',36,N,800)
 sc=min((w-100)/300,1.15)
 s+=board((w-300*sc)/2,115,sc)
 yy=115+270*sc
 s+=text(25,yy+40,'A是棋盤交點，不是標記中心',26,N,700)
 s+=text(25,yy+100,'固定身份 A，位置由標靶定義',28,O,700)
 s+=text(25,h-29,'製作標靶時仍須核對實體尺寸',25,'#5D7184',600)
 return s
def panel2(w,h):
 s=text(25,52,'同一角點，跨視角找回',36,N,800)
 if w<560:
  spots=[(65,120,.54,0,0),(245,165,.54,-12,12),(150,340,.65,10,-12)]
 else:spots=[(65,125,.64,0,0),(380,160,.64,-12,12),(230,325,.60,10,-12)]
 for i,(x,y,sc,sk,ro) in enumerate(spots):
  s+=board(x,y,sc,sk,ro)
  s+=text(x,y-25,'視角 '+str(i+1),25,N,600)
 s+=text(25,h-101,'橘色A始終是同一板上交點',27,O,700)
 s+=text(25,h-64,'影像位置改變，實體身份不變',26)
 s+=text(25,h-29,'同一板座標轉換的視角示意',23,'#5D7184')
 return s
def panel3(w,h):
 s=text(25,52,'估相機參數，再核對',36,N,800)
 s+=text(25,107,'多視角對應 → 內參＋畸變',29,B,700)
 ww=(w-105)/2
 s+=grid(25,140,ww,125,True)+arrow(35+ww,202,65+ww,202)+grid(80+ww,140,ww,125,False)
 s+=text(25,300,'模型解釋像素如何投影',27)
 # Reprojection evidence uses same known-corner coordinate, observed vs predicted.
 s+=rect(25,335,w-50,140,'#F5F9FF',L,14)
 s+=line(55,370,155,370,'#64788B',3)+line(104,346,104,441,'#64788B',3)
 s+='<circle cx="104" cy="370" r="9" fill="#E98B1D"/><circle cx="130" cy="388" r="11" fill="none" stroke="#1765CA" stroke-width="4"/>'
 s+=line(108,374,123,383,N,2)
 s+=text(184,380,'● 觀測角點',26,O,700)+text(184,424,'○ 重投影位置',26,B,700)
 s+=text(25,515,'獨立視角查偏差，再決定補拍',26,N,700)
 s+=text(25,h-70,'單張姿態是另一個問題：',25)
 s+=text(25,h-31,'已知內參＋角點 → R/t',27,B,700)
 return s
def make(mobile):
 width,height=(768,2304) if mobile else (1672,941)
 head=174 if mobile else 150; bottom=180 if mobile else 130
 s=f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}"><style>text{{font-family:"Microsoft JhengHei","Noto Sans CJK TC",sans-serif}}</style>'
 s+=rect(0,0,width,height,'#FFFFFF','none',0)
 if mobile:s+=text(32,64,'ChArUco：用已知角點',48,N,800)+text(32,121,'建立相機幾何',48,N,800)
 else:s+=text(40,69,'ChArUco：用已知角點，建立相機幾何',54,N,800)
 s+=text(33,head-23,'相機校正｜受控幾何示意' if mobile else '多視角相機校正｜不是逐件對位｜受控幾何示意',26,'#5D7184',600)
 if mobile:
  pw=720; ph=640; positions=[(24,head+i*655) for i in range(3)]
 else:pw=510; ph=640; positions=[(24+i*557,head) for i in range(3)]
 for (x,y),fn in zip(positions,[panel1,panel2,panel3]):
  s+=rect(x,y,pw,ph,'#F8FBFF',L,20)+f'<g transform="translate({x},{y})">'+fn(pw,ph)+'</g>'
 if not mobile:
  for x,y in positions[:2]:s+=arrow(x+pw+5,y+305,x+552,y+305)
 by=height-bottom+12
 s+=rect(24,by,width-48,bottom-36,'#FFF4CC','#E9B54A',18)
 s+=text(49,by+53,'💡',38,O)
 if mobile:s+=text(107,by+51,'已知角點跨視角對應，',32,N,800)+text(107,by+99,'才能建立可核對的相機幾何。',32,N,800)
 else:s+=text(112,by+59,'已知角點跨視角對應，才能建立可核對的相機幾何。',39,N,800)
 if mobile:s=re.sub(r'font-size="(2[3-9])"', 'font-size="32"',s)
 return s+'</svg>',width,height
async def main():
 async with async_playwright() as p:
  b=await p.chromium.launch(channel='msedge',headless=True)
  for mode in ['desktop','mobile']:
   svg,w,h=make(mode=='mobile'); path=W/f'charuco-core-r05-{mode}.svg';path.write_text(svg,encoding='utf-8')
   page=await b.new_page(viewport={'width':w,'height':h},device_scale_factor=1)
   await page.goto(path.as_uri());await page.screenshot(path=str(path.with_suffix('.png')));await page.close()
  await b.close()
 print('Rendered new exact-geometry SVG/PNG prototype; requires actual review')
if __name__=='__main__':asyncio.run(main())
